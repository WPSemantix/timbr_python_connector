import pandas as pd
import timbr_connector as timbr

if __name__ == '__main__':

    # timbr default port 11000
    # Use token as DB user when connecting using token and not using password
    # Change ssl=true if SSL is enabled
    conn = timbr.getConnection("jdbc:hive2://<TIMBR_IP/HOST>:<TIMBR_PORT>/<ONTOLOGY_NAME>;transportMode=http;ssl=false", "<TIMBR_USER>", "<TIMBR_PASSWORD>")

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