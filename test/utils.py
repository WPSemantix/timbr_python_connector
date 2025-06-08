import pandas as pd

def get_connection_uri(hostname: str, port: int, ontology: str, enabled_ssl: str, http_path: str) -> str:
  """
  Constructs a connection URI for the Hive database using the provided parameters.
  
  :param hostname: The hostname of the Hive server.
  :param port: The port number on which the Hive server is listening.
  :param ontology: The ontology or database name.
  :param enabled_ssl: A flag indicating whether SSL is enabled (e.g., 'true' or 'false').
  :param http_path: The HTTP path for the Hive server.
  
  :return: A formatted connection URI string for Hive.
  """
  return f"jdbc:hive2://{hostname}:{port}/{ontology};transportMode=http;ssl={enabled_ssl};httpPath={http_path}"

def parse_and_print_results(connection):
  """
  Parses and prints the results from the database cursor.
  :param connection: The database connection object.
  """

  with connection.cursor() as curs:
    curs.execute('SHOW CONCEPTS')
    concepts = curs.fetchall()

    # Recommended
    for i in range(1, curs._meta.getColumnCount() + 1):
      print(curs._meta.getColumnName(i) + " - " + curs._meta.getColumnTypeName(i))

    # DBAPI
    for col in curs.description:
      print(col[0] + " - " + col[1].values[0])

    # Print the results
    for concept in concepts:
      print(concept)

    return dict(
      column_count=curs._meta.getColumnCount(),
      description=curs.description,
      concepts=concepts,
    )

def parse_and_print_results_using_pandas(connection):
  """
  Parses and prints the results from the database cursor using pandas.
  :param connection: The database connection object.
  """

  with connection.cursor() as curs:
    df = pd.read_sql('SHOW CONCEPTS', connection)
    print("--------------------------------------")
    print(df)
    print("--------------------------------------")
    print(df.columns)
    print("--------------------------------------")
    print(df.count())

    return df