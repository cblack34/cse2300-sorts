from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='MathSort',
    version='2019.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='',
    license='',
    author='Clayton Black',
    author_email='cblack@claytontblack.com',
    description='bubble and select sorts for class',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    install_requires=[],
        entry_points={
            'console_scripts': [
                'mathsort=mathsort.cli:main',
            ],
        }
)
