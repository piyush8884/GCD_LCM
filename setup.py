


from setuptools import setup
import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()
def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setup(
    name='GCD_LCM',
    version='0.0.3',
    description='This project provides functions to calculate the Greatest Common Divisor (GCD) and Least Common Multiple (LCM) of two or three numbers. It includes an initial release version with the implementation of these functions, along with a README file for usage instructions',
    long_description=readme(),
    long_description_content_type="text/markdown",
    author= 'GOSWAMI GAURAV',
    author_email='gauravofficial8884@gmail.com',
    url = '',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires = []
)