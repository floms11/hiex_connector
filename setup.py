import re

from setuptools import find_packages, setup

PACKAGE_NAME = 'hiex_connector_admin'
SOURCE_DIRECTORY = 'hiex_connector'
SOURCE_PACKAGE_REGEX = re.compile(rf'^{SOURCE_DIRECTORY}')

source_packages = find_packages(include=[SOURCE_DIRECTORY, f'{SOURCE_DIRECTORY}.*'])
proj_packages = [SOURCE_PACKAGE_REGEX.sub(PACKAGE_NAME, name) for name in source_packages]

setup(
    name=PACKAGE_NAME,
    version='1.0',
    packages=proj_packages,
    package_dir={PACKAGE_NAME: SOURCE_DIRECTORY},
    url='https://docs.hiex.io',
    license='',
    author='hiex',
    author_email='support@hiex.io',
    description=''
)
