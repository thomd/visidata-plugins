# VisiData Plugins

Some [VisiData](https://www.visidata.org/) plugins.

## Install

    git clone https://github.com/thomd/visidata-plugins.git
    cd visidata-plugins
    make install

Uninstall with

    make uninstall

> [!NOTE]
> The plugins are only tested on macOS.

## `hide-empty-cols`

This plugin hides **all** columns which contain no data.

Use command `hide-empty-cols`.

### Example

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

One hot encode values of a column.

Use command `one-hot-encode`.

### Example

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

