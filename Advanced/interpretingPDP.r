# Load necessary library
library(dplyr)

# Read the input file
input_file <- "C:/Users/mille/Documents/Rowdy Datathon 2024/Datathon2024/USDA_PDP_AnalyticalResults.csv"
data <- read.csv(input_file)

# Define a dictionary for converting "Commodity" codes to full product names
commodity_dict <- c(
  "BY" = "barley",
  "CB" = "corn",
  "CD" = "corn",
  "CO" = "corn",
  "CS" = "corn",
  "CY" = "corn",
  "OA" = "oat",
  "PB" = "peanut",
  "RI" = "rice",
  "SY" = "soybean",
  "YF" = "soybean",
  "IS" = "sweet potato",
  "SW" = "sweet potato",
  "WF" = "wheat",
  "WH" = "wheat"            # Add more mappings as needed
)

# Convert "Commodity" to full product names in all lower case
data <- data %>%
  mutate(State = substr(Sample.ID, 1, 2),
         Year = as.numeric(substr(Sample.ID, 3, 4)),
         Month = as.numeric(substr(Sample.ID, 5, 6)),
         Day = as.numeric(substr(Sample.ID, 7, 8)),
         Commodity = tolower(commodity_dict[Commod]))

# Reorder columns to place the new columns immediately after "Sample ID"
data <- data %>%
  select(Sample.ID, State, Year, Month, Day, Commod, Commodity, everything())

# Count the number of observations that contain "imidacloprid" in the "Pesticide Name" column
imidacloprid_count <- sum(grepl("imidacloprid", data$Pesticide.Name, ignore.case = TRUE))
Chlorpyrifos_count <- sum(grepl("Chlorpyrifos", data$Pesticide.Name, ignore.case = TRUE))

# Calculate the percentage of the whole dataset
imidacloprid_percentage <- (imidacloprid_count / nrow(data)) * 100
chlorpyrifos_percentage <- (Chlorpyrifos_count / nrow(data)) * 100

# Display the percentage
print(paste("Percentage of observations containing 'imidacloprid':", imidacloprid_percentage, "%"))
print(paste("Percentage of observations containing 'Chlorpyrifos':", chlorpyrifos_percentage, "%"))

# Display the top 5 frequency values of "Pesticide Names"
top_pesticides <- data %>%
  count(Pesticide.Name) %>%
  arrange(desc(n)) %>%
  head(5)

print("Top 5 Pesticide Names by frequency:")
print(top_pesticides)

# Filter the data for specific Test.Class values
filtered_data <- data %>% 
  filter(Test.Class %in% c("A", "O", "C"))

# Get unique Pesticide.Name values
unique_pesticides <- unique(filtered_data$Pesticide.Name)

# Print the unique values
print("Unique Pesticide Names when Test.Class is 'A', 'O', or 'C':")
print(unique_pesticides)

# Count unique Pesticide.Name values for each Test.Class group
unique_counts <- filtered_data %>%
  group_by(Test.Class) %>%
  summarise(unique_pesticides_count = n_distinct(Pesticide.Name))

# Print the counts
print("Number of unique Pesticide Names in each Test.Class group ('A', 'O', 'C'):")
print(unique_counts)

# Save the modified data frame to a new file
output_file <- 'C:/Users/mille/Documents/Rowdy Datathon 2024/Datathon2024/PDPmodified.csv'
write.csv(data, output_file, row.names = FALSE)
