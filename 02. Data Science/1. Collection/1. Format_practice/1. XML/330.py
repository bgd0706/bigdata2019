from xml.etree.ElementTree import Element, SubElement, dump

note = Element("note")
note.attrib["date"] = '20120104'

to = Element("to")
to.text = "Tove"
note.append(to)

SubElement(note, "from").text = "Jani"
SubElement(note, "heading").text = "Reminder"
SubElement(note, "body").text = "Don't forget me this weekend!"
dump(note)

from xml.etree.ElementTree import ElementTree
ElementTree(note).write("note.xml")

