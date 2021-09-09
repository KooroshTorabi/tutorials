# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ElevationTileDownloader
                                 A QGIS plugin
 Downloads elevation tiles 
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-09-01
        copyright            : (C) 2021 by Christian Beiwinkel
        email                : christian@gis-ops.com
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
    """Load ElevationTileDownloader class from file ElevationTileDownloader.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .elevation_tile_downloader import ElevationTileDownloader
    return ElevationTileDownloader(iface)