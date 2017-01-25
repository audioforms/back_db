import unittest
from flask import Flask
from flask_testing import TestCase
from main_doc import *

class MyTest(TestCase):
    def create_app(self):
        main.app.run(debug=True)
        return main.app

def test_app_basic():
    a = MyTest()
    a.create_app()

if __name__ == '__main__':
    unittest.main()
