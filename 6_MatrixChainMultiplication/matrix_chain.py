def matrix_chain_order(p):
    n = len(p) - 1
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    bracket = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    bracket[i][j] = k

    return dp[1][n], dp, bracket


def print_optimal_parens(bracket, i, j):
    if i == j:
        return f"M{i}"
    else:
        k = bracket[i][j]
        left = print_optimal_parens(bracket, i, k)
        right = print_optimal_parens(bracket, k + 1, j)
        return f"({left} x {right})"


if __name__ == "__main__":
    p = [10, 20, 30, 40, 30]
    min_ops, dp, bracket = matrix_chain_order(p)
    n = len(p) - 1
    print("Matrix dimensions (p):", p)
    print("Minimum number of multiplications:", min_ops)
    print("Optimal Parenthesization:", print_optimal_parens(bracket, 1, n))
