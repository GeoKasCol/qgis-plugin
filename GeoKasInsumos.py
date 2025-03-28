# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GeoKasInsumos
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
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QComboBox, QCheckBox  # Add import for QComboBox and QCheckBox
from qgis.core import QgsRasterLayer, QgsProject  # Import QgsRasterLayer and QgsProject

# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
from .GeoKasInsumos_dialog import GeoKasInsumosDialog
import os.path
import os
from qgis.PyQt.QtWidgets import QFrame


class GeoKasInsumos:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'GeoKasInsumos_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&GeoKas Insumos')

        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        self.first_start = None

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('GeoKasInsumos', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            # Adds plugin icon to Plugins toolbar
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/GeoKasInsumos/icon.png'

        current_directory = os.path.dirname(os.path.realpath(__file__))
        eye_path = current_directory+"/icon_eye_2.png"

        self.add_action(
            eye_path,
            text=self.tr(u'GeoKas Insumos'),
            callback=self.run,
            parent=self.iface.mainWindow())


        self.separador1 = QFrame()
        self.separador1.setFrameShape(QFrame.VLine)
        self.separador1.setFrameShadow(QFrame.Sunken)
        self.iface.addToolBarWidget(self.separador1)
        
        # Add combo box to the toolbar
        self.combo_box = QComboBox(self.iface.mainWindow())
        self.combo_box.addItems(["Ir a ...", "Jamundi", "Zipaquira"])
        self.combo_box.currentTextChanged.connect(self.cambioComboBoxZona)
        self.iface.addToolBarWidget(self.combo_box)

        self.separador2 = QFrame()
        self.separador2.setFrameShape(QFrame.VLine)
        self.separador2.setFrameShadow(QFrame.Sunken)
        self.iface.addToolBarWidget(self.separador2)

        self.check_box = QCheckBox(self.iface.mainWindow())
        self.check_box.setText("Mostrar AOI's")
        self.check_box.stateChanged.connect(self.cambioMostrarAOI)
        self.iface.addToolBarWidget(self.check_box)

        self.separador3 = QFrame()
        self.separador3.setFrameShape(QFrame.VLine)
        self.separador3.setFrameShadow(QFrame.Sunken)
        self.iface.addToolBarWidget(self.separador3)

        self.combo_box2 = QComboBox(self.iface.mainWindow())
        self.combo_box2.addItems(["Agregar Basemap ...", "XYZ Jamundi", "XYZ Bruselas"])
        self.combo_box2.currentTextChanged.connect(self.cambioComboBoxXYZ)
        self.iface.addToolBarWidget(self.combo_box2)

        # will be set False in run()
        self.first_start = True


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&GeoKas Insumos'),
                action)
            self.iface.removeToolBarIcon(action)
        self.separador1.setParent(None)
        self.combo_box.setParent(None)
        self.separador2.setParent(None)
        self.check_box.setParent(None)
        self.separador3.setParent(None)
        self.combo_box2.setParent(None)

    def cambioComboBoxZona(self, text):
        print("Opcion seleccionada: "+text)
    
    def cambioComboBoxXYZ(self, text):
        print("Opcion seleccionada: "+text)
        if text == "XYZ Jamundi":
            layer = QgsRasterLayer(
                "type=xyz&url=https://xyz-jamundi.geokas.com.co/Z{z}/{y}/{X}.jpg?token=asbdasjdbas&zmax=23",
                "XYZ Jamundi",
                "wms"
            )
            if not layer.isValid():
                print("Failed to load XYZ Jamundi layer")
            else:
                QgsProject.instance().addMapLayer(layer)
        elif text == "XYZ Bruselas":
            layer = QgsRasterLayer(
                "type=xyz&url=https://2d-bruselas-pit-col.falconprecision.co/Z{z}/{y}/{X}.png?token=asbdasjdbas&zmax=23",
                "XYZ Bruselas",
                "wms"
            )
            if not layer.isValid():
                print("Failed to load XYZ Bruselas layer")
            else:
                QgsProject.instance().addMapLayer(layer)

    def on_license_changed(self):
        if len(self.dlg.lineEditLicencia.text()) > 0:
            self.dlg.buttonVerificar.setEnabled(True)
        else:
            self.dlg.buttonVerificar.setEnabled(False)

    def verificarClicked(self):
        current_directory = os.path.dirname(os.path.realpath(__file__))
        file_path = current_directory+"/license.txt"
        print(file_path)
    
        if not os.path.exists(file_path):
            # Si el archivo no existe, lo creamos y escribimos algo en él
            with open(file_path, 'w') as file:
                file.write(self.dlg.lineEditLicencia.text())
            #print("Archivo 'license.txt' creado.")
        else:
            # Si el archivo ya existe, lo leemos
            with open(file_path, 'r') as file:
                content = file.read()
            if content != self.dlg.lineEditLicencia.text():
                os.remove(file_path)
                with open(file_path, 'w') as file:
                    file.write(self.dlg.lineEditLicencia.text())
            #print("Contenido del archivo 'license.txt':")
            #print(content)
        self.dlg.labelNombreLicencia.setText("Licencia verificada")
        self.dlg.labelDuracionLicencia.setText("Desde 01/01/2025 hasta 01/01/2026")

    def cambioMostrarAOI(self, state):
        if state == 2:
            print("State changed: " + str(state))
        elif state == 0:
            
        print("State changed: " + str(state))
    
    def run(self):
        """Run method that performs all the real work"""

        # Create the dialog with elements (after translation) and keep reference
        # Only create GUI ONCE in callback, so that it will only load when the plugin is started
        if self.first_start == True:
            self.first_start = False
            self.dlg = GeoKasInsumosDialog()

        # show the dialog
        self.dlg.show()

        self.dlg.lineEditLicencia.textChanged.connect(self.on_license_changed)
        self.dlg.buttonVerificar.clicked.connect(self.verificarClicked)
        

        current_directory = os.path.dirname(os.path.realpath(__file__))
        file_path = current_directory+"/license.txt"
        print(file_path)
    
        if os.path.exists(file_path):
            print("prueba")
            # Si el archivo existe
            with open(file_path, 'r') as file:
                content = file.read()
                self.dlg.lineEditLicencia.setText(content)
            self.dlg.labelNombreLicencia.setText("Licencia verificada")
            self.dlg.labelDuracionLicencia.setText("Desde 01/01/2025 hasta 01/01/2026")
            #print("Contenido del archivo 'license.txt':")
            #print(content)

        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            # Do something useful here - delete the line containing pass and
            # substitute with your code.
            pass
