import pandas as pd

# List of file paths for all the AQI files
file_paths = [
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/aqi_daily/daily_aqi_by_county_1997.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/aqi_daily/daily_aqi_by_county_1998.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/aqi_daily/daily_aqi_by_county_1999.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/aqi_daily/daily_aqi_by_county_2000.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/aqi_daily/daily_aqi_by_county_2001.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/aqi_daily/daily_aqi_by_county_2002.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/aqi_daily/daily_aqi_by_county_2003.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/aqi_daily/daily_aqi_by_county_2004.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/aqi_daily/daily_aqi_by_county_2005.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/aqi_daily/daily_aqi_by_county_2006.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/aqi_daily/daily_aqi_by_county_2007.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/aqi_daily/daily_aqi_by_county_2008.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/aqi_daily/daily_aqi_by_county_2009.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/aqi_daily/daily_aqi_by_county_2010.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/aqi_daily/daily_aqi_by_county_2011.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/aqi_daily/daily_aqi_by_county_2012.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/aqi_daily/daily_aqi_by_county_2013.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/aqi_daily/daily_aqi_by_county_2014.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/aqi_daily/daily_aqi_by_county_2015.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/aqi_daily/daily_aqi_by_county_2016.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/aqi_daily/daily_aqi_by_county_2017.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/aqi_daily/daily_aqi_by_county_2018.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/aqi_daily/daily_aqi_by_county_2019.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/aqi_daily/daily_aqi_by_county_2020.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/aqi_daily/daily_aqi_by_county_2021.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/aqi_daily/daily_aqi_by_county_2022.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/aqi_daily/daily_aqi_by_county_2023.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/aqi_daily/daily_aqi_by_county_2024.csv"
]

# List of states you are interested in
states_of_interest = [
    'Texas', 'Maine', 'New York', 'Rhode Island', 'Oklahoma', 'North Carolina', 'South Carolina', 
    'Georgia', 'Alabama', 'Virginia', 'Mississippi', 'Florida', 'Wisconsin', 'Iowa', 
    'Kentucky', 'West Virginia', 'Arkansas', 'Michigan', 'Ohio', 'Tennessee', 
    'Pennsylvania', 'Connecticut', 'Indiana', 'Illinois', 'Vermont'
]

# Initialize an empty list to store the dataframes
dfs = []

# Loop over file paths and read each CSV file into a dataframe
for file_path in file_paths:
    df = pd.read_csv(file_path)  # Use file_path (not file_paths) to load each file individually
    dfs.append(df)

# Concatenate all the dataframes into a single dataframe
combined_df = pd.concat(dfs)

# Filter the dataframe to only include the specified states
combined_df_filtered = combined_df[combined_df['State Name'].isin(states_of_interest)]

# Sorting by 'State' and 'Date'
combined_df_sorted = combined_df_filtered.sort_values(by=['State Name', 'Date'])

# Exporting each state's data to separate Excel files
for state in states_of_interest:
    state_df = combined_df_sorted[combined_df_sorted['State Name'] == state]
    output_file_path = f'/home/theWizard_m/Desktop/Datathon2024/data/aqi/aqi_by_state/{state}_aqi.xlsx'
    state_df.to_excel(output_file_path, index=False)
    print(f"File saved for {state}: {output_file_path}")

print("All states have been processed and saved.")
