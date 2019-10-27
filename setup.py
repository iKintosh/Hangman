#!/usr/bin/env python3

"""Setup script."""

from setuptools import setup

setup(
    name="hangman",
    version="0.0.1",
    author="Andrey Alekseev",
    author_email="iLekseev@gmal.com",
    url="https://github.com/iKintosh/Hangman",
    license="MIT",
    packages=[
        "hangman",
    ],
    install_requires=[
        "numpy",
        "mock",
        "pytest"
    ],
    setup_requires=[
        "pytest-runner",
        "pytest-pylint",
        "pytest-pycodestyle",
        "pytest-pep257",
        "pytest-cov",
    ],
    tests_require=[
        "pytest",
        "pylint",
        "pycodestyle",
        "pep257",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ]
)
