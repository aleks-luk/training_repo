import pandas as pd
df = pd.read_csv('./data/OPD_Crimes.csv')

print(df.head(10).to_markdown())
print('-------------------------------------------------------\n')
# 1. How many unique case numbers (Case Number) are there in the data?
unique_case_numbers = df['Case Number'].nunique()

# 2. What are the most common offense categories (Case Offense Category)?
common_offense_categories = df['Case Offense Category'].value_counts()

# 3. What percentage of crimes are related to "Theft"?
thefts_crime = df['Case Offense Category'] == 'Theft'
thefts_crime_count = df[thefts_crime].shape[0]
thefts_crime_percantage = round(thefts_crime_count / df.shape[0] * 100,2)
print((thefts_crime_percantage))

# 4. Which crime location (Case Location) appears most frequently?
location_counts = df['Case Location'].value_counts()
most_frequent_location = location_counts.idxmax()
most_frequent_count = location_counts.max()
print(location_counts)
print(most_frequent_location)
print(most_frequent_count)

# 5. What are the most common types of offenses (Case Offense Type) related to the "Assault" category?
# 5.1
filtered_df = df[df['Case Offense Category'] == 'Assault']
filtered_df_query = df.query("`Case Offense Category` == 'Assault'")
most_common_type = filtered_df['Case Offense Type'].value_counts()
print(most_common_type.head(10).to_markdown())

# 5.2
most_common_type = df[df['Case Offense Category'] == 'Assault'].groupby('Case Offense Type').size().idxmax()
print(most_common_type)

# 5.3
most_common_type = df[df['Case Offense Category'] == 'Assault']['Case Offense Type'].mode()[0]
print(most_common_type)

# 6. What is the average number of crimes per neighborhood (Orlando Neighborhoods)?
crimes_per_neighborhood = df.groupby(by='Orlando Neighborhoods').size()
crimes_per_neighborhood_df = crimes_per_neighborhood.reset_index(name='Number of Crimes')
print(crimes_per_neighborhood_df.to_markdown())

# 7. What is the distribution of case statuses (Status) in the data?
status_distribution = df['Status'].value_counts()
print(status_distribution.to_markdown())

# 8. How many cases resulted in an arrest (Case Disposition = Arrest)?
arrest_cases = df[df['Case Disposition'] == 'Arrest'].shape[0]
print(arrest_cases)

# 9. Is there a relationship between offense location type (Case Offense Location Type) and offense type (Case Offense Type)?
offense_location_relationship = pd.crosstab(df['Case Offense Location Type'], df['Case Offense Type'])
print(offense_location_relationship)

# 10. Which neighborhoods (Orlando Neighborhoods) have the highest number of reported crimes?
top_neighborhoods = df['Orlando Neighborhoods'].value_counts().head(5)
print(top_neighborhoods)

# 11. What is the average time to close cases (Case Disposition) based on case date (Case Date Time)?
df['Case Date Time'] = pd.to_datetime(df['Case Date Time'], errors='coerce')
closed_cases = df[df['Case Disposition'] == 'Closed']
average_closing_time = closed_cases['Case Date Time'].mean()
print(average_closing_time)

# 12. How many cases are related to areas within the "Orlando Main Street Program Area"?
main_street_cases = df['Orlando Main Street Program Area'].notna().sum()
print(main_street_cases)
print(df['Orlando Main Street Program Area'].count())

# 13. Which commissioner districts (Orlando Commissioner Districts) have the highest crime rates?
top_commissioner_districts = df['Orlando Commissioner Districts'].value_counts().head(5)
print(top_commissioner_districts)

# 14. Are there differences in the types of crimes between different types of offense locations (Case Offense Location Type)?
offense_location_comparison = pd.crosstab(df['Case Offense Location Type'], df['Case Offense Category'])
print(offense_location_comparison)

# 15. How many crimes occurred in specific locations compared to unknown locations (Location)?
amount_of_unknown_locations = df['Location'].isna().sum()
amount_of_known_locations = (~df['Location'].isna()).sum()
print(amount_of_known_locations)
print(amount_of_unknown_locations)


# 16. What is the average time between reported case dates (difference between Case Date Time)?
time_differences = df['Case Date Time'].sort_values().diff().mean()
print(time_differences)

# 17. What is the distribution of offenses by charge types (Case Offense Charge Type)?
offenses_by_charge_types = df['Case Offense Charge Type'].value_counts()
print(offenses_by_charge_types)

# 18. What percentage of cases have an unknown location (Location = NaN)?
amount_of_unknown_locations = df['Location'].isna().sum()
total_cases = len(df)
unknown_location_percetage = round(amount_of_unknown_locations / total_cases * 100, 2)
print(unknown_location_percetage)

# 19. What percentage of "Robbery" cases were closed (Case Disposition = Closed)?
total_closed_robbery = len(df[(df['Case Offense Category'] == 'Robbery') & (df['Case Disposition'] == 'Closed')])
total_robbery_cases = len(df[df['Case Offense Category'] == 'Robbery'])
percentage_robbery_case_closed = round(total_closed_robbery / total_robbery_cases * 100, 2)
print(percentage_robbery_case_closed)

# 20. What are the most common types of offenses for each case status (Status)?
offense_by_status_grouped = df.groupby(['Status', 'Case Offense Type']).size().reset_index(name='Count')
most_common_offenses = offense_by_status_grouped.sort_values(by=['Status', 'Count'], ascending=[True, False])
top_3_offenses_per_status = most_common_offenses.groupby('Status').head(3)
print(top_3_offenses_per_status)

# 21. What is the median number of crimes in locations that belong to the "Orlando Main Street Program Area"?
median_crimes_main_street = df[df['Orlando Main Street Program Area'].notna()]['Case Location'].value_counts().median()
print(median_crimes_main_street)

# 22. What are the three most frequently committed crimes in neighborhoods with the highest crime rates?
top_neighborhoods = df['Orlando Neighborhoods'].value_counts().head(3).index
top_crimes_in_neighborhoods = df[df['Orlando Neighborhoods'].isin(top_neighborhoods)]['Case Offense Type'].value_counts().head(3)
print(top_crimes_in_neighborhoods)
