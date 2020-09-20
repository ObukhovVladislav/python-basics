student_marks = []
while True:
    mark = input('введите оценки студента:\n')
    if mark:
        student_marks.append(int(mark))
        if int(mark) > 5:
            print('Введите оценки от 1 до 5')
            student_marks.remove(int(mark))
        elif int(mark) == 0:
            student_marks.remove(int(mark))
    else:
        break

avg_mark = 0
for mark in student_marks:
    avg_mark += mark
avg_mark /= len(student_marks)
if not student_marks:
    print('Пусто')
else:
    print('Оценки:', student_marks)
    print('Средний балл', avg_mark)
