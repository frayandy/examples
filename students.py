from datetime import datetime
from typing import Dict


class Student:

    def __init__(self, raw_data: str):
        self._time_format = '%H:%M:%S'
        self._date_format = '%d/%m/%Y'
        self._raw_data = raw_data

    def parse_and_get_data(self) -> Dict[str, str]:
        full_name, birthday, test_date, test_time, test_result = self._raw_data.split(',')
        test_start_time, test_end_time = test_time.split('-')
        return {
            "name": self._parse_and_get_name(full_name),
            "age": self._parse_and_get_age(birthday, test_date),
            "test_time": self._parse_and_get_test_time(test_start_time, test_end_time)
        }

    @staticmethod
    def _parse_and_get_name(full_name: str) -> str:
        surname, name, second_name = full_name.split()
        return f"{surname} {name[0]}.{second_name[0]}."

    def _parse_and_get_age(self, birthday: str, test_date: str) -> str:
        birthday_datetime = datetime.strptime(birthday, self._date_format)
        test_date_datetime = datetime.strptime(test_date, self._date_format)

        age = test_date_datetime.year - birthday_datetime.year
        if birthday_datetime.month < test_date_datetime.month:
            age -= 1
        elif birthday_datetime.month == test_date_datetime.month and birthday_datetime.day < test_date_datetime.day:
            age -= 1

        return str(age)

    def _parse_and_get_test_time(self, start_date: str, end_date: str) -> str:
        return str(datetime.strptime(end_date, self._time_format) - datetime.strptime(start_date, self._time_format))


class StudentV2:

    def __init__(self, raw_data: str):
        self._time_format = '%H:%M:%S'
        self._date_format = '%d/%m/%Y'
        full_name, birthday, test_date, test_time, test_result = raw_data.split(',')
        self._name = self._parse_and_get_name(full_name)
        self._age = self._parse_and_get_age(birthday, test_date)
        test_start_time, test_end_time = test_time.split('-')
        self._test_time = self._parse_and_get_test_time(test_start_time, test_end_time)

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def test_time(self):
        return self._test_time

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Test time: {self.test_time}"

    @staticmethod
    def _parse_and_get_name(full_name: str) -> str:
        surname, name, second_name = full_name.split()
        return f"{surname} {name[0]}.{second_name[0]}."

    def _parse_and_get_age(self, birthday: str, test_date: str) -> str:
        birthday_datetime = datetime.strptime(birthday, self._date_format)
        test_date_datetime = datetime.strptime(test_date, self._date_format)

        age = test_date_datetime.year - birthday_datetime.year
        if birthday_datetime.month < test_date_datetime.month:
            age -= 1
        elif birthday_datetime.month == test_date_datetime.month and birthday_datetime.day < test_date_datetime.day:
            age -= 1

        return str(age)

    def _parse_and_get_test_time(self, start_date: str, end_date: str) -> str:
        return str(datetime.strptime(end_date, self._time_format) - datetime.strptime(start_date, self._time_format))


if __name__ == '__main__':
    data = Student('Jonson John Johnovich,01/01/1985,05/05/2019,12:27:23-13:15:12,150').parse_and_get_data()
    print(f"Name: {data['name']}, Age: {data['age']}, Test time: {data['test_time']}")

    student_v2 = StudentV2('Jonson John Johnovich,01/01/1985,05/05/2019,12:27:23-13:15:12,150')
    print(student_v2)
    print(f"Name: {student_v2.name}, Age: {student_v2.age}, Test time: {student_v2.test_time}")
