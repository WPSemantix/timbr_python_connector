import pandas as pd
# use for pip installation
import timbr_python_connector as timbr

# use for repository installation
import timbr_python_connector.timbr_connector as timbr

if __name__ == '__main__':    
    username = '<TIMBR_USER>' # Use 'token' as the username when connecting using a Timbr token, otherwise its the user name.
    userpass = '<TIMBR_PASSWORD>' # Should be then token value if using a token as a username, otherwise its the user's password
    hostname = '<TIMBR_IP/HOST>' # The IP / Hostname of the Timbr server (not necessarily the hostname of the Timbr platform)
    port = '<TIMBR_PORT>' # Timbr default port 11000
    ontology = '<ONTOLOGY_NAME>' 
    enabled_ssl = 'false' # Change to true if SSL is enabled

    conn = timbr.getConnection(f"jdbc:hive2://{hostname}:{port}/{ontology};transportMode=http;ssl={enabled_ssl};httpPath=/timbr-server", username, userpass)
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