import boto3

auto_s = boto3.client('autoscaling',aws_access_key_id='ASIAYVYV2OLBVNMF2D2B',aws_secret_access_key='uhlFWbFYSPT0u++fQUOPBYwNLrJvlBA9CXMK8Rj7',aws_session_token='FwoGZXIvYXdzEHEaDDCMsNkoLYk4lJhJhiLOAVzBRUKrBIW1JqZwrJJLThAtnfsVpjROSk03oIZxH/zRdt9lBYA5u+kNbkvl0OmC/Xe4vwdey2PzwK6eepx+WIVEnJTQTkM6UEOuj+TvsmSu6jK557+xfmHC56qK9u/JYAUzjQq1L4YAG2+9FDrhGYX6HVkrxtiRz+Zu8e2BvQ9lKSzX4/nVwRzD5rosR4j5X54KMWlyr/yx0XVQOwpsFKO/X20ytDyAlJiKPrWo8hst6g6MRAtjSGc8WmyUH7/iwzq5/v481XsKo2r6oA18KNu144kGMi0HhjzvAOiguRpv6uwzXgoHdnrtp8UkRg7RlriCLoJhTuTidOV3L8y1itEbNJg=',region_name='us-east-2')
lc=auto_s.create_launch_configuration(
LaunchConfigurationName='my-launch-config',
InstanceType='t2.micro',
KeyName='CS351-CG31-KP1',
ImageId = 'ami-0c2b8ca1dad447f8a',
SecurityGroups=['sg-0b8eb7cec9f4e6d68'],
UserData=open('script.sh').read()
)
auto_s.create_auto_scaling_group(
AutoScalingGroupName='my-auto-scaling-group',
LaunchConfigurationName='my-launch-config',
AvailabilityZones=['us-east-1c'],
MaxSize=3,
MinSize=1
)
scale_up_policy=auto_s.put_scaling_policy(
AdjustmentType='ChangeInCapacity',
AutoScalingGroupName='my-auto-scaling-group',
PolicyName='scale_up',
ScalingAdjustment=1
)
scale_down_policy=auto_s.put_scaling_policy(
AdjustmentType='ChangeInCapacity',
AutoScalingGroupName='my-auto-scaling-group',
PolicyName='scale_down',
ScalingAdjustment=-1
)
cloud_w = boto3.client('cloudwatch',aws_access_key_id='ASIAYVYV2OLBVNMF2D2B',aws_secret_access_key='uhlFWbFYSPT0u++fQUOPBYwNLrJvlBA9CXMK8Rj7',aws_session_token='FwoGZXIvYXdzEHEaDDCMsNkoLYk4lJhJhiLOAVzBRUKrBIW1JqZwrJJLThAtnfsVpjROSk03oIZxH/zRdt9lBYA5u+kNbkvl0OmC/Xe4vwdey2PzwK6eepx+WIVEnJTQTkM6UEOuj+TvsmSu6jK557+xfmHC56qK9u/JYAUzjQq1L4YAG2+9FDrhGYX6HVkrxtiRz+Zu8e2BvQ9lKSzX4/nVwRzD5rosR4j5X54KMWlyr/yx0XVQOwpsFKO/X20ytDyAlJiKPrWo8hst6g6MRAtjSGc8WmyUH7/iwzq5/v481XsKo2r6oA18KNu144kGMi0HhjzvAOiguRpv6uwzXgoHdnrtp8UkRg7RlriCLoJhTuTidOV3L8y1itEbNJg=',region_name='us-east-2')
cloud_w.put_metric_alarm(
AlarmName='up_alarm',
Namespace='AWS/EC2',
MetricName='CPUUtilization',
Statistic='Average',
ComparisonOperator='GreaterThanThreshold',
Threshold=70,
Period=60,
EvaluationPeriods=2,
AlarmActions=[scale_up_policy['PolicyARN']]
)
cloud_w.put_metric_alarm(
AlarmName='down_alarm',
Namespace='AWS/EC2',
MetricName='CPUUtilization',
Statistic='Average',
ComparisonOperator='LessThanThreshold',
Threshold=40,
Period=60,
EvaluationPeriods=2,
AlarmActions=[scale_down_policy['PolicyARN']]
)
import time
time.sleep(30)
response = auto_s.describe_auto_scaling_groups(
AutoScalingGroupNames=['my-auto-scaling-group'],
)
list_auto = response['AutoScalingGroups']
req_instance_id = (((list_auto[0])['Instances'])[0])['InstanceId']
print(req_instance_id)
ec2 = boto3.resource('ec2',aws_access_key_id='ASIAYVYV2OLBVNMF2D2B',aws_secret_access_key='uhlFWbFYSPT0u++fQUOPBYwNLrJvlBA9CXMK8Rj7',aws_session_token='FwoGZXIvYXdzEHEaDDCMsNkoLYk4lJhJhiLOAVzBRUKrBIW1JqZwrJJLThAtnfsVpjROSk03oIZxH/zRdt9lBYA5u+kNbkvl0OmC/Xe4vwdey2PzwK6eepx+WIVEnJTQTkM6UEOuj+TvsmSu6jK557+xfmHC56qK9u/JYAUzjQq1L4YAG2+9FDrhGYX6HVkrxtiRz+Zu8e2BvQ9lKSzX4/nVwRzD5rosR4j5X54KMWlyr/yx0XVQOwpsFKO/X20ytDyAlJiKPrWo8hst6g6MRAtjSGc8WmyUH7/iwzq5/v481XsKo2r6oA18KNu144kGMi0HhjzvAOiguRpv6uwzXgoHdnrtp8UkRg7RlriCLoJhTuTidOV3L8y1itEbNJg=',region_name='us-east-2')
instance = ec2.Instance(id=req_instance_id)
instance.wait_until_running()
instance.load()
print(instance.public_dns_name)