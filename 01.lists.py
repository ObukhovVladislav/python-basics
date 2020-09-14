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

student_marks = []
while True:
    mark = input('Введите оценку студента:\n')
    if mark: # '' == False, 0== False, [] == False
        student_marks.append(mark)
    else:
        break

print('Ввод завершен')
print(student_marks)

# ['5', '4', '3', '5' '2']
#   0    1    2    3   4
i = 0
avg_mark = 0
while i < len(student_marks):
    print(type(avg_mark), type(student_marks[i]))
    avg_mark = avg_mark + int(student_marks[i])
    i = i + 1
print(avg_mark)

# <num> + <num2> - binary operation
# - <num> - unary operation

i = 0
avg_mark = 0
while i < len(student_marks):
    # print(type(avg_mark), type(student_marks[i]))
    # avg_mark = avg_mark + int(student_marks[i])
    print(type(avg_mark), type(student_marks[i]))
    avg_mark += int(student_marks[i])
    # i = i + 1
    i += i + 1
#avg_mark = avg_mark / len(student_marks)
avg_mark /= len(student_marks)
print('средний балл', avg_mark)
