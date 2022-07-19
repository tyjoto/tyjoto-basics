import io
import os
import re

from setuptools import setup
"""

try:
    from setuptools import setup
except ImportError:
    from distutiles.core import setup

def read(*names, **kwargs):
    with io.open(
            os.path.join(os.path.dirname(__file__),*names),
            encoding=kwargs.get("encoding","utf8")
            ) as fp:
         return fp.read()


def find_version(*file_paths):
    version_file=read(*file_paths)
    print(version_file)
    version_match = re.search(r"^__version__=['\"]([^'\"]*)['\"]",
            version_file,re.M)
    print(version_match)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

version = find_version('basic','__init__.py')
"""

version = '0.2.0'

with open("README.md", "r") as fh:
        long_description = fh.read()

setup(
        name="tyjoto-basics",
        description="Some fundalmental functions I use elsewhere",
        version=version,
        author="tyjoto",
        author_email="tyjoto@gmail.com",
        url="htpps://github.com/tyjoto/tyjoto-basics",
        packages=['basic'],
        license="Apache-2.0",
        long_description=long_description,
        install_requires=['numpy','matplotlib'],

        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: Apache Software License',
            'Natural Language :: English',
            'Operating System :: POSIX',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: MacOS :: MacOS X',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
        ],


)
