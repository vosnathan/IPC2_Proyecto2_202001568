from xml.dom import minidom

file = 'Docs/ArchivoPrueba.xml'

def MiniDom(file):
    try:
        domTree = minidom.parse(file)
        items = domTree.getElementsByTagName('game')
	    print(rootNode)

    except:
        print('No se cargaron los datos correctamente del piso')