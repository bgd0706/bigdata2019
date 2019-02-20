from xml.etree.ElementTree import Element, dump

note = Element("note")
to = Element('to')
to.text = "Tove"

note.append(to)
dump(note)
dump(to)