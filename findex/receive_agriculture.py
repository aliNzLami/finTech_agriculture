import pandas as pd
import os

# Define file names
input_file = "findex_data.xlsx"
output_account = "agriculture_into_account.xlsx"
output_cash = "agriculture_in_cash.xlsx"

def split_findex_data():
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    print(f"Loading {input_file}...")
    df = pd.read_excel(input_file)

    target_col = 'receive_agriculture'
    if target_col not in df.columns:
        print(f"Error: Column '{target_col}' not found.")
        return

    df_clean = df.dropna(subset=[target_col])
    df_filtered = df_clean[df_clean[target_col].isin([1, 2])]
    
    df_account = df_filtered[df_filtered[target_col] == 1]
    df_cash = df_filtered[df_filtered[target_col] == 2]

    df_account.to_excel(output_account, index=False)
    df_cash.to_excel(output_cash, index=False)

    print("\n--- Data Split Complete ---")
    print(f"Total original rows: {len(df)}")
    print(f"Valid agricultural payment responses: {len(df_filtered)}")
    print(f"Group 1 (Into an account): {len(df_account)}")
    print(f"Group 2 (In cash only): {len(df_cash)}")

if __name__ == "__main__":
    split_findex_data()
