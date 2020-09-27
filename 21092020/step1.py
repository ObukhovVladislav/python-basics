# refactoring
# dry: Do not Repeat Yourself
# habra-effect -> 404
# bottleneck
# brute force

# Первый пример кода прошлого домашнего задания
# student_marks = []
# while True:
#     mark = input('Введите оценку студента:\n')
# #    mark = int(mark) # int('') -> exception
#     if mark:
#         student_marks.append(int(mark))
#         if int(mark) > 5:
#             print('Оценка не подходит под категорию оценивания')
#             student_marks.remove(int(mark))
#         elif int(mark) < 1:
#             print('Оценка не подходит под категорию оценивания')
#             student_marks.remove(int(mark))
#     else:
#         break
# print('Ввод завершён')

# Второй пример кода прошлого домашнего задания
# student_marks = []
# while True:
#     mark = input('Введите оценку студента:\n')
#     # mark = int(mark) # int('') -> exception
#     if mark:
#         mark = int(mark)  # int('5') -> ok
#         student_marks.append(mark)
#         if mark > 5:
#             print('Оценка не подходит под категорию оценивания')
#             student_marks.remove(mark)
#         elif mark < 1:
#             print('Оценка не подходит под категорию оценивания')
#             student_marks.remove(mark)
#     else:
#         break
# print('Ввод завершён')


# 9 mark = '7'
# 11 True
#       students_marks = [4, 4, 3, 2, 4, 5, 5, 4, 2]
# 12 mark = 7
# 13 students_marks = [4, 4, 3, 2, 4, 5, 5, 4, 2, 7]
# 14 True
# 16 student_marks.remove(mark) -> students.marks.remove(7)
# remove() -> search in list (brute force, linear search)
# [4, 4, 3, 2, 4, 5, 5, 4, 2, 7], n = len(student_marks) -> task size, n steps
# [7, 4, 4, 3, 2, 4, 5, 5, 4, 2] -> 1 step, [4, 4, 3, 2, 7, 4, 5, 5, 4, 2] -> n // 2 steps
# list search complexity = O(n)
# O(n) - о большое эн

# Третий пример кода прошлого задания

student_marks = []
while True:
    mark = input('Введите оценку студента:\n')
    if mark:
        mark = int(mark)
        if mark > 5:
            print('Оценка не подходит под категорию оценивания')
        elif mark < 1:
            print('Оценка не подходит под категорию оценивания')
    else:
        student_marks.append(mark)  # O(1)
        break
print('Ввод завершён')