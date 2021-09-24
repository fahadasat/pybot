#python
import urllib
import json

#query all CompSci courses
url = u'https://api.metalab.csun.edu/curriculum/api/2.0/courses/comp'

#try to read the data
try:
   u = urlopen(url)
   data = u.read()
except Exception as e:
	data = {}

#decode into an array
data = json.loads(data)

#setup a blank array
course_list = []

#loop through results and add each course's subject
#and catalog number to course_list array (i.e COMP 100)
for course in data['courses']:
	course_list.append(course['subject'] + ' ' + course['catalog_number'])

print (course_list)