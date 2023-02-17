#!/usr/bin/python3
# -*- coding=utf-8 -*-
__credits__ = ["KOLO, RORIWA"]
__version_info__ = (0, 0, 1)
__version__ = '.'.join(str(_) for _ in __version_info__)
__maintainer__ = "KOLO, RORIWA"
__status__ = "Prototype"  # Prototype, Development, Production
r"""

"""
import re
import typing
from datetime import datetime
import pydantic
import shutil
import os
import tempfile
from git import Repo


REGEX = r"(?P<hash>[a-z0-9]+);(?P<datetime>.+);(?P<author_name>.+);(?P<email>.+)\n\n" \
        r"(?: (?P<files_changed>\d+) files? changed,?)?" \
        r"(?: (?P<lines_inserted>\d+) insertions?\(\+\),?)?" \
        r"(?: (?P<lines_deleted>\d+) deletions?\(\-\))?"
url = "https://github.com/konstantinlob/gitalytics.org"


class ParsedCommit(pydantic.BaseModel):
    hash: str
    author_name: str
    email: str
    datetime: datetime
    files_changed: int
    lines_inserted: int
    lines_deleted: int

    @pydantic.validator('files_changed', 'lines_inserted', 'lines_deleted', pre=True)
    def validate(cls, value):
        return value or 0


def parseLog(log: str) -> typing.Iterator[ParsedCommit]:
    for match in re.finditer(REGEX, log):
        yield ParsedCommit(**match.groupdict())


if __name__ == '__main__':
    my_logger.createLogFilesIfNecessary()
    output=getLog(url)
    for commit in parseLog(output):
        print(commit)
