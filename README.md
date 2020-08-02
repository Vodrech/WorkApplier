# WorkApplier
> This project is for seeking job opportunities and applying to them.

[![Python Version][python-version]][npm-url]
[![NPM Version][npm-image]][npm-url]

## Usage example

The project is devided between 7 different section with a entrypoint through the main.py file.

> Project Structure:
```
<Base Dir>
|
├───Applying
│   └─── Handles Applying Functionality with fetching data on each site.
├───Database
│   └─── Handles all the Database Functionality.
├───Settings
│   └─── Settings over whole project
├───Testing
│   └─── Consists of all the testing within the project. (Not Implented YET)
├───Visualization
│   └─── Handles data outside of the window, such as writing to excell or other ways of visualize data. (NOT Implented YET)
├───Window
│   └─── Handles all the functionality for the GUI (Window)
├───Workflow
│   └─── Handles the main Functionality for the applying process.
└
```
> Dataflow:
```
The dataflow is how the project is processing data to function correctly.

The Optimal Idea how it will work:
Fetching data from worksite (webscraping) --> Saves the worksites to the DB --> Applies to the work recruitment --> Change attributes to "Applied" --> Wait for Response --> Respond to Response --> END 
```

## Development setup

Before using the library, some modules need to be imported
Use Either pip3 or pip dependent on what python intepreter you have.

```sh
pip install requests https://github.com/psf/requests
pip install lxml
pip install BeautifulSoup4
pip install sqlite3
pip install tkinter
```
Checkout more information about each module:
> requests: https://github.com/psf/requests

> lxml: https://github.com/lxml/lxml

> BeautifulSoup4: https://github.com/wention/BeautifulSoup4

> sqlite3: https://docs.python.org/2/library/sqlite3.html

> tkinter: https://docs.python.org/3/library/tk.html

## Release History
* 0.6
    * ADD: Window functionality
    * Mod: Modified Settings
    * Add: Overall Error Handling
* 0.5
    * ADD: Applying functionality
* 0.4
    * ADD: Website data fetching functionality
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
[npm-image]: https://img.shields.io/badge/version-v0.6-brightgreen
[npm-url]: https://npmjs.org/package/datadog-metrics
[python-version]: https://img.shields.io/badge/python-%2B3.7-blue
