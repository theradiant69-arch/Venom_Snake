def simple_calculator():
    while True:
        print("\nПростой калькулятор")
        try:
            a = float(input("Первое число: "))
            op = input("Операция (+, -, *, /): ")
            b = float(input("Второе число: "))
            
            if op == '+':
                result = a + b
            elif op == '-':
                result = a - b
            elif op == '*':
                result = a * b
            elif op == '/':
                if b == 0:
                    print("Ошибка: деление на ноль!")
                    continue
                result = a / b
            else:
                print("Неверная операция!")
                continue
            
            print(f"Результат: {a} {op} {b} = {result}")
            
        except ValueError:
            print("Ошибка: введите числа!")
        except KeyboardInterrupt:
            print("\nВыход из калькулятора")
            break

# Запуск
simple_calculator()