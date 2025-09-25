import sqlite3
import pandas as pd

def top_customers(min_invoice=1):
    try:
        # Kết nối CSDL
        conn = sqlite3.connect('../databases/Chinook_Sqlite.sqlite')
        cursor = conn.cursor()
        # Truy vấn: join Customer + Invoice
        query = f"""
            SELECT 
                c.CustomerId,
                c.FirstName || ' ' || c.LastName AS CustomerName,
                COUNT(i.InvoiceId) AS InvoiceCount,
                SUM(i.Total) AS TotalAmount
            FROM Customer c
            JOIN Invoice i ON c.CustomerId = i.CustomerId
            GROUP BY c.CustomerId
            HAVING COUNT(i.InvoiceId) >= {min_invoice}
            ORDER BY InvoiceCount DESC, TotalAmount DESC;
        """

        # Đọc vào DataFrame
        df = pd.read_sql_query(query, conn)

        return df

    except sqlite3.Error as e:
        print("Lỗi SQLite:", e)
    finally:
        if conn:
            conn.close()


#Ví dụ chạy: lấy khách hàng có ít nhất 3 Invoice
df_customers = top_customers(min_invoice=3)
print(df_customers)