from pathlib import PosixPath, PurePosixPath

from Actions.lxml_tree import destination_name_from_vila_,xml_origin_and_new_
from Paths.paths import *
from lxml import etree


def test_destination_name_from_vila_():
    test = destination_name_from_vila_(test_xml_file)
    result = "202210029_6000605378-1.xml"

    assert test == result


def test_xml_origin_and_new():

    test = xml_origin_and_new_(test_destination,test_xml_file)
    result= (PosixPath('/Users/mike10h/PycharmProjects/pythonProject_MEJ_2022_mysql_bouwer/test_cron/2022-04-18_16_26/202210029.xml'),
             PurePosixPath('/Users/mike10h/PycharmProjects/pythonProject_MEJ_2022_mysql_bouwer/test_cron/2022-04-18_16_40/202210029_6000605378-1.xml'))
    assert test == result
