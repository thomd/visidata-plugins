PREFIX?=$(HOME)

install:
	@mkdir -p $(PREFIX)/.visidata/plugins
	@cp plugins/hide_empty_cols.py $(PREFIX)/.visidata/plugins
	@echo "import plugins.hide_empty_cols" >> $(PREFIX)/.visidata/plugins/__init__.py

uninstall:
	@rm -f $(PREFIX)/.visidata/plugins/hide_empty_cols.py
	@sed -i '' /import\ plugins.hide_empty_cols/d $(PREFIX)/.visidata/plugins/__init__.py

.PHONY: install uninstall
