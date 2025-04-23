import random
def print_matrix(matrix, name):
    print(name + ':')
    for row in matrix: print(' '.join(f"{elem:>4}" for elem in row))
    print()
N= input("Ввод N: ")
assert N.isdigit() and N. isalnum(), 'N должно быть целым числом'
K= input("Ввод K: ")
assert K.isdigit() and K.isalnum(), 'K должно быть целым числом'
N, K, Summa, Odd = int(N), int(K), 0,0
A = [[random.randint(-10, 10) for _ in range(N)] for _ in range(N)]
for x in range(0, N - 2):
    for y in range(1 + x, N - 1 - x):
        if x % 2 == 0: Summa += A[x][y]
for y in range(N - 1, N // 2, -1):
    for x in range(-y + N, y):
        if y % 2 == 0 and A[x][y] % 2 == 1: Odd += 1
print_matrix(A, 'Матрица А')
F, B, B1 = [row[:] for row in A], [row[:] for row in A], [row[:] for row in A]
if Odd < Summa:
    for x in range(0, N - 2):
        for y in range(1 + x, N - 1 - x):
            F[x][y], F[y][N-1-x] = F[y][N-1-x], F[x][y]
    print_matrix(F, 'Матрица F(поменяли области 1 и 2 не cимметрично)')
else:
    for x in range(0, N - 2):
        for y in range(1 + x, N - 1 - x):
            F[x][y], F[N-y-1][N-1-x] = F[N-y-1][N-1-x], F[x][y]
    print_matrix(F, 'Матрица F(поменяли области 1 и 2 cимметрично)')
for x in range(0, len(A)):
    for y in range(0, len(A[x])):
        B[x][y] = A[x][y]*K
print_matrix(B, 'Матричная операция А*К')
result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
transponed = list(map(list, zip(*A)))
print_matrix(transponed, 'Транспонированная матрица А')
for x in range(0, len(A)):
    for y in range(0, len(A[x])):
        B1[x][y] = transponed[x][y]*K
print_matrix(B1, 'Матричная операция A^T * K')
for i in range(len(B)):
    for j in range(len(A[0])):
        for k in range(len(A)):
            result[i][j] += B[i][k] * A[k][j]
print_matrix(result, 'Матричная операция (K*A)*A')
for x in range (0,N):
    for y in range (0,N):
        result[x][y] = result[x][y] - B1[x][y]
print_matrix(result, 'результат матричных операций')
