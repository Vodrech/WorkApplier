# WorkApplier
> This project is for seeking job opportunities in Sweden and applying to them.

[![Python Version][python-version]][npm-url]
[![NPM Version][npm-image]][npm-url]

![Project_Summary_Logo](https://github.com/Vodrech/WorkApplier/blob/master/projectDescription.png?raw=true)

## Usage example
The Project uses the main.py as the entry points towards the project/program.

When main.py is executed, a window (Tkinter) is created and creates all the instances of classes that is needed.
In the window, settings can be modified and later on search after job applications depending on what settings were configured.

The project Tree is devided into different section that can be seen below:

> Project Structure:
```
<Base Dir>
|
├───Applying
│   └─── Handles applying functionality with fetching data on each site. (API CALL)
├───Database
│   └─── Handles all the database functionality.
├───Log
│   └─── Handles all the Logging functionality, mostly for debugging sections.
├───Settings
│   └─── Settings for the whole project, configures most of the changes.
├───Testing
│   └─── Handles all the automated testing to see that the modules/functions work.
├───Visualization
│   └─── Handles the visualization of graphs etc (NOT IMPLENTED)
├───Window
│   └─── Handles the main functionality of the Window(GUI) (TKinter).
├───Workflow
│   └─── Handles the main Functionality for the applying process.
└
```
> Dataflow:
```
The dataflow is how the project is processing data to function correctly.


Fetching data from worksite (webscraping) --> Saves the worksites to the DB --> Applies to the work recruitment --> Change attributes to "Applied" --> Wait for Response --> Respond to Response --> END 
```

## Development setup

Before using the library, some modules need to be imported
Use Either pip3 or pip dependent on what python intepreter you have.

*Note: This is not all modules, sometimes you lose track of everything, but these are the most useful ones.

```sh
pip install requests https://github.com/psf/requests
pip install lxml
pip install BeautifulSoup4
pip install sqlite3
pip install json
pip install tkinter
```
Checkout more information about each module:
> requests: https://github.com/psf/requests

> lxml: https://github.com/lxml/lxml

> BeautifulSoup4: https://github.com/wention/BeautifulSoup4

> sqlite3: https://docs.python.org/2/library/sqlite3.html

> json: https://docs.python.org/3/library/json.html

> tkinter: https://docs.python.org/3/library/tk.html

## Release History

![Github Logo](https://github.com/Vodrech/WorkApplier/blob/master/logo.png?raw=true)
* 1.0
   * CHANGE: Project structure
* 0.9
   * ADD: Testing
   * ADD: Logging
* 0.8
   * Fix: Fixed some GUI bugs
* 0.7
   * ADD: GUI Interface
   * CHANGE: Settings structure
* 0.6
   * ADD: Settings functionality
* 0.5
    * ADD: Applying functionality
* 0.4
    * ADD: Website data fetching functionality. 
* 0.3
    * ADD: Database functionality
* 0.2
    * First Commit
* 0.1
    * Start of project

## Meta

[https://github.com/Vodrech](https://github.com/dbader/)

## Contributing

Currently we are not open to contributors unless you are a student and is looking for education purposes only.


<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/badge/version-v1.0-brightgreen
[npm-url]: https://npmjs.org/package/datadog-metrics
[python-version]: https://img.shields.io/badge/python-%2B3.7-blue
