from core.collector import CloudCollector
from core.normalizer import ResourceNormalizer
from core.evaluator import PolicyEvaluator
import json

def main():
    print("=== Starting Cloud Posture Assessment Tool ===")
    
    # 1. Collect raw data from AWS
    collector = CloudCollector(region_name="eu-north-1")
    raw_sgs = collector.collect_security_groups()
    print(f"[+] Successfully fetched {len(raw_sgs)} security groups from AWS.")
    
    # 2. Normalize the data
    clean_sgs = ResourceNormalizer.normalize_security_groups(raw_sgs)
    
    # 3. Evaluate the security posture (The Brain)
    evaluator = PolicyEvaluator()
    violations = evaluator.evaluate_security_groups(clean_sgs)
    
    # 4. Report the findings
    print(f"\n--- Security Assessment Results ---")
    if violations:
        print(f"[-] Found {len(violations)} security violations!\n")
        print(json.dumps(violations, indent=4))
    else:
        print("[+] No security violations found! Your cloud posture is clean.")

if __name__ == "__main__":
    main()