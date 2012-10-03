# coding: utf-8
from __future__ import unicode_literals
from __future__ import print_function
"""Главный модуль программы"""

import calc

names = (("Феху", "Уруз", "Турисаз", "Ансуз", "Райдо", "Кеназ", "Гебо", "Вуньо", "Вирд"),
         ("Хагалаз", "Наутиз", "Иса", "Йера", "Эйваз", "Перт", "Альгиз", "Совило", "Вирд"),
         ("Тейваз", "Беркана", "Эваз", "Манназ", "Лагуз", "Ингуз", "Одал", "Дагаз", "Вирд"))

class Rune(object):
    """Класс c функциями для рун"""

    def __init__(self):
        pass

    @staticmethod
    def num_day(day):
        """Возвращает число дня"""
        return calc.int_to_digit(day)

    @staticmethod
    def num_month(month):
        """Возвращает число месяца"""
        return calc.int_to_digit(month)

    @staticmethod
    def num_year(year):
        """Возвращает число года"""
        return calc.int_to_digit(year)

    @staticmethod
    def num_last_name(last_name):
        """Возвращает число фамилии"""
        return calc.int_to_digit(calc.name_to_num(last_name))

    @staticmethod
    def num_first_name(first_name):
        """Возвращает число имени"""
        return calc.int_to_digit(calc.name_to_num(first_name))

    @staticmethod
    def num_middle_name(middle_name):
        """Возвращает число отчества"""
        return calc.int_to_digit(calc.name_to_num(middle_name))

    @staticmethod
    def num_essence(date):
        """Возвращает число Судьбы"""
        return (calc.int_to_digit(Rune.num_day(date[0]) +
            Rune.num_month(date[1]) + Rune.num_year(date[2])))

    @staticmethod
    def num_person(name):
        """Возвращает число Имени"""
        return (calc.int_to_digit(Rune.num_last_name(name[0]) +
            Rune.num_first_name(name[1]) + Rune.num_middle_name(name[2])))

    @staticmethod
    def num_gold(date, name):
        """Возвращает Золотое Алхимическое Число"""
        return calc.int_to_digit(Rune.num_essence(date) +
            Rune.num_person(name))


class FirstRune(object):
    """Руна Сущности"""

    def __init__(self, date):
        self.date = date

    @property
    def att(self):
        """Возвращает атт руны Сущности"""
        return calc.att(Rune.num_day(self.date[0]),
            Rune.num_month(self.date[1]),
            Rune.num_year(self.date[2]),
            Rune.num_essence(self.date))

    @property
    def group(self):
        """Возвращает группу руны Сущности"""
        return Rune.num_essence(self.date)


class SecondRune:
    """Руна Личности"""

    def __init__(self, name):
        self.name = name

    @property
    def att(self):
        """Возращает атт руны Личности"""
        return calc.att(Rune.num_last_name(self.name[0]),
            Rune.num_first_name(self.name[1]),
            Rune.num_middle_name(self.name[2]),
            Rune.num_person(self.name))

    @property
    def group(self):
        """Возвращает группу руны Личности"""
        return Rune.num_person(self.name)


class ThirdRune(object):
    """Золотая руна"""

    def __init__(self, date, name):
        self.date = date
        self.name = name

    @property
    def att(self):
        """Возвращает атт Золотой руны"""
        return calc.att(Rune.num_last_name(self.name[0]),
            Rune.num_first_name(self.name[1]),
            Rune.num_middle_name(self.name[2]),
            Rune.num_person(self.name))

    @property
    def group(self):
        """Возвращает группу Золотой руны"""
        return Rune.num_gold(self.date, self.name)

def runes(date, name):
    rune1 = FirstRune(date)
    rune2 = SecondRune(name)
    rune3 = ThirdRune(date, name)
    return (names[rune1.att - 1][rune1.group - 1],
            names[rune2.att - 1][rune2.group - 1],
            names[rune3.att - 1][rune3.group - 1])

def main():
    """Главная функция программы"""
    # Сканируем ФИО и дату рождения (и разбиваем)
    name = raw_input("Введите ФИО:\n> ").decode('utf-8').split()
    date = raw_input("Введите дату рождения:\n> ").decode('utf-8').split('.')

    # Переводим дату рождения из строк в числа
    date = tuple([int(i) for i in date])

    # Вывод результатов
    print(*runes(date, name))


if __name__ == '__main__':
    main()
