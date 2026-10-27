import pandas as pd

def print_demographics():
    print("Loading datasets...")
    df_account = pd.read_excel("agriculture_into_account.xlsx")
    df_cash = pd.read_excel("agriculture_in_cash.xlsx")

    def calculate_stats(df, name):
        print(f"\n--- Profile: {name} ---")
        
        # 1. Mean Age
        mean_age = df['age'].dropna().mean()
        print(f"Average Age: {mean_age:.2f}")
        
        # 2. Percentage Female (Value 1)
        pct_female = (df['female'].dropna() == 1).mean() * 100
        print(f"Female (%): {pct_female:.2f}%")
        
        # 3. Percentage Tertiary Education (Value 3)
        pct_tertiary = (df['educ'].dropna() == 3).mean() * 100
        print(f"Tertiary Education or more (%): {pct_tertiary:.2f}%")
        
        # 4. Percentage Urban (Value 2)
        pct_urban = (df['urbanicity'].dropna() == 2).mean() * 100
        print(f"Urban Residents (%): {pct_urban:.2f}%")

    # Calculate for both groups
    calculate_stats(df_account, "Into an Account (Digital)")
    calculate_stats(df_cash, "In Cash Only (Traditional)")

if __name__ == "__main__":
    print_demographics()
