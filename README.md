Application Introduction
A Concert Merchandising Concession company (called Phoenix) wish to go “paper free”. They have asked you to provide a software solution for them. Their business is to provide the sales function for touring bands at certain concert venues around the country. 

The workflow is as follows :
The touring band (e.g. The Rolling Stones) will supply all the merchandise at the beginning of the day to Phoenix. Merchandise might be T-Shirts, Hoodies, caps, posters etc. together with a sales price for each item• Phoenix count in this stock and note the quantities of each (together with the sales price)

• Phoenix sell the items to the concert goers at the end of the concert
• Phoenix return unsold items to the touring band
• Phoenix pay the touring band for the sold items (less 25% commission)

All the paperwork for this is currently done manually.

Task One: Stock and Sales Control
You have been tasked with producing a demonstration application which allows :

1) Managers to set-up and load the stock database
2) Sales Staff to Sell items in the database
3) Managers to check unsold stock levels to be returned
4) Managers to calculate the payment due to the band

Initial design work has determined that for this demonstration you will use
• Tkinter for the user interface
• SQLite for the database

The eventual intention is to make parts of the system available over the Internet. You must therefore ensure that you can replace the interface without changing the back-end system.

At this stage no payment options / Processing are required.

The interface must allow the user to:
• Create, view, update, and delete stock items from the database
• Create, view and cancel a purchase
• Calculate the sold totals for each item and the payment due to the touring band.

Implementation
The software must be written in the Python programming language, version 3.7 or later (3.11 is recommended). The software must not require any additional software applications or integrated development environment in order to run. Python is distributed with an extensive library, and your software should make use of this. In particular tkinter should be used to implement the graphical user interface, and sqlite3 should be used to implement the database.

The following additional Python libraries should be used
• pytest - testing framework. Do not use unittest from the standard library.
• flake8
Some aspects of your submission will be checked with flake8 and pytest. 

Testing
Both static code checking, with flake8 and unit-testing with pytest will be carried out.
You should write your own unit tests and place your tests in a sub-directory of your application code directory - name this directory tests. 

To test your code, use the commands:

python -m flake8 . tests/ --count --max-complexity=5 – statistics
python -m pytest --cov=. tests/


