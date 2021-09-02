#!/usr/bin/python
 
import os
 
os.system('yum install -y python python-dev python-pip')
os.system('pip install boto3')
 
os.system('yum -y update')
os.system('yum install -y httpd')
os.system('service httpd start')
os.system('cd ~')
 
import boto3
 
 
access_id_key = 'ASIAYVYV2OLBTUC3LNP4'
secret_access_key = 'jicFqwwO2iW0ThAo75oLDHS1gcdlFtdkmS8AdGFE'
session_token_key = 'FwoGZXIvYXdzENX//////////wEaDCX8aR3gF4t/X/LDniLOAUUC6dM9N30Ozi6ZJwrE7LNPlLiukQehOXQb//xwG0UMRTwGVCv8FraSE5n/t7ERxUzKrbN+DKPlPicofq8RAUM2GSHP4Weq5BiZaXLyjoOQZ15hUQ3pKv3MFQAkiGZgf8vGyI2RW8M+Vo7DenGbdWbdm22wfG2pnwdAf7GWYLtfkGal4gBuILQQtqkIBupiFGDz8QzboCKyeksdq3LoJ3OoEeSbF7qyPyMWF5myfGnpcnHRa1UhIfJ2AOAAOhbRdv5pf7dzO9rXu+ihy0HwKPyVwYkGMi0WDks1FXEk5E43ppAgyqw3o2vOQIfGpWYsissuMJamy4M2r7pD1swHA9zEMQM='
 
 
 
 
client = boto3.client('s3',aws_access_key_id = access_id_key,aws_secret_access_key = secret_access_key,aws_session_token = session_token_key)
 
 
client.download_file('bucket1901050','index.html','/var/www/html/'+'index.html')

os.system('sudo cp index.html /var/www/html/')