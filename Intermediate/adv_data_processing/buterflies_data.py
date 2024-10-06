# Spring and Fall file paths
spring_files = [
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/spring_monarch_by_month_01_1997_2024.xlsx",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/spring_monarch_by_month_02_1997_2024.xlsx",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/spring_monarch_by_month_03_1997_2024.xlsx",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/spring_monarch_by_month_04_1997_2024.xlsx",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/spring_monarch_by_month_05_1997_2024.xlsx",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/spring_monarch_by_month_06_1997_2024.xlsx",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/spring_monarch_by_month_07_1997_2024.xlsx",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/spring_monarch_by_month_08_1997_2024.xlsx",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/spring_monarch_by_month_09_1997_2024.xlsx",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/spring_monarch_by_month_10_1997_2024.xlsx",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/spring_monarch_by_month_11_1997_2024.xlsx",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/spring/spring_monarch_by_month_12_1997_2024.xlsx"
]

fall_files = [
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/fall/fall_monarch_by_month_01_1997_2024.xlsx",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/fall/fall_monarch_by_month_02_1997_2024.xlsx",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/fall/fall_monarch_by_month_03_1997_2024.xlsx",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/fall/fall_monarch_by_month_04_1997_2024.xlsx",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/fall/fall_monarch_by_month_05_1997_2024.xlsx",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/fall/fall_monarch_by_month_06_1997_2024.xlsx",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/fall/fall_monarch_by_month_07_1997_2024.xlsx",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/fall/fall_monarch_by_month_08_1997_2024.xlsx",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/fall/fall_monarch_by_month_09_1997_2024.xlsx",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/fall/fall_monarch_by_month_10_1997_2024.xlsx",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/fall/fall_monarch_by_month_11_1997_2024.xlsx",
    "/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/fall/fall_monarch_by_month_12_1997_2024.xlsx"
]

# Function to map the list of files into a dictionary with month as the key
def files_to_dict(file_list):
    month_dict = {}
    for file in file_list:
        # Extract month from the file path (assumes it's the two-digit number before the year)
        month = file.split('_')[-3]
        month_dict[month] = file
    return month_dict

# Create dictionaries for spring and fall
spring_dict = files_to_dict(spring_files)
fall_dict = files_to_dict(fall_files)

# Print or use the dictionaries
# print("Spring Dictionary:", spring_dict)
# print("Fall Dictionary:", fall_dict)


