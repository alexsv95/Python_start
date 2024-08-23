# 1st program
print(9 ** 0.5 * 5)

# 2nd program
print(9.99 > 9.98 and 1000 != 1000.1)

# 3rd program
print(2*2+2 == 2*(2+2))

# 4th program
print(int(float("123.456")*10 % 10))


# Строки и индексация строк
example = 'Топинамбур'
print(example[0]) # первый символ этой строки.
print(example[-1]) # последний символ этой строки (используя отрицательный индекс).
print(example[5:]) # вторую половину этой строки (С нечётным количеством символов: 'Urban' -> 'ban').
print(example[::-1]) # это слово наоборот.
print(example[1::2]) # каждый второй символ этой строки. (Пример: 'Топинамбур'->'оиабр')


# Переменные
tasks_count = 12
time_spent = 1.5
course_name = "Python"
time_spent_one_task = time_spent / tasks_count
print(f"{course_name}, всего задач:{tasks_count}, затрачено часов: {time_spent}, среднее время выполнения {time_spent_one_task} часа")


# Организация программ и методы строк

