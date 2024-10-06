import pandas as pd
import os

# Load the AgCensus data
input_file = "/home/theWizard_m/Desktop/Datathon2024/data/AgCensus_MasterDataFrame.xlsx"
df = pd.read_excel(input_file)

# Directory to save the output files
output_dir = "/home/theWizard_m/Desktop/Datathon2024/data/ag_parced"
os.makedirs(output_dir, exist_ok=True)

# Ensure the 'State' column exists (you may need to adjust the column name if different)
if 'STATE' not in df.columns:
    print("The 'State' column is not found in the data.")
else:
    # Get unique states in the 'State' column
    unique_states = df['STATE'].unique()

    # Loop through each state and save to separate files
    for state in unique_states:
        # Filter the dataframe for the current state
        df_state = df[df['STATE'] == state]

        # Define the output file path
        output_file = os.path.join(output_dir, f"{state}_AgCensus_data.xlsx")

        # Save the filtered dataframe to an Excel file
        df_state.to_excel(output_file, index=False)

        print(f"Data for {state} saved to {output_file}")
