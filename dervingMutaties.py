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
    logger.debug(">>> Entering _11check(mcontr=%s)", mcontr)
    number = str(mcontr)
    logger.debug("_11check(mcontr=%s): number → %s", mcontr, number)
    total = 0       
    fullnumber = number                       
    logger.debug("_11check(mcontr=%s): total → %s", mcontr, total)
    for i in range(8):
        total += int(fullnumber[i])*(9-i)
        logger.debug("_11check(mcontr=%s): fullnumber → %s", mcontr, fullnumber)
        checkdigit = total % 11
    if checkdigit == 10:
        checkdigit = 0
    if checkdigit == int(fullnumber[8]):
        return True
    else:
        logger.debug("<<< Exiting _11check(mcontr=%s)", mcontr)
        return False
    
def foutInvoer():
    logger.debug(">>> Entering foutInvoer()")
    msg = QMessageBox()
    logger.debug("foutInvoer(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Incorrect article number specified.!')
    msg.setWindowTitle('Mutating loss articles')               
    logger.debug("<<< Exiting foutInvoer()")
    msg.exec_() 
    
def ongInvoer():
    logger.debug(">>> Entering ongInvoer()")
    msg = QMessageBox()
    logger.debug("ongInvoer(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Please re-enter incorrect\ninput search term!')
    msg.setWindowTitle('Provide / printing materials')               
    logger.debug("<<< Exiting ongInvoer()")
    msg.exec_() 
    
def geenRecord():
    logger.debug(">>> Entering geenRecord()")
    msg = QMessageBox()
    logger.debug("geenRecord(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('No record found\ncreate another selection please!')
    msg.setWindowTitle('Provide / printing materials')               
    logger.debug("<<< Exiting geenRecord()")
    msg.exec_() 
    
def windowSluit(self, m_email):
    logger.debug(">>> Entering windowSluit(m_email=%s)", m_email)
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email)
    
def invoerOK():
    logger.debug(">>> Entering invoerOK()")
    msg = QMessageBox()
    logger.debug("invoerOK(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Information)
    msg.setText('Insert successful!')
    msg.setWindowTitle('Mutating loss articles')
    logger.debug("<<< Exiting invoerOK()")
    msg.exec_()
				            
def negVoorraad():
        logger.debug(">>> Entering negVoorraad()")
        msg = QMessageBox()
        logger.debug("negVoorraad(): msg → %s", msg)
        msg.setStyleSheet("color: black;  background-color: gainsboro")
        msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
        msg.setIcon(QMessageBox.Critical)
        msg.setText('Too little stock for the transaction!')
        msg.setWindowTitle('Mutating loss articles')
        logger.debug("<<< Exiting negVoorraad()")
        msg.exec_()
        
def foutHoev():
        logger.debug(">>> Entering foutHoev()")
        msg = QMessageBox()
        logger.debug("foutHoev(): msg → %s", msg)
        msg.setStyleSheet("color: black;  background-color: gainsboro")
        msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
        msg.setIcon(QMessageBox.Warning)
        msg.setText('Not the right amount!')
        msg.setWindowTitle('Mutating loss articles')
        logger.debug("<<< Exiting foutHoev()")
        msg.exec_()
                
def dervingMut(m_email):
    logger.debug(">>> Entering dervingMut(m_email=%s)", m_email)
    class Widget(QDialog):
        logger.error("Exception in dervingMut(m_email=%s)", m_email, exc_info=True)
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.debug(">>> Entering __init__(parent=%s)", parent)
            self.setWindowTitle("Mutate material provision")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
                       
            self.Dervingnummer = QLabel()
            logger.debug("__init__(parent=%s): self.Dervingnummer → %s", parent, self.Dervingnummer)
            derving = QComboBox()
            logger.debug("__init__(self=%s,parent=%s): derving → %s", self, parent, derving)
            logger.debug("__init__(parent=%s): derving → %s", parent, derving)
            derving.setFixedWidth(200)
            derving.setFont(QFont("Times", 10))
            derving.setStyleSheet("color: black;  background-color: #F8F7EE")
            derving.addItem(' Choose type off loss')
            derving.addItem('1. Obsolete.')
            derving.addItem('2. Warehouse differences.')
            derving.addItem('3. Damaged')
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap)
            logger.debug("__init__(parent=%s): input_validator → %s", parent, input_validator)
            derving.addItem('4. Shelf life')
            derving.activated[str].connect(self.dervingChanged)
                              
            self.Artikelnummer = QLabel()
            logger.debug("__init__(parent=%s): self.Artikelnummer → %s", parent, self.Artikelnummer)
            artEdit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): artEdit → %s", self, parent, artEdit)
            logger.debug("__init__(parent=%s): artEdit → %s", parent, artEdit)
            artEdit.setFixedWidth(150)
            artEdit.setFont(QFont("Arial",10))
            artEdit.textChanged.connect(self.artChanged) 
            reg_ex = QRegExp("^[2]{1}[0-9]{8}$")
            logger.debug("__init__(self=%s,parent=%s): reg_ex → %s", self, parent, reg_ex)
            logger.debug("__init__(parent=%s): reg_ex → %s", parent, reg_ex)
            input_validator = QRegExpValidator(reg_ex, artEdit)
            logger.debug("__init__(self=%s,parent=%s): input_validator → %s", self, parent, input_validator)
            artEdit.setValidator(input_validator)
            
            self.Hoeveelheid = QLabel()
            logger.debug("__init__(parent=%s): self.Hoeveelheid → %s", parent, self.Hoeveelheid)
            hoevEdit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): hoevEdit → %s", self, parent, hoevEdit)
            logger.debug("__init__(parent=%s): hoevEdit → %s", parent, hoevEdit)
            hoevEdit.setFixedWidth(150)
            hoevEdit.setFont(QFont("Arial",10))
            hoevEdit.textChanged.connect(self.hoevChanged) 
            reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, hoevEdit)
            hoevEdit.setValidator(input_validator)
           
            grid = QGridLayout()
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid)
            logger.debug("__init__(parent=%s): grid → %s", parent, grid)
            grid.setSpacing(20)
                          
            lbl = QLabel()
            logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl)
            logger.debug("__init__(parent=%s): lbl → %s", parent, lbl)
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap)
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl ,0, 0)
            
            logo = QLabel()
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo)
            logger.debug("__init__(parent=%s): logo → %s", parent, logo)
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 2, 1, 1, Qt.AlignRight) 
                         
            lbl1 = QLabel('Loss number')  
            logger.debug("__init__(self=%s,parent=%s): lbl1 → %s", self, parent, lbl1)
            logger.debug("__init__(parent=%s): lbl1 → %s", parent, lbl1)
            lbl1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl1, 1, 0)
            grid.addWidget(derving, 1, 1)
                                          
            lbl2 = QLabel('Article number')  
            logger.debug("__init__(self=%s,parent=%s): lbl2 → %s", self, parent, lbl2)
            logger.debug("__init__(parent=%s): lbl2 → %s", parent, lbl2)
            lbl2.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl2, 2, 0)
            grid.addWidget(artEdit, 2, 1)
             
            lbl3 = QLabel('Amount')  
            logger.debug("__init__(self=%s,parent=%s): lbl3 → %s", self, parent, lbl3)
            logger.debug("__init__(parent=%s): lbl3 → %s", parent, lbl3)
            lbl3.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl3, 3, 0)
            grid.addWidget(hoevEdit, 3 , 1)
                                             
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
    
            applyBtn = QPushButton('Mutate')
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn)
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn)
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 5, 1, 1 , 2, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
           
            cancelBtn = QPushButton('Close')
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn)
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn)
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email)) 
            
            grid.addWidget(cancelBtn,5, 1, Qt.AlignCenter)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 6, 0, 1, 3, Qt.AlignCenter)     
            logger.debug("<<< Exiting __init__(parent=%s)", parent)
                                                                      
        def dervingChanged(self, text):
            logger.debug(">>> Entering dervingChanged(text=%s)", text)
            logger.debug("dervingChanged(self=%s,text=%s): Dervingnummer → %s", self, text, Dervingnummer)
            self.Dervingnummer.setText(text)
            logger.debug("<<< Exiting dervingChanged(text=%s)", text)
            
        def artChanged(self,text):
            logger.debug(">>> Entering artChanged(text=%s)", text)
            logger.debug("artChanged(self=%s,text=%s): Artikelnummer → %s", self, text, Artikelnummer)
            self.Artikelnummer.setText(text)
            logger.debug("<<< Exiting artChanged(text=%s)", text)
            
        def hoevChanged(self,text):
            logger.debug(">>> Entering hoevChanged(text=%s)", text)
            logger.debug("hoevChanged(self=%s,text=%s): Hoeveelheid → %s", self, text, Hoeveelheid)
            self.Hoeveelheid.setText(text)
            logger.debug("<<< Exiting hoevChanged(text=%s)", text)
                                                   
        def returnderving(self):
            logger.debug(">>> Entering returnderving()")
            logger.debug("<<< Exiting returnderving()")
            return self.Dervingnummer.text()
        
        def returnart(self):
            logger.debug(">>> Entering returnart()")
            logger.debug("<<< Exiting returnart()")
            return self.Artikelnummer.text()
        
        def returnhoev(self):
            logger.debug(">>> Entering returnhoev()")
            logger.debug("<<< Exiting returnhoev()")
            return self.Hoeveelheid.text()
                              
        @staticmethod
        def getData(parent=None):
            logger.debug(">>> Entering getData(parent=%s)", parent)
            dialog = Widget(parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog)
            dialog.exec_()
            logger.debug("<<< Exiting getData(parent=%s)", parent)
            return [dialog.returnderving(), dialog.returnart(), dialog.returnhoev()]
    
    window = Widget()
    data = window.getData()
    mhoev = 0
    if not data[0] or data[0][0] == ' ':
        ongInvoer()
        dervingMut(m_email)
    elif data[0][0] == '1':
        mderving = '999999990'
        momschr = 'Obsolete'
    elif data[0][0] == '2':
        mderving = '999999989'
        momschr = 'Warehouse differences'
    elif data[0][0] ==  '3':
        mderving = '999999977'
        momschr = 'Damaged'
    elif data[0][0] == '4':
        mderving = '999999965'
        momschr = 'Shelf life'
                   
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
 