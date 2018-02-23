# SublimeLinter-contrib-aspell [![Build Status](//travis-ci.org/nabijaczleweli/SublimeLinter-contrib-aspell.svg?branch=master)](//travis-ci.org/nabijaczleweli/SublimeLinter-contrib-aspell) [![Licence](//img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)
This linter plugin for [SublimeLinter](//sublimelinter.readthedocs.org) provides an interface to [aspell](//aspell.net). It can be used with files that have the "plain text" or "markdown" syntaxes.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here](//sublimelinter.readthedocs.org/en/latest/installation.html).

### Linter installation
Before using this plugin, you must ensure that `aspell` is installed on your system. To install `aspell`, do the following:

1. Install `aspell` by typing the following in a terminal:
   ```
   <package manager> install aspell
   ```
   Or acquire it from the [aspell website](//aspell.net).

<!-- **Note:** This plugin requires `aspell` __version__ or later. -->

### Linter configuration
In order for `aspell` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in ["Finding a linter executable"](//sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through "Validating your PATH" in the documentation.

Once you have installed and configured `aspell`, you can proceed to install the SublimeLinter-contrib-aspell plugin if it is not yet installed.

### Plugin installation
Please use [Package Control](//sublime.wbond.net/installation) to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette](//docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html) and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `aspell`. Among the entries you should see `SublimeLinter-contrib-aspell`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings](//sublimelinter.readthedocs.org/en/latest/settings.html). For information on generic linter settings, please see [Linter Settings](//sublimelinter.readthedocs.org/en/latest/linter_settings.html).

In addition to the standard SublimeLinter settings, SublimeLinter-contrib-aspell provides its own settings. Those marked as "Inline Setting" or "Inline Override" may also be [used inline](//sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings).

| Setting | Description            |
|:--------|:-----------------------|
| master  | The dictionary to use. |

## Contributing
Note that modifications should follow these guidelines:

  - Indent is 4 spaces.
  - Code should pass flake8 and pep257 linters.
  - Vertical whitespace helps readability, don’t be afraid to use it.
  - Descriptive variable names, no abbreviations unless they are very well known.

[locating-executables]: //sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
