from turtle import ht
from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://flatironschool.com/our-courses", headers=headers)

doc = BeautifulSoup(html.text, 'html.parser')

print(doc.select('.heading-60-black.color-black.mb-20'))

courses = doc.select('.heading-60-black.color-black.mb-20')[0]

for course in courses: 
  print(course.contents[0].strip())
  