# https://www.hackerrank.com/challenges/xml-1-find-the-score/problem

def get_attr_number(node):
    nodeAttrib = len(node.attrib)

    return nodeAttrib + sum([get_attr_number(child) for child in node])

# github.com/ArutselvanManivannan
