"""
    Author: Victor Daniel Gil Becerra
    Version: 0.1.1
    Date: 2022-08-18
    License: MIT
    Description: This script is used to install hadoop and spark on any systems.
    Requirements: Python 3.7.0 or higher and requests library
    Usage: python launcher.py
"""

from urllib import request
import os
import platform

#Hadoop
def hadoop():
    os_config_hadoop = {
        "Windows": {
            "hadoop_home": "C:\Hadoop",
            "hadoop_bin": "C:\Hadoop/bin",
            "hadoop_url": "https://github.com/cdarlint/winutils/raw/master/hadoop-3.2.2/bin/winutils.exe",
            "hadoop_file": "winutils.exe",
            "move_command": "move",
            "env_hadoop_home_command": "setx HADOOP_HOME C:\Hadoop",
            "env_hadoop_bin_command": "setx HADOOP_BIN C:\Hadoop/bin",
        },
        "Linux": "toimplement",
        "Darwin": "toimplement"
    }

    os_config_current = os_config_hadoop.get(platform.system())

    # Set routes for hadoop download
    remote_url = os_config_current.get('hadoop_url')
    local_file = os_config_current.get('hadoop_file')

    # Download file from url
    request.urlretrieve(remote_url, local_file)

    # Create hadooop folder in primary directory if not exists
    if not os.path.exists(os_config_current.get('hadoop_bin')):
        os.makedirs(os_config_current.get('hadoop_bin'))
    
    # Extract the file to the hadoop/bin folder
    os.system(os_config_current.get('move_command') + ' ' + local_file + ' ' + os_config_current.get('hadoop_bin'))
    
    # Remove the downloaded file
    os.remove(local_file)
    # Create enviroment variable for hadoop path
    os.system(os_config_current.get('env_hadoop_home_command'))
    os.system(os_config_current.get('env_hadoop_bin_command'))

# Spark
def spark():

    os_config_spark = {
        "Windows": {
            "spark_home": "C:\Spark",
            "spark_bin": "C:\Spark/bin",
            "spark_url": "https://dlcdn.apache.org/spark/spark-3.2.2/spark-3.2.2-bin-hadoop3.2.tgz",
            "spark_file": "spark-3.2.2-bin-hadoop3.2.tgz",
            "extract_command": "tar -xvf {local_file} -C {home_path}",
            "env_spark_home_command": "setx SPARK_HOME C:\Spark",
            "env_spark_bin_command": "setx SPARK_BIN C:\Spark/bin",
        },
        "Linux": "toimplement",
        "Darwin": "toimplement"
    }

    
    # Save in variable os_config_current the current os configuration
    os_config_current = os_config_spark.get(platform.system())

    # Set routes for spark download
    remote_url = os_config_current.get('spark_url')
    local_file = os_config_current.get('spark_file')

    # Create spark folder in primary directory if not exists
    if not os.path.exists(os_config_current.get('spark_home')):
        os.makedirs(os_config_current.get('spark_home'))
    
    # Download file from url
    request.urlretrieve(remote_url, local_file)

    # Extract the file to the spark folder
    os.system(os_config_current.get('extract_command').format(local_file=local_file, home_path=os_config_current.get('spark_home')))

    # Remove the downloaded file
    os.remove(local_file)
    # Create enviroment variable for spark path
    os.system(os_config_current.get('env_spark_home_command'))
    os.system(os_config_current.get('env_spark_bin_command'))

hadoop()
spark()

