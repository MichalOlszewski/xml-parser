# Import of information about cadastral parcels
>Get information about cadastral parcels from xml file.



## Contents

* [General](#general)
* [Setup](#setup)
* [Tests](#tests)
* [Format data](#format-data)
  * [Adding new format data](#adding-new-format-data)
  * [Add new tag to object](#add-new-tag-to-object)
  * [Delete existing tag in object](#delete-existing-tag-in-object)
  * [Get all tags with description](#get-all-tags-with-description)
  * [Get description of tag](#get-description-of-tag)


## General
This is a small application that we can run via console. We must type data format and 
the file from which we will take the information. 
the program returns the necessary information about parcel.

## Setup
> Note: Requires [Python](https://www.python.org/)3 and pip to run.

Clone repository
```
https://github.com/MichalOlszewski/xml-parser/
```
Open code directory
```
cd xml-parser
```
Run project
```
python main.py [data format] [xml file]
```

>Example: python main.py aaa parcel_aaa.xml


## Tests
```
python test_main
python test_dataformat
```

## Format data
### Adding new format data
In script main.py we must create new object that is DataFormat Class. <br>
Creating the object we can give dictionary as argument.<br> <br>
 Dictionary structure: <br>
  {<br>
  "tag1": "description1", <br>
  "tag2": "description2" <br>
  } <br>
 > Example: <br>
 > { <br>
    "flstkennz": "Numer działki", <br>
    "flaeche": "Wielkość działki", <br>
    "landschl": "Numer landu", <br>
    "kreisschl": "Numer okręgu", <br>
    "gmdschl": "Numer powiatu", <br>
    "gemaschl": "Numer gemarkung", <br>
  } 
<br><br>
### Add new tag to object
We can also add new tags after creating object using method:
```
self.add_tag(tag, description)
```

### Delete existing tag in object
```
self.delete_tag(tag)
```

### Get all tags with description
```
self.get_tags_with_description()
```

### Get all tags without description
```
self.get_tags()
```

### Get description of tag
```
self.get_description(tag)
```
