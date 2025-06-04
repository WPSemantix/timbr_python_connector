import pytest
import pytimbr as timbr
from utils import get_connection_uri, parse_and_print_results

def test_basic_legacy_connection(test_config):
  hostname = test_config['hostname']
  port = test_config['port']
  ontology = test_config['ontology']
  username = test_config['username']
  password = test_config['password']
  enabled_ssl = test_config['enabled_ssl']
  http_path = test_config['http_path']

  conn = timbr.getConnection(hostname, port, ontology, username, password, enabled_ssl, http_path)
  result_obj = parse_and_print_results(conn)

  assert conn is not None, "Connection object is None."
  assert result_obj["column_count"] > 0, "No columns found in the cursor metadata."
  assert len(result_obj["description"]) > 0, "No columns found in the cursor description." 
  assert len(result_obj["concepts"]) > 0, "No concepts found in the database."

def test_jdbc_legacy_connection(test_config):
  hostname = test_config['hostname']
  port = test_config['port']
  ontology = test_config['ontology']
  username = test_config['username']
  password = test_config['password']
  enabled_ssl = test_config['enabled_ssl']
  http_path = test_config['http_path']

  conn = timbr.getJdbcConnection(get_connection_uri(hostname,port,ontology,enabled_ssl,http_path), username, password)
  result_obj = parse_and_print_results(conn)

  assert conn is not None, "Connection object is None."
  assert result_obj["column_count"] > 0, "No columns found in the cursor metadata."
  assert len(result_obj["description"]) > 0, "No columns found in the cursor description." 
  assert len(result_obj["concepts"]) > 0, "No concepts found in the database."