import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# 1. LOAD DATA
# ==========================================

df = pd.read_excel("Ecommerce_Sales_Profit_Analysis_Dataset.xlsx")

print("Original Shape:", df.shape)


# ==========================================
# 2. CHECK DUPLICATES
# ==========================================

print("\nDuplicate Rows:")
print(df.duplicated().sum())


# ==========================================
# 3. CHECK MISSING VALUES
# ==========================================

print("\nMissing Values:")
print(df.isnull().sum())


# ==========================================
# 4. CHECK DATA TYPES
# ==========================================

print("\nData Types:")
print(df.dtypes)


# ==========================================
# 5. CALCULATE PROFIT
# ==========================================

df["Profit"] = df["Sales"] - df["Cost"]


# ==========================================
# 6. CALCULATE PROFIT MARGIN
# ==========================================

df["Profit_Margin"] = (df["Profit"] / df["Sales"]) * 100


# ==========================================
# 7. ROUND PROFIT MARGIN
# ==========================================

df["Profit_Margin"] = df["Profit_Margin"].round(2)


# ==========================================
# 8. DISPLAY NEW COLUMNS
# ==========================================

print("\nUpdated Data:")
print(df.head())


# ==========================================
# 9. BASIC BUSINESS KPIs
# ==========================================

total_sales = df["Sales"].sum()
total_cost = df["Cost"].sum()
total_profit = df["Profit"].sum()
profit_margin = (total_profit / total_sales) * 100


print("\n========== BUSINESS KPIs ==========")

print("Total Sales:", total_sales)
print("Total Cost:", total_cost)
print("Total Profit:", total_profit)
print("Profit Margin:", round(profit_margin, 2), "%")


# ==========================================
# 10. REGION ANALYSIS
# ==========================================

region_analysis = df.groupby("Region").agg(
    Sales=("Sales", "sum"),
    Cost=("Cost", "sum"),
    Profit=("Profit", "sum")
).reset_index()

region_analysis["Profit_Margin"] = (
    region_analysis["Profit"] / region_analysis["Sales"]
) * 100

region_analysis["Profit_Margin"] = region_analysis["Profit_Margin"].round(2)

print("\n========== REGION ANALYSIS ==========")
print(region_analysis.sort_values("Profit", ascending=False))


# ==========================================
# 11. PRODUCT ANALYSIS
# ==========================================

product_analysis = df.groupby("Product").agg(
    Sales=("Sales", "sum"),
    Cost=("Cost", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum")
).reset_index()

product_analysis["Profit_Margin"] = (
    product_analysis["Profit"] / product_analysis["Sales"]
) * 100

product_analysis["Profit_Margin"] = product_analysis["Profit_Margin"].round(2)

print("\n========== PRODUCT ANALYSIS ==========")
print(product_analysis.sort_values("Profit", ascending=False))


# ==========================================
# 12. MONTHLY SALES ANALYSIS
# ==========================================

df["Month"] = df["Order_Date"].dt.month
df["Month_Name"] = df["Order_Date"].dt.strftime("%B")

monthly_sales = df.groupby(["Month", "Month_Name"])["Sales"].sum().reset_index()

monthly_sales = monthly_sales.sort_values("Month")

print("\n========== MONTHLY SALES ==========")
print(monthly_sales)


# ==========================================
# 13. TOP 5 PRODUCTS BY PROFIT
# ==========================================

top_products = product_analysis.sort_values(
    "Profit",
    ascending=False
).head(5)

print("\n========== TOP 5 PRODUCTS ==========")
print(top_products)


# ==========================================
# 14. LOWEST 5 PRODUCTS BY PROFIT
# ==========================================

bottom_products = product_analysis.sort_values(
    "Profit",
    ascending=True
).head(5)

print("\n========== LOWEST 5 PRODUCTS ==========")
print(bottom_products)


# ==========================================
# 15. SAVE CLEANED DATA
# ==========================================

df.to_excel(
    "Ecommerce_Cleaned_Data.xlsx",
    index=False
)

print("\nCleaned file saved successfully!")


# ==========================================
# 16. SALES BY REGION CHART
# ==========================================

plt.figure(figsize=(8, 5))

plt.bar(
    region_analysis["Region"],
    region_analysis["Sales"]
)

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("sales_by_region.png")

plt.show()


# ==========================================
# 17. MONTHLY SALES CHART
# ==========================================

plt.figure(figsize=(10, 5))

plt.plot(
    monthly_sales["Month_Name"],
    monthly_sales["Sales"],
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("monthly_sales_trend.png")

plt.show()

# ==========================================
# 18. CATEGORY ANALYSIS
# ==========================================

category_analysis = df.groupby("Category").agg(
    Sales=("Sales", "sum"),
    Cost=("Cost", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum")
).reset_index()

category_analysis["Profit_Margin"] = (
    category_analysis["Profit"] /
    category_analysis["Sales"]
) * 100

category_analysis["Profit_Margin"] = (
    category_analysis["Profit_Margin"].round(2)
)

print("\n========== CATEGORY ANALYSIS ==========")
print(
    category_analysis.sort_values(
        "Profit",
        ascending=False
    )
)

# ==========================================
# 19. CUSTOMER ANALYSIS
# ==========================================

customer_analysis = df.groupby("Customer").agg(
    Orders=("Order_ID", "count"),
    Sales=("Sales", "sum"),
    Cost=("Cost", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum")
).reset_index()

customer_analysis["Profit_Margin"] = (
    customer_analysis["Profit"] /
    customer_analysis["Sales"]
) * 100

customer_analysis["Profit_Margin"] = (
    customer_analysis["Profit_Margin"].round(2)
)

# Top 10 customers by Sales
top_customers_sales = customer_analysis.sort_values(
    "Sales",
    ascending=False
).head(10)

print("\n========== TOP 10 CUSTOMERS BY SALES ==========")
print(top_customers_sales)


# Top 10 customers by Profit
top_customers_profit = customer_analysis.sort_values(
    "Profit",
    ascending=False
).head(10)

print("\n========== TOP 10 CUSTOMERS BY PROFIT ==========")
print(top_customers_profit)

print("\n========== REGIONAL ANALYSIS ==========")

region_analysis = df.groupby('Region').agg(
    Sales=('Sales', 'sum'),
    Cost=('Cost', 'sum'),
    Profit=('Profit', 'sum'),
    Orders=('Order_ID', 'nunique'),
    Quantity=('Quantity', 'sum')
)

region_analysis['Profit_Margin'] = (
    region_analysis['Profit'] /
    region_analysis['Sales'] * 100
).round(2)

print(region_analysis.sort_values('Sales', ascending=False))

best_region = region_analysis.sort_values(
    'Sales', ascending=False
).head(1)

print("\n========== BEST REGION ==========")
print(best_region)

best_profit_region = region_analysis.sort_values(
    'Profit', ascending=False
).head(1)

print("\n========== MOST PROFITABLE REGION ==========")
print(best_profit_region)

print("\n========== PRODUCT ANALYSIS ==========")

product_analysis = df.groupby('Product').agg(
    Sales=('Sales', 'sum'),
    Cost=('Cost', 'sum'),
    Profit=('Profit', 'sum'),
    Orders=('Order_ID', 'nunique'),
    Quantity=('Quantity', 'sum')
)

product_analysis['Profit_Margin'] = (
    product_analysis['Profit'] /
    product_analysis['Sales'] * 100
).round(2)

print(
    product_analysis
    .sort_values('Sales', ascending=False)
    .head(10)
)

print("\n========== TOP 10 PRODUCTS BY PROFIT ==========")

print(
    product_analysis
    .sort_values('Profit', ascending=False)
    .head(10)
)

df['Order_Date'] = pd.to_datetime(df['Order_Date'])

df['Month'] = df['Order_Date'].dt.to_period('M').astype(str)

print("\n========== MONTHLY SALES ANALYSIS ==========")

monthly_sales = df.groupby('Month').agg(
    Sales=('Sales', 'sum'),
    Cost=('Cost', 'sum'),
    Profit=('Profit', 'sum')
)

monthly_sales['Profit_Margin'] = (
    monthly_sales['Profit'] /
    monthly_sales['Sales'] * 100
).round(2)

print(monthly_sales)

print("\n========== BEST SALES MONTH ==========")

print(
    monthly_sales
    .sort_values('Sales', ascending=False)
    .head(1)
)

print("\n========== OVERALL BUSINESS KPIs ==========")

total_sales = df['Sales'].sum()
total_cost = df['Cost'].sum()
total_profit = df['Profit'].sum()
total_orders = df['Order_ID'].nunique()
total_quantity = df['Quantity'].sum()

profit_margin = (total_profit / total_sales) * 100

print("Total Sales:", total_sales)
print("Total Cost:", total_cost)
print("Total Profit:", total_profit)
print("Total Orders:", total_orders)
print("Total Quantity:", total_quantity)
print("Profit Margin:", round(profit_margin, 2), "%")

with pd.ExcelWriter('Ecommerce_Analysis_Results.xlsx') as writer:

    customer_analysis.to_excel(
        writer,
        sheet_name='Customer Analysis'
    )

    region_analysis.to_excel(
        writer,
        sheet_name='Regional Analysis'
    )

    product_analysis.to_excel(
        writer,
        sheet_name='Product Analysis'
    )

    monthly_sales.to_excel(
        writer,
        sheet_name='Monthly Sales'
    )

print("\nAnalysis results saved successfully!")

