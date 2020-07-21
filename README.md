# OCR-Projet7 - Créez GrandPy Bot, le papy-robot

This program helps you to find an adress and returns you a map when asking question ti the bot

## Prerequisites
* Download this repository
* You must have python3 installed on your computer, otherwise you can follow the guides on python's website https://www.python.org/downloads/
* Set your current directory in the project:
```cd path/to/folder/downloaded```
* run on your console/terminal the following command:
```pip3 install -r requirements.txt```
* deploy on heroku

## Program design
* directory app : directory containing all python files
	* main.py : create flask app
	* views.py : render html visual
	* maps.py : google maps api
	* wiki.py : wikipedia api
	* parser.py : parse user's question
	* template: directory for html
		* index.html : main html
	* tests : directory containing tests
	* static : directory containing ressources
* file wsgi.py : file used to launch the program

## Author
**Mehdi Bichari** - [GitHub Repo](https://github.com/Kaik-a/)

## Acknowledgements
I want to make a special thank to Julien Jacquelinet who helped me all along this project and all the openclassrooms community !
