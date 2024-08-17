from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:

    requirements_list = List[str] = []

    return requirements_list




setup (

    name = "Sensor",
    version = "0.0.1",
    author = "Prabhakar",
    author_email = "Prabhakarkumar313@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements(),
)


