import pandas as pd
import os

def print_demographics():
    print("Loading datasets...")
    
    files = {
        "Online Payment (Mobile)": "online_payment_users.xlsx",
        "ATM / Bank Transfer": "atm_users.xlsx",
        "Cash Only": "agriculture_in_cash.xlsx"
    }

    for group_name, filename in files.items():
        if not os.path.exists(filename):
            print(f"Error: {filename} not found.")
            continue
            
        df = pd.read_excel(filename)
        
        print(f"\n--- Profile: {group_name} (Total: {len(df)}) ---")
        
        # 1. Mean Age
        mean_age = df['age'].dropna().mean()
        print(f"Average Age: {mean_age:.2f}")
        
        # 2. Percentage Tertiary Education (Value 3)
        pct_tertiary = (df['educ'].dropna() == 3).mean() * 100
        print(f"Tertiary Education or more (%): {pct_tertiary:.2f}%")
        
        # 3. Percentage Urban (Value 2)
        pct_urban = (df['urbanicity'].dropna() == 2).mean() * 100
        print(f"Urban Residents (%): {pct_urban:.2f}%")

if __name__ == "__main__":
    print_demographics()
