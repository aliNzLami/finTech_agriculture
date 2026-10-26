import pandas as pd
import os

# Define file names
input_file = "italy_case/database.xlsx"
output_users = "italy_case/blockchain_users.xlsx"
output_non_users = "italy_case/blockchain_non_users.xlsx"

def process_data():
    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found. Check the file path.")
        return

    # Load the Excel file
    print(f"Loading {input_file}...")
    df = pd.read_excel(input_file)
    
    target_col = 'q11_7blockchain'
    
    # Check if the column exists
    if target_col not in df.columns:
        print(f"Error: Column '{target_col}' missing from the dataset.")
        return

    # Drop rows where the blockchain column is empty (NaN)
    initial_count = len(df)
    df_clean = df.dropna(subset=[target_col])
    dropped_count = initial_count - len(df_clean)
    
    if dropped_count > 0:
        print(f"Dropped {dropped_count} rows with missing blockchain data.")

    # Split the data based on the codebook values
    # 2 = selected (users), 1 = not selected (non-users)
    df_users = df_clean[df_clean[target_col] == 2]
    df_non_users = df_clean[df_clean[target_col] == 1]

    # Export to Excel files
    df_users.to_excel(output_users, index=False)
    df_non_users.to_excel(output_non_users, index=False)

    # Print summary statistics
    print("\n--- Export Complete ---")
    print(f"Blockchain users: {len(df_users)} (Saved to {output_users})")
    print(f"Blockchain non-users: {len(df_non_users)} (Saved to {output_non_users})")
    
    valid_total = len(df_users) + len(df_non_users)
    if valid_total > 0:
        adoption_rate = (len(df_users) / valid_total) * 100
        print(f"Adoption rate in this sample: {adoption_rate:.2f}%")

if __name__ == "__main__":
    process_data()
