# T.C : O(log(n))
# S.C : O(1)


MOD = int(1e9 + 7)

# Function to multiply two matrices
def matrix_multiplication(A, B):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % MOD
    return result

# Function to perform matrix exponentiation (binary exponentiation)
def matrix_exponentiation(base, exponent):
    if exponent == 0:
        identity = [[1, 0], [0, 1]]
        return identity

    half = matrix_exponentiation(base, exponent // 2)
    result = matrix_multiplication(half, half)

    if exponent % 2 == 1:
        result = matrix_multiplication(result, base)

    return result

# Multiply a 2x2 matrix with a 2x1 vector
def multiply_matrix(A, B):
    result = [[0], [0]]
    for i in range(2):
        for j in range(2):
            result[i][0] = (result[i][0] + A[i][j] * B[j][0]) % MOD
    return result

def main():
    n = int(input("Enter n: "))
    
    if n == 0:
        print(f"Fibonacci({n}) = 0")
        return

    T = [[1, 1], [1, 0]]
    mat = [[1], [0]]  # Base case matrix: F(1) = 1, F(0) = 0

    Tn = matrix_exponentiation(T, n - 1)
    result = multiply_matrix(Tn, mat)

    print(f"Fibonacci({n}) = {result[0][0]}")

if __name__ == "__main__":
    main()
