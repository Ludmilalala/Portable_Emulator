класс АвтообновлениеИгры:
    "функция инициализации":
        автообновление_включено = Ложь

    "функция включить_автообновление":
        автообновление_включено = Истина
        вывести("Автоматическое обновление включено.")
        
    "функция выключить_автообновление":
        автообновление_включено = Ложь
        вывести("Автоматическое обновление отключено.")

    "функция проверить_обновления":
        если автообновление_включено:
            вывести("Проверка обновлений... Обновление доступно!")
        иначе:
            вывести("Автоматическое обновление отключено.")
