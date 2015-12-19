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

# This script allows to share configuration constants for default values of
# server and client configuration. All configuration directive ought to be still
# configurable, though. Constants of this file shouldn't be used directly, but
# a constant pointing to constants in this file should be created in a using
# file
#
# Both server and client scripts should share default values involving shared
# constants (e.g. maven proxy installation concerns both client and server and
# setting the default value in this file allows client and server configuration
# scripts to pick it up at the same place, but still to override it).
#
# Constants which don't concern both client and server configuration, but might
# in the future can be moved to this file.
#
# Tip: If multiple programs share a setting (e.g. all maven proxies share a host
# and a port in standalone installation), name the variables after the shared
# aspect only. Different names in templates make sense, of course.

# some shared documentation (more elegant, but somehow overkill to move into
# another file
__difftool_doc__ = "the difftool to used (recommended are `meld` if a graphical user interface is availble and `cdiff` if only a console is available or you prefer it"

# tomcat
tomcat_port_default = 8081

# archiva
ARCHIVA_INSTALL_STANDALONE = "standalone"
ARCHIVA_INSTALL_WAR = "war"
ARCHIVA_INSTALLS = [ARCHIVA_INSTALL_STANDALONE, ARCHIVA_INSTALL_WAR]
archiva_install_default = ARCHIVA_INSTALL_STANDALONE

# artifactory
ARTIFACTORY_INSTALL_PACKAGE = "package"
ARTIFACTORY_INSTALL_STANDALONE = "standalone"
ARTIFACTORY_INSTALLS = [ARTIFACTORY_INSTALL_PACKAGE, ARTIFACTORY_INSTALL_STANDALONE]
artifactory_install_default = ARTIFACTORY_INSTALL_STANDALONE

# maven proxy
MAVEN_PROXY_ARCHIVA = "archiva"
MAVEN_PROXY_ARTIFACTORY = "artifactory"
MAVEN_PROXY_NEXUS = "nexus"
MAVEN_PROXYS = [MAVEN_PROXY_ARCHIVA, MAVEN_PROXY_ARTIFACTORY]
maven_proxy_default = MAVEN_PROXY_ARTIFACTORY # archiva stable (both war and
    # standalone seem to be broken)
maven_proxy_host_default = "richtercloud.de"

if maven_proxy_default == MAVEN_PROXY_ARTIFACTORY:
    if artifactory_install_default == ARTIFACTORY_INSTALL_STANDALONE:
        maven_proxy_port_default = 8085
    elif artifactory_install_default == ARTIFACTORY_INSTALL_PACKAGE:
        maven_proxy_port_default = 8085
    else:
        raise ValueError()
elif maven_proxy_default == MAVEN_PROXY_ARCHIVA:
    if archiva_install_default == ARCHIVA_INSTALL_STANDALONE:
        maven_proxy_port_default = 8085
    elif archiva_install_default == ARCHIVA_INSTALL_WAR:
        maven_proxy_port_default = tomcat_port_default
    else:
        raise ValueError()
else:
    raise ValueError()

difftool_default = "meld"
