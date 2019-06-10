# Installation

The Pacifica software is available through PyPi so creating a virtual
environment to install is what is shown below. Please keep in mind
compatibility with the Pacifica Core services.

## Installation in Virtual Environment

These installation instructions are intended to work on both Windows,
Linux, and Mac platforms. Please keep that in mind when following the
instructions.

Please install the appropriate tested version of Python for maximum
chance of success.

### Linux and Mac Installation

```
mkdir ~/.virtualenvs
python -m virtualenv ~/.virtualenvs/pacifica
. ~/.virtualenvs/pacifica/bin/activate
pip install pacifica-policy
```

### Windows Installation

This is done using PowerShell. Please do not use Batch Command.

```
mkdir "$Env:LOCALAPPDATA\virtualenvs"
python.exe -m virtualenv "$Env:LOCALAPPDATA\virtualenvs\pacifica"
& "$Env:LOCALAPPDATA\virtualenvs\pacifica\Scripts\activate.ps1"
pip install pacifica-policy
```
