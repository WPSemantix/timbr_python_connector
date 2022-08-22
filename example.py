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
