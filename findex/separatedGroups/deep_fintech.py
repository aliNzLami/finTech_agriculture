import pandas as pd
import os

def analyze_deep_fintech():
    print("Loading online payment users...")
    file_name = "online_payment_users.xlsx"

    if not os.path.exists(file_name):
        print(f"Error: {file_name} not found.")
        return

    df = pd.read_excel(file_name)

    # Deep Digital condition:
    # We consider them "Deep Digital" if they do ANY of the following:
    # 1. merchantpay_dig == 1 (Made a digital merchant payment)
    # 2. pay_utilities == 1 (Paid a utility bill)
    # 3. fin26a == 1 (Used mobile/computer for bill payment)
    # 4. fin26b == 1 (Used mobile/internet to buy online)
    
    condition_deep = (
        (df['merchantpay_dig'] == 1) | 
        (df['pay_utilities'] == 1) | 
        (df['fin26a'] == 1) | 
        (df['fin26b'] == 1)
    )

    df_deep = df[condition_deep]
    df_shallow = df[~condition_deep]

    def print_profile(df, name):
        print(f"\n--- Profile: {name} (Total: {len(df)}) ---")
        if len(df) == 0:
            print("No cases found for this group.")
            return
            
        mean_inc = df['inc_q'].dropna().mean()
        pct_saved = (df['saved'].dropna() == 1).mean() * 100
        pct_borrowed = (df['borrowed'].dropna() == 1).mean() * 100
        
        print(f"Average Income Quintile (1-5): {mean_inc:.2f}")
        print(f"Saved Money in Past Year (%): {pct_saved:.2f}%")
        print(f"Took a Formal Loan (%): {pct_borrowed:.2f}%")

    print_profile(df_deep, "Deep Digital Users (Multiple Activities)")
    print_profile(df_shallow, "Shallow Digital Users (Agriculture Only)")

if __name__ == "__main__":
    analyze_deep_fintech()
