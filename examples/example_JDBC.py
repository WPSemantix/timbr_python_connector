# use for pip installation
import pytimbr as timbr

# use for repository installation
import pytimbr.timbr_connector as timbr

if __name__ == '__main__':

  # Initiate a connection object
  # Generic example
  conn = timbr.get_jdbc_connection(
    jdbc_url = '<TIMBR_JDBC_CONNECTION_URL>',
    username = '<token/TIMBR_USER>',
    password = '<TOKEN_VALUE/TIMBR_PASSWORD>'
  )

  # jdbc_url  - Required  - String  - The JDBC connection url.
  # username  - Required  - String  - Use 'token' as the username when connecting using a Timbr token, otherwise its the user name.
  # password  - Required  - String  - Should be the token value if using a token as a username, otherwise its the user's password.

  # HTTP example
  conn = timbr.get_jdbc_connection(
    "jdbc:hive2://mytimbrenv.com:11000/my_ontology;transportMode=http;ssl=false;httpPath=/timbr-server",
    'timbr',
    'StrongPassword'
  )

  # HTTPS example
  conn = timbr.get_jdbc_connection(
    "jdbc:hive2://mytimbrenv.com:443/my_ontology;transportMode=http;ssl=true;httpPath=/timbr-server",
    'timbr',
    'StrongPassword'
  )

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
