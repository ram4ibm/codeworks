#!/usr/bin/env python
import requests
import json

# Function to parse path and subPath
def collect_metadata(url,path):
    for metadataPath in requests.get(url).text.split('\n'):
        metadataUrl_withPath = '{0}{1}'.format(url,metadataPath)
        if metadataPath.endswith('/'):
            metadataSubPath = metadataPath.split('/')[-2]
            path[metadataSubPath] = {}
            collect_metadata(metadataUrl_withPath, path[metadataSubPath])
        else:
            response = requests.get(metadataUrl_withPath)
            if response.status_code != 404:
                try:
                    path[metadataPath] = json.loads(response.text)
                except ValueError:
                    path[metadataPath] = response.text
            else:
                path[metadataPath] = ""

# Function to initialize a dict to collect the metadata
def initialize_and_call():
    metadataUrl = 'http://169.254.169.254/latest'
    metadataDictionary = {'COLLECTED-METADATA': {}}
    collect_metadata('{0}/{1}/'.format(metadataUrl,'meta-data'),metadataDictionary['COLLECTED-METADATA'])
    return metadataDictionary

print(json.dumps(initialize_and_call(),indent=4, sort_keys=True))
