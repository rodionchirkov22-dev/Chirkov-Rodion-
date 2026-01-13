def find_common_participants(group1, group2, sep=','):

    # Разделяем строки на списки участников
    list1 = group1.split(sep)
    list2 = group2.split(sep)

    # Находим пересечение множеств и преобразуем в список
    common = list(set(list1) & set(list2))

    # Сортируем по алфавиту
    common.sort()

    return common


# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Проверьте работу функции с разделителем отличным от запятой
result = find_common_participants(
    participants_first_group,
    participants_second_group,
    sep='|'
)

print("Общие участники:", result)