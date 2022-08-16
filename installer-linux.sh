#! /bin/bash

echo "Installing Hadoop..."

# Download hadoop 3.2.4 version
wget http://apache.mirrors.pair.com/hadoop/common/hadoop-3.2.4/hadoop-3.2.4.tar.gz
sudo tar -xvf hadoop-3.2.4.tar.gz -C /opt
# remove the tar file and cd opt    
sudo rm -rf hadoop-3.2.4.tar.gz
cd /opt
sudo mv hadoop-3.2.4 hadoop && sudo chown $USERNAME:$USERNAME -R hadoop

# Export HADOOP_HOME and PATH

echo "export HADOOP_HOME=/opt/hadoop" >> ~/.bashrc
echo "export PATH=\$PATH:\$HADOOP_HOME/sbin" >> ~/.bashrc

echo "look in /opt/hadoop/etc/hadoop/hadoop-env.sh if JAVA_HOME is set"
echo "if not, set JAVA_HOME to the correct value"

echo "Installing Spark.."

# Downdload Spark 3.2.2 version
wget https://dlcdn.apache.org/spark/spark-3.2.2/spark-3.2.2-bin-hadoop3.2.tgz
sudo tar -xvf spark-3.2.2-bin-hadoop3.2.tgz -C /opt
sudo rm -rf spark-3.2.2-bin-hadoop3.2.tgz
cd /opt
sudo mv spark-3.2.2-bin-hadoop3.2 spark && sudo chown $USERNAME:$USERNAME -R spark

#Export environment variables for Spark
echo "export SPARK_HOME=/opt/spark" >> ~/.bashrc
echo "export PATH=\$PATH:\$SPARK_HOME/bin" >> ~/.bashrc

echo "Run bashrc to update environment variables"
source ~/.bashrc

