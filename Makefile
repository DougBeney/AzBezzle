all:
	pyinstaller azbezzle.py --onefile

clean:
	rm *.spec
	rm -rf build/
	rm -rf dist/
	rm -rf __pycache__/
	rm -rf .ropeproject/

