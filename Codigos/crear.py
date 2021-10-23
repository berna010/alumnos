import xml.etree.cElementTree as et

root = et.Element("Alumnos_Edificio_2")

tree = et.ElementTree(root)

tree.write("Alumnos_Edificio_2.xml", xml_declaration=True)
