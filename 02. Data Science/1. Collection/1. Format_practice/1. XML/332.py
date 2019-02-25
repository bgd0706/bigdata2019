from xml.etree.ElementTree import parse
tree = parse("note.xml")
note = tree.getroot()

print(note.get("date"))
print(note.get("foo", "default"))
print(note.keys())
print(note.items())

print('==============================')

from_tag = note.find("from")
print(from_tag)
from_tags = note.findall("from")
print(from_tags)
from_text = note.findtext("from")
print(from_text)
print("end")

for parent in tree.getiterator() :
    for child in parent :
        print(child)
