# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GeoKasInsumos
                                 A QGIS plugin
 GeoKas Insumos
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2025-03-27
        copyright            : (C) 2025 by GeoKas
        email                : contacto@geokas.com
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
    """Load GeoKasInsumos class from file GeoKasInsumos.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .GeoKasInsumos import GeoKasInsumos
    return GeoKasInsumos(iface)
