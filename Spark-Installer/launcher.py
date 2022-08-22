"""
    Author: Victor Daniel Gil Becerra
    Version: 0.1.1
    Update date: 2022-08-18
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
            "hadoop_home": "C:\hadoop",
            "hadoop_bin": "C:\hadoop/bin",
            "hadoop_url": "https://github.com/cdarlint/winutils/raw/master/hadoop-3.2.2/bin/winutils.exe",
            "hadoop_file": "winutils.exe",
            "move_command": "move",
            "env_hadoop_home_command": "setx HADOOP_HOME C:\hadoop",
            "env_hadoop_bin_command": "setx HADOOP_BIN C:\hadoop/bin",
        },
        "Linux": {
            "hadoop_home": "/opt/hadoop",
            "hadoop_bin": "/opt/hadoop/sbin",
            "hadoop_url": "http://apache.mirrors.pair.com/hadoop/common/hadoop-3.2.4/hadoop-3.2.4.tar.gz",
            "hadoop_file": "hadoop-3.2.4.tar.gz",
            "extract_command": "tar -xvf {local_file} -C {home_path}",
            "move_command": "mv",
            "env_hadoop_home_command": 'echo "export HADOOP_HOME=/opt/hadoop" >> ~/.bashrc',
            "env_hadoop_bin_command": 'echo "export PATH=\$PATH:\$HADOOP_HOME/sbin" >> ~/.bashrc',
        },
        "Darwin": "toimplement"
    }

    os_config_current = os_config_hadoop.get(platform.system())

    # Set routes for hadoop download
    remote_url = os_config_current.get('hadoop_url')
    local_file = os_config_current.get('hadoop_file')

    # Create enviroment variable for hadoop path
    os.system(os_config_current.get('env_hadoop_home_command'))
    os.system(os_config_current.get('env_hadoop_bin_command'))

    # Download file from url
    request.urlretrieve(remote_url, local_file)

    # Create hadooop folder in primary directory if not exists
    if not os.path.exists(os_config_current.get('hadoop_bin')):
        os.makedirs(os_config_current.get('hadoop_bin'))
    
    # if os is linux extract the file to the hadoop folder
    if platform.system() == "Linux":
        os.system(os_config_current.get('extract_command').format(local_file=local_file, home_path=os_config_current.get('hadoop_home')))
        os.system(os_config_current.get('move_command').format(local_file=os_config_current.get('hadoop_home')+"/hadoop-3.2.4", home_path=os_config_current.get('hadoop_bin')))
        # Set permissions for hadoop folder
        os.system("chmod $USERNAME:$USERNAME -R hadoop")
        os.remove(local_file)

        os.system("source ~/.bashrc")
    else:
        # Extract the file to the hadoop/bin folder
        os.system(os_config_current.get('move_command') + ' ' + local_file + ' ' + os_config_current.get('hadoop_bin'))

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
            "env_spark_bin_command": "setx SPARK_BIN C:\Spark/bin"
        },
        "Linux": {
            "spark_home": "/opt/spark",
            "spark_bin": "/opt/spark/bin",
            "spark_url": "http://apache.mirrors.pair.com/spark/spark-3.2.2/spark-3.2.2-bin-hadoop3.2.tgz",
            "spark_file": "spark-3.2.2-bin-hadoop3.2.tgz",
            "extract_command": "tar -xvf {local_file} -C /opt",
            "move_command": "mv {source} {dest}",
            "env_spark_home_command": 'echo "export SPARK_HOME=/opt/spark" >> ~/.bashrc',
            "env_spark_bin_command": 'echo "export PATH=\$PATH:\$SPARK_HOME/bin" >> ~/.bashrc'
        },
        "Darwin": "toimplement"
    }

    
    # Save in variable os_config_current the current o  s configuration
    os_config_current = os_config_spark.get(platform.system())

    # Set routes for spark download
    remote_url = os_config_current.get('spark_url')
    local_file = os_config_current.get('spark_file')

    # Create enviroment variable for spark path
    os.system(os_config_current.get('env_spark_home_command'))
    os.system(os_config_current.get('env_spark_bin_command'))

    # Create spark folder in primary directory if not exists
    if not os.path.exists(os_config_current.get('spark_home')):
        os.makedirs(os_config_current.get('spark_home'))
    
    # Download file from url
    request.urlretrieve(remote_url, local_file)

    # Extract the file to the spark folder
    os.system(os_config_current.get('extract_command').format(local_file=local_file, home_path=os_config_current.get('spark_home')))
    if platform.system() == "Linux":
        os.system(os_config_current.get('move_command').format(source=os_config_current.get('spark_home')+"/spark-3.2.2-bin-hadoop3.2", dest="spark"))
        # Set permissions for spark folder
        os.system("chmod $USERNAME:$USERNAME -R spark")
        os.system("source ~/.bashrc")

    # Remove the downloaded file
    os.remove(local_file)

hadoop()
spark()

