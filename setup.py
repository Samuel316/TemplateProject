#!/usr/bin/env python3
# coding=utf-8
"""
Copyright Samuel Lloyd
28/06/2020
samueljohnlloyd12@gmail.com
"""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="templateproject",
    version="0.1",
    author="Samuel Lloyd",
    author_email="samueljohnlloyd12@gmail.com",
    description="",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">3.7",
)
