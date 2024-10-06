# Load required libraries
library(dplyr)
library(tidyr)
library(writexl)
library(readxl)

# Step 1: Load the Excel data
data <- read_excel("C:/Users/mille/Documents/Rowdy Datathon 2024/Datathon2024/AgChange/ag_census_single_sheet_v2.xlsx")

# Step 2: Validate column names after "Lat" follow "ABC1234" convention
lat_index <- which(names(data) == "Lat")
columns_after_lat <- names(data)[(lat_index + 1):ncol(data)]

# Regex to validate "ABC1234" format
invalid_columns <- columns_after_lat[!grepl("^[A-Z]{3}\\d{4}$", columns_after_lat, ignore.case = TRUE)]

# Stop execution if any invalid columns are found
if (length(invalid_columns) > 0) {
  stop(paste("Invalid column names:", paste(invalid_columns, collapse = ", ")))
}

# Step 3: Pivot data to create unique combinations of commodity and year
data_long <- data %>%
  pivot_longer(cols = (lat_index + 1):ncol(data), 
               names_to = c("Commodity", "Year"), 
               names_pattern = "(?i)([A-Z]{3})(\\d{4})", 
               values_to = "Value")

# Step 4: Insert "Commodity" and "Year" columns after "Lat"
data_long <- data_long %>%
  relocate(Commodity, Year, .after = Lat)

# Step 5: Load the data dictionary CSV file
data_dict <- read.csv("C:/Users/mille/Documents/Rowdy Datathon 2024/Datathon2024/AgChange/Data_Dictionary.csv")

# Step 6: Replace "Commodity" values with "Full Name" using the data dictionary
data_long <- data_long %>%
  left_join(data_dict, by = c("Commodity" = "Abbreviation")) %>%
  mutate(Commodity = Full.Name) %>%
  select(-Full.Name)

# Step 7: Split the data by "STATE" into separate sheets
split_data <- split(data_long, data_long$STATE)

# Step 8: Write each split dataframe to separate sheets in a new Excel file
write_xlsx(split_data, "C:/Users/mille/Documents/Rowdy Datathon 2024/Datathon2024/AgChange/output_data_by_state.xlsx")
