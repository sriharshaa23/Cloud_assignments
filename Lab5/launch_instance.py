import boto3

access_id_key="ASIAYVYV2OLBTH7SJLPQ"
secret_access_key="Nb2V6N8t4jI4T3NChV1A8kzmLlkzNeZdBh10LQKL"
session_token_key="FwoGZXIvYXdzEM7//////////wEaDOqvvcg0hyhy0g1Y0iLOAZrOKCgCUFW3SQjw40D5/MIJXkuN9gP4yVy0xhEoogidbm0HGfNcrAooaR5RGAFMm16j1MpCjR3GJ/3eWsPByHjO0KL+bU1JTTsz52b1xq6Dzp5O2T+96sMnZvvx+acyEx18V/s/c2JerJB49dTn7LU/hK4yaGBjbzdVpgxkoDef1MCDsCa7KZu0KPt3x4oArkD0S8WWuj2nEOCRlUhk4fLaRmgYDeNb101XGdtZGM8i//6WRg+IVERDJzVY9evqzPlfvrzls+I5RzYalEsvKOr/r4oGMi1CltOTtWARcxbC8p5j+1xEE3xostMR43r0gi8e7wSbw05xXez81GBYJ/vlF/c="


ec2 = boto3.resource(
    "ec2",
    aws_access_key_id=access_id_key,
    aws_secret_access_key=secret_access_key,
    aws_session_token=session_token_key,
    region_name="us-east-1",
)

instances = ec2.create_instances(
    ImageId="ami-0c2b8ca1dad447f8a",
    MinCount=1,
    MaxCount=1,
    InstanceType="t2.micro",
    KeyName="CS351-CG31-KP1",
    SecurityGroupIds=["sg-0b8eb7cec9f4e6d68"],
    UserData=open("script.sh").read(),
)


print(instances)


instance = instances[0]
instance.wait_until_running()
instance.load()

print(instance.public_dns_name)