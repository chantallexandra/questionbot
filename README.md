# Design and Implementation of a Natural Language Customer Query Platform
## Created by Chantal Montgomery for CISC 499

This project was designed for CISC 499 under Farhana Zulkernine at Queen's University (BAM Lab). The report can be [viewed here](https://docs.google.com/document/d/1QkAHASgwy4FDjfv_ayqTMMU3lFfY0fvXD_mBXJDqVaE/edit?usp=sharing), Chapter 3 discusses the details of the implementation.

### File Structure:
**/src :** Contains the source files for the React front-end. To run the project (from the root folder):
```
npm install
npm start
```

**/server/server :** Contains the source files for the Flask back-end. To start the server:
```
cd server/server
export FLASK_APP=app.py
flask run
```

**/server/test :** Contains the test files for the project. To run the tests, open in IDE and run or:
```
cd server
python3 -m unittest test/test_bot.py
```

**/server/utilities :** Contains general utility files.
