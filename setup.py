from distutils.command import install_lib
from setuptools import setup
import os

setup(name="dlhelpertools",
      version="0.1.1",
      packages=["dlhelpertools"],
      install_requires=["numpy","opencv-python"]
      
      )