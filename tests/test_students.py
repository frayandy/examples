from unittest import TestCase
from students import Student


class TestStudents(TestCase):

    def test_students(self):
        data = 'Jonson John Johnovich,01/01/1985,05/05/2019,12:27:23-13:15:12,150'
        result = Student(data).parse_and_get_data()
        self.assertEqual(result['name'], 'Jonson J.J.')
