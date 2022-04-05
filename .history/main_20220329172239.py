from cgi import print_directory
from xml.etree import ElementTree as ET

file = 'Docs/ArchivoPrueba.xml'

def MiniDom(file):
    try:
        tree = ET.parse(file)
        root = tree.getroot()
        for element in root:
            cities = element.findall('City')
            for City in cities:
                CityName = City.find('nombre')
                CityRows = City.findall('fila')
                CityConvoys = City.findall('unidadMilitar')
                
                print(CityName.text)
                for Row in CityRows:
                    Row.text.replace('"','')
                    print('>',Row.attrib['numero'], Row.text)
                for Convoy in CityConvoys:
                    print(Convoy.text)
                print('===========================================================\n') 
        

    except:
        print('No se cargaron los datos correctamente del piso')



if __name__ == '__main__':
    MiniDom(file)