__version__ = '0.1.1'
__author__ = 'Thomas Dürr <thomduerr@gmail.com>'

from visidata import Sheet, BaseSheet, asyncthread, copy, Progress, vd

def identify_empty_cols(sheet):
    rows = sheet.rows
    for column in sheet.columns:
        values = list(column.getValues(rows))
        if not any(values):
            yield column

@Sheet.api
def hide_empty_cols(sheet):
    vs = copy(sheet)
    vs.name += '_hidden_empty_cols'

    @asyncthread
    def _reload(self=vs):
        num_empty_cols = 0
        self.rows = sheet.rows
        gen = identify_empty_cols(self)
        prog = Progress(gen, gerund='hiding empty cols', total=self.nCols)
        for col in prog:
            num_empty_cols += 1
            col.setWidth(0)
        if num_empty_cols == 0:
            vd.warning(f'No empty cols')
        else:
            vd.status(f"Removed {num_empty_cols} empty column{'s' if num_empty_cols > 1 else ''}")

    vs.reload = _reload
    vd.push(vs)

BaseSheet.addCommand(Null, 'hide-empty-cols', 'sheet.hide_empty_cols()')
