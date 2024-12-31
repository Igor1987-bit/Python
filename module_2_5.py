def get_matrix(n, m, value):
    matrix = []
    for a in range(0, n):
        matrix_1 = []
        for b in range(0, m):
            matrix_1.append(value)
            value += 2
        matrix.append(matrix_1)
    return matrix

print('Матрица 1:')                         #печать матрицы 1 по строкам
result1 = get_matrix(2, 2, 10)
j = 0
for i in result1:
    print(result1[j])

print('Матрица 2:')                         #печать матрицы 2 по строкам
result2 = get_matrix(3, 5, 42)
j = 0
for i in result2:
    print(result2[j])

print('Матрица 3:')                         #печать матрицы 3 по строкам
result3 = get_matrix(4, 2, 12)
j = 0
for i in result3:
    print(result3[j])
  # Consol
  # Матрица 1:
  # [10, 12]
  # [10, 12]
  # Матрица 2:
  # [42, 44, 46, 48, 50]
  # [42, 44, 46, 48, 50]
  # [42, 44, 46, 48, 50]
  # Матрица 3:
  # [12, 14]
  # [12, 14]
  # [12, 14]
  # [12, 14]
