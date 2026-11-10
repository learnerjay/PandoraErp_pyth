from login import hoofdMenu
import datetime
from PyQt5.QtWidgets import QLabel, QLineEdit, QGridLayout, QPushButton,\
  QDialog, QMessageBox, QComboBox, QWidget, QTableView, QCheckBox
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtCore import Qt, QAbstractTableModel
from sqlalchemy import (Table, Column, Integer, String, Float, Boolean,\
                        MetaData, create_engine, select, update, false, and_)
import logging
logger = logging.getLogger(__name__)

def refresh(keuze, zoekterm, m_email, self):
    logger.warning(">>> Entering refresh(keuze=%s,zoekterm=%s,m_email=%s)", keuze, zoekterm, m_email, extra={"event.action": "refresh", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
    self.close()
    toonAfdrachten(keuze, zoekterm, m_email)
    logger.debug("<<< Exiting refresh(keuze=%s,zoekterm=%s,m_email=%s)", keuze, zoekterm, m_email, extra={"event.action": "refresh", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
    
def ongInvoer():
    logger.warning(">>> Entering ongInvoer()", extra={"event.action": "ongInvoer"})
    msg = QMessageBox()
    logger.debug("ongInvoer(): msg → %s", msg, extra={"event.action": "ongInvoer"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Foutieve invoer\nzoekterm opnieuw invoeren s.v.p.!')
    msg.setWindowTitle('Afdrachten betalingen')               
    logger.debug("<<< Exiting ongInvoer()", extra={"event.action": "ongInvoer"})
    msg.exec_()

def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})

def betalingGelukt():
    logger.warning(">>> Entering betalingGelukt()", extra={"event.action": "betalingGelukt"})
    msg = QMessageBox()
    logger.debug("betalingGelukt(): msg → %s", msg, extra={"event.action": "betalingGelukt"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Information)
    msg.setText('Betaling is geboekt!')
    msg.setWindowTitle('Afdrachten betalingen')
    logger.debug("<<< Exiting betalingGelukt()", extra={"event.action": "betalingGelukt"})
    msg.exec_()

def zoeken(m_email):
    logger.warning(">>> Entering zoeken(m_email=%s)", m_email, extra={"event.action": "zoeken"})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            self.setWindowTitle("Afdrachten betalingen")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            self.setFont(QFont('Arial', 10))
                              
            self.Keuze = QLabel()
            logger.debug("__init__(parent=%s): self.Keuze → %s", parent, self.Keuze, extra={"event.action": "__init__"})
            k0Edit = QComboBox()
            logger.debug("__init__(self=%s,parent=%s): k0Edit → %s", self, parent, k0Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): k0Edit → %s", parent, k0Edit, extra={"event.action": "__init__"})
            k0Edit.setFixedWidth(250)
            k0Edit.setFont(QFont("Arial", 10))
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.addItem(' Opvragen/Betalen Afdrachten')
            k0Edit.addItem('1. Gesorteerd op periode')
            k0Edit.addItem('2. Gefilterd op tijdvak')
            k0Edit.addItem('3. Gefilterd niet betaald')
            k0Edit.addItem('4. Gefilterd op instantie')
            k0Edit.addItem('5. Gefilterd op boekdatum')
            k0Edit.addItem('6. Gefilterd op Balieverkopen')
            k0Edit.addItem('7. Gefilterd op Online-orders')
            
            k0Edit.activated[str].connect(self.k0Changed)
    
            self.Zoekterm = QLabel()
            logger.debug("__init__(parent=%s): self.Zoekterm → %s", parent, self.Zoekterm, extra={"event.action": "__init__"})
            zktermEdit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): zktermEdit → %s", self, parent, zktermEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): zktermEdit → %s", parent, zktermEdit, extra={"event.action": "__init__"})
            zktermEdit.setFixedWidth(150)
            zktermEdit.setFont(QFont("Times", 10))
            zktermEdit.textChanged.connect(self.zktermChanged)
     
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
            lbl1 = QLabel('Zoekterm')  
            logger.debug("__init__(parent=%s): lbl1 → %s", parent, lbl1, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl1 → %s", self, parent, lbl1, extra={"event.action": "__init__"})
            grid.addWidget(lbl1, 2, 1)
            grid.addWidget(zktermEdit, 2, 1, 1, 1, Qt.AlignRight)
            
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 4, 0, 1, 2, Qt.AlignCenter)
            
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
    
            grid.addWidget(applyBtn, 3, 1, 1 , 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial", 10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            closeBtn = QPushButton('Sluiten')
            logger.debug("__init__(parent=%s): closeBtn → %s", parent, closeBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): closeBtn → %s", self, parent, closeBtn, extra={"event.action": "__init__"})
            closeBtn.clicked.connect(lambda: windowSluit(self, m_email))
    
            grid.addWidget(closeBtn, 3, 1)
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            closeBtn.setFont(QFont("Arial", 10))
            closeBtn.setFixedWidth(100)
            closeBtn.setStyleSheet("color: black;  background-color: gainsboro")
               
        def k0Changed(self, text):
            logger.warning(">>> Entering k0Changed(text=%s)", text, extra={"event.action": "k0Changed", "logrite.text": text})
            self.Keuze.setText(text)
            logger.debug("<<< Exiting k0Changed(text=%s)", text, extra={"event.action": "k0Changed", "logrite.text": text})
            
        def zktermChanged(self, text):
            logger.warning(">>> Entering zktermChanged(text=%s)", text, extra={"event.action": "zktermChanged", "logrite.text": text})
            self.Zoekterm.setText(text)
            logger.debug("<<< Exiting zktermChanged(text=%s)", text, extra={"event.action": "zktermChanged", "logrite.text": text})
 
        def returnk0(self):
            logger.warning(">>> Entering returnk0()", extra={"event.action": "returnk0"})
            logger.debug("<<< Exiting returnk0()", extra={"event.action": "returnk0"})
            return self.Keuze.text()
        
        def returnzkterm(self):
            logger.warning(">>> Entering returnzkterm()", extra={"event.action": "returnzkterm"})
            logger.debug("<<< Exiting returnzkterm()", extra={"event.action": "returnzkterm"})
            return self.Zoekterm.text()
        
        @staticmethod
        def getData(parent=None):
            logger.warning(">>> Entering getData(parent=%s)", parent, extra={"event.action": "getData"})
            dialog = Widget(parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog, extra={"event.action": "getData"})
            dialog.exec_()
            logger.debug("<<< Exiting getData(parent=%s)", parent, extra={"event.action": "getData"})
            return [dialog.returnk0(), dialog.returnzkterm()]       

    window = Widget()
    data = window.getData()
    if not data[0] or data[0][0] == ' ':
        keuze = 0
    elif data[0]:
        keuze = int(data[0][0])
    else:
        keuze = 0
    if data[1]:
        zoekterm = data[1]
    else:
        zoekterm = ''
    toonAfdrachten(keuze, zoekterm, m_email)
    
def toonAfdrachten(keuze, zoekterm, m_email):         
    logger.warning(">>> Entering toonAfdrachten(keuze=%s,zoekterm=%s,m_email=%s)", keuze, zoekterm, m_email, extra={"event.action": "toonAfdrachten", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
    class MyWindow(QDialog):
        def __init__(self, data_list, header, *args):
            logger.warning(">>> Entering __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})
            QWidget.__init__(self, *args,)
            self.setWindowTitle('Afdrachten opvragen / betalen')        
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
            table_view.resizeColumnsToContents()
            table_view.setSelectionBehavior(QTableView.SelectRows)
            #table_view.clicked.connect(selectRow)
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
            freshBtn.clicked.connect(lambda: refresh(keuze, zoekterm, m_email, self))

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
            self.setGeometry(10, 30, 1900, 900)
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
            logger.debug("__init__(): self.lbl → %s", self.lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.pixmap → %s", self.pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl → %s", self, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.logo → %s", self.logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): logo → %s", self, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Soort → %s", self.Soort, extra={"event.action": "__init__"})
            logger.debug("__init__(): q1Edit → %s", q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q1Edit → %s", self, q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Bedrag → %s", self.Bedrag, extra={"event.action": "__init__"})
            logger.debug("__init__(): q2Edit → %s", q2Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q2Edit → %s", self, q2Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Boekdatum → %s", self.Boekdatum, extra={"event.action": "__init__"})
            logger.debug("__init__(): q3Edit → %s", q3Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q3Edit → %s", self, q3Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Betaaldatum → %s", self.Betaaldatum, extra={"event.action": "__init__"})
            logger.debug("__init__(): q4Edit → %s", q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q4Edit → %s", self, q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Instantie → %s", self.Instantie, extra={"event.action": "__init__"})
            logger.debug("__init__(): q5Edit → %s", q5Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q5Edit → %s", self, q5Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Werknemer → %s", self.Werknemer, extra={"event.action": "__init__"})
            logger.debug("__init__(): q6Edit → %s", q6Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q6Edit → %s", self, q6Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Werknummer → %s", self.Werknummer, extra={"event.action": "__init__"})
            logger.debug("__init__(): q7Edit → %s", q7Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q7Edit → %s", self, q7Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Werkorder → %s", self.Werkorder, extra={"event.action": "__init__"})
            logger.debug("__init__(): q8Edit → %s", q8Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q8Edit → %s", self, q8Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Rekeningnummer → %s", self.Rekeningnummer, extra={"event.action": "__init__"})
            logger.debug("__init__(): q9Edit → %s", q9Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q9Edit → %s", self, q9Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Periode → %s", self.Periode, extra={"event.action": "__init__"})
            logger.debug("__init__(): q10Edit → %s", q10Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q10Edit → %s", self, q10Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Inkooporder → %s", self.Inkooporder, extra={"event.action": "__init__"})
            logger.debug("__init__(): q11Edit → %s", q11Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q11Edit → %s", self, q11Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Verkooporder → %s", self.Verkooporder, extra={"event.action": "__init__"})
            logger.debug("__init__(): q12Edit → %s", q12Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q12Edit → %s", self, q12Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl1 → %s", lbl1, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl1 → %s", self, lbl1, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl2 → %s", lbl2, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl2 → %s", self, lbl2, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl3 → %s", lbl3, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl3 → %s", self, lbl3, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl4 → %s", lbl4, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl4 → %s", self, lbl4, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl5 → %s", lbl5, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl5 → %s", self, lbl5, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl6 → %s", lbl6, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl6 → %s", self, lbl6, extra={"event.action": "__init__"})
            logger.debug("__init__(): cBox → %s", cBox, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): cBox → %s", self, cBox, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl7 → %s", lbl7, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl7 → %s", self, lbl7, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl8 → %s", lbl8, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl8 → %s", self, lbl8, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl9 → %s", lbl9, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl9 → %s", self, lbl9, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl10 → %s", lbl10, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl10 → %s", self, lbl10, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl20 → %s", lbl20, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl20 → %s", self, lbl20, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl21 → %s", lbl21, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl21 → %s", self, lbl21, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl22 → %s", lbl22, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl22 → %s", self, lbl22, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl23 → %s", lbl23, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl23 → %s", self, lbl23, extra={"event.action": "__init__"})
            logger.debug("__init__(): btlBtn → %s", btlBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): btlBtn → %s", self, btlBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(): sluitBtn → %s", sluitBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): sluitBtn → %s", self, sluitBtn, extra={"event.action": "__init__"})
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
        
    header = ['Afdrachtnr', 'Soort afdracht', 'Bedrag        ', 'Boekdatum', 'Betaaldatum',\
              'Betaalstatus', 'Instantie','Werknemer', 'Werknummer', 'Werkorder',\
              'Rekeningnummer', 'Betaling over periode', 'Inkooporder', 'Verkooporder']
    metadata = MetaData()   
    afdrachten = Table('afdrachten', metadata,
        Column('afdrachtID', Integer(), primary_key=True),
        Column('soort', String),
        Column('bedrag', Float),
        Column('boekdatum', String),
        Column('betaaldatum', String),
        Column('betaalstatus', String),
        Column('instantie', String),
        Column('werknemerID', Integer),
        Column('werknummerID', Integer),
        Column('werkorderID', Integer),
        Column('rekeningnummer', String),
        Column('periode', String),
        Column('inkoopordernummer', Integer),
        Column('ovbestelID', Integer))
 
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
    if keuze == 1:
       selafdr = select([afdrachten]).order_by(afdrachten.c.periode,\
                       afdrachten.c.instantie).order_by(afdrachten.c.afdrachtID)
       rpafdr = con.execute(selafdr)
    elif keuze == 2:
        selafdr = select([afdrachten]).where(afdrachten.c.periode.like(zoekterm+'%'))
        rpafdr = con.execute(selafdr)
    elif keuze == 3:
        selafdr = select([afdrachten]).where(afdrachten.c.betaalstatus == false()).\
          order_by(afdrachten.c.periode, afdrachten.c.instantie)
        rpafdr = con.execute(selafdr)
    elif keuze == 4:
        selafdr = select([afdrachten]).where(afdrachten.c.instantie.ilike('%'+zoekterm+'%')).\
          order_by(afdrachten.c.periode, afdrachten.c.instantie)
        rpafdr = con.execute(selafdr)
    elif keuze == 5:
        selafdr = select([afdrachten]).where(afdrachten.c.boekdatum.like(zoekterm+'%')).\
          order_by(afdrachten.c.boekdatum)
        rpafdr = con.execute(selafdr)
    elif keuze == 6:
        selafdr = select([afdrachten]).where(and_(afdrachten.c.ovbestelID<500000000,\
          afdrachten.c.ovbestelID>0)).order_by(afdrachten.c.ovbestelID)
        rpafdr = con.execute(selafdr)
    elif keuze == 7:
        selafdr = select([afdrachten]).where(afdrachten.c.ovbestelID>499999999).\
          order_by(afdrachten.c.ovbestelID)
        rpafdr = con.execute(selafdr)
    else:
        ongInvoer()
        zoeken(m_email)
   
    data_list=[]
    for row in rpafdr:
        data_list += [(row)]
        
    def showSelection(idx):
        logger.warning(">>> Entering showSelection(idx=%s)", idx, extra={"event.action": "showSelection", "logrite.idx": idx})
        mafdrnr = idx.data()
        logger.debug("showSelection(idx=%s): mafdrnr → %s", idx, mafdrnr, extra={"event.action": "showSelection", "logrite.idx": idx})
        if idx.column() == 0:
            mbetaald = str(datetime.datetime.now())[0:10]
            logger.debug("showSelection(idx=%s): mbetaald → %s", idx, mbetaald, extra={"event.action": "showSelection", "logrite.idx": idx})
            metadata = MetaData()   
            afdrachten = Table('afdrachten', metadata,
                Column('afdrachtID', Integer(), primary_key=True),
                Column('soort', String),
                Column('bedrag', Float),
                Column('boekdatum', String),
                Column('betaaldatum', String),
                Column('betaalstatus', Boolean),
                Column('instantie', String),
                Column('werknemerID', Integer),
                Column('werknummerID', Integer),
                Column('werkorderID', Integer),
                Column('rekeningnummer', String),
                Column('periode', String),
                Column('inkoopordernummer', Integer),
                Column('ovbestelID', Integer))
            logger.debug("showSelection(idx=%s): metadata → %s", idx, metadata, extra={"event.action": "showSelection", "logrite.idx": idx})
            
            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            logger.debug("showSelection(idx=%s): engine → %s", idx, engine, extra={"event.action": "showSelection", "logrite.idx": idx})
            con = engine.connect()
            selbet = select([afdrachten]).where(afdrachten.c.afdrachtID == mafdrnr)
            logger.debug("showSelection(idx=%s): con → %s", idx, con, extra={"event.action": "showSelection", "logrite.idx": idx})
            rpbet = con.execute(selbet).first()
                  
            logger.debug("showSelection(idx=%s): selbet → %s", idx, selbet, extra={"event.action": "showSelection", "logrite.idx": idx})
            logger.debug("showSelection(idx=%s): rpbet → %s", idx, rpbet, extra={"event.action": "showSelection", "logrite.idx": idx})
            class MainWindow(QDialog):
                def __init__(self):
                    logger.debug("<<< Exiting showSelection(idx=%s)", idx, extra={"event.action": "showSelection", "logrite.idx": idx})
                    QDialog.__init__(self)
                    
                    grid = QGridLayout()
                    grid.setSpacing(20)
                    
                    self.setWindowTitle("Betalen afdrachtrekening")
                    self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
                    
                    self.setFont(QFont('Arial', 10))   
                                                      
                    self.lbl = QLabel()
                    self.pixmap = QPixmap('./images/logos/verbinding.jpg')
                    self.lbl.setPixmap(self.pixmap)
                    grid.addWidget(self.lbl , 0, 0)
            
                    self.logo = QLabel()
                    self.pixmap = QPixmap('./images/logos/logo.jpg')
                    self.logo.setPixmap(self.pixmap)
                    grid.addWidget(self.logo , 0, 2, 1, 1, Qt.AlignCenter)
                    
                    self.Soort = QLabel()
                    q1Edit = QLineEdit(rpbet[1])
                    q1Edit.setFixedWidth(250)
                    q1Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q1Edit.setDisabled(True)
                                    
                    self.Bedrag = QLabel()
                    q2Edit = QLineEdit(str(round(float(rpbet[2]),2)))
                    q2Edit.setAlignment(Qt.AlignRight)
                    q2Edit.setFixedWidth(150)
                    q2Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q2Edit.setDisabled(True)
                     
                    self.Boekdatum = QLabel(mbetaald)
                    q3Edit = QLineEdit(str(rpbet[3]))
                    q3Edit.setFixedWidth(150)
                    q3Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q3Edit.setDisabled(True)
                    
                    self.Betaaldatum = QLabel()
                    q4Edit = QLineEdit(str(rpbet[4]))
                    q4Edit.setFixedWidth(150)
                    q4Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q4Edit.setDisabled(True)
                                 
                    self.Instantie = QLabel()
                    q5Edit = QLineEdit(rpbet[6])
                    q5Edit.setFixedWidth(250)
                    q5Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q5Edit.setDisabled(True)
                    
                    self.Werknemer = QLabel()
                    q6Edit = QLineEdit(str(rpbet[7]))
                    q6Edit.setAlignment(Qt.AlignRight)
                    q6Edit.setFixedWidth(150)
                    q6Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q6Edit.setDisabled(True)
                    
                    self.Werknummer = QLabel()
                    q7Edit = QLineEdit(str(rpbet[8]))
                    q7Edit.setAlignment(Qt.AlignRight)
                    q7Edit.setFixedWidth(150)
                    q7Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q7Edit.setDisabled(True)
                    
                    self.Werkorder = QLabel()
                    q8Edit = QLineEdit(str(rpbet[9]))
                    q8Edit.setAlignment(Qt.AlignRight)
                    q8Edit.setFixedWidth(150)
                    q8Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q8Edit.setDisabled(True)
                    
                    self.Rekeningnummer = QLabel()
                    q9Edit = QLineEdit(str(rpbet[10]))
                    q9Edit.setFixedWidth(250)
                    q9Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q9Edit.setDisabled(True)
                    
                    self.Periode = QLabel()
                    q10Edit = QLineEdit(str(rpbet[11]))
                    q10Edit.setAlignment(Qt.AlignRight)
                    q10Edit.setFixedWidth(150)
                    q10Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q10Edit.setDisabled(True)
                    
                    self.Inkooporder = QLabel()
                    q11Edit = QLineEdit(str(rpbet[12]))
                    q11Edit.setAlignment(Qt.AlignRight)
                    q11Edit.setFixedWidth(150)
                    q11Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q11Edit.setDisabled(True)
                                                  
                    self.Verkooporder = QLabel()
                    q12Edit = QLineEdit(str(rpbet[13]))
                    q12Edit.setAlignment(Qt.AlignRight)
                    q12Edit.setFixedWidth(150)
                    q12Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q12Edit.setDisabled(True)    
                
                    lbl1 = QLabel('Afdrachtnummer')  
                    lbl1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl1, 1, 0)
                    
                    lbl2 = QLabel(str(mafdrnr))
                    grid.addWidget(lbl2, 1, 1)
                           
                    lbl3 = QLabel('Soort')  
                    lbl3.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl3, 2, 0)
                    grid.addWidget(q1Edit, 2, 1)
                                                         
                    lbl4 = QLabel('Bedrag')  
                    lbl4.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl4, 3, 0)
                    grid.addWidget(q2Edit, 3, 1)
                    
                    lbl5 = QLabel('Boekdatum')  
                    lbl5.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl5, 4, 0)
                    grid.addWidget(q3Edit, 4, 1)
                    
                    lbl6 = QLabel('Betaaldatum')  
                    lbl6.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl6, 5, 0)
                    grid.addWidget(q4Edit, 5, 1)
                    
                    cBox = QCheckBox('Betaal')
                    cBox.stateChanged.connect(self.cBoxChanged)
                    grid.addWidget(cBox, 5, 2)
                    if len(rpbet[4])==10:
                       cBox.setEnabled(False)
                    
                    lbl7 = QLabel('Instantie')  
                    lbl7.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl7, 6, 0)
                    grid.addWidget(q5Edit, 6, 1, 1, 2)
                    
                    lbl8 = QLabel('Werknemer')  
                    lbl8.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl8, 7, 0)
                    grid.addWidget(q6Edit, 7, 1)
                    
                    lbl9 = QLabel('Werknummer')  
                    lbl9.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl9, 8, 0)
                    grid.addWidget(q7Edit, 8, 1)
                    
                    lbl10 = QLabel('Werkorder')  
                    lbl10.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl10, 9, 0)
                    grid.addWidget(q8Edit, 9, 1)
                    
                    lbl20 = QLabel('Rekeningnummer')  
                    lbl20.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl20, 10, 0)
                    grid.addWidget(q9Edit, 10, 1, 1, 2)
                      
                    lbl21 = QLabel('Periode')  
                    lbl21.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl21, 11, 0)
                    grid.addWidget(q10Edit, 11, 1)
                    
                    lbl22 = QLabel('Inkooporder')  
                    lbl22.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl22, 12, 0)
                    grid.addWidget(q11Edit, 12, 1)
                       
                    lbl23 = QLabel('Verkooporder')  
                    lbl23.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl23, 13, 0)
                    grid.addWidget(q12Edit, 13, 1)
                   
                    btlBtn = QPushButton('Betalen')
                    btlBtn.clicked.connect(self.accept)
            
                    grid.addWidget(btlBtn, 14, 2, 1 , 1, Qt.AlignRight)
                    btlBtn.setFont(QFont("Arial",10))
                    btlBtn.setFixedWidth(100)
                    btlBtn.setStyleSheet("color: black;  background-color: gainsboro")
                    
                    sluitBtn = QPushButton('Sluiten')
                    sluitBtn.clicked.connect(self.close)
            
                    grid.addWidget(sluitBtn, 14, 1, 1, 1, Qt.AlignRight)
                    sluitBtn.setFont(QFont("Arial",10))
                    sluitBtn.setFixedWidth(100)
                    sluitBtn.setStyleSheet("color: black;  background-color: gainsboro")
                    
                    grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 15, 0, 1, 2, Qt.AlignCenter)
                                 
                    self.setLayout(grid)
                    self.setGeometry(500, 100, 150, 150)
                                               
                state = False  
                def cBoxChanged(self, state):
                    logger.warning(">>> Entering cBoxChanged(state=%s)", state, extra={"event.action": "cBoxChanged", "logrite.state": state})
                    logger.debug("cBoxChanged(state=%s): self.state → %s", state, self.state, extra={"event.action": "cBoxChanged", "logrite.state": state})
                    logger.debug("cBoxChanged(self=%s,state=%s): self.state → %s", self, state, self.state, extra={"event.action": "cBoxChanged", "logrite.state": state})
                    if state == Qt.Checked:
                        self.state = True
                        logger.debug("<<< Exiting cBoxChanged(state=%s)", state, extra={"event.action": "cBoxChanged", "logrite.state": state})
                        
                def returncBox(self):
                      logger.warning(">>> Entering returncBox()", extra={"event.action": "returncBox"})
                      logger.debug("<<< Exiting returncBox()", extra={"event.action": "returncBox"})
                      return self.state
                       
                @staticmethod
                def getData(parent=None):
                    dialog = MainWindow()
                    dialog.exec_()
                    return [dialog.returncBox()] 
            
            mainWin = MainWindow()
            data = mainWin.getData()
                 
            if data[0]:
                mstatus = True
            else:
                return()
            if mstatus:
                  updafdr = update(afdrachten).where(afdrachten.c.afdrachtID == mafdrnr).\
                   values(betaaldatum = mbetaald, betaalstatus = mstatus)
                  con.execute(updafdr)
                  betalingGelukt()
                  con.close
        
    win = MyWindow(data_list, header)
    win.exec_()
    zoeken(m_email)