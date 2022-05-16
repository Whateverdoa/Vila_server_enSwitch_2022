import re
from datetime import date
from pathlib import Path
import time


def job_map_lezer(folder):
    for path in Path(folder).iterdir():
        if path.is_dir():
            timestamp = date.fromtimestamp(path.stat().st_mtime)
            print(path, timestamp)
    return 0

def regex_xml(xml_file_naam,regex_search_xml = r"\d{9}.xml" ):
    """ stop er een xmlfile in met glob functie en geef specifieke xml file terug """
    try:
        regex_checked_xml_file = re.search(regex_search_xml, xml_file_naam)

        return regex_checked_xml_file.group()

    except AttributeError:
        AttributeError
        return None


def check_ordernummer_met_regex_in(jobfolder, ordernummer,regex_search=r"(\d{4})(\d{2})(\d{3})(.xml)"):
    # input is string otherwise int will be made string
    # regex_search = r"(\d{4})(\d{2})(\d{3})(.xml)"  # geeft 4 zoek groepen
    jobfolder = str(jobfolder)
    ordernummer=str(ordernummer)

    try:
        basisordernummer_check_regex = re.search(regex_search, ordernummer)
        output_regex_search_order = basisordernummer_check_regex.group()
        jaar = basisordernummer_check_regex.group(1)
        mapnr = basisordernummer_check_regex.group(2)

        if jaar + mapnr == jobfolder and output_regex_search_order != "no_match":
            # return 0,"check1", output_regex_search_order,jaar,mapnr
            "match"
        else:
            return "no_match"

        return output_regex_search_order

    except AttributeError:
        "AttributeError: no Match"


def check_jobfolder_with_regex(jobfolder_to_check, jaar):
    # jaar optie is optioneel
    jaar = jaar
    jaar_check = r"(2022)(\d{2})"
    basischeck_verzamelmap = r"\d{6}"  # geeft 6 digits
    jobfolder_is_zes_getallen = len(jobfolder_to_check)
    try:
        jaar_test = re.search(jaar_check, jobfolder_to_check)
        if jaar_test.group(1) == str(jaar) and jobfolder_is_zes_getallen == 6:

            basismap_check_regex = re.search(basischeck_verzamelmap, jobfolder_to_check)
            output_regex_search = basismap_check_regex.group()
        else:
            print(f"vergelijk {jaar_test.group(1)}  met {jaar}")
            print(f'aantal posities (6) van folder = {jobfolder_is_zes_getallen}')

        return output_regex_search

    except AttributeError:
        print("AttributeError: no Match")
        return 0


def standaard_mappen_range_per(jaar):
    begin = str(jaar) + (2*str(0))
    eind = int(begin)+100
    jaar_lijst = [x for x in range(int(begin),eind)]
    return jaar_lijst


def hoogste_ordernummer(lijst_van_te_controleren_mappen):
    # NB: nota bena!!: alle ordernummers omzetten naar int
    hoogste_ordernummer = max(set(lijst_van_te_controleren_mappen))
    return hoogste_ordernummer + 1

#standaard_python functie max hernoemd
max_ordernummer = hoogste_ordernummer


def standaard_map(jaar, map, max_ordernummer):
    """@ todo maak 1 arg van jaar en map"""

    begin = str(jaar) + str(map) + (3 * str(0))
    eind = int(max_ordernummer)
    map_lijst = [x for x in range(int(begin), eind)]
    return map_lijst



def mappen_vergelijker(standaardmap, opgehaalde_map):

    niet_aanwezig = list(set(standaardmap) - set(opgehaalde_map))
    if niet_aanwezig == []:
        return 0
    return niet_aanwezig


def timer_op_functie(functie):
    tic = time.perf_counter()
    functie
    toc = time.perf_counter()
    # print(f"{str(functie)} has been done in {toc - tic:0.8f} seconden")
    print(f"timer funct: done in {toc - tic:0.8f} seconden")
    return functie



