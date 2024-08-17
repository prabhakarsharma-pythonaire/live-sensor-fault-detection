from setuptools import setup, find_packages

def get_requirements()->list[str]:

    requirements_list = list[str] = []

    return requirements_list




setup (

    name = "Sensor",
    version = "0.0.1",
    author = "Prabhakar",
    author_email = "Prabhakarkumar313@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements(),
)


