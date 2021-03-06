#!/usr/bin/env python
"""
Installs ViperMonkey using pip, setuptools or distutils

To install this package, run:
    pip install -e .

Or:
    python setup.py install

Installation using pip is recommended, to create scripts to run vmonkey
and vbashell from any directory.
"""

#--- CHANGELOG ----------------------------------------------------------------

# 2016-12-14 v0.04 PL: - replaced scripts by entry points (issue #17)

#--- TODO ---------------------------------------------------------------------


#--- IMPORTS ------------------------------------------------------------------

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# --- ENTRY POINTS ------------------------------------------------------------

# Entry points to create convenient scripts automatically

entry_points = {
    'console_scripts': [
        'vmonkey=vipermonkey.vmonkey:main',
        'vbashell=vipermonkey.vbashell:main',
    ],
}


setup(
    name="vipermonkey",
    version="0.05",  # not compliant with PEP440, setuptools normalizes to 0.2
    description=(
        "ViperMonkey is a VBA Emulation engine written in Python, designed to "
        "analyze and deobfuscate malicious VBA Macros contained in Microsoft "
        "Office files (Word, Excel, PowerPoint, Publisher, etc)."),
    long_description=open("README.md").read(),
    install_requires=["oletools", "prettytable", "colorlog", "colorama",
                      "pyparsing"],
    packages=["vipermonkey", "vipermonkey.core"],
    #scripts=["vipermonkey/vmonkey.py", "vipermonkey/vbashell.py"],
    entry_points=entry_points,
    author="Philippe Lagadec",
    url="https://github.com/decalage2/ViperMonkey",
    license="BSD",
    download_url="https://github.com/decalage2/ViperMonkey",
)
