# -*- coding: utf-8 -*-

from qgis.core import QGis, QgsFeatureRequest, QgsExpression
from PyQt4.QtGui import QIcon, QAction
from PyQt4.QtCore import QObject, SIGNAL
import resources_rc  
from qgis.gui import QgsMessageBar

class GetFeatureSelected:

    def __init__(self, iface):
        
        self.iface = iface

    def initGui(self):
         
        # cria uma ação que iniciará a configuração do plugin 
        path = self.iface.mainWindow()
        icon_path = ':/plugins/GetFeatureSelected/i.png'
        self.action = QAction (QIcon (icon_path),u"Pega as Feições de uma camada selecionada e envia seu(s)s id(s) no campo filtro", path)
        self.action.setObjectName ("Get Feature Selected")
        self.action.setStatusTip(None)
        self.action.setWhatsThis(None)
        QObject.connect (self.action, SIGNAL ("triggered()"), self.GetFeatureSelected)
        # Adicionar o botão icone
        self.iface.addToolBarIcon (self.action) 

    def unload(self):
        # remove o item de ícone do QGIS GUI.
        self.iface.removeToolBarIcon (self.action)
        
        
    def GetFeatureSelected(self):

      
        canvas = self.iface.mapCanvas()
        layer = canvas.currentLayer()
        
        if layer:

            count = layer.selectedFeatureCount()
            
            selectedId = layer.selectedFeaturesIds()
            print selectedId
            expressao = '(',
            for l in selectedId:
                expressao = expressao+str(l)+','
                expressao.replace(len(expressao)-1,')')
               
                
               
                
                layer.setSubsetString('"id" IN %s'% expressao)
                print layer.setSubsetString('"id" IN %s'% expressao)
           














        #request=QgsFeatureRequest().setFilterExpression(exp)
        #featuresIterator = layer.dataProvider().getFeatures(QgsFeatureRequest().setFilterExpression ('"name" IN ('%s')'% selectedId)
        #expression = QgsExpression('"id" IN ()')
        #layer.setSubsetString(''"id" " IN"'\'%s\'' % selectedId)
        # exp = ('"id" IN ('+str(l)+")")