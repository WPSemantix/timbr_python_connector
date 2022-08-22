#
#             *###              .,              @%             
#       *%##  `#// %%%*  *@     ``              @%             
#        #*.    * .%%%`  @@@@*  @@   @@@@,@@@@  @&@@@@   .&@@@*
#            #%%#   ..   *@     @@  @`  @@` ,@  @%   #@  @@  
#      ,, .,%(##/./%%#,  *@     @@  @`  @@` ,@  @%   #@  @@   
#    ,%##%          ``   `/@@*  @@  @`  @@` ,@  (/@@@#/  @@   
#      ``                                                     
#  ``````````````````````````````````````````````````````````````
#  Copyright (C) 2018-2021 timbr.ai
#
#  This file is part of the timbr-JayDeBeApi connector
#
import jaydebeapi
import os
import platform

main_jar_path = os.environ.get('TIMBR_JDBC_JAR_PATH', os.path.join(os.getcwd(), 'jars'))
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

def getConnection(jdbc_url, username, password):

    conn = jaydebeapi.connect(jdbc_driver, jdbc_url, [username, password], jars_path)
    return conn
