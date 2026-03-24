# @title Domyślny tekst tytułu
import pandas as pd

# 1. Wczytanie danych
df = pd.read_csv("Online_Retail.csv", encoding="ISO-8859-1")

df.head()
df.info()

# 2. Czyszczenie danych

# usunięcie braków CustomerID
df = df.dropna(subset=["CustomerID"])

# usunięcie anulowanych transakcji
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]

# usunięcie błędnych wartości
df = df[df["Quantity"] > 0]
df = df[df["UnitPrice"] > 0]

# konwersja daty
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# usunięcie duplikatów
df = df.drop_duplicates()

# dodanie Revenue
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

df.head()