import csv
import requests
import json

# API URL
API_URL = "http://10.160.0.65:7549/createSubscriberForProvisioning"

# Output file for results
OUTPUT_FILE = "provisioning_results.csv"

# Function to send API request and check response
def provision_account(account_data):
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(API_URL, json=account_data, headers=headers)
        response_data = response.json() if response.status_code == 200 else response.text
        
        status = "Success" if response.status_code == 200 else "Failed"
        print(f"{status}: {account_data['subscriberAccountNumber']} - {response_data}")
        
        return {"status": status, "response": response_data}
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {account_data['subscriberAccountNumber']} - {e}")
        return {"status": "Error", "response": str(e)}

# Read CSV, send requests, and save results
def bulk_provision(csv_filename):
    results = []
    
    with open(csv_filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            account_data = {
                "subscriberAccountNumber": row["subscriberAccountNumber"],
                "subscriberName": row["subscriberName"],
                "provision": row["provision"],
                "packageType": row["packageType"]
            }
            result = provision_account(account_data)
            results.append({**account_data, **result})

    # Save results to CSV
    with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = ["subscriberAccountNumber", "subscriberName", "provision", "packageType", "status", "response"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print(f"\nProvisioning completed. Results saved to {OUTPUT_FILE}")

# Run bulk provisioning
bulk_provision("accounts.csv")
