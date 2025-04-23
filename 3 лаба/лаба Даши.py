def read_matrix(file_path):
    with open(file_path, 'r') as f:
        return [list(map(int, line.strip().split())) for line in f]

def copy_matrix(matrix): 
    return [row[:] for row in matrix]

def print_matrix(matrix, name):
    print(f'\n{name}:')
    for row in matrix:
        print(" ".join(f"{x:3}" for x in row))

def transpone(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def scalar(matrix, scalar_value):
    return [[scalar_value * x for x in row] for row in matrix]

def swap(matrix, n):
    for i in range(n // 2):
        for j in range(i + 1, n - i - 1):
            matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]

def swap2(matrix, n):
    for i in range(n):
        for j in range(i + 1, n):
            if i + j >= n:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

K = int(input('Введите K: '))
A = read_matrix('111.txt')
N = len(A)  # Определяем размер матрицы автоматически

F = copy_matrix(A)
min_odd = min(x for row in A for x in row if x % 2 == 1)
sum_even = sum(x for row in A for x in row if x % 2 == 0)

if min_odd > sum_even: 
    swap2(F, N)
else: 
    swap(F, N)

print_matrix(A, 'Матрица A')
print_matrix(F, 'Матрица F')

A_trans = transpone(A)
F_k = scalar(F, K)
A_trans_k = scalar(A_trans, K)

result = [[F_k[i][j] - A_trans_k[i][j] for j in range(N)] for i in range(N)]

print_matrix(A_trans_k, 'K*A^т')
print_matrix(F_k, 'F*K')
print_matrix(result, 'Результат')
