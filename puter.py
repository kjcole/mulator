#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  puter.py
#  Copyright 2016 Kevin Cole <kevin.cole@novawebcoop.org> 2016.12.13
#
#  This is my crack at a machine language emulator.  The starting point is
#
#    http://appinventor.cs.trincoll.edu/csp/webapps/computer/gen0.html
#
#  However, we're going with an 8-bit machine, implementing it in
#  Python and Bottle (http://bottlepy.org/), and also incorporating
#  elements of Chris Meyer's Python 4 Fun:
#
#    http://www.openbookproject.net/py4fun/
#
#  being copied by Jeff Elkner to:
#
#    http://bazaar.launchpad.net/~jelkner/python4fun/python4fun/view/\
#    head:/source/_static/mm_simulator/mm_simulator.py
#
#           -- GNU General Purpose License (GPL) --
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


class CPU:

    def __init__(self):
        """Build a machine"""
        self.instruction_register = 0
        self.accumulator = 0
        self.instruction_counter = 0
        self.monitor = None
        self.ram = [0] * 8192  # This has a whopping 8 KB of RAM !!!
        self.instruction_set = {0b1000: self.reboot,
                                0b1001: self.add,
                                0x1010: self.store,
                                0x1011: self.load,
                                0x1100: self.prn}

    def reboot(self):
        """Reinitialize everything on a reboot"""
        self.__init__()

    def add(self, address):
        """Add value at address to value in accumulator"""
        self.accumulator += self.ram[address]

    def store(self, address):
        """Store value from accumulator into memory address"""
        self.ram[address] = self.accumulator

    def load(self, address):
        """Load value from memory address into accumulator"""
        self.accumulator = self.ram[address]

    def prn(self, address):
        """Print value at memory address to monitor"""
        self.monitor = self.ram[address]
        print(self.monitor)  # Use bottle, not print to stdout


def main():
    _ = os.system("clear")
    print("{0} v.{1}, {2} <{3}> ({4})\n"
          .format(__appname__,
                  __version__,
                  __copyright__,
                  __email__,
                  __license__))

    cpu = CPU()
    cpu.instruction_set[0x1010](0b1010)  # Print what's at location 1010

    return 0

if __name__ == "__main__":
    main()
