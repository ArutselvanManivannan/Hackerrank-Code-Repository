# https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem

import sys

sys.stdin = open("E:\\REC\\Hackerrank\\input.txt")
sys.stdout = open("E:\\REC\\Hackerrank\\output.txt", "w")


from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f'{tag}')
        for attr in attrs:
            print(f'-> {attr[0]} > {attr[1]}')


parser = MyHTMLParser()

html_code = '\n'.join([input() for _ in range(int(input()))])

parser.feed(html_code)

# github.com/ArutselvanManivannan
