Mac Icon Generator
==================

A simple script I created in order to expedite the process of creating thumbnail and image assets for macOS and iOS in order to
populate the Icon assets, since it can be a pain to manually resize images if you're making no real changes besides the dimension
changes.

Prerequisites
-------------

Besides the latest stable Python 2.* version, you will also need the Python Imaging Library, which has been forked and is being
maintained here: (https://pillow.readthedocs.io/en/3.0.0/installation.html)

If you have the latest `pip` installed, you should be able to use `sudo pip install Pillow`, but can install more manually from source
if you prefer.

Usage
-----

Usage is `python iconGen.py [path to png]`.
The target png must have square dimensions and be at least 1024x1024 px, or the program will complain and raise errors regarding this.
Upon successful completion, in the directory where the target image is there will be a directory called `IconGenTumbnails`
which contain the processed icons in separate macOS and iOS folders.
