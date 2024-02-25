#!/usr/bin/env python

from setuptools import setup, find_packages
from bigone import VERSION

url="https://github.com/Halimao/bigone-sdk-py"

long_description="A Python SDK for BigOne (https://big.one)"

setup(name="bigone-sdk-py",
      version=VERSION,
      description=long_description,
      maintainer="Halimao",
      maintainer_email="halimao.lin@gmail.com",
      url = url,
      long_description=long_description,
      install_requires = ['requests', 'pyjwt'],
      packages=find_packages('.'),
     )
