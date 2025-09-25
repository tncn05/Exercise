import pandas as pd

def top3_best_selling_products(df):
    # Tính doanh thu theo ProductID
    product_sales = df.groupby('ProductID').apply(lambda x: (x['UnitPrice'] * x['Quantity'] * (1 - x['Discount'])).sum()).reset_index(name='TotalSales')
    # Sắp xếp giảm dần theo doanh thu
    top3_products = product_sales.sort_values(by='TotalSales', ascending=False).head(3)

    return top3_products

df = pd.read_csv("../datasets/SalesTransactions.csv")

result = top3_best_selling_products(df)

print("Top 3 sản phẩm bán ra có giá trị lớn nhất:")
print(result)
