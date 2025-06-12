import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
try:
    df = pd.read_csv("sample_online_sales_clean.csv")
except Exception as e:
    print(f"Error loading CSV: {e}")
print("Column names in the DataFrame:")
print(df.columns)
print("First 5 rows of the dataset:")
print(df.head())
df.columns = df.columns.str.strip()
print("\nMissing values in each column:")
print(df.isnull().sum())
print("\nData types before conversion:")
print(df.dtypes)
if 'order_date' in df.columns and 'ship_date' in df.columns:
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')  
    df['ship_date'] = pd.to_datetime(df['ship_date'], errors='coerce')  
else:
    print("Columns 'order_date' or 'ship_date' do not exist in the DataFrame.")
df.drop_duplicates(inplace=True)
print("\nData types after conversion:")
print(df.dtypes)
plt.figure(figsize=(8,5))
sns.barplot(data=df, x='category', y='sales', estimator=sum, ci=None)
plt.title('Total Sales by Category')
plt.ylabel('Sales')
plt.xlabel('Category')
plt.show()
plt.figure(figsize=(8,5))
sns.barplot(data=df, x='region', y='profit', estimator=np.mean, ci=None)
plt.title('Average Profit by Region')
plt.ylabel('Average Profit')
plt.xlabel('Region')
plt.show()
if 'order_date' in df.columns:
    df['month'] = df['order_date'].dt.to_period('M')
    monthly_sales = df.groupby('month')['sales'].sum().reset_index()

    plt.figure(figsize=(10,5))
    sns.lineplot(data=monthly_sales, x='month', y='sales')
    plt.title('Monthly Sales Trend')
    plt.xticks(rotation=45)
    plt.ylabel('Sales')
    plt.xlabel('Month')
    plt.tight_layout()
    plt.show()
print(""" Key Insights:
1. Technology is the highest-selling category.
2. The South region yields the highest average profit.
3. Sales peak in the second and fourth quarters, indicating seasonal trends.""")