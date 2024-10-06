library(sf)
library(dplyr)

# Read shapefile using sf
polygons <- st_read(dsn = "C:/Users/mille/Documents/Rowdy Datathon 2024/Datathon2024/AgChange/shapefiles/US_counties_2012_geoid.shp", quiet = TRUE)

# Check column names of polygons
print(colnames(polygons))

# Read agricultural data from text file
con <- file('C:/Users/mille/Documents/Rowdy Datathon 2024/Datathon2024/AgChange/AgCensus_MasterDataFrame.txt', 'r')
ag1 <- readLines(con)
close(con)

# Process the data
ag.data <- t(apply(array(ag1), 1, function(x) { strsplit(x, '\t')[[1]] }))
colnames(ag.data) <- ag.data[1, ]
ag.data <- ag.data[-1, ]

# Convert ag.data to a data frame
ag.data <- as.data.frame(ag.data, stringsAsFactors = FALSE)

# Check column names of ag.data
print(colnames(ag.data))

# Ensure the column names are correct for the join
if (!"FIPS" %in% colnames(polygons)) {
  stop("Column 'FIPS' not found in polygons data")
}
if (!"FIPS" %in% colnames(ag.data)) {
  stop("Column 'FIPS' not found in ag.data")
}

# Merge shapefile data with agricultural data
merged_data <- polygons %>%
  left_join(ag.data, by = "FIPS")

# Convert columns to numeric where possible, excluding the geometry column
numeric_columns <- setdiff(colnames(merged_data), "geometry")
merged_data <- merged_data %>%
  mutate(across(all_of(numeric_columns), ~ as.numeric(.), .names = "converted_{col}"))

# Output success messages
print(noquote('Ag Census data successfully imported!'))
print(noquote(paste('Number of counties:', nrow(merged_data), sep = ' ')))
print(noquote(paste('Number of variables:', ncol(merged_data), sep = ' ')))

# Save the merged data as a CSV file
write.csv(merged_data, 'C:/Users/mille/Documents/Rowdy Datathon 2024/Datathon2024/AgChange/AgCensus_MasterDataFrame.csv', row.names = FALSE)