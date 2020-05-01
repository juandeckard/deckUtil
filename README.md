# Deck Util
A library composed of a set of tools that focus on makeing Data Analysis less of a pain for no programmers, by giving them flexible, powerful and easy to use functionalities. From easy to use functions for input/output to mapping data with html export capabilities.

## Requirements
If you are going to be installing the library using pip or conda, you can jump to the [Installation](#installation) section down bellow, if you are going to download the project from git and work on it, you may want to setup the following first.

* Python >= 3
* Pip >= 20.1
* Pandas >= 0.25.1
* Folium  >= 0.10.1
* XLRD >= 1.2.0
* python-dateutil >= 2.8.0

It is also recommended to install Jupyter Notebook as it let's you visualize one of the main files containing examples of each function on the package.

## Installation
To install the library you can use pip, conda and there is also the option of installing it via github, but it's not recommended to do so.

### Pip
You can find the project at [https://pypi.org/project/deckutil/](https://pypi.org/project/deckutil/) with more detailed information about each version. To install the package just do write the following command in a terminal.

```sh
$ pip install deckutil
```

### Conda
The current conda version for the project is broken. We will try to fix this issue in future versions.

### Manual
In order to install the project manually, you will first need to have git installed on your computer. You will also need a few extra tools, mainly setuptools and wheel. In some cases, you may need sudo for this.

```sh
$ python -m pip install --upgrade pip setuptools wheel
```
If an error message tells you that there is no setuptools or wheel installed, try installing them using pip as follows.

```sh
$ pip install setuptools wheel
```
Open a terminal and go to the root directory of the project and type the following commands.

```sh
$ python setup.py bdist_wheel
$ python -m pip install dist/dokr-{VERSION}-py3-none-any.whl
```

Make sure to replace the version variable in the second command, you can find which version you are working with inside the setup.py.

## Usage
At this point you should be able to do something like this and the library should work fine.

```
from deckutil.time import today

print(today())
```

For more information on each individual function, go to Sandbox.ipynb, there is examples of every single function and how to use it. You can also use the doc string at any point if you need help like so.

```
print(foo.__doc__)
```

## Contributing
Pull requests are welcome. For changes, please open an issue first to discuss what you would like to change or add to the library. Also, please make sure to update tests as appropriate.