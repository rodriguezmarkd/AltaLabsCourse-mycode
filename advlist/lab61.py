#!/bin/env python3

wordbank = ["indentation", "spaces"]
tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

wordbank.append(str(4))

num = int(input("Enter a number between 0 and 20: "))

#print(type(num))

student_name = tlgstudents[num]

print(student_name + " always uses " + wordbank[-1] + " spaces to indent")
