''' 
- Later we will install PostgreSQL, but in order to connect to a PostgreSQL database
  using NiFi ExecuteSQL processor, we need a connecting pool, and that requires
  JDBC (Java Database Connectivity) driver for the database you will be connecting to.

  To download driver we will go to:
  https://jdbc.postgresql.org/download.html 
  and download the PostgreSQL JDBC 4.2 driver;

  Then make a new folder in your NiFi installation directory named 'drivers'. Move
  the postgresql-42.2.10.jar file into the folder. You will later reference this jar
  file in your NiFi processor.


'''