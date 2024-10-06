# Load required libraries
library(dplyr)
library(tidyr)
library(writexl)
library(readxl)

# Step 1: Load the "TX" sheet from the Excel data
data <- read_excel("C:/Users/mille/Documents/Rowdy Datathon 2024/Datathon2024/AgChange/output_data_by_state.xlsx", sheet = "TX")

# Step 2: Convert "Year" to numeric
data <- data %>%
  mutate(Year = as.numeric(Year))

# Step 3: Select observations where the value of "Unit" is "proportion of county area"
filtered_data <- data %>%
  filter(Unit == "proportion of county area", Year > 1990)

# Step 4: Group the data by "COUNTY" and then by "Commodity", keeping AREA_KM
grouped_data <- filtered_data %>%
  group_by(COUNTY, Commodity, AREA_KM)

# Step 5: Calculate the likelihood of each crop in a given county
likelihood_data <- grouped_data %>%
  group_by(COUNTY) %>%
  mutate(total_proportion = sum(Value)) %>%
  ungroup() %>%
  mutate(likelihood = Value / total_proportion)

# Step 6: Average the likelihoods over the four years for each county and crop
averaged_likelihood_data <- likelihood_data %>%
  group_by(COUNTY, Commodity, AREA_KM) %>%
  summarize(mean_likelihood = mean(likelihood, na.rm = TRUE), .groups = 'drop')

# Step 7: Adjust likelihood by county size using "AREA_KM"
adjusted_likelihood_data <- averaged_likelihood_data %>%
  mutate(weighted_likelihood = mean_likelihood * AREA_KM)

# Step 8: Create a sampling distribution based on the relative likelihoods among all counties
create_sampling_distribution <- function(crop_name, num_samples = 100) {
  # Step 8.1: Filter for the specified crop and use all counties
  all_counties <- adjusted_likelihood_data %>%
    filter(Commodity == crop_name)  # Use all counties
  
  # Step 8.2: Normalize the weighted likelihoods to create a probability distribution
  all_counties <- all_counties %>%
    mutate(normalized_likelihood = weighted_likelihood / sum(weighted_likelihood))
  
  # Step 8.3: Create a sampling distribution by sampling from all counties based on their likelihood
  sampled_counties <- sample(
    all_counties$COUNTY,   # The counties to sample from
    size = num_samples,    # Number of samples
    replace = TRUE,        # Sampling with replacement
    prob = all_counties$normalized_likelihood  # Probabilities based on normalized likelihoods
  )
  
  return(sampled_counties)
}

# Step 9: Bootstrap to estimate where corn is most likely grown based on sampling distributions
bootstrap_sampling <- function(crop_name, num_bootstrap = 1000, num_samples = 100) {
  # Step 9.1: Initialize a table to store the count of appearances for each county
  county_counts <- data.frame(COUNTY = unique(adjusted_likelihood_data$COUNTY), count = 0)
  
  # Step 9.2: Perform bootstrapping
  for (i in 1:num_bootstrap) {
    # Generate a single sampling distribution
    sampled_counties <- create_sampling_distribution(crop_name, num_samples)
    
    # Count occurrences of each county in the sample and update the count in county_counts
    county_counts <- county_counts %>%
      mutate(count = count + ifelse(COUNTY %in% sampled_counties, 1, 0))
  }
  
  # Step 9.3: Normalize the counts to get probabilities (divide by number of bootstraps)
  county_counts <- county_counts %>%
    mutate(probability = count / num_bootstrap)
  
  # Step 9.4: Return the counties sorted by their estimated probability
  county_counts %>%
    arrange(desc(probability))
}

# Example: Bootstrap to estimate where corn is most likely grown
# corn_bootstrap_results <- bootstrap_sampling("corn", num_bootstrap = 1000, num_samples = 100)
# print(corn_bootstrap_results)


# Step 9: Write the averaged likelihood data to a new Excel file
write_xlsx(averaged_likelihood_data, "C:/Users/mille/Documents/Rowdy Datathon 2024/Datathon2024/AgChange/averaged_likelihood_data.xlsx")

# Print the first 100 rows of the averaged likelihood data
print(head(adjusted_likelihood_data, 100))