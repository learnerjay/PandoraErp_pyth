from login import hoofdMenu
import datetime
from PyQt5.QtCore import Qt, QAbstractTableModel, QRegExp
from PyQt5.QtGui import QFont, QPixmap, QRegExpValidator, QIcon
from PyQt5.QtWidgets import QWidget, QTableView, QDialog, QLabel, QGridLayout,\
       QPushButton, QMessageBox, QLineEdit, QComboBox
from sqlalchemy import (Table, Column, Integer, String, Float, Boolean, ForeignKey,\
                        MetaData, create_engine)
from sqlalchemy.sql import select, update, insert, func, and_
import logging
logger = logging.getLogger(__name__)

def refresh(keuze, zoekterm, m_email, self):
    logger.warning(">>> Entering refresh(keuze=%s,zoekterm=%s,m_email=%s)", keuze, zoekterm, m_email, extra={"event.action": "refresh", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
    self.close()
    toonOrders(keuze, zoekterm, m_email)
    logger.debug("<<< Exiting refresh(keuze=%s,zoekterm=%s,m_email=%s)", keuze, zoekterm, m_email, extra={"event.action": "refresh", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})

def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
            
def ongInvoer():
    logger.warning(">>> Entering ongInvoer()", extra={"event.action": "ongInvoer"})
    msg = QMessageBox()
    logger.debug("ongInvoer(): msg → %s", msg, extra={"event.action": "ongInvoer"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Foutieve invoer\nzoekterm opnieuw invoeren s.v.p.!')
    msg.setWindowTitle('Wijzigen interne orders ')               
    logger.debug("<<< Exiting ongInvoer()", extra={"event.action": "ongInvoer"})
    msg.exec_()
    
def geenRecord():
    logger.warning(">>> Entering geenRecord()", extra={"event.action": "geenRecord"})
    msg = QMessageBox()
    logger.debug("geenRecord(): msg → %s", msg, extra={"event.action": "geenRecord"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Geen record gevonden\nmaak een andere selektie s.v.p.!')
    msg.setWindowTitle('Artikelen opvragen')               
    logger.debug("<<< Exiting geenRecord()", extra={"event.action": "geenRecord"})
    msg.exec_() 
 
def invoerOK():
    logger.warning(">>> Entering invoerOK()", extra={"event.action": "invoerOK"})
    msg = QMessageBox()
    logger.debug("invoerOK(): msg → %s", msg, extra={"event.action": "invoerOK"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Information)
    msg.setText('Wijziging gelukt!')
    msg.setWindowTitle('Werkordergegevens')
    logger.debug("<<< Exiting invoerOK()", extra={"event.action": "invoerOK"})
    msg.exec_()

def jaarweek():
    logger.warning(">>> Entering jaarweek()", extra={"event.action": "jaarweek"})
    dt = datetime.datetime.now()
    logger.debug("jaarweek(): dt → %s", dt, extra={"event.action": "jaarweek"})
    week = str('0'+str(dt.isocalendar()[1]))[-2:]
    logger.debug("jaarweek(): week → %s", week, extra={"event.action": "jaarweek"})
    jaar = str(dt.isocalendar()[0])
    jrwk = jaar+week
    logger.debug("jaarweek(): jrwk → %s", jrwk, extra={"event.action": "jaarweek"})
    logger.debug("jaarweek(): jaar → %s", jaar, extra={"event.action": "jaarweek"})
    logger.debug("<<< Exiting jaarweek()", extra={"event.action": "jaarweek"})
    return(jrwk)

def zoeken(m_email):
    logger.warning(">>> Entering zoeken(m_email=%s)", m_email, extra={"event.action": "zoeken"})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            self.setWindowTitle("Orders_ Intern")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
   
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
            grid.addWidget(lbl , 1, 0, 1, 2)
            
            logo = QLabel()
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 1, 1, 1, 1, Qt.AlignRight)
            
            self.Keuze = QLabel()
            logger.debug("__init__(parent=%s): self.Keuze → %s", parent, self.Keuze, extra={"event.action": "__init__"})
            k0Edit = QComboBox()
            logger.debug("__init__(self=%s,parent=%s): k0Edit → %s", self, parent, k0Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): k0Edit → %s", parent, k0Edit, extra={"event.action": "__init__"})
            k0Edit.setFixedWidth(280)
            k0Edit.setFont(QFont("Arial",10))
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.addItem('        Sorteersleutel Orders Intern')
            k0Edit.addItem('1. Alle Interne Orders')
            k0Edit.addItem('2. Gefilterd op Werordernummer')
            k0Edit.addItem('3. Gefilterd op Artikelnummer')
            k0Edit.addItem('4. Gefilterd op (deel) startdatum')
            k0Edit.addItem('5. Gefilterd op (deel) datum afgemeld')
            k0Edit.addItem('6. Gefilterd op voorgangstatus A-H')
            k0Edit.addItem('7. Gefilterd op (deel) omschrijving')
            k0Edit.activated[str].connect(self.k0Changed)
            
            self.Zoekterm = QLabel()
            logger.debug("__init__(parent=%s): self.Zoekterm → %s", parent, self.Zoekterm, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): reg_ex → %s", parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): reg_ex → %s", self, parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): input_validator → %s", parent, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): input_validator → %s", self, parent, input_validator, extra={"event.action": "__init__"})
            zktermEdit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): zktermEdit → %s", self, parent, zktermEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): zktermEdit → %s", parent, zktermEdit, extra={"event.action": "__init__"})
            zktermEdit.setFont(QFont("Arial",10))
            reg_ex = QRegExp('^.{0,40}$')
            input_validator = QRegExpValidator(reg_ex, zktermEdit)
            zktermEdit.setValidator(input_validator)
            zktermEdit.textChanged.connect(self.zktermChanged)
         
            lbl1 = QLabel('Zoekterm')  
            logger.debug("__init__(parent=%s): lbl1 → %s", parent, lbl1, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl1 → %s", self, parent, lbl1, extra={"event.action": "__init__"})
            lbl1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                           
            grid.addWidget(k0Edit, 2, 1)   
            grid.addWidget(lbl1, 3, 0)
            grid.addWidget(zktermEdit, 3, 1)
            
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 5, 0, 1, 3, Qt.AlignCenter)
    
            applyBtn = QPushButton('Zoeken')
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn, extra={"event.action": "__init__"})
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 4, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(110)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Sluiten')
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn, extra={"event.action": "__init__"})
            cancelBtn.clicked.connect(lambda: windowSluit(self,m_email))
    
            grid.addWidget(cancelBtn, 4, 0 , 1 , 2, Qt.AlignCenter)
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(110)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
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
            dialog = Widget(parent)
            dialog.exec_()
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
    toonOrders(keuze, zoekterm, m_email)  

def selectRow(index):
    logger.warning(">>> Entering selectRow(index=%s)", index, extra={"event.action": "selectRow", "logrite.index": index})
    #print('Recordnummer is: ', index.row())
    pass  
    logger.debug("<<< Exiting selectRow(index=%s)", index, extra={"event.action": "selectRow", "logrite.index": index})
       
def toonOrders(keuze, zoekterm, m_email):
    logger.warning(">>> Entering toonOrders(keuze=%s,zoekterm=%s,m_email=%s)", keuze, zoekterm, m_email, extra={"event.action": "toonOrders", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
    import validZt                       
    logger.error("Exception in toonOrders(keuze=%s,zoekterm=%s,m_email=%s)", keuze, zoekterm, m_email, exc_info=True, extra={"event.action": "toonOrders", "event.category": "process", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
    class MyWindow(QDialog):
        logger.debug("<<< Exiting toonOrders(keuze=%s,zoekterm=%s,m_email=%s)", keuze, zoekterm, m_email, extra={"event.action": "toonOrders", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
        def __init__(self, data_list, header, *args):
            logger.warning(">>> Entering __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})
            QWidget.__init__(self, *args,)
            self.setWindowTitle('Wijzigen interne orders')
            self.setWindowFlags(self.windowFlags()| Qt.WindowSystemMenuHint |
                    Qt.WindowMinMaxButtonsHint)
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
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
            table_view.clicked.connect(wijzigOrder)
            #table_view.clicked.connect(selectRow)
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
            logger.debug("__init__(): self.lbl → %s", self.lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.pixmap → %s", self.pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl → %s", self, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.logo → %s", self.logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): logo → %s", self, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Werkordernummer → %s", self.Werkordernummer, extra={"event.action": "__init__"})
            logger.debug("__init__(): q1Edit → %s", q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q1Edit → %s", self, q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Omschrijving → %s", self.Omschrijving, extra={"event.action": "__init__"})
            logger.debug("__init__(): q2Edit → %s", q2Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q2Edit → %s", self, q2Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Voorgangstatus → %s", self.Voorgangstatus, extra={"event.action": "__init__"})
            logger.debug("__init__(): q3Edit → %s", q3Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q3Edit → %s", self, q3Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): font → %s", font, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): font → %s", self, font, extra={"event.action": "__init__"})
            logger.debug("__init__(): reg_ex → %s", reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): reg_ex → %s", self, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(): input_validator → %s", input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): input_validator → %s", self, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Startdatum → %s", self.Startdatum, extra={"event.action": "__init__"})
            logger.debug("__init__(): q4Edit → %s", q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q4Edit → %s", self, q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Afgemeld → %s", self.Afgemeld, extra={"event.action": "__init__"})
            logger.debug("__init__(): q5Edit → %s", q5Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q5Edit → %s", self, q5Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Gereed → %s", self.Gereed, extra={"event.action": "__init__"})
            logger.debug("__init__(): q6Edit → %s", q6Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q6Edit → %s", self, q6Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Goedgekeurd → %s", self.Goedgekeurd, extra={"event.action": "__init__"})
            logger.debug("__init__(): q7Edit → %s", q7Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q7Edit → %s", self, q7Edit, extra={"event.action": "__init__"})
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
            logger.debug("__init__(): lbl7 → %s", lbl7, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl7 → %s", self, lbl7, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl8 → %s", lbl8, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl8 → %s", self, lbl8, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl9 → %s", lbl9, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl9 → %s", self, lbl9, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl10 → %s", lbl10, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl10 → %s", self, lbl10, extra={"event.action": "__init__"})
            logger.debug("__init__(): wijzig → %s", wijzig, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): wijzig → %s", self, wijzig, extra={"event.action": "__init__"})
            logger.debug("__init__(): sluit → %s", sluit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): sluit → %s", self, sluit, extra={"event.action": "__init__"})
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
             
    header = ['Werkorder', 'Omschrijving','Artikelnummer','Hoeveelheid',\
               'Werkbrief','Besteldatum', 'Voortgangstatus','Statusweek','Boekdatum',\
               'Startdatum', 'Afgemeld', 'Begroot Totaal','Werkelijk Totaal',\
               'Begroot Materialen','Werkelijk Materialen','Begroot Lonen',\
               'Werkelijk Lonen', 'Meerminderwerk', 'Szagen','Bzagen', 'Wzagen',\
               'Sschaven','Bschaven', 'Wschaven', 'Ssteken','Bsteken', 'Wsteken',\
               'Sboren','Bboren', 'Wboren','Sfrezen','Bfrezen','WFrezen',\
               'Sdraaien klein', 'Bdraaien klein','Wdraaien klein','Sdraaien groot',\
               'Bdraaien groot','Wdraaien groot','Stappen','Btappen','Wtappen',\
               'Snube draaien','Bnube draaien','Wnube draaien','Snube bewerken',\
               'Bnube bewerken', 'Wnube bewerken', 'Sknippen','Bknippen', 'Wknippen',\
               'Skanten', 'Bkanten', 'Wkanten','Sstansen','Bstansen', 'Wstansen',\
               'Slassen Co2', 'Blassen Co2', 'Wlassen Co2','Slassen hand','Blassen hand',\
               'Wlassen hand','Sverpakken','Bverpakken','Wverpakken', 'Sverzinken',\
               'Bverzinken','Wverzinken','Smoffelen','Bmoffelen', 'Wmoffelen',\
               'Sschilderen','Bschilderen', 'Wschilderen','Sspuiten','Bspuiten',\
               'Wspuiten','Sponsen','Bponsen', 'Wponsen','Spersen','Bpersen',\
               'Wpersen','Sgritstralen','Bgritstralen','Wgritstralen','Smontage',\
               'Bmontage','Wmontage', 'Wreisuren','Gereed', 'Goedgekeurd']
    
    metadata = MetaData()
    orders_intern = Table('orders_intern', metadata,
        Column('werkorderID', Integer(), primary_key=True),
        Column('werkomschrijving', String),
        Column('artikelID', None, ForeignKey('artikelen.artikelID')),
        Column('hoeveelheid', Float),
        Column('werkbrief', String),
        Column('besteldatum', String),
        Column('voortgangstatus', String),
        Column('statusweek', String),
        Column('boekdatum', String),
        Column('startdatum', String),
        Column('afgemeld', String),
        Column('begroot_totaal', Float),
        Column('werk_totaal', Float),
        Column('begr_materialen', Float),
        Column('werk_materialen', Float),
        Column('begr_lonen', Float),
        Column('werk_lonen', Float),
        Column('meerminderwerk', Float),
        Column('szagen', Float),
        Column('bzagen', Float),
        Column('wzagen', Float),
        Column('sschaven', Float),
        Column('bschaven', Float),
        Column('wschaven', Float),
        Column('ssteken', Float),
        Column('bsteken', Float),
        Column('wsteken', Float),
        Column('sboren', Float),
        Column('bboren', Float),
        Column('wboren', Float),
        Column('sfrezen', Float),       
        Column('bfrezen', Float),
        Column('wfrezen', Float),
        Column('sdraaien_klein', Float),
        Column('bdraaien_klein', Float),
        Column('wdraaien_klein', Float),
        Column('sdraaien_groot', Float),        
        Column('bdraaien_groot', Float),
        Column('wdraaien_groot', Float),
        Column('stappen', Float),
        Column('btappen', Float),
        Column('wtappen', Float),
        Column('snube_draaien', Float),
        Column('bnube_draaien', Float),
        Column('wnube_draaien', Float),
        Column('snube_bewerken', Float),
        Column('bnube_bewerken', Float),
        Column('wnube_bewerken', Float),
        Column('sknippen', Float),
        Column('bknippen', Float),
        Column('wknippen', Float),
        Column('skanten', Float),
        Column('bkanten', Float),
        Column('wkanten', Float),
        Column('sstansen', Float),
        Column('bstansen', Float),
        Column('wstansen', Float),
        Column('slassen_co2', Float),
        Column('blassen_co2', Float),
        Column('wlassen_co2', Float),
        Column('slassen_hand', Float),
        Column('blassen_hand', Float),
        Column('wlassen_hand', Float),
        Column('sverpakken', Float),
        Column('bverpakken', Float),
        Column('wverpakken', Float),
        Column('sverzinken', Float),
        Column('bverzinken', Float),
        Column('wverzinken', Float),
        Column('smoffelen', Float),       
        Column('bmoffelen', Float),
        Column('wmoffelen', Float),
        Column('sschilderen', Float),
        Column('bschilderen', Float),
        Column('wschilderen', Float),
        Column('sspuiten', Float),
        Column('bspuiten', Float),
        Column('wspuiten', Float),
        Column('sponsen', Float),
        Column('bponsen', Float),
        Column('wponsen', Float),
        Column('spersen', Float),
        Column('bpersen', Float),
        Column('wpersen', Float),
        Column('sgritstralen', Float),
        Column('bgritstralen', Float),
        Column('wgritstralen', Float),
        Column('smontage', Float),
        Column('bmontage', Float),
        Column('wmontage', Float),
        Column('werk_reis_uren', Float),
        Column('gereed', Float),
        Column('goedgekeurd', Float))
       
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
        
    if keuze == 1:
        sel = select([orders_intern]).order_by(orders_intern.c.werkorderID)
    elif keuze == 2 and validZt.zt(zoekterm, 7):
        sel = select([orders_intern]).where(orders_intern.c.werkorderID== int(zoekterm))
    elif keuze == 3 and validZt.zt(zoekterm, 2):
        sel = select([orders_intern]).where(orders_intern.c.artikelID == int(zoekterm))
    elif keuze == 4 and validZt.zt(zoekterm, 10):
        sel = select([orders_intern]).where(orders_intern.c.startdatum == (zoekterm+'%'))
    elif keuze == 5 and validZt.zt(zoekterm, 10):
        sel = select([orders_intern]).where(orders_intern.c.afgemeld == (zoekterm+'%'))
    elif keuze == 6 and validZt.zt(zoekterm, 18):
        sel = select([orders_intern]).where(orders_intern.c.voortgangstatus == (zoekterm.upper()[0]))
    elif keuze == 7:
        sel = select([orders_intern]).where(orders_intern.c.werkomschrijving.ilike('%'+zoekterm+'%'))
    else:
        ongInvoer()
        zoeken(m_email)
        
    if con.execute(sel).fetchone():
        rp = con.execute(sel)
    else:
        geenRecord()
        zoeken(m_email)
    data_list=[]
    for row in rp:
        data_list += [(row)]
        
    def wijzigOrder(idx):
        logger.warning(">>> Entering wijzigOrder(idx=%s)", idx, extra={"event.action": "wijzigOrder", "logrite.idx": idx})
        mwerkorder = idx.data()
        logger.debug("wijzigOrder(idx=%s): mwerkorder → %s", idx, mwerkorder, extra={"event.action": "wijzigOrder", "logrite.idx": idx})
        if  idx.column() == 0:
            metadata = MetaData()
            logger.debug("wijzigOrder(idx=%s): metadata → %s", idx, metadata, extra={"event.action": "wijzigOrder", "logrite.idx": idx})
            orders_intern = Table('orders_intern', metadata,
                Column('werkorderID', Integer(), primary_key=True),
                Column('werkomschrijving', String),
                Column('besteldatum', String),
                Column('voortgangstatus', String),
                Column('statusweek', String),
                Column('boekdatum', String),
                Column('startdatum', String),
                Column('afgemeld', String),
                Column('begroot_totaal', Float),
                Column('werk_totaal', Float),
                Column('begr_materialen', Float),
                Column('werk_materialen', Float),
                Column('begr_lonen', Float),
                Column('werk_lonen', Float),
                Column('meerminderwerk', Float),
                Column('werk_reis_uren', Float),
                Column('artikelID', None, ForeignKey('artikelen.c.artikelID')),
                Column('hoeveelheid', Float),
                Column('goedgekeurd', Float),
                Column('gereed', Float))
            artikelen = Table('artikelen', metadata,
                Column('artikelID', Integer(), primary_key=True),
                Column('art_voorraad', Float),
                Column('bestelstatus'),
                Column('artikelprijs', Float),
                Column('bestelsaldo', Float))
            artikelmutaties = Table('artikelmutaties', metadata,
                Column('mutatieID', Integer, primary_key=True),
                Column('artikelID', None, ForeignKey('artikelen.artikelID')),
                Column('orderinkoopID', None, ForeignKey('orders_inkoop.orderinkoopID')),
                Column('hoeveelheid', Float),
                Column('boekdatum', String),
                Column('tot_mag_prijs', Float),
                Column('btw_hoog', Float),
                Column('werkorderID', Integer))
            
            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            logger.debug("wijzigOrder(idx=%s): engine → %s", idx, engine, extra={"event.action": "wijzigOrder", "logrite.idx": idx})
            con = engine.connect()
            logger.debug("wijzigOrder(idx=%s): con → %s", idx, con, extra={"event.action": "wijzigOrder", "logrite.idx": idx})
            selord = select([orders_intern]).where(orders_intern.c.werkorderID == mwerkorder)
            logger.debug("wijzigOrder(idx=%s): selord → %s", idx, selord, extra={"event.action": "wijzigOrder", "logrite.idx": idx})
            rpord = con.execute(selord).first()
            logger.debug("wijzigOrder(idx=%s): rpord → %s", idx, rpord, extra={"event.action": "wijzigOrder", "logrite.idx": idx})
        
            logger.error("Exception in wijzigOrder(idx=%s)", idx, exc_info=True, extra={"event.action": "wijzigOrder", "event.category": "process", "logrite.idx": idx})
            class Widget(QDialog):
                logger.debug("<<< Exiting wijzigOrder(idx=%s)", idx, extra={"event.action": "wijzigOrder", "logrite.idx": idx})
                def __init__(self):
                    QDialog.__init__(self)
                    
                    grid = QGridLayout()
                    grid.setSpacing(12)
                    
                    self.setWindowTitle("Wijzigen Werkorders Intern")
                    self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
                      
                    self.setFont(QFont('Arial', 10))   
                                                      
                    self.lbl = QLabel()
                    self.pixmap = QPixmap('./images/logos/verbinding.jpg')
                    self.lbl.setPixmap(self.pixmap)
                    grid.addWidget(self.lbl , 0, 0)
                    
                    self.logo = QLabel()
                    self.pixmap = QPixmap('./images/logos/logo.jpg')
                    self.logo.setPixmap(self.pixmap)
                    grid.addWidget(self.logo , 0, 1, 1, 2, Qt.AlignRight) 
                    
                    grid.addWidget(QLabel('Wijzigen Orders Intern'), 0, 0, 1, 3, Qt.AlignCenter)
                        
                    self.Werkordernummer = QLabel()
                    q1Edit = QLineEdit(str(rpord[0]))
                    q1Edit.setFixedWidth(100)
                    q1Edit.setAlignment(Qt.AlignRight)
                    q1Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q1Edit.setDisabled(True)
                    q1Edit.setFont(QFont("Arial",10))
                 
                    self.Omschrijving = QLabel()
                    q2Edit = QLineEdit(str(rpord[1]))
                    q2Edit.setFixedWidth(400)
                    q2Edit.setFont(QFont("Arial",10))
                    q2Edit.textChanged.connect(self.q2Changed)
                    
                    self.Voorgangstatus = QLabel()
                    q3Edit = QLineEdit(str(rpord[3]))
                    q3Edit.setFixedWidth(20)
                    font = QFont("Arial",10)
                    font.setCapitalization(QFont.AllUppercase)
                    q3Edit.setFont(font)
                    if str(rpord[3]) < 'G':
                        q3Edit.setDisabled(True)
                        q3Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q3Edit.textChanged.connect(self.q3Changed)
                    reg_ex = QRegExp('^[A-Ha-h]{1}$')
                    input_validator = QRegExpValidator(reg_ex, q3Edit)
                    q3Edit.setValidator(input_validator)
                                   
                    self.Startdatum = QLabel()
                    q4Edit = QLineEdit(str(rpord[6]))
                    q4Edit.setFixedWidth(100)
                    q4Edit.setFont(QFont("Arial",10))
                    q4Edit.textChanged.connect(self.q4Changed)
                    reg_ex = QRegExp('^[2]{1}[0]{1}[0-9]{2}[-]{1}[0-1]{1}[0-9]{1}[-]{1}[0-3]{1}[0-9]{1}$')
                    input_validator = QRegExpValidator(reg_ex, q4Edit)
                    q4Edit.setValidator(input_validator)
                                            
                    self.Afgemeld = QLabel()
                    q5Edit = QLineEdit(str(rpord[7]))
                    q5Edit.setFixedWidth(100)
                    q5Edit.setFont(QFont("Arial",10))
                    q5Edit.textChanged.connect(self.q5Changed)
                    reg_ex = QRegExp('^[2]{1}[0]{1}[0-9]{2}[-]{1}[0-1]{1}[0-9]{1}[-]{1}[0-3]{1}[0-9]{1}$')
                    input_validator = QRegExpValidator(reg_ex, q5Edit)
                    q5Edit.setValidator(input_validator)
                  
                    self.Gereed = QLabel()
                    q6Edit = QLineEdit(str(round(float(rpord[19]),2)))
                    q6Edit.setFixedWidth(100)
                    q6Edit.setFont(QFont("Arial",10))
                    q6Edit.setAlignment(Qt.AlignRight)
                    q6Edit.textChanged.connect(self.q6Changed)
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q6Edit)
                    q6Edit.setValidator(input_validator)
                                    
                    self.Goedgekeurd = QLabel()
                    q7Edit = QLineEdit(str(round(float(rpord[18]),2)))
                    q7Edit.setFixedWidth(100)
                    q7Edit.setFont(QFont("Arial",10))
                    q7Edit.setAlignment(Qt.AlignRight)
                    q7Edit.textChanged.connect(self.q7Changed)
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q7Edit)
                    q7Edit.setValidator(input_validator)
                    
                    lbl1 = QLabel('Werkordernummer')
                    grid.addWidget(lbl1, 1, 0)
                    grid.addWidget(q1Edit, 1, 1)
                    
                    lbl2 = QLabel('Werkomschrijving')
                    grid.addWidget(lbl2, 2, 0)
                    grid.addWidget(q2Edit, 2, 1, 1, 2)
                    
                    lbl3 = QLabel('Voorgangstatus')
                    grid.addWidget(lbl3, 3, 0)
                    grid.addWidget(q3Edit, 3, 1)
                    lbl4 = QLabel('Statusweek: '+rpord[4])
                    grid.addWidget(lbl4, 3, 1, 1, 2, Qt.AlignRight)
                    
                    lbl5 = QLabel('Startdatum')
                    grid.addWidget(lbl5, 4, 0)
                    grid.addWidget(q4Edit, 4, 1)
                    
                    lbl6 = QLabel('Afgemeld')
                    grid.addWidget(lbl6, 5, 0)
                    grid.addWidget(q5Edit, 5, 1)
                    
                    lbl7 = QLabel('Hoeveelheid\nGereed')
                    grid.addWidget(lbl7, 6, 0)
                    grid.addWidget(q6Edit, 6, 1)
                    lbl8 = QLabel('                           Artikel: '+str(rpord[16]))
                    grid.addWidget(lbl8, 5, 1, 1, 2, Qt.AlignRight)
                    lbl9 = QLabel('                 Bestelhoeveelheid: '+'{:12.2f}'.format(rpord[17]))
                    grid.addWidget(lbl9, 6, 1, 1, 2, Qt.AlignRight)
                    
                    lbl10 = QLabel('Hoeveelheid\nGoedgekeurd')
                    grid.addWidget(lbl10, 7, 0)
                    grid.addWidget(q7Edit, 7, 1)
              
                    wijzig = QPushButton('Wijzig')
                    wijzig.clicked.connect(self.accept)
    
                    grid.addWidget(wijzig, 9, 2, 1 , 1, Qt.AlignRight)
                    wijzig.setFont(QFont("Arial",10))
                    wijzig.setFixedWidth(100)
                    
                    sluit = QPushButton('Sluiten')
                    sluit.clicked.connect(self.close)
    
                    grid.addWidget(sluit, 9, 1 , 1 , 2, Qt.AlignCenter)
                    sluit.setFont(QFont("Arial",10))
                    sluit.setFixedWidth(100)  
                                                   
                    grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 10, 0, 1, 3, Qt.AlignCenter)
                                                                            
                    self.setLayout(grid)
                    self.setGeometry(500, 300, 150, 150)
                    
                def q2Changed(self,text):
                    logger.warning(">>> Entering q2Changed(text=%s)", text, extra={"event.action": "q2Changed", "logrite.text": text})
                    self.Omschrijving.setText(text)
                    logger.debug("<<< Exiting q2Changed(text=%s)", text, extra={"event.action": "q2Changed", "logrite.text": text})
            
                def q3Changed(self,text):
                    logger.warning(">>> Entering q3Changed(text=%s)", text, extra={"event.action": "q3Changed", "logrite.text": text})
                    self.Voortgangstatus.setText(text)
                    logger.debug("<<< Exiting q3Changed(text=%s)", text, extra={"event.action": "q3Changed", "logrite.text": text})
            
                def q4Changed(self,text):
                    logger.warning(">>> Entering q4Changed(text=%s)", text, extra={"event.action": "q4Changed", "logrite.text": text})
                    self.Startdatum.setText(text)
                    logger.debug("<<< Exiting q4Changed(text=%s)", text, extra={"event.action": "q4Changed", "logrite.text": text})
                    
                def q5Changed(self,text):
                    logger.warning(">>> Entering q5Changed(text=%s)", text, extra={"event.action": "q5Changed", "logrite.text": text})
                    self.Afgemeld.setText(text)
                    logger.debug("<<< Exiting q5Changed(text=%s)", text, extra={"event.action": "q5Changed", "logrite.text": text})

                def q6Changed(self,text):
                    logger.warning(">>> Entering q6Changed(text=%s)", text, extra={"event.action": "q6Changed", "logrite.text": text})
                    self.Gereed.setText(text)
                    logger.debug("<<< Exiting q6Changed(text=%s)", text, extra={"event.action": "q6Changed", "logrite.text": text})
                               
                def q7Changed(self,text):
                    logger.warning(">>> Entering q7Changed(text=%s)", text, extra={"event.action": "q7Changed", "logrite.text": text})
                    self.Goedgekeurd.setText(text)
                    logger.debug("<<< Exiting q7Changed(text=%s)", text, extra={"event.action": "q7Changed", "logrite.text": text})
              
                def returnq2(self):
                    logger.warning(">>> Entering returnq2()", extra={"event.action": "returnq2"})
                    logger.debug("<<< Exiting returnq2()", extra={"event.action": "returnq2"})
                    return self.Omschrijving.text()
                
                def returnq3(self):
                    logger.warning(">>> Entering returnq3()", extra={"event.action": "returnq3"})
                    logger.debug("<<< Exiting returnq3()", extra={"event.action": "returnq3"})
                    return self.Voorgangstatus.text()
                
                def returnq4(self):
                    logger.warning(">>> Entering returnq4()", extra={"event.action": "returnq4"})
                    logger.debug("<<< Exiting returnq4()", extra={"event.action": "returnq4"})
                    return self.Startdatum.text()
                    
                def returnq5(self):
                    logger.warning(">>> Entering returnq5()", extra={"event.action": "returnq5"})
                    logger.debug("<<< Exiting returnq5()", extra={"event.action": "returnq5"})
                    return self.Afgemeld.text()
                
                def returnq6(self):
                    logger.warning(">>> Entering returnq6()", extra={"event.action": "returnq6"})
                    logger.debug("<<< Exiting returnq6()", extra={"event.action": "returnq6"})
                    return self.Gereed.text()
                      
                def returnq7(self):
                    logger.warning(">>> Entering returnq7()", extra={"event.action": "returnq7"})
                    logger.debug("<<< Exiting returnq7()", extra={"event.action": "returnq7"})
                    return self.Goedgekeurd.text()
                
                @staticmethod
                def getData(parent=None):
                    logger.warning(">>> Entering getData(parent=%s)", parent, extra={"event.action": "getData"})
                    dialog = Widget()
                    logger.debug("getData(parent=%s): dialog → %s", parent, dialog, extra={"event.action": "getData"})
                    dialog.exec_()
                    logger.debug("<<< Exiting getData(parent=%s)", parent, extra={"event.action": "getData"})
                    return [dialog.returnq2(), dialog.returnq3(), dialog.returnq4(),\
                            dialog.returnq5(), dialog.returnq6(), dialog.returnq7()]  
                            
            window = Widget()
            data = window.getData()
            if not(data[0] or data[1] or data[2] or data[3] or data[4] or data[5]):       
                return()
            if data[0]:
                momschr = data[0]
            else:
                momschr = rpord[1]
            if data[1]:
                mvgst = data[1]
            else:
                mvgst = rpord[3]
            if data[2]:
                mstart = data[2]
            else:
                mstart = rpord[6]
            if data[3]:
                mafgem = data[3]
            else:
                mafgem = rpord[7]
            if data[4]:
                mgereed = float(data[4])
            else:
                mgereed = rpord[19]
            if data[5]:
                mgoedg = float(data[5])
            else:
                mgoedg = rpord[18]
            mboekd = str(datetime.datetime.now())[0:10] 
            mgoedgversch = mgoedg - rpord[18]
            
            updio = update(orders_intern).where(orders_intern.c.werkorderID == mwerkorder)\
             .values(werkomschrijving = momschr, voortgangstatus = mvgst, startdatum = mstart,\
                    afgemeld = mafgem, boekdatum = mboekd, gereed = mgereed, goedgekeurd = mgoedg)
            con.execute(updio)
            updart = update(artikelen).where(and_(orders_intern.c.werkorderID == mwerkorder,\
              orders_intern.c.artikelID == artikelen.c.artikelID)).values(art_voorraad =\
              artikelen.c.art_voorraad + mgoedgversch, bestelsaldo = artikelen.c.bestelsaldo -\
              mgoedgversch)
            con.execute(updart)
            try:
                mutnr=(con.execute(select([func.max(artikelmutaties.c.mutatieID,\
                        type_=Integer)])).scalar())
                mutnr += 1
            except:
                mutnr = 1
            params_finance = Table('params_finance', metadata,
                                   Column('financeID', Integer, primary_key=True),
                                   Column('factor', Float),
                                   Column('item', String))

            selpar = select([params_finance]).order_by(params_finance.c.financeID)
            rppar = con.execute(selpar).fetchall()
            selart = select([artikelen]).where(rpord[16] == artikelen.c.artikelID)
            rpart = con.execute(selart).first()
            martprijs = rpart[3]

            ins = insert(artikelmutaties).values(mutatieID=mutnr, artikelID= \
                rpord[16], werkorderID=mwerkorder, hoeveelheid=mgoedgversch, \
                                                 boekdatum=mboekd, tot_mag_prijs=mgoedgversch * martprijs, \
                                                 btw_hoog=mgoedgversch * martprijs * (rppar[0][1]))
            con.execute(ins)
            invoerOK()
     
    win = MyWindow(data_list, header)
    win.exec_()
    zoeken(m_email)