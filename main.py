#! venv/bin/python3.10

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from Calculations.calculations import check_ordernummer_met_regex_in, \
    standaard_mappen_range_per, standaard_map, hoogste_ordernummer, mappen_vergelijker, timer_op_functie
from Actions.actions import find_folder_ordernummers_in, get_xml_with_glob_from_
from Paths.paths import wdir_JOBS
from pathlib import Path
# actual days tobe determined  7 DAYS should be more than sufficient
RELEVANT_DAYS = 5

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # collect data (job folders) to work with.

    JOB_folders_to_check = find_folder_ordernummers_in(wdir_JOBS, RELEVANT_DAYS)
    # JOB_folders_to_check = [(202228,0),(202229,0)]

    # run through each separate folder to find missing ordernumbers.
    # todo make listcomp for all the JOB_folders in the list
    order_number_folders_to_check = find_folder_ordernummers_in(JOB_folders_to_check[0][1], RELEVANT_DAYS)

    # ordernummers_out_tuple = [str(ordernummer[0]) for ordernummer in order_number_folders_to_check]

    # check the list for anomaly's, typos and human errors with regexes, this includes LETTERS
    # checked_list = [str(check_ordernummer_met_regex_in(JOB_folders_to_check[0][0]),str(ordernummer[0][0]))
    #                 for ordernummer in order_number_folders_to_check]
    # checked_list = [int(check_ordernummer_met_regex_in(JOB_folders_to_check[0][0], ordernummer, r"(\d{4})(\d{2})(\d{3})")) for
    #                ordernummer in ordernummers_out_tuple
    #                if check_ordernummer_met_regex_in(JOB_folders_to_check[0][0], ordernummer,
    #                                                  r"(\d{4})(\d{2})(\d{3})") is not None]

    # build the perfect list to compare collected list with.

    # jaarmap24 = standaard_map('2022', '24', hoogste_ordernummer(checked_list))

    # For every file make a trigger pdf file for
    # todo report errors on web page with selenium

    # verschil24 = sorted(mappen_vergelijker(jaarmap24, checked_list))


    # jaarmap28_rglob = get_xml_with_glob_from_(wdir_JOBS,202228)


    xmls_uit_relevante_mappen = [get_xml_with_glob_from_(wdir_JOBS,map[0]) for map
                                 in JOB_folders_to_check]
    
    xml_flat_list_voor_destination_name = timer_op_functie([item for sublist in xmls_uit_relevante_mappen for item in sublist])






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
