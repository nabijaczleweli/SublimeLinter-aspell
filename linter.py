#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by nabijaczleweli
# Copyright (c) 2018 nabijaczleweli
#
# License: MIT
#


"""This module exports the Aspell plugin class."""


from SublimeLinter.lint import Linter, util


class Aspell(Linter):
    """Provides an interface to aspell."""

    syntax = ('Plain text', 'Markdown')
    cmd = 'aspell -a'
    executable = None
    version_args = '--version'
    version_re = r'Aspell\s(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.0.0'
    regex = r'&\s(?P<near>\S+)\s(?P<amount>\d+)\s(?P<line>\d+):\s(?P<message>(?:[^,]+(?:,\s)?)+)'
    multiline = False
    line_col_base = (0, 0)
    tempfile_suffix = None
    error_stream = util.STREAM_STDERR
    selectors = {}
    word_re = None
    defaults = {
        '--master': 'en',
    }
    inline_settings = None
    inline_overrides = None
    comment_re = None

    def split_match(self, match):
        """
        Extract and return values from match.

        We override this method so that general errors that do not have
        a line number can be placed at the beginning of the code.
        """

        match, line, col, error, warning, message, near = super().split_match(match)

        if message:
            message = 'Typo, consider these replacements: ' + message

        warning = True

        return match, line, col, error, warning, message, near
