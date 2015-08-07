"""
Flask-Hashing
-------------

This is a Flask extension that provides utility functions
for hashing data within a Flask application.

Flask-Bcrypt restricts you to using bcrypt. What if you want
to use a different hash function? This extension provides access
to other commonly used hash functions such as SHA256.

Links
-----


"""
from setuptools import setup


setup(
    name='Flask-Hashing',
    version='1.1',
    url='https://github.com/ThaWeatherman/flask-hashing',
    license='MIT',
    author='Sean Beck',
    author_email='seanmckaybeck@gmail.com',
    description='Easy hashing of data in Flask',
    long_description=__doc__,
    py_modules=['flask_hashing'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite='test_hashing'
)
