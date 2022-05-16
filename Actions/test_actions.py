from pathlib import Path
from Paths.paths import wdir_JOBS
from Actions.actions import (
    gebruik_shutill_en_verplaats_file_van,
    find_folder_ordernummers_in,
    check_the_found_jobfolders,
    get_xml_with_glob_from_,
)

pad1 = Path(
    r"/Users/mike10h/PycharmProjects/pythonProject_MEJ_2022_mysql_bouwer/test_cron/2022-04-18_16_26/202210029.xml"
)
pad2 = Path(
    r"/Users/mike10h/PycharmProjects/pythonProject_MEJ_2022_mysql_bouwer/test_cron/2022-04-18_16_29/202210029_6000605378-1.xml"
)


def test_gebruik_shutill_en_verplaats_file_van():
    test = gebruik_shutill_en_verplaats_file_van(pad1, pad2)
    result = True, True
    assert test == result


testmap = wdir_JOBS
folders = sorted([int(folder.name) for folder in testmap.iterdir() if folder.is_dir()])


def test_find_folder_ordernummers_in():
    testing = sorted(find_folder_ordernummers_in(testmap, 100))
    test = [test[0] for test in testing]
    result = folders
    assert test == result


def test_check_the_found_jobfolders():
    test = check_the_found_jobfolders(wdir_JOBS, 30)
    result = [
        202224006,
        202224015,
        202224017,
        202224021,
        202224024,
        202224027,
        202224033,
        202224037,
        202224058,
        202224069,
        202224078,
        202224087,
        202224090,
        202224094,
        202224110,
        202224122,
        202224138,
        202224142,
        202224155,
        202224157,
        202224162,
        202224163,
        202224167,
        202224180,
        202224182,
        202224187,
        202224188,
        202224206,
        202224207,
        202224209,
        202224214,
        202224237,
        202224248,
        202224256,
    ]
    assert test == result


def test_get_xml_with_glob_from_():
    test = get_xml_with_glob_from_(wdir_JOBS, "202226")
    result = [
        "202226000.xml",
        "202226001.xml",
        "202226002.xml",
        "202226003.xml",
        "202226004.xml",
        "202226005.xml",
        "202226006.xml",
        "202226009.xml",
        "202226010.xml",
        "202226016.xml",
        "202226017.xml",
        "202226018.xml",
        "202226019.xml",
        "202226020.xml",
        "202226021.xml",
        "202226022.xml",
        "202226023.xml",
        "202226024.xml",
        "202226025.xml",
        "202226026.xml",
        "202226027.xml",
        "202226028.xml",
        "202226029.xml",
        "202226030.xml",
        "202226031.xml",
        "202226033.xml",
        "202226034.xml",
        "202226036.xml",
        "202226037.xml",
        "202226038.xml",
        "202226039.xml",
        "202226040.xml",
        "202226041.xml",
        "202226042.xml",
        "202226043.xml",
        "202226044.xml",
        "202226045.xml",
        "202226046.xml",
        "202226047.xml",
        "202226048.xml",
        "202226049.xml",
        "202226050.xml",
        "202226051.xml",
        "202226052.xml",
        "202226053.xml",
        "202226054.xml",
        "202226055.xml",
        "202226056.xml",
        "202226057.xml",
        "202226058.xml",
        "202226059.xml",
        "202226060.xml",
        "202226061.xml",
        "202226062.xml",
        "202226063.xml",
        "202226064.xml",
        "202226065.xml",
        "202226066.xml",
        "202226067.xml",
        "202226068.xml",
        "202226070.xml",
        "202226071.xml",
        "202226072.xml",
        "202226073.xml",
        "202226074.xml",
        "202226075.xml",
    ]
    assert test == result
