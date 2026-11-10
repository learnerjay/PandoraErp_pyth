from login import hoofdMenu
import datetime
from PyQt5.QtGui import QRegExpValidator, QFont, QPixmap, QIcon
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtWidgets import QLabel, QPushButton,QGridLayout,\
     QMessageBox, QDialog, QLineEdit 
from sqlalchemy import (Table, Column, Integer, Boolean, MetaData, create_engine, select, func)
import logging
logger = logging.getLogger(__name__)

def maak11proef(basisnr):
   logger.warning(">>> Entering maak11proef(basisnr=%s)", basisnr, extra={"event.action": "maak11proef", "logrite.basisnr": basisnr})
   basisnr = str(basisnr)
   basisnr = str((int(basisnr[0:8]))+int(1))
   logger.debug("maak11proef(basisnr=%s): basisnr → %s", basisnr, basisnr, extra={"event.action": "maak11proef", "logrite.basisnr": basisnr})
   total = 0                       
   logger.debug("maak11proef(basisnr=%s): total → %s", basisnr, total, extra={"event.action": "maak11proef", "logrite.basisnr": basisnr})
   for i in range(int(8)):
       total += int(basisnr[i])*(int(9)-i)
   checkdigit = total % 11
   if checkdigit == 10:
            checkdigit = 0
   basisuitnr = basisnr+str(checkdigit)
   logger.debug("maak11proef(basisnr=%s): basisuitnr → %s", basisnr, basisuitnr, extra={"event.action": "maak11proef", "logrite.basisnr": basisnr})
   logger.debug("<<< Exiting maak11proef(basisnr=%s)", basisnr, extra={"event.action": "maak11proef", "logrite.basisnr": basisnr})
   return basisuitnr
   
def _11check(martikelnr):
    logger.warning(">>> Entering _11check(martikelnr=%s)", martikelnr, extra={"event.action": "_11check", "logrite.martikelnr": martikelnr})
    number = str(martikelnr)
    logger.debug("_11check(martikelnr=%s): number → %s", martikelnr, number, extra={"event.action": "_11check", "logrite.martikelnr": martikelnr})
    total = 0       
    fullnumber = number                       
    logger.debug("_11check(martikelnr=%s): total → %s", martikelnr, total, extra={"event.action": "_11check", "logrite.martikelnr": martikelnr})
    for i in range(8):
        total += int(fullnumber[i])*(9-i)
        logger.debug("_11check(martikelnr=%s): fullnumber → %s", martikelnr, fullnumber, extra={"event.action": "_11check", "logrite.martikelnr": martikelnr})
        checkdigit = total % 11
    if checkdigit == 10:
        checkdigit = 0
    if checkdigit == int(fullnumber[8]):
        return True
    else:
        logger.debug("<<< Exiting _11check(martikelnr=%s)", martikelnr, extra={"event.action": "_11check", "logrite.martikelnr": martikelnr})
        return False

def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})

def bepaalWerknr():
    logger.warning(">>> Entering bepaalWerknr()", extra={"event.action": "bepaalWerknr"})
    metadata = MetaData()
    logger.debug("bepaalWerknr(): metadata → %s", metadata, extra={"event.action": "bepaalWerknr"})
    orders_intern = Table('orders_intern', metadata,
        Column('werkorderID', Integer(), primary_key=True))
    
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("bepaalWerknr(): engine → %s", engine, extra={"event.action": "bepaalWerknr"})
    conn = engine.connect()
    logger.debug("bepaalWerknr(): conn → %s", conn, extra={"event.action": "bepaalWerknr"})
    try:
        mwerknr=(conn.execute(select([func.max(orders_intern.c.werkorderID,\
            type_=Integer)])).scalar())
        mwerknr=int(maak11proef(mwerknr))
    except:
        logger.debug("bepaalWerknr(): type_ → %s", type_, extra={"event.action": "bepaalWerknr"})
        mwerknr = 700000008
        logger.debug("bepaalWerknr(): mwerknr → %s", mwerknr, extra={"event.action": "bepaalWerknr"})
            
        logger.error("Exception in bepaalWerknr()", exc_info=True, extra={"event.action": "bepaalWerknr", "event.category": "process"})
    conn.close
    logger.debug("<<< Exiting bepaalWerknr()", extra={"event.action": "bepaalWerknr"})
    return(mwerknr)

def jaarweek():
    logger.warning(">>> Entering jaarweek()", extra={"event.action": "jaarweek"})
    dt = datetime.datetime.now()
    logger.debug("jaarweek(): dt → %s", dt, extra={"event.action": "jaarweek"})
    week = ('0'+str(dt.isocalendar()[1]))[-2:]
    logger.debug("jaarweek(): week → %s", week, extra={"event.action": "jaarweek"})
    jaar = str(dt.isocalendar()[0])
    jrwk = jaar+week
    logger.debug("jaarweek(): jaar → %s", jaar, extra={"event.action": "jaarweek"})
    logger.debug("jaarweek(): jrwk → %s", jrwk, extra={"event.action": "jaarweek"})
    logger.debug("<<< Exiting jaarweek()", extra={"event.action": "jaarweek"})
    return(jrwk)
    
def foutInvoer():
    logger.warning(">>> Entering foutInvoer()", extra={"event.action": "foutInvoer"})
    msg = QMessageBox()
    logger.debug("foutInvoer(): msg → %s", msg, extra={"event.action": "foutInvoer"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Verplichte Invoer!')
    msg.setWindowTitle('Invoer werkorders')
    logger.debug("<<< Exiting foutInvoer()", extra={"event.action": "foutInvoer"})
    msg.exec_()
  
def Invoer():
    logger.warning(">>> Entering Invoer()", extra={"event.action": "Invoer"})
    msg = QMessageBox()
    logger.debug("Invoer(): msg → %s", msg, extra={"event.action": "Invoer"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Information)
    msg.setText('Invoer gelukt!')
    msg.setWindowTitle('Invoeren werkorders')
    logger.debug("<<< Exiting Invoer()", extra={"event.action": "Invoer"})
    msg.exec_()
    
def foutArtikel():
    logger.warning(">>> Entering foutArtikel()", extra={"event.action": "foutArtikel"})
    msg = QMessageBox()
    logger.debug("foutArtikel(): msg → %s", msg, extra={"event.action": "foutArtikel"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Foutief Artikelnummer ingevoerd!')
    msg.setWindowTitle('Invoer Artikelnummer')               
    logger.debug("<<< Exiting foutArtikel()", extra={"event.action": "foutArtikel"})
    msg.exec_() 
    
def geenArtnr():
    logger.warning(">>> Entering geenArtnr()", extra={"event.action": "geenArtnr"})
    msg = QMessageBox()
    logger.debug("geenArtnr(): msg → %s", msg, extra={"event.action": "geenArtnr"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Geen bestaand artikel gevonden\nNieuw artikelnummer wordt aangemaakt!')
    msg.setWindowTitle('Invoer Artikelnummer')               
    logger.debug("<<< Exiting geenArtnr()", extra={"event.action": "geenArtnr"})
    msg.exec_() 

def invWerkorder(m_email):
    logger.warning(">>> Entering invWerkorder(m_email=%s)", m_email, extra={"event.action": "invWerkorder"})
    from sqlalchemy import (Table, Column, String, Integer, Float, MetaData,\
                            create_engine, update, insert)
    logger.error("Exception in invWerkorder(m_email=%s)", m_email, exc_info=True, extra={"event.action": "invWerkorder", "event.category": "process"})
    class Widget(QDialog):
        logger.debug("<<< Exiting invWerkorder(m_email=%s)", m_email, extra={"event.action": "invWerkorder"})
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            self.setWindowTitle("Invoer werkorders")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
                                  
            self.setFont(QFont('Arial', 10))
                                                 
            self.Omschrijving = QLabel()
            logger.debug("__init__(parent=%s): self.Omschrijving → %s", parent, self.Omschrijving, extra={"event.action": "__init__"})
            q1Edit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): q1Edit → %s", self, parent, q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q1Edit → %s", parent, q1Edit, extra={"event.action": "__init__"})
            q1Edit.setFont(QFont("Arial",10))
            q1Edit.textChanged.connect(self.q1Changed) 
            reg_ex = QRegExp("^.{0,49}$")
            logger.debug("__init__(parent=%s): reg_ex → %s", parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): reg_ex → %s", self, parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.StartWerk → %s", parent, self.StartWerk, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q2Edit → %s", parent, q2Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q2Edit → %s", self, parent, q2Edit, extra={"event.action": "__init__"})
            input_validator = QRegExpValidator(reg_ex, q1Edit)
            logger.debug("__init__(self=%s,parent=%s): input_validator → %s", self, parent, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): input_validator → %s", parent, input_validator, extra={"event.action": "__init__"})
            q1Edit.setValidator(input_validator)
                                     
            self.StartWerk = QLabel()
            q2Edit = QLineEdit()
            q2Edit.setFixedWidth(110)
            q2Edit.setFont(QFont("Arial",10))
            q2Edit.textChanged.connect(self.q2Changed) 
            reg_ex = QRegExp('^[2]{1}[0]{1}[0-9]{2}[-]{1}[0-1]{1}[0-9]{1}[-]{1}[0-3]{1}[0-9]{1}$')
            input_validator = QRegExpValidator(reg_ex, q2Edit)
            q2Edit.setValidator(input_validator)
            
            self.Artikelnummer = QLabel()
            logger.debug("__init__(parent=%s): self.Artikelnummer → %s", parent, self.Artikelnummer, extra={"event.action": "__init__"})
            q3Edit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): q3Edit → %s", self, parent, q3Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q3Edit → %s", parent, q3Edit, extra={"event.action": "__init__"})
            q3Edit.setFixedWidth(110)
            q3Edit.setFont(QFont("Arial",10))
            q3Edit.textChanged.connect(self.q3Changed) 
            reg_ex = QRegExp("^[2]{1}[0-9]{8}$")
            input_validator = QRegExpValidator(reg_ex, q3Edit)
            q3Edit.setValidator(input_validator)
            
            self.Hoeveelheid = QLabel()
            logger.debug("__init__(parent=%s): self.Hoeveelheid → %s", parent, self.Hoeveelheid, extra={"event.action": "__init__"})
            q4Edit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): q4Edit → %s", self, parent, q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q4Edit → %s", parent, q4Edit, extra={"event.action": "__init__"})
            q4Edit.setFixedWidth(110)
            q4Edit.setFont(QFont("Arial",10))
            q4Edit.textChanged.connect(self.q4Changed) 
            reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q4Edit)
            q4Edit.setValidator(input_validator)
                      
            grid = QGridLayout()
            logger.debug("__init__(parent=%s): grid → %s", parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid, extra={"event.action": "__init__"})
            grid.setSpacing(20)
            
            lbl1 = QLabel('Werkorder')  
            logger.debug("__init__(parent=%s): lbl1 → %s", parent, lbl1, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl1 → %s", self, parent, lbl1, extra={"event.action": "__init__"})
            lbl1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl1, 1, 0)
            
            lbl2 = QLabel(str(bepaalWerknr()))
            logger.debug("__init__(parent=%s): lbl2 → %s", parent, lbl2, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl2 → %s", self, parent, lbl2, extra={"event.action": "__init__"})
            grid.addWidget(lbl2, 1, 1)
                   
            lbl3 = QLabel('Omschrijving')  
            logger.debug("__init__(parent=%s): lbl3 → %s", parent, lbl3, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl3 → %s", self, parent, lbl3, extra={"event.action": "__init__"})
            lbl3.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl3, 2, 0)
            grid.addWidget(q1Edit, 2, 1, 1, 3)
              
            lbl4 = QLabel('Start werk')  
            logger.debug("__init__(parent=%s): lbl4 → %s", parent, lbl4, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl4 → %s", self, parent, lbl4, extra={"event.action": "__init__"})
            lbl4.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl4, 3, 0)
            grid.addWidget(q2Edit, 3, 1)
        
            lbl5 = QLabel('Artikelnummer\n       Halffabrikaat   ')  
            logger.debug("__init__(parent=%s): lbl5 → %s", parent, lbl5, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl5 → %s", self, parent, lbl5, extra={"event.action": "__init__"})
            lbl5.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl5, 4, 0)
            grid.addWidget(q3Edit, 4, 1) 
            
            lbl6 = QLabel('Hoeveelheid')  
            logger.debug("__init__(parent=%s): lbl6 → %s", parent, lbl6, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl6 → %s", self, parent, lbl6, extra={"event.action": "__init__"})
            lbl6.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl6, 5, 0)
            grid.addWidget(q4Edit, 5, 1) 
           
            lbl = QLabel()
            logger.debug("__init__(parent=%s): lbl → %s", parent, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl, extra={"event.action": "__init__"})
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap, extra={"event.action": "__init__"})
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl, 0, 0, 1, 2)
            
            logo = QLabel()
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 2, 1, 1, Qt.AlignRight)
                                 
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 7, 0, 1, 3, Qt.AlignCenter)          
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
    
            applyBtn = QPushButton('Invoer')
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn, extra={"event.action": "__init__"})
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 6, 2, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Sluiten')
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn, extra={"event.action": "__init__"})
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
    
            grid.addWidget(cancelBtn, 6, 1, 1 , 1, Qt.AlignRight)
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
                                 
        def q1Changed(self,text):
            logger.warning(">>> Entering q1Changed(text=%s)", text, extra={"event.action": "q1Changed", "logrite.text": text})
            self.Omschrijving.setText(text)
            logger.debug("<<< Exiting q1Changed(text=%s)", text, extra={"event.action": "q1Changed", "logrite.text": text})
    
        def q2Changed(self,text):
            logger.warning(">>> Entering q2Changed(text=%s)", text, extra={"event.action": "q2Changed", "logrite.text": text})
            self.StartWerk.setText(text)
            logger.debug("<<< Exiting q2Changed(text=%s)", text, extra={"event.action": "q2Changed", "logrite.text": text})
    
        def q3Changed(self,text):
            logger.warning(">>> Entering q3Changed(text=%s)", text, extra={"event.action": "q3Changed", "logrite.text": text})
            self.Artikelnummer.setText(text)
            logger.debug("<<< Exiting q3Changed(text=%s)", text, extra={"event.action": "q3Changed", "logrite.text": text})
            
        def q4Changed(self,text):
            logger.warning(">>> Entering q4Changed(text=%s)", text, extra={"event.action": "q4Changed", "logrite.text": text})
            self.Hoeveelheid.setText(text)
            logger.debug("<<< Exiting q4Changed(text=%s)", text, extra={"event.action": "q4Changed", "logrite.text": text})
     
        def returnq1(self):
            logger.warning(">>> Entering returnq1()", extra={"event.action": "returnq1"})
            logger.debug("<<< Exiting returnq1()", extra={"event.action": "returnq1"})
            return self.Omschrijving.text()
        
        def returnq2(self):
            logger.warning(">>> Entering returnq2()", extra={"event.action": "returnq2"})
            logger.debug("<<< Exiting returnq2()", extra={"event.action": "returnq2"})
            return self.StartWerk.text()
        
        def returnq3(self):
            logger.warning(">>> Entering returnq3()", extra={"event.action": "returnq3"})
            logger.debug("<<< Exiting returnq3()", extra={"event.action": "returnq3"})
            return self.Artikelnummer.text()
            
        def returnq4(self):
            logger.warning(">>> Entering returnq4()", extra={"event.action": "returnq4"})
            logger.debug("<<< Exiting returnq4()", extra={"event.action": "returnq4"})
            return self.Hoeveelheid.text()
     
        @staticmethod
        def getData(parent=None):
            logger.warning(">>> Entering getData(parent=%s)", parent, extra={"event.action": "getData"})
            dialog = Widget(parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog, extra={"event.action": "getData"})
            dialog.exec_()
            logger.debug("<<< Exiting getData(parent=%s)", parent, extra={"event.action": "getData"})
            return [dialog.returnq1(), dialog.returnq2(), dialog.returnq3(), dialog.returnq4()]  
                          
    window = Widget()
    data = window.getData()
    if data[0]:
        ms0 = str(data[0])
    else:
        foutInvoer()
        invWerkorder(m_email)
    if data[1] and len(data[1]) == 10:
        mf1 = str(data[1])
    else:
        foutInvoer()
        invWerkorder(m_email)
    if data[3]:
        mf3 = float(data[3])
    else: 
        foutInvoer()
        invWerkorder(m_email)
    metadata = MetaData()
    artikelen = Table('artikelen', metadata,
        Column('artikelID', Integer(), primary_key=True),
        Column('artikelomschrijving', String),
        Column('categorie', Integer),
        Column('artikelgroep', String),
        Column('art_eenheid', String),
        Column('bestelsaldo', Float),
        Column('bestelstatus', Boolean))
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
    selart = select([artikelen]).where(artikelen.c.artikelID==int(data[2]))
    if con.execute(selart):
        mf2 = int(data[2])
        updart = update(artikelen).where(artikelen.c.artikelID == int(mf2)).\
                values(bestelsaldo = artikelen.c.bestelsaldo+mf3, bestelstatus = True)
        con.execute(updart)
    else:
        foutInvoer()
        invWerkorder(m_email) 
        
    mboekd = str(datetime.datetime.now())[0:10] 
        
    from sqlalchemy import (Table, Column, Integer, String, Float, MetaData, create_engine, ForeignKey)
    from sqlalchemy.exc import IntegrityError
    
    metadata = MetaData()
    orders_intern = Table('orders_intern', metadata,
        Column('werkorderID', Integer(), primary_key=True),
        Column('werkomschrijving', String(50)),
        Column('voortgangstatus', String(1)),
        Column('besteldatum', String),
        Column('statusweek',  String(6)),
        Column('startdatum', String),
        Column('artikelID', None, ForeignKey('artikelen.artikelID')),
        Column('hoeveelheid', Float),
        Column('gereed', Float))

    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    metadata.create_all(engine)
    conn = engine.connect()
    try:
        inswrk = insert(orders_intern).values(
        werkorderID=bepaalWerknr(),  
        werkomschrijving=ms0,
        besteldatum = mboekd,
        voortgangstatus='A',
        statusweek=jaarweek(),
        startdatum=mf1,
        artikelID = mf2,
        hoeveelheid = mf3)
        result = conn.execute(inswrk)
    except IntegrityError:
        foutArtikel()
        invWerkorder(m_email)
    result.close
    conn.close
    Invoer()
    invWerkorder(m_email)