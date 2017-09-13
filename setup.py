# -*- coding:utf-8 -*-

from setuptools import find_packages, setup

README = """# candy_utils
"""


setup(
    name='candy_utils',
    version='0.0.1',
    description='useful python snips',
    long_description=README,
    author='程飞',
    url='https://github.com/faycheng/candy_utils.git',
    packages=find_packages(exclude=['tests']),
    install_requires=['pytest==3.2.1'],
    entry_points={
        'console_scripts': [],
    },
    zip_safe=True,
    license='MIT License',
    classifiers=['development status :: 1 - planning', 'programming language :: python :: 3 :: only', 'topic :: software development :: libraries', 'environment :: macos x']
)