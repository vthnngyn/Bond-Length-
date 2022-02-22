# Calculate Bond Lengths & Coordination Numbers

A python script to calculate the bond lengths and atomic coordination between xyz-based atomic coordinates

## Table of Contents
* [Introduction](#introduction)
* [General Info](#general-info)
* [Technologies](#technologies)
* [Launch](#launch)
* [Example of Use](#example-of-use)

### Introduction

For many computational chemistry softwares, a .xyz file or xyz-based coordinates can be obtained for a molecular system. Without having to utilizing a GUI, this script tabulates all bond lengths and number of bonds per atom for each atom.

### General Info

The script takes an .xyz file or xyz coordinates of atomic coordinates and calculates the bond length (with the average and standard deviation) between each atom up to an inputted upper limit. The coordination number per each atom is calculated by counting the number of other atoms that atom has a counted bond length with. A sample input file is provided: example.xyz.  

### Technologies
* Python 3
  * prettytable 3.1.1

### Launch

```
$ python bond_length.py
```

### Example of Use
Using the provided example .xyz file, the script will first ask for a file input of xyz coordinates:
```
File of xyz coordinates:example.xyz
```
The number of atoms in the .xyz file will be printed along with a table that indexes each atom to a number.
The upper length limit for defining a bond is then requested where the units are dependent on the input file:
```
Upper limit for desired bond length (units defined by inputted file):3
```
Each bond is then shown in a table where each row has the two atoms in a bond with their numeric indices and the bond length. 
The average bond length with the standard deviation is calculated from all those bonds. 
The coordination number for each atom and its numeric index is shown next along then with the average coordination number and standard deviation.  
