import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("/home/theWizard_m/Desktop/Datathon2024/data/monarch_data/monarch_data_all.csv")

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Ensure the 'State' column exists and filter relevant states
states_of_interest = ['TX', 'ME', 'NY', 'RI', 'OK', 'NC', 'SC', 'GA', 'AL', 'VA', 
                      'MS', 'FL', 'WI', 'IA', 'KY', 'WV', 'AR', 'MI', 'OH', 'TN', 
                      'PA', 'CT', 'IN', 'IL', 'VT']
df_filtered = df[df['State/Province'].isin(states_of_interest)]

# Create a strip plot with states on the y-axis and time on the x-axis


# Show the plot
#plt.show()

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Extract the year and month from the date for easier plotting
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

# Filter the relevant states
states_of_interest = ['TX', 'ME', 'NY', 'RI', 'OK', 'NC', 'SC', 'GA', 'AL', 'VA', 
                      'MS', 'FL', 'WI', 'IA', 'KY', 'WV', 'AR', 'MI', 'OH', 'TN', 
                      'PA', 'CT', 'IN', 'IL', 'VT']
df_filtered = df[df['State/Province'].isin(states_of_interest)]

### Box Plot ###

### Box Plot ###
### Strip Plot ###
plt.figure(figsize=(12, 8))
sns.stripplot(x='Date', y='State/Province', data=df_filtered, jitter=True, palette='Set1')
plt.title('Monarch Sightings by State Over Time')
plt.xlabel('Date')
plt.ylabel('State')
plt.xticks(rotation=45)
plt.tight_layout()
# plt.show()  # Display the strip plot

### Box Plot ###
plt.figure(figsize=(12, 8))
sns.boxplot(x='State/Province', y='Number', data=df_filtered)
plt.title('Box Plot: Monarch Sightings by State')
plt.xlabel('State')
plt.ylabel('Number of Monarch Sightings')
plt.xticks(rotation=45)
plt.ylim(0, 20)  # Adjusted y-axis as requested
plt.tight_layout()
# plt.show()  # Display the box plot

### Histogram ###
plt.figure(figsize=(12, 8))
sns.histplot(data=df_filtered, x='State/Province', hue='Month', multiple='stack', bins=30)
plt.title('Histogram: Distribution of Monarch Sightings by State')
plt.xlabel('State')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.tight_layout()
# plt.show()  # Display the histogram

### Heatmap ###
plt.figure(figsize=(12, 8))
# Create pivot table for the heatmap (count of sightings by state and year)
heatmap_data = df_filtered.pivot_table(index='State/Province', columns='Year', values='Number', aggfunc='sum')
sns.heatmap(heatmap_data, cmap="YlGnBu", annot=True, fmt=".0f")  # Show numeric values
plt.title('Heatmap: Monarch Sightings by State and Year')
plt.xlabel('Year')
plt.ylabel('State')
plt.tight_layout()
plt.show()  # Display the heatmap
