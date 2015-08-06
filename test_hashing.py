import unittest

from flask import Flask
from flask.ext.hashing import Hashing

class MyTest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['HASHING_METHOD'] = 'sha256'
        self.h = Hashing(self.app)

    def test_hash_capability(self):
        val = 'somethingsecret'
        salt = 'abcd'
        valhash = self.h.hash_value(val, salt)
        self.assertTrue(self.h.check_value(valhash, val, salt))
        self.assertFalse(self.h.check_value(valhash, val, 'efgh'))
        self.assertFalse(self.h.check_value(valhash, val+'poop', salt))

    def test_multiple_rounds(self):
        self.app.config['HASHING_ROUNDS'] = 5
        self.h = Hashing(self.app)
        self.test_hash_capability()

    def test_different_algorithm(self):
        self.app.config['HASHING_METHOD'] = 'md5'
        self.h = Hashing(self.app)
        self.test_hash_capability()

    def test_rounds_not_int(self):
        self.app.config['HASHING_ROUNDS'] = 'notanint'
        self.assertRaises(TypeError, Hashing().init_app, self.app)
        self.app.config['HASHING_ROUNDS'] = 1

    def test_algorithm_not_valid(self):
        self.app.config['HASHING_METHOD'] = 'notahashalgorithm'
        self.assertRaises(ValueError, Hashing().init_app, self.app)


if __name__ == '__main__':
    unittest.main()
