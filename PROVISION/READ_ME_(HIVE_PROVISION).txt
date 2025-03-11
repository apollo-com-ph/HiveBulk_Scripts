** Install Python (if not installed) **

Download from python.org
Check "Add Python to PATH" during installation
Verify installation:


python --version

** Install Required Library **

pip install requests


** Prepare Your CSV File (accounts.csv) **

Create accounts.csv in the same folder as the script
Example format:

subscriberAccountNumber,subscriberName,provision,packageType
RES-202103-14054,Eduave, Sam Kresser,hiveconnect,SP220K12M
RES-202103-14055,Doe, John,hiveconnect,SP220K12M


*** Run the Script ***

Open Command Prompt/Terminal
Navigate to the script folder using cd
Run the script:

python bulk_provision.py
(Use python3 if needed)

***Check the Output ***

The script will print results in the terminal
Results are saved in provisioning_results.csv

Prepared By: Charina Castillano