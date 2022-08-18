
# Spark Installer

A tool that facilitates the installation of Spark and Hadoop on different systems

## Python version
Currently it downloads and moves the packages for windows with a fixed version of spark and hadoop, it is pending to make a dynamic mode for versions.

### Bugs
None

### Features
The installation will be generated for different systems and we will be able to pass it arguments to dynamically decide where to install it, always maintaining a default configuration for the ease of users.

Environment variables will be added automatically for each system

## Windows Version
Running the ps1 script in the powershell as follows:
**.\your_directory\installer-win.ps1**
You can install version 3.2.2 of spark and hadoop

### Common problems
If when launching you get an error message like the following '...because script execution is disabled on this system' you should run this command as administrator in your powershell before starting the script

**Set-ExecutionPolicy RemoteSigned -Scope CurrentUser**

This version auto-set windows enviroment variables
### Bugs 
None

### Feautures
We will be able to pass it arguments to dynamically decide where to install it, always maintaining a default configuration for the ease of users.

## Linux version
Running the sh script in terminal as follows:
**source installer-linux.sh**
You can install version 3.2.2 of spark and hadoop

This version auto-set windows enviroment variables

### Common problems
During launch you may be asked to enter your admin password

### Bugs 
None

### Feautures
We will be able to pass it arguments to dynamically decide where to install it, always maintaining a default configuration for the ease of users.

## Mac version
State: Pending

