import pandas as pd
import matplotlib.pyplot as plt

file_path = "chipotle.tsv"

df = pd.read_csv(file_path, sep="\t")
print("Số dòng, số cột:", df.shape)
print(df.head())

df["item_price"] = df["item_price"].str.replace("$", "", regex=False).astype(float)

products_over_10 = df.loc[df["item_price"] > 10, "item_name"].drop_duplicates()

print("\nCác sản phẩm có giá > 10$: ")
print(products_over_10)

sorted_products = df["item_name"].drop_duplicates().sort_values()

print("\nDanh sách sản phẩm sắp xếp theo tên:")
print(sorted_products)

max_price = df["item_price"].max()
most_expensive_products = df.loc[df["item_price"] == max_price, "item_name"].drop_duplicates()

print("\nSản phẩm có giá cao nhất:")
print("Giá:", max_price)
print(most_expensive_products)

veggie_df = df[df["item_name"] == "Veggie Salad Bowl"]

num_orders = veggie_df["order_id"].nunique()
total_quantity = veggie_df["quantity"].sum()

print("\nVeggie Salad Bowl:")
print("Số đơn hàng xuất hiện:", num_orders)
print("Tổng số lượng được đặt:", total_quantity)

top5_items = (
    df.groupby("item_name")["quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

plt.figure(figsize=(8, 5))
plt.bar(top5_items.index, top5_items.values)
plt.title("Top 5 Products Purchased Most Frequently")
plt.xlabel("Product Name")
plt.ylabel("Purchase Frequency")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.show()

items_per_order = df.groupby("order_id")["quantity"].sum()

plt.figure(figsize=(8, 5))
plt.scatter(items_per_order.index, items_per_order.values)
plt.title("Number of Items Ordered per Order")
plt.xlabel("Order ID")
plt.ylabel("Total Quantity")
plt.tight_layout()
plt.show()
