#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Fichier: test_incert.py
# Auteur: Marc COATANHAY

"""
    Test pour le module incert.
"""

# Import des modules
from incert import acos, Incert, i, pi, zero
import unittest

class IncertTest(unittest.TestCase):
    def test_acos(self):
        self.assertEqual(acos(0), pi/2)

if (__name__ == "__main__"):
    unittest.main()