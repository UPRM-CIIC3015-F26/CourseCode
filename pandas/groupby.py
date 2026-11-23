# import
import pandas as pd

# Read csv file
df = pd.read_csv("cafe_sales.csv")

# Creating a new column "revenue"

# Clean data first
clean_data = df.dropna()

# Create column
clean_data["revenue"] = clean_data["units"] * clean_data["price"]

print("Print dataframe after adding new column (first 5 rows)")
print(clean_data.head())

# Group by category 
# Get total sum of revenue
print("Total revenue by category")
print(clean_data.groupby("category")["revenue"].sum())

# Get total sum of units and revenue
print("Total units and revenue by category")
print(clean_data.groupby("category")[["units", "revenue"]].sum())

# Group by item 
# Get max of units sold
print("Maximum price sold per item")
print(clean_data.groupby("item")["price"].max())

# Get average of units sold and price per item
print("Maximum units sold per item")
print(clean_data.groupby("item")[["units", "price"]].mean())


# Export results to a csv. Exporting the revenue per item
revenue_per_item = clean_data.groupby("item")["revenue"].sum()
revenue_per_item.to_csv("revenue_per_cafe_item.csv")

# Aggregates like min, max, average (Getting multiple statistics at once)
print("Get mean, max, min and median of revenue per item")
print(clean_data.groupby("item")["revenue"].agg(["mean", "max", "min", "median"]))
