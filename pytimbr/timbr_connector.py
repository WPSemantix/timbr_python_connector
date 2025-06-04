#
#             *###              .,              @%             
#       *%##  `#// %%%*  *@     ``              @%             
#        #*.    * .%%%`  @@@@*  @@   @@@@,@@@@  @&@@@@   .&@@@*
#            #%%#   ..   *@     @@  @`  @@` ,@  @%   #@  @@  
#      ,, .,%(##/./%%#,  *@     @@  @`  @@` ,@  @%   #@  @@   
#    ,%##%          ``   `/@@*  @@  @`  @@` ,@  (/@@@#/  @@   
#      ``                                                     
#  ``````````````````````````````````````````````````````````````
#  Copyright (C) 2018-2024 timbr.ai
#

from . import timbr_jdbapi
import os
import platform
import pathlib

main_jar_path = os.environ.get('TIMBR_JDBC_JAR_PATH', os.path.join(pathlib.Path(__file__).parent.resolve(), 'jars'))
jdbc_driver = 'org.apache.hive.jdbc.HiveDriver'

def get_combined_jars_path(maindir):
  jar_dir = os.walk(maindir)
  jars_array = []
  for _root, _dirs, files in jar_dir:
    for filename in files:
      if filename.find('.jar') > 0:
        jars_array.append(os.path.join(maindir, filename))
  jars = ":".join(jars_array)
  if "Windows" in platform.platform():
    jars = ";".join(jars_array)
  
  return jars

jars_path = get_combined_jars_path(main_jar_path)

def get_jdbc_connection(jdbc_url, username, password):
  conn = timbr_jdbapi.connect(jdbc_driver, jdbc_url, [username, password], jars_path)
  return conn

def get_connection(hostname, port, ontology, username, password, enabled_ssl = 'true', http_path = '/timbr-server'):
  jdbc_url = f"jdbc:hive2://{hostname}:{port}/{ontology};transportMode=http;ssl={enabled_ssl};httpPath={http_path}"
  conn = timbr_jdbapi.connect(jdbc_driver, jdbc_url, [username, password], jars_path)
  return conn

# Deprecated - Backward compatibility

def getJdbcConnection(jdbc_url, username, password):
  conn = timbr_jdbapi.connect(jdbc_driver, jdbc_url, [username, password], jars_path)
  return conn

def getConnection(hostname, port, ontology, username, password, enabled_ssl = True, http_path = '/timbr-server'):
  jdbc_url = f"jdbc:hive2://{hostname}:{port}/{ontology};transportMode=http;ssl={enabled_ssl};httpPath={http_path}"
  conn = timbr_jdbapi.connect(jdbc_driver, jdbc_url, [username, password], jars_path)
  return conn
