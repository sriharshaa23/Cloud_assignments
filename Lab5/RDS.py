import boto3


# aws configuration
access_id_key="ASIAYVYV2OLBZSUI2OWZ"
secret_access_key="l+748GYDlclPR9Fa+RUj+8yIGT2/DaIZhPFZcKGf"
session_token_key="FwoGZXIvYXdzEMf//////////wEaDPfnLqMbXI78UNv/4CLOAT2bvSJyQCMjjvaR7IQCOINn4bZnaPV937bdJVAj/m1BBEbiLqWM4qZHHfblgMrVt/y0UsCbq2QvBNfekQeYPP9saSWrfs2+9E9TKrBi/QZYSpP16EIuormCcK9HQovcLLyeMUBjTmozHffNvsDRePC0QUggjnyJMpgVVEeafbez8l5DsP3aqyw6TVwvwrHIuKj+5hEOH5nnAfHxyJWWLFOD9mXjQgS2HXe3mpM1o+fEEPjPlaHd4/GUgPbA21/uIzeYZuhAf7hcGecSpzhPKLzOrooGMi0614LZdKeLRToJzRNEnWLylVTas/UzQ/hyxqw2YsEzbyQ1KtBmxEg7HveDSJY="

rdsClient = boto3.client(
    "rds",
    aws_access_key_id=access_id_key,
    aws_secret_access_key=secret_access_key,
    aws_session_token=session_token_key,
    region_name="us-east-1",
)

response = rdsClient.create_db_instance(
    DBName="seethu",
    DBInstanceIdentifier="seethu",
    AllocatedStorage=5,
    DBInstanceClass="db.t2.micro",
    Engine="MySQL",
    MasterUsername="seethu",
    MasterUserPassword="seethu123",
    PubliclyAccessible=True,
)