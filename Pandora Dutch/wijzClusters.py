from login import hoofdMenu
from PyQt5.QtCore import Qt, QAbstractTableModel, QRegExp
from PyQt5.QtGui import QFont, QPixmap, QRegExpValidator, QIcon
from PyQt5.QtWidgets import QWidget, QTableView, QDialog, QLabel,\
       QGridLayout, QPushButton, QMessageBox, QLineEdit, QComboBox
from sqlalchemy import (Table, Column, Integer, String, Float, MetaData,\
                         create_engine, select, update)
import logging
logger = logging.getLogger(__name__)

def refresh(keuze, m_email, self):
    logger.warning(">>> Entering refresh(keuze=%s,m_email=%s)", keuze, m_email, extra={"event.action": "refresh", "logrite.keuze": keuze})
    self.close()
    toonClusters(keuze, m_email)
    logger.debug("<<< Exiting refresh(keuze=%s,m_email=%s)", keuze, m_email, extra={"event.action": "refresh", "logrite.keuze": keuze})
    
def updateOK():
    logger.warning(">>> Entering updateOK()", extra={"event.action": "updateOK"})
    msg = QMessageBox()
    logger.debug("updateOK(): msg → %s", msg, extra={"event.action": "updateOK"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Information)
    msg.setText('Je gegevens zijn aangepast!')
    msg.setWindowTitle('Clusters invoeren')
    logger.debug("<<< Exiting updateOK()", extra={"event.action": "updateOK"})
    msg.exec_()

def invoerOK():
    logger.warning(">>> Entering invoerOK()", extra={"event.action": "invoerOK"})
    msg = QMessageBox()
    logger.debug("invoerOK(): msg → %s", msg, extra={"event.action": "invoerOK"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Information)
    msg.setText('Invoer gelukt')
    msg.setWindowTitle('Clusters invoeren')
    logger.debug("<<< Exiting invoerOK()", extra={"event.action": "invoerOK"})
    msg.exec_()
    
def calcBestaat():
    logger.warning(">>> Entering calcBestaat()", extra={"event.action": "calcBestaat"})
    msg = QMessageBox()
    logger.debug("calcBestaat(): msg → %s", msg, extra={"event.action": "calcBestaat"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Information)
    msg.setText('Calculatieregel bestaat al\nen is verrekend met\ningebrachte hoeveelheid!')
    msg.setWindowTitle('Clusters invoeren')
    logger.debug("<<< Exiting calcBestaat()", extra={"event.action": "calcBestaat"})
    msg.exec_()   

def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    
def geenRecord():
    logger.warning(">>> Entering geenRecord()", extra={"event.action": "geenRecord"})
    msg = QMessageBox()
    logger.debug("geenRecord(): msg → %s", msg, extra={"event.action": "geenRecord"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Geen cluster gevonden\nmaak een andere selektie\nof maak een nieuwe cluster s.v.p.!')
    msg.setFont(QFont("Arial",10))
    msg.setWindowTitle('Clusters invoeren')               
    logger.debug("<<< Exiting geenRecord()", extra={"event.action": "geenRecord"})
    msg.exec_() 
    
def ongKeuze():
    logger.warning(">>> Entering ongKeuze()", extra={"event.action": "ongKeuze"})
    msg = QMessageBox()
    logger.debug("ongKeuze(): msg → %s", msg, extra={"event.action": "ongKeuze"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Ongeldige keuze')
    msg.setWindowTitle('Clusters invoeren')               
    logger.debug("<<< Exiting ongKeuze()", extra={"event.action": "ongKeuze"})
    msg.exec_() 
                
def zoeken(m_email):
    logger.warning(">>> Entering zoeken(m_email=%s)", m_email, extra={"event.action": "zoeken"})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            self.setWindowTitle("Cluster selektie")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
                              
            self.Keuze = QLabel()
            logger.debug("__init__(parent=%s): self.Keuze → %s", parent, self.Keuze, extra={"event.action": "__init__"})
            k0Edit = QComboBox()
            logger.debug("__init__(self=%s,parent=%s): k0Edit → %s", self, parent, k0Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): k0Edit → %s", parent, k0Edit, extra={"event.action": "__init__"})
            k0Edit.setFixedWidth(340)
            k0Edit.setFont(QFont("Arial",10))
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.addItem('         Sorteersleutel Clustergroepen')
            k0Edit.addItem('0. Alle Clusters')
            k0Edit.addItem('AA-AL. Spoorstaven + lasmiddelen')
            k0Edit.addItem('BA-BK. Liggers + bevestiging')
            k0Edit.addItem('CA-CK. Overwegen + overwegbeveiliging')
            k0Edit.addItem('DA-DK. Steenslag + grond aanvulling')
            k0Edit.addItem('EA-EK. Wissel + baanconstrukties')
            k0Edit.addItem('FA-FK. Ondergrondse infrastruktuur')
            k0Edit.addItem('GA-GK. Treinbeheersing + seinen')
            k0Edit.addItem('HA-HK. Bovenleiding + draagconstruktie')
            k0Edit.addItem('JA-JK. Voedingen + Onderstations')
            k0Edit.activated[str].connect(self.k0Changed)

            grid = QGridLayout()
            logger.debug("__init__(parent=%s): grid → %s", parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid, extra={"event.action": "__init__"})
            grid.setSpacing(20)
                          
            lbl = QLabel()
            logger.debug("__init__(parent=%s): lbl → %s", parent, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl, extra={"event.action": "__init__"})
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap, extra={"event.action": "__init__"})
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 0, 0, 1, 2)
                        
            grid.addWidget(k0Edit, 1, 1)
            
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 3, 0, 1, 2, Qt.AlignCenter)
            
            logo = QLabel()
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 1, 1, 1, Qt.AlignRight)
   
            applyBtn = QPushButton('Zoeken')
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn, extra={"event.action": "__init__"})
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 2, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Sluiten')
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn, extra={"event.action": "__init__"})
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
    
            grid.addWidget(cancelBtn, 2, 1, 1, 1,Qt.AlignCenter)
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
           
        def k0Changed(self, text):
            logger.warning(">>> Entering k0Changed(text=%s)", text, extra={"event.action": "k0Changed", "logrite.text": text})
            self.Keuze.setText(text)
            logger.debug("<<< Exiting k0Changed(text=%s)", text, extra={"event.action": "k0Changed", "logrite.text": text})
            
        def returnk0(self):
            logger.warning(">>> Entering returnk0()", extra={"event.action": "returnk0"})
            logger.debug("<<< Exiting returnk0()", extra={"event.action": "returnk0"})
            return self.Keuze.text()
                 
        @staticmethod
        def getData(parent=None):
            logger.warning(">>> Entering getData(parent=%s)", parent, extra={"event.action": "getData"})
            dialog = Widget(parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog, extra={"event.action": "getData"})
            dialog.exec_()
            logger.debug("<<< Exiting getData(parent=%s)", parent, extra={"event.action": "getData"})
            return [dialog.returnk0()]       

    window = Widget()
    data = window.getData()
    keuze = ''
    if not data[0]:
        ongKeuze()
        zoeken(m_email)
    elif data[0][0] == '0':
        keuze = ''
    elif data[0]:
        keuze = data[0][0]
    toonClusters(keuze, m_email)  
  
def toonClusters(keuze, m_email):              
    logger.warning(">>> Entering toonClusters(keuze=%s,m_email=%s)", keuze, m_email, extra={"event.action": "toonClusters", "logrite.keuze": keuze})
    class MyWindow(QDialog):
        def __init__(self, data_list, header, *args):
            logger.warning(">>> Entering __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})
            QWidget.__init__(self, *args,)
            self.setWindowTitle('Cluster Calculatie')
            self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
            self.setWindowFlags(self.windowFlags()| Qt.WindowSystemMenuHint |
                              Qt.WindowMinMaxButtonsHint)
            self.setFont(QFont('Arial', 10))
            
            grid = QGridLayout()
            logger.debug("__init__(data_list=%s,header=%s): grid → %s", data_list, header, grid, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): grid → %s", self, data_list, header, grid, extra={"event.action": "__init__", "logrite.data_list": data_list})
            grid.setSpacing(20)
            
            table_model = MyTableModel(self, data_list, header)
            logger.debug("__init__(data_list=%s,header=%s): table_model → %s", data_list, header, table_model, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): table_model → %s", self, data_list, header, table_model, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(data_list=%s,header=%s): font → %s", data_list, header, font, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): font → %s", self, data_list, header, font, extra={"event.action": "__init__", "logrite.data_list": data_list})
            table_view = QTableView()
            logger.debug("__init__(self=%s,data_list=%s,header=%s): table_view → %s", self, data_list, header, table_view, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(data_list=%s,header=%s): table_view → %s", data_list, header, table_view, extra={"event.action": "__init__", "logrite.data_list": data_list})
            table_view.setModel(table_model)
            font = QFont("Arial", 10)
            table_view.setFont(font)
            table_view.hideColumn(31)
            table_view.hideColumn(32)
            table_view.hideColumn(33)
            table_view.hideColumn(34)
            table_view.hideColumn(35)
            table_view.hideColumn(36)
            table_view.hideColumn(37)
            table_view.resizeColumnsToContents()
            table_view.setSelectionBehavior(QTableView.SelectRows)
            table_view.clicked.connect(showSelection)
            grid.addWidget(table_view, 0, 0, 1, 16)
            
            lbl = QLabel()
            logger.debug("__init__(data_list=%s,header=%s): lbl → %s", data_list, header, lbl, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): lbl → %s", self, data_list, header, lbl, extra={"event.action": "__init__", "logrite.data_list": data_list})
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            logger.debug("__init__(self=%s,data_list=%s,header=%s): pixmap → %s", self, data_list, header, pixmap, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(data_list=%s,header=%s): pixmap → %s", data_list, header, pixmap, extra={"event.action": "__init__", "logrite.data_list": data_list})
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl, 1, 0, 1, 2)
       
            logo = QLabel()
            logger.debug("__init__(data_list=%s,header=%s): logo → %s", data_list, header, logo, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): logo → %s", self, data_list, header, logo, extra={"event.action": "__init__", "logrite.data_list": data_list})
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 1, 15, 1, 1, Qt.AlignRight)
            
            freshBtn = QPushButton('Verversen')
            logger.debug("__init__(data_list=%s,header=%s): freshBtn → %s", data_list, header, freshBtn, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): freshBtn → %s", self, data_list, header, freshBtn, extra={"event.action": "__init__", "logrite.data_list": data_list})
            freshBtn.clicked.connect(lambda: refresh(keuze, m_email, self))

            freshBtn.setFont(QFont("Arial",10))
            freshBtn.setFixedWidth(100) 
            freshBtn.setStyleSheet("color: black;  background-color: gainsboro")
   
            grid.addWidget(freshBtn, 1, 14, 1, 1, Qt.AlignRight)
        
            sluitBtn = QPushButton('Sluiten')
            logger.debug("__init__(data_list=%s,header=%s): sluitBtn → %s", data_list, header, sluitBtn, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): sluitBtn → %s", self, data_list, header, sluitBtn, extra={"event.action": "__init__", "logrite.data_list": data_list})
            sluitBtn.clicked.connect(self.close)

            sluitBtn.setFont(QFont("Arial",10))
            sluitBtn.setFixedWidth(100) 
            sluitBtn.setStyleSheet("color: black;  background-color: gainsboro") 
            
            grid.addWidget(sluitBtn, 1, 13, 1, 1, Qt.AlignRight)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 1, 0, 1, 16, Qt.AlignCenter)
            
            self.setLayout(grid)
            self.setGeometry(50, 50, 1800, 900)
            self.setLayout(grid)
            logger.debug("<<< Exiting __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})

    class MyTableModel(QAbstractTableModel):
        def __init__(self, parent, mylist, header, *args):
            logger.warning(">>> Entering __init__(parent=%s,mylist=%s,header=%s)", parent, mylist, header, extra={"event.action": "__init__", "logrite.mylist": mylist})
            logger.debug("__init__(self=%s,parent=%s,mylist=%s,header=%s): self.mylist → %s", self, parent, mylist, header, self.mylist, extra={"event.action": "__init__", "logrite.mylist": mylist})
            logger.debug("__init__(self=%s,parent=%s,mylist=%s,header=%s): self.header → %s", self, parent, mylist, header, self.header, extra={"event.action": "__init__", "logrite.mylist": mylist})
            QAbstractTableModel.__init__(self, parent, *args)
            logger.debug("<<< Exiting __init__(parent=%s,mylist=%s,header=%s)", parent, mylist, header, extra={"event.action": "__init__", "logrite.mylist": mylist})
            self.mylist = mylist
            logger.warning(">>> Entering __init__()", extra={"event.action": "__init__"})
            logger.debug("__init__(): grid → %s", grid, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): grid → %s", self, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Omschrijving → %s", self.Omschrijving, extra={"event.action": "__init__"})
            logger.debug("__init__(): q1Edit → %s", q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q1Edit → %s", self, q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): reg_ex → %s", reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): reg_ex → %s", self, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(): input_validator → %s", input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): input_validator → %s", self, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Prijs → %s", self.Prijs, extra={"event.action": "__init__"})
            logger.debug("__init__(): q2Edit → %s", q2Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q2Edit → %s", self, q2Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Eenheid → %s", self.Eenheid, extra={"event.action": "__init__"})
            logger.debug("__init__(): q3Edit → %s", q3Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q3Edit → %s", self, q3Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Materialen → %s", self.Materialen, extra={"event.action": "__init__"})
            logger.debug("__init__(): q4Edit → %s", q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q4Edit → %s", self, q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Lonen → %s", self.Lonen, extra={"event.action": "__init__"})
            logger.debug("__init__(): q5Edit → %s", q5Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q5Edit → %s", self, q5Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Diensten → %s", self.Diensten, extra={"event.action": "__init__"})
            logger.debug("__init__(): q6Edit → %s", q6Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q6Edit → %s", self, q6Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): q7Edit → %s", q7Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q7Edit → %s", self, q7Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Inhuur → %s", self.Inhuur, extra={"event.action": "__init__"})
            logger.debug("__init__(): q8Edit → %s", q8Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q8Edit → %s", self, q8Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Construktieuren → %s", self.Construktieuren, extra={"event.action": "__init__"})
            logger.debug("__init__(): q9Edit → %s", q9Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q9Edit → %s", self, q9Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Montageuren → %s", self.Montageuren, extra={"event.action": "__init__"})
            logger.debug("__init__(): q10Edit → %s", q10Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q10Edit → %s", self, q10Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Retourlasuren → %s", self.Retourlasuren, extra={"event.action": "__init__"})
            logger.debug("__init__(): q11Edit → %s", q11Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q11Edit → %s", self, q11Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.BFIuren → %s", self.BFIuren, extra={"event.action": "__init__"})
            logger.debug("__init__(): q12Edit → %s", q12Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q12Edit → %s", self, q12Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Telecomuren → %s", self.Telecomuren, extra={"event.action": "__init__"})
            logger.debug("__init__(): q29Edit → %s", q29Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q29Edit → %s", self, q29Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Voedinguren → %s", self.Voedinguren, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q13Edit → %s", self, q13Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): q13Edit → %s", q13Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Bvluren → %s", self.Bvluren, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q14Edit → %s", self, q14Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): q14Edit → %s", q14Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Spoorleguren → %s", self.Spoorleguren, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q15Edit → %s", self, q15Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): q15Edit → %s", q15Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Spoorlasuren → %s", self.Spoorlasuren, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q16Edit → %s", self, q16Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): q16Edit → %s", q16Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Inhuururen → %s", self.Inhuururen, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q17Edit → %s", self, q17Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): q17Edit → %s", q17Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Sleuvengraver → %s", self.Sleuvengraver, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q18Edit → %s", self, q18Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): q18Edit → %s", q18Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Persapparaat → %s", self.Persapparaat, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q19Edit → %s", self, q19Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): q19Edit → %s", q19Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Atlaskraan → %s", self.Atlaskraan, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q20Edit → %s", self, q20Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): q20Edit → %s", q20Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Kraan_groot → %s", self.Kraan_groot, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q21Edit → %s", self, q21Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): q21Edit → %s", q21Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Mainliner → %s", self.Mainliner, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q22Edit → %s", self, q22Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): q22Edit → %s", q22Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Hormachine → %s", self.Hormachine, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q23Edit → %s", self, q23Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): q23Edit → %s", q23Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Wagon → %s", self.Wagon, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q24Edit → %s", self, q24Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): q24Edit → %s", q24Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Locomotor → %s", self.Locomotor, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q25Edit → %s", self, q25Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): q25Edit → %s", q25Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Locomotief → %s", self.Locomotief, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q26Edit → %s", self, q26Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): q26Edit → %s", q26Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Stormobiel → %s", self.Stormobiel, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q27Edit → %s", self, q27Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): q27Edit → %s", q27Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Montagewagen → %s", self.Montagewagen, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q28Edit → %s", self, q28Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): q28Edit → %s", q28Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Robeltrein → %s", self.Robeltrein, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q30Edit → %s", self, q30Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): q30Edit → %s", q30Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl1 → %s", self, lbl1, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl1 → %s", lbl1, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl2 → %s", self, lbl2, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl2 → %s", lbl2, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl3 → %s", self, lbl3, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl3 → %s", lbl3, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl4 → %s", self, lbl4, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl4 → %s", lbl4, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl5 → %s", self, lbl5, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl5 → %s", lbl5, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl6 → %s", self, lbl6, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl6 → %s", lbl6, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl7 → %s", self, lbl7, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl7 → %s", lbl7, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl8 → %s", self, lbl8, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl8 → %s", lbl8, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl9 → %s", self, lbl9, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl9 → %s", lbl9, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl10 → %s", self, lbl10, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl10 → %s", lbl10, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl20 → %s", lbl20, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl20 → %s", self, lbl20, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl21 → %s", lbl21, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl21 → %s", self, lbl21, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl22 → %s", lbl22, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl22 → %s", self, lbl22, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl23 → %s", lbl23, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl23 → %s", self, lbl23, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl24 → %s", lbl24, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl24 → %s", self, lbl24, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl25 → %s", lbl25, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl25 → %s", self, lbl25, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl26 → %s", lbl26, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl26 → %s", self, lbl26, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl27 → %s", lbl27, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl27 → %s", self, lbl27, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl28 → %s", lbl28, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl28 → %s", self, lbl28, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl29 → %s", lbl29, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl29 → %s", self, lbl29, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl30 → %s", lbl30, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl30 → %s", self, lbl30, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl31 → %s", lbl31, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl31 → %s", self, lbl31, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl19 → %s", lbl19, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl19 → %s", self, lbl19, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl11 → %s", lbl11, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl11 → %s", self, lbl11, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl12 → %s", lbl12, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl12 → %s", self, lbl12, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl13 → %s", lbl13, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl13 → %s", self, lbl13, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl14 → %s", lbl14, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl14 → %s", self, lbl14, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl15 → %s", lbl15, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl15 → %s", self, lbl15, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl16 → %s", lbl16, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl16 → %s", self, lbl16, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl17 → %s", lbl17, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl17 → %s", self, lbl17, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl18 → %s", lbl18, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl18 → %s", self, lbl18, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl → %s", lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl → %s", self, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(): pixmap → %s", pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): pixmap → %s", self, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(): logo → %s", logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): logo → %s", self, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(): applyBtn → %s", applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): applyBtn → %s", self, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(): closeBtn → %s", closeBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): closeBtn → %s", self, closeBtn, extra={"event.action": "__init__"})
            logger.debug("<<< Exiting __init__()", extra={"event.action": "__init__"})
            self.header = header
        def rowCount(self, parent):
            logger.warning(">>> Entering rowCount(parent=%s)", parent, extra={"event.action": "rowCount"})
            return len(self.mylist)
        def columnCount(self, parent):
            logger.warning(">>> Entering columnCount(parent=%s)", parent, extra={"event.action": "columnCount"})
            return len(self.mylist[0])
        def data(self, index, role):
            logger.warning(">>> Entering data(index=%s,role=%s)", index, role, extra={"event.action": "data", "logrite.index": index, "logrite.role": role})
            veld = self.mylist[index.row()][index.column()]
            logger.debug("data(index=%s,role=%s): veld → %s", index, role, veld, extra={"event.action": "data", "logrite.index": index, "logrite.role": role})
            logger.debug("data(self=%s,index=%s,role=%s): veld → %s", self, index, role, veld, extra={"event.action": "data", "logrite.index": index, "logrite.role": role})
            if not index.isValid():
                return None
            elif role == Qt.TextAlignmentRole and (type(veld) == float or type(veld) == int):
                return Qt.AlignRight | Qt.AlignVCenter
            elif role != Qt.DisplayRole:
                return None
            if type(veld) == float:
                return '{:12.2f}'.format(veld)
            else:
                logger.debug("<<< Exiting data(index=%s,role=%s)", index, role, extra={"event.action": "data", "logrite.index": index, "logrite.role": role})
                return veld
        def headerData(self, col, orientation, role):
            logger.warning(">>> Entering headerData(col=%s,orientation=%s,role=%s)", col, orientation, role, extra={"event.action": "headerData", "logrite.col": col, "logrite.orientation": orientation, "logrite.role": role})
            if orientation == Qt.Horizontal and role == Qt.DisplayRole:
                return self.header[col]
            logger.debug("<<< Exiting headerData(col=%s,orientation=%s,role=%s)", col, orientation, role, extra={"event.action": "headerData", "logrite.col": col, "logrite.orientation": orientation, "logrite.role": role})
            return None
             
    header = ['Clusternr', 'Omschrijving', 'Prijs', 'Eenheid', 'Materialen', 'Lonen',\
              'Diensten', 'Materiëel', 'Inhuur', 'uren_constr', 'uren_mont','uren_retourlas',\
              'uren_bfi', 'uren_voeding', 'uren_bvl', 'uren_spoorleg', 'uren_spoorlas',\
              'uren_inhuur', 'Sleuvengraver', 'Persapparaat', 'Atlaskraan',\
              'Kraan_groot', 'Mainliner', 'Hormachine', 'Wagon', 'Locomotor',\
              'Locomotief', 'Montagewagen', 'Stormobiel', 'uren_telecom', 'Robeltrein',\
              '', '', '', '', '', '', '']
    
    metadata = MetaData()
    clusters = Table('clusters', metadata,
        Column('clusterID', String, primary_key=True),
        Column('omschrijving', String),
        Column('prijs', Float),
        Column('eenheid', String),
        Column('materialen', Float),
        Column('lonen', Float),
        Column('diensten', Float),
        Column('materieel', Float),
        Column('inhuur', Float),
        Column('uren_constr', Float),
        Column('uren_mont', Float),
        Column('uren_retourlas', Float),
        Column('uren_bfi', Float),
        Column('uren_voeding', Float),
        Column('uren_bvl', Float),
        Column('uren_spoorleg', Float),
        Column('uren_spoorlas', Float),
        Column('uren_inhuur', Float),
        Column('sleuvengraver', Float),
        Column('persapparaat', Float),
        Column('atlaskraan', Float),
        Column('kraan_groot', Float),
        Column('mainliner', Float),
        Column('hormachine', Float),
        Column('wagon', Float),
        Column('locomotor', Float),
        Column('locomotief', Float),
        Column('montagewagen', Float),
        Column('stormobiel', Float),
        Column('uren_telecom', Float),
        Column('robeltrein', Float),
        Column('leiding', Float),
        Column('huisvesting', Float),
        Column('kabelwerk', Float),
        Column('grondverzet', Float),
        Column('betonwerk', Float),
        Column('vervoer', Float),
        Column('overig', Float))
       
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
        
    sel = select([clusters]).where(clusters.c.clusterID.ilike(keuze+'%'))\
                              .order_by(clusters.c.clusterID)

    if con.execute(sel).fetchone():
        rp = con.execute(sel)
    else:
        geenRecord()
        zoeken(m_email)
      
    data_list=[]
    for row in rp:
        data_list += [(row)]

    def showSelection(idx):
        logger.warning(">>> Entering showSelection(idx=%s)", idx, extra={"event.action": "showSelection", "logrite.idx": idx})
        clusternr = idx.data()
        logger.debug("showSelection(idx=%s): clusternr → %s", idx, clusternr, extra={"event.action": "showSelection", "logrite.idx": idx})
        if idx.column() == 0:
            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            logger.debug("showSelection(idx=%s): engine → %s", idx, engine, extra={"event.action": "showSelection", "logrite.idx": idx})
            con = engine.connect()
            selcl = select([clusters]).where(clusters.c.clusterID == clusternr)
            logger.debug("showSelection(idx=%s): con → %s", idx, con, extra={"event.action": "showSelection", "logrite.idx": idx})
            rpsel = con.execute(selcl).first()
            
            logger.debug("showSelection(idx=%s): selcl → %s", idx, selcl, extra={"event.action": "showSelection", "logrite.idx": idx})
            logger.debug("showSelection(idx=%s): rpsel → %s", idx, rpsel, extra={"event.action": "showSelection", "logrite.idx": idx})
            class MainWindow(QDialog):
                def __init__(self):
                    logger.debug("<<< Exiting showSelection(idx=%s)", idx, extra={"event.action": "showSelection", "logrite.idx": idx})
                    QDialog.__init__(self)
                    
                    grid = QGridLayout()
                    grid.setSpacing(20)
                    self.setWindowTitle("Wijzigen Cluster")
                    self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
                    
                    self.setFont(QFont('Arial', 10))   
                    
                    self.Omschrijving = QLabel()
                    q1Edit = QLineEdit(rpsel[1])
                    q1Edit.setFont(QFont("Arial",10))
                    q1Edit.textChanged.connect(self.q1Changed) 
                    reg_ex = QRegExp("^.{0,49}$")
                    input_validator = QRegExpValidator(reg_ex, q1Edit)
                    q1Edit.setValidator(input_validator)
                                    
                    self.Prijs = QLabel()
                    q2Edit = QLineEdit(('{:12.2f}'.format(rpsel[2])))
                    q2Edit.setFixedWidth(150)
                    q2Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q2Edit.setAlignment(Qt.AlignRight)
                    q2Edit.setDisabled(True)
                     
                    self.Eenheid = QLabel()
                    q3Edit = QLineEdit(str(rpsel[3]))
                    q3Edit.setFixedWidth(150)
                    q3Edit.setFont(QFont("Arial",10))
                    q3Edit.textChanged.connect(self.q3Changed) 
                    reg_ex = QRegExp("^.{0,10}$")
                    input_validator = QRegExpValidator(reg_ex, q3Edit)
                    q3Edit.setValidator(input_validator)
                    
                    self.Materialen = QLabel()
                    q4Edit = QLineEdit('{:12.2f}'.format(rpsel[4]))
                    q4Edit.setFixedWidth(150)
                    q4Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q4Edit.setAlignment(Qt.AlignRight)
                    q4Edit.setDisabled(True)
                    
                    self.Lonen = QLabel()
                    q5Edit = QLineEdit('{:12.2f}'.format(rpsel[5]))
                    q5Edit.setFixedWidth(150)
                    q5Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q5Edit.setAlignment(Qt.AlignRight)
                    q5Edit.setDisabled(True)
                    
                    self.Diensten = QLabel()
                    q6Edit = QLineEdit('{:12.2f}'.format(rpsel[6]))
                    q6Edit.setFixedWidth(150)
                    q6Edit.setAlignment(Qt.AlignRight)
                    q6Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q6Edit.setDisabled(True)
                    
                    self.Materiëel = QLabel()
                    q7Edit = QLineEdit('{:12.2f}'.format(rpsel[7]))
                    q7Edit.setFixedWidth(150)
                    q7Edit.setAlignment(Qt.AlignRight)
                    q7Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q7Edit.setValidator(input_validator)
                    q7Edit.setDisabled(True)
                    
                    self.Inhuur = QLabel()
                    q8Edit = QLineEdit('{:12.2f}'.format(rpsel[8]))
                    q8Edit.setFixedWidth(150)
                    q8Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q8Edit.setAlignment(Qt.AlignRight)
                    q8Edit.setDisabled(True)
                                   
                    self.Construktieuren = QLabel()
                    q9Edit = QLineEdit(str(round(float(rpsel[9]),2)))
                    q9Edit.setFixedWidth(150)
                    q9Edit.setFont(QFont("Arial",10))
                    q9Edit.setAlignment(Qt.AlignRight)
                    q9Edit.textChanged.connect(self.q9Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q9Edit)
                    q9Edit.setValidator(input_validator)
                    
                    self.Montageuren = QLabel()
                    q10Edit = QLineEdit(str(round(float(rpsel[10]),2)))
                    q10Edit.setFixedWidth(150)
                    q10Edit.setAlignment(Qt.AlignRight)
                    q10Edit.setFont(QFont("Arial",10))
                    q10Edit.textChanged.connect(self.q10Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q10Edit)
                    q10Edit.setValidator(input_validator)
                    
                    self.Retourlasuren = QLabel()
                    q11Edit = QLineEdit(str(round(float(rpsel[11]),2)))
                    q11Edit.setFixedWidth(150)
                    q11Edit.setAlignment(Qt.AlignRight)
                    q11Edit.setFont(QFont("Arial",10))
                    q11Edit.textChanged.connect(self.q11Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q11Edit)
                    q11Edit.setValidator(input_validator)
                    
                    self.BFIuren = QLabel()
                    q12Edit = QLineEdit(str(round(float(rpsel[12]),2)))
                    q12Edit.setFixedWidth(150)
                    q12Edit.setAlignment(Qt.AlignRight)
                    q12Edit.setFont(QFont("Arial",10))
                    q12Edit.textChanged.connect(self.q12Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q12Edit)
                    q12Edit.setValidator(input_validator)
                    
                    self.Telecomuren = QLabel()
                    q29Edit = QLineEdit(str(round(float(rpsel[29]),2)))
                    q29Edit.setFixedWidth(150)
                    q29Edit.setAlignment(Qt.AlignRight)
                    q29Edit.setFont(QFont("Arial",10))
                    q29Edit.textChanged.connect(self.q29Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q29Edit)
                    q29Edit.setValidator(input_validator)      
                         
                    self.Voedinguren = QLabel()
                    q13Edit = QLineEdit(str(round(float(rpsel[13]),2)))
                    q13Edit.setFixedWidth(150)
                    q13Edit.setAlignment(Qt.AlignRight)
                    q13Edit.setFont(QFont("Arial",10))
                    q13Edit.textChanged.connect(self.q13Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q13Edit)
                    q13Edit.setValidator(input_validator)
                    
                    self.Bvluren = QLabel()
                    q14Edit = QLineEdit(str(round(float(rpsel[14]),2)))
                    q14Edit.setFixedWidth(150)
                    q14Edit.setFont(QFont("Arial",10))
                    q14Edit.setAlignment(Qt.AlignRight)
                    q14Edit.textChanged.connect(self.q14Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q14Edit)
                    q14Edit.setValidator(input_validator)
                       
                    self.Spoorleguren = QLabel()
                    q15Edit = QLineEdit(str(round(float(rpsel[15]),2)))
                    q15Edit.setFixedWidth(150)
                    q15Edit.setAlignment(Qt.AlignRight)
                    q15Edit.setFont(QFont("Arial",10))
                    q15Edit.textChanged.connect(self.q15Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q15Edit)
                    q15Edit.setValidator(input_validator)
                    
                    self.Spoorlasuren = QLabel()
                    q16Edit = QLineEdit(str(round(float(rpsel[16]),2)))
                    q16Edit.setFixedWidth(150)
                    q16Edit.setAlignment(Qt.AlignRight)
                    q16Edit.setFont(QFont("Arial",10))
                    q16Edit.textChanged.connect(self.q16Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q16Edit)
                    q16Edit.setValidator(input_validator)
                    
                    self.Inhuururen = QLabel()
                    q17Edit = QLineEdit(str(round(float(rpsel[17]),2)))
                    q17Edit.setFixedWidth(150)
                    q17Edit.setAlignment(Qt.AlignRight)
                    q17Edit.setFont(QFont("Arial",10))
                    q17Edit.textChanged.connect(self.q17Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q17Edit)
                    q17Edit.setValidator(input_validator)
                       
                    self.Sleuvengraver = QLabel()
                    q18Edit = QLineEdit(str(round(float(rpsel[18]),2)))
                    q18Edit.setFixedWidth(150)
                    q18Edit.setAlignment(Qt.AlignRight)
                    q18Edit.setFont(QFont("Arial",10))
                    q18Edit.textChanged.connect(self.q18Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q18Edit)
                    q18Edit.setValidator(input_validator)
                            
                    self.Persapparaat = QLabel()
                    q19Edit = QLineEdit(str(round(float(rpsel[19]),2)))
                    q19Edit.setFixedWidth(150)
                    q19Edit.setAlignment(Qt.AlignRight)
                    q19Edit.setFont(QFont("Arial",10))
                    q19Edit.textChanged.connect(self.q19Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q19Edit)
                    q19Edit.setValidator(input_validator)
                    
                    self.Atlaskraan = QLabel()
                    q20Edit = QLineEdit(str(round(float(rpsel[20]),2)))
                    q20Edit.setFixedWidth(150)
                    q20Edit.setFont(QFont("Arial",10))
                    q20Edit.setAlignment(Qt.AlignRight)
                    q20Edit.textChanged.connect(self.q20Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q20Edit)
                    q20Edit.setValidator(input_validator)
                    
                    self.Kraan_groot = QLabel()
                    q21Edit = QLineEdit(str(round(float(rpsel[21]),2)))
                    q21Edit.setFixedWidth(150)
                    q21Edit.setFont(QFont("Arial",10))
                    q21Edit.setAlignment(Qt.AlignRight)
                    q21Edit.textChanged.connect(self.q21Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q21Edit)
                    q21Edit.setValidator(input_validator)
                    
                    self.Mainliner = QLabel()
                    q22Edit = QLineEdit(str(round(float(rpsel[22]),2)))
                    q22Edit.setFixedWidth(150)
                    q22Edit.setFont(QFont("Arial",10))
                    q22Edit.setAlignment(Qt.AlignRight)
                    q22Edit.textChanged.connect(self.q22Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q22Edit)
                    q22Edit.setValidator(input_validator)
                    
                    self.Hormachine = QLabel()
                    q23Edit = QLineEdit(str(round(float(rpsel[23]),2)))
                    q23Edit.setFixedWidth(150)
                    q23Edit.setAlignment(Qt.AlignRight)
                    q23Edit.setFont(QFont("Arial",10))
                    q23Edit.textChanged.connect(self.q23Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q23Edit)
                    q23Edit.setValidator(input_validator)
                    
                    self.Wagon = QLabel()
                    q24Edit = QLineEdit(str(round(float(rpsel[24]),2)))
                    q24Edit.setAlignment(Qt.AlignRight)
                    q24Edit.setFixedWidth(150)
                    q24Edit.setFont(QFont("Arial",10))
                    q24Edit.textChanged.connect(self.q24Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q24Edit)
                    q24Edit.setValidator(input_validator)
                    
                    self.Locomotor = QLabel()
                    q25Edit = QLineEdit(str(round(float(rpsel[25]),2)))
                    q25Edit.setFixedWidth(150)
                    q25Edit.setAlignment(Qt.AlignRight)
                    q25Edit.setFont(QFont("Arial",10))
                    q25Edit.textChanged.connect(self.q25Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q25Edit)
                    q25Edit.setValidator(input_validator)
        
                    self.Locomotief = QLabel()
                    q26Edit = QLineEdit(str(round(float(rpsel[26]),2)))
                    q26Edit.setFixedWidth(150)
                    q26Edit.setAlignment(Qt.AlignRight)
                    q26Edit.setFont(QFont("Arial",10))
                    q26Edit.textChanged.connect(self.q26Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q26Edit)
                    q26Edit.setValidator(input_validator)
                    
                    self.Stormobiel = QLabel()
                    q27Edit = QLineEdit(str(round(float(rpsel[27]),2)))
                    q27Edit.setFixedWidth(150)
                    q27Edit.setAlignment(Qt.AlignRight)
                    q27Edit.setFont(QFont("Arial",10))
                    q27Edit.textChanged.connect(self.q27Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q27Edit)
                    q27Edit.setValidator(input_validator)
                    
                    self.Montagewagen = QLabel()
                    q28Edit = QLineEdit(str(round(float(rpsel[28]),2)))
                    q28Edit.setFixedWidth(150)
                    q28Edit.setAlignment(Qt.AlignRight)
                    q28Edit.setFont(QFont("Arial",10))
                    q28Edit.textChanged.connect(self.q28Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q28Edit)
                    q28Edit.setValidator(input_validator)
                    
                    self.Robeltrein = QLabel()
                    q30Edit = QLineEdit(str(round(float(rpsel[30]),2)))
                    q30Edit.setFixedWidth(150)
                    q30Edit.setFont(QFont("Arial",10))
                    q30Edit.setAlignment(Qt.AlignRight)
                    q30Edit.textChanged.connect(self.q30Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q30Edit)
                    q30Edit.setValidator(input_validator)
                    
                    grid = QGridLayout()
                    grid.setSpacing(10)
                    
                    lbl1 = QLabel('Clusternummer')  
                    lbl1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl1, 1, 0)
                    
                    lbl2 = QLabel(clusternr)
                    grid.addWidget(lbl2, 1, 1)
                           
                    lbl3 = QLabel('Omschrijving')  
                    lbl3.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl3, 2, 0)
                    grid.addWidget(q1Edit, 2, 1, 1, 3) # RowSpan 1 ,ColumnSpan 3
                                                         
                    lbl4 = QLabel('Prijs')  
                    lbl4.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl4, 3, 0)
                    grid.addWidget(q2Edit, 3, 1)
                    
                    lbl5 = QLabel('Eenheid')  
                    lbl5.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl5, 4, 0)
                    grid.addWidget(q3Edit, 4, 1)
                    
                    lbl6 = QLabel('Materialen')  
                    lbl6.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl6, 5, 0)
                    grid.addWidget(q4Edit, 5, 1)
                    
                    lbl7 = QLabel('Lonen')  
                    lbl7.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl7, 6, 0)
                    grid.addWidget(q5Edit, 6, 1)
                    
                    lbl8 = QLabel('Diensten')  
                    lbl8.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl8, 7, 0)
                    grid.addWidget(q6Edit, 7, 1)
                    
                    lbl9 = QLabel('Materiëel')  
                    lbl9.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl9, 8, 0)
                    grid.addWidget(q7Edit, 8, 1)
                    
                    lbl10 = QLabel('Inhuur')  
                    lbl10.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl10, 9, 0)
                    grid.addWidget(q8Edit, 9, 1)
                    
                    lbl20 = QLabel('Sleuvengraven-uren')  
                    lbl20.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl20, 10, 0)
                    grid.addWidget(q18Edit, 10, 1)
                      
                    lbl21 = QLabel('Persapparaat-uren')  
                    lbl21.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl21, 11, 0)
                    grid.addWidget(q19Edit, 11, 1)
                    
                    lbl22 = QLabel('Atlaskraan-uren')  
                    lbl22.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl22, 12, 0)
                    grid.addWidget(q20Edit, 12, 1)
                    
                    lbl23 = QLabel('Kraan_groot-uren')  
                    lbl23.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl23, 13, 0)
                    grid.addWidget(q21Edit, 13, 1)
                    
                    lbl24 = QLabel('Mainliner-uren')  
                    lbl24.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl24, 14, 0)
                    grid.addWidget(q22Edit, 14, 1)
                    
                    lbl25 = QLabel('Hormachine-uren')  
                    lbl25.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl25, 15, 0)
                    grid.addWidget(q23Edit, 15, 1)
                    
                    lbl26 = QLabel('Wagon-uren')  
                    lbl26.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl26, 16, 0)
                    grid.addWidget(q24Edit, 16, 1)
                    
                    lbl27 = QLabel('Locomotor-uren')  
                    lbl27.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl27, 3, 2)
                    grid.addWidget(q25Edit, 3, 3)
                    
                    lbl28 = QLabel('Locomotief-uren')  
                    lbl28.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl28, 4, 2)
                    grid.addWidget(q26Edit, 4, 3)
                    
                    lbl29 = QLabel('Stormobiel-uren')  
                    lbl29.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl29, 5, 2)
                    grid.addWidget(q27Edit, 5, 3)
                    
                    lbl30 = QLabel('Montagewagen-uren')  
                    lbl30.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl30, 6, 2)
                    grid.addWidget(q28Edit, 6, 3)
                    
                    lbl31 = QLabel('Robeltrein-uren')  
                    lbl31.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl31, 7, 2)
                    grid.addWidget(q30Edit, 7, 3)
                    
                    lbl19 = QLabel('Inhuur-uren')  
                    lbl19.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl19, 8, 2)
                    grid.addWidget(q17Edit, 8, 3)      
                    
                    lbl11 = QLabel('Construktie-uren')  
                    lbl11.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl11, 9, 2)
                    grid.addWidget(q9Edit, 9, 3)
                        
                    lbl12 = QLabel('Montage-uren')  
                    lbl12.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl12, 10, 2)
                    grid.addWidget(q10Edit, 10, 3)
                    
                    lbl13 = QLabel('Retourlas-uren')  
                    lbl13.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl13, 11, 2)
                    grid.addWidget(q11Edit, 11, 3)
                    
                    lbl14 = QLabel('BFI-uren')  
                    lbl14.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl14, 12, 2)
                    grid.addWidget(q12Edit, 12, 3)
                    
                    lbl19 = QLabel('Telecom-uren')  
                    lbl19.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl19, 13, 2)
                    grid.addWidget(q29Edit, 13, 3)
                                                              
                    lbl15 = QLabel('Voeding-uren')  
                    lbl15.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl15, 14, 2)
                    grid.addWidget(q13Edit, 14, 3)
                 
                    lbl16 = QLabel('Bovenleiding-uren')
                    lbl16.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl16, 15, 2)
                    grid.addWidget(q14Edit, 15, 3)
                    
                    lbl17 = QLabel('Spoorleg-uren')  
                    lbl17.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl17, 16, 2)
                    grid.addWidget(q15Edit, 16, 3)
                    
                    lbl18 = QLabel('Spoorlas-uren')  
                    lbl18.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl18, 17, 2)
                    grid.addWidget(q16Edit, 17, 3)

                    lbl = QLabel()
                    pixmap = QPixmap('./images/logos/verbinding.jpg')
                    lbl.setPixmap(pixmap)
                    grid.addWidget(lbl, 0, 0, 1, 1, Qt.AlignRight)
                                     
                    logo = QLabel()
                    pixmap = QPixmap('./images/logos/logo.jpg')
                    logo.setPixmap(pixmap)
                    grid.addWidget(logo , 0, 3, 1 , 1, Qt.AlignRight)
                    
                    grid.addWidget(QLabel('Wijzigen Cluster'), 0, 1, 1, 2, Qt.AlignCenter)
                                                    
                    grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 22, 1, 1, 3)
                      
                    self.setLayout(grid)
                    self.setGeometry(400, 50, 150, 150)
            
                    applyBtn = QPushButton('Wijzig')
                    applyBtn.clicked.connect(self.accept)
            
                    grid.addWidget(applyBtn, 21, 3, 1, 1, Qt.AlignRight)
                    applyBtn.setFont(QFont("Arial",10))
                    applyBtn.setFixedWidth(100)
                    applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
                    
                    closeBtn = QPushButton('Sluiten')
                    closeBtn.clicked.connect(self.close)
            
                    grid.addWidget(closeBtn, 21, 2, 1, 2, Qt.AlignCenter)
                    closeBtn.setFont(QFont("Arial",10))
                    closeBtn.setFixedWidth(100)
                    closeBtn.setStyleSheet("color: black;  background-color: gainsboro")
                                             
                def q1Changed(self,text):
                    logger.warning(">>> Entering q1Changed(text=%s)", text, extra={"event.action": "q1Changed", "logrite.text": text})
                    self.Omschrijving.setText(text)
                    logger.debug("<<< Exiting q1Changed(text=%s)", text, extra={"event.action": "q1Changed", "logrite.text": text})
            
                def q3Changed(self,text):
                    logger.warning(">>> Entering q3Changed(text=%s)", text, extra={"event.action": "q3Changed", "logrite.text": text})
                    self.Eenheid.setText(text)
                    logger.debug("<<< Exiting q3Changed(text=%s)", text, extra={"event.action": "q3Changed", "logrite.text": text})
                             
                def q9Changed(self,text):
                    logger.warning(">>> Entering q9Changed(text=%s)", text, extra={"event.action": "q9Changed", "logrite.text": text})
                    self.Construktieuren.setText(text)
                    logger.debug("<<< Exiting q9Changed(text=%s)", text, extra={"event.action": "q9Changed", "logrite.text": text})
                    
                def q10Changed(self,text):
                    logger.warning(">>> Entering q10Changed(text=%s)", text, extra={"event.action": "q10Changed", "logrite.text": text})
                    self.Montageuren.setText(text)
                    logger.debug("<<< Exiting q10Changed(text=%s)", text, extra={"event.action": "q10Changed", "logrite.text": text})
                       
                def q11Changed(self,text):
                    logger.warning(">>> Entering q11Changed(text=%s)", text, extra={"event.action": "q11Changed", "logrite.text": text})
                    self.Retourlasuren.setText(text)
                    logger.debug("<<< Exiting q11Changed(text=%s)", text, extra={"event.action": "q11Changed", "logrite.text": text})
                    
                def q12Changed(self,text):
                    logger.warning(">>> Entering q12Changed(text=%s)", text, extra={"event.action": "q12Changed", "logrite.text": text})
                    self.BFIuren.setText(text)
                    logger.debug("<<< Exiting q12Changed(text=%s)", text, extra={"event.action": "q12Changed", "logrite.text": text})
                    
                def q13Changed(self,text):
                    logger.warning(">>> Entering q13Changed(text=%s)", text, extra={"event.action": "q13Changed", "logrite.text": text})
                    self.Voedinguren.setText(text)
                    logger.debug("<<< Exiting q13Changed(text=%s)", text, extra={"event.action": "q13Changed", "logrite.text": text})
                    
                def q14Changed(self,text):
                    logger.warning(">>> Entering q14Changed(text=%s)", text, extra={"event.action": "q14Changed", "logrite.text": text})
                    self.Bvluren.setText(text)
                    logger.debug("<<< Exiting q14Changed(text=%s)", text, extra={"event.action": "q14Changed", "logrite.text": text})
                    
                def q15Changed(self,text):
                    logger.warning(">>> Entering q15Changed(text=%s)", text, extra={"event.action": "q15Changed", "logrite.text": text})
                    self.Spoorleguren.setText(text)
                    logger.debug("<<< Exiting q15Changed(text=%s)", text, extra={"event.action": "q15Changed", "logrite.text": text})
                    
                def q16Changed(self,text):
                    logger.warning(">>> Entering q16Changed(text=%s)", text, extra={"event.action": "q16Changed", "logrite.text": text})
                    self.Spoorlasuren.setText(text)
                    logger.debug("<<< Exiting q16Changed(text=%s)", text, extra={"event.action": "q16Changed", "logrite.text": text})
                    
                def q17Changed(self,text):
                    logger.warning(">>> Entering q17Changed(text=%s)", text, extra={"event.action": "q17Changed", "logrite.text": text})
                    self.Inhuururen.setText(text)
                    logger.debug("<<< Exiting q17Changed(text=%s)", text, extra={"event.action": "q17Changed", "logrite.text": text})
                    
                def q18Changed(self,text):
                    logger.warning(">>> Entering q18Changed(text=%s)", text, extra={"event.action": "q18Changed", "logrite.text": text})
                    self.Sleuvengraver.setText(text)
                    logger.debug("<<< Exiting q18Changed(text=%s)", text, extra={"event.action": "q18Changed", "logrite.text": text})
                    
                def q19Changed(self,text):
                    logger.warning(">>> Entering q19Changed(text=%s)", text, extra={"event.action": "q19Changed", "logrite.text": text})
                    self.Persapparaat.setText(text)
                    logger.debug("<<< Exiting q19Changed(text=%s)", text, extra={"event.action": "q19Changed", "logrite.text": text})
                    
                def q20Changed(self,text):
                    logger.warning(">>> Entering q20Changed(text=%s)", text, extra={"event.action": "q20Changed", "logrite.text": text})
                    self.Atlaskraan.setText(text)
                    logger.debug("<<< Exiting q20Changed(text=%s)", text, extra={"event.action": "q20Changed", "logrite.text": text})
                    
                def q21Changed(self,text):
                    logger.warning(">>> Entering q21Changed(text=%s)", text, extra={"event.action": "q21Changed", "logrite.text": text})
                    self.Kraan_groot.setText(text)
                    logger.debug("<<< Exiting q21Changed(text=%s)", text, extra={"event.action": "q21Changed", "logrite.text": text})
                    
                def q22Changed(self,text):
                    logger.warning(">>> Entering q22Changed(text=%s)", text, extra={"event.action": "q22Changed", "logrite.text": text})
                    self.Mainliner.setText(text)
                    logger.debug("<<< Exiting q22Changed(text=%s)", text, extra={"event.action": "q22Changed", "logrite.text": text})
                    
                def q23Changed(self,text):
                    logger.warning(">>> Entering q23Changed(text=%s)", text, extra={"event.action": "q23Changed", "logrite.text": text})
                    self.Hormachine.setText(text)
                    logger.debug("<<< Exiting q23Changed(text=%s)", text, extra={"event.action": "q23Changed", "logrite.text": text})
                    
                def q24Changed(self,text):
                    logger.warning(">>> Entering q24Changed(text=%s)", text, extra={"event.action": "q24Changed", "logrite.text": text})
                    self.Wagon.setText(text)
                    logger.debug("<<< Exiting q24Changed(text=%s)", text, extra={"event.action": "q24Changed", "logrite.text": text})
                    
                def q25Changed(self,text):
                    logger.warning(">>> Entering q25Changed(text=%s)", text, extra={"event.action": "q25Changed", "logrite.text": text})
                    self.Locomotor.setText(text)
                    logger.debug("<<< Exiting q25Changed(text=%s)", text, extra={"event.action": "q25Changed", "logrite.text": text})
                    
                def q26Changed(self,text):
                    logger.warning(">>> Entering q26Changed(text=%s)", text, extra={"event.action": "q26Changed", "logrite.text": text})
                    self.Locomotief.setText(text)
                    logger.debug("<<< Exiting q26Changed(text=%s)", text, extra={"event.action": "q26Changed", "logrite.text": text})
                    
                def q27Changed(self,text):
                    logger.warning(">>> Entering q27Changed(text=%s)", text, extra={"event.action": "q27Changed", "logrite.text": text})
                    self.Stormobiel.setText(text)
                    logger.debug("<<< Exiting q27Changed(text=%s)", text, extra={"event.action": "q27Changed", "logrite.text": text})
                    
                def q28Changed(self,text):
                    logger.warning(">>> Entering q28Changed(text=%s)", text, extra={"event.action": "q28Changed", "logrite.text": text})
                    self.Montagewagen.setText(text)
                    logger.debug("<<< Exiting q28Changed(text=%s)", text, extra={"event.action": "q28Changed", "logrite.text": text})
                    
                def q29Changed(self,text):
                    logger.warning(">>> Entering q29Changed(text=%s)", text, extra={"event.action": "q29Changed", "logrite.text": text})
                    self.Telecomuren.setText(text)
                    logger.debug("<<< Exiting q29Changed(text=%s)", text, extra={"event.action": "q29Changed", "logrite.text": text})
                    
                def q30Changed(self,text):
                    logger.warning(">>> Entering q30Changed(text=%s)", text, extra={"event.action": "q30Changed", "logrite.text": text})
                    self.Robeltrein.setText(text)
                    logger.debug("<<< Exiting q30Changed(text=%s)", text, extra={"event.action": "q30Changed", "logrite.text": text})

                def returnq1(self):
                    logger.warning(">>> Entering returnq1()", extra={"event.action": "returnq1"})
                    logger.debug("<<< Exiting returnq1()", extra={"event.action": "returnq1"})
                    return self.Omschrijving.text()
                                
                def returnq3(self):
                    logger.warning(">>> Entering returnq3()", extra={"event.action": "returnq3"})
                    logger.debug("<<< Exiting returnq3()", extra={"event.action": "returnq3"})
                    return self.Eenheid.text()
                                
                def returnq9(self):
                    logger.warning(">>> Entering returnq9()", extra={"event.action": "returnq9"})
                    logger.debug("<<< Exiting returnq9()", extra={"event.action": "returnq9"})
                    return self.Construktieuren.text()
                
                def returnq10(self):
                    logger.warning(">>> Entering returnq10()", extra={"event.action": "returnq10"})
                    logger.debug("<<< Exiting returnq10()", extra={"event.action": "returnq10"})
                    return self.Montageuren.text()
                
                def returnq11(self):
                    logger.warning(">>> Entering returnq11()", extra={"event.action": "returnq11"})
                    logger.debug("<<< Exiting returnq11()", extra={"event.action": "returnq11"})
                    return self.Retourlasuren.text()
                
                def returnq12(self):
                    logger.warning(">>> Entering returnq12()", extra={"event.action": "returnq12"})
                    logger.debug("<<< Exiting returnq12()", extra={"event.action": "returnq12"})
                    return self.BFIuren.text()
                
                def returnq13(self):
                    logger.warning(">>> Entering returnq13()", extra={"event.action": "returnq13"})
                    logger.debug("<<< Exiting returnq13()", extra={"event.action": "returnq13"})
                    return self.Voedinguren.text()
                
                def returnq14(self):
                    logger.warning(">>> Entering returnq14()", extra={"event.action": "returnq14"})
                    logger.debug("<<< Exiting returnq14()", extra={"event.action": "returnq14"})
                    return self.Bvluren.text()
                
                def returnq15(self):
                    logger.warning(">>> Entering returnq15()", extra={"event.action": "returnq15"})
                    logger.debug("<<< Exiting returnq15()", extra={"event.action": "returnq15"})
                    return self.Spoorleguren.text()
                
                def returnq16(self):
                    logger.warning(">>> Entering returnq16()", extra={"event.action": "returnq16"})
                    logger.debug("<<< Exiting returnq16()", extra={"event.action": "returnq16"})
                    return self.Spoorlasuren.text()
                
                def returnq17(self):
                    logger.warning(">>> Entering returnq17()", extra={"event.action": "returnq17"})
                    logger.debug("<<< Exiting returnq17()", extra={"event.action": "returnq17"})
                    return self.Inhuururen.text()
                
                def returnq18(self):
                    logger.warning(">>> Entering returnq18()", extra={"event.action": "returnq18"})
                    logger.debug("<<< Exiting returnq18()", extra={"event.action": "returnq18"})
                    return self.Sleuvengraver.text()
                
                def returnq19(self):
                    logger.warning(">>> Entering returnq19()", extra={"event.action": "returnq19"})
                    logger.debug("<<< Exiting returnq19()", extra={"event.action": "returnq19"})
                    return self.Persapparaat.text()
                
                def returnq20(self):
                    logger.warning(">>> Entering returnq20()", extra={"event.action": "returnq20"})
                    logger.debug("<<< Exiting returnq20()", extra={"event.action": "returnq20"})
                    return self.Atlaskraan.text()
                
                def returnq21(self):
                    logger.warning(">>> Entering returnq21()", extra={"event.action": "returnq21"})
                    logger.debug("<<< Exiting returnq21()", extra={"event.action": "returnq21"})
                    return self.Kraan_groot.text()
                
                def returnq22(self):
                    logger.warning(">>> Entering returnq22()", extra={"event.action": "returnq22"})
                    logger.debug("<<< Exiting returnq22()", extra={"event.action": "returnq22"})
                    return self.Mainliner.text()
                
                def returnq23(self):
                    logger.warning(">>> Entering returnq23()", extra={"event.action": "returnq23"})
                    logger.debug("<<< Exiting returnq23()", extra={"event.action": "returnq23"})
                    return self.Hormachine.text()
              
                def returnq24(self):
                    logger.warning(">>> Entering returnq24()", extra={"event.action": "returnq24"})
                    logger.debug("<<< Exiting returnq24()", extra={"event.action": "returnq24"})
                    return self.Wagon.text()
                
                def returnq25(self):
                    logger.warning(">>> Entering returnq25()", extra={"event.action": "returnq25"})
                    logger.debug("<<< Exiting returnq25()", extra={"event.action": "returnq25"})
                    return self.Locomotor.text()
                
                def returnq26(self):
                    logger.warning(">>> Entering returnq26()", extra={"event.action": "returnq26"})
                    logger.debug("<<< Exiting returnq26()", extra={"event.action": "returnq26"})
                    return self.Locomotief.text()
              
                def returnq27(self):
                    logger.warning(">>> Entering returnq27()", extra={"event.action": "returnq27"})
                    logger.debug("<<< Exiting returnq27()", extra={"event.action": "returnq27"})
                    return self.Stormobiel.text()
                
                def returnq28(self):
                    logger.warning(">>> Entering returnq28()", extra={"event.action": "returnq28"})
                    logger.debug("<<< Exiting returnq28()", extra={"event.action": "returnq28"})
                    return self.Montagewagen.text()
                
                def returnq29(self):
                    logger.warning(">>> Entering returnq29()", extra={"event.action": "returnq29"})
                    logger.debug("<<< Exiting returnq29()", extra={"event.action": "returnq29"})
                    return self.Telecomuren.text()
        
                def returnq30(self):
                    logger.warning(">>> Entering returnq30()", extra={"event.action": "returnq30"})
                    logger.debug("<<< Exiting returnq30()", extra={"event.action": "returnq30"})
                    return self.Robeltrein.text()

                @staticmethod
                def getData(parent=None):
                    dialog = MainWindow()
                    dialog.exec_()
                    return [dialog.returnq1(), dialog.returnq3(), dialog.returnq9(),\
                            dialog.returnq10(), dialog.returnq11(), dialog.returnq12(),\
                            dialog.returnq13(), dialog.returnq14(), dialog.returnq15(),\
                            dialog.returnq16(), dialog.returnq17(), dialog.returnq18(),\
                            dialog.returnq19(), dialog.returnq20(), dialog.returnq21(),\
                            dialog.returnq22(), dialog.returnq23(), dialog.returnq24(),\
                            dialog.returnq25(), dialog.returnq26(), dialog.returnq27(),\
                            dialog.returnq28(), dialog.returnq29(), dialog.returnq30()]

            mainWin = MainWindow()
            data = mainWin.getData()
     
            chflag = 0
            for k in range(0,24):
                if data[k]:
                    chflag = 1
            if chflag == 0:
                return
            if data[0]:
                ms0 = str(data[0])
            else:
                ms0 = rpsel[1]
            if data[1]:
                mf1 = data[1]
            else:
                mf1 = rpsel[3]  
            if data[2]:
                mf2 = float(data[2])
            else:
                mf2= rpsel[9]
            if data[3]:
                mf3 = data[3]
            else:
                mf3 = rpsel[10]
            if data[4]:
                mf4 = float(data[4])
            else:
                mf4= rpsel[11]
            if data[5]:
                mf5 = float(data[5])
            else:
                mf5 = rpsel[12]
            if data[6]:
                mf6 = float(data[6])
            else:
                mf6 = rpsel[13]
            if data[7]:
                mf7 = float(data[7])
            else:
                mf7 = rpsel[14]
            if data[8]:
                mf8 = float(data[8])
            else:
                mf8= rpsel[15]
            if data[9]:
                mf9 = float(data[9])
            else:
                mf9= rpsel[16]
            if data[10]:
                mf10 = float(data[10])
            else:
                mf10= rpsel[17]     
            if data[11]:
                mf11 = float(data[11])
            else:
                mf11= rpsel[18]     
            if data[12]:
                mf12 = float(data[12])
            else:
                mf12= rpsel[19]
            if data[13]:
                mf13 = float(data[13])
            else:
                mf13= rpsel[20]
            if data[14]:
                mf14 = float(data[14])
            else:
                mf14= rpsel[21]
            if data[15]:
                mf15 = float(data[15])
            else:
                mf15= rpsel[22]
            if data[16]:
                mf16 = float(data[16])
            else:
                mf16= rpsel[23]
            if data[17]:
                mf17 = float(data[17])
            else:
                mf17 = rpsel[24]
            if data[18]:
                mf18 = float(data[18])
            else:
                mf18= rpsel[25]
            if data[19]:
                mf19 = float(data[19])
            else:
                mf19= rpsel[26]
            if data[20]:
                mf20 = float(data[20])
            else:
                mf20= rpsel[27]
            if data[21]:
                mf21 = float(data[21])
            else:
                mf21= rpsel[28]
            if data[22]:
                mf22 = data[22]
            else:
                mf22= rpsel[29]
            if data[23]:
                mf23 = float(data[23])
            else:
                mf23= rpsel[30]

            metadata = MetaData()
            params_hours = Table('params_hours', metadata,
                                 Column('rateID', Integer, primary_key=True),
                                 Column('hourly_tariff', Float),
                                 Column('item', String))

            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            con = engine.connect()
            selpar = select([params_hours]).order_by(params_hours.c.rateID)
            rppar = con.execute(selpar).fetchall()

            metadata = MetaData()
            params_services = Table('params_services', metadata,
                                    Column('servicesID', Integer, primary_key=True),
                                    Column('hourly_tariff', Float),
                                    Column('item', String))

            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            con = engine.connect()
            selpar1 = select([params_services]).order_by(params_services.c.servicesID)
            rppar1 = con.execute(selpar1).fetchall()
                                                                 
            upd1 = update(clusters).where(clusters.c.clusterID == clusternr).values(
                omschrijving=ms0, eenheid=mf1, uren_constr = mf2,\
                uren_mont=mf3, uren_retourlas=mf4, uren_bfi=mf5, uren_voeding=mf6,\
                uren_bvl=mf7, uren_spoorleg=mf8, uren_spoorlas=mf9, uren_inhuur=mf10,\
                sleuvengraver=mf11, persapparaat=mf12, atlaskraan=mf13, kraan_groot=mf14,\
                mainliner=mf15, hormachine=mf16, wagon=mf17,locomotor=mf18,locomotief=mf19,\
                montagewagen=mf20, stormobiel=mf21, uren_telecom=mf22, robeltrein=mf23)
            con.execute(upd1)
            upd2 = update(clusters).where(clusters.c.clusterID == clusternr).values( \
                lonen=clusters.c.uren_constr * rppar[1][1] + clusters.c.uren_mont * rppar[2][1] \
                      + clusters.c.uren_retourlas * rppar[8][1] + clusters.c.uren_bfi * rppar[3][1] \
                      + clusters.c.uren_voeding * rppar[4][1] + clusters.c.uren_bvl * rppar[5][1] \
                      + clusters.c.uren_spoorleg * rppar[6][1] + clusters.c.uren_spoorlas * rppar[7][1] \
                      + clusters.c.uren_telecom * rppar[10][1], \
                materieel=clusters.c.sleuvengraver * rppar1[0][1] + clusters.c.persapparaat \
                          * rppar1[1][1] + clusters.c.atlaskraan * rppar1[2][1] + clusters.c.kraan_groot \
                          * rppar1[3][1] + clusters.c.mainliner * rppar1[4][1] + clusters.c.hormachine \
                          * rppar1[5][1] + clusters.c.wagon * rppar1[6][1] + clusters.c.locomotor \
                          * rppar1[7][1] + clusters.c.locomotief * rppar1[8][1] + clusters.c.montagewagen \
                          * rppar1[9][1] + clusters.c.stormobiel * rppar1[10][1] + clusters.c.robeltrein \
                          * rppar1[11][1], inhuur=clusters.c.uren_inhuur * rppar[0][1])
            con.execute(upd2)
            upd3 = update(clusters).where(clusters.c.clusterID == clusternr).values(\
                    diensten = clusters.c.inhuur+clusters.c.leiding+clusters.c.huisvesting+\
                    clusters.c.kabelwerk+clusters.c.grondverzet+clusters.c.betonwerk+\
                    clusters.c.vervoer+clusters.c.overig)
            con.execute(upd3)
            upd4 = update(clusters).where(clusters.c.clusterID == clusternr).values(\
                    prijs = clusters.c.lonen+clusters.c.materialen+clusters.c.diensten+\
                    clusters.c.materieel)
            con.execute(upd4)
            invoerOK()
        
    win = MyWindow(data_list, header)
    win.exec_()
    zoeken(m_email)