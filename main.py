from xml.etree import ElementTree as ET
from SparceMatrix import SparceMatrix

file = 'Docs/ArchivoPrueba.xml'

Lista1 = SparceMatrix()

def ElementTree(file):
    try:
        tree = ET.parse(file)
        root = tree.getroot()
        for element in root:
            cities = element.findall('ciudad')
            for City in cities:
                CityName = City.find('nombre')
                CityRows = City.findall('fila')
                CityConvoys = City.findall('unidadMilitar')
                
                print(CityName.text, CityName.attrib['filas'], CityName.attrib['columnas'])
                for Row in CityRows:
                    patron = Row.text.replace('"','')
                    print('>',Row.attrib['numero'], patron)
                    PosX = 0
                    PosY = int(Row.attrib['numero'])
                    PosY = PosY -1
                    for character in patron:
                        if character != '*':
                            Lista1.Insert(PosX,PosY,character)
                        PosX += 1    
                            

                
                print('\n\n\n\n')      
                
                for Convoy in CityConvoys:
                    print(Convoy.text)
                print('===========================================================\n') 

    except:
        print('No se cargaron los datos correctamente del piso')



if __name__ == '__main__':
    ElementTree(file)