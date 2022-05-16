import shutil
from datetime import date, timedelta
from pathlib import Path
import time

from Calculations.calculations import (
    check_ordernummer_met_regex_in,
    standaard_map,
    hoogste_ordernummer,
    mappen_vergelijker,
)


def find_folder_ordernummers_in(wdir_folder, days):
    """
    parameters:
        wdir_folder(Path)
        days(int)

    returns:
    tuple(int, Path, timestamp )

    note:
    Walks through a designated root folder produces all (folders,paths and timestamps) as a tuple
    checks the optional timestamp"""

    past_time = date.today() - timedelta(days=days)
    folders_in_map = []
    try:
        for path in Path(wdir_folder).iterdir():
            timestamp = date.fromtimestamp(path.stat().st_mtime)

            if path.is_dir() and past_time < timestamp:
                print(f"{path = } \n{path.name = }")
                try:
                    ordernummer_als_int = int(path.name)

                    folders_in_map.append(
                        (
                            ordernummer_als_int,
                            path,
                            timestamp,
                        )
                    )
                    print(path.is_dir())
                except ValueError:
                    print(ValueError)

    except ValueError as e:
        print(e)

    return sorted(folders_in_map)


def check_the_found_jobfolders(wdir_JOBS, RELEVANT_DAYS):
    """lijst is  order_number_folders_to_check"""
    JOB_folders_to_check = find_folder_ordernummers_in(wdir_JOBS, RELEVANT_DAYS)

    # run through each separate folder to find missing ordernumbers.
    # todo make listcomp for all the JOB_folders in the list
    order_number_folders_to_check = find_folder_ordernummers_in(
        JOB_folders_to_check[0][1], 30
    )

    ordernummers_out_tuple = [
        str(ordernummer[0]) for ordernummer in order_number_folders_to_check
    ]

    # check the list for anomaly's, typos and human errors with regexes, this includes LETTERS
    # checked_list = [str(check_ordernummer_met_regex_in(JOB_folders_to_check[0][0]),str(ordernummer[0][0]))
    #                 for ordernummer in order_number_folders_to_check]

    checked_list = [
        int(
            check_ordernummer_met_regex_in(
                JOB_folders_to_check[0][0], ordernummer, r"(\d{4})(\d{2})(\d{3})"
            )
        )
        for ordernummer in ordernummers_out_tuple
        if check_ordernummer_met_regex_in(
            JOB_folders_to_check[0][0], ordernummer, r"(\d{4})(\d{2})(\d{3})"
        )
        is not None
    ]

    # build the perfect list to compare collected list with.
    jaarmap24 = standaard_map("2022", "24", hoogste_ordernummer(checked_list))

    # For every file make a trigger pdf file for
    # todo report errors on web page with selenium
    verschil24 = sorted(mappen_vergelijker(jaarmap24, checked_list))
    print(f"{verschil24} = ")

    return verschil24




def get_xml_with_glob_from_(WDIR_JOBS, de_te_doorzoeken_folder):

    # de jaar maand map waarin naar xmls gezocht kan worden
    folder = str(de_te_doorzoeken_folder)
    # bouw het pad naar de te doorzoeken folder
    folder_naar_xml = WDIR_JOBS.joinpath(folder)

    globxml = sorted(folder_naar_xml.rglob("*.xml"))

    tic = time.perf_counter()
    xml_named_files = [
        (padnaam.stem, check_ordernummer_met_regex_in(folder, padnaam.name),padnaam)
        for padnaam in globxml
        if check_ordernummer_met_regex_in(folder, padnaam.name) != None
    ]
    toc = time.perf_counter()
    print(f"built in timer : done in {toc - tic:0.8f} seconden")
    return xml_named_files


def gebruik_shutill_en_verplaats_file_van(original_pad, destination_pad):

    try:

        shutil.copyfile(original_pad, destination_pad)

    except OSError as e:
        print(e)

    return original_pad.stem, destination_pad.stem
