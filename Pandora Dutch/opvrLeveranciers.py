from login import hoofdMenu
from postcode import checkpostcode
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import  QLabel, QPushButton, QWidget, QGridLayout,\
       QComboBox, QDialog, QLineEdit, QMessageBox, QTableView, QVBoxLayout
from sqlalchemy import (Table, Column, Integer, String, MetaData,\
                        create_engine)
from sqlalchemy.sql import select, desc
import logging
logger = logging.getLogger(__name__)

def ongInvoer():
    logger.warning(">>> Entering ongInvoer()", extra={"event.action": "ongInvoer"})
    msg = QMessageBox()
    logger.debug("ongInvoer(): msg → %s", msg, extra={"event.action": "ongInvoer"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Information)
    msg.setText('Foutieve invoer\nzoekterm opnieuw invoeren s.v.p.!')
    msg.setWindowTitle('Leveranciers opvragen')               
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
    msg.setWindowTitle('Leveranciers opvragen')               
    logger.debug("<<< Exiting geenRecord()", extra={"event.action": "geenRecord"})
    msg.exec_() 
    
def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})

def leveranciersKeuze(m_email):
    logger.warning(">>> Entering leveranciersKeuze(m_email=%s)", m_email, extra={"event.action": "leveranciersKeuze"})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            self.setWindowTitle("Leveranciers Overzicht")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Times', 10))
    
            self.Keuze4 = QLabel()
            logger.debug("__init__(parent=%s): self.Keuze4 → %s", parent, self.Keuze4, extra={"event.action": "__init__"})
            k4Edit = QComboBox()
            logger.debug("__init__(self=%s,parent=%s): k4Edit → %s", self, parent, k4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): k4Edit → %s", parent, k4Edit, extra={"event.action": "__init__"})
            k4Edit.setFixedWidth(230)
            k4Edit.setFont(QFont("Times", 10))
            k4Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k4Edit.addItem(' Sorteersleutel voor zoeken')
            k4Edit.addItem('1. Alle Leveranciers')
            k4Edit.addItem('2. Bedrijfsnaam')
            k4Edit.addItem('3. Leveranciernummer.')
            k4Edit.activated[str].connect(self.k4Changed)
            
            self.Zoekterm = QLabel()
            logger.debug("__init__(parent=%s): self.Zoekterm → %s", parent, self.Zoekterm, extra={"event.action": "__init__"})
            zktermEdit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): zktermEdit → %s", self, parent, zktermEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): zktermEdit → %s", parent, zktermEdit, extra={"event.action": "__init__"})
            zktermEdit.setFixedWidth(220)
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
                                  
            grid.addWidget(k4Edit, 2, 1)
            lbl1 = QLabel('Zoekterm')  
            logger.debug("__init__(parent=%s): lbl1 → %s", parent, lbl1, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl1 → %s", self, parent, lbl1, extra={"event.action": "__init__"})
            lbl1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl1, 3, 0)
            grid.addWidget(zktermEdit, 3, 1)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 5, 0, 1, 2,Qt.AlignCenter)
            
            logo = QLabel()
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 1, 1, 1, Qt.AlignRight)
            
            self.setLayout(grid)
            self.setGeometry(600, 300, 150, 150)
    
            applyBtn = QPushButton('Zoeken')
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn, extra={"event.action": "__init__"})
            applyBtn.clicked.connect(self.accept)
                
            grid.addWidget(applyBtn, 4, 1, 1 , 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial", 10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Sluiten')
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn, extra={"event.action": "__init__"})
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
    
            grid.addWidget(cancelBtn, 4, 1)
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            cancelBtn.setFont(QFont("Arial", 10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
                   
        def k4Changed(self, text):
            logger.warning(">>> Entering k4Changed(text=%s)", text, extra={"event.action": "k4Changed", "logrite.text": text})
            self.Keuze4.setText(text)
            logger.debug("<<< Exiting k4Changed(text=%s)", text, extra={"event.action": "k4Changed", "logrite.text": text})
            
        def zktermChanged(self, text):
            logger.warning(">>> Entering zktermChanged(text=%s)", text, extra={"event.action": "zktermChanged", "logrite.text": text})
            self.Zoekterm.setText(text)
            logger.debug("<<< Exiting zktermChanged(text=%s)", text, extra={"event.action": "zktermChanged", "logrite.text": text})
 
        def returnk4(self):
            logger.warning(">>> Entering returnk4()", extra={"event.action": "returnk4"})
            logger.debug("<<< Exiting returnk4()", extra={"event.action": "returnk4"})
            return self.Keuze4.text()
        
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
            return [dialog.returnk4(), dialog.returnzkterm()]       

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
    toonLeveranciers(keuze, zoekterm, m_email)

def toonLeveranciers(keuze,zoekterm, m_email):
    logger.warning(">>> Entering toonLeveranciers(keuze=%s,zoekterm=%s,m_email=%s)", keuze, zoekterm, m_email, extra={"event.action": "toonLeveranciers", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
    import validZt
    metadata = MetaData()
    logger.debug("toonLeveranciers(keuze=%s,zoekterm=%s,m_email=%s): metadata → %s", keuze, zoekterm, m_email, metadata, extra={"event.action": "toonLeveranciers", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
    leveranciers = Table('leveranciers', metadata,
        Column('leverancierID', Integer(), primary_key=True),
        Column('bedrijfsnaam', String),
        Column('rechtsvorm', String),
        Column('btwnummer', String),
        Column('kvknummer', String),
        Column('telnr', String),
        Column('postcode', String),  
        Column('huisnummer', String),
        Column('toevoeging', String))
                          
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("toonLeveranciers(keuze=%s,zoekterm=%s,m_email=%s): engine → %s", keuze, zoekterm, m_email, engine, extra={"event.action": "toonLeveranciers", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
    con = engine.connect()
    logger.debug("toonLeveranciers(keuze=%s,zoekterm=%s,m_email=%s): con → %s", keuze, zoekterm, m_email, con, extra={"event.action": "toonLeveranciers", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
    if keuze == 1:
         sel = select([leveranciers]).order_by(desc(leveranciers.c.leverancierID)) 
    elif keuze == 2:
         sel = select([leveranciers]).where(leveranciers.c.bedrijfsnaam.ilike('%'+zoekterm+'%'))
         logger.debug("toonLeveranciers(keuze=%s,zoekterm=%s,m_email=%s): sel → %s", keuze, zoekterm, m_email, sel, extra={"event.action": "toonLeveranciers", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
    elif keuze == 3 and validZt.zt(zoekterm, 3):
        zoekterm = int(zoekterm)
        logger.debug("toonLeveranciers(keuze=%s,zoekterm=%s,m_email=%s): zoekterm → %s", keuze, zoekterm, m_email, zoekterm, extra={"event.action": "toonLeveranciers", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
        sel = select([leveranciers]).where(leveranciers.c.leverancierID == zoekterm)
    else:
        ongInvoer()
        leveranciersKeuze(m_email)
        
    if con.execute(sel).fetchone():
        rplev = con.execute(sel)
    else:
        logger.debug("toonLeveranciers(keuze=%s,zoekterm=%s,m_email=%s): rplev → %s", keuze, zoekterm, m_email, rplev, extra={"event.action": "toonLeveranciers", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
        geenRecord()
        leveranciersKeuze(m_email)
     
    class MyWindow(QDialog):
        logger.debug("<<< Exiting toonLeveranciers(keuze=%s,zoekterm=%s,m_email=%s)", keuze, zoekterm, m_email, extra={"event.action": "toonLeveranciers", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
        def __init__(self, data_list, header, *args):
            logger.warning(">>> Entering __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})
            QWidget.__init__(self, *args,)
            self.setGeometry(50, 50, 1500, 900)
            self.setWindowTitle('Leveranciers opvragen')
            self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
            self.setWindowFlags(self.windowFlags()| Qt.WindowSystemMenuHint |
                              Qt.WindowMinMaxButtonsHint)
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
            #table_view.clicked.connect(showLeverancier)
            layout = QVBoxLayout(self)
            logger.debug("__init__(data_list=%s,header=%s): layout → %s", data_list, header, layout, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): layout → %s", self, data_list, header, layout, extra={"event.action": "__init__", "logrite.data_list": data_list})
            layout.addWidget(table_view)
            self.setLayout(layout)
            logger.debug("<<< Exiting __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})
    
    class MyTableModel(QAbstractTableModel):
        def __init__(self, parent, mylist, header, *args):
            logger.warning(">>> Entering __init__(parent=%s,mylist=%s,header=%s)", parent, mylist, header, extra={"event.action": "__init__", "logrite.mylist": mylist})
            logger.debug("__init__(self=%s,parent=%s,mylist=%s,header=%s): self.mylist → %s", self, parent, mylist, header, self.mylist, extra={"event.action": "__init__", "logrite.mylist": mylist})
            logger.debug("__init__(self=%s,parent=%s,mylist=%s,header=%s): self.header → %s", self, parent, mylist, header, self.header, extra={"event.action": "__init__", "logrite.mylist": mylist})
            QAbstractTableModel.__init__(self, parent, *args)
            logger.debug("<<< Exiting __init__(parent=%s,mylist=%s,header=%s)", parent, mylist, header, extra={"event.action": "__init__", "logrite.mylist": mylist})
            self.mylist = mylist
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
  
    header = ['Leveranciernummer','Bedrijfsnaam', 'Rechtsvorm','BTWnummer',\
              'KvKnummer','Telefoonnummer','Straat', 'Huisnummer','Toevoeging',\
              'Postcode','Woonplaats']  
  
    data_list=[]
    for row in rplev:
        mstrtplts = checkpostcode(row[6], int(row[7]))
        data_list += [(row[0],row[1],row[2],row[3],row[4],row[5],mstrtplts[0],int(row[7]),\
                      row[8],row[6], mstrtplts[1])] 
        
    win = MyWindow(data_list, header)
    win.exec_()
    leveranciersKeuze(m_email)  
