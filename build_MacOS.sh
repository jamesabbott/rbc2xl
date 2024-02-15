#!/usr/bin/env bash

# Builds a distributable package on MacOS

paths=('build' 'dist' 'rbc2xl.spec')

for path in ${paths[@]}; do 
	if [[ -e "$path" ]]; then
		rm -rv "$path"
	fi
done

PYINST=$(which pyinstaller)
if [[ -z "$PYINST" ]]; then
	echo "pyinstaller not available..."
	exit 1
fi

$PYINST rbc2xl.py -w --onefile
