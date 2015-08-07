'''
Flask-Hashing
-------------

An extension providing easy hashing using the ``hashlib`` module.
'''
import hashlib
try:
    from hashlib import algorithms as algs
except ImportError:
    from hashlib import algorithms_available as algs
from sys import version_info


VER = version_info[0]


class Hashing(object):
    '''An extension that provides easy hashing and comparing of hashes to a
    Flask application. This extension uses the standard library ``hashlib``
    to allow access to any available hash functions on the system via OpenSSL,
    depending on your version of Python in use.
    The ``hashlib`` module guarantees access to ``md5``, ``sha1``, ``sha224``,
    ``sha256``, ``sha384``, and ``sha512``.

    To begin using this extension you must first wrap the application.::

        from flask import Flask
        from flask.ext.hashing import Hashing

        app = Flask(__name__)
        hashing = Hashing(app)

    If you prefer to use the factory pattern you can also use :class: as follows:::
    
        from flask import Flask
        from flask.ext.hashing import Hashing

        hashing = Hashing()
        # do some stuff
        app = create_app()
        hashing.init_app(app)

    If you would like to customize your instance of :class:, you may specify values
    for HASHING_METHOD and HASHING_ROUNDS in the Flask application configuration.
    HASHING_METHOD defaults to ``sha256`` and HASHING_ROUNDS defaults to 1. If you
    are using anything less than Python 2.7.9 you will only have the guaranteed
    functions provided by ``hashlib``. Python 2.7.9 or higher allows access to OpenSSL
    hash functions. The name you supply to HASHING_METHOD must be valid to ``hashlib``.
    To get a list of valid names, supply a random string to HASHING_METHOD and check
    the output when initializing your application (it raises and exception), or check
    ``hashlib.algorithms`` for Python 2.7.8 or less, or ``hashlib.algorithms_available``
    if using Python 2.7.9+.
    '''
    algorithm = 'sha256'
    rounds = 1

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        '''Initializes the Flask application with this extension. It grabs
        the necessary configuration values from ``app.config``, those being
        HASHING_METHOD and HASHING_ROUNDS. HASHING_METHOD defaults to ``sha256``
        but can be any one of ``hashlib.algorithms``. HASHING_ROUNDS specifies
        the number of times to hash the input with the specified algorithm.
        This defaults to 1.

        :param app: Flask application object
        '''
        self.algorithm = app.config.get('HASHING_METHOD', 'sha256')
        if self.algorithm not in algs:
            raise ValueError('{} not one of {}'.format(self.algorithm, algs))
        self.rounds = app.config.get('HASHING_ROUNDS', 1)
        if not isinstance(self.rounds, int):
            raise TypeError('HASHING_ROUNDS must be type int')

    def hash_value(self, value, salt=''):
        '''Hashes the specified value combined with the specified salt.
        The hash is done HASHING_ROUNDS times as specified by the application
        configuration.

        An example usage of :class:``hash_value`` would be::

            val_hash = hashing.hash_value('mysecretdata', salt='abcd')
            # save to a db or check against known hash

        :param value: The value we want hashed
        :param salt: The salt to use when generating the hash of ``value``. Default is ''.
        :return: The resulting hash as a string
        :rtype: str
        '''
        def hashit(value, salt):
            h = hashlib.new(self.algorithm)
            tgt = salt+value
            h.update(tgt)
            return h.hexdigest()

        def fix_unicode(value):
            if VER < 3 and isinstance(value, unicode):
                value = str(value)
            elif VER >= 3 and isinstance(value, str):
                value = str.encode(value)
            return value

        salt = fix_unicode(salt)
        for i in range(self.rounds):
            value = fix_unicode(value)
            value = hashit(value, salt)
        return value

    def check_value(self, value_hash, value, salt=''):
        '''Checks the specified hash value against the hash of the provided
        salt and value.

        An example usage of :class:`check_value` would be::

            val_hash = hashing.hash_value('mysecretdata', salt='abcd')
            if hashing.check_value(val_hash, 'mysecretdata', salt='abcd'):
                # do something special

        :param value_hash: The hash value to check against
        :param value: The value we want hashed to compare
        :param salt: The salt to use when generating the hash of ``value``. Default is ''.
        :return: True if equal, False otherwise
        :rtype: bool
        '''
        h = self.hash_value(value, salt=salt)
        return h == value_hash
