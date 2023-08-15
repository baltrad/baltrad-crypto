#!/usr/bin/env python
import setuptools
import sys

REQUIRED_PACKAGES= [
    "python3-pycryptodomex"
]

setuptools.setup(name="baltrad.crypto",
    version="0.1-dev",
    namespace_packages=["baltrad"],
    zip_safe=False,
    packages=setuptools.find_packages(
        "src",
        exclude=["*.tests.*", "*.tests"],
    ),
    package_dir={
        "": "src"
    },
    install_requires=REQUIRED_PACKAGES,
)
