import pandas as pd

# Load the dataset (just the filename since we are already inside the folder)
df = pd.read_excel("blockchain_users.xlsx")

# Drop duplicates to get unique farmers (since DCE has 8 rows per person)
unique_farmers = df.drop_duplicates(subset=['RID'])

# Filter: IoT is NOT selected (1 = not selected)
target_group = unique_farmers[unique_farmers['q11_1iot'] == 1]

# Save to a new Excel file
target_group.to_excel("blockchain_no_iot.xlsx", index=False)

# Print results
print(f"Total unique blockchain users: {len(unique_farmers)}")
print(f"Blockchain users without IoT: {len(target_group)}")
print("\nList of RIDs:")
print(target_group['RID'].tolist())
