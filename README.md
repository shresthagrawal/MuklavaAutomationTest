

To run: 

ansible playbook run.yml --ask-become-pass

As per the instructions and the previous documentation of the automation I have tried to create an awesome Anible automation role that will automate everything in my project for the Stock Management. In this project I have created my own dynamic inventory script, used it simultaneously with static inventories, created APIs for SQL Dump and firebase push notification, integrated docker to run msbuild and deploy C#, used Gradelew to build apk from android studio project, actively worked with modules like git, copy, fetch, mysql_db, shell and URI. It was really a great experience automating with Andible, and this will actually help me in the original project. The ansible role is well commented, I hope you like it.  

Below is a brief about all the tasks it performs:

Task1 -> Get the latest c# code from the gitbucket, run a Docker container with msbuild pre setup; using msbuild publish the C# code, take the published code and update it in the server.

Task2 -> Get the latest android studio project code, use gradelew to build apk in debug mode, copy the apk to the server, notify all the users about the latest release using Google Firbase push notification.(In further updates will also install the app into the android system using adb)

Task3 -> Get all the latest PHP codes for the server from git, Upload it in the server.  

Task4 -> use SQL dump to create a dump of the Online server, save a backup in the local system and using dynamic inventory and custom ansible directory get the IP of the offline local server and update the SQL theirs.

While working on the task I found that there as no module to install/launch apps and run shell commands on the Android device. After researching a while I found ADB which can be used to run shell commands, launch/install apps and do everything from CLI. I have planned to write custom ansible module of ADB for the next GCI task, this module will also help the Ansible community. Let me know what do you think about the plan ? and I would love to do even more challenging automation tasks!!

Project Repo: https://github.com/shresthagrawal/MuklavaAutomation.git

