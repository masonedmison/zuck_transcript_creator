import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('Zuckerberg Master-498abb4493ad.json', scope)
gc = gspread.authorize(credentials)
master = gc.open('Zuckerberg Files Source List').sheet1

record_id = master.col_values(1)
participants = master.col_values(2)
type = master.col_values(3)
format = master.col_values(4)
date = master.col_values(10)
source = master.col_values(11)
title = master.col_values(12)
url = master.col_values(16)
description = master.col_values(17)
keywords = master.col_values(18)


def build_dict():
    metadata = dict()

    metadata['record_id'] = record_id[1:]
    metadata['participants'] = participants[1:]
    metadata['type'] = type[1:]
    metadata['format'] = format[1:]
    metadata['date'] = date[1:]
    metadata['source'] = source[1:]
    metadata['title'] = title[1:]
    metadata['url'] = url[1:]
    metadata['description'] = description[1:]
    metadata['keywords'] = keywords[1:]

    # return dictionary of all values
    return metadata





