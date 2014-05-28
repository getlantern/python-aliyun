# Copyright 2014, Quixey Inc.
# 
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License. You may obtain a copy of the
# License at
# 
#      http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

BUILD=0
all: clean test

clean:
	rm -rf build
	rm -rf python-aliyun*.deb build *.egg-info *.egg
	find . -name '*.pyc' -exec rm {} \;
	mkdir build

test: clean
	python ./setup.py nosetests -v --with-coverage --cover-package aliyun --cover-xml --cover-xml-file=build/coverage.xml
	mv *.egg-info build/

deb: test
	fpm -s python -t deb --deb-user root --deb-group root --iteration=$(BUILD) .
	rm -rf *.egg-info
	mv *.deb build/

docs: test
	sphinx-apidoc --separate --full -H "python-aliyun" -A "Adam Gray, Akshay Dayal, North Bits" . -o docs/
	rm -rf docs/tests* docs/setup*
	python ./setup.py build_sphinx -a -s docs --build-dir docs/_build