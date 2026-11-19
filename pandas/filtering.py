# import
import pandas as pd

# Read csv file
df = pd.read_csv("cafe_sales.csv")

# Filtering values using .loc[]
print("First 7 items that sold 3 or more")
sold_three_or_more = df.loc[df["units"] >= 3, ["item", "units"]]
print(sold_three_or_more[:7])

# Filtering columns directly [][]
print("First 5 items that sold 5 or more")
sold_five_or_more = df[df["units"] >= 5][["item", "units"]]
print(sold_five_or_more.head(5))

# Using isna and isnotna na = not a number
print("Check if column has values that aren't a valid number")
print(df["units"].isna().head(5))

print("Check if columns has values that are a valid number")
print(df.notna().head(5))

# Using drop na
clean_data = df.dropna()
print("Print first 5 rows of cleaned data and it's new shape")
print(clean_data[:5])
print(clean_data.shape)

# Using fillna
fixed_data = df["units"].fillna(0)
print("Print first 5 rows of fixed data where we replace NaN with 0")
print(fixed_data[:5])
print(fixed_data.shape)