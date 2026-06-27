# %%

import os

# Check if we're in the right place
print("Current directory:", os.getcwd())

# Check if our data file exists
data_path = "sales-analysis/data/sales.csv"
if os.path.exists(data_path):
    print(f"✅ Found {data_path}")
else:
    print(f"❌ Cannot find {data_path}")
    print("Make sure you're running from the sales-analysis folder!")

# folder ke andr andr jaana then use /
# folder ke baahr jaana then use ../
# eg-

data_path = "../Python/AI/01_requests_and_url.py"
if os.path.exists(data_path):
    print(f"✅ Found {data_path}")
else:
    print(f"❌ Cannot find {data_path}")
    print("Make sure you're running from the sales-analysis folder!")
