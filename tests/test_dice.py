import unittest

import app

def test_test():
    assert app.test() == "Works!"
    assert app.hello() == "Goodbye World"
