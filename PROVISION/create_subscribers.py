import csv
import requests
import json

# API endpoint
API_URL = "http://10.160.0.65:7549/createSubscriberForMigration"
HEADERS = {'Content-Type': 'application/json'}

# CSV file path
CSV_FILE = "subscribers.csv"

def create_subscriber(data):
    response = requests.post(API_URL, headers=HEADERS, json=data)
    return response.status_code, response.text

def process_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            subscriber_data = {
                "subscriberAccountNumber": row["subscriberAccountNumber"],
                "provision": row["provision"],
                "clientName": row["clientName"],
                "oltReportedUpstream": int(row["oltReportedUpstream"]),
                "oltReportedDownstream": int(row["oltReportedDownstream"]),
                "onuDeviceName": row["onuDeviceName"],
                "packageType": row["packageType"],
                "status": row["status"]
            }
            
            status_code, response_text = create_subscriber(subscriber_data)
            print(f"Account: {subscriber_data['subscriberAccountNumber']} - Status: {status_code} - Response: {response_text}")

if __name__ == "__main__":
    process_csv(CSV_FILE)
