# import
import pandas as pd
# For graphing
import matplotlib.pyplot as plt

# Read csv file
df = pd.read_csv("cafe_sales.csv")

clean = df.dropna()

clean["revenue"] = clean["units"] * clean["price"]

# Get median, median, min and max revenue from rows
print(clean["revenue"].agg(["mean", "median", "max", "min"]))

# Revenue per item
rev_per_item = clean.groupby("item")["revenue"].sum()
print(rev_per_item)

# plot
rev_per_item.plot.bar(rot=0)
plt.title("Total revenue by item")
plt.ylabel("Dollars")
plt.show()
