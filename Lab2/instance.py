import boto3
 
ec2 = boto3.resource('ec2')
instances = ec2.create_instances(ImageId='ami-0c2b8ca1dad447f8a', MinCount=1, MaxCount=1, InstanceType = 't2.micro',KeyName='CS351-CG31-KP1',
SecurityGroupIds=['sg-0b8eb7cec9f4e6d68'], UserData = open('script.sh').read())
 
print(instances)
#printing instances.
for instance in instances:
        print(instance)
 
 
instance = instances[0]
#waiting until the launched instance is running.import boto3
 
instance.wait_until_running()
instance.load()
print("dns name =",instance.public_dns_name)