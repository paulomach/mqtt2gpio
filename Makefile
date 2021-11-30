clean:
	rm -rf .tox/ src/mqtt2gpio.egg-info build/ dist/

build:
	tox -e build
