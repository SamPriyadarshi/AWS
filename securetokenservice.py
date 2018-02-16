import boto3


def role_arn_to_session(**args):
    """
    Usage :
        session = role_arn_to_session(
            RoleArn='arn:aws:iam::012345678901:role/example-role',
            RoleSessionName='ExampleSessionName')
        client = session.client('sqs')
    """
    client = boto3.client('sts')
    response = client.assume_role(**args)
    return boto3.Session(
        aws_access_key_id=response['Credentials']['AccessKeyId'],
        aws_secret_access_key=response['Credentials']['SecretAccessKey'],
        aws_session_token=response['Credentials']['SessionToken'])


session = role_arn_to_session(
            RoleArn='<ARN of the role which you want to assume>',
            RoleSessionName='ExampleSessionName')

client = boto3.client('ec2', region_name='us-east-1')

regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
for region in regions:
    ec2 = session.client('ec2', region_name=region)
    allinstances1 = ec2.describe_instances()
    allinstances = allinstances1['Reservations']
    #ec2list = []
    for instance in allinstances:
        #ec2list.append(instance['Instances'][0]['InstanceId'])
        print(instance['Instances'][0]['InstanceId'])
        print(instance['Instances'][0]['PrivateIpAddress'])
        print(instance['OwnerId'])
        print(instance['Instances'][0]['LaunchTime'])