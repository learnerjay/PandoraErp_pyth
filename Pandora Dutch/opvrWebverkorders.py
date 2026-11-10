from login import hoofdMenu
from postcode import checkpostcode
import os, datetime
from PyQt5.QtCore import Qt, QAbstractTableModel, QRegExp
from PyQt5.QtGui import QFont, QPixmap, QIcon, QRegExpValidator
from PyQt5.QtWidgets import  QDialog, QLabel, QGridLayout,\
                             QPushButton, QLineEdit, QWidget, QMessageBox,\
                             QTableView, QComboBox, QCheckBox
from sqlalchemy import (Table, Column, Integer, String, MetaData,\
                         create_engine, Float, ForeignKey)
from sqlalchemy.sql import select, update, and_
import logging
logger = logging.getLogger(__name__)

def refresh(m_email, keuze, zoekterm, afd, self):
    logger.warning(">>> Entering refresh(m_email=%s,keuze=%s,zoekterm=%s,afd=%s)", m_email, keuze, zoekterm, afd, extra={"event.action": "refresh", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm, "logrite.afd": afd})
    self.close()
    bestelOrder(m_email, keuze, zoekterm, afd)
    logger.debug("<<< Exiting refresh(m_email=%s,keuze=%s,zoekterm=%s,afd=%s)", m_email, keuze, zoekterm, afd, extra={"event.action": "refresh", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm, "logrite.afd": afd})

def ongInvoer():
    logger.warning(">>> Entering ongInvoer()", extra={"event.action": "ongInvoer"})
    msg = QMessageBox()
    logger.debug("ongInvoer(): msg → %s", msg, extra={"event.action": "ongInvoer"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Foutieve invoer\nzoekterm opnieuw invoeren s.v.p.!')
    msg.setWindowTitle('Webverkooporders opvragen')               
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
    msg.setWindowTitle('Webverkooporders opvragen')               
    logger.debug("<<< Exiting geenRecord()", extra={"event.action": "geenRecord"})
    msg.exec_() 
    
def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})

def geenOrder():
    logger.warning(">>> Entering geenOrder()", extra={"event.action": "geenOrder"})
    msg = QMessageBox()
    logger.debug("geenOrder(): msg → %s", msg, extra={"event.action": "geenOrder"})
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Information)
    msg.setText('Webverkooporder niet gevonden!')
    msg.setWindowTitle('Webverkooporders opvragen')               
    logger.debug("<<< Exiting geenOrder()", extra={"event.action": "geenOrder"})
    msg.exec_()
     
def printing():
    logger.warning(">>> Entering printing()", extra={"event.action": "printing"})
    msg = QMessageBox()
    logger.debug("printing(): msg → %s", msg, extra={"event.action": "printing"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Information)
    msg.setText('Ogenblik afdrukken wordt gestart!')
    msg.setWindowTitle('Webverkooporders opvragen')
    logger.debug("<<< Exiting printing()", extra={"event.action": "printing"})
    msg.exec_()
    
def printFactuur(rpord,mstraat,mplaats,movbestnr):
    logger.warning(">>> Entering printFactuur(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s)", rpord, mstraat, mplaats, movbestnr, extra={"event.action": "printFactuur", "logrite.rpord": rpord, "logrite.mstraat": mstraat, "logrite.mplaats": mplaats, "logrite.movbestnr": movbestnr})
    from sys import platform
    metadata = MetaData()
    logger.debug("printFactuur(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): metadata → %s", rpord, mstraat, mplaats, movbestnr, metadata, extra={"event.action": "printFactuur", "logrite.rpord": rpord, "logrite.mstraat": mstraat, "logrite.mplaats": mplaats, "logrite.movbestnr": movbestnr})
    orders_verkoop_artikelen = Table('orders_verkoop_artikelen', metadata,
        Column('ovaID', Integer, primary_key=True),
        Column('ovbestelID', None, ForeignKey('orders_verkoop.ovbestelID')),
        Column('artikelID', None, ForeignKey('artikelen.artikelID')),
        Column('ovaantal', Integer),
        Column('ovleverdatum', String),
        Column('verkoopprijs', Float),
        Column('regel', Integer),
        Column('retour', Float),
        Column('betaaldatum', String),
        Column('leveringsdatum', String))
    logger.debug("printFactuur(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): selova → %s", rpord, mstraat, mplaats, movbestnr, selova, extra={"event.action": "printFactuur", "logrite.rpord": rpord, "logrite.mstraat": mstraat, "logrite.mplaats": mplaats, "logrite.movbestnr": movbestnr})
    artikelen = Table('artikelen', metadata,
        Column('artikelID', Integer(), primary_key=True),
        Column('artikelomschrijving', String),
        Column('artikelprijs', Float),
        Column('art_voorraad', Float),
        Column('art_eenheid', String),
        Column('locatie_magazijn', String))
        
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("printFactuur(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): engine → %s", rpord, mstraat, mplaats, movbestnr, engine, extra={"event.action": "printFactuur", "logrite.rpord": rpord, "logrite.mstraat": mstraat, "logrite.mplaats": mplaats, "logrite.movbestnr": movbestnr})
    con = engine.connect()
    logger.debug("printFactuur(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): con → %s", rpord, mstraat, mplaats, movbestnr, con, extra={"event.action": "printFactuur", "logrite.rpord": rpord, "logrite.mstraat": mstraat, "logrite.mplaats": mplaats, "logrite.movbestnr": movbestnr})
    selova = select([orders_verkoop_artikelen,artikelen]).where(and_(\
      orders_verkoop_artikelen.c.ovbestelID == movbestnr, orders_verkoop_artikelen\
      .c.artikelID == artikelen.c.artikelID)).order_by(orders_verkoop_artikelen.c.ovaID)
    rpova = con.execute(selova)
    logger.debug("printFactuur(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): rpova → %s", rpord, mstraat, mplaats, movbestnr, rpova, extra={"event.action": "printFactuur", "logrite.rpord": rpord, "logrite.mstraat": mstraat, "logrite.mplaats": mplaats, "logrite.movbestnr": movbestnr})
        
    mblad = 1
    logger.debug("printFactuur(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): mblad → %s", rpord, mstraat, mplaats, movbestnr, mblad, extra={"event.action": "printFactuur", "logrite.rpord": rpord, "logrite.mstraat": mstraat, "logrite.mplaats": mplaats, "logrite.movbestnr": movbestnr})
    rgl = 0
    if platform == 'win32':
        filename = '.\\forms\\Weborders_Facturen\\Weborder-factuur-'+str(rpord[0])+'.txt'
    else:
        filename = './forms/Weborders_Facturen/Weborder-factuur-'+str(rpord[0])+'.txt'
        logger.debug("printFactuur(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): filename → %s", rpord, mstraat, mplaats, movbestnr, filename, extra={"event.action": "printFactuur", "logrite.rpord": rpord, "logrite.mstraat": mstraat, "logrite.mplaats": mplaats, "logrite.movbestnr": movbestnr})
    adreskop=\
    ('\n\n\n\n\n\n\nFACTUUR\n\n'+rpord[10]+' '+rpord[11]+' '+rpord[12]+' '+rpord[13]+',\n'+\
     mstraat+' '+rpord[15]+rpord[16]+',\n'+\
     rpord[14]+' '+mplaats+'.\n\n\n\n\n')
    logger.debug("printFactuur(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): adreskop → %s", rpord, mstraat, mplaats, movbestnr, adreskop, extra={"event.action": "printFactuur", "logrite.rpord": rpord, "logrite.mstraat": mstraat, "logrite.mplaats": mplaats, "logrite.movbestnr": movbestnr})
    kop=\
    ('Ordernummer: '+ str(rpord[0])+'          Datum: '+str(datetime.datetime.now())[0:10]+'  Blad : '+str(mblad)+'\n'+
    '==============================================================================================\n'+
    'Artikelnr  Omschrijving                        Eenheid Aantal     Prijs   Subtotaal       BTW \n'+
    '==============================================================================================\n')
    logger.debug("printFactuur(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): kop → %s", rpord, mstraat, mplaats, movbestnr, kop, extra={"event.action": "printFactuur", "logrite.rpord": rpord, "logrite.mstraat": mstraat, "logrite.mplaats": mplaats, "logrite.movbestnr": movbestnr})
    mtotaal = 0
    logger.debug("printFactuur(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): mtotaal → %s", rpord, mstraat, mplaats, movbestnr, mtotaal, extra={"event.action": "printFactuur", "logrite.rpord": rpord, "logrite.mstraat": mstraat, "logrite.mplaats": mplaats, "logrite.movbestnr": movbestnr})
    
    for row in rpova:
        if rgl == 0 and mblad == 1:
            open(filename, 'w').write(adreskop)
            open(filename, 'a').write(kop)
            rgl = 16
        elif rgl%57 == 0:
            open(filename, 'a').write(kop)
            mblad += 1
        msub = row[3]*row[5]
        logger.debug("printFactuur(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): msub → %s", rpord, mstraat, mplaats, movbestnr, msub, extra={"event.action": "printFactuur", "logrite.rpord": rpord, "logrite.mstraat": mstraat, "logrite.mplaats": mplaats, "logrite.movbestnr": movbestnr})
        open(filename,'a').write('{:<11d}'.format(row[2])+'{:<37.35s}'.format(row[11])+\
         '{:>6s}'.format(row[14])+' '+'{:>6.2f}'.format(row[3])+'{:>10.2f}'.format(row[5])+\
         ' '+'{:>10.2f}'.format(msub)+' '+'{:>10.2f}'.format(msub*21/121)+'\n')
        mtotaal = mtotaal+msub
        rgl += 1
   
    tail =(\
           
    '----------------------------------------------------------------------------------------------\n'+
    'Totaal factuurbedrag inclusief 21% BTW                                  '+'{:10.2f}'.format(mtotaal)+' \n'+
    '==============================================================================================\n')    
    open(filename,'a').write(tail)
    if platform == 'win32':
        os.startfile(filename, "print")
    else:
        os.system("lpr "+filename)
    printing()
    logger.debug("<<< Exiting printFactuur(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s)", rpord, mstraat, mplaats, movbestnr, extra={"event.action": "printFactuur", "logrite.rpord": rpord, "logrite.mstraat": mstraat, "logrite.mplaats": mplaats, "logrite.movbestnr": movbestnr})
    
def printPakbon(rpord,mstraat,mplaats,movbestnr): 
    logger.warning(">>> Entering printPakbon(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s)", rpord, mstraat, mplaats, movbestnr, extra={"event.action": "printPakbon", "logrite.rpord": rpord, "logrite.mstraat": mstraat, "logrite.mplaats": mplaats, "logrite.movbestnr": movbestnr})
    from sys import platform
    metadata = MetaData()
    logger.debug("printPakbon(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): metadata → %s", rpord, mstraat, mplaats, movbestnr, metadata, extra={"event.action": "printPakbon", "logrite.rpord": rpord, "logrite.mstraat": mstraat, "logrite.mplaats": mplaats, "logrite.movbestnr": movbestnr})
    orders_verkoop_artikelen = Table('orders_verkoop_artikelen', metadata,
        Column('ovaID', Integer, primary_key=True),
        Column('ovbestelID', None, ForeignKey('orders_verkoop.ovbestelID')),
        Column('artikelID', None, ForeignKey('artikelen.artikelID')),
        Column('ovaantal', Integer),
        Column('ovleverdatum', String),
        Column('verkoopprijs', Float),
        Column('regel', Integer),
        Column('retour', Float),
        Column('betaaldatum', String),
        Column('leveringsdatum', String))
    logger.debug("printPakbon(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): selova → %s", rpord, mstraat, mplaats, movbestnr, selova, extra={"event.action": "printPakbon", "logrite.rpord": rpord, "logrite.mstraat": mstraat, "logrite.mplaats": mplaats, "logrite.movbestnr": movbestnr})
    artikelen = Table('artikelen', metadata,
        Column('artikelID', Integer(), primary_key=True),
        Column('artikelomschrijving', String),
        Column('artikelprijs', Float),
        Column('art_voorraad', Float),
        Column('art_eenheid', String),
        Column('locatie_magazijn', String))
        
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("printPakbon(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): engine → %s", rpord, mstraat, mplaats, movbestnr, engine, extra={"event.action": "printPakbon", "logrite.rpord": rpord, "logrite.mstraat": mstraat, "logrite.mplaats": mplaats, "logrite.movbestnr": movbestnr})
    con = engine.connect()
    logger.debug("printPakbon(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): con → %s", rpord, mstraat, mplaats, movbestnr, con, extra={"event.action": "printPakbon", "logrite.rpord": rpord, "logrite.mstraat": mstraat, "logrite.mplaats": mplaats, "logrite.movbestnr": movbestnr})
    selova = select([orders_verkoop_artikelen,artikelen]).where(and_(\
      orders_verkoop_artikelen.c.ovbestelID == movbestnr, orders_verkoop_artikelen\
      .c.artikelID == artikelen.c.artikelID)).order_by(orders_verkoop_artikelen.c.ovaID)
    rpova = con.execute(selova)
    logger.debug("printPakbon(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): rpova → %s", rpord, mstraat, mplaats, movbestnr, rpova, extra={"event.action": "printPakbon", "logrite.rpord": rpord, "logrite.mstraat": mstraat, "logrite.mplaats": mplaats, "logrite.movbestnr": movbestnr})

    mblad = 1
    logger.debug("printPakbon(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): mblad → %s", rpord, mstraat, mplaats, movbestnr, mblad, extra={"event.action": "printPakbon", "logrite.rpord": rpord, "logrite.mstraat": mstraat, "logrite.mplaats": mplaats, "logrite.movbestnr": movbestnr})
    rgl = 0
    if platform == 'win32':
        filename = '.\\forms\\Weborders_Pakbonnen\\Weborder-pakbon-'+str(rpord[0])+'.txt'
    else:
        filename = './forms/Weborders_Pakbonnen/Weborder-pakbon-'+str(rpord[0])+'.txt'
        logger.debug("printPakbon(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): filename → %s", rpord, mstraat, mplaats, movbestnr, filename, extra={"event.action": "printPakbon", "logrite.rpord": rpord, "logrite.mstraat": mstraat, "logrite.mplaats": mplaats, "logrite.movbestnr": movbestnr})
    adreskop=\
    ('\n\n\n\n\n\n\nPAKBON\n\n'+rpord[10]+' '+rpord[11]+' '+rpord[12]+' '+rpord[13]+',\n'+\
     mstraat+' '+rpord[15]+rpord[16]+',\n'+\
     rpord[14]+' '+mplaats+'.\n\n\n\n\n')
    logger.debug("printPakbon(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): adreskop → %s", rpord, mstraat, mplaats, movbestnr, adreskop, extra={"event.action": "printPakbon", "logrite.rpord": rpord, "logrite.mstraat": mstraat, "logrite.mplaats": mplaats, "logrite.movbestnr": movbestnr})
    open(filename,'w').write(adreskop)
    kop=\
    ('Ordernummer: '+ str(rpord[0])+'          Datum: '+str(datetime.datetime.now())[0:10]+'  Blad : '+str(mblad)+'\n'+
    '==============================================================================================\n'+
    'Artikelnr  Omschrijving                        Eenheid Aantal  Locatie    Geleverd            \n'+
    '==============================================================================================\n')
    logger.debug("printPakbon(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s): kop → %s", rpord, mstraat, mplaats, movbestnr, kop, extra={"event.action": "printPakbon", "logrite.rpord": rpord, "logrite.mstraat": mstraat, "logrite.mplaats": mplaats, "logrite.movbestnr": movbestnr})
    
    for row in rpova:
        if rgl == 0 and mblad == 1:
            open(filename, 'w').write(adreskop)
            open(filename, 'a').write(kop)
            rgl = 16
        elif rgl%57 == 0:
            open(filename, 'a').write(kop)
            mblad += 1
        open(filename,'a').write('{:<11d}'.format(row[2])+'{:<37.35s}'.format(row[11])+\
           '{:>6s}'.format(row[14])+' '+'{:>6.2f}'.format(row[3])+' '\
           +'{:>8s}'.format(row[15])+'{:>12s}'.format(row[9])+'  ________ \n')
        rgl += 1
    if platform == 'win32':
        os.startfile(filename, "print")
    else:
        os.system("lpr "+filename)
    printing()
    logger.debug("<<< Exiting printPakbon(rpord=%s,mstraat=%s,mplaats=%s,movbestnr=%s)", rpord, mstraat, mplaats, movbestnr, extra={"event.action": "printPakbon", "logrite.rpord": rpord, "logrite.mstraat": mstraat, "logrite.mplaats": mplaats, "logrite.movbestnr": movbestnr})
    
def zoekWeborder(m_email, afd):
    logger.warning(">>> Entering zoekWeborder(m_email=%s,afd=%s)", m_email, afd, extra={"event.action": "zoekWeborder", "logrite.afd": afd})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            self.setWindowTitle("Opvragen Webverkooporder")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
            
            self.Keuze = QLabel()
            logger.debug("__init__(parent=%s): self.Keuze → %s", parent, self.Keuze, extra={"event.action": "__init__"})
            k0Edit = QComboBox()
            logger.debug("__init__(self=%s,parent=%s): k0Edit → %s", self, parent, k0Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): k0Edit → %s", parent, k0Edit, extra={"event.action": "__init__"})
            k0Edit.setFixedWidth(230)
            k0Edit.setFont(QFont("Arial",10))
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.addItem(' Sorteersleutel voor zoeken')
            k0Edit.addItem('1. Alle Orders')
            k0Edit.addItem('2. Gefilterd op postcode')
            k0Edit.addItem('3. Gefilterd op achternaam')
            k0Edit.addItem('4. Gefilterd op ordernummer')
            k0Edit.addItem('5. Gefilterd op besteldatum')
            k0Edit.activated[str].connect(self.k0Changed)
               
            self.Zoekterm = QLabel()
            logger.debug("__init__(parent=%s): self.Zoekterm → %s", parent, self.Zoekterm, extra={"event.action": "__init__"})
            zktrmEdit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): zktrmEdit → %s", self, parent, zktrmEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): zktrmEdit → %s", parent, zktrmEdit, extra={"event.action": "__init__"})
            zktrmEdit.setFixedWidth(220)
            zktrmEdit.setFont(QFont("Arial",10))
            zktrmEdit.textChanged.connect(self.zktrmChanged)
            reg_ex = QRegExp('.*$')
            logger.debug("__init__(parent=%s): reg_ex → %s", parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): reg_ex → %s", self, parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): grid → %s", parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid, extra={"event.action": "__init__"})
            input_validator = QRegExpValidator(reg_ex, zktrmEdit)
            logger.debug("__init__(self=%s,parent=%s): input_validator → %s", self, parent, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): input_validator → %s", parent, input_validator, extra={"event.action": "__init__"})
            zktrmEdit.setValidator(input_validator)
     
            grid = QGridLayout()
            grid.setSpacing(20)
                          
            lbl = QLabel()
            logger.debug("__init__(parent=%s): lbl → %s", parent, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl, extra={"event.action": "__init__"})
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap, extra={"event.action": "__init__"})
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 1, 0, 1 ,2)
            
            logo = QLabel()
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 1, 1, 1, 2, Qt.AlignRight)
                                  
            lbl1 = QLabel('Zoekterm')  
            logger.debug("__init__(parent=%s): lbl1 → %s", parent, lbl1, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl1 → %s", self, parent, lbl1, extra={"event.action": "__init__"})
            grid.addWidget(lbl1, 3, 0, 1, 1, Qt.AlignRight)
            grid.addWidget(zktrmEdit, 3, 1, 1, 2)
            grid.addWidget(k0Edit, 2, 1, 1 , 2, Qt.AlignRight)
            
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 5, 0, 1, 3, Qt.AlignCenter)
        
            applyBtn = QPushButton('Zoeken')
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn, extra={"event.action": "__init__"})
            applyBtn.clicked.connect(self.accept)
                
            grid.addWidget(applyBtn, 4, 2, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            closeBtn = QPushButton('Sluiten')
            logger.debug("__init__(parent=%s): closeBtn → %s", parent, closeBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): closeBtn → %s", self, parent, closeBtn, extra={"event.action": "__init__"})
            closeBtn.clicked.connect(lambda: windowSluit(self,m_email))
    
            grid.addWidget(closeBtn, 4, 1, 1, 1, Qt.AlignRight)
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            closeBtn.setFont(QFont("Arial",10))
            closeBtn.setFixedWidth(100)
            closeBtn.setStyleSheet("color: black;  background-color: gainsboro")
            logger.warning(">>> Entering __init__()", extra={"event.action": "__init__"})
            logger.debug("__init__(): grid → %s", grid, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): grid → %s", self, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.lbl → %s", self.lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.pixmap → %s", self.pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl → %s", self, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.logo → %s", self.logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): logo → %s", self, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl1 → %s", lbl1, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl1 → %s", self, lbl1, extra={"event.action": "__init__"})
            logger.debug("__init__(): q1Edit → %s", q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q1Edit → %s", self, q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl2 → %s", lbl2, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl2 → %s", self, lbl2, extra={"event.action": "__init__"})
            logger.debug("__init__(): q2Edit → %s", q2Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q2Edit → %s", self, q2Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl3 → %s", lbl3, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl3 → %s", self, lbl3, extra={"event.action": "__init__"})
            logger.debug("__init__(): q3Edit → %s", q3Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q3Edit → %s", self, q3Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl9 → %s", lbl9, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl9 → %s", self, lbl9, extra={"event.action": "__init__"})
            logger.debug("__init__(): q9Edit → %s", q9Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q9Edit → %s", self, q9Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl4 → %s", lbl4, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl4 → %s", self, lbl4, extra={"event.action": "__init__"})
            logger.debug("__init__(): q4Edit → %s", q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q4Edit → %s", self, q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl5 → %s", lbl5, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl5 → %s", self, lbl5, extra={"event.action": "__init__"})
            logger.debug("__init__(): q5Edit → %s", q5Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q5Edit → %s", self, q5Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl6 → %s", lbl6, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl6 → %s", self, lbl6, extra={"event.action": "__init__"})
            logger.debug("__init__(): q6Edit → %s", q6Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q6Edit → %s", self, q6Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl7 → %s", lbl7, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl7 → %s", self, lbl7, extra={"event.action": "__init__"})
            logger.debug("__init__(): q7Edit → %s", q7Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q7Edit → %s", self, q7Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl8 → %s", lbl8, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl8 → %s", self, lbl8, extra={"event.action": "__init__"})
            logger.debug("__init__(): q8Edit → %s", q8Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q8Edit → %s", self, q8Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): cBox → %s", cBox, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): cBox → %s", self, cBox, extra={"event.action": "__init__"})
            logger.debug("__init__(): cBox1 → %s", cBox1, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): cBox1 → %s", self, cBox1, extra={"event.action": "__init__"})
            logger.debug("__init__(): regelBtn → %s", regelBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): regelBtn → %s", self, regelBtn, extra={"event.action": "__init__"})
            logger.debug("<<< Exiting __init__()", extra={"event.action": "__init__"})

        def k0Changed(self, text):
            logger.warning(">>> Entering k0Changed(text=%s)", text, extra={"event.action": "k0Changed", "logrite.text": text})
            self.Keuze.setText(text)
            logger.debug("<<< Exiting k0Changed(text=%s)", text, extra={"event.action": "k0Changed", "logrite.text": text})
            
        def zktrmChanged(self, text):
            logger.warning(">>> Entering zktrmChanged(text=%s)", text, extra={"event.action": "zktrmChanged", "logrite.text": text})
            self.Zoekterm.setText(text)
            logger.debug("<<< Exiting zktrmChanged(text=%s)", text, extra={"event.action": "zktrmChanged", "logrite.text": text})
            
        def returnk0(self):
            logger.warning(">>> Entering returnk0()", extra={"event.action": "returnk0"})
            logger.debug("<<< Exiting returnk0()", extra={"event.action": "returnk0"})
            return self.Keuze.text()
        
        def returnzktrmEdit(self):
            logger.warning(">>> Entering returnzktrmEdit()", extra={"event.action": "returnzktrmEdit"})
            logger.debug("<<< Exiting returnzktrmEdit()", extra={"event.action": "returnzktrmEdit"})
            return self.Zoekterm.text()
        
        @staticmethod
        def getData(parent=None):
            logger.warning(">>> Entering getData(parent=%s)", parent, extra={"event.action": "getData"})
            dialog = Widget(parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog, extra={"event.action": "getData"})
            dialog.exec_()
            logger.debug("<<< Exiting getData(parent=%s)", parent, extra={"event.action": "getData"})
            return [dialog.returnk0(), dialog.returnzktrmEdit()] 
        
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
    bestelOrder(m_email, keuze, zoekterm, afd)
     
def regelsOrder(rpova, afd):
    logger.warning(">>> Entering regelsOrder(rpova=%s,afd=%s)", rpova, afd, extra={"event.action": "regelsOrder", "logrite.rpova": rpova, "logrite.afd": afd})
    for rij in rpova:
        class RegelWindow(QDialog):
            logger.debug("<<< Exiting regelsOrder(rpova=%s,afd=%s)", rpova, afd, extra={"event.action": "regelsOrder", "logrite.rpova": rpova, "logrite.afd": afd})
            def __init__(self):
                logger.warning(">>> Entering __init__()", extra={"event.action": "__init__"})
                QDialog.__init__(self)
                
                grid = QGridLayout()
                grid.setSpacing(20)
                            
                self.setWindowTitle("Bestelling Artikelregel")
                self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
                
                self.setFont(QFont('Arial', 10))   
                                                  
                self.lbl = QLabel()
                self.pixmap = QPixmap('./images/logos/verbinding.jpg')
                self.lbl.setPixmap(self.pixmap)
                grid.addWidget(self.lbl , 0, 0)
                
                grid.addWidget(QLabel('Bestelling Artikelregel: ' +str(rij[6])),0, 1, 1, 2)
        
                self.logo = QLabel()
                self.pixmap = QPixmap('./images/logos/logo.jpg')
                self.logo.setPixmap(self.pixmap)
                grid.addWidget(self.logo , 0, 5, 1, 1, Qt.AlignRight) 
                
                lbl1 = QLabel('OrderregelID')
                q1Edit = QLineEdit(str(rij[0]))
                q1Edit.setAlignment(Qt.AlignRight)
                q1Edit.setFixedWidth(90)
                q1Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                q1Edit.setDisabled(True)
                
                grid.addWidget(lbl1, 1, 0)
                grid.addWidget(q1Edit, 1,1)
                
                lbl2 = QLabel('Ordernummer')
                q2Edit = QLineEdit(str(rij[1]))
                q2Edit.setFixedWidth(100)
                q2Edit.setAlignment(Qt.AlignRight)
                q2Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                q2Edit.setDisabled(True)
                
                grid.addWidget(lbl2, 1, 2)
                grid.addWidget(q2Edit, 1,3)
                
                lbl3 = QLabel('Artikelnummer')
                q3Edit = QLineEdit(str(rij[10]))
                q3Edit.setFixedWidth(100)
                q2Edit.setAlignment(Qt.AlignRight)
                q3Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                q3Edit.setDisabled(True)
                
                grid.addWidget(lbl3, 2, 0)
                grid.addWidget(q3Edit, 2,1)
                
                lbl9 = QLabel('Omschrijving')
                q9Edit = QLineEdit(str(rij[11]))
                q9Edit.setFixedWidth(350)
                q9Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                q9Edit.setDisabled(True)
                
                grid.addWidget(lbl9, 2, 2)
                grid.addWidget(q9Edit, 2, 3, 1 ,3)
                                     
                lbl4 = QLabel('Aantal')
                q4Edit = QLineEdit('{:12.2f}'.format(rij[3]))
                q4Edit.setFixedWidth(100)
                q4Edit.setAlignment(Qt.AlignRight)
                q4Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                q4Edit.setDisabled(True)
                
                grid.addWidget(lbl4, 3, 0)
                grid.addWidget(q4Edit, 3, 1)
                
                lbl5 = QLabel('Verkoopprijs')
                q5Edit = QLineEdit('{:12.2f}'.format(rij[5]))
                q5Edit.setFixedWidth(100)
                q5Edit.setAlignment(Qt.AlignRight)
                q5Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                q5Edit.setDisabled(True)
             
                grid.addWidget(lbl5, 3, 2)
                grid.addWidget(q5Edit, 3, 3)
                
                lbl6 = QLabel('Leverdatum')
                q6Edit = QLineEdit(str(rij[4]))
                q6Edit.setFixedWidth(100)
                q6Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                q6Edit.setDisabled(True)
                
                grid.addWidget(lbl6, 4, 0)
                grid.addWidget(q6Edit, 4, 1)
                
                lbl7 = QLabel('RetourLevering')
                q7Edit = QLineEdit('{:12.2f}'.format(rij[7]))
                q7Edit.setFixedWidth(100)
                q7Edit.setAlignment(Qt.AlignRight)
                q7Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                q7Edit.setDisabled(True)
                                            
                grid.addWidget(lbl7, 4, 2)
                grid.addWidget(q7Edit, 4, 3)
                          
                lbl8 = QLabel('Betaaldatum')
                q8Edit = QLineEdit(str(rij[8]))
                q8Edit.setFixedWidth(100)
                q8Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                q8Edit.setDisabled(True)
                                            
                grid.addWidget(lbl8, 5, 0)
                grid.addWidget(q8Edit, 5, 1)
                
                cBox = QCheckBox('Betaling ontvangen')
                cBox.stateChanged.connect(self.cBoxChanged)
                if not afd or afd == 2 or rij[8]:
                    cBox.setDisabled(True)
                grid.addWidget(cBox, 5, 2)
                
                lbl9 = QLabel('Datum geleverd')
                q9Edit = QLineEdit(str(rij[9]))
                q9Edit.setFixedWidth(100)
                q9Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                q9Edit.setDisabled(True)
                                            
                grid.addWidget(lbl9, 5, 3)
                grid.addWidget(q9Edit, 5, 4)
                
                cBox1 = QCheckBox('Geleverd')
                cBox1.stateChanged.connect(self.cBox1Changed)
                if afd or rij[9] :
                    cBox1.setDisabled(True)
                grid.addWidget(cBox1,5, 5)
                
                regelBtn = QPushButton('Regel')
                regelBtn.clicked.connect(self.accept)
        
                grid.addWidget(regelBtn, 6, 5)
                regelBtn.setFont(QFont("Arial",10))
                regelBtn.setFixedWidth(100)
                regelBtn.setStyleSheet("color: black;  background-color: gainsboro")
              
                grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 7, 1, 1, 3, Qt.AlignCenter)
                                                                                                       
                self.setLayout(grid)
                self.setGeometry(250, 300, 150, 150)
                logger.debug("<<< Exiting __init__()", extra={"event.action": "__init__"})
           
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
            
            state1 = False   
            def cBox1Changed(self, state1):
                logger.warning(">>> Entering cBox1Changed(state1=%s)", state1, extra={"event.action": "cBox1Changed", "logrite.state1": state1})
                logger.debug("cBox1Changed(self=%s,state1=%s): self.state1 → %s", self, state1, self.state1, extra={"event.action": "cBox1Changed", "logrite.state1": state1})
                if state1 == Qt.Checked:
                    logger.debug("<<< Exiting cBox1Changed(state1=%s)", state1, extra={"event.action": "cBox1Changed", "logrite.state1": state1})
                    self.state1 = True
                    
            def returncBox1(self):
                logger.warning(">>> Entering returncBox1()", extra={"event.action": "returncBox1"})
                logger.debug("<<< Exiting returncBox1()", extra={"event.action": "returncBox1"})
                return self.state1
        
            @staticmethod
            def getData(parent=None):
                dialog = RegelWindow()
                dialog.exec_()
                return [dialog.returncBox(), dialog.returncBox1()]
                   
        regelWin = RegelWindow()
        data = regelWin.getData()
        
        metadata = MetaData()
        orders_verkoop_artikelen = Table('orders_verkoop_artikelen', metadata,
            Column('ovaID', Integer, primary_key=True),
            Column('ovbestelID', None, ForeignKey('orders_verkoop.ovbestelID')),
            Column('regel', Integer),
            Column('betaaldatum', String),
            Column('leveringsdatum', String))
          
        engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
        con = engine.connect()
        selb = select([orders_verkoop_artikelen]).where(and_(orders_verkoop_artikelen.\
            c.ovbestelID == rij[1], orders_verkoop_artikelen.c.regel == rij[6]))
        rpb = con.execute(selb).first()
        if data[0] and not rpb[3]:
            up = update(orders_verkoop_artikelen).where(and_(orders_verkoop_artikelen\
             .c.regel == rij[6], orders_verkoop_artikelen.c.ovbestelID == rij[1]))\
             .values(betaaldatum = str(datetime.datetime.now())[0:10]) 
            con.execute(up)
        if data[1] and not rpb[4]:
                upl = update(orders_verkoop_artikelen).where(and_(orders_verkoop_artikelen\
                 .c.regel == rij[6], orders_verkoop_artikelen.c.ovbestelID == rij[1]))\
                 .values(leveringsdatum = str(datetime.datetime.now())[0:10]) 
                con.execute(upl)
        metadata = MetaData()
        orders_verkoop = Table('orders_verkoop', metadata,
            Column('ovbestelID', Integer, primary_key=True),
            Column('datum_betaald', String),
            Column('datum_geleverd', String))
        orders_verkoop_artikelen = Table('orders_verkoop_artikelen', metadata,
            Column('ovaID', Integer, primary_key=True),
            Column('ovbestelID', None, ForeignKey('orders_verkoop.ovbestelID')),
            Column('regel', Integer),
            Column('betaaldatum', String),
            Column('leveringsdatum', String))
        engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
        con = engine.connect()
        selb = select([orders_verkoop, orders_verkoop_artikelen]).where(and_\
            (orders_verkoop_artikelen.c.ovbestelID==rij[1], orders_verkoop_artikelen.\
             c.ovbestelID == orders_verkoop.c.ovbestelID)).order_by\
            (orders_verkoop_artikelen.c.regel.desc())
        rpbal = con.execute(selb)
        rpbmax = con.execute(selb).first()
        mrgl = rpbmax[5]
        mregel = 0
        if not rpbmax[1]:
            for item in rpbal:
                mbet=item[6]
                if mbet:
                    mregel += 1
                    if mrgl == mregel:
                        updbet = update(orders_verkoop).where(orders_verkoop.c.ovbestelID ==\
                         rij[1]).values(datum_betaald = str(datetime.datetime.now())[0:10])
                        con.execute(updbet)
                        rpbal = con.execute(selb)
        mregel1 = 0
        if not rpbmax[2]:
            for item1 in rpbal:
                mlev=item1[7]
                if mlev:
                    mregel1 += 1
                    if mrgl == mregel1:
                        updlev =  update(orders_verkoop).where(orders_verkoop.c.ovbestelID ==\
                         rij[1]).values(datum_geleverd = str(datetime.datetime.now())[0:10])
                        con.execute(updlev)
                                                   
def bestelOrder(m_email, keuze, zoekterm, afd): 
    logger.warning(">>> Entering bestelOrder(m_email=%s,keuze=%s,zoekterm=%s,afd=%s)", m_email, keuze, zoekterm, afd, extra={"event.action": "bestelOrder", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm, "logrite.afd": afd})
    class MyWindow(QDialog):
        def __init__(self, data_list, header, *args):
            logger.warning(">>> Entering __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})
            QWidget.__init__(self, *args,)
            self.setWindowTitle('Webverkooporders')
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
            table_view.setColumnHidden(1,True)
            table_view.setColumnHidden(6,True)
            table_view.setColumnHidden(9,True)
            table_view.clicked.connect(showSelorder)
            grid.addWidget(table_view, 0, 0, 1, 13)
            
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
            grid.addWidget(logo , 1, 12, 1, 1, Qt.AlignRight)
            
            freshBtn = QPushButton('Verversen')
            logger.debug("__init__(data_list=%s,header=%s): freshBtn → %s", data_list, header, freshBtn, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): freshBtn → %s", self, data_list, header, freshBtn, extra={"event.action": "__init__", "logrite.data_list": data_list})
            freshBtn.clicked.connect(lambda: refresh(m_email, keuze, zoekterm, afd, self))

            freshBtn.setFont(QFont("Arial",10))
            freshBtn.setFixedWidth(100) 
            freshBtn.setStyleSheet("color: black;  background-color: gainsboro")
   
            grid.addWidget(freshBtn, 1, 11, 1, 1, Qt.AlignRight)
            
            sluitBtn = QPushButton('Sluiten')
            logger.debug("__init__(data_list=%s,header=%s): sluitBtn → %s", data_list, header, sluitBtn, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): sluitBtn → %s", self, data_list, header, sluitBtn, extra={"event.action": "__init__", "logrite.data_list": data_list})
            sluitBtn.clicked.connect(self.close)

            sluitBtn.setFont(QFont("Arial",10))
            sluitBtn.setFixedWidth(100) 
            sluitBtn.setStyleSheet("color: black;  background-color: gainsboro") 
            
            grid.addWidget(sluitBtn, 1, 10)
          
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 1, 0, 1, 13, Qt.AlignCenter)
            
            self.setLayout(grid)
            self.setGeometry(50, 50, 1500, 900)
            logger.debug("<<< Exiting __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})
     
    class MyTableModel(QAbstractTableModel):
        def __init__(self, parent, mylist, header, *args):
            logger.warning(">>> Entering __init__(parent=%s,mylist=%s,header=%s)", parent, mylist, header, extra={"event.action": "__init__", "logrite.mylist": mylist})
            logger.debug("__init__(self=%s,parent=%s,mylist=%s,header=%s): self.mylist → %s", self, parent, mylist, header, self.mylist, extra={"event.action": "__init__", "logrite.mylist": mylist})
            logger.debug("__init__(self=%s,parent=%s,mylist=%s,header=%s): self.header → %s", self, parent, mylist, header, self.header, extra={"event.action": "__init__", "logrite.mylist": mylist})
            QAbstractTableModel.__init__(self, parent, *args)
            logger.debug("<<< Exiting __init__(parent=%s,mylist=%s,header=%s)", parent, mylist, header, extra={"event.action": "__init__", "logrite.mylist": mylist})
            self.mylist = mylist
            logger.debug("__init__(): q17Edit → %s", q17Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q17Edit → %s", self, q17Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl10 → %s", lbl10, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl10 → %s", self, lbl10, extra={"event.action": "__init__"})
            logger.debug("__init__(): q10Edit → %s", q10Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q10Edit → %s", self, q10Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl11 → %s", lbl11, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl11 → %s", self, lbl11, extra={"event.action": "__init__"})
            logger.debug("__init__(): q11Edit → %s", q11Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q11Edit → %s", self, q11Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl12 → %s", lbl12, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl12 → %s", self, lbl12, extra={"event.action": "__init__"})
            logger.debug("__init__(): q12Edit → %s", q12Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q12Edit → %s", self, q12Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl13 → %s", lbl13, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl13 → %s", self, lbl13, extra={"event.action": "__init__"})
            logger.debug("__init__(): q13Edit → %s", q13Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q13Edit → %s", self, q13Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl14 → %s", lbl14, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl14 → %s", self, lbl14, extra={"event.action": "__init__"})
            logger.debug("__init__(): q14Edit → %s", q14Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q14Edit → %s", self, q14Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl15 → %s", lbl15, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl15 → %s", self, lbl15, extra={"event.action": "__init__"})
            logger.debug("__init__(): q15Edit → %s", q15Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q15Edit → %s", self, q15Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl16 → %s", lbl16, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl16 → %s", self, lbl16, extra={"event.action": "__init__"})
            logger.debug("__init__(): q16Edit → %s", q16Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q16Edit → %s", self, q16Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): terugBtn → %s", terugBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): terugBtn → %s", self, terugBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(): pakbonBtn → %s", pakbonBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): pakbonBtn → %s", self, pakbonBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(): factuurBtn → %s", factuurBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): factuurBtn → %s", self, factuurBtn, extra={"event.action": "__init__"})
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
  
    header = ['Ordernr','-','Besteldatum', 'Betaald','Geleverd','Totaalbedrag','-', 'Accountnr',\
              'Rekeningnr','-','Aanhef', 'Voornaam','Tussen', 'Achternaam',\
              'Postcode', 'Huisnummer', 'Toev','e-mailadres','Telefoon']
    
    metadata = MetaData()
    orders_verkoop = Table('orders_verkoop', metadata,
        Column('ovbestelID', Integer, primary_key=True),
        Column('klantID', None, ForeignKey('klanten.klantID')),
        Column('ovbesteldatum', String),
        Column('datum_betaald', String),
        Column('datum_geleverd', String),
        Column('bedrag', Float))
    klanten = Table('klanten', metadata,
        Column('klantID', Integer(), primary_key=True),
        Column('accountID', None, ForeignKey('accounts.accountID')),
        Column('rekening', String))
    accounts = Table('accounts', metadata,
        Column('accountID', Integer(), primary_key=True),
        Column('aanhef', String),
        Column('voornaam', String), 
        Column('tussenvoegsel', String),
        Column('achternaam', String),
        Column('postcode', String),       
        Column('huisnummer', String),
        Column('toevoeging', String),
        Column('email', String),
        Column('telnr', String)) 

    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
    import validZt  
    if keuze == 1:
        selwo = select([orders_verkoop, klanten, accounts]).where(and_(orders_verkoop\
            .c.klantID == klanten.c.klantID, klanten.c.accountID == accounts\
            .c.accountID)).order_by(orders_verkoop.c.ovbestelID)
    elif keuze == 2 and validZt.zt(zoekterm, 9):
        selwo = select([orders_verkoop, klanten, accounts]).where(and_(orders_verkoop\
            .c.klantID == klanten.c.klantID, klanten.c.accountID == accounts\
            .c.accountID, accounts.c.postcode.ilike(zoekterm+'%')))\
            .order_by(orders_verkoop.c.ovbestelID)
    elif keuze == 3:
        selwo = select([orders_verkoop, klanten, accounts]).where(and_(orders_verkoop\
            .c.klantID == klanten.c.klantID, klanten.c.accountID == accounts\
            .c.accountID, accounts.c.achternaam.ilike('%'+zoekterm+'%')))\
            .order_by(orders_verkoop.c.ovbestelID)
    elif keuze == 4 and validZt.zt(zoekterm, 5):
        selwo = select([orders_verkoop, klanten, accounts]).where(and_(orders_verkoop\
            .c.klantID == klanten.c.klantID, klanten.c.accountID == accounts\
            .c.accountID, orders_verkoop.c.ovbestelID == int(zoekterm)))\
            .order_by(orders_verkoop.c.ovbestelID)
    elif keuze == 5 and validZt.zt(zoekterm, 10):
        selwo = select([orders_verkoop, klanten, accounts]).where(and_(orders_verkoop\
            .c.klantID == klanten.c.klantID, klanten.c.accountID == accounts\
            .c.accountID, orders_verkoop.c.ovbesteldatum.like(zoekterm+'%')))\
            .order_by(orders_verkoop.c.ovbestelID)
    else:
        ongInvoer()
        zoekWeborder(m_email, afd)
    
    if con.execute(selwo).fetchone():
        rpwo = con.execute(selwo)
    else:
        geenRecord()
        zoekWeborder(m_email, afd)
  
    data_list=[]
    for row in rpwo:
        data_list += [(row)]
        
    def showSelorder(idx):
        logger.warning(">>> Entering showSelorder(idx=%s)", idx, extra={"event.action": "showSelorder", "logrite.idx": idx})
        movbestnr = idx.data()
        logger.debug("showSelorder(idx=%s): movbestnr → %s", idx, movbestnr, extra={"event.action": "showSelorder", "logrite.idx": idx})
        if idx.column() == 0:
            metadata = MetaData()
            logger.debug("showSelorder(idx=%s): metadata → %s", idx, metadata, extra={"event.action": "showSelorder", "logrite.idx": idx})
            orders_verkoop = Table('orders_verkoop', metadata,
                Column('ovbestelID', Integer, primary_key=True),
                Column('klantID', None, ForeignKey('klanten.klantID')),
                Column('ovbesteldatum', String),
                Column('bedrag', Float),
                Column('datum_betaald', String),
                Column('datum_geleverd',String))
            klanten = Table('klanten', metadata,
                Column('klantID', Integer(), primary_key=True),
                Column('accountID', None, ForeignKey('accounts.accountID')),
                Column('rekening', String))
            accounts = Table('accounts', metadata,
                Column('accountID', Integer(), primary_key=True),
                Column('aanhef', String),
                Column('voornaam', String), 
                Column('tussenvoegsel', String),
                Column('achternaam', String),
                Column('postcode', String),       
                Column('huisnummer', String),
                Column('toevoeging', String),
                Column('email', String),
                Column('telnr', String)) 
            orders_verkoop_artikelen = Table('orders_verkoop_artikelen', metadata,
                Column('ovaID', Integer, primary_key=True),
                Column('ovbestelID', None, ForeignKey('orders_verkoop.ovbestelID')),
                Column('artikelID', None, ForeignKey('artikelen.artikelID')),
                Column('ovaantal', Integer),
                Column('ovleverdatum', String),
                Column('verkoopprijs', Float),
                Column('regel', Integer),
                Column('retour', Float),
                Column('betaaldatum', String),
                Column('leveringsdatum', String))
            artikelen = Table('artikelen', metadata,
                Column('artikelID', Integer(), primary_key=True),
                Column('artikelomschrijving', String),
                Column('artikelprijs', Float),
                Column('art_voorraad', Float),
                Column('art_eenheid', String),
                Column('locatie_magazijn', String))
            
            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            logger.debug("showSelorder(idx=%s): engine → %s", idx, engine, extra={"event.action": "showSelorder", "logrite.idx": idx})
            con = engine.connect()
            
            selord = select([orders_verkoop, klanten, accounts]).where(and_(orders_verkoop\
                .c.ovbestelID == movbestnr, orders_verkoop.c.klantID == klanten.c.klantID,\
                 klanten.c.accountID == accounts.c.accountID))
            rpord = con.execute(selord).first()
            logger.debug("showSelorder(idx=%s): rpord → %s", idx, rpord, extra={"event.action": "showSelorder", "logrite.idx": idx})
                 
            selova = select([orders_verkoop_artikelen,artikelen]).where(and_(\
              orders_verkoop_artikelen.c.ovbestelID == movbestnr, orders_verkoop_artikelen\
             .c.artikelID == artikelen.c.artikelID)).order_by(orders_verkoop_artikelen.c.ovaID)
            rpova = con.execute(selova)
            logger.debug("showSelorder(idx=%s): rpova → %s", idx, rpova, extra={"event.action": "showSelorder", "logrite.idx": idx})
            
            mpostcode = rpord[14]
            logger.debug("showSelorder(idx=%s): mpostcode → %s", idx, mpostcode, extra={"event.action": "showSelorder", "logrite.idx": idx})
            mhuisnr = int(rpord[15])
            logger.debug("showSelorder(idx=%s): mhuisnr → %s", idx, mhuisnr, extra={"event.action": "showSelorder", "logrite.idx": idx})
            madres = checkpostcode(mpostcode,mhuisnr)
            logger.debug("showSelorder(idx=%s): madres → %s", idx, madres, extra={"event.action": "showSelorder", "logrite.idx": idx})
            mstraat = madres[0]
            logger.debug("showSelorder(idx=%s): mstraat → %s", idx, mstraat, extra={"event.action": "showSelorder", "logrite.idx": idx})
            mplaats = madres[1]
            logger.debug("showSelorder(idx=%s): mplaats → %s", idx, mplaats, extra={"event.action": "showSelorder", "logrite.idx": idx})
                 
            class MainWindow(QDialog):
                logger.debug("<<< Exiting showSelorder(idx=%s)", idx, extra={"event.action": "showSelorder", "logrite.idx": idx})
                def __init__(self):
                    QDialog.__init__(self)
                    
                    grid = QGridLayout()
                    grid.setSpacing(20)
                                
                    self.setWindowTitle("Bestelling Webartikelen")
                    self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
                    
                    self.setFont(QFont('Arial', 10))   
                                                      
                    self.lbl = QLabel()
                    self.pixmap = QPixmap('./images/logos/verbinding.jpg')
                    self.lbl.setPixmap(self.pixmap)
                    grid.addWidget(self.lbl , 0, 0)
                    
                    grid.addWidget(QLabel('Bestelling Webartikelen'),0, 1, 1, 2)
            
                    self.logo = QLabel()
                    self.pixmap = QPixmap('./images/logos/logo.jpg')
                    self.logo.setPixmap(self.pixmap)
                    grid.addWidget(self.logo , 0, 4, 1, 1, Qt.AlignRight) 
                    
                    lbl1 = QLabel('Ordernummer')
                    q1Edit = QLineEdit(str(rpord[0]))
                    q1Edit.setAlignment(Qt.AlignRight)
                    q1Edit.setFixedWidth(90)
                    q1Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q1Edit.setDisabled(True)
                    
                    grid.addWidget(lbl1, 1, 0)
                    grid.addWidget(q1Edit, 1,1)
                    
                    lbl2 = QLabel('Bestel- / Leveringsdatum')
                    q2Edit = QLineEdit(str(rpord[2]))
                    q2Edit.setFixedWidth(100)
                    q2Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q2Edit.setDisabled(True)
                    q17Edit = QLineEdit(str(rpord[5]))
                    q17Edit.setFixedWidth(90)
                    q17Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q17Edit.setDisabled(True)
                    
                    grid.addWidget(lbl2, 1, 2)
                    grid.addWidget(q2Edit, 1, 3)
                    grid.addWidget(q17Edit, 1, 4, 1, 1,Qt.AlignRight)
                    
                    lbl3 = QLabel('Totaalbedrag')
                    q3Edit = QLineEdit('{:12.2f}'.format(rpord[3]))
                    q3Edit.setFixedWidth(100)
                    q3Edit.setAlignment(Qt.AlignRight)
                    q3Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q3Edit.setDisabled(True)
                    
                    grid.addWidget(lbl3, 2, 0)
                    grid.addWidget(q3Edit, 2,1)
                                         
                    lbl4 = QLabel('Betaaldatum')
                    q4Edit = QLineEdit(rpord[4])
                    q4Edit.setFixedWidth(100)
                    q4Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q4Edit.setDisabled(True)
                    
                    grid.addWidget(lbl4, 2, 2)
                    grid.addWidget(q4Edit, 2, 3, 1, 2)
                    
                    lbl5 = QLabel('Accountnummer')
                    q5Edit = QLineEdit(str(rpord[7]))
                    q5Edit.setFixedWidth(100)
                    q5Edit.setAlignment(Qt.AlignRight)
                    q5Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q5Edit.setDisabled(True)
                 
                    grid.addWidget(lbl5, 3, 0)
                    grid.addWidget(q5Edit,3,1)
                    
                    lbl6 = QLabel('Rekeningnummer')
                    q6Edit = QLineEdit(str(rpord[8]))
                    q6Edit.setFixedWidth(200)
                    q6Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q6Edit.setDisabled(True)
                    
                    grid.addWidget(lbl6, 3, 2)
                    grid.addWidget(q6Edit, 3, 3, 1 ,2)
                    
                    lbl7 = QLabel('Aanhef')
                    q7Edit = QLineEdit(str(rpord[10]))
                    q7Edit.setFixedWidth(100)
                    q7Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q7Edit.setDisabled(True)
                    
                    grid.addWidget(lbl7, 4, 0)
                    grid.addWidget(q7Edit, 4, 1)
                    
                    lbl8 = QLabel('Voornaam')
                    q8Edit = QLineEdit(str(rpord[11]))
                    q8Edit.setFixedWidth(230)
                    q8Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q8Edit.setDisabled(True)
                    
                    grid.addWidget(lbl8, 4, 2)
                    grid.addWidget(q8Edit, 4, 3, 1 ,2)
                    
                    lbl9 = QLabel('Tussen')
                    q9Edit = QLineEdit(str(rpord[12]))
                    q9Edit.setFixedWidth(100)
                    q9Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q9Edit.setDisabled(True)
                    
                    grid.addWidget(lbl9, 5, 0)
                    grid.addWidget(q9Edit, 5, 1)
                    
                    lbl10 = QLabel('Achternaam')
                    q10Edit = QLineEdit(str(rpord[13]))
                    q10Edit.setFixedWidth(230)
                    q10Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q10Edit.setDisabled(True)
                    
                    grid.addWidget(lbl10, 5, 2)
                    grid.addWidget(q10Edit, 5, 3, 1, 2)
                                  
                    lbl11= QLabel('Straatnaam')
                    q11Edit = QLineEdit(mstraat)
                    q11Edit.setFixedWidth(260)
                    q11Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q11Edit.setDisabled(True)
                    
                    grid.addWidget(lbl11, 6, 0)
                    grid.addWidget(q11Edit, 6, 1, 1, 3)
                    
                    lbl12= QLabel('Huisnummer')
                    q12Edit = QLineEdit(str(rpord[15])+rpord[16])
                    q12Edit.setFixedWidth(100)
                    q12Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q12Edit.setDisabled(True)
                    
                    grid.addWidget(lbl12, 6, 3)
                    grid.addWidget(q12Edit, 6, 4)
                                                   
                    lbl13= QLabel('Postcode')
                    q13Edit = QLineEdit(rpord[14])
                    q13Edit.setFixedWidth(70)
                    q13Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q13Edit.setDisabled(True)
                    
                    grid.addWidget(lbl13, 7, 0)
                    grid.addWidget(q13Edit, 7, 1)
                    
                    lbl14= QLabel('Woonplaats')
                    q14Edit = QLineEdit(str(mplaats))
                    q14Edit.setFixedWidth(230)
                    q14Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q14Edit.setDisabled(True)
                    
                    grid.addWidget(lbl14, 7, 2)
                    grid.addWidget(q14Edit, 7, 3, 1 , 2)
                    
                    lbl15= QLabel('E-Mailadres')
                    q15Edit = QLineEdit(rpord[17])
                    q15Edit.setFixedWidth(260)
                    q15Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q15Edit.setDisabled(True)
                    
                    grid.addWidget(lbl15, 8, 0)
                    grid.addWidget(q15Edit, 8, 1, 1, 3)
                    
                    lbl16= QLabel('Telefoon')
                    q16Edit = QLineEdit(str(rpord[18]))
                    q16Edit.setFixedWidth(100)
                    q16Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q16Edit.setDisabled(True)
                    
                    grid.addWidget(lbl16, 8, 3)
                    grid.addWidget(q16Edit, 8, 3 , 1, 2, Qt.AlignRight)
                    
                    regelBtn = QPushButton('Bestelregels')
                    regelBtn.clicked.connect(lambda: regelsOrder(rpova, afd))
                            
                    grid.addWidget(regelBtn, 10, 4)
                    regelBtn.setFont(QFont("Arial",10))
                    regelBtn.setFixedWidth(110)
                    regelBtn.setStyleSheet("color: black;  background-color: gainsboro")
                    
                    terugBtn = QPushButton('Sluiten')
                    terugBtn.clicked.connect(self.accept)
            
                    grid.addWidget(terugBtn, 10, 3, 1, 1, Qt.AlignRight)
                    terugBtn.setFont(QFont("Arial",10))
                    terugBtn.setFixedWidth(110)
                    terugBtn.setStyleSheet("color: black;  background-color: gainsboro")
                                   
                    pakbonBtn = QPushButton('Print Pakbon')
                    pakbonBtn.clicked.connect(lambda: printPakbon(rpord,mstraat,mplaats,movbestnr))
                           
                    grid.addWidget(pakbonBtn, 9, 4)
                    pakbonBtn.setFont(QFont("Arial",10))
                    pakbonBtn.setFixedWidth(110)
                               
                    factuurBtn = QPushButton('Print Factuur')
                    factuurBtn.clicked.connect(lambda: printFactuur(rpord,mstraat,mplaats,movbestnr))
    
                    grid.addWidget(factuurBtn, 9, 3, 1, 1, Qt.AlignRight)
                    factuurBtn.setFont(QFont("Arial",10))
                    factuurBtn.setFixedWidth(110)
                      
                    if afd == 1:
                        pakbonBtn.setDisabled(True)
                        factuurBtn.setStyleSheet("color: black;  background-color: gainsboro")
                    elif afd == 0:
                        factuurBtn.setDisabled(True)
                        pakbonBtn.setStyleSheet("color: black;  background-color: gainsboro")
                    elif afd == 2:
                        factuurBtn.setDisabled(True)
                        pakbonBtn.setDisabled(True)
                            
                    grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 11, 1, 1, 3, Qt.AlignCenter)
                                                                                                           
                    self.setLayout(grid)
                    self.setGeometry(300, 150, 150, 150)
                         
            mainWin = MainWindow()
            mainWin.exec_()
      
    win = MyWindow(data_list, header)
    win.exec_()
    zoekWeborder(m_email, afd)