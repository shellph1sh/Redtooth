# Bluey
Bluetooth Manipulation Software for GNU/Linux based operating systems systems

## General Info
I am not responsible for any damages or misuse of this software.
I will assume no liability as this software is under the responsibility of the end user

This software has only been tested so far on a kali-everything live image

## Installation
currently one of the dependencies for this software, the python3 PyBluez module does not work through pip.
so a source installation is required
```
git clone https://https://github.com/pybluez/pybluez.git
cd pybluez
sudo python3 setup.py install
cd ..
sudo rm -rf pybluez
```
after that install the pip dependencies for Bluey

```
python3 setup.py
```

## Dependencies
### software
- l2ping
- BlueZ official Linux Bluetooth protocol stack

### Python
 - pybluez
 - art
 - alive-progress
