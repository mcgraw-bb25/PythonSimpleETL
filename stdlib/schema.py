

complete_schema = {
    "schema": ["key1", "key2", "key3", "date1", "date2", "date3",
               "amount1", "amount2", "amount3", "amount4", "amount5",
               "amount6", "description1", "description2", "ignored_varchar1",
               "ignored_varchar2", "ignored_varchar3", "ignored_varchar4",
               "ignored_numeric1", "ignored_numeric2", "ignored_numeric3",
               "ignored_numeric4"],
    "validators": {
        "float": ["amount1", "amount2", "amount3", "amount4",
                  "amount5", "amount6"],
        "int": ["key1", "key2", "key3"],
        "date": ["date1", "date2", "date3"],
        "varchar": ["description1", "description2"],
    },
    "tablename": "orders",
    "db_schema": ["key1", "key2", "key3", "date1", "date2", "date3",
                  "amount1", "amount2", "amount3", "amount4", "amount5",
                  "amount6", "description1", "description2"]
}

matching_schema = {
    "schema": ["key1", "key2", "description1", "date1"],
    "validators": {
        "int": ["key1", "key2"],
        "date": ["date1"],
        "varchar": ["description1"],
    },
    "tablename": "orders",
    "db_schema": ["key1", "key2", "description1", "date1"]
}
