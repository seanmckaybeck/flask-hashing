# Flask-Hashing

Flask-Hashing is a Flask extension that provides an easy way to
hash data and check a hash of a value against a given hash.
Flask-Hashing uses `hashlib` to actually hash data.

This extension prevents the user from needing to worry about how
to hash data. Instead, developers are provided a simple call to
do any necessary hashing of data.

This extension is intended to be used in place of Flask-Bcrypt,
if the user so desires. Not everyone may want to use `bcrypt`
for their hashing needs, and this provides a way to handle that
use case.

## Installation

```
$ pip install flask-hashing
```

or if you don't have `pip`:

```
$ easy_install flask-hashing
```

## Usage

```
from flask import Flask
from flask.ext.hashing import Hashing

app = Flask(__name__)
hashing = Hashing(app)
```

After creating an instance of `Hashing`, we can hash data and
check hashes of data as follows:

```
h = hashing.hash_value('secretdata', salt='abcd')
if hashing.check_value(h, 'secretdata', salt='abcd'):
    # do some stuff because the hashes are equal
```

## Tests

Run

```
$ python setup.py test
```

or

```
$ python test_hashing.py
```

## Documentation

Install `sphinx` then in the `docs` directory run `make html`.

You can see a live copy of the docs at [Read the Docs](http://flask-hashing.readthedocs.org/en/latest/).
