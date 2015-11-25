#!/usr/bin/python
# -*- coding: utf-8 -*-

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#    Dieses Programm ist Freie Software: Sie können es unter den Bedingungen
#    der GNU General Public License, wie von der Free Software Foundation,
#    Version 3 der Lizenz oder (nach Ihrer Wahl) jeder neueren
#    veröffentlichten Version, weiterverbreiten und/oder modifizieren.
#
#    Dieses Programm wird in der Hoffnung, dass es nützlich sein wird, aber
#    OHNE JEDE GEWÄHRLEISTUNG, bereitgestellt; sogar ohne die implizite
#    Gewährleistung der MARKTFÄHIGKEIT oder EIGNUNG FÜR EINEN BESTIMMTEN ZWECK.
#    Siehe die GNU General Public License für weitere Details.
#
#    Sie sollten eine Kopie der GNU General Public License zusammen mit diesem
#    Programm erhalten haben. Wenn nicht, siehe <http://www.gnu.org/licenses/>.

import unittest
import template_helper

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(Test, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_generate_header(self):
        # check one row
        result = template_helper.template_header("0123456789")
        self.assertEquals("# 0123456789"+" "*(80-2-2-10)+" #", result)
        # check multiple rows
        result = template_helper.template_header("0123456789"*30)
        self.assertEquals("# 0123456789012345678901234567890123456789012345678901234567890123456789012345 #\n# 6789012345678901234567890123456789012345678901234567890123456789012345678901 #\n# 2345678901234567890123456789012345678901234567890123456789012345678901234567 #\n# 890123456789012345678901234567890123456789012345678901234567890123456789     #", result)

if __name__ == "__main__":
    unittest.main()

