from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pymugi",
    version="0.1.2",
    packages=["pymugi"],
    author="Gareth Bryan",
    author_email="gareth@mx9.org",
    url="https://github.com/wh1terat/pymugi",
    keywords="hitachi mugi crypto prng",
    description="Native Python3 implementation of Hitachi's Mugi PRNG",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GPLv3",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Security :: Cryptography",
        "Programming Language :: Python :: 3.6",       
        "Programming Language :: Python :: 3 :: Only",
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    zip_safe=True,
    python_requires='>3.6',
)
