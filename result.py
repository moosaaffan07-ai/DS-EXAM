# SECTION-A

# QUESTION 1:
# Option B.

# QUESTION 2:
# Option B.

# QUETION 3:
# Option C.

# QUESTION 4:
# Option A.

# QUESTION 5;
# Option D.

# QUESTION 6:
# Option B.

# QUESTION 7:
# Option  A.

# QUESTION 8:
# Option C.

# QUESTION 9:
# Option B.

# QUESTION 10:
# Option B.



# SECTION-B

# QUESTION 11:

# a: Sara 80.0
#    Ali 65.0
#    John 90.0

# CALCULATIONS:

# Sara: (75 + 85 + 80) / 3 = 80



# Ali: (60 + 70 + 65) / 3 = 65



# John: (90 + 95 + 85) / 3 = 90

# b:  for name, marks in students.items():
#     average = calculate_average(marks)
#     if average >= 80:
#         print(name, average)


# c: It returns the dictionary's key-value pairs. Here, each pair contains a student's name and their marks.

# d: ZeroDivisionError, because the function tries to divide by zero.


# QUESTION 12:

# a: SELECT c.Name, SUM(o.Amount) AS Total_Amount
#    FROM Customers c
#    JOIN Orders o
#    ON c.CustomerID = o.CustomerID
#    GROUP BY c.CustomerID, c.Name;


# b: SELECT c.Name, SUM(o.Amount) AS Total_Amount
#    FROM Customers c
#    JOIN Orders o
#    ON c.CustomerID = o.CustomerID
#    GROUP BY c.CustomerID, c.Name
#    HAVING SUM(o.Amount) > 3000;


# c: Sara's total = 2000 + 3000 = 5000.

# d: LEFT JOIN — it includes all customers from the left table, even if they have no matching order.


 
# QUESTION 13:

# import numpy as np

# scores = np.array([35, 50, 65, 80, 95])

# mean_score = scores.mean()
# selected = scores[scores >= mean_score]

# print(mean_score)  # 65.0
# print(selected)    # [65 80 95]
# print(selected.size)  # 3


# QUESTION 14:

# import pandas as pd

# df = pd.DataFrame({
#     "Department": ["IT", "HR", "IT", "HR", "IT"],
#     "Salary": [50000, 40000, None, 45000, 40000]
# })

# # a. Count missing values
# print(df.isnull().sum())

# # b. Replace missing salary with the mean
# df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# # c. Calculate mean salary for IT
# it_mean = df[df["Department"] == "IT"]["Salary"].mean()
# print(it_mean)  # 44583.333333...


# SECTION-C

# Q15 = B
# Q16 = D
# Q17 = C
# Q18 = B
# Q19 = B
# Q20 = B
# Q21 = C
# Q22 = B
# Q23 = B
# Q24 = B
# Q25 = B
# Q26 = A
# Q27 = B
# Q28 = B
# Q29 = C


# SECTION-D

# QUESTION 30:

# import pandas as pd

# # a. Load CSV file
# df = pd.read_csv("retail_sales.csv")

# # Display first five rows
# print(df.head())

# # Display column information
# print(df.info())

# # Display missing values
# print(df.isnull().sum())

# # b. Replace missing prices with median
# df["Unit_Price"] = df["Unit_Price"].fillna(
#     df["Unit_Price"].median()
# )

# # c. Calculate sales
# df["Sales"] = df["Quantity"] * df["Unit_Price"]

# # Calculate total sales by category
# category_sales = df.groupby("Category")["Sales"].sum()

# # Sort in descending order
# category_sales = category_sales.sort_values(ascending=False)

# print(category_sales)


# QUESTION 31:

# a: 

# import pandas as pd

# # Load dataset
# df = pd.read_csv("student_performance.csv")

# # Display first five rows
# print(df.head())

# # Check missing values
# print(df.isnull().sum())

# # Calculate correlation
# correlation = df["Study_Hours"].corr(df["Final_Score"])

# print("Correlation:", correlation)


# b:

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression

# # Load dataset
# df = pd.read_csv("student_performance.csv")

# # Input and target
# X = df[["Study_Hours"]]
# y = df["Final_Score"]

# # Split data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# # Create model
# model = LinearRegression()

# # Train model
# model.fit(X_train, y_train)

# # Predict scores
# predictions = model.predict(X_test)

# print("Actual Scores:")
# print(y_test.tolist())

# print("Predicted Scores:")
# print(predictions)

