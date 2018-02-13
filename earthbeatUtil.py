# -*- coding: utf-8 -*-
"""
/***************************************************************************
 EarthBeat
                                 A QGIS plugin
 Display pixel multi-bands values in a chart
                              -------------------
        begin                : 2018-01-24
        git sha              : $Format:%H$
        copyright            : (C) 2018 by Bruno Combal
        email                : bruno.combal@gmail.com
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
from qgis.gui import QgsMapToolEmitPoint
from qgis.core import QgsMapLayerRegistry

class earthbeatPointData():
	def __init__(self, layer, point, data):
		self.layer = layer
		self.point = point
		self.data = data

class getClickedPoint(QgsMapToolEmitPoint):
    def __init__(self, canvas, dockwidget):
        self.canvas = canvas
        self.dockwidget = dockwidget
        QgsMapToolEmitPoint.__init__(self, self.canvas)

    def canvasPressEvent( self, e ):
    	# is there any multiband layers selected?
    	for layer in QgsMapLayerRegistry.instance().mapLayers().values():
    		print layer.name()


    	# get current position
        point = self.toMapCoordinates(self.canvas.mouseLastXY())
        point = list(point)
        print point
        self.dockwidget.label.setText('done')


