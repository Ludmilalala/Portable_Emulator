класс УправлениеПрогрессомИгры:
    "функция инициализации":
        сохраненный_прогресс = {}

    "функция сохранить_прогресс(идентификатор_игры, данные_прогресса)":
        сохраненный_прогресс[идентификатор_игры] = данные_прогресса

    "функция загрузить_прогресс(идентификатор_игры)":
        вернуть сохраненный_прогресс.get(идентификатор_игры, Ничто)
