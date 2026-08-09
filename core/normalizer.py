class ResourceNormalizer:
    @staticmethod
    def normalize_security_groups(raw_sgs):
        """Takes messy AWS security group data and turns it into a clean, simple format."""
        normalized = []
        for sg in raw_sgs:
            formatted_rules = []
            
            # Loop through every inbound firewall rule in the security group
            for perm in sg.get('IpPermissions', []):
                from_port = perm.get('FromPort', 0)
                to_port = perm.get('ToPort', 65535)
                # Extract all IP address ranges allowed through this rule (e.g., 0.0.0.0/0)
                ip_ranges = [ip['CidrIp'] for ip in perm.get('IpRanges', [])]
                
                formatted_rules.append({
                    "from_port": from_port,
                    "to_port": to_port,
                    "ip_ranges": ip_ranges
                })
                
            normalized.append({
                "resource_id": sg['GroupId'],
                "resource_name": sg.get('GroupName', 'Unknown'),
                "service": "EC2",
                "type": "SecurityGroup",
                "rules": formatted_rules
            })
            
        return normalized