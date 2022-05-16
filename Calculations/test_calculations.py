from pathlib import Path


def test_standaard_mappen_range_per():
    assert False


from Calculations.calculations import (
    standaard_mappen_range_per,
    standaard_map,
    mappen_vergelijker,
    max_ordernummer,
    check_jobfolder_with_regex,
    check_ordernummer_met_regex_in,
    job_map_lezer, timer_op_functie,
)


# testmap = Path(r"//test_cron")
# folders = [folder.name for folder in testmap.iterdir() if folder.is_dir()]


def test_standaard_mappenlijst():
    a = list(range(202200, 202300))
    b = standaard_mappen_range_per(2022)
    assert a == b


def test_standaard_map():
    inmap = [x for x in range(202200000, 202200123)]
    test = standaard_map("2022", "00", "202200123")

    assert test == inmap


def test_mappen_vergelijker():
    # er wordt een folder bekeken in de map Jobs,
    # deze wordt vergeleken tegen de standaard inhoud
    # van een ordermap de mappen die overbljven moeten gegenereerd
    # gaan worden. Maar er speelt ook nog een grace periode
    # te snel is ook niet raadzaam.

    opgehaald_uit_systeem = [202200001, 202200004, 202200005, 202200007]
    laatsteordernummer = max(set(opgehaald_uit_systeem))

    tegen = standaard_map("2022", "00", max_ordernummer(opgehaald_uit_systeem))
    result = [202200000, 202200002, 202200003, 202200006]
    test = mappen_vergelijker(tegen, opgehaald_uit_systeem)
    assert test == result


def test_check_jobfolder_with_regex():
    test = check_jobfolder_with_regex("202100", "2022")
    result = "202200"
    test2 = check_jobfolder_with_regex("202200", "2022")
    result2 = "202200"
    # assert test == result2
    assert test2 == result2


def test_check_ordernummer_met_regex_in():
    test = check_ordernummer_met_regex_in("202200", "202200234.xml")
    result = "202200234.xml"
    assert test == result


def test_job_map_lezer():
    wdir = Path("/Users/mike10h/.anydesk/incoming/2022-04-28 17:07:02.418")

    # wdir =Path(r'/Users/mike10h/SWITCH WORKFLOWS/printdotcom/SWITCH WORKFLOW 15032022/Volumes/Afdeling Prepress/ESKO/Jobs')
    lijst = [202226]
    folders_metrange = [wdir.joinpath(str(pad)) for pad in lijst]
    test = job_map_lezer(folders_metrange)
    assert False


def test_timer_op_functie():
    def add():
        return 1000 +1000

    test = timer_op_functie(add())
    result = 2000

    assert test == result

