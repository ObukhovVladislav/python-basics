import sys
# to contain -> container -> arrays
# to read -> reader
# Объекты(пользователь)
#    - атрибуты: свойсва(id, name, login, password)
#    - методы: действия (edit, delete, create, input_data)
# snake_case
# 'ya.ru' -> reference
my_var = [12, '15', 95.32, 55, True]
print(my_var, type(my_var), id(my_var), sys.getsizeof(my_var))

my_var = 12
print(my_var, type(my_var), id(my_var), sys.getsizeof(my_var))

my_var = 12.5
print(my_var, type(my_var), id(my_var), sys.getsizeof(my_var))

my_var = '12.5'
print(my_var, type(my_var), id(my_var), sys.getsizeof(my_var))

