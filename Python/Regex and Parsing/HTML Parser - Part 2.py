# https://www.hackerrank.com/challenges/html-parser-part-2/problem

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        data = data.split('\n')
        if len(data) > 1:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')

        [print(d.strip()) for d in data]

    def handle_data(self, data):
        if data != '\n':
            print('>>> Data')
            print(data)


html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()

# github.com/ArutselvanManivannan
