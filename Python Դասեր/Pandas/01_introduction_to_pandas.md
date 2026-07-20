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

It is commonly used alongside:

- NumPy for numeric computation,
- Matplotlib and Seaborn for visualization,
- Scikit-learn for machine learning,
- Statsmodels for statistical modeling.

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

A common convention is to import pandas as `pd`.

## 4. Core pandas objects

pandas has two most important data structures:

### 4.1 Series

A Series is a one-dimensional labeled array. It is similar to a column in a spreadsheet or a single column in a database table.

```python
s = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
print(s)
```

A Series has:

- values,
- an index,
- a dtype.

### 4.2 DataFrame

A DataFrame is a two-dimensional table with rows and columns. It is the most commonly used pandas object.

```python
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["Yerevan", "Tbilisi", "Baku"]
})
print(df)
```

A DataFrame is like a spreadsheet, but better because it is programmable, reproducible, and powerful.

### 4.3 Index

The Index is the labels that define the row or column positions. It is not just a simple list; it gives pandas powerful alignment and lookup capabilities.

```python
idx = pd.Index(["a", "b", "c"])
print(idx)
```

## 5. Creating data structures

### 5.1 From Python lists

```python
s = pd.Series([1, 2, 3, 4])
df = pd.DataFrame([[1, 2], [3, 4]], columns=["x", "y"])
```

### 5.2 From dictionaries

```python
data = {
    "product": ["Laptop", "Phone", "Tablet"],
    "price": [1000, 700, 400]
}

products = pd.DataFrame(data)
print(products)
```

### 5.3 From NumPy arrays

```python
arr = np.array([[1, 2], [3, 4]])
df = pd.DataFrame(arr, columns=["A", "B"])
print(df)
```

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

These commands help you quickly understand the structure of your data.

## 7. Selecting and accessing data

### 7.1 Accessing a column

```python
df["name"]
```

### 7.2 Accessing a row by label

```python
df.loc[1]
```

### 7.3 Accessing a single value

```python
df.loc[0, "name"]
```

### 7.4 Filtering rows

```python
filtered = df[df["score"] > 85]
print(filtered)
```

This is one of the most common operations in pandas.

## 8. Basic arithmetic and column creation

You can create new columns from existing ones.

```python
sales = pd.DataFrame({
    "price": [10, 20, 30],
    "quantity": [2, 3, 1]
})

sales["revenue"] = sales["price"] * sales["quantity"]
print(sales)
```

This is a very common pattern in data transformation.

## 9. Aggregation basics

pandas can quickly summarize data.

```python
df = pd.DataFrame({
    "category": ["A", "A", "B", "B"],
    "value": [10, 20, 30, 40]
})

print(df.groupby("category")["value"].sum())
print(df.groupby("category")["value"].mean())
```

Groupby is one of the most powerful concepts in pandas and will appear throughout the course.

## 10. Reading data from files

One of the most common tasks in pandas is reading tabular data from external files.

```python
from io import StringIO

csv_data = StringIO("name,age,city\nAlice,25,Yerevan\nBob,30,Tbilisi\nCharlie,35,Baku\n")
df = pd.read_csv(csv_data)
print(df)
```

In real projects, you would often read from CSV files on disk:

```python
df = pd.read_csv("data.csv")
```

## 11. A beginner-friendly workflow

A common first workflow in pandas is:

1. load data,
2. inspect its structure,
3. select the relevant columns,
4. filter rows,
5. create derived columns,
6. summarize the results.

Example:

```python
df = pd.DataFrame({
    "customer": ["A", "B", "C", "D"],
    "spent": [100, 200, 50, 300],
    "region": ["North", "South", "North", "South"]
})

summary = (
    df.groupby("region")["spent"]
      .sum()
      .sort_values(ascending=False)
)
print(summary)
```

## 12. Algorithms & Under the Hood

### 12.1 Vectorization

pandas is fast because it is built around vectorized operations. Instead of processing each element one-by-one in Python, pandas performs operations on whole arrays or blocks of data.

For example:

```python
s = pd.Series([1, 2, 3, 4])
print(s * 2)
```

This works efficiently because the multiplication is applied to the entire array, rather than looping manually in Python.

### 12.2 Why this matters

Manual loops are often slow because Python has interpreter overhead for each iteration. Vectorization reduces that overhead and leverages highly optimized low-level code.

### 12.3 Index alignment

pandas aligns data by index automatically.

```python
s1 = pd.Series([10, 20], index=["a", "b"])
s2 = pd.Series([1, 2], index=["b", "a"])
print(s1 + s2)
```

This is powerful because it allows you to combine datasets without manually reordering them.

### 12.4 Time complexity of common operations

- Accessing a single element by position: approximately $O(1)$
- Filtering rows with a condition: $O(n)$
- Sorting values: $O(n \log n)$
- Grouping and aggregation: often $O(n)$ to $O(n \log n)$ depending on the operation
- Merging two tables: often close to $O(n + m)$ for simple joins, but can grow depending on the join strategy

### 12.5 Memory considerations

pandas stores data in a columnar-like structure and uses efficient block types under the hood. A DataFrame is not just a list of Python objects; it is optimized for repeated operations over columns.

Important memory ideas:

- using appropriate dtypes reduces memory usage,
- object dtype is flexible but often slower and more memory-heavy,
- converting large numeric columns to `int64` or `float64` can improve performance,
- avoiding unnecessary copies is important in large datasets.

## 13. Best practices for beginners

- use meaningful column names,
- inspect data early,
- avoid using Python loops when a pandas method already exists,
- prefer vectorized operations over manual iteration,
- keep a clear workflow: load -> inspect -> transform -> analyze.

## 14. Exercises

### Easy

1. Create a Series named `temperatures` with the values `[20, 22, 19, 24]` and an index of `["Mon", "Tue", "Wed", "Thu"]`.
2. Create a DataFrame named `students` with columns `name`, `score`, and `city` using the following rows:
   - Alice, 88, Yerevan
   - Bob, 76, Tbilisi
   - Charlie, 95, Baku
3. Print the first 2 rows of `students`.
4. Filter `students` to keep only students with `score >= 85`.

### Medium

1. Create a DataFrame called `sales` with columns `product`, `price`, `quantity`, and `region` using the following rows:
   - Laptop, 1000, 2, North
   - Phone, 700, 3, South
   - Tablet, 400, 5, North
   - Headphones, 200, 4, South
2. Add a new column called `revenue` equal to `price * quantity`.
3. Compute the total revenue by region.
4. Sort the result in descending order of total revenue.

### VERY HARD

1. Create a DataFrame called `customers` with the following messy data:
   - customer_id: `1001, 1002, 1001, 1003, 1004`
   - customer_name: `" alice ", "Bob", "Alice", " carol ", "dave "`
   - country: `"armenia", "georgia", "ARMENIA", "", "azerbaijan"`
   - age: `25, "", 30, 40, 35`
   - salary: `5000, 6500, "", 7800, 9000`
2. Clean the data by:
   - trimming whitespace from names and countries,
   - standardizing country names to uppercase,
   - converting age and salary to numeric types,
   - filling missing ages with the median age,
   - filling missing salaries with the median salary,
   - removing duplicate rows based on `customer_id`.
3. Create a new column `segment` using age ranges:
   - `0-25` → `Young`
   - `26-40` → `Adult`
   - `41+` → `Senior`
4. Compute the average salary by country and segment.

## 15. Solutions

### Easy solution

```python
import pandas as pd

temperatures = pd.Series([20, 22, 19, 24], index=["Mon", "Tue", "Wed", "Thu"])

students = pd.DataFrame(
    {
        "name": ["Alice", "Bob", "Charlie"],
        "score": [88, 76, 95],
        "city": ["Yerevan", "Tbilisi", "Baku"],
    }
)

print(temperatures)
print(students.head(2))
print(students[students["score"] >= 85])
```

This solution uses a Series for labeled numeric data and a DataFrame for tabular data. The filtering step is fully vectorized and idiomatic.

### Medium solution

```python
import pandas as pd

sales = pd.DataFrame(
    {
        "product": ["Laptop", "Phone", "Tablet", "Headphones"],
        "price": [1000, 700, 400, 200],
        "quantity": [2, 3, 5, 4],
        "region": ["North", "South", "North", "South"],
    }
)

sales["revenue"] = sales["price"] * sales["quantity"]
summary = (
    sales.groupby("region", as_index=False)["revenue"]
    .sum()
    .sort_values("revenue", ascending=False)
)
print(summary)
```

This solution is pandas-idiomatic because it creates a derived column and performs grouped aggregation in a single expressive pipeline.

### VERY HARD solution

```python
import pandas as pd
import numpy as np

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
print(customers)
print(result)
```

This is a realistic “data cleaning + transformation + aggregation” workflow. It demonstrates how pandas can handle messy data in a compact, efficient, and readable manner.

## 16. Key takeaways

By the end of this lesson, you should understand:

- what pandas is and why it is essential,
- the difference between Series and DataFrame,
- how to create and inspect data,
- how to select, filter, and aggregate data,
- why vectorization makes pandas fast,
- how pandas supports realistic data cleaning workflows.
