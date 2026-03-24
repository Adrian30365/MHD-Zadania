# łączenie z wymiarami
fact = df.merge(dim_customer, on=["CustomerID", "Country"])
fact = fact.merge(dim_product, on=["StockCode", "Description"])
fact = fact.merge(dim_date, on=["InvoiceDate"])

# wybór kolumn do fact table
fact_sales = fact[[
    "customer_key",
    "product_key",
    "date_key",
    "Quantity",
    "Revenue"
]]

fact_sales.head()