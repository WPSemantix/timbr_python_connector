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
- For an example of how to use the Python connector for Timbr, follow this [Example file](example.py) 
- For an example of using the Timbr Python connector with Pandas:
  - Make sure you have the pandas library installed, or you can install it by running `pip install pandas`
  - Follow this [Pandas Example File](pandas_example.py)

## Create basic connection 

### Create JDBC connection
```python
  # username - Use 'token' as the username when connecting using a Timbr token, otherwise its the user name.
  username = '<TIMBR_USER>'
  # userpass - Should be the token value if using a token as a username, otherwise its the user's password.
  userpass = '<TIMBR_PASSWORD>'
  # hostname - The IP / Hostname of the Timbr server (not necessarily the hostname of the Timbr platform).
  hostname = '<TIMBR_IP/HOST>'
  # port - Timbr default port 11000
  port = '<TIMBR_PORT>'
  # ontology - the ontology / knowledge graph to connect to.
  ontology = '<ONTOLOGY_NAME>'
  # enabled_ssl - Change to true if SSL is enabled.
  enabled_ssl = 'false'
  
  # Create new JDBC connection
  conn = pytimbr.getJdbcConnection(f"jdbc:hive2://{hostname}:{port}/{ontology};transportMode=http;ssl={enabled_ssl};httpPath=/timbr-server", username, userpass)

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

### Create connection with params
```python
  # username - Use 'token' as the username when connecting using a Timbr token, otherwise its the user name.
  # userpass - Should be the token value if using a token as a username, otherwise its the user's password.
  # hostname - The IP / Hostname of the Timbr server (not necessarily the hostname of the Timbr platform).
  # port - Timbr default port 11000
  # ontology - the ontology / knowledge graph to connect to.
  # enabled_ssl - Change to true if SSL is enabled.
  conn = pytimbr.getConnection(hostname='<TIMBR_IP/HOST>', port='<TIMBR_PORT>', ontology='<ONTOLOGY_NAME>', username='<TIMBR_USER>', password='<TIMBR_PASSWORD>', enabled_ssl='false')

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
