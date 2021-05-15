from setuptools import setup, find_packages

version = '0.1.2'

with open('README.md', 'r', encoding = 'utf-8') as f:
  long_description = f.read()

setup(
        name = 'googlesearch',
        version = version,
        description = 'A module that searches google lmao',
        long_description = long_description,
        long_description_content_type = 'text/markdown',
        url = 'https://github.com/Sengolda/googlesearch',  
        author = 'Sengolda',
        license = 'MIT', 
        packages = find_packages(),
)
