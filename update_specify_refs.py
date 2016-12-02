#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Update all the references that point to a specific record
in a Specify database.
"""

import argparse
import getpass
import sys

import pymysql.cursors

from count_record_refs import get_related_columns


__author__ = 'Markus Englund'
__license__ = 'GNU GPLv3'
__version__ = '0.1.0'


def update_refs(
        user, host, password, db, related_columns,
        user_agentid, old_id, new_id, zero_counts=False):
    connection = pymysql.connect(
        host=host, user=user, password=password, db=db,
        cursorclass=pymysql.cursors.DictCursor)
    sys.stdout.write('table_name\tcolumn_name\tcount\n')
    try:
        with connection.cursor() as cursor:
            for row in related_columns:
                sql = """UPDATE {table_name}
                      SET
                          {column_name} = '{new_id}',
                          version = version + 1,
                          timestampmodified = now(),
                          modifiedbyagentid = {user_agentid}
                      WHERE {column_name} = '{old_id}'
                      """.format(
                          table_name=row['TABLE_NAME'],
                          column_name=row['COLUMN_NAME'],
                          user_agentid=user_agentid,
                          old_id=old_id,
                          new_id=new_id)
                cnt = cursor.execute(sql)
                if (zero_counts and cnt == 0) or cnt > 0:
                    sys.stdout.write(
                        row['TABLE_NAME'] + '\t' +
                        row['COLUMN_NAME'] + '\t' +
                        str(cnt) + '\n')
        connection.commit()  # make all changes within a single transaction
    finally:
        connection.close()


def parse_args(args):
    parser = argparse.ArgumentParser(
        description=(
            'Command-line utility that updates all the references '
            'that point to a record in a Specify database. '
            'Information about updates is written to <stdout>.'))
    parser.add_argument(
        '-V', '--version', action='version',
        version='update_specify_refs.py ' + __version__)
    parser.add_argument(
        '--user', type=str, action='store', default='root',
        dest='user', help='MySQL user (default: "root")')
    parser.add_argument(
        '--password', type=str, action='store', default=None,
        dest='password', help='MySQL password')
    parser.add_argument(
        '--host', type=str, action='store', default='localhost',
        dest='host', help='database host (default: "localhost")')
    parser.add_argument(
        '-z', '--zero-counts', action='store_true',
        dest='zero_counts', help='include counts of zero in output')
    parser.add_argument(
        'database_name', type=str, action='store', help='MySQL database name')
    parser.add_argument(
        'agent_id', type=str, action='store',
        help='AgentID for the user that makes the changes to the database.')
    parser.add_argument(
        'table_name', type=str, action='store',
        help='table name')
    parser.add_argument(
        'old_id', type=str, action='store',
        help='primary key value to be replaced')
    parser.add_argument(
        'new_id', type=str, action='store',
        help='primary key value to be inserted')
    return parser.parse_args(args)


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    parser = parse_args(args)

    if not parser.password:
        password = getpass.getpass('Password:')
    else:
        password = parser.password

    related_columns = get_related_columns(
        user=parser.user,
        host=parser.host,
        password=password,
        db=parser.database_name,
        table_name=parser.table_name)

    update_refs(
        user=parser.user,
        host=parser.host,
        password=password,
        db=parser.database_name,
        related_columns=related_columns,
        user_agentid=parser.agent_id,
        old_id=parser.old_id,
        new_id=parser.new_id,
        zero_counts=parser.zero_counts)


if __name__ == '__main__':
    main()
