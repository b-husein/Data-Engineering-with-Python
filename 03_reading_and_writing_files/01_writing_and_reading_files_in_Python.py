''' 
- One of the most basic tasks in data engineering is moving data from a text file to a database.
  Now we will focus on reading data from and writing data to a several different text-based
  formats such as CSV and JSON.

- In this chapter we're going to cover the following main topics:
    - Reading and writing files in Python
    - Processing files in Airflow
    - NiFi processors for handling files
    - Reading and writing data to databases in Python
    - Databases in Airflow
    - Database processors in NiFi
'''

''' 
- WRITING AND READING FILES IN PYTHON

- In this section we will write data to files first, then read it. The goal of writing is to
  actually understand the structure of the data and we will know what it is that we are trying
  to read.

- To write data, we will use a library named 'FAKER' that allows us to easily create fake data
  for common fields. We can generate an address by simply calling address(), or a female name
  using name_female(). This will simplify the creation of fake data, while at the same time
  making it more realistic.

- To install faker, we can use pip:

    pip3 install faker

With faker now installed, we are ready to start writing files. The next section will start with CSV files.
'''

''' 
- WRITING AND READING CSVs

- The most common file type you will encounter is Comma-Separated Values (CSV). A CSV is a file made up of
  fields separated by commas. The Python standard library for andling CSVs simplifies the process of handling
  CSV data.



'''