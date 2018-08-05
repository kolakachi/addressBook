# addressBook

Django App
---------------
Address Book is an application that stores names and email addresses in a database (SQLite). Address Book has a:

•	welcome page in http://localhost/ 

Note: this page has links to list and create functions

• Page-- http://localhost/list, that lists all stored names/email addresses in the database

•	Page-- http://localhost/add, that adds a names/email addresses to the database

Note: it validates input and show errors


This is a Django based application, it uses all of Django infrastructure (form, template inheritance, ORM) correctly. 
This application has solved major security problems--CSRF, XSS, SQL Injection.

Assumptions
------------------
I assumed users would be more drawn to a well-structured site, so I designed the front end using tools like Bootstrap & CSS.

I assumed the admin would like to know when each entry was made so I added a column for entry date.
