#Дополнительное практическое задание по модулю*
#Задание "Средний балл"
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_to_list = sorted(list(students)) # Преобразование множества в лист с использованием функции sorted, что бы дальше ссылаться на упорядоченные элементы по индексу
# Ниже реализован расчет среднего арифметического значения каждого элемента по индексу в списке grades
grades_avg_0 = sum(grades[0]) / len(grades[0])
grades_avg_1 = sum(grades[1]) / len(grades[1])
grades_avg_2 = sum(grades[2]) / len(grades[2])
grades_avg_3 = sum(grades[3]) / len(grades[3])
grades_avg_4 = sum(grades[4]) / len(grades[4])

dict_grades_avg = {} # Создание пустого словаря
# Добавление данных в словарь
dict_grades_avg.update({students_to_list[0] : grades_avg_0,
                        students_to_list[1] : grades_avg_1,
                        students_to_list[2] : grades_avg_2,
                        students_to_list[3] : grades_avg_3,
                        students_to_list[4] : grades_avg_4})
print(dict_grades_avg)