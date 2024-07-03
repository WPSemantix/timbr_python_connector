# use for pip installation
import pytimbr as timbr

# use for repository installation
import pytimbr.timbr_connector as timbr

if __name__ == '__main__':
  # Initiate a connection object

  # General example
  conn = timbr.getConnection(
    hostname = '<TIMBR_IP/HOST>',
    port = '<TIMBR_PORT>',
    ontology = '<ONTOLOGY_NAME>',
    username = '<TIMBR_USER>',
    password = '<TIMBR_PASSWORD>',
    enabled_ssl = '<false/true>',
    http_path = '<TIMBR_SERVER_HTTP_PATH>'
  )
  
  # hostname - The IP / Hostname of the Timbr server (not necessarily the hostname of the Timbr platform).
  # port - Timbr's default port with enabled_ssl is 443 without SSL is 11000
  # ontology - the ontology / knowledge graph to connect to.
  # username - Use 'token' as the username when connecting using a Timbr token, otherwise its the user name.
  # password - Should be the token value if using a token as a username, otherwise its the user's password.
  # enabled_ssl - true if SSL is enabled, false if SSL is disabled.
  # http_path - Use only if your timbr server http path is not '/timbr-server'
  
  # HTTP example
  conn = timbr.getConnection(
    hostname = 'mytimbrenv.com',
    port = '11000',
    ontology = 'my_ontology',
    username = 'timbr',
    password = 'StrongPassword',
    enabled_ssl = 'false',
    http_path = '/timbr-server'
  )

  # HTTPS example
  conn = timbr.getConnection(
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
    # Print the results
    for concept in concepts:
      print(concept)
