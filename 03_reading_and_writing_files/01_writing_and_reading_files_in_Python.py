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

- WRITING CSVs USING THE PYTHON CSV LIBRARY

- To write a CSV with the CSV library, we need to use following steps (in terminal):

    1. OPEN A FILE IN WRITING MODE. To open a file, we need to specify a filename and a mode. The mode for 
    writing is 'w', but we can also open a file for reading with 'r', appending with 'a' or reading and 
    writing with 'r+'. Lastly, if we are handling files that are not text, we can add 'b', for binary mode,
    to any of the preceding modes to write in bytes, for example, 'wb' will allow us to write in bytes:

    output = open('myCSV.CSV', mode='w')

    2. CREATE CSV_writter. At a minimum, we must specify a file to write to, but we can also pass additional
    parameters, such as a dialect. A dialect can be defined CSV type, such as Excel, or it can be options such
    as delimiter to use or the level of quoting. The defaults are usually what you will need, so we can create 
    a writer as shown:

    mywriter=csv.writer(output)

    3. INCLUDE A HEADER. You might be able to remember wat the fields are in your CSV, but it is best to include
    a header. Writing a header is the same as writing any other row: define the values, then you will use writerow()
    as shown:

    header=['name', 'age']
    mywriter.writerow(header)

    4. WRITE THE DATA TO A FILE. You can now write a data row by using writerow(0) and passing some data as shown.

    data=['Bob Smith', 40]
    mywriter.writerow(data)
    output.close()

    Now if you look in the directory, you will have a CSV file named myCSV.CSV;

- The previous example was very basic. However, if you're trying to write a lot of data, you would most likely want
  to loop through some condition or iterate through existing data. In the following example, we will use Faker to 
  generate 1000 records. (via terminal)

  from faker import Faker
  import csv
  output=open('data.CSV', 'w')
  fake=Faker()
  header=['name','age','street','city','state','zip','lng','lat']
  mywriter=csv.writer(output)
  mywriter.writerow(header)
  for r in range(1000):
      mywriter.writerow([fake.name(),fake.random_int(min=18,max=80,step=1),fake.street_address(),fake.city(),fake.state(),fake.zipcode(),fake.longitude(),fake.latitude()])
      output.close()
'''

''' 
- READING CSVs

- Reading a CSV is somewhat similar to writing one. The same steps are followed with slight modifications:

    1. OPEN A FILE USING 'with'. Using 'with' has some additional benefits. If you do not specify a mode,
    open defaults to read (r). After 'open', you will need to specify what to refer to the file as; in this
    case, you will open the data.CSV file and refer to it as f:

    with open('data.csv') as f:
    
    2. CREATE THE READER. Instead of just using reader(), you will use DictReader(). By using the dictionary
    reader, you will be able to call fields in the data by name instead of position. For example, instead of
    calling the first item in a row as row(0), you can now call it as row['name']. Just like the writer, the
    defaults are usually sufficient, and you will only need to specify a file to read. The following code opens
    data.CSV using the f variable name:

    myreader=CSV.DictReader(f)

    3. GRAB THE HEADERS by reading a single line with next():

    headers=next(myreader)

    4. Now we can iterate through the rest of the rows using the following:

    for row in myreader:

    5. At the end you can print the names using the following:

    print(row['name'])

'''
''' 
- READING AND WRITING CSVs USING PANDAS DATAFRAMES

- pandas DataFrames are powerful tool not only for reading and writing data but also for the querying 
  and manipulation of data. We can install it via:

  pip3 install pandas
  
- We can think of pandas DataFrame as an Excel sheet or table. You will have rows, columns and index.
  To load CSV data into a DataFrame, the following steps must be followed:

    1. import pandas (usually as pd)

    import pandas as pd

    2. then, read the file using read_csv() method which takes several optional parameters and one
    required parameter - the file or file-like buffer. The two optional parameters that maybe of 
    interest are 'header', which by default attepts to inder the headers. 

    If we set header=0, then you can use the 'names' parameter with an array of column names. If you
    have a large file and you just want to look at piece of it, you can use 'nrows' to specify the
    number of rows to spread, so 'nrows=100' it means it will only read 100 rows for the data. 

    In the following snippet, you will load the entire file using the defaults:

    df=pd.read_csv('data.CSV')

    3. Let's now look at the first 10 records by using the following:

    df.head(10)

- You can create a DataFrame in Python with the following steps:

    1. CREATE A DICTIONARY OF DATA. A dictionary is a data structure that stores data
    as a key:value pair. The value can be of any Python data type - for example, an array.
    Dictionaries have methods for finding keys(), values(), and items(). They also allow you
    to find the value of a key by using the key name in brackets - for example, dictionary['key']
    will return the value for that key:

    data={'Name' : ['Paul','Bob','Susan','Yolanda'],
    'Age' : [23, 45, 18, 21]}

    2. PASS THE DATA TO THE DATAFRAME:

    df=pd.DataFrame(data)

    3. THE COLUMNS ARE SPECIFIED AS THE KEYS IN THE DICTIONARY. Now that you have a DataFrame, you 
    can write the contents to a CSV using to_csv() method and passing a filename.

    In the example we did not set an index, which means the row names will be a number from 0 to n, 
    where n is length of the DataFrame. When you export to CSV, these values will be written to the 
    file, but the column name will be blank. So, in a case where you do not need the row names or 
    index to be written to the file, pass the index parameter to to_csv(), as shown:

    df.to_csv('fromdf.CSV', index=False)

    You will now have a CSV file with the contents of the DataFrame.
'''

''' 
- WRITING JSON WITH PYTHON

'''