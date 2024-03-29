# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 12:14:28 2019

@author: Baith
"""
"""
Problem Statement
This class provides a template for holding and manipulating information
about a book. The class definition provides a single method (besides the initialization method) that returns 
a formatted bibliographic reference for the book. The code below gives the class definition and 
then creates two instances of the class (note line continuations are added to fit the code on the
page):

"""

class Book(object):
    def __init__(self, authorlast, authorfirst, title, place, publisher, year):
        self.authorlast = authorlast
        self.authorfirst = authorfirst
        self.title = title
        self.place = place
        self.publisher = publisher
        self.year = year
    def write_bib_entry(self):
        return self.authorlast + ', ' + self.authorfirst \
                               + ', ' + self.title + ', ' + self.place \
                               + ':  ' + self.publisher + ', ' \
                               + self.year + '.'
                               
                               
#- Create a few instances of Book and Article classes:

beauty = Book( "Dubay", "Thomas", "The Evidential Power of Beauty",
               "San Francisco", "Ignatius Press", "1999", )
pynut = Book( "Martelli", "Alex", "Python in a Nutshell",
              "Sebastopol, CA", "O'Reilly Media, Inc.", "2003" )


#How would you print out the author attribute of the pynut instance
print(Book.write_bib_entry(pynut))
                            
#If you type print beauty.write bib entry() at the interpreter
#(after running the file), what will happen?
print(beauty.write_bib_entry())
# It'll give all attributes values

#How would you change the publication year for the beauty book to"2010"?
beauty.year="2010"
print(beauty.write_bib_entry()) # It will year 2010 along with remaining attributes

#Defining own Class 
"""Create another instance of the Book class using book of your choosing
(or make up a book). Execute the write bib entry method for that
instance to check if it looks like what you wanted."""
#soln
makeup = Book("Nitesh" , "Baith", "Who the fuck Cares!", "Jaipur rajasthan","Baith Publications", "2019")
print(makeup.write_bib_entry())


"""
Add a method make authoryear to the class definition that will create an attribute authoryear 
and will set that attribute to a string that has the last name of the author and then the year
in parenthesis. For instance, for the beauty instance, this method will set authoryear to
’Dubay (1999)’. The method should not have a return statement.
"""
class Book(object):
    def __init__(self, authorlast, authorfirst, title, place, publisher, year):
        self.authorlast = authorlast
        self.authorfirst = authorfirst
        self.title = title
        self.place = place
        self.publisher = publisher
        self.year = year
    def make_authoyear(self):
        self.authoyear= self.authorlast + '('+ self.year +' )'
    def write_bib_entry(self):
        return self.authorlast + ', ' + self.authorfirst \
                               + ', ' + self.title + ', ' + self.place \
                               + ':  ' + self.publisher + ', ' \
                               + self.year + '.'

print(makeup.make_authoyear()) # It will return None becuase make_authoyear has not return attributes

"""
Create an Article class that manages information about articles. It
will be very similar to the class definition for Book, except publisher
and place information will be unneeded and article title, volume number,
and pages will be needed. Make sure this class also has the methods write bib entry and make authoryear.

"""

class Article(object):
    def __init__(self, authorlast, authorfirst, title, volume, pages, year):
        self.authorlast = authorlast
        self.authorfirst = authorfirst
        self.title = title
        self.volume = volume
        self.pages = pages
        self.year = year
    def make_authoyear(self):
        self.authoyear= self.authorlast + '('+ self.year +' )'
    def write_bib_entry(self):
        return self.authorlast + ', ' + self.authorfirst \
                               + ', ' + self.title + ', ' + self.volume \
                               + ':  ' + self.pages + ', ' \
                               + self.year + '.'



"""

CASE STUDY 1

"""  
import operator

class Bibliography(object):
    def __init__(self,entrieslist):
        self.entrieslist = entrieslist
        
    def sort_entries_alpha(self):
        tmp = sorted(self.entrieslist , key = operator.attrgetter('authorlast','authorfirst'))
        self.entrieslist= tmp
        del tmp



#Exercise in extending the Bibliography class
"""
Since we programmed Book and Article with write bib entry methods, let’s take advantage of that. 
Write a method write_bibliog_alpha for the Bibliography class we just created that actually writes out a bibliography
(as a string) with blank lines between the entries, with the entries sorted alphabetically by author name. 
The bibliography should be returned using a return statement in the method. Some hints:
    
• Elements of a list do not have to all have the same type.

• for loops do not only loop through lists of numbers but through any
iterable. This includes lists of any sort, including lists of objects (such
as Book and Article instances.

• Strings are immutable, so you cannot append to an existing string. Instead, do a reassignment combined with concatenation (i.e., a=a+b).

• To initialize a string, in order to grow it in concatenation steps such
as in a for loop, start by setting the string variable to an empty string
(which is just ’’).

"""

import operator

class Bibliography(object):
    def __init__(self,entrieslist):
        self.entrieslist = entrieslist
        
    def sort_entries_alpha(self):
        tmp = sorted(self.entrieslist , key = operator.attrgetter('authorlast','authorfirst'))
        self.entrieslist= tmp
        del tmp
    def write_bibliog_alpha(self):
        self.sort_entries_alpha()
        output = ''
        for each in self.entrieslist:
            output = output + each.write_bib_entry() +'\n'
        return output[0:]
    
            
beauty = Book( "Dubay", "Thomas", "The Evidential Power of Beauty",
               "San Francisco", "Ignatius Press", "1999", )
pynut = Book( "Martelli", "Alex", "Python in a Nutshell",
              "Sebastopol, CA", "O'Reilly Media, Inc.", "2003" )            
nature = Article( "Smith", "Jane", "My Nobel prize-winning paper",
                   "481", "234-236", "2012" )
science = Article( "Doe", "Samuel", "My almost Nobel prize-winning paper",
                   "500", "36-38", "2011" )
noname = Article( "Doe", "John", "My no-one-has-heard-of paper",
                   "49", "34-36", "2005" )            
        

# Since it works on array so we have to create list instance
mybib = Bibliography([beauty, pynut, nature, science, noname])

if __name__ == '__main__':
    print ("Entries list Befor sorting : \n",[i.authorlast for i in mybib.entrieslist])
    mybib.sort_entries_alpha()
    print("Entries list after sorting : \n",[i.authorlast for i in mybib.entrieslist])
    print("Writting Bibliography: \n\n",mybib.write_bibliog_alpha())























                      
