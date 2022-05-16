from pathlib import Path, PurePath
from lxml import etree
try:
    from lxml import etree

    print("running with lxml.etree")
except ImportError:
    try:
        # Python 2.5
        import xml.etree.cElementTree as etree

        print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # Python 2.5
            import xml.etree.ElementTree as etree

            print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree

                print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree

                    print("running with ElementTree")
                except ImportError:
                    print("Failed to import ElementTree from any known place")


def destination_name_from_vila_(xml_file):
    """builds a new name for switch scan Hierarchy from
    # todo make tuple with origin and destination path for shutil"""
    vila_order = xml_file.stem
    tree = etree.parse(str(xml_file))
    root = tree.getroot()
    CustomerJobReference = root[1][3].text
    print(xml_file)
    return f'{vila_order}_{CustomerJobReference}.xml'


def xml_origin_and_new_(destination_wdir, from_xml_file):
    """builds a new name for switch scan Hierarchy from args
    # factory that builds a tuple with origin(xml file) and destination path for shutil"""

    vila_order = from_xml_file.stem
    tree = etree.parse(str(from_xml_file))
    root = tree.getroot()
    CustomerJobReference = root[1][3].text
    print(from_xml_file)
    new_file_xml_name =f'{vila_order}_{CustomerJobReference}.xml'
    xml_destination = PurePath(destination_wdir,new_file_xml_name)
    xml_destination = Path(xml_destination)

    return (from_xml_file, xml_destination)
