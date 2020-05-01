from setuptools import setup, find_namespace_packages

def readme():
    with open('README.md','r') as file:
        return file.read()
    
setup(name    = 'deckutil',
      version = '0.0.6',
      description = 'A set of tools to make data analysis a bit less painful. Built in functions that include input/output managment, datetime transformations and scraping tools.',
      long_description = readme(),
      long_description_content_type = 'text/markdown',
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent"
      ],
      url = 'https://github.com/juandeckard/deckUtil',
      author='Juan Manuel Mejía Botero',
      author_email='juan@deckardtech.com',
      keywords = 'Data Analysis Normalization Input Time Visualization',
      license = 'MIT',
      packages=find_namespace_packages(where='src'),
      package_dir={'': 'src'},
      install_requires=['pandas>=0.25.1','python-dateutil>=2.8.0','folium>=0.10.1','xlrd>=1.2.0'],
      include_package_data = True,
      python_requires='>=3',
      zip_safe = False)