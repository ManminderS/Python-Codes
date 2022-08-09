
import boto3

ec2 = boto3.resource("ec2")

instances = ec2.create_instances(ImageId ='ami-090fa75af13c156b4', InstanceType='t2.micro', MinCount=1, MaxCount=2,)





