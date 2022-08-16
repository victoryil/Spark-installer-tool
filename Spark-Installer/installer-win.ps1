# Download hadoop from apache
$remote_url = 'https://github.com/cdarlint/winutils/raw/master/hadoop-3.2.2/bin/winutils.exe'
$local_file = 'c:\hadoop\bin\winutils.exe'


Write-Host "Installing Hadoop"

if(!(Get-Item -Path 'c:\hadoop\bin' -ErrorAction Ignore))
{
    Write-Host "Folder Doesn't Exists"
    #PowerShell Create directory if not exists
    New-Item 'c:\hadoop\bin' -ItemType Directory
}

Start-BitsTransfer -Source $remote_url -Destination $local_file

# Set environment variables permaneltly for hadoop in this user profile

Write-Host "Setting Environment Variables"

[System.Environment]::SetEnvironmentVariable('HADOOP_HOME','C:\hadoop',[System.EnvironmentVariableTarget]::User)
[System.Environment]::SetEnvironmentVariable('HADOOP_BIN','C:\hadoop\bin',[System.EnvironmentVariableTarget]::User)


Write-Host "Installing Spark"

if(!(Get-Item -Path 'c:\Spark' -ErrorAction Ignore))
{
    Write-Host "Folder Doesn't Exists"
    #PowerShell Create directory if not exists
    New-Item 'c:\Spark' -ItemType Directory
}

$remote_url = 'https://dlcdn.apache.org/spark/spark-3.2.2/spark-3.2.2-bin-hadoop3.2.tgz'
$local_file = 'spark-3.2.2-bin-hadoop3.2.tgz'

Start-BitsTransfer -Source $remote_url -Destination $local_file

# Extract spark to c:\Spark

Write-Host "Extracting Spark"

tar -xvf spark-3.2.2-bin-hadoop3.2.tgz -C c:\Spark

# Set environment variables permaneltly for spark in this user profile

Write-Host "Setting Environment Variables"

[System.Environment]::SetEnvironmentVariable('SPARK_HOME','C:\Spark\spark-3.2.2-bin-hadoop3.2',[System.EnvironmentVariableTarget]::User)
[System.Environment]::SetEnvironmentVariable('SPARK_BIN','C:\Spark\spark-3.2.2-bin-hadoop3.2\bin',[System.EnvironmentVariableTarget]::User)



Write-Host "Done"
