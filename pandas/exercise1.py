# import
import pandas as pd

# Read csv file
df = pd.read_csv("cafe_sales.csv")
# print(type(df).__name__)
# print(df)

print(df.head())

items = df["item"]
print(items.head(5))

reduced_view = df[["item", "units"]]
print("Reduced View")
print(reduced_view[:7])

# All items that sold 3 units or more
print("Sold 3 or more")
soldThreeOrMore = df.loc[df["units"] >= 3, ["item", "units"]]
print(soldThreeOrMore[:7])

# Filtering NaN
nanRows = df.isna()
print(nanRows)
notNaNRows = df.notna()
print(notNaNRows)

# Removing invalid values
valid_sales = df.dropna()
print(valid_sales[:7])

print(f"Shape before drop: {df.shape}")
print(f"Shape after drop: {valid_sales.shape}")

valid_sales["revenue"] = valid_sales["units"] * valid_sales["price"]
print("Revenue")
print(valid_sales.head(7))
# Get the revenue of all items that have sold 2 or more units
rev_of_items_sold_2_or_more = valid_sales.loc[valid_sales["units"] >= 2,["item", "units", "revenue"]]
print("Revenue of items that sold 2 or more")
print(rev_of_items_sold_2_or_more)

total_sales_per_category = valid_sales.groupby("category")["revenue"].sum()
print("Total sales per Category")
print(total_sales_per_category)

total_sales_per_category.to_csv("total_cafe_revenue.csv")