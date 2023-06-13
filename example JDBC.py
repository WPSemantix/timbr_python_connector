# use for pip installation
import PyTimbr as timbr

# use for repository installation
import PyTimbr.timbr_connector as timbr

if __name__ == '__main__':
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

  # Initiate a connection object
  conn = timbr.getJdbcConnection(f"jdbc:hive2://{hostname}:{port}/{ontology};transportMode=http;ssl={enabled_ssl};httpPath=/timbr-server", username, userpass)

  # Use the connection to execute a query
  with conn.cursor() as curs:
    # Execute query
    curs.execute('SHOW CONCEPTS')
    # Fetch results
    concepts = curs.fetchall()
    # Print the results
    for concept in concepts:
      print(concept)
