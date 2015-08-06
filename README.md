# Flask-Hashing

Flask-Hashing is a Flask extension that provides an easy way to
hash data and check a hash of a value against a given hash.
Flask-Hashing uses `hashlib` to actually hash data.

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

FILL ME IN
