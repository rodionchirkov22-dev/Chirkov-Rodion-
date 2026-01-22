import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # Читаем содержимое CSV файла
    with open(INPUT_FILENAME, 'r', newline='') as csv_file:
        # Создаем reader объект для чтения CSV
        csv_reader = csv.DictReader(csv_file)

        # Преобразуем каждую строку в словарь и собираем в список
        data = [row for row in csv_reader]

    # Сериализуем в JSON файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w') as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
