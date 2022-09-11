"""
py2app build script for MyApplication

Usage:
    python setup.py py2app
"""
from setuptools import setup
setup(
    app=["app.py"],
setup_requires=["py2app"],
)
