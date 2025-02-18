# Домашнее задание по уроку "Try и Except".
# Задание "Программистам всё можно":

def add_everything_up(a, b):
    """Функция принимает a и b, которые могут быть как числами(int, float), так и строками(str).
        TypeError - когда a и b окажутся разными типами (числом и строкой),
        то возвращать строковое представление этих двух данных вместе (в том же порядке).
        Во всех остальных случаях выполнять стандартные действия"""
    res = None  # переменная для хранения результата вычисления
    try:  # блок кода программы с ожидаемым выполнением
        res = round(a + b, 3)  # ожидаемое выполнение программы
    except TypeError as exc:  # блок кода программы, где можем перехватить ошибку
        if isinstance(a, str):  # если параметр а является строкой
            res = a + str(b)  # параметр b конвертируем в строку и производим конкатенацию строк
        else:  # если параметр b является строкой
            res = str(a) + b  # конвертируем параметр a в строку и производим конкатенацию строк
    finally:  # блок кода, который выполняется в обязательном порядке
        return res


if __name__ == '__main__':
    # Пример кода:
    print(add_everything_up(123.456, 'строка'))
    print(add_everything_up('яблоко', 4215))
    print(add_everything_up(123.456, 7))
