import pandas as pd
import os

def analyze_financials():
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
        
        print(f"\n--- Financial Profile: {group_name} (Total: {len(df)}) ---")
        
        # 1. Average Income Quintile (1 to 5)
        mean_inc = df['inc_q'].dropna().mean()
        print(f"Average Income Quintile (1-5): {mean_inc:.2f}")
        
        # 2. Percentage who Saved (Value 1 = Yes)
        pct_saved = (df['saved'].dropna() == 1).mean() * 100
        print(f"Saved Money in Past Year (%): {pct_saved:.2f}%")
        
        # 3. Percentage who Borrowed (Value 1 = Yes)
        pct_borrowed = (df['borrowed'].dropna() == 1).mean() * 100
        print(f"Borrowed Money in Past Year (%): {pct_borrowed:.2f}%")
        
        # 4. Financial Resilience (fin24b, 1 to 4)
        mean_resilience = df['fin24b'].dropna().mean()
        print(f"Financial Resilience (1-4): {mean_resilience:.2f}")

if __name__ == "__main__":
    analyze_financials()
