import boto3

def spot_fleet_id():
    response = ec2.describe_spot_fleet_requests()
    fleet_request_ids = [f['SpotFleetRequestId'] for f in response['SpotFleetRequestConfigs']]
    return fleet_request_ids

fleet_id = spot_fleet_id()
aws_region = "us-east-2"
ec2 = boto3.client("ec2", region_name=aws_region)

def request_spot_fleet():
    response = ec2.request_spot_fleet(
        DryRun=True,
        SpotFleetRequestConfig={
            "IamFleetRole": "arn:aws:iam::871641431188:role/aws-ec2-spot-fleet-tagging-role",
            "AllocationStrategy": "priceCapacityOptimized",
            "TargetCapacity": 1,
            "ValidFrom": "2023-04-03T06:01:28.000Z",
            "ValidUntil": "2024-04-03T06:01:28.000Z",
            "TerminateInstancesWithExpiration": True,
            "Type": "maintain",
            "SpotMaxTotalPrice": "0.70",
            "InstanceInterruptionBehavior": "stop",
            "OnDemandAllocationStrategy": "lowestPrice",
            "LaunchSpecifications": [],
            "LaunchTemplateConfigs": [
                {
                    "LaunchTemplateSpecification": {
                        "LaunchTemplateId": "lt-005715fa9210a4257",
                        "Version": "2"
                    },
                    "Overrides": [
                        {
                            "InstanceType": "g4dn.xlarge",
                            "WeightedCapacity": 1,
                            "SubnetId": "subnet-7f0f6816"
                        },
                        {
                            "InstanceType": "g4dn.xlarge",
                            "WeightedCapacity": 1,
                            "SubnetId": "subnet-f5e04f8e"
                        },
                        {
                            "InstanceType": "g4dn.xlarge",
                            "WeightedCapacity": 1,
                            "SubnetId": "subnet-d452ab99"
                        }
                    ]
                }
            ],
            "SpotPrice": "0.22"
        }
    )

def boot_spot_instance():
    response = ec2.modify_spot_fleet_request(
            SpotFleetRequestId = fleet_id,
            TargetCapacity = 2,
            DryRun = True
            )

def shutdown_spot_instance():
    response = ec2.modify_spot_fleet_request(
            SpotFleetRequestId = fleet_id,
            TargetCapacity = 1,
            DryRun = True
            )
