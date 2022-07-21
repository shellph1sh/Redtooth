# Redtooth
Bluetooth DOS (Denial of service) and manipulation software.

## Showcase 
<p align="left">
   <img src="https://user-images.githubusercontent.com/55106700/180107134-171fcc54-18f2-4a16-944f-9a2ae7a32bcb.png" width="770" height="490">
</p>


<p align="left">
   <img src="https://user-images.githubusercontent.com/55106700/180120594-393711a4-de96-411a-a261-9719e6b05fe2.gif" width="770" height="490">
</p>




## General Info
I AM NOT LIABLE FOR ANY DAMAGE OR MISUSE OF THIS SOFTWARE, AS THIS SOFTWARE IS UNDER THE RESPONSIBILITY OF THE END USER.
THIS SOFTWARE IS MEANT FOR EDUCATIONAL PURPOSES ONLY.

## Dependencies
### software
- BlueZ official Linux Bluetooth protocol stack (included in most distros)

### Python
 - pybluez
 - art
 - alive-progress
 
 ## Installation

 1. Run ```sudo git clone https://github.com/Lionskey/Redtooth.git```
 2. Then ```cd Redtooth```
 3. Run the ```setup.py``` file for pip related dependencies with ```sudo python3 setup.py```
 
 After running ```sudo python3 setup.py``` Redtooth will be installed globally and can be called from the command ```redtooth```
 in your favorite terminal.
 
 ### For Gentoo users
 (For gentoo users, pip does not function without the user flag, so just go into ```setup.py``` and change every ```-U``` to ```--user```)
 
 ## Removal
 
 To uninstall redtooth just delete the binary saved under ```/usr/bin/redtooth```
 ```
 sudo rm -rf /usr/bin/redtooth
 ```
 and delete the main library directory that the binary leads to under ```/usr/lib/Redtooth```
 ```
 sudo rm -rf /usr/lib/Redtooth
 ```

## Extra Note
Currently the PyBlueZ library is not under active development and have a current problem with their pip installation.
The setup.py file installs the PyBlueZ library from source.
