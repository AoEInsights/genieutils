export SHELL := /usr/bin/env bash

build:
	swig -Wall -c++ -python GenieUtils/DatFile.i
