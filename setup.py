import os

missingLibrary = False
print("Verifying required libraries...")
try:
  import art
  
except ModuleNotFoundError:
  missingLibrary = True
  print("Could not find a required library. Installing...")
  os.system("pip install -U art")
  print("Done!")

try:
  import bluetooth
  
except ModuleNotFoundError:
  missingLibrary = True
  print("Could not find a required library. Installing...")
  os.system("git clone https://github.com/pybluez/pybluez.git")
  os.system("python3 pybluez/setup.py install")
  os.system("sudo rm -rf pybluez")
  print("Done!")

try:
  import alive_progress
  
except ModuleNotFoundError:
  missingLibrary = True
  print("Could not find a required library. Installing...")
  os.system("pip install -U alive-progress")
  print("Done!")


if missingLibrary:
  print("Restarting to refresh content...")
  import bluey
  exit()

