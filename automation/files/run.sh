#!/bin/sh

# change the directory to the dir containing .netproject
cd C#.netProjectClone/muklavacsharp/
# pull the latest updates from server
git pull 
# use msbuild to build
msbuild.exe Muklava_Software.sln /p:DeployOnBuild=true 