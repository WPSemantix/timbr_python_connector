import pandas as pd
# use for pip installation
import pytimbr as timbr

# use for repository installation
import pytimbr.timbr_connector as timbr

if __name__ == '__main__':    
  # Initiate a connection object
  conn = timbr.getConnection(hostname='<TIMBR_IP/HOST>', port='<TIMBR_PORT>', ontology='<ONTOLOGY_NAME>', username='<TIMBR_USER>', password='<TIMBR_PASSWORD>', enabled_ssl='false')
  # username - Use 'token' as the username when connecting using a Timbr token, otherwise its the user name.
  # userpass - Should be the token value if using a token as a username, otherwise its the user's password.
  # hostname - The IP / Hostname of the Timbr server (not necessarily the hostname of the Timbr platform).
  # port - Timbr default port 11000
  # ontology - the ontology / knowledge graph to connect to.
  # enabled_ssl - Change to true if SSL is enabled.

  with conn.cursor() as curs:
    curs.execute('SHOW CONCEPTS')
    concepts = curs.fetchall()
    for concept in concepts:
      print(concept)

  # Change the query to a concept from your Knowledge Graph
  df = pd.read_sql("SELECT * FROM timbr.person limit 1000", conn)
  print("--------------------------------------")
  print(df)
  print("--------------------------------------")
  print(df.columns)
  print("--------------------------------------")
  print(df.count())