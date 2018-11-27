#!/usr/bin/env python
# Custom Ansible script to get the remoteOfflineServer from the online server api

import os
import sys
import argparse
import requests 

try:
    import json
except ImportError:
    import simplejson as json

class createInventory(object):

    def __init__(self):
        self.inventory = {}
        self.readCliArgs()
        # call the API and get the IP address
        ip = self.getIP() 
        # Called with `--list`.
        if self.args.list:
            self.inventory = self.makeInventory(ip)

        # prints the JSON File
        print (json.dumps(self.inventory))

    def getIP(self):
        # make Api request and get the IP address
        apiURL = "http://muklava.com/salabs/getLocalIP.php"
        result = requests.get(url = apiURL) 
        return result.text  
        
    # Inventory script
    def makeInventory(self, ip):
        return {
            'remoteOfflineServer': {
                'hosts': [ip],
                'vars': {
                    'login_user': 'muklava',
                    'login_password': 'shresthharsh'
                }
            }
        }

    # Read the command line args passed to the script.
    def readCliArgs(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action = 'store_true')
        self.args = parser.parse_args()

# Get the inventory.
createInventory()