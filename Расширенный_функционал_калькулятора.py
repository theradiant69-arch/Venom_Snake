def simple_calculator():
    while True:
        print("\nПростой калькулятор")
        try:
            a = float(input("Первое число: "))
            op = input("Операция (+, -, *, /, **, %, //, sqrt, pow): ")
            
            # Операции, требующие только одно число
            if op == 'sqrt':
                if a < 0:
                    print("Ошибка: нельзя извлечь корень из отрицательного числа!")
                    continue
                result = a ** 0.5
                print(f"Результат: √{a} = {result}")
                continue
            
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
            elif op == '**':
                result = a ** b
            elif op == '%':
                if b == 0:
                    print("Ошибка: деление на ноль!")
                    continue
                result = a % b
            elif op == '//':
                if b == 0:
                    print("Ошибка: деление на ноль!")
                    continue
                result = a // b
            elif op == 'pow':
                result = a ** b
            else:
                print("Неверная операция!")
                continue
            
            print(f"Результат: {a} {op} {b} = {result}")
            
        except ValueError:
            print("Ошибка: введите числа!")
        except KeyboardInterrupt:
            print("\nВыход из калькулятора")
            break
        except OverflowError:
            print("Ошибка: слишком большое число!")
        except Exception as e:
            print(f"Неизвестная ошибка: {e}")

# Дополнительная функция для вычисления выражений
def calculate_expression(expression):
    """Вычисляет математическое выражение"""
    try:
        # Безопасное вычисление выражения
        result = eval(expression, {"__builtins__": None}, {})
        return result
    except:
        return None

# Функция для работы с памятью
class CalculatorMemory:
    def __init__(self):
        self.memory = 0
    
    def store(self, value):
        self.memory = value
        print(f"Значение {value} сохранено в памяти")
    
    def recall(self):
        print(f"Значение в памяти: {self.memory}")
        return self.memory
    
    def clear(self):
        self.memory = 0
        print("Память очищена")

# Расширенная версия калькулятора с дополнительными функциями
def advanced_calculator():
    memory = CalculatorMemory()
    
    while True:
        print("\n" + "="*40)
        print("Расширенный калькулятор")
        print("1 - Простые операции")
        print("2 - Вычисление выражений")
        print("3 - Работа с памятью")
        print("4 - Научные функции")
        print("0 - Выход")
        
        choice = input("Выберите режим: ")
        
        if choice == '1':
            simple_calculator()
        elif choice == '2':
            expr = input("Введите выражение: ")
            result = calculate_expression(expr)
            if result is not None:
                print(f"Результат: {expr} = {result}")
            else:
                print("Ошибка в выражении!")
        elif choice == '3':
            print("\nРабота с памятью:")
            print("1 - Сохранить значение")
            print("2 - Получить значение")
            print("3 - Очистить память")
            mem_choice = input("Выберите действие: ")
            
            if mem_choice == '1':
                try:
                    value = float(input("Введите значение: "))
                    memory.store(value)
                except ValueError:
                    print("Ошибка: введите число!")
            elif mem_choice == '2':
                memory.recall()
            elif mem_choice == '3':
                memory.clear()
        