runtests:
	python -m unittest discover
run:
	python3 src/main_graphical.py

clear:
	rm -rf src/__pycache__
	rm -rf tests/__pycache__
