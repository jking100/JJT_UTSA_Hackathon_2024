import pandas as pd
import os

# Load the data from the CSV file
input_file_path = "/home/theWizard_m/Desktop/Datathon2024/data/CORRECT_LLM_monarch_data_us_with_counties.csv"  # Update this to the correct file path
df = pd.read_csv(input_file_path)

# Ensure the column containing state abbreviations exists
if 'State/Province' not in df.columns:
    print("No 'State' column found. Please ensure there is a column named 'State'.")
else:
    # Get the unique state abbreviations
    unique_states = df['State/Province'].unique()

    # Directory to save the state-separated files
    output_dir = "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/states/states2"  # Update to the desired output folder
    os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist

    # Loop through each state and export the data for that state to a separate CSV file
    for state in unique_states:
        # Filter the dataframe for the current state
        df_state = df[df['State/Province'] == state]

        # Create a file name based on the state abbreviation
        output_file = os.path.join(output_dir, f"monarch_data_{state}.csv")

        # Save the filtered dataframe to a CSV file
        df_state.to_csv(output_file, index=False)

        print(f"Data for {state} saved to {output_file}")

print("All state files have been created.")
