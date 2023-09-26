README
======


About
-----
Baltrad Crypto, provides the cryptographic routines used when exchanging data as part of the BALTRAD project.

Setting up development
----------------------
This description is valid for RedHat 8 based distributions. Other distributions requires installation from source for both bdb and hlhdf.

First, you will need to get the baltrad package repository and the dependencies installed. As super user

.. code:: sh

   %> cd /etc/yum.repos.d/
   %> wget http://rpm.baltrad.eu/CentOS/8/latest/baltrad-package-latest.repo
   %> sudo dnf install python3-lockfile python3-pycryptodomex python3-numpy 
   %> sudo dnf install python3-paramiko python3-scp
   
Fetch the baltrad-crypto project by downloading it from github as your ordinary user

.. code:: sh

   %> cd /projects
   %> git clone https://github.com/baltrad/baltrad-crypto.git
   %> cd baltrad-crypto

The easiest way to start developing in baltrad-crypto is to create a virtual environment that will be used for local installations and tests. 

.. code:: sh

   %> python3 -m venv --system-site-packages env
   %> . env/bin/activate

With the virtual environment created you can just install the baltrad-crypto software into your own environment by typing

.. code:: sh

  %> python3 setup.py install

Installation
------------
The installation of the software can either be done in a similar way to how the development environment is setup. You can either decide to
use a virtual environment for running the software or you can just install it without creating the virtual environment.

There is a third alternative as well and that is to use the prebuilt packages av available for the RH 8 distributions which is done by
running:

.. code:: sh

   %> sudo dnf install baltrad-crypto




