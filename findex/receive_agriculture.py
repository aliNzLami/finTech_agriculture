import pandas as pd
import os
import zipfile

# Define zip and output file names
zip_file = "findex_data.xlsx.zip"
input_file = "findex_data.xlsx.csv"
output_account = "agriculture_into_account.xlsx"
output_cash = "agriculture_in_cash.xlsx"

def split_findex_data():
    # 1. Extract the zip file if it exists
    if os.path.exists(zip_file):
        print(f"Extracting {zip_file}...")
        try:
            with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                zip_ref.extractall(".") 
            print("Extraction successful.")
        except Exception as e:
            print(f"Error extracting zip: {e}")
            return
    elif not os.path.exists(input_file):
        print(f"Error: Neither {zip_file} nor {input_file} found.")
        return

    # 2. Load the extracted dataset
    print(f"Loading {input_file}...")
    df = pd.read_excel(input_file, engine='openpyxl')

    target_col = 'receive_agriculture'
    if target_col not in df.columns:
        print(f"Error: Column '{target_col}' not found in the dataset.")
        return

    # 3. Filter the data
    # Drop rows with missing values for the target column
    df_clean = df.dropna(subset=[target_col])
    
    # Keep only values 1 (account) and 2 (cash)
    df_filtered = df_clean[df_clean[target_col].isin([1, 2])]
    
    # Split into two groups
    df_account = df_filtered[df_filtered[target_col] == 1]
    df_cash = df_filtered[df_filtered[target_col] == 2]

    # 4. Save to new Excel files
    df_account.to_excel(output_account, index=False)
    df_cash.to_excel(output_cash, index=False)

    # 5. Print summary results to GitHub Actions logs
    print("\n--- Data Split Complete ---")
    print(f"Total original rows: {len(df)}")
    print(f"Valid agricultural payment responses: {len(df_filtered)}")
    print(f"Group 1 (Into an account): {len(df_account)}")
    print(f"Group 2 (In cash only): {len(df_cash)}")

if __name__ == "__main__":
    split_findex_data()
