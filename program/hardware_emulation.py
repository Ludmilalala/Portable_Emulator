класс ЭмуляторОборудования:
    "функция инициализации":
        включено = Истина
        кнопки = {}

    "функция включить_питание":
        включено = Истина

    "функция выключить_питание":
        включено = Ложь

    "функция нажать_кнопку(кнопка)":
        если включено:
            кнопки[кнопка] = Истина
            вывести(f"Кнопка {кнопка} нажата.")
        иначе:
            вывести("Устройство не включено.")

    "функция отпустить_кнопку(кнопка)":
        если включено:
            кнопки[кнопка] = Ложь
            вывести(f"Кнопка {кнопка} отпущена.")
        иначе:
            вывести("Устройство не включено.")
