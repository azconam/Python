tally 0.2.0


A program for political scientists that counts and analyzes voters
based on demographic factors

Feature
•	Simple way to count voters
•	County, State, Country setup
•	Methods to compare voters
•	Methods to forecast elections

Installation
To install Tally.py, enter the line below on your command line (Windows) or terminal (Mac)
git clone https://github.com/azconam/Python.git
Organization
Tally is organized by a county, state and country setup. Voters can be added to a county, counties to a state, and states to a country. Each level provides the user with different analysis tools.
Usage
The complete source code documentation can be found at: github.com/azconam/indevelopment 
Here is a reduced sample of a common usage scenario:
Instantiation
To create a voter, simply:
>>> v = Voter()
>>> v
<<__main__.Voter object at 0x1055a9b38>>
>>>
and now a county:
>>> c = Voter()
>>> c
<<__main__.Voter object at 0x1055a9b38>>
>>>
to add voter v to county c:
>>> c.add_voter(v)
>>> c
<<__main__.Voter object at 0x1055a9b38>>
>>>

to populate a county with 30 undefined (without demographic records) voters:

>>> c.populate(30)
>>> c
<<__main__.Voter object at 0x1055a9b38>>
>>>

Reading values
Voters’ demographics are accessible by simply:
>>> print(v)
20
M
I
H
>>>
Each individual demographic factor can be independently accessed:
>>> x.age
>>> x.sex
>>> x.party
>>> x.race
A note: due to Python’s design of dynamic typing, a voter’s age has been set to 0 by default. 
Modifying voter objects
All the demographic factors can be changed:
>>> x.age = 30
>>> x.party = ‘I’

Analysis
Counties can be analyzed by sex ratios:
>>> c.sex_ratio()
Male:Female = 1.00
by party distribution:
>>> c.party_distribution()
Democrats: 20%	Republicans:	20%	Independents:	60%

The content of the document......


These are a few examples of Tally’s features. For a complete list of features, consult the code source documentation.




Changelog
0.1.1 (2017-07-24)
0.1.2 (2017-07-30)

Author: Mauricio Azcona
Home Page: https://github.com/azconam/Python
License: BSD 3-Clause License
Categories
o	License :: OSI Approved :: BSD License
o	Programming Language :: Python
o	Programming Language :: Python :: 2
o	Programming Language :: Python :: 2.7
o	Programming Language :: Python :: 3
o	Programming Language :: Python :: 3.3
o	Programming Language :: Python :: 3.4
o	Programming Language :: Python :: 3.5
o	Programming Language :: Python :: 3.6
o	Topic :: Software Development :: Libraries :: Python Modules
1
