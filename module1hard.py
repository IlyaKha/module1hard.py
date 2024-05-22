grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Преобразование множества в список для упорядоченного доступа
students_list = list(students)

# Словарь для хранения средних баллов
average_grades = {}

# Перебираем списки оценок и имена учеников
for i in range(len(grades)):
    # Вычисляем средний балл для текущего ученика
    average_grade = sum(grades[i]) / len(grades[i])

    # Добавляем в словарь имя ученика как ключ и средний балл как значение
    average_grades[students_list[i]] = average_grade
print(average_grades)