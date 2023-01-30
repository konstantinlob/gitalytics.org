#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
__version_info__ = (0, 1, 0)
__version__ = '.'.join(str(_) for _ in __version_info__)

import argparse as __ap
from dataclasses import dataclass as _dt


@_dt(init=False)
class Namespace:
    host: str
    port: int
    reload: bool
    workers: int


__parser = __ap.ArgumentParser(
    description=__doc__,
    formatter_class=__ap.ArgumentDefaultsHelpFormatter
)
__parser.add_argument("-v", "--version", action="version", version=__version__)
__parser.add_argument("--global", action="store_const", dest="host", const="0.0.0.0", default="127.0.0.1",
                      help="make this api available in the local network")
__parser.add_argument("-p", "--port", type=int, default=8000,
                      help="port to bind to")
__parser.add_argument("--reload", action="store_true", default=False,
                      help="automatically reload after changes")
__parser.add_argument("-w", "--workers", type=int,
                      help="number of workers (for production)")

args = __parser.parse_args(namespace=Namespace())