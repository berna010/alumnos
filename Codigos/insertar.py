import xml.etree.cElementTree as et
from xml.etree.ElementTree import SubElement, parse

xml_file = parse('Alumnos_Edificio_2.xml')

root = et.Element("alumnos")

xmlRoot = xml_file.getroot()

se = SubElement(root, "alumno000")
et.SubElement(se, "Nombre").text = "Alfredo_Garza"
et.SubElement(se, "Matricula").text = "18040000"
et.SubElement(se, "Carrera").text = "Logistica"


xmlRoot.append(se)

xml_file.write("Alumnos_Edificio_2.xml",xml_declaration=True)
