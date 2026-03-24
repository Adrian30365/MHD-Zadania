# DimCustomer
dim_customer = df[["CustomerID", "Country"]].drop_duplicates().reset_index(drop=True)
dim_customer["customer_key"] = dim_customer.index + 1

# DimProduct
dim_product = df[["StockCode", "Description"]].drop_duplicates().reset_index(drop=True)
dim_product["product_key"] = dim_product.index + 1

# DimDate
dim_date = df[["InvoiceDate"]].drop_duplicates().reset_index(drop=True)
dim_date["date_key"] = dim_date.index + 1
dim_date["Year"] = dim_date["InvoiceDate"].dt.year
dim_date["Month"] = dim_date["InvoiceDate"].dt.month
dim_date["Day"] = dim_date["InvoiceDate"].dt.day