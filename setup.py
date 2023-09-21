#!/usr/bin/env python
import setuptools
import sys

REQUIRED_PACKAGES= [
    "pycryptodomex",
    "pyasn1"
]

setuptools.setup(name="baltradcrypto",
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
    entry_points = {
        "baltradcrypto.config.commands": [
            "create_keys = baltradcrypto.client.cfgcmd:CreateKeys"
        ],
        "console_scripts" : [
            "baltrad-crypto-config = baltradcrypto.config_main:run"
        ]
    },
    test_suite="nose.collector",
    tests_require=[
        "mock >= 0.7",
    ],
    
)
