#!/bin/bash

# adapted heavily from Veil-Evasion's setup file

# Print Title Function
func_title(){
  # Clear (For Prettyness)
  clear

  # Echo Title
  echo '========================================================================='
  echo ' Pwnstaller Setup Script | [Updated]: 05.04.2015'
  echo '========================================================================='
  echo ' [Web]: https://blog.harmj0y.net | [Twitter]: @harmj0y'
  echo '========================================================================='
}

# Validation Checks Function
func_validate(){
  # Check User Permissions
  if [ `whoami` != 'root' ]
  then
    echo
    echo ' [ERROR]: Either Run This Setup Script As Root Or Use Sudo.'
    echo
    exit 1
  fi

  # Check If Wine Python Is Already Installed
  if [ -f ~/.wine/drive_c/windows/system32/python27.dll ] && [ -f ~/.wine/drive_c/Python27/python.exe ]
  then
    echo
    echo " [*] Wine Python Already Installed... Skipping."
    echo
    echo ' [*] Initializing Apt Package Installation'
    func_apt_deps
    func_update_config
  else
    echo
    echo ' [*] Initializing Apt Dependencies Installation'
    func_apt_deps
    echo
    echo ' [*] Initializing Wine Python Dependencies Installation'
    func_python_deps
  fi
}

# Install Architecture Dependent Dependencies
func_apt_deps(){
  # Check For 64-bit Kernel
  if [ `uname -m` == 'x86_64' ]
  then
    echo
    echo ' [*] Adding i386 Architecture To x86_64 System'
    dpkg --add-architecture i386
    echo
    echo ' [*] Updating Apt Package Lists'
    apt-get update
    echo
    echo ' [*] Installing Wine i386 Binaries'
    apt-get install wine-bin:i386
  fi

  # Start Apt Dependency Install
  echo
  echo ' [*] Installing Apt Dependencies'
  apt-get install mingw-w64 wine python
}

# Install Wine Python Dependent Dependencies
func_python_deps(){
  # Install Wine Python and Dependencies
  # Download required files, doing no check cert because wget is having an issue with our wildcard cert
  # if you're reading this, and actually concerned you might be mitm, use a browser and just download these
  # files and then just comment these next two lines out :)
  echo
  echo ' [*] Downloading Setup Files From http://www.veil-framework.com'
  wget https://www.veil-framework.com/InstallMe/requiredfiles.zip --no-check-certificate
  wget https://www.veil-framework.com/InstallMe/pyinstaller-2.0.zip --no-check-certificate

  # Unzip Setup Files
  echo
  echo ' [*] Uncompressing Setup Archive'
  unzip requiredfiles.zip

  # Prepare Wine Directories
  echo
  echo ' [*] Preparing Wine Directories'
  mkdir -p ~/.wine/drive_c/Python27/Lib/
  cp distutils -r ~/.wine/drive_c/Python27/Lib/
  cp tcl -r ~/.wine/drive_c/Python27/
  cp Tools -r ~/.wine/drive_c/Python27/

  # Install Setup Files
  echo
  echo ' [*] Installing Wine Python Dependencies'
  wine msiexec /i python-2.7.5.msi
  wine pywin32-218.win32-py2.7.exe
  if [ -d "/usr/share/pyinstaller" ]
  then
    echo
    echo ' [*] PyInstaller Already Installed... Skipping.'
  else
    unzip -d /opt pyinstaller-2.0.zip
  fi

  # Clean Up Setup Files
  echo
  echo ' [*] Cleaning Up Setup Files'
  rm python-2.7.5.msi
  rm pywin32-218.win32-py2.7.exe
  rm pycrypto-2.6.win32-py2.7.exe
  rm pyinstaller-2.0.zip
  rm requiredfiles.zip

  # Remove Temp Directories
  echo
  echo ' [*] Removing Temporary Directories'
  rm -rf distutils
  rm -rf tcl
  rm -rf Tools
}

# Menu Case Statement
case $1 in
  # Force Clean Install Of Wine Python Dependencies
  --clean)
    if [ `whoami` != 'root' ]
    then
      echo
      echo ' [ERROR]: Either Run This Setup Script As Root Or Use Sudo.'
      echo
      exit 1
    fi
    # Bypass Validation Checks To Force Install Dependencies
    func_title
    func_apt_deps
    func_python_deps
    ;;
  # Print Help Menu
  -h|--help)
    func_title
    echo
    echo "  [Usage]....: ${0} [OPTIONAL]"
    echo '  [Optional].:'
    echo '               --clean   = Force Clean Install Of Python Dependencies'
    echo '               -h|--help = Show Help Menu'
    echo
    ;;
  # Run Standard Setup
  *)
    func_title
    func_validate
    ;;
esac

