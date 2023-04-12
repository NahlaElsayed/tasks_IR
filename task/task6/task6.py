def edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert
                                    dp[i-1][j],        # Remove
                                        dp[i-1][j-1])      # Replace

    operations = []
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            operations.append(('No change', str2[j - 1]))
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i - 1][j - 1] + 1:
            operations.append(('Replace', str2[j - 1]))
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i - 1][j] + 1:
            operations.append(('Delete', ''))
            i -= 1
        elif dp[i][j] == dp[i][j - 1] + 1:
            operations.append(('Insert', str2[j - 1]))
            j -= 1
    while i > 0:
        operations.append(('Delete', ''))
        i -= 1
    while j > 0:
        operations.append(('Insert', str2[j - 1]))
        j -= 1

    return dp[m][n], operations[::-1]
# Example usage
str1 = "abcdef"
str2 = "azced"
distance, operations = edit_distance(str1, str2)
print(f"Minimum number of operations: {distance}")
print("Operations:")
for operation in operations:
    print(f"{operation[0]} {operation[1]}")