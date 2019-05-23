from unittest import TestCase

from triangles import Triangle


class TestTriangles(TestCase):

    def test_triangles(self):
        exist_triangles = [Triangle(1, 1, 1), Triangle(2, 2, 2), Triangle(3, 3, 3)]
        expected_areas_order = [Triangle(3, 3, 3).area, Triangle(2, 2, 2).area, Triangle(1, 1, 1).area]
        self.assertEqual(
            [t.area for t in sorted(exist_triangles, key=lambda x: x.area, reverse=True)], expected_areas_order
        )
