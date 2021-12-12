# ColabCode

[![license](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)
![python version](https://img.shields.io/badge/python-3.6%2C3.7%2C3.8-blue?logo=python)


## Installation

```
$ pip install codeONssh
```

Run code on Google Colab or Kaggle Notebooks

## Getting Started

codeONssh also has a command-line script. So you can just run `colabcode` from command line.

`codeONssh -h` will give the following:

```
usage: codeONssh [-h] --port PORT [--password PASSWORD] [--mount_drive]

CodeONssh: Run Code On Colab / Kaggle Notebooks

required arguments:
  --port PORT          the port you want to run code-server on

optional arguments:
  --password PASSWORD  password to protect your code-server from unauthorized access
  --mount_drive        if you use --mount_drive, your google drive will be mounted
```

Else, you can do the following:


```shell

# import codeONssh
$ from codeONssh import CodeONssh

# run codeONssh with by deafult options.
$ CodeONssh()

# CodeONssh has the following arguments:
# - port: the port you want to run code-server on, default 10000
# - password: password to protect your code server from being accessed by someone else. Note that there is no password by default!
# - mount_drive: True or False to mount your Google Drive

$ CodeONssh(port=10000, password="Your password", mount_drive=True)
```
## How to use it?
CodeONssh starter notebook: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/abhishekkrthakur/colabcode/blob/master/colab_starter.ipynb)

## License

[MIT](LICENSE)
