PYTHON = python
# needs kivy installed or in PYTHONPATH

.PHONY: theming apk clean

theming:
	$(PYTHON) -m kivy.atlas pydelhiapp/data/default 2048 tools/theming/*.png
apk:
	bulldozer android_new debug
apk_release:
	buildozer android_new release
