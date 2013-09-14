**Author:** Jacob Magnusson. [Follow me on Twitter](twitter)

## About

Generate empty packages with sane defaults, for publishing to GitHub.

Currently only supports generating python packages. Features for
python include:

* Generates .gitignore, AUTHORS, CHANGELOG,
  LICENSE (BSD simplified by default), MANIFEST.in, README.md,
  requirements.txt, setup.py, tests.py and tox.ini.
* Sets your name, github username, package name in the templates by
  reading a config that should be located @ ~/.config/pkgtmpl.ini or where
  you specify
* Optional: Add Travis CI status and twitter account to the readme
* Sets your name and year in the copyright notice of the license file


## Installation

    $ git clone https://github.com/jmagnusson/pkgtmpl.git
    $ pip install -r requirements.txt


## Usage

Basic example:

    $ ./generate mypackage ~/apps/mypackage

For more options, issue the following:

    $ ./generate --help


## Python support

Should support most Python 2 versions. Python 3 needs to be 3.3 or higher
because of the usage of unicode literals.


## Documentation
[docs]


[twitter]: https://twitter.com/pyjacob
[docs]: https://github.com/jmagnusson/pkgtmpl