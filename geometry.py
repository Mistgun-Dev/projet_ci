# coding=utf-8
import math


def rectangle_area(longueur, largeur):
    """
    @brief Calcule l'aire d'un rectangle.

    @param longueur: La longueur du rectangle.
    @param largeur: La largeur du rectangle.
    @return L'aire du rectangle.
    """
    return longueur * largeur


def rectangle_perimeter(longueur, largeur):
    """
    @brief Calcule le périmètre d'un rectangle.

    @param longueur: La longueur du rectangle.
    @param largeur: La largeur du rectangle.
    @return Le périmètre du rectangle.
    """
    return 2 * (longueur + largeur)


def circle_area(rayon):
    """
    @brief Calcule l'aire d'un cercle.

    @param rayon: Le rayon du cercle.
    @return L'aire du cercle.
    """
    return math.pi * (rayon ** 2)

def circle_circumference(rayon):
    """
    @brief Calcule la circonférence d'un cercle.
    
    @param rayon Le rayon du cercle.
    @return La circonférence du cercle.
    """
    return 2 * math.pi * rayon