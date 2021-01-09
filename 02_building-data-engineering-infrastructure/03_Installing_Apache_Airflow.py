''' 
- Apache Airflow performs the same role as Apache NiFi, however it allows
  you to create your data flows using pure Python. It is currently one of 
  the most popular open source data pipeline tools. What it lacks in polished
  GUI - compared to NiFi - it more than makes up for in the power and freedom
  to create tasks.

- Installing Apache Airflow can be done using 'pip'. But before installing 
  Apache Airflow, you can change the location of the Airflow install by 
  exporting AIRFLOW_HOME. If you want Airflow to install to opt/airflow
  export the AIRFLOW_HOME variable as shown:

  in terminal:

  export AIRFLOW_HOME=/opt/airflow

- The default location for Airflow is ~/airflow. The next consideration before 
  installing Airflow is to determine which sub-packages you want to install. 
  If you do not specify any, Airflow installs only what it needs to run.

- If you know that you will work with PostgreSQL, then you should install the
  sub-package by running the following:

  apache-airflow[postgres]

- to install Apache Airflow, with the options for postgreSQL, slack and celery,
  use the following command:

  pip3 install 'apache-airflow[postgres, slack, celery]'

- To run Airflow we need to initialize database using the following command:

  airflow db init #updated (january 9th 2021)

- The default database for Airflow is SQLite. This is good enough for testing and 
  running on a signle machine, but to run in production and in clusters, you will
  need to change the database to something else, such as PostgreSQL;

- In the case of 'no command airflow' in terminal, we need to add it to our path:

  export PATH=$PATH:/home/<username>/.local/bin

- The Airflow web server runs on port 8080, the same port as Apache NiFi. We
  already changed the NiFi port to 9300 in the nifi.properties file, so we can
  start the Airflow web server using the following command:

  airflow webserver

  Airflow documentation for a reference:
  https://airflow.apache.org/docs/apache-airflow/stable/start.html

- Open web browser and use credentials to login. We can create credentials by using 
  airflow users create command from documentation

- Next, start the Airflow scheduler so that you can run your data flows as set 
  intervals. Run this command in a different terminal so that you do not kill the web server:

  airflow scheduler

- When the scheduler runs, we have the warning in terminal about parallelism being set to 1
  because of the use of SQLite. We can ignore this warning for now, but later, you will want
  to be able to run more than one task at a time. 

- With the database initialized, the web server running, and the scheduler running, you can
  now browse to http://localhost:8080 and see the Airflow GUI. Airflow installs several example
  data flows (Directed Acyclic Graphs (DAGs)) during install. We can see them in our browser on
  the main screen.

- The examples are great for learning how to use Airflow GUI, but they will be cluttered later.
  It will be easier to find the tasks we created without all of these extra examples. 
  We can remove the examples by editing the airflow.cfg file; by changing load_examples from 
  True to False:

  load_examples = False

- After that we need to shutdown the web server. (Ctrl + C) Once the web server has stopped
  the changes to the configuration need to be loaded into the database by reseting it:

  airflow db reset (updated command January 2021)

- This will load in the changes from airflow.cfg to the metadata database. Now we will restart
  the web server:

  airflow webserver

- And when we open the localhost:8080 there shouldn't be any examples left. Now Airflow is clean
  and ready to load in the DAGs we will create in the future.

'''