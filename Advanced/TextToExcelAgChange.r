# Load necessary libraries
library(openxlsx)

# Define the file path
file_path <- "C:/Users/mille/Documents/Rowdy Datathon 2024/Datathon2024/AgChange/AgCensus_MasterDataFrame.txt"

# Read the text file into R
ag_census_data <- read.delim(file_path, header = TRUE, sep = "\t")

# Define the output Excel file path
output_file <- "C:/Users/mille/Documents/Rowdy Datathon 2024/Datathon2024/AgChange/AgCensus_MasterDataFrame.xlsx"

# Write the data to an Excel file
write.xlsx(ag_census_data, output_file)

# Output success message
cat("Data successfully written to Excel file:", output_file, "\n")
