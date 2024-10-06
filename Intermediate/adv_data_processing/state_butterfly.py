import pandas as pd
import os

# List of Excel file paths for the spring monarch data (Jan-Jul)
spring_files = [
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/spring_monarch_by_month_01_1997_2024.xlsx",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/spring_monarch_by_month_02_1997_2024.xlsx",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/spring_monarch_by_month_03_1997_2024.xlsx",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/spring_monarch_by_month_04_1997_2024.xlsx",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/spring_monarch_by_month_05_1997_2024.xlsx",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/spring_monarch_by_month_06_1997_2024.xlsx",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/spring_monarch_by_month_07_1997_2024.xlsx"
]

# List of specific states you're interested in
states_of_interest = [
    'TX', 'ME', 'NY', 'RI', 'OK', 'NC', 'SC', 
    'GA', 'AL', 'VA', 'MS', 'FL', 'WI', 'IA', 
    'KY', 'WV', 'AR', 'MI', 'OH', 'TN', 
    'PA', 'CT', 'IN', 'IL', 'VT'
]

# Initialize an empty list to store the dataframes
dfs = []

# Loop through each file path, load the data, and append to the list
for file_path in spring_files:
    df = pd.read_excel(file_path)
    dfs.append(df)

# Concatenate all the dataframes into one large dataframe
combined_df = pd.concat(dfs, ignore_index=True)

# Ensure the correct column (e.g., 'State/Province') is available
if 'State/Province' not in combined_df.columns:
    print("No 'State/Province' column found. Please ensure there is a column named 'State/Province'.")
else:
    # Filter the dataframe to only include the specified states
    df_filtered = combined_df[combined_df['State/Province'].isin(states_of_interest)]

    # Directory to save the state-separated files
    output_dir = "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/states/spring"
    os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist

    # Get the unique states from the filtered dataframe
    unique_states = df_filtered['State/Province'].unique()

    # Loop through each state and export the data for that state to a separate Excel file
    for state in unique_states:
        # Filter the dataframe for the current state
        df_state = df_filtered[df_filtered['State/Province'] == state]

        # Create a file name based on the state
        output_file = os.path.join(output_dir, f"spring_monarch_{state}_1997_2024.xlsx")

        # Save the filtered dataframe to an Excel file
        df_state.to_excel(output_file, index=False)

        print(f"Data for {state} saved to {output_file}")
