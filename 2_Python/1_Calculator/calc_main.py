print('Вас приветствует пррограмма "Калькулятор" \n Сначала введите первое число, затем арифметическую операцию '
      '(+, -, *, **, /, //, %), а после третье число. \n Для выхода из программы введите "exit" \n')

while True:
    a = input('Введите первое число: ')
    if a == 'exit':
        break
    o = input('Введите арифметическую операцию (+, -, *, **, /, //, %): ')
    if o == 'exit':
        break
    b = input('Введите второе число: ')
    if b == 'exit':
        break
    a = int(a)
    b = int(b)
    if o == '+':
        print(f'{a} + {b} = {a + b} \n Для выхода из программы введите "exit" \n')
    elif o == '-':
        print(f'{a} - {b} = {a - b} \n Для выхода из программы введите "exit" \n')
    elif o == '*':
        print(f'{a} * {b} = {a * b} \n Для выхода из программы введите "exit" \n')
    elif o == '**':
        print(f'{a} ** {b} = {a ** b} \n Для выхода из программы введите "exit" \n')
    elif o == '/':
        print(f'{a} / {b} = {a / b} \n Для выхода из программы введите "exit" \n')
    elif o == '//':
        print(f'{a} // {b} = {a // b} \n Для выхода из программы введите "exit" \n')
    elif o == '%':
        print(f'{a} % {b} = {a % b} \n Для выхода из программы введите "exit" \n')
print('Вы вышли из программы.')
