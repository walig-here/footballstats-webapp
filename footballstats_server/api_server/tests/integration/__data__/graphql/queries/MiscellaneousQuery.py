#-------------------------------------------------------------------------------------
# QUERY FOR DATA DATE RANGE IN FILLED DATA BASE
#-------------------------------------------------------------------------------------

DATA_DATE_RANGE_QUERY: str = """\
{
	dataDateRange
}
"""

DATA_DATE_RANGE_RESPONSE__NOT_EMPTY_DATA_BASE: dict = {
    "data": {
        "dataDateRange": [
            "1958-06-24",
            "2022-04-29"
        ]
    }
}

#-------------------------------------------------------------------------------------
# QUERY FOR DATA DATE RANGE IN EMPTY DATA BASE
#-------------------------------------------------------------------------------------

DATA_DATE_RANGE_RESPONSE__EMPTY_DATA_BASE: dict = {
    "data": {
        "dataDateRange": [
            "2025-01-01",
            "2025-01-01"
        ]
    }
}

#-------------------------------------------------------------------------------------
# QUERY FOR COUNTRY LIST
#-------------------------------------------------------------------------------------

COUNTRY_LIST_QUERY: str = """\
{
	countryList{
        name
    }
}
"""

COUNTRY_LIST_RESPONSE__NOT_EMPTY_DATA_BASE: dict = {
    "data": {
        "countryList": [
            {"name": "Argentyna"},
            {"name": "Armenia"},
            {"name": "Azerbejdżan"},
            {"name": "Belgia"},
            {"name": "Białoruś"},
            {"name": "Bośnia i Hercegowina"},
            {"name": "Brazylia"},
            {"name": "Francja"},
            {"name": "Gana"},
            {"name": "Hiszpania"},
            {"name": "Holandia"},
            {"name": "Japonia"},
            {"name": "Kostaryka"},
            {"name": "Maroko"},
            {"name": "Międzynarodowy"},
            {"name": "Niemcy"},
            {"name": "Polska"},
            {"name": "Portugalia"},
            {"name": "Rosja"},
            {"name": "Senegal"},
            {"name": "Szwecja"},
            {"name": "Ukraina"},
            {"name": "Włochy"},
            {"name": "Wybrzeże Kości Słoniowej"},
        ]
    }
}

COUNTRY_LIST_RESPONSE__EMPTY_DATA_BASE: dict = {
    "data": {
        "countryList": []
    }
}

#-------------------------------------------------------------------------------------
# QUERY FOR EVENT TYPES
#-------------------------------------------------------------------------------------

EVENT_TYPES_QUERY: str = """\
{
	eventTypesList {
        name
	}
}
"""

EVENT_TYPES_RESPONSE: dict = {
    "data": {
        "eventTypesList": [
            {"name": "Czerwona kartka"},
            {"name": "Obrona"},
            {"name": "Podanie nieskuteczne"},
            {"name": "Podanie skuteczne"},
            {"name": "Przegrana"},
            {"name": "Remis"},
            {"name": "Rzut rożny"},
            {"name": "Strzał celny"},
            {"name": "Strzał niecelny"},
            {"name": "Zdobycie gola"},
            {"name": "Żółta kartka"},
            {"name": "Zwycięstwo"},
        ]
    }
}