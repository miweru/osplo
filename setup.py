#from distutils.core import setup
from setuptools import setup

setup(
    name="osplo",
    version="0.1.10",
    packages=["osplo"], #die enthaltenden Packages
    #scripts=[],
    license="GNU GENERAL PUBLIC LICENSE V3 OR LATER (GPLV3+)",
    author="Michael Ruppert",
    author_email="michael.ruppert@fau.de",
    description="Stellt einen langsamen Iterator über Textdateien (komprimiert, txt, online) zur Verfügung, der einen Satz pro Iteration zurückliefert.",
    long_description=open("README.md").read(),
    install_requires=[
    "somajo>=1.8.3",
    "smart_open>=1.8.0",],
    python_requires=">=3.5",
     classifiers=[
        "Programming Language :: Python :: 3",
        "LICENSE :: OSI APPROVED :: GNU GENERAL PUBLIC LICENSE V3 OR LATER (GPLV3+)",
        "Operating System :: POSIX :: LINUX",
    ],
    #package_data={
    #}
    )
    
"""
Protokoll dabei:

python3 setup.py sdist bdist_wheel
pip3 install --user dist/osplo-0.1.4-py3-non-any.whl

from osplo import OSLOpen

"""