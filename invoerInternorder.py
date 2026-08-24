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
   logger.debug(">>> Entering maak11proef(basisnr=%s)", basisnr)
   basisnr = str(basisnr)
   basisnr = str((int(basisnr[0:8]))+int(1))
   logger.debug("maak11proef(basisnr=%s): basisnr → %s", basisnr, basisnr)
   total = 0                       
   logger.debug("maak11proef(basisnr=%s): total → %s", basisnr, total)
   for i in range(int(8)):
       total += int(basisnr[i])*(int(9)-i)
   checkdigit = total % 11
   if checkdigit == 10:
            checkdigit = 0
   basisuitnr = basisnr+str(checkdigit)
   logger.debug("maak11proef(basisnr=%s): basisuitnr → %s", basisnr, basisuitnr)
   logger.debug("<<< Exiting maak11proef(basisnr=%s)", basisnr)
   return basisuitnr
   
def _11check(martikelnr):
    logger.debug(">>> Entering _11check(martikelnr=%s)", martikelnr)
    number = str(martikelnr)
    logger.debug("_11check(martikelnr=%s): number → %s", martikelnr, number)
    total = 0       
    fullnumber = number                       
    logger.debug("_11check(martikelnr=%s): total → %s", martikelnr, total)
    for i in range(8):
        total += int(fullnumber[i])*(9-i)
        logger.debug("_11check(martikelnr=%s): fullnumber → %s", martikelnr, fullnumber)
        checkdigit = total % 11
    if checkdigit == 10:
        checkdigit = 0
    if checkdigit == int(fullnumber[8]):
        return True
    else:
        logger.debug("<<< Exiting _11check(martikelnr=%s)", martikelnr)
        return False

def windowSluit(self, m_email):
    logger.debug(">>> Entering windowSluit(m_email=%s)", m_email)
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email)

def bepaalWerknr():
    logger.debug(">>> Entering bepaalWerknr()")
    metadata = MetaData()
    logger.debug("bepaalWerknr(): metadata → %s", metadata)
    orders_intern = Table('orders_intern', metadata,
        Column('werkorderID', Integer(), primary_key=True))
    
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    conn = engine.connect()
    try:
        logger.debug("bepaalWerknr(): conn → %s", conn)
        mwerknr=(conn.execute(select([func.max(orders_intern.c.werkorderID,\
            type_=Integer)])).scalar())
        mwerknr=int(maak11proef(mwerknr))
        logger.debug("bepaalWerknr(): mwerknr → %s", mwerknr)
        logger.debug("bepaalWerknr(): type_ → %s", type_)
    except:
        mwerknr = 700000008
            
    conn.close
    logger.error("Exception in bepaalWerknr()", exc_info=True)
    logger.debug("<<< Exiting bepaalWerknr()")
    return(mwerknr)

def jaarweek():
    logger.debug(">>> Entering jaarweek()")
    dt = datetime.datetime.now()
    logger.debug("jaarweek(): dt → %s", dt)
    week = ('0'+str(dt.isocalendar()[1]))[-2:]
    logger.debug("jaarweek(): week → %s", week)
    jaar = str(dt.isocalendar()[0])
    jrwk = jaar+week
    logger.debug("jaarweek(): jaar → %s", jaar)
    logger.debug("jaarweek(): jrwk → %s", jrwk)
    logger.debug("<<< Exiting jaarweek()")
    return(jrwk)
    
def foutInvoer():
    logger.debug(">>> Entering foutInvoer()")
    msg = QMessageBox()
    logger.debug("foutInvoer(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Required input!')
    msg.setWindowTitle('Insert work orders')
    logger.debug("<<< Exiting foutInvoer()")
    msg.exec_()
  
def Invoer():
    logger.debug(">>> Entering Invoer()")
    msg = QMessageBox()
    logger.debug("Invoer(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Information)
    msg.setText('Insert successful!')
    msg.setWindowTitle('Insert work orders')
    logger.debug("<<< Exiting Invoer()")
    msg.exec_()
    
def foutArtikel():
    logger.debug(">>> Entering foutArtikel()")
    msg = QMessageBox()
    logger.debug("foutArtikel(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Incorrect Article number entered!')
    msg.setWindowTitle('Insert work orders')               
    logger.debug("<<< Exiting foutArtikel()")
    msg.exec_() 
    
def geenArtnr():
    logger.debug(">>> Entering geenArtnr()")
    msg = QMessageBox()
    logger.debug("geenArtnr(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Warning)
    msg.setText('No existing article found\nNew article number is created!')
    msg.setWindowTitle('Insert article number')
    logger.debug("<<< Exiting geenArtnr()")
    msg.exec_() 

def invWerkorder(m_email):
    logger.debug(">>> Entering invWerkorder(m_email=%s)", m_email)
    from sqlalchemy import (Table, Column, String, Integer, Float, MetaData,\
                            create_engine, update, insert)
    logger.error("Exception in invWerkorder(m_email=%s)", m_email, exc_info=True)
    class Widget(QDialog):
        logger.debug("<<< Exiting invWerkorder(m_email=%s)", m_email)
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.debug(">>> Entering __init__(parent=%s)", parent)
            self.setWindowTitle("Insert work orders")
            logger.debug("__init__(parent=%s): input_validator → %s", parent, input_validator)
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
                                  
            self.setFont(QFont('Arial', 10))
                                                 
            self.Omschrijving = QLabel()
            logger.debug("__init__(parent=%s): self.Omschrijving → %s", parent, self.Omschrijving)
            q1Edit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): q1Edit → %s", self, parent, q1Edit)
            logger.debug("__init__(parent=%s): q1Edit → %s", parent, q1Edit)
            q1Edit.setFont(QFont("Arial",10))
            q1Edit.textChanged.connect(self.q1Changed) 
            reg_ex = QRegExp("^.{0,49}$")
            logger.debug("__init__(self=%s,parent=%s): reg_ex → %s", self, parent, reg_ex)
            logger.debug("__init__(parent=%s): reg_ex → %s", parent, reg_ex)
            input_validator = QRegExpValidator(reg_ex, q1Edit)
            logger.debug("__init__(self=%s,parent=%s): input_validator → %s", self, parent, input_validator)
            q1Edit.setValidator(input_validator)
                                     
            self.StartWerk = QLabel()
            logger.debug("__init__(parent=%s): self.StartWerk → %s", parent, self.StartWerk)
            q2Edit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): q2Edit → %s", self, parent, q2Edit)
            logger.debug("__init__(parent=%s): q2Edit → %s", parent, q2Edit)
            q2Edit.setFixedWidth(110)
            q2Edit.setFont(QFont("Arial",10))
            q2Edit.textChanged.connect(self.q2Changed) 
            reg_ex = QRegExp('^[2]{1}[0]{1}[0-9]{2}[-]{1}[0-1]{1}[0-9]{1}[-]{1}[0-3]{1}[0-9]{1}$')
            input_validator = QRegExpValidator(reg_ex, q2Edit)
            q2Edit.setValidator(input_validator)
            
            self.Artikelnummer = QLabel()
            logger.debug("__init__(parent=%s): self.Artikelnummer → %s", parent, self.Artikelnummer)
            q3Edit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): q3Edit → %s", self, parent, q3Edit)
            logger.debug("__init__(parent=%s): q3Edit → %s", parent, q3Edit)
            q3Edit.setFixedWidth(110)
            q3Edit.setFont(QFont("Arial",10))
            q3Edit.textChanged.connect(self.q3Changed) 
            reg_ex = QRegExp("^[2]{1}[0-9]{8}$")
            input_validator = QRegExpValidator(reg_ex, q3Edit)
            q3Edit.setValidator(input_validator)
            
            self.Hoeveelheid = QLabel()
            logger.debug("__init__(parent=%s): self.Hoeveelheid → %s", parent, self.Hoeveelheid)
            q4Edit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): q4Edit → %s", self, parent, q4Edit)
            logger.debug("__init__(parent=%s): q4Edit → %s", parent, q4Edit)
            q4Edit.setFixedWidth(110)
            q4Edit.setFont(QFont("Arial",10))
            q4Edit.textChanged.connect(self.q4Changed) 
            reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q4Edit)
            q4Edit.setValidator(input_validator)
                      
            grid = QGridLayout()
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid)
            logger.debug("__init__(parent=%s): grid → %s", parent, grid)
            grid.setSpacing(20)
            
            lbl1 = QLabel('Work order')
            logger.debug("__init__(self=%s,parent=%s): lbl1 → %s", self, parent, lbl1)
            logger.debug("__init__(parent=%s): lbl1 → %s", parent, lbl1)
            lbl1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl1, 1, 0)
            
            lbl2 = QLabel(str(bepaalWerknr()))
            logger.debug("__init__(self=%s,parent=%s): lbl2 → %s", self, parent, lbl2)
            logger.debug("__init__(parent=%s): lbl2 → %s", parent, lbl2)
            grid.addWidget(lbl2, 1, 1)
                   
            lbl3 = QLabel('Description')  
            logger.debug("__init__(self=%s,parent=%s): lbl3 → %s", self, parent, lbl3)
            logger.debug("__init__(parent=%s): lbl3 → %s", parent, lbl3)
            lbl3.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl3, 2, 0)
            grid.addWidget(q1Edit, 2, 1, 1, 3)
              
            lbl4 = QLabel('Start work')  
            logger.debug("__init__(self=%s,parent=%s): lbl4 → %s", self, parent, lbl4)
            logger.debug("__init__(parent=%s): lbl4 → %s", parent, lbl4)
            lbl4.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl4, 3, 0)
            grid.addWidget(q2Edit, 3, 1)
        
            lbl5 = QLabel('Article number\n       Semi-finished product')
            logger.debug("__init__(self=%s,parent=%s): lbl5 → %s", self, parent, lbl5)
            logger.debug("__init__(parent=%s): lbl5 → %s", parent, lbl5)
            lbl5.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl5, 4, 0)
            grid.addWidget(q3Edit, 4, 1) 
            
            lbl6 = QLabel('Amount')  
            logger.debug("__init__(self=%s,parent=%s): lbl6 → %s", self, parent, lbl6)
            logger.debug("__init__(parent=%s): lbl6 → %s", parent, lbl6)
            lbl6.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl6, 5, 0)
            grid.addWidget(q4Edit, 5, 1) 
           
            lbl = QLabel()
            logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl)
            logger.debug("__init__(parent=%s): lbl → %s", parent, lbl)
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap)
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap)
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl, 0, 0, 1, 2)
            
            logo = QLabel()
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo)
            logger.debug("__init__(parent=%s): logo → %s", parent, logo)
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 2, 1, 1, Qt.AlignRight)
                                 
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 7, 0, 1, 3, Qt.AlignCenter)          
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
    
            applyBtn = QPushButton('Insert')
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn)
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn)
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 6, 2, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Close')
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn)
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn)
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
    
            grid.addWidget(cancelBtn, 6, 1, 1 , 1, Qt.AlignRight)
            logger.debug("<<< Exiting __init__(parent=%s)", parent)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
                                 
        def q1Changed(self,text):
            logger.debug(">>> Entering q1Changed(text=%s)", text)
            logger.debug("q1Changed(self=%s,text=%s): Omschrijving → %s", self, text, Omschrijving)
            self.Omschrijving.setText(text)
            logger.debug("<<< Exiting q1Changed(text=%s)", text)
    
        def q2Changed(self,text):
            logger.debug(">>> Entering q2Changed(text=%s)", text)
            logger.debug("q2Changed(self=%s,text=%s): StartWerk → %s", self, text, StartWerk)
            self.StartWerk.setText(text)
            logger.debug("<<< Exiting q2Changed(text=%s)", text)
    
        def q3Changed(self,text):
            logger.debug(">>> Entering q3Changed(text=%s)", text)
            logger.debug("q3Changed(self=%s,text=%s): Artikelnummer → %s", self, text, Artikelnummer)
            self.Artikelnummer.setText(text)
            logger.debug("<<< Exiting q3Changed(text=%s)", text)
            
        def q4Changed(self,text):
            logger.debug(">>> Entering q4Changed(text=%s)", text)
            logger.debug("q4Changed(self=%s,text=%s): Hoeveelheid → %s", self, text, Hoeveelheid)
            self.Hoeveelheid.setText(text)
            logger.debug("<<< Exiting q4Changed(text=%s)", text)
     
        def returnq1(self):
            logger.debug(">>> Entering returnq1()")
            logger.debug("<<< Exiting returnq1()")
            return self.Omschrijving.text()
        
        def returnq2(self):
            logger.debug(">>> Entering returnq2()")
            logger.debug("<<< Exiting returnq2()")
            return self.StartWerk.text()
        
        def returnq3(self):
            logger.debug(">>> Entering returnq3()")
            logger.debug("<<< Exiting returnq3()")
            return self.Artikelnummer.text()
            
        def returnq4(self):
            logger.debug(">>> Entering returnq4()")
            logger.debug("<<< Exiting returnq4()")
            return self.Hoeveelheid.text()
     
        @staticmethod
        def getData(parent=None):
            logger.debug(">>> Entering getData(parent=%s)", parent)
            dialog = Widget(parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog)
            dialog.exec_()
            logger.debug("<<< Exiting getData(parent=%s)", parent)
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