# -*- coding: utf-8 -*-
"""
/***************************************************************************
 sample
                                 A QGIS plugin
 samlpe
                             -------------------
        begin                : 2014-05-11
        copyright            : (C) 2014 by samlpe
        email                : samlpe
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

def classFactory(iface):
    # load sample class from file sample
    from sample import sample
    return sample(iface)
