SHELL = /bin/bash
PREFIX?=$(HOME)/Library/Preferences/visidata

install:
	@mkdir -p $(PREFIX)/plugins
	@while read -r f; do cp $${f} $(PREFIX)/$${f}; done < <(fd -e py . plugins)
	@while read -r n; do sed -i '' "/$${n}/d" $(PREFIX)/plugins/__init__.py; done < <(fd -e py . plugins -x echo {/.})
	@while read -r n; do echo "import plugins.$${n}" >> $(PREFIX)/plugins/__init__.py; done < <(fd -e py . plugins -x echo {/.})

uninstall:
	@while read -r f; do rm -f $(PREFIX)/$${f}; done < <(fd -e py . plugins)
	@while read -r n; do sed -i '' "/$${n}/d" $(PREFIX)/plugins/__init__.py; done < <(fd -e py . plugins -x echo {/.})

.PHONY: install uninstall
