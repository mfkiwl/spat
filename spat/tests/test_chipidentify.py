'''
NOTICE

Copyright 2018 National Technology & Engineering Solutions of Sandia, LLC
(NTESS). Under the terms of Contract DE-NA0003525 with NTESS, the U.S.
Government retains certain rights in this software.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

---

Tests for module spat.sigfile
'''

from __future__ import print_function
import os
import sys
if sys.version_info[0] > 2:
    from unittest.mock import patch, call, MagicMock, mock_open
    from unittest import TestCase, main, skipIf
    from io import StringIO
else:
    from mock import patch, call, MagicMock, mock_open
    from unittest2 import TestCase, main, skipIf
    from StringIO import StringIO

from bitstring import Bits
from spat.chipidentify import ChipIdentify

class ChipIdentifyTests(TestCase):
    'ChipIdentify unit tests'

    def setUp(self):
        with patch('spat.chipidentify.ChipIdentify.load') as self.m_load, \
                patch('os.path.isfile') as self.m_isfile, \
                patch('spat.chipidentify.ChipIdentify.__len__') as self.m_len, \
                patch('os.path.isdir') as self.m_isdir, \
                patch('os.makedirs') as self.m_makedirs, \
                patch('spat.chipidentify.ChipIdentify.setup') as self.m_setup:
            self.m_isfile.return_value = True
            self.m_len.return_value = 3
            self.ci = ChipIdentify('foo', 10)


    def test_init(self):
        self.assertEqual(self.ci.n_bits, 10)
        self.assertEqual(self.ci.fileName, 'foo')

        self.m_load.assert_called()
        self.m_isfile.assert_called_with('foo')
        self.m_len.assert_called()
        self.m_setup.assert_called()
