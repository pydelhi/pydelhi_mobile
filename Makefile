PYTHON = python
# needs kivy installed or in PYTHONPATH

.PHONY: theming apk clean

theming:
	$(PYTHON) -m kivy.atlas pyconindia/data/default 2048 tools/theming/*.png
apk:
	buildozer android_new debug
apk_release:
	buildozer android_new release
