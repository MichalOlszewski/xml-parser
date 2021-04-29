import xml.etree.ElementTree as ET
import sys
from dataformat import DataFormat


def get_info_with_description(name_file_xml, tags_with_desc):
    for tag, tag_text in parser(name_file_xml, list(tags_with_desc.keys())):
        yield tags_with_desc[tag], tag_text


def parser(filename, tags):
    try:
        tree = ET.iterparse(filename)

        for event, node in tree:
            tag = clear_tag(node.tag)
            if tag in tags:
                yield tag, node.text
    except FileNotFoundError:
        print("The wrong file name was entered!")


def clear_tag(tag):
    ind_start = tag.rfind("}") + 1
    if ind_start:
        return tag[ind_start:]
    return tag


aaa_tags = {
    "flstkennz": "Numer działki",
    "flaeche": "Wielkość działki",
    "landschl": "Numer landu",
    "kreisschl": "Numer okręgu",
    "gmdschl": "Numer powiatu",
    "gemaschl": "Numer gemarkung",
}

nas_tags = {
    "flurstueckskennzeichen": "Numer działki",
    "amtlicheFlaeche": "Wielkość działki",
    "land": "Numer landu",
    "kreis": "Numer okręgu",
    "gemeinde": "Numer powiatu",
    "gemarkungsnummer": "Numer gemarkung",
}

if __name__ == "__main__":
    # Creating "aaa" format data
    aaa = DataFormat(**aaa_tags)

    # Creating "nas" format data
    nas = DataFormat(**nas_tags)

    del aaa_tags
    del nas_tags

    try:
        obj_DataFormat = globals()[sys.argv[1]]
        tags_with_description = obj_DataFormat.get_tags_with_description()
        file = sys.argv[2]

        for desc, text in get_info_with_description(file, tags_with_description):
            print(desc, text)

    except IndexError:
        print("Too few arguments were specified!")
    except KeyError:
        print("The specified file format doesn't exist!")
    except FileNotFoundError:
        print("The wrong file name was entered!")
