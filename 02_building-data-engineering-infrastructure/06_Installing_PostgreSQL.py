''' 
- PostgreSQL is an open source relational database; It compares to Oracle or 
  Microsoft SQL Server. PostgreSQL also has a plugin - postGIS - which allows
  spacial capabilities in PostgreSQL. Now we will choose it as our own
  relational database, and it can be installed on Linux as package:

1. For a Debian-based system, we will use apt-get:

    sudo apt-get install postgresql-11

    my own version: 
    sudo apt install postgresql postgresql-contrib

2. check status

    sudo systemctl status postgresql

3. to add a password

    sudo -u postgres psql

4. to create a database

    sudo -u postgres createdb dataengineeringwithpython

- Using the command line is fast, but sometimes a GUI makes life easier. 
  PostgreSQL has an administration tool - pgAdmin 4;


'''