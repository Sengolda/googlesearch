from setuptools import setup, find_packages

version = '0.1.0'


with open('README.md', 'r', encoding = 'utf-8') as f:
  long_description = f.read()

setup(
        name = 'googlesearch',
        version = version,
        description = 'A module that searches google lmao',
        long_description = long_description,
        long_description_content_type = 'text/markdown',
        url = '',  
        author = 'Sengolda',
        license = 'MIT', 
        classifiers = classifiers,
        packages = find_packages(),
)