"""
One-hot encode the currently selected column.

This function creates a new binary column for each unique value in the selected column,
indicating the presence (1) or absence (0) of that value in each row. The new columns
are inserted immediately after the original column.
"""

__version__ = '0.1.0'
__author__ = 'Thomas Dürr <thomduerr@gmail.com>'

from visidata import Sheet, Column

@Sheet.api
def one_hot_encode_col(sheet):
    col = sheet.cursorCol
    col_idx = sheet.columns.index(col)
    unique_values = sorted(set([row[col_idx] for row in sheet.rows]), reverse=True)

    for val in unique_values:
        def make_func(v):
            return lambda c, r: '1' if r[col_idx] == v else '0'
        new_col = Column(f"{col.name}_{val}", getter=make_func(val))
        sheet.addColumn(new_col, index=col_idx+1)

    sheet.vd.status(f'Added {len(unique_values)} columns')

Sheet.addCommand('', 'one-hot-encode', 'sheet.one_hot_encode_col()', 'one-hot encode the currently selected column')
