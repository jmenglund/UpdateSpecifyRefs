UpdateSpecifyRefs
=================

Command-line utility for updating record references in a Specify database.
The program outputs the number of affected records for each foreign key
that is being updated.

The code is written in Python and should work with both
Python 2 and 3.

--------------------------------

.. contents:: Table of contents
   :depth: 2
   :backlinks: none
   :local:


Prerequisites
-------------

You need to have a `MySQL <https://www.mysql.com>`_  and a 
`Specify <http://specifysoftware.org>`_ installed. The code make use of
the Python packages `PyMySQL <https://github.com/PyMySQL/PyMySQL>`_ 
and `CountRecordRefs <https://github.com/CountRecordRefs>`_. If you follow 
the instructions below, the requred Python packages will be installed
automatically for you.


Installation
------------

The project is hosted at https://github.com/jmenglund/UpdateSpecifyRefs
and can be installed using git:

.. code-block::

    $ git clone https://github.com/jmenglund/UpdateSpecifyRefs.git
    $ cd UpdateSpecifyRefs
    $ python setup.py install

You may consider installing ``UpdateSpecifyRefs`` within a virtual 
environment in order to avoid cluttering your system's Python path. 
See for example the environment management system  
`conda <http://conda.pydata.org>`_ or the package 
`virtualenv <https://virtualenv.pypa.io/en/latest/>`_.

This project is centered around a self-contained single-module
(single-file) executable script that can also be used as such.


Usage
-----

.. code-block::

    $ UpdateSpecifyRefs.py --help
    usage: UpdateSpecifyRefs.py [-h] [-V] [--user USER] [--password PASSWORD]
                                [--host HOST] [-z]
                                database_name agent_id table_name old_id new_id
    
    Command-line utility that updates all the references that point to a record in
    a Specify database. Information about updates is written to <stdout>.
    
    positional arguments:
      database_name        MySQL database name
      agent_id             AgentID for the user that makes the changes to the
                           database.
      table_name           table name
      old_id               primary key value to be replaced
      new_id               primary key value to be inserted
    
    optional arguments:
      -h, --help           show this help message and exit
      -V, --version        show program's version number and exit
      --user USER          MySQL user (default: "root")
      --password PASSWORD  MySQL password
      --host HOST          database host (default: "localhost")
      -z, --zero-counts    include counts of zero in output


License
-------

``UpdateSpecifyRefs`` is distributed under the 
`GNU General Public License, version 3 (GPL-3.0) <https://opensource.org/licenses/GPL-3.0>`_.


Author
------

Markus Englund, `orcid.org/0000-0003-1688-7112 <http://orcid.org/0000-0003-1688-7112>`_

.. |License| image:: https://img.shields.io/badge/license-GNU%20GPL%20version%203-blue.svg
   :target: https://raw.githubusercontent.com/jmenglund/UpdateSpecifyRefs/master/LICENSE.txt
