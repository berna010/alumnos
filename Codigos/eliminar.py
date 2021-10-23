from xml.etree.ElementTree import parse, Element

file_name = "Alumnos_Edificio_2.xml"
doc_xml = parse(file_name)
root = doc_xml.getroot()

root.remove(root.find("alumno010"))

new_file = "Alumnos_Edificio_2.xml"
doc_xml.write(new_file, xml_declaration=True)
