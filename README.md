# learn-python-sandbox

A collection of Python3 practice problems.

# How to Run

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) on Host Machine.
2. Install [Download Visual Studio Code - Mac, Linux, Windows](https://code.visualstudio.com/download) on Host Machine.
3. If you want to get straight to running and debugging:
   1. Run VSCode Task `"docker compose run"` (this will also run the `"docker compose build"` task, prior).
   2. While the docker containter is running, open VSCode Debugger tab and run `"Python: Attach to Docker"` launcher. Set breakpoints for whatever module lines you want to pause at.
   3. On the VSCode Terminal, you can select between all the sub-packages and their entry-points right under the main root-package: `"sandbox"`.

# Adding/Remove More Modules

The way this project works is that `select_module` package's `main.__main__` function is called, and it recursively lists all sub-packages under `"sandbox"`, and allows the user to run the `main.py` modules in those packages.

Simply delete/duplicate any of the sub-package directories and modify the names and code to reflect what you want your package to do. It should automatically show up when the entry point of the entire project starts (stop and re-run `"docker compose run"` to see changes).

# TODO

1. Ommit `select_module` from the list of selectable modules.
2. Allow a keyboard shortcut or someway to return to the menu, when selected module is done running.
