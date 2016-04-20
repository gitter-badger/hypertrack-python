HyperTrack Python Bindings
==========================
[![Build Status](https://travis-ci.org/hypertrack/hypertrack-python.png)](https://travis-ci.org/hypertrack/hypertrack-python/)
[![Pypi](https://badge.fury.io/py/hypertrack.png)](http://badge.fury.io/py/hypertrack)
[![Coverage Status](https://coveralls.io/repos/github/hypertrack/hypertrack-python/badge.svg?branch=master)](https://coveralls.io/github/hypertrack/hypertrack-python?branch=master)
[![Code Health](https://landscape.io/github/hypertrack/hypertrack-python/master/landscape.png)](https://landscape.io/github/hypertrack/hypertrack-python/master)

A python wrapper for the [HyperTrack api](http://docs.hypertrack.io).

Installation
------------
```
pip install hypertrack
```

Usage
------

You'll need your hypertrack secret key. You can find this from your account page.
Then, you can just import hypertrack and set your secret key on it.

```python
import hypertrack

hypertrack.secret_key = 'c237rtyfeo9893u2t4ghoevslsd'

customer = hypertrack.Customer.create(
    name='John Doe',
    email='john@customer.com',
    phone='+15555555555',
)

print customer
```

Documentation
-------------

For detailed documentation of the methods available, please visit the official [HyperTrack API documentation](http://docs.hypertrack.io).

Testing
-------
