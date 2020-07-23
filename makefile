TEST_PATH=tests/

run:
	python fdnq/fdnq.py -q 2 --input data/diagonal.inp

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +

.ONESHELL:
tests: clean
	cd $(TEST_PATH) && python -m pytest --verbose --color=yes fdnq_test.py

