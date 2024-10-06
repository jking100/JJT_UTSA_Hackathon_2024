import pandas as pd
import matplotlib.pyplot as plt
import os
import joypy

# List of states you want to generate ridgeline plots for
states_of_interest = ['TX', 'ME', 'NY', 'RI', 'OK', 'NC', 'SC', 'GA', 'AL', 'VA', 
                      'MS', 'FL', 'WI', 'IA', 'KY', 'WV', 'AR', 'MI', 'OH', 'TN', 
                      'PA', 'CT', 'IN', 'IL', 'VT']

# Directory to save the output graphs
output_dir = "/home/theWizard_m/Desktop/Datathon2024/data/monarch_plots/ridgeline_plots"
os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist

# Loop through each state and process the data
for state in states_of_interest:
    # Load the data for the current state (use f-string to format the file path)
    file_path = f"/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/states/combined/combined_monarch_{state}_1997_2024.xlsx"
    try:
        df = pd.read_excel(file_path)

        # Convert 'Date' column to datetime
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

        # Ensure 'Number' column is numeric (convert non-numeric values to NaN)
        df['Number'] = pd.to_numeric(df['Number'], errors='coerce')

        # Drop rows where 'Number' or 'Date' is NaN
        df = df.dropna(subset=['Number', 'Date'])

        # Extract 'Year' and 'Month' from 'Date'
        df['Year'] = df['Date'].dt.year
        df['Month'] = df['Date'].dt.month

        # Ensure 'Month' column contains valid values between 1 and 12
        df = df[df['Month'].between(1, 12)]

        if not df.empty:
            # Create a ridgeline plot for the current state across all years
            plt.figure(figsize=(12, 8))
            
            # Generate the ridgeline plot using joypy (removed invalid argument 'xlabel')
            joypy.joyplot(df, by='Year', column='Month', ylim='own', overlap=1.5, 
                          figsize=(12, 8), title=f'Ridgeline Plot of Monarch Sightings by Year ({state})')

            # Add labels after plot generation
            plt.xlabel('Month')
            plt.ylabel('Year')

            # Save the plot to a file
            output_file = os.path.join(output_dir, f'ridgeline_sightings_{state}_1997_2024.png')
            plt.savefig(output_file)
            plt.close()  # Close the plot to free up memory

            print(f"Ridgeline plot for {state} saved as {output_file}")
        else:
            print(f"No data available for {state}")

    except FileNotFoundError:
        print(f"File not found for state {state}: {file_path}")

print("All ridgeline plots for all states generated successfully.")
