#!/usr/bin/python



import os


os.system('yum install -y python python-dev python-pip')
os.system('pip install boto3')


os.system('sudo yum update -y')
os.system('sudo amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2')
os.system('sudo yum install -y httpd')
os.system('sudo systemctl start httpd')
os.system('sudo usermod -a -G apache ec2-user')
os.system('sudo chown -R ec2-user:apache /var/www')
os.system('sudo chmod 2775 /var/www')
os.system('find /var/www -type d -exec sudo chmod 2775 {} \;')
os.system('find /var/www -type f -exec sudo chmod 0664 {} \;')

os.system('mkdir var/www/inc')
os.system("""echo " <?php define('DB_SERVER', 'seethu.cbepdtekbwql.us-east-1.rds.amazonaws.com');define('DB_USERNAME', 'seethu');define('DB_PASSWORD', 'seethu123');
define('DB_DATABASE', 'seethu');?>" >> var/www/inc/dbinfo.inc""")

import boto3

access_id_key="ASIAYVYV2OLBTH7SJLPQ"
secret_access_key="Nb2V6N8t4jI4T3NChV1A8kzmLlkzNeZdBh10LQKL"
session_token_key="FwoGZXIvYXdzEM7//////////wEaDOqvvcg0hyhy0g1Y0iLOAZrOKCgCUFW3SQjw40D5/MIJXkuN9gP4yVy0xhEoogidbm0HGfNcrAooaR5RGAFMm16j1MpCjR3GJ/3eWsPByHjO0KL+bU1JTTsz52b1xq6Dzp5O2T+96sMnZvvx+acyEx18V/s/c2JerJB49dTn7LU/hK4yaGBjbzdVpgxkoDef1MCDsCa7KZu0KPt3x4oArkD0S8WWuj2nEOCRlUhk4fLaRmgYDeNb101XGdtZGM8i//6WRg+IVERDJzVY9evqzPlfvrzls+I5RzYalEsvKOr/r4oGMi1CltOTtWARcxbC8p5j+1xEE3xostMR43r0gi8e7wSbw05xXez81GBYJ/vlF/c="


s3client = boto3.client('s3',aws_access_key_id = access_id_key,aws_secret_access_key = secret_access_key,aws_session_token = session_token_key)
s3client.download_file('sriharsha','index.html','var/www/html/index.html')
s3client.download_file('sriharsha','authentication.php','var/www/html/authentication.php')
s3client.download_file('sriharsha','connection.php','var/www/html/connection.php')
s3client.download_file('sriharsha','customer.html','var/www/html/customer.html')
s3client.download_file('sriharsha','customer.php','var/www/html/customer.php')
s3client.download_file('sriharsha','feedback.php','var/www/html/feedback.php')
s3client.download_file('sriharsha','style.css','var/www/html/style.css')
