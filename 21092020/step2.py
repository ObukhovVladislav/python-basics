student_marks = []
while True:
    mark = input('введите оценку студента:\n')
    if mark:
        mark = int(mark)
        if mark > 5 or mark < 1:
            print('Оценка не подходит под категорию оценивания')
        else:
            student_marks.append(mark)
    else:
        break

print('ввод завершен')


# student_marks = []
# while True:
#     mark = input('введите оценку студента:\n')
#     if mark:
#         mark = int(mark)
#         if 1 <= mark <= 5:
#             student_marks.append(mark)
#         elif mark > 5:
#             print("Оценка больше 5")
#         elif mark < 1:
#             print("Оценка меньше 1")
#     else:
#         break
#
# print('ввод завершен')