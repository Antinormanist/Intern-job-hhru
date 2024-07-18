import math


def circle_area(r: float|int) -> float|int:
    """
    Возвращает площадь круга, округлённую до двух знаков после запятой, по его радиусу
    """
    return round(math.pi * r ** 2, 2)


def triangle_area(a: float|int, b: float|int, c: float|int) -> float|int:
    """
    Возвращает площадь треугольника, округлённую до двух знаков после запятой, по трём сторонам
    """
    if (
        a ** 2 + b ** 2 == c ** 2 or
        a ** 2 + c ** 2 == b ** 2 or
        b ** 2 + c ** 2 == a ** 2
    ):
        print('А треугольник то прямоугольный!')
    # Triangle  S = √p · (p — a)(p — b)(p — c), где a, b и c это стороны треугольника и p – половина периметра треугольника.
    p = (a + b + c) / 2
    S = round((p * (p - a) * (p - b) * (p - c)) ** 0.5, 2)
    return S
    
        


if __name__ == '__main__':
    assert circle_area(1) == 3.14, 'Код фигня, переделывай'
    assert circle_area(5) == 78.54, 'Как уже говорилось, переделывай'
    assert triangle_area(2, 2, 3) == 1.98, 'Ошибка'
    assert triangle_area(5, 5, 5) == 10.83, 'Другая ошибка'
    assert triangle_area(3, 4, 5) == 6, '...'