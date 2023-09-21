#!/usr/bin/env python
import setuptools
import sys

REQUIRED_PACKAGES= [
    "python3-pycryptodomex"
]

setuptools.setup(name="baltradcrypto.crypto",
    version="0.1.dev0",
    namespace_packages=["baltradcrypto"],
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
