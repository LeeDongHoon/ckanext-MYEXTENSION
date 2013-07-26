from setuptools import setup, find_packages
import sys, os

version = '2.0'

setup(
	name='ckanext-MYEXTENSION',
	version=version,
	description="custom field",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='ldhspace',
	author_email='ldhspace@yahoo.co.kr',
	url='',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.MYEXTENSION'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
	# Add plugins here, eg
	# myplugin=ckanext.MYEXTENSION:PluginClass
	""",
)
