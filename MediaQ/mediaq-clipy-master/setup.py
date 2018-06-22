import sys
from setuptools import setup, find_packages



# To install the library, open a Terminal shell, then run this
# file by typing:
#
# python setup.py install
#
# You need to have the setuptools module installed.
# Try reading the setuptools documentation:
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.10", "six >= 1.9", "certifi"]

setup(
    name="SwaggerMediaq",
    version="1.0.0",
    description="MediaQ API",
    author_email="mediaq.imsc@gmail.com",
    url="http://local.eclipse.org",
    keywords=["Swagger", "MediaQ API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    An API to access MediaQ data
    """
)










