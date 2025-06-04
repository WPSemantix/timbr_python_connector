import pytest
import pytimbr as timbr
import pandas as pd
from utils import get_connection_uri, parse_and_print_results_using_pandas

def test_basic_connection(test_config):
  hostname = test_config['hostname']
  port = test_config['port']
  ontology = test_config['ontology']
  username = test_config['username']
  password = test_config['password']
  enabled_ssl = test_config['enabled_ssl']
  http_path = test_config['http_path']

  conn = timbr.get_connection(hostname, port, ontology, username, password, enabled_ssl, http_path)

  df = parse_and_print_results_using_pandas(conn)

  assert not df.empty, "DataFrame is empty."
  assert len(df.columns) > 0, "No columns found in the DataFrame."

def test_jdbc_connection(test_config):
  hostname = test_config['hostname']
  port = test_config['port']
  ontology = test_config['ontology']
  username = test_config['username']
  password = test_config['password']
  enabled_ssl = test_config['enabled_ssl']
  http_path = test_config['http_path']

  conn = timbr.get_jdbc_connection(get_connection_uri(hostname, port, ontology, enabled_ssl, http_path), username, password)
  
  df = parse_and_print_results_using_pandas(conn)

  assert not df.empty, "DataFrame is empty."
  assert len(df.columns) > 0, "No columns found in the DataFrame."