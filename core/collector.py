import boto3
from botocore.exceptions import ClientError, NoCredentialsError

class CloudCollector:
    def __init__(self, region_name="eu-north-1"):
        self.region_name = region_name
        try:
            # Initialize the EC2 client to talk to AWS
            self.ec2_client = boto3.client('ec2', region_name=self.region_name)
        except (NoCredentialsError, Exception) as e:
            print(f"[-] Error initializing AWS clients: {e}")
            exit(1)

    def collect_security_groups(self):
        """Asks AWS for a raw list of all security groups and their firewall rules."""
        print("[*] Collecting Security Group configurations from AWS...")
        try:
            response = self.ec2_client.describe_security_groups()
            # Return just the list of security groups from AWS's large response dictionary
            return response.get('SecurityGroups', [])
        except ClientError as e:
            print(f"[-] Failed to fetch security groups: {e}")
            return []