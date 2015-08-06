Flask-Hashing
==============

.. module:: flask.ext.hashing

Flask-Hashing is a Flask extension that provides an easy way to
hash data and check a hash of a value against a given hash.
Flask-Hashing uses `hashlib` to actually hash data.

The main use case for hashing in web applications is for user
passwords. But because an application may have a different need
for a hash function, this extension's naming choices are not
password-specific.

Installation
------------

Install Flask-Hashing with either of the following commands:::

    $ easy_install flask-hashing
    $ pip install flask-hashing

Usage
-----

Initialize the extension as follows:::

    from flask import Flask
    from flask.ext.hashing import Hashing

    app = Flask(__name__)
    hashing = Hashing(app)

After creating an instance of `Hashing`, we can hash data and
check hashes of data as follows:::

    h = hashing.hash_value('secretdata', salt='abcd')
    if hashing.check_value(h, 'secretdata', salt='abcd'):
        do some stuff because the hashes are equal

And that is all there is to it!

API
---

.. autoclass:: flask.ext.hashing.Hashing
    :members:
