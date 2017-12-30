all:
	pyinstaller azbezzle.py --onefile

clean:
	rm *.spec
	rm -rf build/
	rm -rf dist/
	rm -rf __pycache__/
	rm -rf .ropeproject/

install_windows:
	@echo "Windows install script not availible. You will have to do it manually."
	@echo "If you have ran 'make' you should have a CLI-executable application in your `dist/` folder"

install_unix:
	@echo "Installing for Mac/Linux operating systems..."
	sudo cp ./dist/azbezzle /usr/bin/azbezzle
uninstall_unix:
	@echo "Uninstalling for Mac/Linux operating systems..."
	sudo rm /usr/bin/azbezzle
