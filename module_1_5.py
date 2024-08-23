# Неизменяемые и изменяемые объекты. Кортежи и списки
# 2. Задайте переменные разных типов данных:
immutable_var = (555, "String", True)
print(immutable_var) # Выполните операции вывода кортежа immutable_var на экран.

# 3. Изменение значений переменных:
# Элементы в кортеже нельзя изменять, кроме тех, которые добавлены в виде списка через квадратные скобки.

# 4. Создание изменяемых структур данных:
mutable_list = ["Blue", "Green", "Black"]
mutable_list[0:] = ["Red","Grey","White"] # Измените элементы списка mutable_list.
print(mutable_list)