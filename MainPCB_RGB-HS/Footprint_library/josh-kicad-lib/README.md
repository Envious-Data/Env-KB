# josh-kicad-lib
KiCad library for all of my projects

## To Use
Create a new directory  

Initialise git  
```git init```  

Create library submodule  
``` git submodule add https://github.com/joshajohnson/josh-kicad-lib.git```  

Create a hardware directory, and copy the template folder into hardware folder  

Rename template files as required  

Ready to design your next board!

### Script to generate files
Thanks to [Silvio](https://twitter.com/silviocesare) for making `setup.sh` which automates the generation of the required files. 

From `josh-kicad-lib` run `./setup.sh version MyProject "Your Name"` which will copy the template directory to hardware/$Version and change the names of template * to MyProject, along with changing the company name of the KiCad files. 

### Folder Structure
This should result in a folder structure which looks like the below. If your KiCad project is not two levels below this library, things will not work properly.

``` 
kicad-project-git
|- .git
|
|- .gitmodules
|- hardware
|  |- version
|     |- fp-info-cache
|     |- fp-lib-table
|     |- sim-lib-table
|     |- <project>.kicad_pcb
|     |- ...
|
|- josh-kicad-lib
|  |- lib files
|
|- README.md 
```

### Addition of new libraries / 3d models
Ensure all paths use the below text at the start of the path, as this keeps everything relative and ensures that it will work across different locations and computers. 

``` ${KIPRJMOD}/../../josh-kicad-lib/...```

### Common part details used in library
`common-parts.xlsx` contains details for a bunch of the parts commonly used in this library / my designs, and can be used to make generating the bom files with MPN/DigiKey/LCSC/etc details easier.

### Thanks to the below people for use of their symbols / footprints / 3D models
* [arturo182](https://twitter.com/arturo182) for the USB Type-C Connector.