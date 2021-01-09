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

  airflow initdb



'''