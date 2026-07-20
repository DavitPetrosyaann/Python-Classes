import pandas as pd
import numpy as np

# ==============================
# Lecture code examples
# ==============================

# 1. Creating a Series
s = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
print("Series:")
print(s)
print()

# 2. Creating a DataFrame
students = pd.DataFrame(
    {
        "name": ["Alice", "Bob", "Charlie"],
        "score": [88, 76, 95],
        "city": ["Yerevan", "Tbilisi", "Baku"],
    }
)
print("DataFrame:")
print(students)
print()

# 3. Inspecting data
print("Head:")
print(students.head(2))
print()
print("Shape:")
print(students.shape)
print()
print("Dtypes:")
print(students.dtypes)
print()
print("Info:")
students.info()
print()
print("Describe:")
print(students.describe())
print()

# 4. Selecting a column
print("Column access:")
print(students["name"])
print()

# 5. Filtering rows
filtered = students[students["score"] >= 85]
print("Filtered rows:")
print(filtered)
print()

# 6. Creating a new column
sales = pd.DataFrame(
    {
        "price": [10, 20, 30],
        "quantity": [2, 3, 1],
    }
)
sales["revenue"] = sales["price"] * sales["quantity"]
print("Revenue column:")
print(sales)
print()

# 7. Groupby summary
summary_df = pd.DataFrame(
    {
        "category": ["A", "A", "B", "B"],
        "value": [10, 20, 30, 40],
    }
)
print("Grouped summary:")
print(summary_df.groupby("category")["value"].sum())
print()

# 8. Reading from a CSV-like string
from io import StringIO

csv_data = StringIO("name,age,city\nAlice,25,Yerevan\nBob,30,Tbilisi\nCharlie,35,Baku\n")
read_df = pd.read_csv(csv_data)
print("Read from CSV-like input:")
print(read_df)
print()


# ==============================
# Easy exercise solution
# ==============================

def solve_easy():
    temperatures = pd.Series([20, 22, 19, 24], index=["Mon", "Tue", "Wed", "Thu"])
    students_df = pd.DataFrame(
        {
            "name": ["Alice", "Bob", "Charlie"],
            "score": [88, 76, 95],
            "city": ["Yerevan", "Tbilisi", "Baku"],
        }
    )
    hot_days = temperatures[temperatures > 20]
    high_scorers = students_df[students_df["score"] >= 85]
    return temperatures, students_df, hot_days, high_scorers


# ==============================
# Medium exercise solution
# ==============================

def solve_medium():
    sales = pd.DataFrame(
        {
            "product": ["Laptop", "Phone", "Tablet", "Headphones"],
            "price": [1000, 700, 400, 200],
            "quantity": [2, 3, 5, 4],
            "region": ["North", "South", "North", "South"],
        }
    )
    sales = sales.assign(revenue=sales["price"] * sales["quantity"])
    summary = (
        sales.groupby("region", as_index=False)["revenue"]
        .sum()
        .sort_values("revenue", ascending=False)
    )
    return sales, summary


# ==============================
# VERY HARD exercise solution
# ==============================

def solve_very_hard():
    customers = pd.DataFrame(
        {
            "customer_id": [1001, 1002, 1001, 1003, 1004],
            "customer_name": [" alice ", "Bob", "Alice", " carol ", "dave "],
            "country": ["armenia", "georgia", "ARMENIA", "", "azerbaijan"],
            "age": [25, "", 30, 40, 35],
            "salary": [5000, 6500, "", 7800, 9000],
        }
    )

    customers = customers.copy()
    customers["customer_name"] = customers["customer_name"].astype(str).str.strip().str.title()
    customers["country"] = customers["country"].astype(str).str.strip().str.upper()
    customers["age"] = pd.to_numeric(customers["age"], errors="coerce")
    customers["salary"] = pd.to_numeric(customers["salary"], errors="coerce")

    median_age = customers["age"].median()
    median_salary = customers["salary"].median()

    customers["age"] = customers["age"].fillna(median_age).round(0).astype(int)
    customers["salary"] = customers["salary"].fillna(median_salary)
    customers = customers.drop_duplicates(subset=["customer_id"]).reset_index(drop=True)

    customers["segment"] = pd.cut(
        customers["age"],
        bins=[0, 25, 40, np.inf],
        labels=["Young", "Adult", "Senior"],
        right=True,
    )

    result = (
        customers.groupby(["country", "segment"], as_index=False)["salary"]
        .mean()
        .sort_values(["country", "segment"])
    )
    return customers, result


if __name__ == "__main__":
    temps, students_df, hot_days, high_scorers = solve_easy()
    print("Easy solution:")
    print(temps)
    print(students_df)
    print(hot_days)
    print(high_scorers)
    print()

    sales_df, sales_summary = solve_medium()
    print("Medium solution:")
    print(sales_df)
    print(sales_summary)
    print()

    cleaned_customers, salary_summary = solve_very_hard()
    print("VERY HARD solution:")
    print(cleaned_customers)
    print(salary_summary)
