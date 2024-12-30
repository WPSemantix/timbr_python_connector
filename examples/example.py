# use for pip installation
import pytimbr as timbr

# use for repository installation
import pytimbr.timbr_connector as timbr

if __name__ == '__main__':

  # Initiate a connection object
  # Generic example
  conn = timbr.get_connection(
    hostname = '<TIMBR_IP/HOST>',
    port = '<TIMBR_PORT>',
    ontology = '<ONTOLOGY_NAME>',
    username = '<token/TIMBR_USER>',
    password = '<TOKEN_VALUE/TIMBR_PASSWORD>',
    enabled_ssl = '<false/true>',
    http_path = '<TIMBR_SERVER_HTTP_PATH>'
  )

  # hostname    - Required  - String  - The IP / Hostname of the Timbr server (not necessarily the hostname of the Timbr platform).
  # port        - Required  - String  - The port to connect to in the Timbr server. Timbr's default port with enabled_ssl is 443 without SSL is 11000.
  # ontology    - Required  - String  - the ontology / knowledge graph to connect to.
  # username    - Required  - String  - Use 'token' as the username when connecting using a Timbr token, otherwise its the user name.
  # password    - Required  - String  - Should be the token value if using a token as a username, otherwise its the user's password.
  # enabled_ssl - Optional  - String  - 'true' if SSL is enabled, 'false' if SSL is disabled. The default value is 'true'.
  # http_path   - Optional  - String  - Use only if your timbr server http path is not '/timbr-server'. The default value is '/timbr-server'.

  # HTTP example
  conn = timbr.get_connection(
    hostname = 'mytimbrenv.com',
    port = '11000',
    ontology = 'my_ontology',
    username = 'timbr',
    password = 'StrongPassword',
    enabled_ssl = 'false',
    http_path = '/timbr-server'
  )

  # HTTPS example
  conn = timbr.get_connection(
    hostname = 'mytimbrenv.com',
    port = '443',
    ontology = 'my_ontology',
    username = 'timbr',
    password = 'StrongPassword',
    enabled_ssl = 'true',
    http_path = '/timbr-server'
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
