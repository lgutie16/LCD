## Technical Overview
This project was developed using _Python 2.7_ and  _nosetest_ test runner package

## Folder Structure

```
LCD/
  app/
  	__init__.py
  	lcd.py
  	main.py
  	processor.py
  test/
  	__init__.py
  	test_lcd.py  
```


## Instruction to run this Project
I assume that you have Python already installed, so you just need to follow the next instructions in order to run this project.

``` 
 https://github.com/lgutie16/LCD     [Clone the project in your selected directory]
 cd LCD/app                          [Go inside the main source directory]
 python main.py                      [Run app]

``` 

In the other hand, to run tests, you'll need to install _nosetest_ test runner package and after that, tests file can be executed

``` 
pip install nose        [Install Python package]
cd LDC/test 			[Go inside test directory]
nosetests test_lcd.py  	[Run tests]

```


 