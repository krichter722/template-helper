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

import os
import logging
import tempfile
import subprocess as sp

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
logger.addHandler(ch)

meld_default = "meld"

def template_header(tmpl_file_path):
    """
    Generates line breaks for a one or multiline path statement in the "Don't
    modify statement" in a template output file. Rather than dealing with an
    offset at the beginning the file path can always start in a new line and
    contain a newline character at the end. Usage could be the following

    ################################################################################
    # DO NOT MODIFY THIS FILE.                                                     #
    # It is generated by the                                                       #
    $template_helper($tmpl_file_path)
    # template. Make modifications there and regenerate this file.                 #
    ################################################################################

    """
    ret_value = ""
    remaining = tmpl_file_path
    while len(remaining) > 0:
        ret_value += "# "
        if len(remaining) < 80-2-2:
            ret_value += remaining
            ret_value += " "*(80-2-2-len(remaining))
            remaining = ""
            ret_value += " #"
        else:
            ret_value += remaining[:80-2-2]
            remaining = remaining[80-2-2:]
            ret_value += " #\n"
    return ret_value


def write_template_file(tmpl, target, check_output=True, meld=meld_default):
    """generates a `str` from tmpl and writes it into the path pointed to by
    `target`. If `check_output` is `True` and the file pointed to by
    `target` exists its content is compared to the generated `str` and the
    `meld` command is invoked with the file pointed to by `target` and the
    generated `str` written into a temporary file (because `melt` only
    accepts file paths as argument) if the two don't match.
    """
    tmpl_str = str(tmpl)
    if check_output and os.path.exists(target):
        target_file = open(target, "r")
        target_file_content = target_file.read()
        target_file.close()
        if tmpl_str != target_file_content:
            logger.warn("template content doesn't match with content of existing target file '%s', opening meld in order to investigate" % (target,))
            tmpl_str_temp_file, tmpl_str_temp_file_path = tempfile.mkstemp(text=True)
            logger.info("writing template content for target '%s' into temporary file '%s' in order to be able to pass it to meld" % (target, tmpl_str_temp_file_path,))
            os.write(tmpl_str_temp_file, tmpl_str)
            os.close(tmpl_str_temp_file)
            sp.check_call([meld, target, tmpl_str_temp_file_path])
            answer = None
            while answer != "y" and answer != "n":
                answer = raw_input("Proceed with script (y/n)? ")
            if answer == "n":
                raise RuntimeError("Aborted by user")
    t_file = open(target, "w") # open target for writing after opening and
        # closing it for reading
    t_file.write(tmpl_str)
    t_file.flush()
    t_file.close()
    logger.info("created %s" % (target,))

