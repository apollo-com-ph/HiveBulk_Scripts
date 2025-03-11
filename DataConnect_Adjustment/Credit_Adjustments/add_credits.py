import requests
import pandas as pd
import base64
import json
import os

# API Configuration
API_URL = "http://10.160.0.84:30000/1.0/kb/credits?autoCommit=true"
USERNAME = "admin"  # Replace with actual username
PASSWORD = "password"  # Replace with actual password

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Killbill-ApiKey": "tenant01",
    "X-Killbill-ApiSecret": "secret01",
    "X-Killbill-CreatedBy": "admin",
    "X-Killbill-Reason": "Adding credit",
    "X-Killbill-Comment": "Manual credit",
    "Authorization": "Basic " + base64.b64encode(f"{USERNAME}:{PASSWORD}".encode()).decode()
}

# CSV File
CSV_FILE = "credits.csv"

# Check if CSV file exists
if not os.path.exists(CSV_FILE):
    print(f"Error: CSV file '{CSV_FILE}' not found.")
    exit(1)

# Read CSV
df = pd.read_csv(CSV_FILE)

# Validate CSV file structure
required_columns = {"accountId", "amount"}
if not required_columns.issubset(df.columns):
    print("Error: CSV file must contain 'accountId' and 'amount' columns.")
    exit(1)

# Initialize log list
log_results = []

# Display header in terminal
print("\nProcessing Credits...")
print("=" * 60)
print(f"{'Account ID':<40} {'Amount':<10} {'Status'}")
print("=" * 60)

# Process each account
for _, row in df.iterrows():
    account_id = row["accountId"]
    amount = row["amount"]

    # Validate amount (ensure it's a positive number)
    if not isinstance(amount, (int, float)) or amount <= 0:
        status = "Failed - Invalid amount"
        log_results.append({"accountId": account_id, "amount": amount, "status": status})
        print(f"{account_id:<40} {amount:<10} {status}")
        continue

    # Prepare API payload
    payload = [{"accountId": account_id, "amount": float(amount)}]  # Ensure amount is a valid float

    try:
        # Send API request
        response = requests.post(API_URL, headers=HEADERS, json=payload)

        # Check response status
        if response.status_code in [200, 201]:
            status = "Success"
        else:
            status = f"Failed - {response.status_code} - {response.text}"

    except requests.exceptions.RequestException as e:
        status = f"Failed - {str(e)}"

    # Print log in terminal
    print(f"{account_id:<40} {amount:<10} {status}")

    # Append to log list
    log_results.append({"accountId": account_id, "amount": amount, "status": status})

# Save log results to a CSV file
log_df = pd.DataFrame(log_results)
log_df.to_csv("credit_log.csv", index=False)

print("\nProcess completed. Log saved as 'credit_log.csv'.")
