#!/usr/bin/python3

# in test_fancy.py
from nose2.tools import params

@params("Sir Bedevere", "Miss Islington", "Duck")
def test_is_knight(value):
        assert value.startswith('Sir')

