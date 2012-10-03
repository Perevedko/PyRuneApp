# coding: utf-8
from __future__ import unicode_literals
"""Модуль программы для вычислений"""


def name_to_num(name):
    """Побуквенно пересчитывает буквы в имени в числа"""
    name = name.upper()
    result = 0
    my_list = ("АИСЪ", "БЙТЫ", "ВКУЬ", "ГЛФЭ", "ДМХЮ", "ЕНЦЯ", "ЁОЧ", "ЖПШ",
        "ЗРЩ")
    for char in name:
        for j in range(9):
            if char in my_list[j]:
                result += j + 1
                continue
    return result


def int_to_digit(num):
    """'Складывает' число в цифру"""
    while num > 9:
        num = sum([int(i) for i in str(num)])
    return num


def to_three(num):
    """Переводит цифру в троичную систему"""
    remainder = num % 3
    return {1: 1, 2: 2, 0: 3}[remainder]


def att(one, two, three, grand):
    """Переводит 4 аргумента в 1 атт (подробности на сайте)"""
    count = [0, 0, 0, 0]

    count[to_three(one)] += 1
    count[to_three(two)] += 1
    count[to_three(three)] += 1

    if count[1] > count[2] and count[1] > count[3]:
        return 1
    elif count[2] > count[1] and count[2] > count[3]:
        return 2
    elif count[3] > count[1] and count[3] > count[2]:
        return 3
    else:
        return to_three(grand)
