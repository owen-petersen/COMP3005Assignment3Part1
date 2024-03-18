# COMP 3005 Assignment 3 Part 1 Submission
## 1 - Application Overview
This program was written to connect to a postgresql database and perform simple CRUD operations. The main application
consists of repeatedly prompting the user to select a function to perform then prompting the user for input for the
chosen function if required. Then the corresponding query is executed with the specified information.
## 2 - Database Format
This application assumes that the database being accessed has one table named students. This table must have five
attributes: student_id, first_name, last_name, email, and enrollment_date.
## 3 - Code Design
This assignment was completed using python as the primary language. The reason for this decision was that the final 
project will also use python as the language for making a series of scripts to interact with a database and I decided 
that this assignment was a good oppourtunity to practice. The four functions are encapsulated in a class which acts as
the interface for interacting with the database. The program runs in a while-loop, repeatedly prompting the user to
select one of the four functions and then taking further input from the user if the selected function requires arguments.
## 4 - Video Submission Link
https://mediaspace.carleton.ca/media/OwenPetersen_COMP3005_Assignment3Part1/1_wutb60lr
