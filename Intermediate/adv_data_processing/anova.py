import pandas as pd
import matplotlib.pyplot as plt
import os

# Load your ANOVA results
anova_by_county_df = pd.read_csv('/home/theWizard_m/Desktop/Datathon2024/data/anova_results_by_county_combined.csv')

# Extract p-values from the 'ANOVA Result' column
anova_by_county_df['p-value'] = anova_by_county_df['ANOVA Result'].str.extract(r'p-value: ([\d\.]+)').astype(float)

# Function to visualize and save p-values per county and per chemical for a given state
def visualize_and_save_pscores_by_county_and_chemical(state_name, output_dir):
    # Filter the data for the selected state
    state_data = anova_by_county_df[anova_by_county_df['State'] == state_name]
    
    # Pivot the data so that chemicals are columns and counties are rows
    state_pivot = state_data.pivot_table(values='p-value', index='County', columns='Chemical')
    
    # Plot the p-values for each county and chemical
    plt.figure(figsize=(14, 8))
    state_pivot.plot(kind='bar', figsize=(14, 8), colormap='viridis')
    plt.title(f'Average P-values (ANOVA) by County and Chemical in {state_name}')
    plt.xlabel('County')
    plt.ylabel('P-value')
    plt.xticks(rotation=90)
    plt.tight_layout()
    
    # Save the plot
    output_file = os.path.join(output_dir, f'{state_name}_pvalues_by_county_chemical.png')
    plt.savefig(output_file)
    print(f'Saved plot for {state_name} to {output_file}')
    plt.close()

# Example usage: Save the plots for all states
output_directory = '/home/theWizard_m/Desktop/Datathon2024/data/anova_graph'  # Replace with the directory where you want to save the plots
os.makedirs(output_directory, exist_ok=True)

# Loop through all the states in your dataset and save the plots
for state_name in anova_by_county_df['State'].unique():
    visualize_and_save_pscores_by_county_and_chemical(state_name, output_directory)
