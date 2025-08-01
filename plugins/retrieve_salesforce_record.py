# uses Salesforce REST API to retrieve data of a Salesforce Org.
#
# Requires to have the `sf` CLI tool installed and having set a default authenticated org.
#

__version__ = '0.1.0'
__author__ = 'Thomas Dürr <thomduerr@gmail.com>'

import subprocess
import json
import re
import logging

from visidata import vd, AttrDict, Sheet, Column, ColumnExpr

# logger = logging.getLogger(__name__)
# logging.basicConfig(filename='sf.log', encoding='utf-8', level=logging.DEBUG)

def retrieve_record(id):
    # logger.debug(id)
    output = subprocess.check_output(f'sf data query -q "SELECT QualifiedApiName FROM EntityDefinition WHERE KeyPrefix=\'{id[0:3]}\'" --json', shell=True)
    sObject = json.loads(output)['result']['records'][0]['QualifiedApiName']
    output = subprocess.check_output(f'sf data query -q "SELECT Fields(all) FROM {sObject} WHERE Id = \'{id}\' LIMIT 1" --json', shell=True)
    record = json.loads(output)['result']['records'][0]
    record.pop('attributes')
    record = {key: ('' if value is None else  value if isinstance(value, str) else str(value))for key, value in record.items()}
    return sObject, record

@Sheet.api
def salesforce(sheet):
    value = sheet.cursorValue
    if not bool(re.match(r'^[a-zA-Z0-9]{15}|[a-zA-Z0-9]{18}$', value)):
        sheet.vd.status(f'{value} does not look like a Salesforce ID')
        return None

    sObject, record = retrieve_record(value)
    sheet.vd.status(f'{value} is a {sObject}')
    sheet.vd.status(f'{len(record)}')

    # logger.debug(record)

    new_sheet = Sheet(f'{sObject}')
    for field, value in record.items():
        field_col = Column(field, getter=lambda col, row, field=field: row.get(field))
        new_sheet.addColumn(field_col)
    new_sheet.rows = [record]
    vd.push(new_sheet)

Sheet.addCommand('1', 'retrieve-salesforce-record', 'sheet.salesforce()')
