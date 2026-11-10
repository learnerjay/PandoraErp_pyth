from login import hoofdMenu
import os, datetime
from PyQt5.QtCore import Qt, QAbstractTableModel, QRegExp
from PyQt5.QtGui import QFont, QPixmap, QIcon, QRegExpValidator
from PyQt5.QtWidgets import  QDialog, QLabel, QGridLayout,\
          QPushButton, QMessageBox, QLineEdit, QWidget, QTableView, QVBoxLayout
from sqlalchemy import (Table, Column, Integer, String, Float,\
                        MetaData, create_engine, ForeignKey)
from sqlalchemy.sql import select, update, insert, and_, func
import logging
logger = logging.getLogger(__name__)

def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})

def calcBestaatniet():
    logger.warning(">>> Entering calcBestaatniet()", extra={"event.action": "calcBestaatniet"})
    msg = QMessageBox()
    logger.debug("calcBestaatniet(): msg → %s", msg, extra={"event.action": "calcBestaatniet"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Calculation is not present!')
    msg.setWindowTitle('Entry')
    logger.debug("<<< Exiting calcBestaatniet()", extra={"event.action": "calcBestaatniet"})
    msg.exec_()
    
def printing():
    logger.warning(">>> Entering printing()", extra={"event.action": "printing"})
    msg = QMessageBox()
    logger.debug("printing(): msg → %s", msg, extra={"event.action": "printing"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Information)
    msg.setText('Just a moment printing is started!')
    msg.setWindowTitle('Printing')
    logger.debug("<<< Exiting printing()", extra={"event.action": "printing"})
    msg.exec_()
     
def zoekCalculatie(m_email):
    logger.warning(">>> Entering zoekCalculatie(m_email=%s)", m_email, extra={"event.action": "zoekCalculatie"})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            self.setWindowTitle("Calculate / Request / Printing")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
  
            self.Calculatie = QLabel()
            logger.debug("__init__(parent=%s): self.Calculatie → %s", parent, self.Calculatie, extra={"event.action": "__init__"})
            zkcalcEdit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): zkcalcEdit → %s", self, parent, zkcalcEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): zkcalcEdit → %s", parent, zkcalcEdit, extra={"event.action": "__init__"})
            zkcalcEdit.setFixedWidth(100)
            zkcalcEdit.setFont(QFont("Arial",10))
            zkcalcEdit.textChanged.connect(self.zkcalcChanged)
            reg_ex = QRegExp('^[1-9]{1}[0-9]{0,8}$')
            logger.debug("__init__(parent=%s): reg_ex → %s", parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): reg_ex → %s", self, parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): grid → %s", parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid, extra={"event.action": "__init__"})
            input_validator = QRegExpValidator(reg_ex, zkcalcEdit)
            logger.debug("__init__(self=%s,parent=%s): input_validator → %s", self, parent, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): input_validator → %s", parent, input_validator, extra={"event.action": "__init__"})
            zkcalcEdit.setValidator(input_validator)  
            
            grid = QGridLayout()
            grid.setSpacing(20)
                          
            lbl = QLabel()
            logger.debug("__init__(parent=%s): lbl → %s", parent, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl, extra={"event.action": "__init__"})
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap, extra={"event.action": "__init__"})
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 0, 0, 1, 2)
            
            lbl1 = QLabel('Calculation number\nor work order.')
            logger.debug("__init__(parent=%s): lbl1 → %s", parent, lbl1, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl1 → %s", self, parent, lbl1, extra={"event.action": "__init__"})
            lbl1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl1, 1, 0)
            grid.addWidget(zkcalcEdit, 1, 1)
            
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 4, 0, 1, 2, Qt.AlignCenter)
             
            logo = QLabel()
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 1, 1, 1, Qt.AlignRight)
   
            applyBtn = QPushButton('Search')
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn, extra={"event.action": "__init__"})
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 3, 1)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Close')
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn, extra={"event.action": "__init__"})
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
    
            grid.addWidget(cancelBtn, 3, 0, 1, 1,Qt.AlignRight)
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
             
        def zkcalcChanged(self, text):
            logger.warning(">>> Entering zkcalcChanged(text=%s)", text, extra={"event.action": "zkcalcChanged", "logrite.text": text})
            self.Calculatie.setText(text)
            logger.debug("<<< Exiting zkcalcChanged(text=%s)", text, extra={"event.action": "zkcalcChanged", "logrite.text": text})
             
        def returnCalculatie(self):
            logger.warning(">>> Entering returnCalculatie()", extra={"event.action": "returnCalculatie"})
            logger.debug("<<< Exiting returnCalculatie()", extra={"event.action": "returnCalculatie"})
            return self.Calculatie.text()
        
        @staticmethod
        def getData(parent=None):
            logger.warning(">>> Entering getData(parent=%s)", parent, extra={"event.action": "getData"})
            dialog = Widget(parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog, extra={"event.action": "getData"})
            dialog.exec_()
            logger.debug("<<< Exiting getData(parent=%s)", parent, extra={"event.action": "getData"})
            return [dialog.returnCalculatie()]       

    window = Widget()
    data = window.getData()
    
    metadata = MetaData()
    icalculaties = Table('icalculaties', metadata,
        Column('icalculatie', Integer),
        Column('werkomschrijving', String),
        Column('verwerkt', Integer),
        Column('koppelnummer', Integer))
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()

    if not data[0]:
       return
    elif data[0][0]=='7'and len(data[0]) == 9:
        mcalnr = data[0]
        selcl = select([icalculaties]).where(icalculaties.c.koppelnummer == int(mcalnr))
        rpcl = con.execute(selcl).first()
    elif data[0] and len(data[0]) <9:
        mcalnr = data[0]
        selcl = select([icalculaties]).where(icalculaties.c.icalculatie == int(mcalnr))
        rpcl = con.execute(selcl).first()
    else:
        calcBestaatniet()
        zoekCalculatie(m_email)
    if not rpcl:
        calcBestaatniet()
        zoekCalculatie(m_email)
    elif rpcl and (not rpcl[2]):
        opbouwRp(rpcl[0], rpcl[1], rpcl[2], rpcl[3], m_email)
    elif rpcl and rpcl[2]:
        opvragenCalc(rpcl[0], rpcl[1], rpcl[2], rpcl[3], m_email)
           
def opvragenCalc(mcalnr, mwerkomschr,mverw, mwerknr, m_email):
    logger.warning(">>> Entering opvragenCalc(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s)", mcalnr, mwerkomschr, mverw, mwerknr, m_email, extra={"event.action": "opvragenCalc", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
    class MainWindow(QDialog):
        def __init__(self):
            QDialog.__init__(self)
            
            grid = QGridLayout()
            grid.setSpacing(20)
            
            self.lbl = QLabel()
            self.pixmap = QPixmap('./images/logos/verbinding.jpg')
            self.lbl.setPixmap(self.pixmap)
            grid.addWidget(self.lbl , 0, 1)
    
            self.logo = QLabel()
            self.pixmap = QPixmap('./images/logos/logo.jpg')
            self.logo.setPixmap(self.pixmap)
            grid.addWidget(self.logo , 0, 2, 1, 1, Qt.AlignRight)
              
            self.setFont(QFont('Arial', 10))
            grid.addWidget(QLabel('Calculation: '+str(mcalnr)+'\nWork number: '+str(mwerknr)), 1, 1, 1, 3)
            grid.addWidget(QLabel(mwerkomschr[0:35]), 2 , 1, 1, 3)
                                   
            self.setWindowTitle("Request calculation / printing")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
                                                      
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved\n   dj.jansen@casema.nl'), 6, 0, 2, 3, Qt.AlignCenter)
                             
            self.printBtn = QPushButton('Calculation\nPrinting')
            self.printBtn.clicked.connect(lambda: printCalculatie(mcalnr, mwerknr))
            grid.addWidget(self.printBtn, 4, 2)
            self.printBtn.setFont(QFont("Arial",10))
            self.printBtn.setFixedWidth(100)
            self.printBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            self.artprintBtn = QPushButton('Article list\nPrinting')
            self.artprintBtn.clicked.connect(lambda: printArtikellijst(mcalnr, mwerknr))
            grid.addWidget(self.artprintBtn, 4, 1, 1, 1, Qt.AlignRight)
            self.artprintBtn.setFont(QFont("Arial",10))
            self.artprintBtn.setFixedWidth(100)
            self.artprintBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            self.toonBtn = QPushButton('Calculation\nRequesting')
            self.toonBtn.clicked.connect(lambda: toonCalculatie(mcalnr, mwerknr))
            grid.addWidget(self.toonBtn, 5, 2)
            self.toonBtn.setFont(QFont("Arial",10))
            self.toonBtn.setFixedWidth(100)
            self.toonBtn.setStyleSheet("color: black;  background-color: gainsboro")
              
            self.artlijstBtn = QPushButton('Article list\nRequesting')
            self.artlijstBtn.clicked.connect(lambda: toonArtikellijst(mcalnr, mwerknr))
            grid.addWidget(self.artlijstBtn,5, 1, 1, 1, Qt.AlignRight)
            self.artlijstBtn.setFont(QFont("Arial",10))
            self.artlijstBtn.setFixedWidth(100)
            self.artlijstBtn.setStyleSheet("color: black;  background-color: gainsboro")
           
            self.terugBtn = QPushButton('B\na\nc\nk')
            self.terugBtn.clicked.connect(self.close)
            grid.addWidget(self.terugBtn, 4, 1, 5, 1, Qt.AlignTop)
            self.terugBtn.setFont(QFont("Arial", 10))
            self.terugBtn.setFixedWidth(40)
            self.terugBtn.setFixedHeight(115)
            self.terugBtn.setStyleSheet("color: black;  background-color: gainsboro")
                                             
            self.setLayout(grid)
            self.setGeometry(500, 100, 150, 150)
                
    mainWin = MainWindow()
    mainWin.exec_()
    zoekCalculatie(m_email)
   
def opbouwRp(mcalnr, mwerkomschr, mverw, mwerknr, m_email):
    logger.warning(">>> Entering opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s)", mcalnr, mwerkomschr, mverw, mwerknr, m_email, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
    metadata = MetaData()
    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): metadata → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, metadata, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
    icalculaties = Table('icalculaties', metadata,
        Column('icalcID', Integer(), primary_key=True),
        Column('iclusterID', None, ForeignKey('iclusters.iclusterID')),
        Column('hoeveelheid', Float),
        Column('icalculatie', Integer),
        Column('materialen', Float))
    icluster_artikelen = Table('icluster_artikelen', metadata,
        Column('icluster_artID',Integer, primary_key=True),
        Column('artikelID', None, ForeignKey('artikelen.artikelID')),
        Column('iclusterID', None, ForeignKey('iclusters.iclusterID')),
        Column('hoeveelheid', Float))
    artikelen = Table('artikelen', metadata,
        Column('artikelID', Integer(), primary_key=True),
        Column('artikelprijs', Float))
   
    params_finance = Table('params_finance', metadata,
        Column('financeID', Integer, primary_key=True),
        Column('factor', Float),
        Column('item', String))

    params_hours = Table('params_hours', metadata,
       Column('rateID', Integer, primary_key=True),
       Column('hourly_tariff', Float),
       Column('item', String))

    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
    selpar = select([params_finance]).order_by(params_finance.c.financeID)
    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): selpar → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, selpar, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
    rppar = con.execute(selpar).fetchall()
    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): rppar → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, rppar, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
    selpar1 = select([params_hours]).order_by(params_hours.c.rateID)
    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): selpar1 → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, selpar1, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
    rppar1 = con.execute(selpar1).fetchall()
    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): rppar1 → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, rppar1, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
    
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): engine → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, engine, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
    con = engine.connect()
    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): con → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, con, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
    selmat=select([icalculaties, icluster_artikelen, artikelen]).where(and_(\
            icalculaties.c.icalculatie == mcalnr,\
            icalculaties.c.iclusterID == icluster_artikelen.c.iclusterID,\
            icluster_artikelen.c.artikelID == artikelen.c.artikelID))
    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): selmat → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, selmat, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
    rpmat = con.execute(selmat)
    for rij in rpmat:
        logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): rpmat → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, rpmat, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
        updcalmat = update(icalculaties).where(and_(icalculaties.c.icalculatie ==\
           mcalnr, icalculaties.c.iclusterID == rij[1],\
           icluster_artikelen.c.artikelID == rij[9])).values(\
           materialen = icalculaties.c.materialen+rij[2]*rij[8]*rij[10]*(1+rppar[6][1]))
        con.execute(updcalmat)
        logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): updcalmat → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, updcalmat, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
        logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): materialen → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, materialen, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
   
    metadata = MetaData()
    icalculaties = Table('icalculaties', metadata,
        Column('icalcID', Integer(), primary_key=True),
        Column('iclusterID', None, ForeignKey('iclusters.iclusterID')),
        Column('koppelnummer', Integer),
        Column('icalculatie', Integer),
        Column('omschrijving', String),
        Column('hoeveelheid', Float),
        Column('eenheid', String),
        Column('prijs', Float),
        Column('materialen', Float),
        Column('lonen', Float),
        Column('szagen', Float),
        Column('zagen', Float),
        Column('sschaven', Float),
        Column('schaven', Float),
        Column('ssteken', Float),
        Column('steken', Float),
        Column('sboren', Float),
        Column('boren', Float),
        Column('sfrezen', Float),
        Column('frezen', Float),
        Column('sdraaien_klein', Float),
        Column('draaien_klein', Float),
        Column('sdraaien_groot', Float),
        Column('draaien_groot', Float),
        Column('stappen', Float),
        Column('tappen', Float),
        Column('snube_draaien', Float),
        Column('nube_draaien', Float),
        Column('snube_bewerken', Float),
        Column('nube_bewerken', Float),
        Column('sknippen', Float),
        Column('knippen', Float),
        Column('skanten', Float),
        Column('kanten', Float),
        Column('sstansen', Float),
        Column('stansen', Float),
        Column('slassen_co2', Float),
        Column('lassen_co2', Float),
        Column('slassen_hand', Float),
        Column('lassen_hand', Float),
        Column('sverpakken', Float),
        Column('verpakken', Float),
        Column('sverzinken', Float),
        Column('verzinken', Float),
        Column('smoffelen', Float),
        Column('moffelen', Float),
        Column('sschilderen', Float),
        Column('schilderen', Float),
        Column('sspuiten', Float),
        Column('spuiten', Float),
        Column('sponsen', Float),
        Column('ponsen', Float),
        Column('spersen', Float),
        Column('persen', Float),
        Column('sgritstralen', Float),
        Column('gritstralen', Float),
        Column('smontage', Float),
        Column('montage', Float),
        Column('werkomschrijving', String),
        Column('verwerkt', Integer))
    iclusters = Table('iclusters', metadata,
        Column('iclusterID', Integer(), primary_key=True),
        Column('omschrijving', String),
        Column('prijs', Float),
        Column('eenheid', String),
        Column('materialen', Float),
        Column('lonen', Float),
        Column('szagen', Float),
        Column('zagen', Float),
        Column('sschaven', Float),
        Column('schaven', Float),
        Column('ssteken', Float),
        Column('steken', Float),
        Column('sboren', Float),
        Column('boren', Float),
        Column('sfrezen', Float),
        Column('frezen', Float),
        Column('sdraaien_klein', Float),
        Column('draaien_klein', Float),
        Column('sdraaien_groot', Float),
        Column('draaien_groot', Float),
        Column('stappen', Float),
        Column('tappen', Float),
        Column('snube_draaien', Float),
        Column('nube_draaien', Float),
        Column('snube_bewerken', Float),
        Column('nube_bewerken', Float),
        Column('sknippen', Float),
        Column('knippen', Float),
        Column('skanten', Float),
        Column('kanten', Float),
        Column('sstansen', Float),
        Column('stansen', Float),
        Column('slassen_co2', Float),
        Column('lassen_co2', Float),
        Column('slassen_hand', Float),
        Column('lassen_hand', Float),
        Column('sverpakken', Float),
        Column('verpakken', Float),
        Column('sverzinken', Float),
        Column('verzinken', Float),
        Column('smoffelen', Float),
        Column('moffelen', Float),
        Column('sschilderen', Float),
        Column('schilderen', Float),
        Column('sspuiten', Float),
        Column('spuiten', Float),
        Column('sponsen', Float),
        Column('ponsen', Float),
        Column('spersen', Float),
        Column('persen', Float),
        Column('sgritstralen', Float),
        Column('gritstralen', Float),
        Column('smontage', Float),
        Column('montage', Float))
    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): schaven → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, schaven, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
    icluster_artikelen = Table('icluster_artikelen', metadata,
        Column('icluster_artID',Integer, primary_key=True),
        Column('artikelID', None, ForeignKey('artikelen.artikelID')),
        Column('iclusterID', None, ForeignKey('iclusters.iclusterID')),
        Column('hoeveelheid', Float))
    artikelen = Table('artikelen', metadata,
        Column('artikelID', Integer(), primary_key=True),
        Column('artikelomschrijving', String),
        Column('artikelprijs', Float),
        Column('art_eenheid', String))
    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): selclart → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, selclart, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
    materiaallijsten = Table('materiaallijsten', metadata,
        Column('matlijstID', Integer, primary_key=True),
        Column('icalculatie', Integer),
        Column('hoeveelheid', Float),
        Column('artikelID', None, ForeignKey('artikelen.artikelID')),
        Column('artikelprijs', Float),
        Column('subtotaal', Float),
        Column('resterend', Float))

    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
    
    selcalc = select([icalculaties]).where(icalculaties.c.icalculatie == int(mcalnr))
    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): selcalc → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, selcalc, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
    rpcalc = con.execute(selcalc)
    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): rpcalc → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, rpcalc, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
    selclart = select([icluster_artikelen,artikelen]).where(and_(icluster_artikelen.c.\
      artikelID == artikelen.c.artikelID, icalculaties.c.iclusterID ==\
      icluster_artikelen.c.iclusterID, icalculaties.c.icalculatie == (int(mcalnr))))\
      .order_by(icluster_artikelen.c.iclusterID, icluster_artikelen.c.artikelID)
    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): zagen → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, zagen, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): updcalc → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, updcalc, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
    rpclart = con.execute(selclart)
    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): rpclart → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, rpclart, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
    for record in rpcalc:
        updcalc = update(icalculaties).where(and_(icalculaties.c.icalculatie == record[3],\
           icalculaties.c.iclusterID == iclusters.c.iclusterID)).values(verwerkt = 1,\
           zagen = (icalculaties.c.zagen+iclusters.c.zagen)*icalculaties.c.hoeveelheid,\
           szagen = icalculaties.c.szagen+iclusters.c.szagen,\
           schaven = (icalculaties.c.schaven+iclusters.c.schaven)*icalculaties.c.hoeveelheid,\
           sschaven = icalculaties.c.sschaven+iclusters.c.schaven,\
           steken = (icalculaties.c.steken+iclusters.c.steken)*icalculaties.c.hoeveelheid,\
           ssteken = icalculaties.c.ssteken+iclusters.c.steken,\
           boren = (icalculaties.c.boren+iclusters.c.boren)*icalculaties.c.hoeveelheid,\
           sboren = icalculaties.c.sboren+iclusters.c.sboren,\
           frezen = (icalculaties.c.frezen+iclusters.c.frezen)*icalculaties.c.hoeveelheid,\
           sfrezen = icalculaties.c.sfrezen+iclusters.c.sfrezen,\
           draaien_klein = (icalculaties.c.draaien_klein+iclusters.c.draaien_klein)*icalculaties.c.hoeveelheid,\
           sdraaien_klein = icalculaties.c.sdraaien_klein+iclusters.c.sdraaien_klein,\
           draaien_groot = (icalculaties.c.draaien_groot+iclusters.c.draaien_groot)*icalculaties.c.hoeveelheid,\
           sdraaien_groot = icalculaties.c.sdraaien_groot+iclusters.c.sdraaien_groot,\
           tappen = (icalculaties.c.tappen+iclusters.c.tappen)*icalculaties.c.hoeveelheid,\
           stappen = icalculaties.c.stappen+iclusters.c.stappen,\
           nube_draaien = (icalculaties.c.nube_draaien+iclusters.c.nube_draaien)*icalculaties.c.hoeveelheid,\
           snube_draaien = icalculaties.c.snube_draaien+iclusters.c.snube_draaien,\
           nube_bewerken = (icalculaties.c.nube_bewerken+iclusters.c.nube_bewerken)*icalculaties.c.hoeveelheid,\
           snube_bewerken = icalculaties.c.snube_bewerken+iclusters.c.snube_bewerken,\
           knippen = (icalculaties.c.knippen+iclusters.c.knippen)*icalculaties.c.hoeveelheid,\
           sknippen = icalculaties.c.sknippen+iclusters.c.sknippen,\
           kanten = (icalculaties.c.kanten+iclusters.c.kanten)*icalculaties.c.hoeveelheid,\
           skanten = icalculaties.c.skanten+iclusters.c.skanten,\
           stansen = (icalculaties.c.stansen+iclusters.c.stansen)*icalculaties.c.hoeveelheid,\
           sstansen = icalculaties.c.sstansen+iclusters.c.sstansen,\
           lassen_co2 = (icalculaties.c.lassen_co2+iclusters.c.lassen_co2)*icalculaties.c.hoeveelheid,\
           slassen_co2 = icalculaties.c.slassen_co2+iclusters.c.slassen_co2,\
           lassen_hand = (icalculaties.c.lassen_hand+iclusters.c.lassen_hand)*icalculaties.c.hoeveelheid,\
           slassen_hand = icalculaties.c.slassen_hand+iclusters.c.slassen_hand,\
           verpakken = (icalculaties.c.verpakken+iclusters.c.verpakken)*icalculaties.c.hoeveelheid,\
           sverpakken = icalculaties.c.sverpakken+iclusters.c.sverpakken,\
           verzinken = (icalculaties.c.verzinken+iclusters.c.verzinken)*icalculaties.c.hoeveelheid,\
           sverzinken = icalculaties.c.sverzinken+iclusters.c.sverzinken,\
           moffelen = (icalculaties.c.moffelen+iclusters.c.moffelen)*icalculaties.c.hoeveelheid,\
           smoffelen = icalculaties.c.smoffelen+iclusters.c.smoffelen,\
           schilderen = (icalculaties.c.schilderen+iclusters.c.schilderen)*icalculaties.c.hoeveelheid,\
           sschilderen = icalculaties.c.sschilderen+iclusters.c.sschilderen,\
           spuiten = (icalculaties.c.spuiten+iclusters.c.spuiten)*icalculaties.c.hoeveelheid,\
           sspuiten = icalculaties.c.sspuiten+iclusters.c.sspuiten,\
           ponsen = (icalculaties.c.ponsen+iclusters.c.ponsen)*icalculaties.c.hoeveelheid,\
           sponsen = icalculaties.c.sponsen+iclusters.c.sponsen,\
           persen = (icalculaties.c.persen+iclusters.c.persen)*icalculaties.c.hoeveelheid,\
           spersen = icalculaties.c.spersen+iclusters.c.spersen,\
           gritstralen = (icalculaties.c.gritstralen+iclusters.c.gritstralen)*icalculaties.c.hoeveelheid,\
           sgritstralen = icalculaties.c.sgritstralen+iclusters.c.sgritstralen,\
           montage = (icalculaties.c.montage+iclusters.c.montage)*icalculaties.c.hoeveelheid,\
           smontage = icalculaties.c.smontage+iclusters.c.smontage,\
           lonen = (icalculaties.c.zagen+iclusters.c.zagen)*rppar1[11][1]*icalculaties.c.hoeveelheid+\
           (icalculaties.c.szagen+iclusters.c.szagen)*rppar1[11][1]+\
           (icalculaties.c.schaven+iclusters.c.schaven)*rppar1[12][1]*icalculaties.c.hoeveelheid+\
           (icalculaties.c.sschaven+iclusters.c.sschaven)*rppar1[12][1]+\
           (icalculaties.c.steken+iclusters.c.steken)*rppar1[13][1]*icalculaties.c.hoeveelheid+\
           (icalculaties.c.ssteken+iclusters.c.ssteken)*rppar1[13][1]+\
           (icalculaties.c.boren+iclusters.c.boren)*rppar1[14][1]*icalculaties.c.hoeveelheid+\
           (icalculaties.c.sboren+iclusters.c.sboren)*rppar1[14][1]+\
           (icalculaties.c.frezen+iclusters.c.frezen)*rppar1[15][1]*icalculaties.c.hoeveelheid+\
           (icalculaties.c.sfrezen+iclusters.c.sfrezen)*rppar1[15][1]+\
           (icalculaties.c.draaien_klein+iclusters.c.draaien_klein)*rppar1[16][1]*icalculaties.c.hoeveelheid+\
           (icalculaties.c.sdraaien_klein+iclusters.c.sdraaien_klein)*rppar1[16][1]+\
           (icalculaties.c.draaien_groot+iclusters.c.draaien_groot)*rppar1[17][1]*icalculaties.c.hoeveelheid+\
           (icalculaties.c.sdraaien_groot+iclusters.c.sdraaien_groot)*rppar1[17][1]+\
           (icalculaties.c.tappen+iclusters.c.tappen)*rppar1[18][1]*icalculaties.c.hoeveelheid+\
           (icalculaties.c.stappen+iclusters.c.stappen)*rppar1[18][1]+\
           (icalculaties.c.nube_draaien+iclusters.c.nube_draaien)*rppar1[19][1]*icalculaties.c.hoeveelheid+\
           (icalculaties.c.snube_draaien+iclusters.c.snube_draaien)*rppar1[19][1]+\
           (icalculaties.c.nube_bewerken+iclusters.c.nube_bewerken)*rppar1[20][1]*icalculaties.c.hoeveelheid+\
           (icalculaties.c.snube_bewerken+iclusters.c.snube_bewerken)*rppar1[20][1]+\
           (icalculaties.c.knippen+iclusters.c.knippen)*rppar1[21][1]*icalculaties.c.hoeveelheid+\
           (icalculaties.c.sknippen+iclusters.c.sknippen)*rppar1[21][1]+\
           (icalculaties.c.kanten+iclusters.c.kanten)*rppar1[22][1]*icalculaties.c.hoeveelheid+\
           (icalculaties.c.skanten+iclusters.c.skanten)*rppar1[22][1]+\
           (icalculaties.c.stansen+iclusters.c.stansen)*rppar1[23][1]*icalculaties.c.hoeveelheid+\
           (icalculaties.c.sstansen+iclusters.c.sstansen)*rppar1[23][1]+\
           (icalculaties.c.lassen_co2+iclusters.c.lassen_co2)*rppar1[24][1]*icalculaties.c.hoeveelheid+\
           (icalculaties.c.slassen_co2+iclusters.c.slassen_co2)*rppar1[24][1]+\
           (icalculaties.c.lassen_hand+iclusters.c.lassen_hand)*rppar1[25][1]*icalculaties.c.hoeveelheid+\
           (icalculaties.c.slassen_hand+iclusters.c.slassen_hand)*rppar1[25][1]+\
           (icalculaties.c.verpakken+iclusters.c.verpakken)*rppar1[26][1]*icalculaties.c.hoeveelheid+\
           (icalculaties.c.sverpakken+iclusters.c.sverpakken)*rppar1[26][1]+\
           (icalculaties.c.verzinken+iclusters.c.verzinken)*rppar1[27][1]*icalculaties.c.hoeveelheid+\
           (icalculaties.c.sverzinken+iclusters.c.sverzinken)*rppar1[27][1]+\
           (icalculaties.c.moffelen+iclusters.c.moffelen)*rppar1[28][1]*icalculaties.c.hoeveelheid+\
           (icalculaties.c.smoffelen+iclusters.c.smoffelen)*rppar1[28][1]+\
           (icalculaties.c.schilderen+iclusters.c.schilderen)*rppar1[29][1]*icalculaties.c.hoeveelheid+\
           (icalculaties.c.sschilderen+iclusters.c.sschilderen)*rppar1[29][1]+\
           (icalculaties.c.spuiten+iclusters.c.spuiten)*rppar1[30][1]*icalculaties.c.hoeveelheid+\
           (icalculaties.c.sspuiten+iclusters.c.sspuiten)*rppar1[30][1]+\
           (icalculaties.c.ponsen+iclusters.c.ponsen)*rppar1[31][1]*icalculaties.c.hoeveelheid+\
           (icalculaties.c.sponsen+iclusters.c.sponsen)*rppar1[31][1]+\
           (icalculaties.c.persen+iclusters.c.persen)*rppar1[32][1]*icalculaties.c.hoeveelheid+\
           (icalculaties.c.spersen+iclusters.c.spersen)*rppar1[32][1]+\
           (icalculaties.c.gritstralen+iclusters.c.gritstralen)*rppar1[33][1]*icalculaties.c.hoeveelheid+\
           (icalculaties.c.sgritstralen+iclusters.c.sgritstralen)*rppar1[33][1]+\
           (icalculaties.c.montage+iclusters.c.montage)*rppar1[34][1]*icalculaties.c.hoeveelheid+\
           (icalculaties.c.smontage+iclusters.c.smontage)*rppar1[34][1])
        logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): steken → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, steken, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
        logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): boren → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, boren, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
        logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): frezen → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, frezen, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
        logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): draaien_klein → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, draaien_klein, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
            
        con.execute(updcalc)
        for row in rpclart:
            selart = select([materiaallijsten.c.artikelID, materiaallijsten.c.icalculatie]).where(and_(materiaallijsten.\
                c.artikelID == row[1], materiaallijsten.c.icalculatie == record[3]))
            logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): draaien_groot → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, draaien_groot, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
            logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): tappen → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, tappen, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
            logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): nube_draaien → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, nube_draaien, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
            rpart = con.execute(selart).first()
            if rpart:
                updmatlijst = update(materiaallijsten).where(and_(materiaallijsten.c.\
                  artikelID == row[1], materiaallijsten.c.icalculatie == record[3]))\
                 .values(hoeveelheid = materiaallijsten.c.hoeveelheid+(record[5]*row[3]),\
                artikelprijs = row[6]*(1+rppar[6][1]), subtotaal = materiaallijsten.\
                c.subtotaal+record[5]*row[3]*row[6]*(1+rppar[6][1]))
                logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): knippen → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, knippen, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
                logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): nube_bewerken → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, nube_bewerken, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
                logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): stansen → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, stansen, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
                logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): kanten → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, kanten, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
                logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): lassen_co2 → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, lassen_co2, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
                logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): lassen_hand → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, lassen_hand, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
                con.execute(updmatlijst)
            elif not rpart:
                mmatlijstnr = (con.execute(select([func.max(materiaallijsten.c.matlijstID,\
                        type_=Integer).label('mmatlijstnr')])).scalar())
                mmatlijstnr += 1
                insmatlijst = insert(materiaallijsten).values(matlijstID = mmatlijstnr,\
                    icalculatie = record[3], artikelID = row[1],\
                    hoeveelheid = record[5]*row[3], resterend = record[5]*row[3],\
                    artikelprijs = row[6]*(1+rppar[6][1]),\
                    subtotaal = record[5]*row[3]*row[6]*(1+rppar[6][1]))
                logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): verpakken → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, verpakken, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
                logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): verzinken → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, verzinken, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
                con.execute(insmatlijst)
        selber = select([icalculaties.c.icalcID, icalculaties.c.icalculatie])\
                           .where(icalculaties.c.icalculatie == mcalnr)
        logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): schilderen → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, schilderen, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
        logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): moffelen → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, moffelen, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
        logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): spuiten → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, spuiten, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
        logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): ponsen → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, ponsen, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
        rpselber = con.execute(selber)
        for regel in rpselber:
            updber = update(icalculaties).where(icalculaties.c.icalculatie==mcalnr)\
             .values(prijs=icalculaties.c.materialen+icalculaties.c.lonen,\
              werkomschrijving = mwerkomschr)
            logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): persen → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, persen, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
            logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): gritstralen → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, gritstralen, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
            logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): montage → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, montage, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
            logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): selart → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, selart, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
            logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): lonen → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, lonen, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
            con.execute(updber)
    opvragenCalc(mcalnr, mwerkomschr, mverw, mwerknr, m_email)
    logger.debug("<<< Exiting opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s)", mcalnr, mwerkomschr, mverw, mwerknr, m_email, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
                        
def printCalculatie(mcalnr, mwerknr):
    from sys import platform
    metadata = MetaData()
    logger.warning(">>> Entering printCalculatie(mcalnr=%s,mwerknr=%s)", mcalnr, mwerknr, extra={"event.action": "printCalculatie", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    logger.debug("printCalculatie(mcalnr=%s,mwerknr=%s): metadata → %s", mcalnr, mwerknr, metadata, extra={"event.action": "printCalculatie", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    icalculaties = Table('icalculaties', metadata,
        Column('icalcID', Integer(), primary_key=True),
        Column('iclusterID', None, ForeignKey('iclusters.iclusterID')),
        Column('koppelnummer', Integer),
        Column('icalculatie', Integer),
        Column('omschrijving', String),
        Column('hoeveelheid', Float),
        Column('eenheid', String),
        Column('prijs', Float),
        Column('materialen', Float),
        Column('lonen', Float),
        Column('werkomschrijving', String))
    
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("printCalculatie(mcalnr=%s,mwerknr=%s): engine → %s", mcalnr, mwerknr, engine, extra={"event.action": "printCalculatie", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    con = engine.connect()
    logger.debug("printCalculatie(mcalnr=%s,mwerknr=%s): con → %s", mcalnr, mwerknr, con, extra={"event.action": "printCalculatie", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    
    selcal = select([icalculaties]).where(icalculaties.c.icalculatie == mcalnr)
    logger.debug("printCalculatie(mcalnr=%s,mwerknr=%s): selcal → %s", mcalnr, mwerknr, selcal, extra={"event.action": "printCalculatie", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    rpcal = con.execute(selcal)
    logger.debug("printCalculatie(mcalnr=%s,mwerknr=%s): rpcal → %s", mcalnr, mwerknr, rpcal, extra={"event.action": "printCalculatie", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    
    mblad = 1
    logger.debug("printCalculatie(mcalnr=%s,mwerknr=%s): mblad → %s", mcalnr, mwerknr, mblad, extra={"event.action": "printCalculatie", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    rgl = 0
    mmat = 0
    logger.debug("printCalculatie(mcalnr=%s,mwerknr=%s): mmat → %s", mcalnr, mwerknr, mmat, extra={"event.action": "printCalculatie", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    mlon = 0
    logger.debug("printCalculatie(mcalnr=%s,mwerknr=%s): mlon → %s", mcalnr, mwerknr, mlon, extra={"event.action": "printCalculatie", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    mtotaal = 0
    logger.debug("printCalculatie(mcalnr=%s,mwerknr=%s): mtotaal → %s", mcalnr, mwerknr, mtotaal, extra={"event.action": "printCalculatie", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    for row in rpcal:
        if rgl == 0 or rgl%57 == 0:
            if platform == 'win32':
                filename = '.\\forms\\Intern_Clustercalculaties\\clustercalculation_'+str(row[3])+'-'+str(mwerknr)+'.txt'
            else:
                filename = './forms/Intern_Clustercalculaties/clustercalculation_'+str(row[3])+'-'+str(mwerknr)+'.txt'
                logger.debug("printCalculatie(mcalnr=%s,mwerknr=%s): filename → %s", mcalnr, mwerknr, filename, extra={"event.action": "printCalculatie", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
            kop=\
    ('Work order: '+ str(mwerknr)+' '+'{:<24.24s}'.format(str(row[10]))+'  Calculation: '+str(row[3])+'  Date: '+str(datetime.datetime.now())[0:10]+'  Page : '+str(mblad)+'\n'+
    '================================================================================================\n'+
    'Cluster  Description        Unit    Number  Materials        Wages                       Amount\n'+
    '================================================================================================\n')
            logger.debug("printCalculatie(mcalnr=%s,mwerknr=%s): kop → %s", mcalnr, mwerknr, kop, extra={"event.action": "printCalculatie", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
            if rgl == 0:
                open(filename, 'w').write(kop)
            elif rgl%57 == 0:
                open(filename, 'a').write(kop)
            mblad += 1
            
        open(filename,'a').write('{:<9s}'.format(row[1])+'{:<23.21}'.format(row[4])+'{:<5s}'.format(row[6])+'{:5.2f}'.format(row[5])+'{:12.2f}'.format(row[8])+'{:12.2f}'.format(row[9])+'                 '+'{:12.2f}'.format(row[7])+'\n')
        mmat = mmat+row[8]
        mlon = mlon+row[9]
        mtotaal = mtotaal+row[7]
        rgl += 1
    tail =(\
    '-------------------------------------------------------------------------------------------------\n'+
    'Totals                                    '+'{:12.2f}'.format(mmat)+'{:12.2f}'.format(mlon)+'                 '+'{:12.2f}'.format(mtotaal)+'\n'
    '=================================================================================================\n')    
    open(filename,'a').write(tail)
    if platform == 'win32':
        os.startfile(filename, "print")
    else:
        os.system("lpr "+filename)
    printing()
    logger.debug("<<< Exiting printCalculatie(mcalnr=%s,mwerknr=%s)", mcalnr, mwerknr, extra={"event.action": "printCalculatie", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
                     
def printArtikellijst(mcalnr, mwerknr):
    logger.warning(">>> Entering printArtikellijst(mcalnr=%s,mwerknr=%s)", mcalnr, mwerknr, extra={"event.action": "printArtikellijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    from sys import platform
    metadata = MetaData()
    logger.debug("printArtikellijst(mcalnr=%s,mwerknr=%s): metadata → %s", mcalnr, mwerknr, metadata, extra={"event.action": "printArtikellijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    materiaallijsten = Table('materiaallijsten', metadata,
         Column('matlijstID', Integer, primary_key=True),
         Column('icalculatie', Integer),
         Column('artikelID', None, ForeignKey('artikelen.artikelID')),
         Column('artikelprijs', Float),
         Column('hoeveelheid', Float),
         Column('subtotaal', Float))
    artikelen = Table('artikelen', metadata,
         Column('artikelID', Integer(), primary_key=True),
         Column('artikelomschrijving', String),
         Column('art_eenheid', String),
         Column('locatie_magazijn', String))
    icalculaties = Table('icalculaties', metadata,
        Column('icalculatie', Integer),
        Column('koppelnummer', Integer))
                                    
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("printArtikellijst(mcalnr=%s,mwerknr=%s): engine → %s", mcalnr, mwerknr, engine, extra={"event.action": "printArtikellijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    con = engine.connect()
    logger.debug("printArtikellijst(mcalnr=%s,mwerknr=%s): con → %s", mcalnr, mwerknr, con, extra={"event.action": "printArtikellijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    
    selmat = select([materiaallijsten, artikelen])\
      .where(and_(materiaallijsten.c.artikelID == artikelen.c.artikelID,\
      materiaallijsten.c.artikelID == artikelen.c.artikelID,\
      materiaallijsten.c.icalculatie == mcalnr)).order_by(materiaallijsten.c.artikelID)
    logger.debug("printArtikellijst(mcalnr=%s,mwerknr=%s): selmat → %s", mcalnr, mwerknr, selmat, extra={"event.action": "printArtikellijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    rpmat = con.execute(selmat)
    logger.debug("printArtikellijst(mcalnr=%s,mwerknr=%s): rpmat → %s", mcalnr, mwerknr, rpmat, extra={"event.action": "printArtikellijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    selkop = select([icalculaties]).where(icalculaties.c.icalculatie == mcalnr)
    logger.debug("printArtikellijst(mcalnr=%s,mwerknr=%s): selkop → %s", mcalnr, mwerknr, selkop, extra={"event.action": "printArtikellijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    rpkop = con.execute(selkop).first()
    logger.debug("printArtikellijst(mcalnr=%s,mwerknr=%s): rpkop → %s", mcalnr, mwerknr, rpkop, extra={"event.action": "printArtikellijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    mblad = 1
    logger.debug("printArtikellijst(mcalnr=%s,mwerknr=%s): mblad → %s", mcalnr, mwerknr, mblad, extra={"event.action": "printArtikellijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    rgl = 0
    for row in rpmat:
        if rgl == 0 or rgl%57 == 0:
            if platform == 'win32':
                filename =  filename = '.\\forms\\Intern_Clustercalculaties\\materials_list_'+str(rpkop[0])+'-'+str(mwerknr)+'.txt'
            else:
                filename =  filename = './forms/Intern_Clustercalculaties/materials_list_'+str(rpkop[0])+'-'+str(mwerknr)+'.txt'
                logger.debug("printArtikellijst(mcalnr=%s,mwerknr=%s): filename → %s", mcalnr, mwerknr, filename, extra={"event.action": "printArtikellijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
            kop=\
    ('Work order   '+ str(mwerknr)+'  Calculation:'+str(rpkop[0])+'   Date : '+str(datetime.datetime.now())[0:10]+'  Page :  '+str(mblad)+'\n'+
    '=============================================================================================\n'+
    'Articlenr  Description                         Unit          Price      Number               \n'+
    '=============================================================================================\n')
            logger.debug("printArtikellijst(mcalnr=%s,mwerknr=%s): kop → %s", mcalnr, mwerknr, kop, extra={"event.action": "printArtikellijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
            if rgl == 0:
                open(filename, 'w').write(kop)
            elif rgl%57 == 0:
                open(filename, 'a').write(kop)
            mblad += 1
            
        open(filename,'a').write('{:<11d}'.format(row[6])+'{:<37.35s}'.format(row[7])+'{:<8.6s}'.format(row[8])+'{:10.2f}'.format(row[3])+'  '+'{:10.2f}'.format(row[4])+'\n')
        rgl += 1
    if platform == 'win32':
        os.startfile(filename, "print")
    else:
        os.system("lpr "+filename)
    printing()
    logger.debug("<<< Exiting printArtikellijst(mcalnr=%s,mwerknr=%s)", mcalnr, mwerknr, extra={"event.action": "printArtikellijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
        
def toonCalculatie(mcalnr, mwerknr):
    logger.warning(">>> Entering toonCalculatie(mcalnr=%s,mwerknr=%s)", mcalnr, mwerknr, extra={"event.action": "toonCalculatie", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    class MyWindow(QDialog):
        def __init__(self, data_list, header, *args):
            QWidget.__init__(self, *args,)
            self.setGeometry(50, 50, 1800, 900)
            self.setWindowTitle('Cluster calculation')
            self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
            self.setWindowFlags(self.windowFlags()| Qt.WindowSystemMenuHint |
                              Qt.WindowMinMaxButtonsHint)
            table_model = MyTableModel(self, data_list, header)
            table_view = QTableView()
            table_view.setModel(table_model)
            font = QFont("Arial", 10)
            table_view.setFont(font)
            table_view.resizeColumnsToContents()
            table_view.setSelectionBehavior(QTableView.SelectRows)
            #table_view.clicked.connect(selectRow)
            table_view.clicked.connect(ShowSelection)
            layout = QVBoxLayout(self)
            layout.addWidget(table_view)
            self.setLayout(layout)
    
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
             
    header = ['ID','Calculation','Cluster number', 'Description','Work description','Processed',
      'Amount','Unit','Link number','Total price','Materials', 'Wages',\
      'Equipment','Services','Hiring','Set costs\nsawing','Sawing','Set costs\nplaning','Planing',\
      'Set costs\nstabbing','Stabbing','Set costs\ndrilling','Drilling','Set costs\nmilling','Milling','Set costs\nturning small',\
      'Turning small','Set costs\nturning big','Turning big','Set costs\nthreading','Threading',\
      'Set costs\nCNC turning','CNC turning','Set costs\nCNC milling','CNC milling',\
      'Set costs\ncutting','Cutting','Set costs\nfolding','Folding','Set costs\ndie-cutting','Die-cutting',\
      'Set costs\nwelding co2','Welding co2','Set costs\nwelding hand','Welding hand','Set costs\npacking',\
      'Packing','Set costs\ngalvanise','Galvanise','Set costs\nmuffling','Muffling','Set costs\npainting',\
      'Painting','Set costs\nspraying','Spraying','Set costs\nstamping','Stamping','Set costs\npressing',\
      'Pressing','Set costs\ngrit blasting','Grit blasting','Set costs\nmounting','Mounting']

    metadata = MetaData()               
    icalculaties = Table('icalculaties', metadata,
        Column('icalcID', Integer(), primary_key=True),
        Column('icalculatie', Integer),
        Column('iclusterID', None, ForeignKey('iclusters.iclusterID')),
        Column('omschrijving', String),
        Column('werkomschrijving', String),
        Column('verwerkt', Integer),
        Column('hoeveelheid', Float),
        Column('eenheid', String),
        Column('koppelnummer', Integer),
        Column('prijs', Float),
        Column('materialen', Float),
        Column('lonen', Float),
        Column('materieel', Float),
        Column('diensten', Float),
        Column('inhuur', Float),
        Column('szagen', Float),
        Column('zagen', Float),
        Column('sschaven', Float),
        Column('schaven', Float),
        Column('ssteken', Float),
        Column('steken', Float),
        Column('sboren', Float),
        Column('boren', Float),
        Column('sfrezen', Float),
        Column('frezen', Float),
        Column('sdraaien_klein', Float),
        Column('draaien_klein', Float),
        Column('sdraaien_groot', Float),
        Column('draaien_groot', Float),
        Column('stappen', Float),
        Column('tappen', Float),
        Column('snube_draaien', Float),
        Column('nube_draaien', Float),
        Column('snube_bewerken', Float),
        Column('nube_bewerken', Float),
        Column('sknippen', Float),
        Column('knippen', Float),
        Column('skanten', Float),
        Column('kanten', Float),
        Column('sstansen', Float),
        Column('stansen', Float),
        Column('slassen_co2', Float),
        Column('lassen_co2', Float),
        Column('slassen_hand', Float),
        Column('lassen_hand', Float),
        Column('sverpakken', Float),
        Column('verpakken', Float),
        Column('sverzinken', Float),
        Column('verzinken', Float),
        Column('smoffelen', Float),
        Column('moffelen', Float),
        Column('sschilderen', Float),
        Column('schilderen', Float),
        Column('sspuiten', Float),
        Column('spuiten', Float),
        Column('sponsen', Float),
        Column('ponsen', Float),
        Column('spersen', Float),
        Column('persen', Float),
        Column('sgritstralen', Float),
        Column('gritstralen', Float),
        Column('smontage', Float),
        Column('montage', Float))
                                                 
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
    
    selcal = select([icalculaties]).where(icalculaties.c.icalculatie == mcalnr).\
     order_by(icalculaties.c.iclusterID)
    rpcal = con.execute(selcal)
          
    data_list=[]
    for row in rpcal:
        data_list += [(row)]
        
    def ShowSelection(idx):
        logger.warning(">>> Entering ShowSelection(idx=%s)", idx, extra={"event.action": "ShowSelection", "logrite.idx": idx})
        mcalnr = idx.data()
        logger.debug("ShowSelection(idx=%s): mcalnr → %s", idx, mcalnr, extra={"event.action": "ShowSelection", "logrite.idx": idx})
        if  idx.column() == 0:
                     
            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            logger.debug("ShowSelection(idx=%s): engine → %s", idx, engine, extra={"event.action": "ShowSelection", "logrite.idx": idx})
            con = engine.connect()
            logger.debug("ShowSelection(idx=%s): con → %s", idx, con, extra={"event.action": "ShowSelection", "logrite.idx": idx})
            selcal = select([icalculaties]).where(icalculaties.c.icalcID == mcalnr)
            rpcal = con.execute(selcal).first()
            logger.debug("ShowSelection(idx=%s): selcal → %s", idx, selcal, extra={"event.action": "ShowSelection", "logrite.idx": idx})
            logger.debug("ShowSelection(idx=%s): rpcal → %s", idx, rpcal, extra={"event.action": "ShowSelection", "logrite.idx": idx})

            header = ['ID', 'Calculation', 'Cluster number', 'Description', 'Work description', 'Processed','Amount', 'Unit',\
                      'Link number', 'Total price', 'Materials', 'Wages', \
                      'Equipment', 'Services', 'Hiring', 'Set costs\nsawing', 'Sawing', 'Set costs\nplaning', 'Planing', \
                      'Set costs\nstabbing', 'Stabbing', 'Set costs\ndrilling', 'Drilling', 'Set costs\nmilling','Milling', 'Set costs\nturning small', \
                      'Turning small', 'Set costs\nturning big', 'Turning big', 'Set costs\nthreading', 'Threading', \
                      'Set costs\nCNC turning', 'CNC turning', 'Set costs\nCNC milling', 'CNC milling', \
                      'Set costs\ncutting', 'Cutting', 'Set costs\nfolding', 'Folding', 'Set costs\ndie-cutting','Die-cutting', \
                      'Set costs\nwelding co2', 'Welding co2', 'Set costs\nwelding hand', 'Welding hand','Set costs\npacking', \
                      'Packing', 'Set costs\ngalvanise', 'Galvanise', 'Set costs\nmuffling', 'Muffling','Set costs\npainting', \
                      'Painting', 'Set costs\nspraying', 'Spraying', 'Set costs\nstamping', 'Stamping','Set costs\npressing', \
                      'Pressing', 'Set costs\ngrit blasting', 'Grit blasting', 'Set costs\nmounting', 'Mounting']

            logger.debug("ShowSelection(idx=%s): header → %s", idx, header, extra={"event.action": "ShowSelection", "logrite.idx": idx})
            class MainWindow(QDialog):
                logger.debug("<<< Exiting ShowSelection(idx=%s)", idx, extra={"event.action": "ShowSelection", "logrite.idx": idx})
                def __init__(self):
                    QDialog.__init__(self)
                    
                    grid = QGridLayout()
                    grid.setSpacing(20)
                    
                    self.setWindowTitle("Requesting cluster calculation")
                    self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
                    
                    self.setFont(QFont('Arial', 10))   
                                                      
                    self.lbl = QLabel()
                    self.pixmap = QPixmap('./images/logos/verbinding.jpg')
                    self.lbl.setPixmap(self.pixmap)
                    grid.addWidget(self.lbl , 0, 0)
                    
                    grid.addWidget(QLabel('Requesting cluster calculation'),0, 0, 1, 9, Qt.AlignCenter)
            
                    self.logo = QLabel()
                    self.pixmap = QPixmap('./images/logos/logo.jpg')
                    self.logo.setPixmap(self.pixmap)
                    grid.addWidget(self.logo , 0, 9, 1, 1, Qt.AlignRight)                
                    index = 0
                    for item in header:
                        horpos = index%5
                        if index%5 == 0:
                            verpos = index 
                        elif index%5 == 1:
                            verpos = index-1
                        elif index%5 == 2:
                            verpos = index-2
                        elif index%5 == 3:
                            verpos = index -3
                        elif index%5 == 4:
                            verpos = index-4
                        self.lbl = QLabel(header[index])
                        
                        self.Gegevens = QLabel()
                        if type(rpcal[index]) == float :
                            q1Edit = QLineEdit('{:12.2f}'.format(rpcal[index]))
                            q1Edit.setAlignment(Qt.AlignRight)
                        elif  type(rpcal[index]) == int:
                            q1Edit = QLineEdit(str(rpcal[index]))
                            q1Edit.setAlignment(Qt.AlignRight)
                        else:
                            q1Edit = QLineEdit(str(rpcal[index]))
                        q1Edit.setFixedWidth(150)
                        q1Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                        grid.addWidget(self.lbl, verpos+2, horpos+horpos%5)
                        grid.addWidget(q1Edit, verpos+2, horpos+horpos%5+1)
                        q1Edit.setDisabled(True)
    
                        index +=1
                        
                    terugBtn = QPushButton('Close')
                    terugBtn.clicked.connect(self.accept)
            
                    grid.addWidget(terugBtn, verpos+3, 9, 1 , 1, Qt.AlignRight)
                    terugBtn.setFont(QFont("Arial",10))
                    terugBtn.setFixedWidth(100) 
                    terugBtn.setStyleSheet("color: black;  background-color: gainsboro")
                    
                    grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), verpos+4, 0, 1, 9, Qt.AlignCenter)
                                                                            
                    self.setLayout(grid)
                    self.setGeometry(100, 100, 150, 150)
                            
            mainWin = MainWindow()
            mainWin.exec_()
             
    win = MyWindow(data_list, header)
    win.exec_()
            
def toonArtikellijst(mcalnr, mwerknr):
    logger.warning(">>> Entering toonArtikellijst(mcalnr=%s,mwerknr=%s)", mcalnr, mwerknr, extra={"event.action": "toonArtikellijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    class MyWindow(QDialog):
        def __init__(self, data_list, header, *args):
            logger.warning(">>> Entering __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})
            QWidget.__init__(self, *args,)
            self.setGeometry(100, 50, 1700, 900)
            self.setWindowTitle('Material list')
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
            table_view.setColumnHidden(4, True)
            table_view.setSelectionBehavior(QTableView.SelectRows)
            #table_view.clicked.connect(selectRow)
            table_view.clicked.connect(showSelart)
            layout = QVBoxLayout(self)
            logger.debug("__init__(data_list=%s,header=%s): layout → %s", data_list, header, layout, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): layout → %s", self, data_list, header, layout, extra={"event.action": "__init__", "logrite.data_list": data_list})
            layout.addWidget(table_view)
            self.setLayout(layout)
            logger.debug("<<< Exiting __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})
    
    class MyTableModel(QAbstractTableModel):
        def __init__(self, parent, mylist, header, *args):
            QAbstractTableModel.__init__(self, parent, *args)
            self.mylist = mylist
            logger.warning(">>> Entering __init__()", extra={"event.action": "__init__"})
            logger.debug("__init__(): grid → %s", grid, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): grid → %s", self, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.lbl → %s", self.lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.pixmap → %s", self.pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl → %s", self, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.logo → %s", self.logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): logo → %s", self, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Gegevens → %s", self.Gegevens, extra={"event.action": "__init__"})
            logger.debug("__init__(): q1Edit → %s", q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q1Edit → %s", self, q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): terugBtn → %s", terugBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): terugBtn → %s", self, terugBtn, extra={"event.action": "__init__"})
            logger.debug("<<< Exiting __init__()", extra={"event.action": "__init__"})
            self.header = header
        def rowCount(self, parent):
            return len(self.mylist)
        def columnCount(self, parent):
            return len(self.mylist[0])
        def data(self, index, role):
            veld = self.mylist[index.row()][index.column()]
            if not index.isValid():
                return None
            elif role == Qt.TextAlignmentRole and (type(veld) == float or type(veld) == int):
                return Qt.AlignRight | Qt.AlignVCenter
            elif role != Qt.DisplayRole:
                return None
            if type(veld) == float:
                return '{:12.2f}'.format(veld)
            else:
                return veld
        def headerData(self, col, orientation, role):
            if orientation == Qt.Horizontal and role == Qt.DisplayRole:
                return self.header[col]
            return None
             
    header = ['Article number','Description','Reservation balance','ListID','Calculation',\
              'Work number','Order purchase number', 'Article number','Article price',\
              'Amount','Call-off','Remaining','Subtotal','Reservation date',\
              'Delivery end','Delivery begin','Category']
                   
    metadata = MetaData()
    materiaallijsten = Table('materiaallijsten', metadata,
         Column('matlijstID', Integer, primary_key=True),
         Column('icalculatie', Integer),
         Column('werknummerID', Integer),
         Column('orderinkoopID', Integer),
         Column('artikelID', None, ForeignKey('artikelen.artikelID')),
         Column('artikelprijs', Float),
         Column('hoeveelheid', Float),
         Column('afroep', Float),
         Column('resterend', Float),
         Column('subtotaal', Float),
         Column('reserverings_datum', String),
         Column('levertijd_end', String),
         Column('levertijd_begin', String),
         Column('categorie', Integer))
    artikelen = Table('artikelen', metadata,
         Column('artikelID', Integer(), primary_key=True),
         Column('artikelomschrijving', String),
         Column('reserveringsaldo', Float))
                                    
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
    
    selmat = select([artikelen, materiaallijsten]).where(and_(materiaallijsten.c.artikelID\
       == artikelen.c.artikelID, materiaallijsten.c.artikelID == artikelen.c.artikelID,\
       materiaallijsten.c.icalculatie == mcalnr))\
       .order_by(materiaallijsten.c.artikelID)
    rpmat = con.execute(selmat)
    
    data_list=[]
    for row in rpmat:
        data_list += [(row)]
        
    def showSelart(idx):
        logger.warning(">>> Entering showSelart(idx=%s)", idx, extra={"event.action": "showSelart", "logrite.idx": idx})
        martnr = idx.data()
        logger.debug("showSelart(idx=%s): martnr → %s", idx, martnr, extra={"event.action": "showSelart", "logrite.idx": idx})
        if idx.column() == 0:
            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            logger.debug("showSelart(idx=%s): engine → %s", idx, engine, extra={"event.action": "showSelart", "logrite.idx": idx})
            con = engine.connect()
                
            logger.debug("showSelart(idx=%s): con → %s", idx, con, extra={"event.action": "showSelart", "logrite.idx": idx})
            selmat = select([artikelen, materiaallijsten]).where(and_(\
                 materiaallijsten.c.artikelID == artikelen.c.artikelID,\
                 materiaallijsten.c.artikelID == int(martnr),\
                 materiaallijsten.c.icalculatie == mcalnr))\
                 .order_by(materiaallijsten.c.artikelID)
            logger.debug("showSelart(idx=%s): selmat → %s", idx, selmat, extra={"event.action": "showSelart", "logrite.idx": idx})
            rpmat = con.execute(selmat).first()

            logger.debug("showSelart(idx=%s): rpmat → %s", idx, rpmat, extra={"event.action": "showSelart", "logrite.idx": idx})
            header = ['Article number', 'Description', 'Reservation balance', 'ListID', 'Calculation', \
                      'Work number', 'Order purchase number', 'Article number', 'Article price', \
                      'Amount', 'Call-off', 'Remaining', 'Subtotal', 'Reservation date', \
                      'Delivery end', 'Delivery begin', 'Category']
            
            logger.debug("showSelart(idx=%s): header → %s", idx, header, extra={"event.action": "showSelart", "logrite.idx": idx})
            class MainWindow(QDialog):
                logger.debug("<<< Exiting showSelart(idx=%s)", idx, extra={"event.action": "showSelart", "logrite.idx": idx})
                def __init__(self):
                    logger.warning(">>> Entering __init__()", extra={"event.action": "__init__"})
                    QDialog.__init__(self)
                    
                    grid = QGridLayout()
                    grid.setSpacing(20)
                    
                    self.setWindowTitle("Request Articles Cluster calculation")
                    self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
                    
                    self.setFont(QFont('Arial', 10))   
                                                      
                    self.lbl = QLabel()
                    self.pixmap = QPixmap('./images/logos/verbinding.jpg')
                    self.lbl.setPixmap(self.pixmap)
                    grid.addWidget(self.lbl , 0, 0)
                    
                    grid.addWidget(QLabel('Request articles calculation'),0, 1, 1, 2)
            
                    self.logo = QLabel()
                    self.pixmap = QPixmap('./images/logos/logo.jpg')
                    self.logo.setPixmap(self.pixmap)
                    grid.addWidget(self.logo , 0, 3, 1, 1, Qt.AlignRight)                
                    index = 1
                    for item in header:
                        self.lbl = QLabel(header[index-1])
                        self.Gegevens = QLabel()
                        if index == 1:
                            if type(rpmat[index-1]) == float:
                                q1Edit = QLineEdit('{:12.2f}'.format(rpmat[index-1]))
                                q1Edit.setAlignment(Qt.AlignRight)
                            elif type(rpmat[index-1]) == int:
                                q1Edit = QLineEdit(str(rpmat[index-1])) 
                                q1Edit.setAlignment(Qt.AlignRight)
                            else:
                                q1Edit = QLineEdit(str(rpmat[index-1]))
                            q1Edit .setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                            q1Edit.setFixedWidth(100)
                            q1Edit.setDisabled(True)
                            grid.addWidget(self.lbl, 1, 0)
                            grid.addWidget(q1Edit, index, 1, 1, 2)
                        elif index == 2:
                            q1Edit = QLineEdit(str(rpmat[index-1]))
                            q1Edit.setFixedWidth(400)
                            q1Edit.setDisabled(True)
                            q1Edit .setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                            grid.addWidget(self.lbl, 2, 0)
                            grid.addWidget(q1Edit, index, 1, 1, 3)
                        elif index%2 == 0:
                            if type(rpmat[index-1]) == float:
                                q1Edit = QLineEdit('{:12.2f}'.format(rpmat[index-1]))
                                q1Edit.setAlignment(Qt.AlignRight)
                            elif type(rpmat[index-1]) == int:
                                q1Edit = QLineEdit(str(rpmat[index-1]))
                                q1Edit.setAlignment(Qt.AlignRight)
                            else:
                                q1Edit = QLineEdit(str(rpmat[index-1]))
                            q1Edit.setFixedWidth(100)
                            q1Edit.setDisabled(True)
                            q1Edit .setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                            grid.addWidget(self.lbl, index, 0)
                            grid.addWidget(q1Edit, index, 1)
                        else:
                            if type(rpmat[index-1]) == float:
                                q1Edit = QLineEdit('{:12.2f}'.format(rpmat[index-1]))
                                q1Edit.setAlignment(Qt.AlignRight)
                            elif type(rpmat[index-1]) == int:
                                q1Edit = QLineEdit(str(rpmat[index-1]))
                                q1Edit.setAlignment(Qt.AlignRight)
                            else:
                                q1Edit = QLineEdit(str(rpmat[index-1]))
                            q1Edit.setFixedWidth(100)
                            q1Edit .setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                            q1Edit.setDisabled(True)
                            grid.addWidget(self.lbl, index+1, 2)
                            grid.addWidget(q1Edit, index+1, 3)
                        index += 1
                        
                    terugBtn = QPushButton('Close')
                    terugBtn.clicked.connect(self.accept)
            
                    grid.addWidget(terugBtn, index+1, 3, 1, 1, Qt.AlignRight)
                    terugBtn.setFont(QFont("Arial",10))
                    terugBtn.setFixedWidth(100)  
                    
                    grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), index+2, 0, 1, 4, Qt.AlignCenter)                           
                    
                    self.setLayout(grid)
                    self.setGeometry(400, 200, 150, 150)
                    logger.debug("<<< Exiting __init__()", extra={"event.action": "__init__"})
                            
            mainWin = MainWindow()
            mainWin.exec_()
      
    win = MyWindow(data_list, header)
    win.exec_()   