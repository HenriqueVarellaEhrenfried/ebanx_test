# EBANX Take Home assignment 

## Information
This software was developed using Python 3.11 and FastAPI.
The directory structure is the following:
```
ebanx_test
├── LICENSE
├── README.md
├── main.py
├── requirements.txt
└── src
    ├── Router.py
    ├── database
    │   └── Data.py
    └── helpers
        └── Tools.py

```
The above files are the following:

* **LICENSE :** File containing the license information;
* **README.md :** This file. Contains information about the software;
* **main.py :** The main file to run the solution;
* **requirements.txt :** File that contains the required packages for this app;
* **Router.py :** File that contains the the routes of the app;
* **Data.py :** File that emulates a database controller;
* **Tools.py :** File to define helper functions;

This app was developed following the requirements sent by e-mail.

## How to run this app: 
- Create an environment (the author used miniconda and Python 3.11)
- Initialize your environment 
- Install the dependencies (`pip install -r requirements.txt`)
- Run `uvicorn main:app --reload` in the main directory

## License
This software is licensed under GNU General Public License V3. Read the license file for more information.

The author of this project is Henrique Varella Ehrenfried.