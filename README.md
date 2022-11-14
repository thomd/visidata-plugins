# VisiData Plugins

The plugins are only tested for VisiData 2.x

## `hide-empty-cols`

This plugin hides **all** columns which contain no data.

Use command `hide-empty-cols` or the `E` key.

### Test

    echo -e "a,b,c,d\n1,,,\n5,,7," | vd

Before:

| a | b | c | d |
| - | - | - | - |
| 1 |   |   |   |
| 5 |   | 7 |   |

After:

| a | c |
| - | - |
| 1 |   |
| 5 | 7 |

### Install

    git clone https://github.com/thomd/visidata-plugins.git
    cd visidata-plugins
    make install

Uninstall with

    make uninstall
