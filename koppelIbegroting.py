import datetime
from login import hoofdMenu
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QFont, QPixmap, QIcon, QRegExpValidator
from PyQt5.QtWidgets import QDialog, QLabel, QGridLayout,\
                             QPushButton, QMessageBox, QLineEdit
from sqlalchemy import (Table, Column, Integer, String, Float,\
                        MetaData, create_engine, ForeignKey)
from sqlalchemy.sql import select, update, and_
import logging
logger = logging.getLogger(__name__)
   
def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    
def foutWerknr():
    logger.warning(">>> Entering foutWerknr()", extra={"event.action": "foutWerknr"})
    msg = QMessageBox()
    logger.debug("foutWerknr(): msg → %s", msg, extra={"event.action": "foutWerknr"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Work order not present, \ncreate a work order first,\nbefore linking the budget!')
    msg.setWindowTitle('Linking budget')
    logger.debug("<<< Exiting foutWerknr()", extra={"event.action": "foutWerknr"})
    msg.exec_()
    
def gekoppeld():
    logger.warning(">>> Entering gekoppeld()", extra={"event.action": "gekoppeld"})
    msg = QMessageBox()
    logger.debug("gekoppeld(): msg → %s", msg, extra={"event.action": "gekoppeld"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Critical)
    msg.setText('Work number is already linked!')
    msg.setWindowTitle('Linking budget')
    logger.debug("<<< Exiting gekoppeld()", extra={"event.action": "gekoppeld"})
    msg.exec_()
        
def verwFout(mwerknr):
    logger.warning(">>> Entering verwFout(mwerknr=%s)", mwerknr, extra={"event.action": "verwFout", "logrite.mwerknr": mwerknr})
    msg = QMessageBox()
    logger.debug("verwFout(mwerknr=%s): msg → %s", mwerknr, msg, extra={"event.action": "verwFout", "logrite.mwerknr": mwerknr})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Link has already taken place\nthe budgeted data is earlier\nto work '+str(mwerknr)+' transferred!')
    msg.setWindowTitle('Linking budget')
    logger.debug("<<< Exiting verwFout(mwerknr=%s)", mwerknr, extra={"event.action": "verwFout", "logrite.mwerknr": mwerknr})
    msg.exec_()
    
def foutCalc():
    logger.warning(">>> Entering foutCalc()", extra={"event.action": "foutCalc"})
    msg = QMessageBox()
    logger.debug("foutCalc(): msg → %s", msg, extra={"event.action": "foutCalc"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Calculation not present!')
    msg.setWindowTitle('Linking budget')
    logger.debug("<<< Exiting foutCalc()", extra={"event.action": "foutCalc"})
    msg.exec_()

def noLinking():
    logger.warning(">>> Entering noLinking()", extra={"event.action": "noLinking"})
    msg = QMessageBox()
    logger.debug("noLinking(): msg → %s", msg, extra={"event.action": "noLinking"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Critical)
    msg.setText('No linking possible, first retrieve order!')
    msg.setWindowTitle('Link calculation')
    logger.debug("<<< Exiting noLinking()", extra={"event.action": "noLinking"})
    msg.exec_()
        
def geenOpdracht():
    logger.warning(">>> Entering geenOpdracht()", extra={"event.action": "geenOpdracht"})
    msg = QMessageBox()
    logger.debug("geenOpdracht(): msg → %s", msg, extra={"event.action": "geenOpdracht"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Order not yet present!')
    msg.setWindowTitle('Linking budget')
    logger.debug("<<< Exiting geenOpdracht()", extra={"event.action": "geenOpdracht"})
    msg.exec_()

def gegevensOk():
    logger.warning(">>> Entering gegevensOk()", extra={"event.action": "gegevensOk"})
    msg = QMessageBox()
    logger.debug("gegevensOk(): msg → %s", msg, extra={"event.action": "gegevensOk"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Information)
    msg.setText('Transfer is successful!')
    msg.setWindowTitle('Linking budget')
    logger.debug("<<< Exiting gegevensOk()", extra={"event.action": "gegevensOk"})
    msg.exec_()
   
def zoekBegroting(m_email):
    logger.warning(">>> Entering zoekBegroting(m_email=%s)", m_email, extra={"event.action": "zoekBegroting"})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            self.setWindowTitle("Linking calculation")
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
            logger.debug("__init__(parent=%s): self.Werkorder → %s", parent, self.Werkorder, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): zkwerknrEdit → %s", parent, zkwerknrEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): zkwerknrEdit → %s", self, parent, zkwerknrEdit, extra={"event.action": "__init__"})
            input_validator = QRegExpValidator(reg_ex, zkcalcEdit)
            logger.debug("__init__(self=%s,parent=%s): input_validator → %s", self, parent, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): input_validator → %s", parent, input_validator, extra={"event.action": "__init__"})
            zkcalcEdit.setValidator(input_validator)  
            
            self.Werkorder = QLabel()
            zkwerknrEdit = QLineEdit()
            zkwerknrEdit.setFixedWidth(100)
            zkwerknrEdit.setFont(QFont("Arial",10))
            zkwerknrEdit.textChanged.connect(self.zkwerknrChanged)
            reg_ex = QRegExp('^[7]{1}[0-9]{8}$')
            input_validator = QRegExpValidator(reg_ex, zkwerknrEdit)
            zkwerknrEdit.setValidator(input_validator)  
           
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
            grid.addWidget(lbl , 1, 0)
            
            lbl1 = QLabel('Calculation number')
            logger.debug("__init__(parent=%s): lbl1 → %s", parent, lbl1, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl1 → %s", self, parent, lbl1, extra={"event.action": "__init__"})
            lbl1.setAlignment(Qt.AlignRight)
            grid.addWidget(lbl1, 3, 0)
            grid.addWidget(zkcalcEdit, 3, 1)
            
            lbl2 = QLabel('Work order')
            logger.debug("__init__(parent=%s): lbl2 → %s", parent, lbl2, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl2 → %s", self, parent, lbl2, extra={"event.action": "__init__"})
            lbl2.setAlignment(Qt.AlignRight)
            grid.addWidget(lbl2, 4, 0)
            grid.addWidget(zkwerknrEdit, 4, 1)
            
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 7, 0, 1, 2, Qt.AlignCenter)
             
            logo = QLabel()
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo ,  1, 0, 1, 2, Qt.AlignRight)
   
            applyBtn = QPushButton('Search')
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn, extra={"event.action": "__init__"})
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 6, 1)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Close')
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn, extra={"event.action": "__init__"})
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
    
            grid.addWidget(cancelBtn, 6, 0, 1, 1,Qt.AlignRight)
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
              
        def zkcalcChanged(self, text):
            logger.warning(">>> Entering zkcalcChanged(text=%s)", text, extra={"event.action": "zkcalcChanged", "logrite.text": text})
            self.Calculatie.setText(text)
            logger.debug("<<< Exiting zkcalcChanged(text=%s)", text, extra={"event.action": "zkcalcChanged", "logrite.text": text})
            
        def zkwerknrChanged(self, text):
            logger.warning(">>> Entering zkwerknrChanged(text=%s)", text, extra={"event.action": "zkwerknrChanged", "logrite.text": text})
            self.Werkorder.setText(text)
            logger.debug("<<< Exiting zkwerknrChanged(text=%s)", text, extra={"event.action": "zkwerknrChanged", "logrite.text": text})
             
        def returnCalculatie(self):
            logger.warning(">>> Entering returnCalculatie()", extra={"event.action": "returnCalculatie"})
            logger.debug("<<< Exiting returnCalculatie()", extra={"event.action": "returnCalculatie"})
            return self.Calculatie.text()
        
        def returnWerkorder(self):
            logger.warning(">>> Entering returnWerkorder()", extra={"event.action": "returnWerkorder"})
            logger.debug("<<< Exiting returnWerkorder()", extra={"event.action": "returnWerkorder"})
            return self.Werkorder.text()
        
        @staticmethod
        def getData(parent=None):
            logger.warning(">>> Entering getData(parent=%s)", parent, extra={"event.action": "getData"})
            dialog = Widget(parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog, extra={"event.action": "getData"})
            dialog.exec_()
            logger.debug("<<< Exiting getData(parent=%s)", parent, extra={"event.action": "getData"})
            return [dialog.returnCalculatie(), dialog.returnWerkorder()]       

    window = Widget()
    data = window.getData()
    if not data[0] or not data[1]:
        zoekBegroting(m_email)
    mcalnr = int(data[0])
    mwerknr = int(data[1])
    metadata = MetaData()
    icalculaties = Table('icalculaties', metadata,
        Column('icalculatie', Integer),
        Column('werkomschrijving', String),
        Column('verwerkt', Integer))
    orders_intern = Table('orders_intern', metadata,
        Column('werkorderID', Integer, primary_key=True),
        Column('besteldatum', String),
        Column('icalculatienummer', Integer))
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
    selcl = select([icalculaties]).where(icalculaties.c.icalculatie == mcalnr)
    rpcl = con.execute(selcl).first()
    selwrk = select([orders_intern]).where(orders_intern.c.werkorderID == mwerknr)
    rpwerk = con.execute(selwrk).first()
    if not rpcl:
        foutCalc()
        zoekBegroting(m_email)
    if not rpwerk:
        foutWerknr()
        zoekBegroting(m_email)
    mcalnr = rpcl[0]
    mwerkomschr = rpcl[1]
    mverw = rpcl[2]
    if rpwerk[1]:
        mverw = 1
    else:
        noLinking()
        zoekBegroting(m_email)
    verder = False
    if rpcl and mverw == 1:
        verder = True
    elif rpcl and mverw > 1:
        verwFout(mwerknr)
        zoekBegroting(m_email)    
    if rpwerk and rpwerk[1] == '':
        geenOpdracht()
        zoekBegroting(m_email)
    elif rpwerk[2] > 0:
        gekoppeld()
        zoekBegroting(m_email)
    elif rpwerk and rpwerk[1] and verder:
        koppelCalc(mcalnr, mwerknr,mwerkomschr, m_email)
  
def koppelCalc(mcalnr, mwerknr, mwerkomschr, m_email):
    logger.warning(">>> Entering koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s)", mcalnr, mwerknr, mwerkomschr, m_email, extra={"event.action": "koppelCalc", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr, "logrite.mwerkomschr": mwerkomschr})
    msgBox=QMessageBox()
    logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): msgBox → %s", mcalnr, mwerknr, mwerkomschr, m_email, msgBox, extra={"event.action": "koppelCalc", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr, "logrite.mwerkomschr": mwerkomschr})
    msgBox.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msgBox.setWindowTitle("Linking budget")
    msgBox.setIcon(QMessageBox.Warning)
    msgBox.setText('Description: '+mwerkomschr+'\nThis calculation only linking\nthen data is definitive\nProceed?')
    msgBox.setStandardButtons(QMessageBox.Yes)
    msgBox.addButton(QMessageBox.No)
    msgBox.setDefaultButton(QMessageBox.Yes)
    if(msgBox.exec_() == QMessageBox.Yes):
        metadata = MetaData()
        logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): metadata → %s", mcalnr, mwerknr, mwerkomschr, m_email, metadata, extra={"event.action": "koppelCalc", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr, "logrite.mwerkomschr": mwerkomschr})
        icalculaties = Table('icalculaties', metadata,
            Column('icalcID', Integer(), primary_key=True),
            Column('iclusterID', None, ForeignKey('iclusters.iclusterID')),
            Column('koppelnummer', Integer),
            Column('werkomschrijving', String),
            Column('verwerkt', Integer),
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
            Column('montage', Float))
        orders_intern = Table('orders_intern', metadata,
            Column('werkorderID', Integer(), primary_key=True),
            Column('werkomschrijving', String),
            Column('icalculatienummer', Integer),
            Column('begroot_totaal', Float),
            Column('begr_materialen', Float),
            Column('begr_lonen', Float),
            Column('hoeveelheid', Float),
            Column('szagen', Float),
            Column('bzagen', Float),
            Column('sschaven', Float),
            Column('bschaven', Float),
            Column('ssteken', Float),
            Column('bsteken', Float),
            Column('sboren', Float), 
            Column('bboren', Float),
            Column('sfrezen', Float),
            Column('bfrezen', Float),
            Column('sdraaien_klein', Float),
            Column('bdraaien_klein', Float),
            Column('sdraaien_groot', Float),
            Column('bdraaien_groot', Float),
            Column('stappen', Float),
            Column('btappen', Float),
            Column('snube_draaien', Float),
            Column('bnube_draaien', Float),
            Column('snube_bewerken', Float),
            Column('bnube_bewerken', Float),
            Column('sknippen', Float),
            Column('bknippen', Float),
            Column('skanten', Float),
            Column('bkanten', Float),
            Column('sstansen', Float),
            Column('bstansen', Float),
            Column('slassen_co2', Float),
            Column('blassen_co2', Float),
            Column('slassen_hand', Float),
            Column('blassen_hand', Float),
            Column('sverpakken', Float),
            Column('bverpakken', Float),
            Column('sverzinken', Float),
            Column('bverzinken', Float),
            Column('smoffelen', Float),
            Column('bmoffelen', Float),
            Column('sschilderen', Float),
            Column('bschilderen', Float),
            Column('sspuiten', Float),
            Column('bspuiten', Float),
            Column('sponsen', Float),
            Column('bponsen', Float),
            Column('spersen', Float),
            Column('bpersen', Float),
            Column('sgritstralen', Float),
            Column('bgritstralen', Float),
            Column('smontage', Float),
            Column('bmontage', Float),
            Column('artikelID', Integer),
            Column('gereed', Float))
              
        engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
        logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): engine → %s", mcalnr, mwerknr, mwerkomschr, m_email, engine, extra={"event.action": "koppelCalc", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr, "logrite.mwerkomschr": mwerkomschr})
        con = engine.connect()
        logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): con → %s", mcalnr, mwerknr, mwerkomschr, m_email, con, extra={"event.action": "koppelCalc", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr, "logrite.mwerkomschr": mwerkomschr})
        selcal = select([icalculaties]).where(icalculaties.c.icalculatie == mcalnr)
        logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): selcal → %s", mcalnr, mwerknr, mwerkomschr, m_email, selcal, extra={"event.action": "koppelCalc", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr, "logrite.mwerkomschr": mwerkomschr})
        rpcal = con.execute(selcal)
        logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): rpcal → %s", mcalnr, mwerknr, mwerkomschr, m_email, rpcal, extra={"event.action": "koppelCalc", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr, "logrite.mwerkomschr": mwerkomschr})
        
        for regel in rpcal:
            updwerk = update(orders_intern).where(orders_intern.c.werkorderID == mwerknr)\
              .values(begroot_totaal = orders_intern.c.begroot_totaal+regel[9],\
              begr_materialen = orders_intern.c.begr_materialen+regel[10],\
              begr_lonen = orders_intern.c.begr_lonen+regel[11],\
              szagen = orders_intern.c.szagen+regel[12],\
              bzagen = orders_intern.c.bzagen+regel[13],\
              sschaven = orders_intern.c.sschaven+regel[14],\
              bschaven = orders_intern.c.bschaven+regel[15],\
              ssteken = orders_intern.c.ssteken+regel[16],\
              bsteken = orders_intern.c.bsteken+regel[17],\
              sboren = orders_intern.c.sboren+regel[18],\
              bboren = orders_intern.c.bboren+regel[19],\
              sfrezen = orders_intern.c.sfrezen+regel[20],\
              bfrezen = orders_intern.c.bfrezen+regel[21],\
              sdraaien_klein = orders_intern.c.sdraaien_klein+regel[22],\
              bdraaien_klein = orders_intern.c.bdraaien_klein+regel[23],\
              sdraaien_groot = orders_intern.c.sdraaien_groot+regel[24] ,\
              bdraaien_groot = orders_intern.c.bdraaien_groot+regel[25] ,\
              stappen = orders_intern.c.stappen+regel[26],\
              btappen = orders_intern.c.btappen+regel[27],\
              snube_draaien = orders_intern.c.snube_draaien+regel[28],\
              bnube_draaien = orders_intern.c.bnube_draaien+regel[29],\
              snube_bewerken = orders_intern.c.snube_bewerken+regel[30],\
              bnube_bewerken = orders_intern.c.bnube_bewerken+regel[31],\
              sknippen = orders_intern.c.sknippen+regel[32],\
              bknippen = orders_intern.c.bknippen+regel[33],\
              skanten = orders_intern.c.skanten+regel[34],\
              bkanten = orders_intern.c.bkanten+regel[35],\
              sstansen = orders_intern.c.sstansen+regel[36],\
              bstansen = orders_intern.c.bstansen+regel[37],\
              slassen_co2 = orders_intern.c.slassen_co2+regel[38],\
              blassen_co2 = orders_intern.c.blassen_co2+regel[39],\
              slassen_hand = orders_intern.c.slassen_hand+regel[40],\
              blassen_hand = orders_intern.c.blassen_hand+regel[41],\
              sverpakken =orders_intern.c.sverpakken+regel[42],\
              bverpakken =orders_intern.c.bverpakken+regel[43],\
              sverzinken=orders_intern.c.sverzinken+regel[44],\
              bverzinken=orders_intern.c.bverzinken+regel[45],\
              smoffelen=orders_intern.c.smoffelen+regel[46],\
              bmoffelen=orders_intern.c.bmoffelen+regel[47],\
              sschilderen=orders_intern.c.sschilderen+regel[48],\
              bschilderen=orders_intern.c.bschilderen+regel[49],\
              sspuiten=orders_intern.c.sspuiten+regel[50],\
              bspuiten=orders_intern.c.bspuiten+regel[51],\
              sponsen=orders_intern.c.sponsen+regel[52],\
              bponsen=orders_intern.c.bponsen+regel[53],\
              spersen=orders_intern.c.spersen+regel[54],\
              bpersen=orders_intern.c.bpersen+regel[55],\
              sgritstralen=orders_intern.c.sgritstralen+regel[56],\
              bgritstralen=orders_intern.c.bgritstralen+regel[57],\
              smontage=orders_intern.c.smontage+regel[58],
              bmontage=orders_intern.c.bmontage+regel[59],\
              icalculatienummer = mcalnr, hoeveelheid = regel[7])
            logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): updwerk → %s", mcalnr, mwerknr, mwerkomschr, m_email, updwerk, extra={"event.action": "koppelCalc", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr, "logrite.mwerkomschr": mwerkomschr})
            con.execute(updwerk)

        updcal = update(icalculaties).where(icalculaties.c.icalculatie == mcalnr) \
            .values(koppelnummer=mwerknr, werkomschrijving=mwerkomschr, verwerkt=2)
        logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): updcal → %s", mcalnr, mwerknr, mwerkomschr, m_email, updcal, extra={"event.action": "koppelCalc", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr, "logrite.mwerkomschr": mwerkomschr})
        con.execute(updcal)
    
        materiaallijsten = Table('materiaallijsten', metadata,
            Column('matlijstID', Integer, primary_key=True),
            Column('icalculatie', Integer),
            Column('hoeveelheid', Float),
            Column('artikelID', None, ForeignKey('artikelen.artikelID')),
            Column('werknummerID', Integer),
            Column('orderinkoopID', Integer),
            Column('reserverings_datum', String),
            Column('levertijd_begin', String),
            Column('levertijd_end', String),
            Column('categorie', Integer))
        logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): selmat → %s", mcalnr, mwerknr, mwerkomschr, m_email, selmat, extra={"event.action": "koppelCalc", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr, "logrite.mwerkomschr": mwerkomschr})
        artikelen = Table('artikelen', metadata,
            Column('artikelID', Integer(), primary_key=True),
            Column('artikelomschrijving', String),
            Column('art_eenheid', String),
            Column('reserveringsaldo', Float),
            Column('categorie', Integer),
            Column('bestelsaldo', Float),
            Column('artikelprijs', Float))
   
        engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
        con = engine.connect()
        selmat = select([materiaallijsten, artikelen]).where(and_(materiaallijsten.\
            c.icalculatie == mcalnr, materiaallijsten.c.artikelID == artikelen.c.artikelID))
        rpmat = con.execute(selmat)
        logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): rpmat → %s", mcalnr, mwerknr, mwerkomschr, m_email, rpmat, extra={"event.action": "koppelCalc", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr, "logrite.mwerkomschr": mwerkomschr})
        logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): updres → %s", mcalnr, mwerknr, mwerkomschr, m_email, updres, extra={"event.action": "koppelCalc", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr, "logrite.mwerkomschr": mwerkomschr})
        mboekd = str(datetime.datetime.now())[0:10]
        logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): mboekd → %s", mcalnr, mwerknr, mwerkomschr, m_email, mboekd, extra={"event.action": "koppelCalc", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr, "logrite.mwerkomschr": mwerkomschr})
        for row in rpmat:
           updres = update(materiaallijsten).where(and_(materiaallijsten.c.icalculatie == mcalnr,\
             materiaallijsten.c.artikelID == artikelen.c.artikelID)).values(werknummerID = mwerknr,\
             reserverings_datum = mboekd, categorie = artikelen.c.categorie)
           con.execute(updres)
           updart = update(artikelen).where(and_(materiaallijsten.c.artikelID ==\
                artikelen.c.artikelID, materiaallijsten.c.icalculatie == mcalnr))\
                .values(reserveringsaldo = artikelen.c.reserveringsaldo + materiaallijsten.c.hoeveelheid)
           logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): updprijs → %s", mcalnr, mwerknr, mwerkomschr, m_email, updprijs, extra={"event.action": "koppelCalc", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr, "logrite.mwerkomschr": mwerkomschr})
           con.execute(updart)
        params_finance = Table('params_finance', metadata,
            Column('financeID', Integer, primary_key=True),
            Column('factor', Float),
            Column('amount', String))
    
        engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
        con = engine.connect()
        selpar = select([params_finance]).order_by(params_finance.c.financeID)
        logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): selpar → %s", mcalnr, mwerknr, mwerkomschr, m_email, selpar, extra={"event.action": "koppelCalc", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr, "logrite.mwerkomschr": mwerkomschr})
        rppar = con.execute(selpar).fetchall()
        logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): rppar → %s", mcalnr, mwerknr, mwerkomschr, m_email, rppar, extra={"event.action": "koppelCalc", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr, "logrite.mwerkomschr": mwerkomschr})
        updprijs = update(artikelen).where(orders_intern.c.artikelID ==\
            artikelen.c.artikelID).values(artikelprijs = (orders_intern.c.begroot_totaal/\
            orders_intern.c.hoeveelheid)*(1+rppar[5][1]))
        con.execute(updprijs)
        gegevensOk()
        zoekBegroting(m_email)    
    else:
        logger.debug("<<< Exiting koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s)", mcalnr, mwerknr, mwerkomschr, m_email, extra={"event.action": "koppelCalc", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr, "logrite.mwerkomschr": mwerkomschr})
        hoofdMenu(m_email)