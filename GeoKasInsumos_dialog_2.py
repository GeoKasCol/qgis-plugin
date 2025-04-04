# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GeoKasInsumosDialog
                                 A QGIS plugin
 GeoKas Insumos
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2025-03-27
        git sha              : $Format:%H$
        copyright            : (C) 2025 by GeoKas
        email                : contacto@geokas.com
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

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
#from qgis.core import QgisInterface

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'GeoKasInsumos_dialog_base_2.ui'))


class GeoKasInsumosDialog_2(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(GeoKasInsumosDialog_2, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

# Crear una subclase de QDockWidget para anclar tu diálogo
class GeoKasInsumosDockableDialog2(QtWidgets.QDockWidget):
    def __init__(self):
        super().__init__("Modelo 3D - GeoKas Insumos")
        
        # Crear una instancia de tu QDialog (GeoKasInsumosDialog_2)
        self.dialog_widget = GeoKasInsumosDialog_2()

        # Establecer tu QDialog como el widget dentro del QDockWidget
        self.setWidget(self.dialog_widget)
