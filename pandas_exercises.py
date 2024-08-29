import pandas as pd

df = pd.read_csv('./data/Mcdonalds.csv')

# 1. Check how many missing values there are in each column.
missing_values = df.isnull().sum()

# 2. Remove all rows that have missing values.
df_cleaned = df.dropna()

# 3. Change the data type of the 'Calories' column to float.
df['Calories'] = df['Calories'].astype(float)

# 4. Create a new column 'Calories per Serving' that calculates the number of calories per gram of serving (Calories/Serving Size).
df['Calories per Servin'] = df['Calories']/df['Serving Size'].str.extract(r'(\d+)')[0].astype(int)

# 5. Filter the data to show only the items that have more than 500 kcal.
df_filtered = df[df['Calories'] > 500]

# 6. Sort the data by the 'Calories' column in ascending order.
df_sorted = df_filtered.sort_values(by='Calories')

# 7. Group the data by 'Category' and calculate the average calorie value for each category.
category_avg_calories = df.groupby('Category')['Calories'].mean()

# 8. Find the item with the highest 'TotalFat' content.
max_fat_item = df.loc[[df['TotalFat'].idxmax()]]

# 9. Find the item with the highest 'TotalFat' content within each category.
highest_fat_categories = df.groupby(by='Category')['Calories'].idxmax()

# 10. Display all items that contain less than 10g of fat ('TotalFat').
low_fat_items = df[df['TotalFat'] < 10]

# 11. Count the number of products in each category.
products_count_by_category = df['Category'].value_counts()

# 12. Count the number of unique product categories in the data.
unique_categories_count = df['Category'].nunique()

# 13. Create a new column 'Fat to Protein Ratio' that calculates the ratio of fat to protein ('TotalFat'/'Protein').
df['Fat to Protein Ratio'] = df['TotalFat'] / df['Protein']

# 14. Replace all values in the 'Category' column with uppercase letters.
df['Category'] = df['Category'].str.upper()

# 15. Filter the data to show only items that belong to the 'Breakfast' category.
breakfast_items = df[df['Category'] == 'Breakfast']

# 16. Sum the calorie value for each category.
calories_sum_by_category = df.groupby('Category')['Calories'].sum()

# 17. Display all items whose name ('Item') contains the word "Chicken".
chicken_items = df[df['Item'].str.contains('Chicken', case=False)]

# 18. Calculate the average sodium ('Sodium') value for each product category.
avg_sodium_by_category = df.groupby('Category')['Sodium'].mean()

mean_sodium_agg = df.groupby(by='Category').agg(SodiumAvg=('Sodium', 'mean'))

# 19. Add a 'Healthy' column that has the value True if the product has fewer than 300 kcal and less than 10g of fat.
df['Healthy'] = (df['Calories'] < 300) & (df['TotalFat'] < 10)

# 20. Display the first 10 rows sorted by the percentage of vitamin C ('Vitamin C (% Daily Value)') in descending order.
sorted_first_10 = df.sort_values(by='Vitamin C (% Daily Value)', ascending=False).head(10)

# 21. Calculate the total number of calories for each category ('Category').
total_calories_by_category = df.groupby('Category')['Calories'].sum()

overall_summed_calories = df.groupby(by='Category').agg(TotalCalories=('Calories', 'sum'))

# 22. Calculate the maximum protein ('Protein') content in each category ('Category').
max_protein_by_category = df.groupby('Category')['Protein'].max()

max_protein = df.groupby(by='Category').agg(MaxProtein=('Protein', 'max'))

# 23. Calculate the average sugar ('Sugars') and dietary fiber ('Dietary Fiber') content for each category ('Category').
avg_sugar_fiber_by_category = df.groupby('Category')[['Sugars', 'Dietary Fiber']].mean()

mean_sugar_fiber = df.groupby(by='Category').agg(
    MeanSugar=('Sugars', 'mean'),
    MeanFiber=('Dietary Fiber', 'mean')
)

# 24. Count the number of products in each category ('Category').
product_count_by_category = df.groupby('Category').size()

# 25. Group the data by 'Category' and 'Calories', then find the minimum fat content ('TotalFat') in each group.
min_fat_by_group = df.groupby(['Category', 'Calories'])['TotalFat'].min()

min_fat_grouped = df.groupby(by=['Category', 'Calories'])['TotalFat'].min()

# 26. Group the data by 'Category' and calculate the sum of vitamin A and C (% Daily Value) for each category.
vitamin_sum_by_category = df.groupby('Category')[['Vitamin A (% Daily Value)', 'Vitamin C (% Daily Value)']].sum()

df['VitaminsSum'] = df['Vitamin A (% Daily Value)'] + df['Vitamin C (% Daily Value)']
sum_results = df.groupby(by='Category').agg(
    VitaminsSumAC=('VitaminsSum', 'sum'))

# 28. Using 'loc', display all columns for the item named 'Big Mac'.
big_mac_details = df.loc[df['Item'] == 'Big Mac']

# 29. Using 'loc', change the value of the 'Category' column to 'Lunch' for items containing 'Burger' in the name.
df.loc[df['Item'].str.contains('Burger', case=False), 'Category'] = 'Lunch'

# 30. Using 'loc', display the product name and calorie count for all items that have less than 400 kcal and more than 15g of protein.
low_cal_high_protein_items = df.loc[(df['Calories'] < 400) & (df['Protein'] > 15), ['Item', 'Calories']]

# 31. Using 'loc', assign a value of 0 to the 'Sugars' column for all items that have less than 1g of sugar.
df.loc[df['Sugars'] < 1, 'Sugars'] = 0

# 32. Using 'loc', display all columns for the item named 'Chicken McNuggets' with a calorie content below 300.
mc_nuggets_details = df_cleaned.loc[(df_cleaned['Item'] == 'Chicken McNuggets') & (df_cleaned['Calories'] < 300)]
