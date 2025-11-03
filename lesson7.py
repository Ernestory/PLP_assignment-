# ============================================
#   PYTHON DATA ANALYSIS ASSIGNMENT
#   Student Name: [Your Name]
#   Course: Data Analysis with Python
#   Objective: Load, analyze, and visualize a dataset using pandas and matplotlib
# ============================================

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Enable inline plotting (only needed for Jupyter)
%matplotlib inline

# --------------------------------------------
# TASK 1: LOAD AND EXPLORE THE DATASET
# --------------------------------------------

# You can use your own dataset or the Iris dataset from sklearn
from sklearn.datasets import load_iris
iris = load_iris()

# Convert to a pandas DataFrame
df = pd.DataFrame(
    iris.data, 
    columns=iris.feature_names
)
df["species"] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Display the first few rows
print("=== First 5 rows of the dataset ===")
print(df.head())

# Check info about dataset
print("\n=== Dataset Info ===")
print(df.info())

# Check for missing values
print("\n=== Missing Values ===")
print(df.isnull().sum())

# (No missing data in Iris dataset, but example cleaning code:)
# df.fillna(df.mean(), inplace=True)

# --------------------------------------------
# TASK 2: BASIC DATA ANALYSIS
# --------------------------------------------

# Basic statistics
print("\n=== Basic Statistics ===")
print(df.describe())

# Grouping by categorical column (species) and computing mean
group_means = df.groupby("species").mean()
print("\n=== Mean values by species ===")
print(group_means)

# Example insight:
print("\nInsight: Iris-virginica flowers have the largest average petal and sepal sizes.")

# --------------------------------------------
# TASK 3: DATA VISUALIZATION
# --------------------------------------------

# Set visual style
sns.set(style="whitegrid")

# 1️⃣ Line chart – example of sepal length trend (index as pseudo time)
plt.figure(figsize=(8,5))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length", color="blue")
plt.title("Trend of Sepal Length Across Samples")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2️⃣ Bar chart – average petal length per species
plt.figure(figsize=(8,5))
sns.barplot(x="species", y="petal length (cm)", data=df, palette="coolwarm")
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3️⃣ Histogram – distribution of sepal width
plt.figure(figsize=(8,5))
plt.hist(df["sepal width (cm)"], bins=10, color="green", alpha=0.7)
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4️⃣ Scatter plot – relationship between sepal and petal length
plt.figure(figsize=(8,5))
sns.scatterplot(
    x="sepal length (cm)",
    y="petal length (cm)",
    hue="species",
    data=df,
    palette="viridis"
)
plt.title("Sepal Length vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()

# --------------------------------------------
# ADDITIONAL FINDINGS
# --------------------------------------------
print("\n=== Observations ===")
print("1. Sepal and petal length are strongly correlated.")
print("2. Iris-virginica has noticeably larger petals than the other species.")
print("3. Sepal width is less variable compared to sepal length.")
print("4. Clear species separation is visible in scatter plots.")
