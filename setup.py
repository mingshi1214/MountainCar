from setuptools import setup, find_packages
import sys

setup(name='mountaincargym',
        py_modules=['mountaincargym'],
        install_requires=[
            'gym',
            'matplotlib',
            'numpy',
        ],
        description='Trying to make mountain car',
        author='Mingshi'
        url='https://github.com/mingshi1214/MountainCar',
        version='0.0')
