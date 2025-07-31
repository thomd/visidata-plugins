# uses Salesforce REST API.
#
# Requires to have the `sf` CLI tool installed and having set a default org.
#

__version__ = '0.1.0'
__author__ = 'Thomas Dürr <thomduerr@gmail.com>'

import subprocess
import json
import re
import logging

from visidata import vd, AttrDict, Sheet, Column, ColumnExpr

logger = logging.getLogger(__name__)
logging.basicConfig(filename='sf.log', encoding='utf-8', level=logging.DEBUG)

def retrieve_record(id):
    'TODO: description'
    logger.debug(id)
    output = subprocess.check_output(f'sf data query -q "SELECT QualifiedApiName FROM EntityDefinition WHERE KeyPrefix=\'{id[0:3]}\'" --json', shell=True)
    logger.debug(output)
    sObject = json.loads(output)['result']['records'][0]['QualifiedApiName']
    logger.debug(f'sf data query -q "SELECT Fields(all) FROM {sObject} WHERE Id = \'{id}\' LIMIT 1" --json')
    output = subprocess.check_output(f'sf data query -q "SELECT Fields(all) FROM {sObject} WHERE Id = \'{id}\' LIMIT 1" --json', shell=True)
    logger.debug(output)
    record = json.loads(output)['result']['records'][0]
    logger.debug(record)
    record.pop('attributes')
    return sObject, record

@Sheet.api
def salesforce(sheet):
    value = sheet.cursorValue
    if not bool(re.match(r'^[a-zA-Z0-9]{15}|[a-zA-Z0-9]{18}$', value)):
        sheet.vd.status(f'{value} does not look like a Salesforce ID')
        return None

    sObject, record = retrieve_record(value)
    sheet.vd.status(f'Id {value} is a {sObject}')

    # new_sheet = Sheet('new_sheet')
    # new_col = Column('Value')
    # new_sheet.addColumn(new_col)
    # sheet.vd.status(new_sheet)
    # new_sheet.addRow([value])
    # sheet.vd.addSheet(new_sheet)

Sheet.addCommand('1', 'retrieve-salesforce-record', 'sheet.salesforce()')
