# temp = 0.1
#
# if условие:
#     блок если Да
# else:
#     блок если Нет

    # temp = 0.1
    #
    # if temp > 0:
    #     print("Можно шапку не надевать))")
    # else:
    #     print("Надень шапку")




# case = input("Кинь кубик:")   # vsegda str!!!
# # case = int(case)
# print(case, type(case))
# if case == "6":
#     print("Победил, Вася!")
# elif case == "1":
#     print("Победил Петя!")
# else:
#     print("Вы проиграли!")


# from random import randint
# case = randint(1, 6)   # vsegda str!!!
# case = int(case)
# print("Выпало число:", case)
# if case == 6:
#     print("Победил, Вася!")
# elif case == 1:
#     print("Победил Петя!")
# else:
#     print("Вы проиграли!")
#############################################
# тернарный оператор
# if case > 3:
#     result = case ** 2
# else:
#     result = - case

# from random import randint
# case = randint(1, 6)

# if case > 3:
#     result = case ** 2
# else:
#     result = - case

# result = case ** 2 if case > 3 else - case

# print("Выпало число:", case, "Результат:", result)

######################################################
# Строки и методы строк
# форматирование строк
# case = 1
# result = "qwe"
# print(f"Выпало число: {case} с результатом: {result}")

# dirname = "home"
# filename = "test.py"
# path = f"{dirname}/{filename}"
# print(path)
# литералы строк
my_str_1 = "I'm Qwerty"
my_str_2 = '"apple" asdf'
my_str_3 = '''zsada'''
my_str_4 = """QWERS"""

# index = -5      # индекс -1 последний с конца
# symbol = my_str_1[index]
# print(symbol)

# my_str_1_len = len(my_str_1)
# print(my_str_1_len, my_str_1[my_str_1_len -1])

# срез строки
# new_str = my_str_1[4:7]   # часть стрроки от левого индекса (включительно) до правого индекса (не включительно)
# new_str = my_str_1[40:70]

# index = 5
# new_str = my_str_1[: index] + "K" + my_str_1[index + 1:]   # замена символа на конкретном месте в строке
# new_str = my_str_1[1:-1:3]  # 3 - шаг среза
# new_str = my_str_1[::2]  # символы на четных местах в строке
# new_str = my_str_1[1::2]   # Символы на нечетных местах в строке
# new_str = my_str_1[::-1]   # Разворот строки
# print(new_str)

# my_str_1 = "I'm Qwerty"
#
# if my_str_1[-1] == "a":
#     print(f"'a' at last position in {my_str_1}")
# else:
#     print(f"'a' not on last position in {my_str_1}")

# for symbol in my_str_1:  # строка итерируемый объект
#     if (symbol.lower() not in "eyuioa") and symbol.isalpha() and symbol.isupper():
#         print(symbol)

# for symbol in my_str_1:
#     print(f"symbol '{symbol}' --> {ord(symbol)}")

# for index in range(ord("a"), ord('z') + 1):
#     print(f"index {index} --> '{chr(index)}")