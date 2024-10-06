import pandas as pd
import matplotlib.pyplot as plt
import os

# Function to calculate the correlation for each county in a state
def calculate_county_correlation(state_df):
    return state_df.groupby('county Name').apply(lambda x: x[['Number', 'AQI']].corr().loc['Number', 'AQI'])

# Function to plot the correlation for a state's counties
def plot_county_correlations(correlations, state_name):
    plt.figure(figsize=(12, 6))
    county_names = correlations.index
    plt.bar(county_names, correlations, color='skyblue')
    plt.title(f'Correlation Between Butterfly Counts and AQI Across Counties in {state_name}')
    plt.xlabel('County')
    plt.ylabel('Correlation Coefficient')
    plt.axhline(0, color='black', linewidth=0.8)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

# Load each state file and process
def process_state_file(file_path, state_name):
    try:
        state_data = pd.read_excel(file_path)
        correlations = calculate_county_correlation(state_data)
        plot_county_correlations(correlations, state_name)
    except Exception as e:
        print(f"Error processing {state_name}: {e}")

# List of all state files with their corresponding paths and names
state_files = {
    'Alabama': '/home/theWizard_m/Desktop/Datathon2024/data/merged_data/super_merged/final_merged_AL_data.xlsx',
    'West Virginia': '/home/theWizard_m/Desktop/Datathon2024/data/merged_data/super_merged/final_merged_WV_data.xlsx',
    'Wisconsin': '/home/theWizard_m/Desktop/Datathon2024/data/merged_data/super_merged/final_merged_WI_data.xlsx',
    'Vermont': '/home/theWizard_m/Desktop/Datathon2024/data/merged_data/super_merged/final_merged_VT_data.xlsx',
    'Virginia': '/home/theWizard_m/Desktop/Datathon2024/data/merged_data/super_merged/final_merged_VA_data.xlsx',
    'Tennessee': '/home/theWizard_m/Desktop/Datathon2024/data/merged_data/super_merged/final_merged_TN_data.xlsx',
    'South Carolina': '/home/theWizard_m/Desktop/Datathon2024/data/merged_data/super_merged/final_merged_SC_data.xlsx',
    'Rhode Island': '/home/theWizard_m/Desktop/Datathon2024/data/merged_data/super_merged/final_merged_RI_data.xlsx',
    'Pennsylvania': '/home/theWizard_m/Desktop/Datathon2024/data/merged_data/super_merged/final_merged_PA_data.xlsx',
    'Oklahoma': '/home/theWizard_m/Desktop/Datathon2024/data/merged_data/super_merged/final_merged_OK_data.xlsx',
    'Ohio': '/home/theWizard_m/Desktop/Datathon2024/data/merged_data/super_merged/final_merged_OH_data.xlsx'
}


# Generalized loop to process each state file
for state_name, file_path in state_files.items():
    process_state_file(file_path, state_name)
