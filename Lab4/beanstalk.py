import boto3
import time

client=boto3.client('elasticbeanstalk',region_name='us-east-1',aws_access_key_id='ASIAYVYV2OLBZL7Z3HOG',
aws_secret_access_key='Nw4BtRmZvB/Njx2N60h/LoRp5d+7Rj3D4+x7nv/q',aws_session_token='FwoGZXIvYXdzECUaDOytYI8iqs948pbl9yLOAV5hBkWB7Cn5KO0+OGXFtiaHWukbWS8k29oDxIac9ZGISb6bYJPZOS/L6Y5P3+QJEp4oJSFBPDKmdCFf5NKfm6h0qgTxCbYmbD5+GabEzdMqApCqF64fnvlXXw/QLZY68q/09ujt5dk2xMDo8EVke8zVVJtR9gfhu2RAniYMjFCju5CRmhdSt6bbjAlZbFlyac1sz4U/lCp35E/sJY/wUkWouYxNOV13uzJqk4cAx26YIdvzkoc+Ur032Dm2hXI2c2kHSt5WjLp+lV5sZlQsKLD+iooGMi0INtpadGXkUQzooyE5hSN3URJuBoWuCohJRlH2doUwai2MFbs1IZPJaJ8f1aI=')




def create_version():
    response = client.create_application_version(
        ApplicationName='my-app',
        AutoCreateApplication=True,
        Description='my-app-v4',
        Process=True,
        SourceBundle={
        'S3Bucket': '1901050lab4',
        'S3Key': 'Portfolio-main.zip',
        },
        VersionLabel='v6',

    )
    print(response)

def create_environment():
    response = client.create_environment(
        ApplicationName='my-app',
        EnvironmentName='my-env-5',
        SolutionStackName='64bit Amazon Linux 2 v3.3.5 running PHP 8.0',
        VersionLabel='v6',
        OptionSettings=[
        {
            'Namespace':'aws:autoscaling:launchconfiguration',
            'OptionName': 'IamInstanceProfile',
            'Value':'EMR_EC2_DefaultRole'
            
            
        },{
            'Namespace':'aws:autoscaling:launchconfiguration',
            'OptionName': 'EC2KeyName',
            'Value':'CS351-CG31-KP1'
        },{
            'Namespace':'aws:autoscaling:asg',
            'OptionName':'MaxSize',
            'Value':'2'
        }
    ],
    )

    print(response)

if __name__ == "__main__":
    #cloudFront_distribution
    create_version()
    time.sleep(5)
    create_environment()