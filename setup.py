#!/usr/bin/env python

from setuptools import setup, find_packages
import subprocess

version = subprocess.check_output(["git", "describe", "--tags"]).strip().decode('utf-8')
setup(name="bigone-sdk-py",
      version=version,
      description="A Python SDK for BigOne (https://big.one)",
      maintainer="Halimao",
      maintainer_email="halimao.lin@gmail.com",
      url = "https://github.com/Halimao/bigone-sdk-py",
      install_requires = ['requests', 'pyjwt'],
      packages=find_packages('.'),
     )
