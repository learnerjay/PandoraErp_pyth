from login import hoofdMenu
import  datetime
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QFont, QPixmap, QRegExpValidator, QIcon
from PyQt5.QtWidgets import QLabel, QPushButton, QComboBox, QMessageBox,\
                             QLineEdit, QGridLayout, QDialog
from sqlalchemy import (Table, Column, Integer, String, Float, Boolean,\
                     MetaData, create_engine, CheckConstraint, ForeignKey)
from sqlalchemy.sql import select, update, insert, func
from sqlalchemy.exc import IntegrityError
import logging
logger = logging.getLogger(__name__)
 
def _11check(mcontr):
    logger.warning(">>> Entering _11check(mcontr=%s)", mcontr, extra={"event.action": "_11check", "logrite.mcontr": mcontr})
    number = str(mcontr)
    logger.debug("_11check(mcontr=%s): number → %s", mcontr, number, extra={"event.action": "_11check", "logrite.mcontr": mcontr})
    total = 0       
    fullnumber = number                       
    logger.debug("_11check(mcontr=%s): total → %s", mcontr, total, extra={"event.action": "_11check", "logrite.mcontr": mcontr})
    for i in range(8):
        total += int(fullnumber[i])*(9-i)
        logger.debug("_11check(mcontr=%s): fullnumber → %s", mcontr, fullnumber, extra={"event.action": "_11check", "logrite.mcontr": mcontr})
        checkdigit = total % 11
    if checkdigit == 10:
        checkdigit = 0
    if checkdigit == int(fullnumber[8]):
        return True
    else:
        logger.debug("<<< Exiting _11check(mcontr=%s)", mcontr, extra={"event.action": "_11check", "logrite.mcontr": mcontr})
        return False
    
def foutInvoer():
    logger.warning(">>> Entering foutInvoer()", extra={"event.action": "foutInvoer"})
    msg = QMessageBox()
    logger.debug("foutInvoer(): msg → %s", msg, extra={"event.action": "foutInvoer"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Foutief artikelnummer opgegeven.!')
    msg.setWindowTitle('Dervingsartikelen muteren')               
    logger.debug("<<< Exiting foutInvoer()", extra={"event.action": "foutInvoer"})
    msg.exec_() 
    
def ongInvoer():
    logger.warning(">>> Entering ongInvoer()", extra={"event.action": "ongInvoer"})
    msg = QMessageBox()
    logger.debug("ongInvoer(): msg → %s", msg, extra={"event.action": "ongInvoer"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Foutieve invoer\nzoekterm opnieuw invoeren s.v.p.!')
    msg.setWindowTitle('Materialen uitgeven/ printen')               
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
    msg.setWindowTitle('Materialen uitgeven/ printen')               
    logger.debug("<<< Exiting geenRecord()", extra={"event.action": "geenRecord"})
    msg.exec_() 
    
def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    
def invoerOK():
    logger.warning(">>> Entering invoerOK()", extra={"event.action": "invoerOK"})
    msg = QMessageBox()
    logger.debug("invoerOK(): msg → %s", msg, extra={"event.action": "invoerOK"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Information)
    msg.setText('Invoer gelukt!')
    msg.setWindowTitle('Dervingmutaties')
    logger.debug("<<< Exiting invoerOK()", extra={"event.action": "invoerOK"})
    msg.exec_()
				            
def negVoorraad():
        logger.warning(">>> Entering negVoorraad()", extra={"event.action": "negVoorraad"})
        msg = QMessageBox()
        logger.debug("negVoorraad(): msg → %s", msg, extra={"event.action": "negVoorraad"})
        msg.setStyleSheet("color: black;  background-color: gainsboro")
        msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
        msg.setIcon(QMessageBox.Critical)
        msg.setText('Te weinig voorraad\nvoor de transactie!')
        msg.setWindowTitle('Dervingmutatities')
        logger.debug("<<< Exiting negVoorraad()", extra={"event.action": "negVoorraad"})
        msg.exec_()
        
def foutHoev():
        logger.warning(">>> Entering foutHoev()", extra={"event.action": "foutHoev"})
        msg = QMessageBox()
        logger.debug("foutHoev(): msg → %s", msg, extra={"event.action": "foutHoev"})
        msg.setStyleSheet("color: black;  background-color: gainsboro")
        msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
        msg.setIcon(QMessageBox.Warning)
        msg.setText('Geen juiste hoeveelheid!')
        msg.setWindowTitle('Dervingmutaties')
        logger.debug("<<< Exiting foutHoev()", extra={"event.action": "foutHoev"})
        msg.exec_()
                
def dervingMut(m_email):
    logger.warning(">>> Entering dervingMut(m_email=%s)", m_email, extra={"event.action": "dervingMut"})
    class Widget(QDialog):
        logger.error("Exception in dervingMut(m_email=%s)", m_email, exc_info=True, extra={"event.action": "dervingMut", "event.category": "process"})
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            self.setWindowTitle("Materiaaluitgifte muteren")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
                       
            self.Dervingnummer = QLabel()
            logger.debug("__init__(parent=%s): self.Dervingnummer → %s", parent, self.Dervingnummer, extra={"event.action": "__init__"})
            derving = QComboBox()
            logger.debug("__init__(self=%s,parent=%s): derving → %s", self, parent, derving, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): derving → %s", parent, derving, extra={"event.action": "__init__"})
            derving.setFixedWidth(200)
            derving.setFont(QFont("Times", 10))
            derving.setStyleSheet("color: black;  background-color: #F8F7EE")
            derving.addItem('    Kies soort Derving')
            derving.addItem('1. Incourant')
            derving.addItem('2. Magazijn verschillen.')
            derving.addItem('3. Beschadiging')
            derving.addItem('4. Houdbaarheid')
            derving.activated[str].connect(self.dervingChanged)
                              
            self.Artikelnummer = QLabel()
            logger.debug("__init__(parent=%s): self.Artikelnummer → %s", parent, self.Artikelnummer, extra={"event.action": "__init__"})
            artEdit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): artEdit → %s", self, parent, artEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): artEdit → %s", parent, artEdit, extra={"event.action": "__init__"})
            artEdit.setFixedWidth(150)
            artEdit.setFont(QFont("Arial",10))
            artEdit.textChanged.connect(self.artChanged) 
            reg_ex = QRegExp("^[2]{1}[0-9]{8}$")
            logger.debug("__init__(parent=%s): reg_ex → %s", parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): reg_ex → %s", self, parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Hoeveelheid → %s", parent, self.Hoeveelheid, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): hoevEdit → %s", parent, hoevEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): hoevEdit → %s", self, parent, hoevEdit, extra={"event.action": "__init__"})
            input_validator = QRegExpValidator(reg_ex, artEdit)
            logger.debug("__init__(self=%s,parent=%s): input_validator → %s", self, parent, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): input_validator → %s", parent, input_validator, extra={"event.action": "__init__"})
            artEdit.setValidator(input_validator)
            
            self.Hoeveelheid = QLabel()
            hoevEdit = QLineEdit()
            hoevEdit.setFixedWidth(150)
            hoevEdit.setFont(QFont("Arial",10))
            hoevEdit.textChanged.connect(self.hoevChanged) 
            reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, hoevEdit)
            hoevEdit.setValidator(input_validator)
           
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
            grid.addWidget(lbl ,0, 0)
            
            logo = QLabel()
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 2, 1, 1, Qt.AlignRight) 
                         
            lbl1 = QLabel('Dervingnummer')  
            logger.debug("__init__(parent=%s): lbl1 → %s", parent, lbl1, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl1 → %s", self, parent, lbl1, extra={"event.action": "__init__"})
            lbl1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl1, 1, 0)
            grid.addWidget(derving, 1, 1)
                                          
            lbl2 = QLabel('Artikelnummer')  
            logger.debug("__init__(parent=%s): lbl2 → %s", parent, lbl2, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl2 → %s", self, parent, lbl2, extra={"event.action": "__init__"})
            lbl2.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl2, 2, 0)
            grid.addWidget(artEdit, 2, 1)
             
            lbl3 = QLabel('Hoeveelheid')  
            logger.debug("__init__(parent=%s): lbl3 → %s", parent, lbl3, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl3 → %s", self, parent, lbl3, extra={"event.action": "__init__"})
            lbl3.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl3, 3, 0)
            grid.addWidget(hoevEdit, 3 , 1)
                                             
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
    
            applyBtn = QPushButton('Muteren')
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn, extra={"event.action": "__init__"})
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 5, 1, 1 , 2, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
           
            cancelBtn = QPushButton('Sluiten')
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn, extra={"event.action": "__init__"})
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email)) 
            
            grid.addWidget(cancelBtn,5, 1, Qt.AlignCenter)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 6, 0, 1, 3, Qt.AlignCenter)     
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
                                                                      
        def dervingChanged(self, text):
            logger.warning(">>> Entering dervingChanged(text=%s)", text, extra={"event.action": "dervingChanged", "logrite.text": text})
            self.Dervingnummer.setText(text)
            logger.debug("<<< Exiting dervingChanged(text=%s)", text, extra={"event.action": "dervingChanged", "logrite.text": text})
            
        def artChanged(self,text):
            logger.warning(">>> Entering artChanged(text=%s)", text, extra={"event.action": "artChanged", "logrite.text": text})
            self.Artikelnummer.setText(text)
            logger.debug("<<< Exiting artChanged(text=%s)", text, extra={"event.action": "artChanged", "logrite.text": text})
            
        def hoevChanged(self,text):
            logger.warning(">>> Entering hoevChanged(text=%s)", text, extra={"event.action": "hoevChanged", "logrite.text": text})
            self.Hoeveelheid.setText(text)
            logger.debug("<<< Exiting hoevChanged(text=%s)", text, extra={"event.action": "hoevChanged", "logrite.text": text})
                                                   
        def returnderving(self):
            logger.warning(">>> Entering returnderving()", extra={"event.action": "returnderving"})
            logger.debug("<<< Exiting returnderving()", extra={"event.action": "returnderving"})
            return self.Dervingnummer.text()
        
        def returnart(self):
            logger.warning(">>> Entering returnart()", extra={"event.action": "returnart"})
            logger.debug("<<< Exiting returnart()", extra={"event.action": "returnart"})
            return self.Artikelnummer.text()
        
        def returnhoev(self):
            logger.warning(">>> Entering returnhoev()", extra={"event.action": "returnhoev"})
            logger.debug("<<< Exiting returnhoev()", extra={"event.action": "returnhoev"})
            return self.Hoeveelheid.text()
                              
        @staticmethod
        def getData(parent=None):
            logger.warning(">>> Entering getData(parent=%s)", parent, extra={"event.action": "getData"})
            dialog = Widget(parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog, extra={"event.action": "getData"})
            dialog.exec_()
            logger.debug("<<< Exiting getData(parent=%s)", parent, extra={"event.action": "getData"})
            return [dialog.returnderving(), dialog.returnart(), dialog.returnhoev()]
    
    window = Widget()
    data = window.getData()
    mhoev = 0
    if not data[0] or data[0][0] == ' ':
        ongInvoer()
        dervingMut(m_email)
    elif data[0][0] == '1':
        mderving = '999999990'
        momschr = 'Incourant'
    elif data[0][0] == '2':
        mderving = '999999989'
        momschr = 'Magazijn verschillen'
    elif data[0][0] ==  '3':
        mderving = '999999977'
        momschr = 'Beschadiging'
    elif data[0][0] == '4':
        mderving = '999999965'
        momschr = 'Houdbaarheid'
                   
    if data[1] and len(data[1]) == 9 and _11check(data[1]):
        martikelnr = int(data[1])
    else:
        foutInvoer()
        dervingMut(m_email)
    if data[2]:
        mhoev = float(data[2])
    else:
        foutHoev()
        dervingMut(m_email)
   
    metadata = MetaData()
    artikelen = Table('artikelen', metadata,
        Column('artikelID', Integer(), primary_key=True),
        Column('artikelomschrijving', String),
        Column('artikelprijs', Float),
        Column('art_voorraad', Float, CheckConstraint('art_voorraad >= 0')),
        Column('art_min_voorraad', Float),
        Column('bestelstatus', Boolean))
    derving = Table('derving', metadata,
        Column('dervingID', Integer, primary_key=True),
        Column('artikelID', None, ForeignKey('artikelen.artikelID')),
        Column('categorienummer', None, ForeignKey('werken.werknoID')),
        Column('omschrijving', String),
        Column('hoeveelheid', Float),
        Column('boekdatum', String),
        Column('waarde', Float))
          
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
    sel = select([artikelen]).where(artikelen.c.artikelID == martikelnr)
    transaction = con.begin()
    result = con.execute(sel).first()
    if not result:
        geenRecord()
        dervingMut(m_email)
    martprijs = result[2]
    martvrd = result[3]
    martminvrd = result[4]
    mboekd = str(datetime.datetime.now())[0:10]
    if martvrd - mhoev <= martminvrd:
        martbestst = False
    else:
        martbestst = True
    if mhoev <= 0:
        foutHoev()
        dervingMut(m_email)
    try:
        stmt = update(artikelen).where(artikelen.c.artikelID == martikelnr).values(\
         art_voorraad = artikelen.c.art_voorraad - mhoev, bestelstatus = martbestst)
        con.execute(stmt)
        con = engine.connect()
        try:
            dervingnr=(con.execute(select([func.max(derving.c.dervingID,\
                type_=Integer)])).scalar())
            dervingnr += 1
        except:
            dervingnr = 1
            
        ins = insert(derving).values(dervingID = dervingnr, artikelID =\
            martikelnr, categorienummer = mderving, hoeveelheid = -mhoev, boekdatum = mboekd,\
            waarde = mhoev*martprijs, omschrijving = momschr)
        con.execute(ins)
        transaction.commit()
        invoerOK()
        dervingMut(m_email)
    except IntegrityError:
        transaction.rollback()
        negVoorraad()
        dervingMut(m_email)
    con.close 
 