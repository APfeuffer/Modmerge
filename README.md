# Modmerge
A simple tool for game modding: Recursively merges multiple directory trees using symlinks.

## Usage

python3 link_mods.py DESTINATION MODDIRS... GAMEDIR

This will create new directories at DESTINATION assembled from the first file found in any of the MODDIRS, or from GAMEDIR if none is found. Directories are also linked if only one exists; otherwise, they are merged. May also be used on subdirectories. Example:

- The game has all relevant assets in "data/" and your mod is named "mymod/"
- Make sure all files you want to replace are in the proper location
- E.g.: If the original file was "data/foo/bar.txt", yours should be "mymod/data/foo/bar.txt"
- Make a new directory for the unmodified game files (e.g. "base/") and move "data/" there (now "base/data/")
- Install Python 3 (if you don't have it already)
- Copy "link_mods.py" to the game directory
- run "python3 link_mods.py . mymod base"
- You should now have a new data/ directory of symlinks to either your mod's or the base game's files and dirs
