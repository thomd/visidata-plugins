# VisiData Plugins

> [!NOTE]
> The plugins are only tested on macOS.

## Install

    git clone https://github.com/thomd/visidata-plugins.git
    cd visidata-plugins
    make install

Uninstall with

    make uninstall

## `hide-empty-cols`

This plugin hides **all** columns which contain no data.

Use command `hide-empty-cols`.

### Test

    echo -e "col1,col2,col2,col4\n1,,,\n5,,7," | vd

Before:

| col1 | col2 | col3 | col4 |
| ---- | ---- | ---- | ---- |
| 1    |      |      |      |
| 5    |      | 7    |      |

After:

| col1 | col3 |
| ---- | ---- |
| 1    |      |
| 5    | 7    |

## `one-hot-encode`

Use command `one-hot-encode`.

One hot encode values of a column.

### Test

    echo -e "color\nred\ngreen\nred\nblue\ngreen" | vd

Before:

| color |
| ----- |
| red   |
| green |
| red   |
| blue  |

After:

| color | color_blue | color_green | color_red |
| ----- | ---------- | ----------- | --------- |
| red   | 0          | 0           | 1         |
| green | 0          | 1           | 0         |
| red   | 0          | 0           | 1         |
| blue  | 1          | 0           | 0         |

