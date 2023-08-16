#!/usr/bin/env python
import setuptools
import sys

REQUIRED_PACKAGES= [
    "python3-pycryptodomex"
]

setuptools.setup(name="bcrypto.crypto",
    version="0.1-dev",
    namespace_packages=["bcrypto"],
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
