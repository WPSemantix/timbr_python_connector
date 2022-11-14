import timbr_connector as timbr

def exportOntology(cursor, path):
    cursor.execute('export ontology owl')
    # Fetch results
    rows = cursor.fetchall()
    # Save the results
    
    with open(path, "w") as outputFile:
        for row in rows:
            outputFile.write(row[0] + "\n")

def exportConcept(cursor, path, concept):
    cursor.execute('export rdf concept ' + concept)
    # Fetch results
    rows = cursor.fetchall()
    # Save the results
    with open(path, "w") as outputFile:
        for row in rows:
            outputFile.write(row[0] + "\n")

def exportRelationship(cursor, path, relationship):
    cursor.execute('export rdf relationship ' + relationship)
    # Fetch results
    rows = cursor.fetchall()
    # Save the results
    with open(path, "w") as outputFile:
        for row in rows:
            outputFile.write(row[0] + "\n")

if __name__ == '__main__':
    # username - Use 'token' as the username when connecting using a Timbr token, otherwise its the user name.
    username = 'token'
    # userpass - Should be the token value if using a token as a username, otherwise its the user's password.
    userpass = ''
    # hostname - The IP / Hostname of the Timbr server (not necessarily the hostname of the Timbr platform).
    hostname = ''
    # port - Timbr default port 11000
    port = '11000'
    # ontology - the ontology / knowledge graph to connect to.
    ontology = ''
    # enabled_ssl - Change to true if SSL is enabled.
    enabled_ssl = 'false'

    # Initiate a connection object
    conn = timbr.getConnection(f"jdbc:hive2://{hostname}:{port}/{ontology};transportMode=http;ssl={enabled_ssl};httpPath=/timbr-server", username, userpass)
    
    # Export ontology, concept and relationships
    path = ""
    concept = ""
    relationship = ""
    with conn.cursor() as cursor:
        exportOntology(cursor, path + "ontology_" + ontology + ".ttl")
        exportConcept(cursor, path + "concept_" + concept + ".ttl", concept)
        exportRelationship(cursor, path + "relationship" + relationship + ".ttl", relationship)

