# VisiData Plugins

Some [VisiData](https://www.visidata.org/) plugins:

- [hide-empty-cols](#hide-empty-cols):
- [one-hot-encode](#one-hot-encode): One-hot encode a column

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

One-hot encode the currently selected column.

This function creates a new binary column for each unique value in the selected column, indicating the presence (1) or absence (0) of that value in each row. The new columns are inserted immediately after the original column.

This prevents assuming an ordinal relationship between categories (e.g., "red" > "green") when using categorical data in models like linear regression, logistic regression and neural networks.

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
