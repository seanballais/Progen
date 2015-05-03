# Progen
## Project Generator

Generate projects easily with a single command(`progen [generator]`). As of v0.0.1a, Progen supports generating C++ projects. More efforts are needed to improve it.

### Creating your own generator
You can create your own project generator that will be utilized by Progen. A generator is simply a python file.    
There are two types of generators:
- **Folders Only**
This type of generator only requires that you specify folders that will be created with a variable called `folders`.    
For example:
```python
folders = [
    "bin",
    "bin/epic",
    "build",
    "src"
]
```
    
Just save the code above as a python script (for example, `testscript.py`) inside Progen's generator folder in the installation directory.    
    
To generate a project based on the specified folders above, just run `progen testscript` inside the terminal.
- **Full Generator**
This type of generator requires that you be responsible for making the folders. This is useful if you want to create a generator that is interactive and flexible.    
    
The code must be inside a `main()` function in order for it to work. Running a full generator is similar to running a *Folders only* generator.     

*NOTE: Generators must be saved inside Progen's `generators` folder in the installation directory*    

### License
Progen is licensed under the GNU General Public License v3.0.    
    
Copyright (C) 2015 Sean Francis N. Ballais