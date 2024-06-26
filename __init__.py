# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Consumo_servicio_IGAC
                                 A QGIS plugin
 Plugin para cosumir servicio estaciones CORS
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-04-28
        copyright            : (C) 2024 by Ricardo cepeda
        email                : idu054441@usal.es
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
    """Load Consumo_servicio_IGAC class from file Consumo_servicio_IGAC.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Validador_CORS import Consumo_servicio_IGAC
    return Consumo_servicio_IGAC(iface)
