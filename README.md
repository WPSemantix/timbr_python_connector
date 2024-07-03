![Timbr logo](https://timbr.ai/wp-content/uploads/2023/06/timbr-ai-l-5-226x60-1.png)

# timbr Python connector sample file
This project is a sample connecting to timbr using Python.

## Dependencies
- Python 3.7.13+ or 3.8.x or 3.9.x
- Java 8 or Java 11

## Installation
- Install as clone repository:
  - Install Python: https://www.python.org/downloads/release/python-3713/
  - Install Java: https://www.oracle.com/il-en/java/technologies/javase/jdk11-archive-downloads.html
  - Run the following command to install the Python dependencies: `pip install -r requirements.txt`  (optional install pandas to run pandas example)
  - Download the following jar to `jars` path: https://repo1.maven.org/maven2/org/apache/hive/hive-jdbc/2.3.9/hive-jdbc-2.3.9-standalone.jar

- Install using pip and git:
  - `pip install git+https://github.com/WPSemantix/timbr_python_connector`

- Install using pip:
  - `pip install pytimbr`

## Sample usage
- For an example of how to use the Python connector for Timbr:
  - Create connection with params, follow this [Example file](examples/example.py) 
  - Create JDBC connection, follow this [Example file](examples/example_JDBC.py) 
- For an example of using the Timbr Python connector with Pandas:
  - Make sure you have the pandas library installed, or you can install it by running `pip install pandas`
  - Create connection with params, follow this [Example File](examples/pandas_example.py)
  - Create JDBC connection, follow this [Example File](examples/pandas_example_JDBC.py)

## Create basic connection 

### Create connection with params
```python
  conn = pytimbr.getConnection(
    hostname = '<TIMBR_IP/HOST>',
    port = '<TIMBR_PORT>',
    ontology = '<ONTOLOGY_NAME>',
    username = '<TIMBR_USER/token>',
    password = '<TIMBR_PASSWORD/TOKEN_VALUE>',
    enabled_ssl = '<false/true>',
    http_path = '<TIMBR_SERVER_HTTP_PATH>'
  )

  # hostname - The IP / Hostname of the Timbr server (not necessarily the hostname of the Timbr platform).
  # port - The port to connect to in the Timbr server. Timbr's default port with enabled_ssl is 443 without SSL is 11000.
  # ontology - the ontology / knowledge graph to connect to.
  # username - Use 'token' as the username when connecting using a Timbr token, otherwise its the user name.
  # password - Should be the token value if using a token as a username, otherwise its the user's password.
  # enabled_ssl - true if SSL is enabled, false if SSL is disabled.
  # http_path - Use only if your timbr server http path is not '/timbr-server'.
```

### Create JDBC connection
```python
  hostname = '<TIMBR_IP/HOST>'
  port = '<TIMBR_PORT>'
  ontology = '<ONTOLOGY_NAME>'
  username = '<TIMBR_USER/token>'
  password = '<TIMBR_PASSWORD/TOKEN_VALUE>'
  enabled_ssl = '<false/true>'
  http_path = '<TIMBR_SERVER_HTTP_PATH>'
  
  # hostname - The IP / Hostname of the Timbr server (not necessarily the hostname of the Timbr platform).
  # port - The port to connect to in the Timbr server. Timbr's default port with enabled_ssl is 443 without SSL is 11000.
  # ontology - the ontology / knowledge graph to connect to.
  # username - Use 'token' as the username when connecting using a Timbr token, otherwise its the user name.
  # password - Should be the token value if using a token as a username, otherwise its the user's password.
  # enabled_ssl - true if SSL is enabled, false if SSL is disabled.
  # http_path - Use only if your timbr server http path is not '/timbr-server'.
  
  # Create new JDBC connection
  conn = pytimbr.getJdbcConnection(
    f"jdbc:hive2://{hostname}:{port}/{ontology};transportMode=http;ssl={enabled_ssl};httpPath={http_path}",
    username,
    password
  )
```

## Execute a query

### Execute using the connection
```python
  # Use the connection to execute a query
  with conn.cursor() as curs:
    # Execute query
    curs.execute('SHOW CONCEPTS')
    # Fetch results
    concepts = curs.fetchall()
    # Print the results
    for concept in concepts:
      print(concept)
```

### Execute using the Pandas
```python
  # Execute a query using Pandas
  df = pandas.read_sql("SELECT * FROM timbr.person limit 1000", conn)
  print("--------------------------------------")
  print(df)
  print("--------------------------------------")
  print(df.columns)
  print("--------------------------------------")
  print(df.count())
```