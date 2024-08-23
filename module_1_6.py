# Словари и множества
#2. Работа со словарями:
my_dict = {"Alex" : 1995, "Misha" : 1994}
print(my_dict.get("Alex")) #Выведите на экран одно значение по существующему ключу
print(my_dict.get("Masha", "Ключ отсутствует")) #одно по отсутствующему из словаря my_dict без ошибки.
my_dict.update({"Masha" : 2002, "Sveta" : 2000}) #Добавьте ещё две произвольные пары того же формата в словарь my_dict
print(my_dict)
value_del = my_dict.pop("Masha") #Удалите одну из пар в словаре по существующему ключу из словаря my_dict
print(value_del)
print(my_dict)

#3. Работа с множествами:
my_set = {22, 22, "Text", "Text", "Max", 17}
print(my_set)
my_set.update({40,"Denis"}) #Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
my_set.remove(22) #Удалите один любой элемент из множества my_set.
print(my_set)