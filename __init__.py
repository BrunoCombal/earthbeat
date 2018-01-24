# -*- coding: utf-8 -*-
"""
/***************************************************************************
 EarthBeat
                                 A QGIS plugin
 Display pixel multi-bands values in a chart
                             -------------------
        begin                : 2018-01-24
        copyright            : (C) 2018 by Bruno Combal
        email                : bruno.combal@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load EarthBeat class from file EarthBeat.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .earthbeat import EarthBeat
    return EarthBeat(iface)
