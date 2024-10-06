import pandas as pd

# List of file paths (You will have to update it with your files)
file_paths = [
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/daily_aqi_by_county_1997.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/daily_aqi_by_county_1998.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/daily_aqi_by_county_1999.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/daily_aqi_by_county_2000.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/daily_aqi_by_county_2001.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/daily_aqi_by_county_2002.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/daily_aqi_by_county_2003.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/daily_aqi_by_county_2004.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/daily_aqi_by_county_2005.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/daily_aqi_by_county_2006.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/daily_aqi_by_county_2007.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/daily_aqi_by_county_2008.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/daily_aqi_by_county_2009.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/daily_aqi_by_county_2010.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/daily_aqi_by_county_2011.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/daily_aqi_by_county_2012.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/daily_aqi_by_county_2013.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/daily_aqi_by_county_2014.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/daily_aqi_by_county_2015.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/daily_aqi_by_county_2016.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/daily_aqi_by_county_2017.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/daily_aqi_by_county_2018.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/daily_aqi_by_county_2019.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/daily_aqi_by_county_2020.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/daily_aqi_by_county_2021.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/daily_aqi_by_county_2022.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/daily_aqi_by_county_2023.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/aqi/daily_aqi_by_county_2024.csv"
    
    # Add all files from 1997 to 2024
]

# Initialize an empty list to store the dataframes
dfs = []

# Read and combine all the CSV files
for file_path in file_paths:
    df = pd.read_csv(file_path)
    dfs.append(df)

# Concatenate all the dataframes into one
combined_df = pd.concat(dfs)

# Convert the 'Date' column to datetime format
combined_df['Date'] = pd.to_datetime(combined_df['Date'])

# Extract the month and year
combined_df['Month'] = combined_df['Date'].dt.month
combined_df['Year'] = combined_df['Date'].dt.year

# Export data for each month (across all years)
for month in range(1, 13):  # 1 to 12 for each month
    month_data = combined_df[combined_df['Month'] == month]
    output_file_path = f'/home/theWizard_m/Desktop/Datathon2024/data/aqi/aqi_by_month_{month:02d}_1997_2024.xlsx'
    month_data.to_excel(output_file_path, index=False)
    print(f"Exported {output_file_path}")

print("All months have been exported.")
