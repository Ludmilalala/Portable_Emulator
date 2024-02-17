класс БезопасностьПриватность:
    "функция инициализации":
        шифрование_включено = Ложь
        брандмауэр_включен = Ложь

    "функция включить_шифрование":
        шифрование_включено = Истина
        вывести("Шифрование включено.")
        
    "функция включить_брандмауэр":
        брандмауэр_включен = Истина
        вывести("Брандмауэр включен.")

    "функция защитить_данные_пользователя":
        если шифрование_включено и брандмауэр_включен:
            вывести("Данные пользователя защищены.")
        иначе:
            вывести("Данные пользователя находятся под угрозой. Пожалуйста, включите шифрование и брандмауэр.")