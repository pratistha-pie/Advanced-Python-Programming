# Write a Python program to find the number of unique paths in a grid using Dynamic Programming.
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
dp = [[1 for j in range(cols)] for i in range(rows)]
for i in range(1, rows):
    for j in range(1, cols):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
print("Total number of unique paths:", dp[rows-1][cols-1])
