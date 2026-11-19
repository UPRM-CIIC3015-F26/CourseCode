# import
import pandas as pd

# Read csv file
df = pd.read_csv("cafe_sales.csv")


# Read first values
print("Print first few rows of data (default is 5)")
print(df.head())

# Read first 10 values
print("Print first 10 rows of data")
print(df.head(10))

# Read last 10 values
print("Print last 10 rows of data")
print(df.tail(10))

# Get shape
print("Shape of the data frame")
print(df.shape)

# Read only a column
print("Print a specific column")
print(df["item"])

# Read a few rows
print("Print multiple columns")
print(df[["item", "units"]])

# Read unique
print("List unique items")
print(df["item"].unique())