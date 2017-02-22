from setuptools import setup

setup(
    name="name2gender",
    version="0.1",

    description="Useful script to find out a gender from a Czech name",
    url="https://github.com/Thyrst/name2gender",

    author="Thyrst",
    author_email="thyrst@seznam.cz",

    license="MIT",

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 3 - 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Czech",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.6",
    ],

    keywords="gender names",
    py_modules=["name2gender"],
)