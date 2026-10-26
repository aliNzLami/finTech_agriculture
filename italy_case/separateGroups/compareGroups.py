import pandas as pd

# Load both files
df_users = pd.read_excel("/italy_case/separateGroups/blockchain_users.xlsx")
df_non_users = pd.read_excel("/italy_case/separateGroups/blockchain_non_users.xlsx")

def get_summary(df, name):
    print(f"\n--- Profile: {name} ---")
    
    # Demographics
    print(f"Average Age: {df['q26age'].mean():.2f}")
    print(f"Average Farm Size (Hectares): {df['q8farm_size'].mean():.2f}")
    print(f"Average Annual Revenue (Euros): {df['q17annual_revenues'].mean():.2f}")
    
    # Education Level (Percentage of Master's degree holders, code 6)
    masters = (df['q27education'] == 6).mean() * 100
    print(f"Master's Degree Holders: {masters:.2f}%")
    
    # Top Barrier: Insufficient Funds (code 2 = selected)
    funds_barrier = (df['q22_1insufficient_funds'] == 2).mean() * 100
    print(f"Reported 'Insufficient Funds' as barrier: {funds_barrier:.2f}%")
    
    # Top Barrier: High Cost (code 2 = selected)
    cost_barrier = (df['q22_2high_cost'] == 2).mean() * 100
    print(f"Reported 'High Cost' as barrier: {cost_barrier:.2f}%")

# Run the comparison
get_summary(df_users, "Blockchain Users")
get_summary(df_non_users, "Non-Users")
