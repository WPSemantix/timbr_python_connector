import pandas as pd
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

  # Execute a query using Pandas
  df = pd.read_sql("SELECT * FROM timbr.person limit 1000", conn)
  print("--------------------------------------")
  print(df)
  print("--------------------------------------")
  print(df.columns)
  print("--------------------------------------")
  print(df.count())