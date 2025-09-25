import pandas as pd


def find_orders_within_range_sorted(df, minValue, maxValue, SortType=True):
    """
    Trả về danh sách các hóa đơn (OrderID + tổng giá trị)
    mà tổng giá trị nằm trong khoảng [minValue, maxValue]
    và sắp xếp theo SortType.

    SortType = True  -> tăng dần
    SortType = False -> giảm dần
    """
    # Tính tổng giá trị cho từng OrderID
    order_totals = df.groupby('OrderID').apply(
        lambda x: (x['UnitPrice'] * x['Quantity'] * (1 - x['Discount'])).sum()
    ).reset_index(name='Sum')

    # Lọc theo khoảng giá trị
    filtered_orders = order_totals[
        (order_totals['Sum'] >= minValue) & (order_totals['Sum'] <= maxValue)
        ]

    # Sắp xếp theo yêu cầu
    filtered_orders = filtered_orders.sort_values(by='Sum', ascending=SortType)

    return filtered_orders


# ------------------- Ví dụ sử dụng -------------------
df = pd.read_csv("dataset/SalesTransactions.csv")

minValue = float(input("Nhập giá trị min: "))
maxValue = float(input("Nhập giá trị max: "))
sortType = input("Nhập SortType (True/False): ").strip().lower() == "true"

result = find_orders_within_range_sorted(df, minValue, maxValue, SortType=sortType)

print("\nDanh sách hóa đơn thỏa điều kiện:")
print(result)