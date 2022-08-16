# Spark Installer

A tool that facilitates the installation of Spark and Hadoop on different systems

## Python version
Currently it downloads and moves the packages for windows with a fixed version of spark and hadoop, it is pending to make a dynamic mode for versions.

### Bugs
Does not create environment variables for windows

### Features
The installation will be generated for different systems and we will be able to pass it arguments to dynamically decide where to install it, always maintaining a default configuration for the ease of users.

Environment variables will be added automatically for each system

## Windows Version
Running the ps1 script in the powershell as follows:
**.\your_directory\launcher.ps1**
You can install version 3.2.2 of spark and hadoop

This version auto-set windows enviroment variables
### Bugs 
None

### Feautures
The installation will be generated for different systems and we will be able to pass it arguments to dynamically decide where to install it, always maintaining a default configuration for the ease of users.