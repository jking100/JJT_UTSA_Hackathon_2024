import pandas as pd

# List of file paths (add more as needed)
file_paths = [
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/monarch_data_1997_spring.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/monarch_data_1998_spring.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/monarch_data_1999_spring.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/monarch_data_2000_spring.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/monarch_data_2001_spring.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/monarch_data_2002_spring.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/monarch_data_2003_spring.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/monarch_data_2004_spring.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/monarch_data_2005_spring.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/monarch_data_2006_spring.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/monarch_data_2007_spring.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/monarch_data_2008_spring.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/monarch_data_2009_spring.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/monarch_data_2010_spring.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/monarch_data_2011_spring.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/monarch_data_2012_spring.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/monarch_data_2013_spring.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/monarch_data_2014_spring.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/monarch_data_2015_spring.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/monarch_data_2016_spring.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/monarch_data_2017_spring.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/monarch_data_2018_spring.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/monarch_data_2019_spring.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/monarch_data_2020_spring.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/monarch_data_2021_spring.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/monarch_data_2022_spring.csv",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/monarch_data_2023_spring.csv",
    #"/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/monarch_data_2024_spring.csv"
    # Add files from 1998 to 2024
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
    output_file_path = f'/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/spring_monarch_by_month_{month:02d}_1997_2024.xlsx'
    month_data.to_excel(output_file_path, index=False)
    print(f"Exported {output_file_path}")

print("All months have been exported.")