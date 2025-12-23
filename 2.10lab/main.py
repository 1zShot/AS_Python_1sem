def power_positive(num, pw):
    if pw < 0:
        raise ValueError("Отрицательная степень")
    return num ** pw
try:
    n = float(input("число: "))
    p = int(input("степень: "))
    res = power_positive(n, p)
    print(f"Результат: {res}")
except ValueError as e:
    print(f"Ошибка: {e}")
print()
def check_even(num):
    if num % 2 != 0:
        raise Exception("Число нечет")
    return True
try:
    n = int(input("Введите число для проверки: "))
    check_even(n)
    print("Число чет")
except Exception as e:
    print(f"Ошибка: {e}")
print()
def power_with_assert(num, pw):
    assert pw >= 0, "Отрицательная степень"
    return num ** pw
try:
    n = float(input("Число: "))
    p = int(input("Степень: "))
    res = power_with_assert(n, p)
    print(f"Результат: {res}")
except AssertionError as e:
    print(f"Ошибка: {e}")
