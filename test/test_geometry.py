# coding=utf-8
import unittest
import math

import sys
sys.path.append('../projet_ci')

from geometry import rectangle_area, rectangle_perimeter, circle_area, circle_circumference

if __name__ == '__main__':
    print(__package__)

class TestGeometricFunctions(unittest.TestCase):

    def test_rectangle_area(self):
    # Tests de cas normaux
        self.assertEqual(rectangle_area(5, 3), 15)
        self.assertEqual(rectangle_area(7, 2), 14)
        
        # Tests de cas limites
        self.assertEqual(rectangle_area(0, 10), 0)  # longueur zéro
        self.assertEqual(rectangle_area(10, 0), 0)  # largeur zéro
        self.assertEqual(rectangle_area(0, 0), 0)   # longueur et largeur zéro
        self.assertEqual(rectangle_area(1, 1), 1)   # carré de côté 1

    def test_rectangle_perimeter(self):
        # Tests de cas normaux
        self.assertEqual(rectangle_perimeter(5, 3), 16)
        self.assertEqual(rectangle_perimeter(7, 2), 18)
        
        # Tests de cas limites
        self.assertEqual(rectangle_perimeter(0, 10), 20)  # longueur zéro
        self.assertEqual(rectangle_perimeter(10, 0), 20)  # largeur zéro
        self.assertEqual(rectangle_perimeter(0, 0), 0)    # longueur et largeur zéro
        self.assertEqual(rectangle_perimeter(1, 1), 4)    # carré de côté 1

    def test_circle_area(self):
        # Tests de cas normaux
        self.assertAlmostEqual(circle_area(4), math.pi * 16)
        self.assertAlmostEqual(circle_area(2.5), math.pi * 2.5**2)
        
        # Tests de cas limites
        self.assertAlmostEqual(circle_area(0), 0)     # rayon zéro
        self.assertAlmostEqual(circle_area(1), math.pi) # rayon 1

    def test_circle_circumference(self):
        # Tests de cas normaux
        self.assertAlmostEqual(circle_circumference(4), 2 * math.pi * 4)
        self.assertAlmostEqual(circle_circumference(2.5), 2 * math.pi * 2.5)
        
        # Tests de cas limites
        self.assertAlmostEqual(circle_circumference(0), 0)   # rayon zéro
        self.assertAlmostEqual(circle_circumference(1), 2 * math.pi) # rayon 1

if __name__ == '__main__':
    unittest.main()
