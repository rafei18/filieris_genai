from setuptools import find_packages,setup

setup(name="filieris-bot",
       version="0.0.1",
       author="Rafei",
       author_email="rafei.tchouar@gmail.com",
       packages=find_packages(),
       install_requires=['langchain-astradb','langchain'])