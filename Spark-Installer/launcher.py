from urllib import request
import os
import platform

#Hadoop
def hadoop():
    if(platform.system() == 'Windows'):
        # Download file from url 'https://github.com/cdarlint/winutils/raw/master/hadoop-3.2.2/bin/winutils.exe' and save locally as 'winutils.exe'
        remote_url = 'https://github.com/cdarlint/winutils/raw/master/hadoop-3.2.2/bin/winutils.exe'
        local_file = 'winutils.exe'
        request.urlretrieve(remote_url, local_file)
        
        # Create hadooop folder in primary directory if not exists
        if not os.path.exists('C:\hadoop'):
            os.makedirs('C:\hadoop')
        # Create bin folder in hadoop directory if not exists
        if not os.path.exists('C:\hadoop/bin'):
            os.makedirs('C:\hadoop/bin')
        # move the file to the hadoop/bin folder
        os.system('move ' + local_file + ' C:\hadoop/bin')
        # Create enviroment variable for hadoop path
        os.environ['HADOOP_HOME'] = 'C:\hadoop'
        # Create enviroment variable for hadoop bin path in windows
        os.environ['HADOOP_BIN'] = 'C:\hadoop/bin'
    elif(platform.system() == 'Linux'):
        print('Linux')
    elif(platform.system() == 'Darwin'):
        print('Mac')
    else:
        print('Unknown')

# Spark
def spark():
    if(platform.system() == 'Windows'):
            
        # Define the remote file to retrieve
        remote_url = 'https://dlcdn.apache.org/spark/spark-3.2.2/spark-3.2.2-bin-hadoop3.2.tgz'
        # Define the local filename to save data
        local_file = 'spark-3.2.2-bin-hadoop3.2.tgz'
        # Download remote and save locally
        request.urlretrieve(remote_url, local_file)

        # Create bin folder in diskroot directory if not exists
        if not os.path.exists('C:\Spark'):
            os.makedirs('C:\Spark')
        # Extract the file to the Spark folder
        os.system('tar -xvf ' + local_file + ' -C C:\Spark')
        # Remove the downloaded file
        os.remove(local_file)
        # Create enviroment variable for spark path
        os.environ['SPARK_HOME'] = 'C:\Spark/spark-3.2.2-bin-hadoop3.2'
        # Create enviroment variable for spark bin path
        os.environ['SPARK_BIN'] = 'C:\Spark/spark-3.2.2-bin-hadoop3.2/bin'
    elif(platform.system() == 'Linux'):
        print('Linux')
    elif(platform.system() == 'Darwin'):
        print('Mac')
    else:
        print('Unknown')
        
hadoop()
spark()

