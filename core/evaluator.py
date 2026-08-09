class PolicyEvaluator:
    def __init__(self):
        # Define high-risk ports that should never be open to 0.0.0.0/0
        self.risky_ports = {
            22: "SSH (Remote Administration)",
            3389: "RDP (Remote Desktop)",
            21: "FTP (Unencrypted File Transfer)",
            3306: "MySQL Database",
            5432: "PostgreSQL Database"
        }

    def evaluate_security_groups(self, normalized_sgs):
        """Scans normalized security groups for open ports exposing risk to 0.0.0.0/0."""
        print("[*] Running Policy Evaluator against security groups...")
        violations = []

        for sg in normalized_sgs:
            sg_id = sg['resource_id']
            sg_name = sg['resource_name']

            for rule in sg['rules']:
                from_port = rule['from_port']
                to_port = rule['to_port']
                ip_ranges = rule['ip_ranges']

                # Check if the rule exposes access to the entire internet (0.0.0.0/0)
                if "0.0.0.0/0" in ip_ranges:
                    # Check if any risky port falls within this rule's range
                    for port, description in self.risky_ports.items():
                        if from_port <= port <= to_port:
                            violations.append({
                                "severity": "HIGH",
                                "resource_id": sg_id,
                                "resource_name": sg_name,
                                "issue": f"Exposed {description} (Port {port}) to the public internet (0.0.0.0/0)",
                                "rule_details": rule
                            })
                            
        return violations