#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import os
import logging.handlers


LOGGING_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        'backend-logs'
    )
)
if not os.path.isdir(LOGGING_PATH):
    os.mkdir(LOGGING_PATH)


class WatchFilesFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return not record.name.startswith("watchfiles")


debugHandler = logging.handlers.TimedRotatingFileHandler(
    filename=os.path.join(LOGGING_PATH, "backend.log"),
    when="midnight",
    backupCount=4,
    delay=True,
    utc=True,
)
debugHandler.addFilter(WatchFilesFilter())
debugHandler.setLevel(logging.DEBUG if __debug__ else logging.INFO)  # DEBUG/INFO and up

warningHandler = logging.handlers.TimedRotatingFileHandler(
    filename=os.path.join(LOGGING_PATH, "backend-warning.log"),
    when="midnight",
    backupCount=7,
    delay=True,
    utc=True,
)
warningHandler.addFilter(WatchFilesFilter())
warningHandler.setLevel(logging.WARNING)  # WARNING and up

consoleLoggingHandler = logging.StreamHandler()
consoleLoggingHandler.addFilter(WatchFilesFilter())

FORMAT = "{asctime} | {levelname:.3} | {processName}/{threadName} | {module:20} | {funcName:20} | {lineno:3} | {message}"  # noqa: E501

logging.basicConfig(
    format=FORMAT,
    style="{",
    level=logging.DEBUG,  # minimum LEVEL (is overwritten by the handlers)
    handlers=[
        debugHandler,
        warningHandler,
        consoleLoggingHandler if __debug__ else logging.NullHandler()
    ],
)
