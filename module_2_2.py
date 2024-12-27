first = int(input('Ввведите число 1: '))
second  = int(input('Введите число 2: '))
third  = int(input('Введите число 3: '))
if first ==  second  == third:
    print(3, " - ура, все числа равны")
elif first == second or first == third or second == third:
    print(2, " - хоть два числа равны, и то хорошо")
else:
    print(0, ' - Числа не равны друг другу')
  # консоль с решением для чисел 51, 52, 53
  # Ввведите число 1: 51
  # Введите число 2: 52
  # Введите число 3: 53
  # 0  - Числа не равны друг другу
  # Process finished with exit code 0
