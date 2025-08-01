# uses Salesforce REST API to retrieve data of a Salesforce Org.
#
# Requires to have the `sf` CLI tool installed and having set a default authenticated org.
#

__version__ = '0.1.0'
__author__ = 'Thomas Dürr <thomduerr@gmail.com>'

import subprocess
import json
import re

from visidata import vd, Sheet, Column, asyncthread

def retrieve_record(id):
    output = subprocess.check_output(f'sf data query -q "SELECT QualifiedApiName FROM EntityDefinition WHERE KeyPrefix=\'{id[0:3]}\'" --json', shell=True)
    sObject = json.loads(output)['result']['records'][0]['QualifiedApiName']
    output = subprocess.check_output(f'sf data query -q "SELECT Fields(all) FROM {sObject} WHERE Id = \'{id}\' LIMIT 1" --json', shell=True)
    records = json.loads(output)['result']['records']
    if len(records) > 0:
        record = records[0]
        record.pop('attributes')
        record = {key: ('' if value is None else value if isinstance(value, str) else str(value))for key, value in record.items()}
    else:
        record = None
    return sObject, record

@Sheet.api
def salesforce(sheet):
    value = sheet.cursorValue
    if not bool(re.match(r'^[a-zA-Z0-9]{15}|[a-zA-Z0-9]{18}$', value)):
        vd.fail(f'{value} is not a Salesforce ID')
        return None

    sheet.vd.status(f'Retrieving Salesforce record for ID {value} ...')

    @asyncthread
    def _retrieve_and_display():
        try:
            sObject, record = retrieve_record(value)
            if record is None:
                vd.fail(f"{sObject} {value} does not exist on your Org")
                return

            new_sheet = Sheet(f'{sObject}_{value}')
            for field, field_value in record.items():
                field_col = Column(field, getter=lambda col, row, field=field: row.get(field))
                new_sheet.addColumn(field_col)
            new_sheet.rows = [record]
            vd.push(new_sheet)
            sheet.vd.status(f"Retrieved '{sObject}' record with {len(record)} fields")
        except Exception as e:
            sheet.vd.exceptionCaught(e)

    _retrieve_and_display()

Sheet.addCommand('0', 'retrieve-salesforce-record', 'sheet.salesforce()')
