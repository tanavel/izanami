# izanami

## TOC
- [izanami](#izanami)
  - [TOC](#toc)
  - [About](#about)
    - [Built With](#built-with)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
  - [Contact](#contact)


## About
Set up your Mac setting with Ansible.

### Built With
- [Ansible](https://github.com/ansible/ansible)
- [pipenv](https://github.com/pypa/pipenv)
- [pyenv](https://github.com/pyenv/pyenv)
- [Homebrew](https://brew.sh/)

## Getting Started
### Prerequisites
- pyenv
  ```
  brew install pyenv
  ```
- pipenv
  ```
  brew install pipenv
  ```

### Installation
- Clone the repo
  ```
  git clone git@github.com:tanavel/izanami.git
  ```
- Install Python3.9.1
  ```
  cd izanami
  pyenv install 3.9.1
  pyenv local 3.9.1
  ```
- Create virtualenv
  ```
  pipenv install --python 3.9.1
  ```

## Usage
- Execute playbook
  ```
  pipenv run ansible-playbook site.yml
  ```

## Contact
tanavel - [@tanavel1118](https://twitter.com/tanavel1118) - tanavel1118@gmail.com
