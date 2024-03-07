#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    """
    0-pascal_triangle
    """
    if n <= 0:
        return []
    
    liste_1 = []
    liste_2 = []

    for i in range(n):
        listeP = []
        for j in range(i+1):
            if j == 0 or j == i:
                listeP.append(1)
            else:
                liste_2 = liste_1[i-1]
                listeP.append(liste_2[j-1] + liste_2[j])
        liste_1.append(listeP)
    return liste_1
