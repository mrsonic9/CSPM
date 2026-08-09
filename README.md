# Cloud Infrastructure Security Posture Assessment & Automated Remediation Tool (Custom CSPM)

**Author:** Muhammad Zubair  
**Language:** Python 3  
**Cloud Provider:** AWS (Amazon Web Services)

## Overview
**CSPM** stands for Cloud Security Posture Management. 

This project is a custom Cloud Infrastructure Security Posture Assessment & Automated Remediation Tool. It is designed to ensure that necessary server ports (such as SSH, RDP, FTP, MySQL, and PostgreSQL) remain secure. The tool automatically scans your cloud environment for critical misconfigurations—like ports left open to the public internet (`0.0.0.0/0`)—reports the findings, and can automatically revoke the dangerous access to secure your infrastructure.

## Features
* **Automated Discovery:** Connects to AWS via `boto3` to extract live Security Group configurations.
* **Data Normalization:** Converts complex cloud JSON payloads into a unified, readable schema.
* **Policy Evaluation:** Scans rules against security best practices to flag publicly exposed critical ports.
* **Interactive CLI Launcher:** User-friendly terminal interface to dynamically select target regions.
* **Automated Reporting:** Generates a clean, professional `complete.csv` spreadsheet of all detected vulnerabilities.
* **Remediation Engine:** Features a default **Dry-Run Mode** for safe simulation, and an **Active Remediation Mode** that executes API calls to instantly close exposed ports.

---

## Step-by-Step Setup Guide

Follow these steps to set up the project on your local machine.

### 1. Prerequisites
* **Python 3.x** installed on your system.
* An **AWS Account** with an IAM User created for programmatic access.
* The IAM User must have the `AmazonEC2ReadOnlyAccess` policy attached (for scanning) and `AmazonEC2FullAccess` (if you wish to use Active Remediation).

### 2. Clone the Repository
```bash
git clone https://github.com/mrsonic9/CSPM.git
```
### 3. Set Up the Virtual Environment
```bash
# Create the virtual environment
python3 -m venv venv

# Activate the virtual environment (Linux/macOS)
source venv/bin/activate
```
### For Windows copy this one
```bash
# Activate the virtual environment (Windows)
# venv\Scripts\activate
```
### 4. Install Dependencies
With your virtual environment active, install the required Python libraries:
```bash
pip install -r requirements.txt
```
### 5. Configure AWS Credentials
Provide your IAM User credentials so the tool can securely connect to your cloud environment. Run the AWS CLI configuration command:
```bash
aws configure
```
You will be prompted to enter:

**AWS Access Key ID:** Your access key
**AWS Secret Access Key:** Your secret key
**Default region name:** (e.g., eu-north-1 or us-east-1)
**Default output format:** json

### Usage
To run the tool, ensure your virtual environment is active and execute the launcher script:
```bash
python launcher.py
```
What to Expect:
Region Selection: The script will prompt you to select your target AWS region.

Mode Selection: You will be asked to choose between Dry-Run Mode (safe) or Active Remediation Mode (modifies live infrastructure).

Execution: The tool will fetch, normalize, and evaluate your security groups.

Results: Vulnerabilities will be printed to the terminal in a clean table, and a complete.csv file will be generated in your project folder containing the full audit report.

### 📁 Project Structure
```Plaintext
cloud-posture-guard/
│
├── core/
│   ├── __init__.py
│   ├── collector.py      # Connects to AWS and gathers raw data
│   ├── normalizer.py     # Converts raw data into a standard format
│   └── evaluator.py      # The rule engine that flags violations
│
├── remediation/
│   ├── __init__.py
│   └── fixer.py          # Executes Dry-Run or Active API fixes
│
├── launcher.py           # The interactive CLI entry point
├── main.py               # The core orchestration logic and CSV exporter
├── requirements.txt      # Python package dependencies
└── README.md             # Project documentation
```
