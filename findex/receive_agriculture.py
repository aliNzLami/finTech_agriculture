import pandas as pd
import os

# Define file names (change 'findex_data.xlsx' to your actual dataset name)
input_file = "findex/findex_data.xlsx"
output_account = "findex/agriculture_into_account.xlsx"
output_cash = "findex/agriculture_in_cash.xlsx"

def split_findex_data():
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    print(f"Loading {input_file}...")
    # Load dataset
    df = pd.read_excel(input_file)

    # Check if column exists
    target_col = 'receive_agriculture'
    if target_col not in df.columns:
        print(f"Error: Column '{target_col}' not found.")
        return

    # Drop missing values (NaN) for this specific column
    initial_count = len(df)
    df_clean = df.dropna(subset=[target_col])
    
    # Filter only values 1 and 2
    df_filtered = df_clean[df_clean[target_col].isin([1, 2])]
    
    # Split based on value 1 (Account) and value 2 (Cash)
    df_account = df_filtered[df_filtered[target_col] == 1]
    df_cash = df_filtered[df_filtered[target_col] == 2]

    # Save to Excel
    df_account.to_excel(output_account, index=False)
    df_cash.to_excel(output_cash, index=False)

    # Print Summary
    print("\n--- Data Split Complete ---")
    print(f"Total original rows: {initial_count}")
    print(f"Valid agricultural payment responses (1 or 2): {len(df_filtered)}")
    print(f"Group 1 (Into an account): {len(df_account)} cases (Saved to {output_account})")
    print(f"Group 2 (In cash only): {len(df_cash)} cases (Saved to {output_cash})")

if __name__ == "__main__":
    split_findex_data()
