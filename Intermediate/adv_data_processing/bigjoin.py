import pandas as pd
import os

# List of states with abbreviations and full names
states = {
    'AL': 'Alabama', 'TX': 'Texas', 'ME': 'Maine', 'NY': 'New York', 'RI': 'Rhode Island', 
    'OK': 'Oklahoma', 'NC': 'North Carolina', 'SC': 'South Carolina', 'GA': 'Georgia', 
    'VA': 'Virginia', 'MS': 'Mississippi', 'FL': 'Florida', 'WI': 'Wisconsin', 'IA': 'Iowa', 
    'KY': 'Kentucky', 'WV': 'West Virginia', 'AR': 'Arkansas', 'MI': 'Michigan', 
    'OH': 'Ohio', 'TN': 'Tennessee', 'PA': 'Pennsylvania', 'CT': 'Connecticut', 
    'IN': 'Indiana', 'IL': 'Illinois', 'VT': 'Vermont'
}

# Directory for the output merged data
output_dir = "/home/theWizard_m/Desktop/Datathon2024/data/merged_data/super_merged"
os.makedirs(output_dir, exist_ok=True)

# Loop through each state, load both datasets, and join by county name
for abbrev, state in states.items():
    # Load the first dataset (for example: AL_AgCensus_data.xlsx)
    ag_file_path = f"/home/theWizard_m/Desktop/Datathon2024/data/ag_parced/{abbrev}_AgCensus_data.xlsx"
    merged_file_path = f"/home/theWizard_m/Desktop/Datathon2024/data/merged_data/merged_{abbrev}_data.xlsx"

    try:
        ag_df = pd.read_excel(ag_file_path)
        merged_df = pd.read_excel(merged_file_path)

        # Convert county names to lowercase and strip any extra spaces for both datasets
        ag_df['COUNTY'] = ag_df['COUNTY'].str.lower().str.strip()
        merged_df['county Name'] = merged_df['county Name'].str.lower().str.strip()

        # Merge the datasets on 'county Name' and 'COUNTY' using an inner join
        final_merged_df = pd.merge(merged_df, ag_df, left_on='county Name', right_on='COUNTY', how='inner')

        # Save the final merged dataframe
        output_file = os.path.join(output_dir, f'final_merged_{abbrev}_data.xlsx')
        final_merged_df.to_excel(output_file, index=False)

        print(f"Data for {state} ({abbrev}) merged and saved to {output_file}")

    except FileNotFoundError:
        print(f"File not found for {state} ({abbrev}). Skipping...")

print("All state data merged successfully.")
