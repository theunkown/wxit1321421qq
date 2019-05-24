#!/usr/bin/python #!/usr/bin/env python
#
# Netmaxiot Python Setup
#
# The Netmaxiot connects the Raspberry Pi 
'''
Netmaxiot for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2017  Netmax  Technologies 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

'''

try:
	with open('package_description.rst', 'r') as file_description:
		description = file_description.read()

except IOError:
	description = "Check more on https://netmax.co.in/Netmaxiot"

with open('requirements.txt') as fp:
    install_requires = fp.read()

# To install the Netmaxiot library systemwide, use: sudo python setup.py install
import setuptools
import os
import sys
import shutil

# from setuptools.command.develop import develop
# from setuptools.command.install import install

temp_dir = '.tmp_modules'

# read the module names and append the .py extension
with open('package_modules.txt', 'r') as fmodules:
    modules = fmodules.readlines()
    modules = list(map(lambda mod: mod.strip() + '.py', modules))

# create .tmp_modules directory
# and make sure to have it clean before proceeding further
try:
	os.mkdir(temp_dir)
except FileExistsError:
	shutil.rmtree(temp_dir)
	os.mkdir(temp_dir)

# copy modules from all over the place to the designated
# temporary directory
to_copy_modules = []
for root, dirs, files in os.walk('.'):
    for file in files:
	    if file in modules:
		    to_copy_modules.append(root + '/' + file)
for module in to_copy_modules:
    print('Copying to ' + temp_dir + ' module ' + module)
    shutil.copy(module, temp_dir)

# the same for develop and build, just import the right modules
# class PostInstallCommand(install):
#     """Post-installation for installation mode."""
#     def run(self):
# 		"""Post Install Commands Here"""
#         install.run(self)

setuptools.setup(
	# cmdclass={
    #     'develop': PostDevelopCommand,
    #     'install': PostInstallCommand,
    # },

    name = "Netmaxiot",
    version = "1.0.4",

    description = "Drivers for using the Netmaxiot+ in Python",
    long_description = description,

    author = "Netmax  technologies Rohit Khosla",
    author_email = "er.rohitkhosla@gmail.com",

    license = 'MIT',
    classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'License :: OSI Approved :: MIT License',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Topic :: Software Development :: Embedded Systems',
    'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    url = "https://github.com/Netmaxiot",

    keywords = ['robot', 'Netmaxiot', 'Netmaxiot+', 'Netmax  industries', 'learning', 'education', 'iot', 'internet of things', 'prototyping'],

	package_dir = {
		'' : temp_dir
	},

	py_modules = [script.split('.')[0] for script in os.listdir(temp_dir)],
    install_requires = install_requires,
	test_suite = 'test_script.test_suite.TestMethods'
)

# removing everything under the temp directory
shutil.rmtree(temp_dir)
