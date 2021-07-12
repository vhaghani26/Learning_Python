#!/usr/bin/env python3

# Think of an HTML tag name as a class in Python
# Each individual tag is an instance
# HTML tables start with <td> tags
# Webscraping is a process that can be used to automatically extract information from a website

from bs4 import BeautifulSoup

# Store the webpage HTML as a string in the variable HTML
html = "<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $92,000,000 </p><h3> Stephen Curry</h3> Salary: $85,000,000 </p><h3> Kevin Durant </h3><p> Salary: $73,000,000</p></body></html>"

# To parse a document, pass it into the BeautifulSoup constructor

soup = BeautifulSoup(html, 'html5lib')

# The tag corresponds to an HTML tag in the original document
# If there is more than one tag with the same name, the first element with that tag is selected
tag_object = soup.title
tag_object = soup.h3

# Navigating the HTML tree
tag_child = tag_object.b
# tag_child: <b id="boldest">Lebron James</b>
parent_tag = tag_child.parent
# parent_tag: <h3><b id="boldest">Lebron James</b><h3>
sibling_1 = tag_object.next_sibling
# sibling_1: <p> Salary: $92,000,000 </p>
sibling_2 = sibling_1.next_sibling
# sibling_2: <h3> Stephen Curry</h3>

# You can access the attribute name and value as a key value pair in a dictionary
# tag_child: <b id="boldest">Lebron James</b>
# tag_child.attrs: {'id': 'boldest'}
# tag_child.string: 'Lebron James'

# find_all method
html = "<table><tr><td>Pizza Place</td><td>Orders</td><td>Slices </td></tr><tr><td>Domino'sPizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td>144</td></table>"

table = BeautifulSoup(html, 'html5lib')

table_row = table.find_all(name='tr')
# table_row:
# <tr><td>Pizza Place</td><td>Orders</td><td>Slices </td></tr>,
# <tr><td>Domino'sPizza</td><td>10</td><td>100</td></tr>,
# <tr><td>Little Caesars</td><td>12</td><td>144</td></tr>

first_row = table_row[0]
# first_row: <tr><td>Pizza Place</td><td>Orders</td><td>Slices </td></tr>

first_row.td
# <td>Pizza Place</td>

# First iterate through the list "table rows" via the variable row
for i,row in enumerate(table,rows):
    print("row", i)
    cells=row.find_all("td")
# Iterate through the variable cells for each row
    for j, cell in enumerate(cells):
        print("column", j, "cell", cell)
        



# Example:
'''
import requests
from bs4 import BeautifulSoup

page = requests.get("https://EnterWebsiteUrl...").text

# Creates BeautifulSoup object
soup = BeautifulSoup(page, "html.parser")

# Pulls all instances of <a> tag
artists = soup.find_all('a')

# Clears data of all tags
for artist in artists:
    names = artist.contents[0]
    fullLink = artist.get('href')
    print(names)
    print(fullLink)
'''