import boto3
import functions

aws_region = "us-east-2"
ec2 = boto3.resource("ec2", region_name=aws_region)

instances = ec2.instances.filter(Filters=[{'Name': 'instance-lifecycle', 'Values': ['spot']}, 
    {'Name': 'instance-state-name', 'Values':['running']}])
instance_list = []

for instance in instances:
        instance_id = instance.id
        instance_list.append(instance_id)

# no running spot instances 
if not instance_list :
    print("no results")

# running spot instances exist 
else : 
    print("The current running spot instances : ",instance_list)
    functions.request_spot_fleet()