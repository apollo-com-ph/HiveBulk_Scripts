1️⃣ Install Python & Dependencies:

Ensure Python is installed (python --version).
Install required libraries:

'pip install requests pandas openpyxl'


2️⃣ Convert Excel File to CSV (If Needed):

Run this Python snippet to convert subscribers.xlsx to subscribers.csv:
python

import pandas as pd
df = pd.read_excel("subscribers.xlsx")
df.to_csv("subscribers.csv", index=False)

3️⃣ Prepare Files:

Place subscribers.csv and create_subscribers.py in the same folder.

4️⃣ Run the Script:

Open a terminal/command prompt and navigate to the script’s folder.
Execute:

'python create_subscribers.py'

5️⃣ Check the Output:

The script will display API responses for each subscriber.