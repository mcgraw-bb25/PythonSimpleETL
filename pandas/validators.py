import datetime


def to_float(float_as_string):
    new_float = 0.0
    try:
        new_float = float(float_as_string)
    except:
        pass
    return new_float

def to_int(int_as_string):
    new_int = 0.0
    try:
        new_int = int(int_as_string)
    except:
        pass
    return new_int

def to_date(date_as_string):
    new_date = datetime.datetime(2099,12,31)
    try:
        year, month, day = date_as_string.split("-")
        new_date = datetime.datetime(int(year), int(month), int(day))
    except:
        pass
    return new_date

def to_varchar(varchar_as_string):
    new_varchar = ""
    try:
        new_varchar = varchar_as_string[:254]
    except:
        pass
    return new_varchar