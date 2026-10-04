import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Task 1: Find best math schools (math score >= 640, sorted descending)
best_math_schools = schools[schools["average_math"] >= 640][
    ["school_name", "average_math"]
].sort_values(by="average_math", ascending=False)

# Task 2: Top 10 performing schools based on total SAT scores
schools["total_SAT"] = (
    schools["average_math"] + schools["average_reading"] + schools["average_writing"]
)
top_10_schools = schools[["school_name", "total_SAT"]].sort_values(
    by="total_SAT", ascending=False
).head(10)

# Task 3: Borough with the highest standard deviation for total SAT score
boroughs = schools.groupby("borough")["total_SAT"].agg(["count", "mean", "std"]).round(2)

# Filter for the borough with maximum standard deviation
largest_std_dev = boroughs[boroughs["std"] == boroughs["std"].max()].reset_index()

# Rename columns to match DataCamp requirements
largest_std_dev = largest_std_dev.rename(
    columns={"count": "num_schools", "mean": "average_SAT", "std": "std_SAT"}
)

# Display results
print("Best Math Schools:")
print(best_math_schools)
print("\nTop 10 Schools:")
print(top_10_schools)
print("\nBorough with Largest Standard Deviation:")
print(largest_std_dev)
