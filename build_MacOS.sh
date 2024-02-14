#!/usr/bin/env bash

# Builds a distributable binary on MacOS

rm -r {build,dist,rbc2xl.spec}

# Using onedir mode since onefile looks neater, but startup time is woeful...
pyinstaller rbc2xl.py -w --onedir