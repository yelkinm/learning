nested2= {'a':{'b':{'s':8,'j':999}},
'u':55,
'b':{'s':8}
          }
nested = {'Q':44, 'S': {'Z':42}}
def flatten_dict(nested):
    #фдаг, что у нас более 1го уровня вложенности и нужна рекурсия
    v_more_1 = False
    # переменная для собирания результата
    v_result = {}
    # цикл для перебора значений
    for key in nested:
        # проверяем, тип значения
        if (isinstance(nested[key], int )):
            #для целого просто дублируем
            v_result[key] = nested[key]
        else:
            # для словаря разбиваем 1 уровень вложенности
            for key2 in nested[key]:
                # если уровень вложенности дальше есть - выставим флаг
                if not (isinstance(nested[key][key2], int)):
                    v_more_1 = True
                # разбиваем наш словарь вложенный на отдельные записи. только текущий уровень
                v_result[key+'_'+key2] = nested[key][key2]
    #print(v_result)
    #проверяем, надо ли спускаться глубже одного уровня
    if v_more_1:
        return flatten_dict(v_result)
    else:
        return v_result

print(flatten_dict(nested))