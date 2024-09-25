import pandas as pd

df = pd.read_csv('./data/cars.csv')
df = df.drop(columns=["Images URL's", "Car Profile"])
df = df.replace(r'\n', ' ', regex=True)

# 1. Remove all rows containing NaN values.
df = df.dropna()

# 2. Remove leading and trailing whitespace and newline characters from all text columns.
df = df.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)

# 3. Count and remove duplicate rows, if they exist.
duplicates = df[df.duplicated(keep=False)]
duplicates_count = duplicates.groupby(list(df.columns)).size().reset_index(name='count')
df = df.drop_duplicates()

# 4. Convert column names to lowercase and remove leading/trailing spaces.
df.columns = df.columns.str.lower().str.strip()

# 5. Change the data types of numerical columns (e.g., 'Price', 'Mileage') to appropriate types (e.g., float).
for col in df.columns:
    if df[col].dtype in ['int64', 'float64']:
        df[col] = df[col].astype(int)

# 6. Group the data by 'Make' and calculate the average 'Price' and the count of cars for each make.
results = df.groupby(by='make').agg(
    AvgPrice=('price', 'mean'),
    Count=('make', 'count'))

# 7. Group the data by 'Make', 'Model' and calculate the average 'Price' and average 'Mileage' for each body type.
avg_price_mileage = df.groupby(by=['make', 'model']).agg(
    AvgPrice=('price', 'mean'),
    AvgMileage=("km's driven", 'mean'))

# 8. Group the data by 'FuelType' and calculate the maximum and minimum price for each fuel type.
min_max_fuel_price = df.groupby(by='fuel').agg(
    MinPrice=('price', 'min'),
    MaxPrice=('price', 'max')
)

# 9. Group the data by 'Year' and calculate the number of cars produced in each year.
counted_cars_by_year = df.groupby(by='year').agg(
    count=('year', 'count')
)

# 10. Group the data by the first letter of the 'Make' column and calculate the average price and the count of cars for each group of makes starting with the same letter.
results = df.groupby(by=df['make'].str[0]).agg(
    AvgPrice=('price', 'mean'),
    Count=("make", 'count')
)

# 11. Add a column that shows the difference between a car's price and the average price for its make.
avg_price_by_make = df.groupby('make')['price'].transform('mean')
df['price_diff'] = df['price'] - avg_price_by_make

# 12. Add a column that indicates whether the car's price is above or below the average price for its make.
df['above/below avg'] = df['price_diff'].apply(lambda price: 'above average price' if price > 0 else 'below average price')

# 13. Calculate the total number of cars produced after the year 2015.
results = len(df[df['year'] > 2015])
print(results)

# 14. Calculate the median price of cars for each fuel type.
results = df.groupby(by=df['fuel'])['price'].median()

# 15. Identify cars with mileage greater than 100,000 km and add a corresponding boolean column ('high_mileage').
df['high_mileage'] = df["km's driven"].apply(lambda mileage: mileage > 100000)