import pandas as pd
import os

def split_mobile_vs_atm():
    input_file = "agriculture_into_account.xlsx"
    output_online = "online_payment_users.xlsx"
    output_atm = "atm_users.xlsx"

    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    print(f"Loading {input_file}...")
    df = pd.read_excel(input_file)

    # Value 1 = Yes (Mobile Phone)
    df_online = df[df['fin43b'] == 1]
    # Value 2 = No (ATM/Bank/Card)
    df_atm = df[df['fin43b'] == 2]

    df_online.to_excel(output_online, index=False)
    df_atm.to_excel(output_atm, index=False)

    print("\n--- Split Complete ---")
    print(f"Total Account Holders: {len(df)}")
    print(f"Online Payment Users (Mobile): {len(df_online)}")
    print(f"ATM Users (Not Mobile): {len(df_atm)}")

if __name__ == "__main__":
    split_mobile_vs_atm()
