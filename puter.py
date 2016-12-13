#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  puter.py
#
#  Copyright 2016 Kevin Cole <kevin.cole@novawebcoop.org> 2016.12.13
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License as
#  published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public
#  License along with this program; if not, write to the Free
#  Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
#  Boston, MA 02110-1301, USA.
#
#


from __future__ import print_function
from six.moves  import input           # use raw_input when I say input
from os.path    import expanduser      # Cross-platform home directory finder
import os
import sys

__appname__    = ""
__author__     = "Kevin Cole, Jeff Elkner, and Christopher Hedrick"
__copyright__  = "Copyright 2016, NOVA Web Development, LLC"
__credits__    = ["Kevin Cole", "Jeff Elkner", "Christopher Hedrick",
                  "Mayra Villanueva"]  # Authors and bug reporters
__license__    = "GPL"
__version__    = "1.0"
__maintainer__ = "Kevin Cole"
__email__      = "kevin.cole@novawebcoop.org"
__status__     = "Prototype"  # "Prototype", "Development" or "Production"
__module__     = ""


def main():
    _ = os.system("clear")
    print("{0} v.{1}, {2} <{3}> ({4})\n"
          .format(__appname__,
                  __version__,
                  __copyright__,
                  __email__,
                  __license__))

    # [Your code here]

    return 0

if __name__ == "__main__":
    main()
