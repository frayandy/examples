import math

from typing import Union


class Triangle:

    def __init__(self, a: Union[int, float], b: Union[int, float], c: Union[int, float]):
        self._validate_sides(a, b, c)
        self._a_side = a
        self._b_side = b
        self._c_side = c
        self._h_perimeter = (self._a_side + self._b_side + self._c_side) * 0.5
        self._area = None

    @property
    def a_side(self) -> Union[int, float]:
        return self._a_side

    @property
    def b_side(self) -> Union[int, float]:
        return self._b_side

    @property
    def c_side(self) -> Union[int, float]:
        return self._c_side

    @property
    def area(self) -> Union[int, float]:
        if self._area is None:
            self._area = self._calculate_area()

        return self._area

    def __str__(self):
        return f'Triangle[a:{self.a_side}, b:{self.b_side}, c:{self.c_side}, area:{self.area}]'

    def _calculate_area(self):
        return math.sqrt(
            self._h_perimeter
            * (self._h_perimeter - self._a_side)
            * (self._h_perimeter - self._b_side)
            * (self._h_perimeter - self._c_side)
        )

    @staticmethod
    def _validate_sides(a: Union[int, float], b: Union[int, float], c: Union[int, float]):
        if not (a + b > c and b + c > a and a + c > b):
            raise ValueError('You can\'t create triangle with this a, b, c. Please try again')


def make_triangle():
    side_a = input('Please enter triangle side A: ')
    side_b = input('Please enter triangle side B: ')
    side_c = input('Please enter triangle side C: ')
    return Triangle(float(side_a), float(side_b), float(side_c))


def get_user_input_and_make_triangles():
    triangles_list = []

    while True:
        try:
            triangles_list.append(make_triangle())
        except Exception as e:
            print(str(e))
        else:
            new_one = input('Do you want to add another one ? Press (y,n): ')
            if new_one.lower() in ('n', 'no'):
                break

    return triangles_list


if __name__ == '__main__':
    triangles = get_user_input_and_make_triangles()
    triangles.sort(key=lambda x: x.area, reverse=True)
    for t in triangles:
        print(t)
