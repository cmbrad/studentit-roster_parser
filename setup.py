#!/usr/bin/env python

from setuptools import setup, find_packages
print(find_packages(exclude=['tests*']))

setup(
	name='sit-roster',
	version='0.0.1',
	description='StudentIT Rostering Application',
	author='Christopher Bradley',
	author_email='chris.bradley@unimelb.edu.au',
	packages=find_packages(exclude=['tests*']),
	entry_points={
		'console_scripts': [
			'sit-roster=bin.entry:cli',
		],
	},
)
