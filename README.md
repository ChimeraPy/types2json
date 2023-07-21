# types2json
`types2json` is a Python package to generate a JSON(REST API) compatible data models from python type annotations.

## Installation
```bash
$ git clone https://github.com/chimerapy/types2json.git
$ cd types2json
$ pip install -e .
```

## Usage
This project is still in early stages of development and API hasn't been hashed out yet.

## Development and Contribution
To install the development version, clone the repository and install it using `pip` with the `test` extra. It is recommended to use a virtual environment using `virtualenv` or `conda` to avoid conflicts with other packages. To contribute a new feature, use pre-commit for code formatting.

```shell
$ conda env create -n types2json-dev python=3.10 -c defaults -c conda-forge
$ conda activate types2json-dev
$ git clone https://github.com/chimerapy/types2json.git
$ cd types2json
$ pip install -e ."[test]"
$ pre-commit install
```
