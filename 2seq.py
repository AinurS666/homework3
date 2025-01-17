# создать модуль 2seq.py. Задание:
# Пользователь вводит любые цифры через запятую
# Сохранить цифры в список
# Получить новый список в котором будут только уникальные элементы исходного (уникальным считается символ, который встречается в исходном списке только 1 раз)
# Вывести новый список на экран
# Порядок цифр в новом списке не важен
# Пример работы: Введите элементы списка через запятую: 2,3,4,5,5,6,5,3,9
# Результат: 2, 4, 6, 9
# (Дополнительно*) Предусмотреть что пользователь может использовать один из 3-х разделителей:
# запятую, точку с запятой, слэш (1,2,3 1;2;3 1/2/3), но только какой то один 1,2;3/4 - так нельзя


posledovatelnost_dannix = input("Введите элементы списка через запятую, точку с запятой или слэш: ")

# Заменяем все разделители на запятую
posledovatelnost_dannix = posledovatelnost_dannix.replace(';', ',').replace('/', ',')

# Создаем список чисел, удаляя пробелы
# Разбиваем строку на части и создаем пустой список для чисел
numbers = []

# Проходим по каждому элементу в результате разбиения
for num in posledovatelnost_dannix.split(','):
    # Убираем пробелы вокруг числа и преобразуем его в целое число
    stripped_num = num.strip()  # Убираем пробелы
    if stripped_num:  # Проверяем, что строка не пустая
        numbers.append(int(stripped_num))  # Преобразуем в int и добавляем в список

# Используем множество для получения уникальных элементов
unique_elements = set(numbers)

# Выводим результат
print("Результат: ", ', '.join(str(num) for num in unique_elements))

