r"""
# Lesson 1: Introduction to pandas

## 1. What is pandas?

pandas is one of the most important libraries in the Python data ecosystem. It provides powerful, flexible, and highly expressive tools for working with tabular and time-based data. In practice, pandas is used for:

- loading datasets from CSV, Excel, JSON, SQL, and other sources,
- cleaning and transforming messy data,
- performing exploratory data analysis,
- preparing data for machine learning and visualization,
- building data pipelines and reporting systems.

At a high level, pandas helps you think about data in a structured way: rows, columns, labels, groups, and time-based indexes.

## 2. Why pandas matters in Data Science

pandas sits at the center of many real-world data workflows because it combines the flexibility of spreadsheets with the power and reproducibility of programming.

Compared to raw Python lists and dictionaries, pandas offers:

- tabular data structures that are easier to reason about,
- built-in tools for missing values, filtering, grouping, and merging,
- vectorized operations that are much faster than loops,
- rich support for analysis, transformation, and reporting.

## 3. Installation and setup

If pandas is not installed yet, you can install it using pip:

```bash
pip install pandas
```

You can also install it together with NumPy:

```bash
pip install pandas numpy
```

Once installed, import it in Python:

```python
import pandas as pd
import numpy as np
```

## 4. Core pandas objects

### 4.1 Series

A Series is a one-dimensional labeled array. It is similar to a column in a spreadsheet or a single column in a database table.

### 4.2 DataFrame

A DataFrame is a two-dimensional table with rows and columns. It is the most commonly used pandas object.

### 4.3 Index

The Index is the labels that define the row or column positions. It gives pandas powerful alignment and lookup capabilities.

## 5. Creating data structures

### 5.1 From Python lists

### 5.2 From dictionaries

### 5.3 From NumPy arrays

## 6. Basic inspection of data

When you start working with a dataset, the first step is usually inspection.

```python
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "score": [90, 85, 95],
    "active": [True, False, True]
})

print(df.head())
print(df.tail())
print(df.shape)
print(df.dtypes)
print(df.info())
print(df.describe())
```

## 7. Selecting and accessing data

### 7.1 Accessing a column

### 7.2 Accessing a row by label

### 7.3 Accessing a single value

### 7.4 Filtering rows

## 8. Basic arithmetic and column creation

You can create new columns from existing ones.

## 9. Aggregation basics

pandas can quickly summarize data.

## 10. Reading data from files

One of the most common tasks in pandas is reading tabular data from external files.

## 11. A beginner-friendly workflow

A common first workflow in pandas is:

1. load data,
2. inspect its structure,
3. select the relevant columns,
4. filter rows,
5. create derived columns,
6. summarize the results.

## 12. Algorithms & Under the Hood

### 12.1 Vectorization

pandas is fast because it is built around vectorized operations. Instead of processing each element one-by-one in Python, pandas performs operations on whole arrays or blocks of data.

### 12.2 Why this matters

Manual loops are often slow because Python has interpreter overhead for each iteration. Vectorization reduces that overhead and leverages highly optimized low-level code.

### 12.3 Index alignment

pandas aligns data by index automatically.

### 12.4 Time complexity of common operations

- Accessing a single element by position: approximately $O(1)$
- Filtering rows with a condition: $O(n)$
- Sorting values: $O(n \log n)$
- Grouping and aggregation: often $O(n)$ to $O(n \log n)$ depending on the operation
- Merging two tables: often close to $O(n + m)$ for simple joins, but can grow depending on the join strategy

### 12.5 Memory considerations

pandas stores data in a columnar-like structure and uses efficient block types under the hood. A DataFrame is not just a list of Python objects; it is optimized for repeated operations over columns.

## 13. Best practices for beginners

- use meaningful column names,
- inspect data early,
- avoid using Python loops when a pandas method already exists,
- prefer vectorized operations over manual iteration,
- keep a clear workflow: load -> inspect -> transform -> analyze.

## 14. Exercises

### Easy

1. Create a Series named temperatures with the values [20, 22, 19, 24] and an index of ["Mon", "Tue", "Wed", "Thu"].
2. Create a DataFrame named students with columns name, score, and city using the following rows:
   - Alice, 88, Yerevan
   - Bob, 76, Tbilisi
   - Charlie, 95, Baku
3. Print the first 2 rows of students.
4. Filter students to keep only students with score >= 85.

### Medium

1. Create a DataFrame called sales with columns product, price, quantity, and region using the following rows:
   - Laptop, 1000, 2, North
   - Phone, 700, 3, South
   - Tablet, 400, 5, North
   - Headphones, 200, 4, South
2. Add a new column called revenue equal to price * quantity.
3. Compute the total revenue by region.
4. Sort the result in descending order of total revenue.

### VERY HARD

1. Create a DataFrame called customers with the following messy data:
   - customer_id: 1001, 1002, 1001, 1003, 1004
   - customer_name: " alice ", "Bob", "Alice", " carol ", "dave "
   - country: "armenia", "georgia", "ARMENIA", "", "azerbaijan"
   - age: 25, "", 30, 40, 35
   - salary: 5000, 6500, "", 7800, 9000
2. Clean the data by:
   - trimming whitespace from names and countries,
   - standardizing country names to uppercase,
   - converting age and salary to numeric types,
   - filling missing ages with the median age,
   - filling missing salaries with the median salary,
   - removing duplicate rows based on customer_id.
3. Create a new column segment using age ranges:
   - 0-25 -> Young
   - 26-40 -> Adult
   - 41+ -> Senior
4. Compute the average salary by country and segment.

## 15. Solutions

### Easy solution

### Medium solution

### VERY HARD solution

## 16. Key takeaways

By the end of this lesson, you should understand:

- what pandas is and why it is essential,
- the difference between Series and DataFrame,
- how to create and inspect data,
- how to select, filter, and aggregate data,
- why vectorization makes pandas fast,
- how pandas supports realistic data cleaning workflows.
"""

import pandas as pd
import numpy as np
from io import StringIO


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
sales = pd.DataFrame({"price": [10, 20, 30], "quantity": [2, 3, 1]})
sales["revenue"] = sales["price"] * sales["quantity"]
print("Revenue column:")
print(sales)
print()

# 7. Groupby summary
summary_df = pd.DataFrame({"category": ["A", "A", "B", "B"], "value": [10, 20, 30, 40]})
print("Grouped summary:")
print(summary_df.groupby("category")["value"].sum())
print()

# 8. Reading from a CSV-like string
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
