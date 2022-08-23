from installer import *
from version_grabber import *




installer = Installer()
installer.hadoop_version = "3.2"
installer.spark("spark-3.2.2")