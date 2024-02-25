#!/usr/bin/env python

from setuptools import setup, find_packages
import urllib.request
import json

data = urllib.request.urlopen("https://api.github.com/repos/Halimao/bigone-sdk-py/releases/latest").read().decode('utf-8')

version = json.loads(data)["tag_name"]
setup(name="bigone-sdk-py",
      version=version,
      description="A Python SDK for BigOne (https://big.one)",
      long_description="A Python SDK for BigOne (https://big.one)",
      maintainer="Halimao",
      maintainer_email="halimao.lin@gmail.com",
      url = "https://github.com/Halimao/bigone-sdk-py",
      install_requires = ['requests', 'pyjwt'],
      packages=find_packages('.'),
     )
