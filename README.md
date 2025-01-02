![Timbr logo](https://timbr.ai/wp-content/uploads/2023/06/timbr-ai-l-5-226x60-1.png)

[![FOSSA Status](https://app.fossa.com/api/projects/custom%2B50508%2Fgithub.com%2FWPSemantix%2Ftimbr_python_connector.svg?type=shield&issueType=license)](https://app.fossa.com/projects/custom%2B50508%2Fgithub.com%2FWPSemantix%2Ftimbr_python_connector?ref=badge_shield&issueType=license)
[![FOSSA Status](https://app.fossa.com/api/projects/custom%2B50508%2Fgithub.com%2FWPSemantix%2Ftimbr_python_connector.svg?type=shield&issueType=security)](https://app.fossa.com/projects/custom%2B50508%2Fgithub.com%2FWPSemantix%2Ftimbr_python_connector?ref=badge_shield&issueType=security)

[![Python 3.7.13](https://img.shields.io/badge/python-3.7.13+-blue.svg)](https://www.python.org/downloads/release/python-3713/)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-3820/)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-3921/)

[![Java 11](https://img.shields.io/badge/Java-11-red.svg)](https://www.oracle.com/il-en/java/technologies/javase/jdk11-archive-downloads.html)
[![Java 17](https://img.shields.io/badge/Java-17-red.svg)](https://www.oracle.com/il-en/java/technologies/javase/jdk17-archive-downloads.html)
[![Java 21](https://img.shields.io/badge/Java-21-red.svg)](https://www.oracle.com/il-en/java/technologies/javase/jdk21-archive-downloads.html)

[![PypiVersion](https://img.shields.io/pypi/v/pytimbr.svg)](https://badge.fury.io/py/pytimbr)

# timbr Python connector using JDBC
This project is a python connector to timbr using JDBC.

## Dependencies
- Python 3.7.13+ or 3.8.x or 3.9.x
- Java 11 or Java 17 or Java 21

## Installation
- Install as clone repository:
  - Install Python: https://www.python.org/downloads/release/python-3713/
  - Install Java: https://www.oracle.com/il-en/java/technologies/javase/jdk11-archive-downloads.html
  - Run the following command to install the Python dependencies: `pip install -r requirements.txt`  (optional install pandas to run pandas example)
  - Download the following jar to `jars` path: https://repo1.maven.org/maven2/org/apache/hive/hive-jdbc/4.0.1/hive-jdbc-4.0.1-standalone.jar

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

## Connection parameters examples

### Parameters for Basic function

#### Generic example and explanation for each parameter
```python
  hostname = '<TIMBR_IP/HOST>'
  port = '<TIMBR_PORT>'
  ontology = '<ONTOLOGY_NAME>'
  username = '<token/TIMBR_USER>'
  password = '<TOKEN_VALUE/TIMBR_PASSWORD>'
  enabled_ssl = '<false/true>'
  http_path = '<TIMBR_SERVER_HTTP_PATH>'
  
  # hostname    - Required  - String  - The IP / Hostname of the Timbr server (not necessarily the hostname of the Timbr platform).
  # port        - Required  - String  - The port to connect to in the Timbr server. Timbr's default port with enabled_ssl is 443 without SSL is 11000.
  # ontology    - Required  - String  - the ontology / knowledge graph to connect to.
  # username    - Required  - String  - Use 'token' as the username when connecting using a Timbr token, otherwise its the user name.
  # password    - Required  - String  - Should be the token value if using a token as a username, otherwise its the user's password.
  # enabled_ssl - Optional  - String  - 'true' if SSL is enabled, 'false' if SSL is disabled. The default value is 'true'.
  # http_path   - Optional  - String  - Use only if your timbr server http path is not '/timbr-server'. The default value is '/timbr-server'.
```

#### HTTP example
```python
  hostname = 'mytimbrenv.com'
  port = '11000'
  ontology = 'my_ontology'
  username = 'timbr'
  password = 'StrongPassword'
  enabled_ssl = 'false'
  http_path = '/timbr-server'
```

#### HTTPS example
```python
  hostname = 'mytimbrenv.com'
  port = '443'
  ontology = 'my_ontology'
  username = 'timbr'
  password = 'StrongPassword'
  enabled_ssl = 'true'
  http_path = '/timbr-server'
```

### Parameters for JDBC function

#### Generic example and explanation for each parameter
```python
  jdbc_url = '<TIMBR_JDBC_CONNECTION_URL>'
  username = '<token/TIMBR_USER>'
  password = '<TOKEN_VALUE/TIMBR_PASSWORD>'

  # jdbc_url  - Required  - String  - The JDBC connection url.
  # username  - Required  - String  - Use 'token' as the username when connecting using a Timbr token, otherwise its the user name.
  # password  - Required  - String  - Should be the token value if using a token as a username, otherwise its the user's password.
```

#### HTTP example
```python
  jdbc_url = 'jdbc:hive2://mytimbrenv.com:11000/my_ontology;transportMode=http;ssl=false;httpPath=/timbr-server'
  username = 'timbr'
  password = 'StrongPassword'
```

#### HTTPS example
```python
  jdbc_url = 'jdbc:hive2://mytimbrenv.com:443/my_ontology;transportMode=http;ssl=true;httpPath=/timbr-server'
  username = 'timbr'
  password = 'StrongPassword'
```

## Create new connection 

### Create connection using basic function

#### Generic example
```python
  conn = pytimbr.get_connection(
    hostname,
    port,
    ontology,
    username,
    password,
    enabled_ssl,
    http_path
  )
```

#### HTTP example
```python
  conn = pytimbr.get_connection(
    'mytimbrenv.com',
    '11000',
    'my_ontology',
    'timbr',
    'StrongPassword',
    'false',
    '/timbr-server'
  )
```

#### HTTPS example
```python
  hostname = 'mytimbrenv.com'
  port = '443'
  ontology = 'my_ontology'
  username = 'timbr'
  password = 'StrongPassword'
  enabled_ssl = 'true'
  http_path = '/timbr-server'
```

### Create connection using JDBC function

#### Generic example
```python
  conn = pytimbr.get_jdbc_connection(
    jdbc_url,
    username,
    password
  )
```

#### HTTP example
```python
  conn = pytimbr.get_jdbc_connection(
    "jdbc:hive2://mytimbrenv.com:11000/my_ontology;transportMode=http;ssl=false;httpPath=/timbr-server",
    'timbr',
    'StrongPassword'
  )
```

#### HTTPS example
```python
  conn = pytimbr.get_jdbc_connection(
    "jdbc:hive2://mytimbrenv.com:443/my_ontology;transportMode=http;ssl=true;httpPath=/timbr-server",
    'timbr',
    'StrongPassword'
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

    # Print returned object headers
    # Option 1 - Recommended
    for i in range(1, curs._meta.getColumnCount() + 1):
      print(curs._meta.getColumnName(i) + " - " + curs._meta.getColumnTypeName(i))

    # Option 2- DBAPI
    for col in curs.description:
      print(col[0] + " - " + col[1].values[0])

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
