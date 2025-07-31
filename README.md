# VisiData Plugins

Some [VisiData](https://www.visidata.org/) plugins:

- [hide-empty-cols](#hide-empty-cols)
- [one-hot-encode](#one-hot-encode)
- [retrieve-salesforce-record](#retrieve-salesforce-record)

## Install

    git clone https://github.com/thomd/visidata-plugins.git
    cd visidata-plugins
    make install

Uninstall with

    make uninstall

> [!NOTE]
> The plugins are only tested on macOS.

## `hide-empty-cols`

Hide all columns which contain no data.

### Usage

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

This prevents assuming an ordinal relationship between categories (e.g., "red" > "green") when using categorical data in linear regression, logistic regression and neural networks.

### Usage

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

## `retrieve-salesforce-record`

Retrieve a Salesforce record of the selected Salesforce ID in a new sheet.

### Example

```
echo -e "A,B,C\n0019V0000138V4QQAU,0039V00001Cv5BiQAJ,8lW9V000001owrRUAQ" | vd
```
