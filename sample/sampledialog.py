# -*- coding: utf-8 -*-
"""
/***************************************************************************
 sampleDialog
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
"""

from PyQt4 import QtCore, QtGui
from ui_sample import Ui_sample
# create the dialog for zoom to point


class sampleDialog(QtGui.QDialog, Ui_sample):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
