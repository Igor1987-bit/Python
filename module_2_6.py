print('Very old cipher')
def password(number):
    passcode = ''
    for i in range(1, number):
        j = 0
        while j <= number:
            j += 1
            if j <= i:
                continue
            if number % (i + j) == 0:
                passcode += str(i) + str(j)
    return passcode

number = int(input('Enter a number from 3 to 20: '))
if number >= 3 and number <= 20:
    print(password(number))
else:
    print('the number is not in range [3:20]')
console
# Very old cipher
# Enter a number from 3 to 20: 7
# 162534
