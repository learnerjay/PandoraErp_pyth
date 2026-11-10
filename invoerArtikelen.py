from login import hoofdMenu
from datetime import date
from sys import platform
import barcode
from barcode.writer import ImageWriter #for barcode as png
from PyQt5.QtWidgets import QLabel, QLineEdit, QGridLayout, QPushButton,\
                            QDialog, QComboBox, QMessageBox
import time
from PyQt5.QtGui import QRegExpValidator, QFont, QPixmap, QIcon
from PyQt5.QtCore import  QRegExp, Qt
from sqlalchemy import (Table, Column, Integer, String, MetaData,\
                            create_engine, func, Float)
from sqlalchemy.sql import select
import logging
logger = logging.getLogger(__name__)

def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})

def Invoer():
    logger.warning(">>> Entering Invoer()", extra={"event.action": "Invoer"})
    msg = QMessageBox()
    logger.debug("Invoer(): msg → %s", msg, extra={"event.action": "Invoer"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Information)
    msg.setText('Insert successful!')
    msg.setWindowTitle('Articles')
    msg.exec_()
    logger.debug("<<< Exiting Invoer()", extra={"event.action": "Invoer"})
    return

def geenGegevens():
    logger.warning(">>> Entering geenGegevens()", extra={"event.action": "geenGegevens"})
    msg = QMessageBox()
    logger.debug("geenGegevens(): msg → %s", msg, extra={"event.action": "geenGegevens"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Critical)
    msg.setText('Not (all) required data inserted!')
    msg.setWindowTitle('Data')
    logger.debug("<<< Exiting geenGegevens()", extra={"event.action": "geenGegevens"})
    msg.exec_()
    
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

def bepaalArtikelnr():
    logger.warning(">>> Entering bepaalArtikelnr()", extra={"event.action": "bepaalArtikelnr"})
    metadata = MetaData()
    logger.debug("bepaalArtikelnr(): metadata → %s", metadata, extra={"event.action": "bepaalArtikelnr"})
    artikelen = Table('artikelen', metadata,
        Column('artikelID', Integer(), primary_key=True))
    
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("bepaalArtikelnr(): engine → %s", engine, extra={"event.action": "bepaalArtikelnr"})
    conn = engine.connect()
    logger.debug("bepaalArtikelnr(): conn → %s", conn, extra={"event.action": "bepaalArtikelnr"})
    
    try:
        __log_start = time.time()
        martikelnr=(conn.execute(select([func.max(artikelen.c.artikelID,\
                type_=Integer)])).scalar())
        martikelnr=int(maak11proef(martikelnr))
    except:
        logger.debug("bepaalArtikelnr(): type_ → %s", type_, extra={"event.action": "bepaalArtikelnr"})
        logger.info("bepaalArtikelnr()=: find operation took %s ms", int((time.time() - __log_start) * 1000), extra={"event.action": "bepaalArtikelnr", "event.category": "database"})
        martikelnr = 200000019
        logger.debug("bepaalArtikelnr(): martikelnr → %s", martikelnr, extra={"event.action": "bepaalArtikelnr"})
        
        logger.error("Exception in bepaalArtikelnr()", exc_info=True, extra={"event.action": "bepaalArtikelnr", "event.category": "process"})
    conn.close
    logger.debug("<<< Exiting bepaalArtikelnr()", extra={"event.action": "bepaalArtikelnr"})
    return(martikelnr)
 
def invArtikel(m_email): 
    logger.warning(">>> Entering invArtikel(m_email=%s)", m_email, extra={"event.action": "invArtikel"})
    martikelnr = bepaalArtikelnr()
    logger.debug("invArtikel(m_email=%s): martikelnr → %s", m_email, martikelnr, extra={"event.action": "invArtikel"})
    ean = barcode.get('ean13', '800'+str(martikelnr), writer=ImageWriter()) # for barcode as png
    mbarcode = ean.get_fullcode()  
    logger.debug("invArtikel(m_email=%s): ean → %s", m_email, ean, extra={"event.action": "invArtikel"})
    
    class Widget(QDialog):
        logger.debug("invArtikel(m_email=%s): mbarcode → %s", m_email, mbarcode, extra={"event.action": "invArtikel"})
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.debug("<<< Exiting invArtikel(m_email=%s)", m_email, extra={"event.action": "invArtikel"})
            self.setWindowTitle("Insert Articles")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
    
            self.Artikelnummer = QLabel()
            logger.debug("__init__(parent=%s): self.Artikelnummer → %s", parent, self.Artikelnummer, extra={"event.action": "__init__"})
            q1Edit = QLineEdit(str(martikelnr))
            logger.debug("__init__(self=%s,parent=%s): q1Edit → %s", self, parent, q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q1Edit → %s", parent, q1Edit, extra={"event.action": "__init__"})
            q1Edit.setFixedWidth(100)
            q1Edit.setDisabled(True)
            q1Edit.setFont(QFont("Arial",10))
            q1Edit.textChanged.connect(self.q1Changed)
            
            self.Artikelomschrijving = QLabel()
            logger.debug("__init__(parent=%s): self.Artikelomschrijving → %s", parent, self.Artikelomschrijving, extra={"event.action": "__init__"})
            q2Edit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): q2Edit → %s", self, parent, q2Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q2Edit → %s", parent, q2Edit, extra={"event.action": "__init__"})
            q2Edit.setFixedWidth(400)
            q2Edit.setFont(QFont("Arial",10))
            q2Edit.textChanged.connect(self.q2Changed)
            reg_ex = QRegExp("^.{1,50}$")
            logger.debug("__init__(parent=%s): reg_ex → %s", parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): reg_ex → %s", self, parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Artikelprijs → %s", parent, self.Artikelprijs, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q3Edit → %s", parent, q3Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q3Edit → %s", self, parent, q3Edit, extra={"event.action": "__init__"})
            input_validator = QRegExpValidator(reg_ex, q2Edit)
            logger.debug("__init__(self=%s,parent=%s): input_validator → %s", self, parent, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): input_validator → %s", parent, input_validator, extra={"event.action": "__init__"})
            q2Edit.setValidator(input_validator)
            
            self.Artikelprijs = QLabel()
            q3Edit = QLineEdit('0')
            q3Edit.setFixedWidth(100)
            q3Edit.setFont(QFont("Arial",10))
            q3Edit.textChanged.connect(self.q3Changed)
            reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q3Edit)
            q3Edit.setValidator(input_validator)
                           
            self.Artikelvoorraad = QLabel()
            logger.debug("__init__(parent=%s): self.Artikelvoorraad → %s", parent, self.Artikelvoorraad, extra={"event.action": "__init__"})
            q4Edit = QLineEdit('0')
            logger.debug("__init__(self=%s,parent=%s): q4Edit → %s", self, parent, q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q4Edit → %s", parent, q4Edit, extra={"event.action": "__init__"})
            q4Edit.setFixedWidth(100)
            q4Edit.setFont(QFont("Arial",10))
            q4Edit.setDisabled(True)
            q4Edit.textChanged.connect(self.q4Changed)
            reg_ex = QRegExp("^[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q4Edit)
            q4Edit.setValidator(input_validator)
            
            self.Artikeleenheid = QLabel()
            logger.debug("__init__(parent=%s): self.Artikeleenheid → %s", parent, self.Artikeleenheid, extra={"event.action": "__init__"})
            q5Edit = QComboBox()
            logger.debug("__init__(self=%s,parent=%s): q5Edit → %s", self, parent, q5Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q5Edit → %s", parent, q5Edit, extra={"event.action": "__init__"})
            q5Edit.setFixedWidth(160)
            q5Edit.setStyleSheet("color: black;  background-color: #D9E1D")
            q5Edit.setFont(QFont("Arial",10))
            q5Edit.addItem(' Make your choice')
            q5Edit.addItem('piece')
            q5Edit.addItem('100')
            q5Edit.addItem('meter')
            q5Edit.addItem('kg')
            q5Edit.addItem('liter')
            q5Edit.addItem('m²')
            q5Edit.addItem('m³')
            q5Edit.activated[str].connect(self.q5Changed)      
                    
            self.Minimumvoorraad = QLabel()
            logger.debug("__init__(parent=%s): self.Minimumvoorraad → %s", parent, self.Minimumvoorraad, extra={"event.action": "__init__"})
            q6Edit = QLineEdit('0')
            logger.debug("__init__(self=%s,parent=%s): q6Edit → %s", self, parent, q6Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q6Edit → %s", parent, q6Edit, extra={"event.action": "__init__"})
            q6Edit.setFixedWidth(100)
            q6Edit.setFont(QFont("Arial",10))
            q6Edit.textChanged.connect(self.q6Changed)
            reg_ex = QRegExp("^[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q6Edit)
            q6Edit.setValidator(input_validator)
          
            self.Bestelgrootte = QLabel()
            logger.debug("__init__(parent=%s): self.Bestelgrootte → %s", parent, self.Bestelgrootte, extra={"event.action": "__init__"})
            q7Edit = QLineEdit('0')
            logger.debug("__init__(self=%s,parent=%s): q7Edit → %s", self, parent, q7Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q7Edit → %s", parent, q7Edit, extra={"event.action": "__init__"})
            q7Edit.setFixedWidth(100)
            q7Edit.setFont(QFont("Arial",10))
            q7Edit.textChanged.connect(self.q7Changed)
            reg_ex = QRegExp("^[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q7Edit)
            q7Edit.setValidator(input_validator)
                         
            self.Magazijnlocatie = QLabel()
            logger.debug("__init__(parent=%s): self.Magazijnlocatie → %s", parent, self.Magazijnlocatie, extra={"event.action": "__init__"})
            q8Edit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): q8Edit → %s", self, parent, q8Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q8Edit → %s", parent, q8Edit, extra={"event.action": "__init__"})
            q8Edit.setFixedWidth(100)
            q8Edit.setFont(QFont("Arial",10))
            q8Edit.textChanged.connect(self.q8Changed)
            
            self.Artikelgroep = QLabel()
            logger.debug("__init__(parent=%s): self.Artikelgroep → %s", parent, self.Artikelgroep, extra={"event.action": "__init__"})
            q9Edit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): q9Edit → %s", self, parent, q9Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q9Edit → %s", parent, q9Edit, extra={"event.action": "__init__"})
            q9Edit.setFixedWidth(200)
            q9Edit.setFont(QFont("Arial",10))
            q9Edit.textChanged.connect(self.q9Changed)
            
            self.Barcode = QLabel()
            logger.debug("__init__(parent=%s): self.Barcode → %s", parent, self.Barcode, extra={"event.action": "__init__"})
            q10Edit = QLineEdit(mbarcode)
            logger.debug("__init__(self=%s,parent=%s): q10Edit → %s", self, parent, q10Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q10Edit → %s", parent, q10Edit, extra={"event.action": "__init__"})
            q10Edit.setFixedWidth(130)
            q10Edit.setFont(QFont("Arial",10))
            q10Edit.textChanged.connect(self.q10Changed)
            reg_ex = QRegExp('^[1-9]{1,13}$')
            input_validator = QRegExpValidator(reg_ex, q10Edit)
            q10Edit.setValidator(input_validator)
    
            self.Artikelthumbnail = QLabel()
            logger.debug("__init__(parent=%s): self.Artikelthumbnail → %s", parent, self.Artikelthumbnail, extra={"event.action": "__init__"})
            q11Edit = QLineEdit('./images/thumbs/')
            logger.debug("__init__(self=%s,parent=%s): q11Edit → %s", self, parent, q11Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q11Edit → %s", parent, q11Edit, extra={"event.action": "__init__"})
            q11Edit.setFixedWidth(400)
            q11Edit.setFont(QFont("Arial",10))
            q11Edit.textChanged.connect(self.q11Changed)
                    
            self.Artikelfoto = QLabel()
            logger.debug("__init__(parent=%s): self.Artikelfoto → %s", parent, self.Artikelfoto, extra={"event.action": "__init__"})
            q12Edit = QLineEdit('./images/')
            logger.debug("__init__(self=%s,parent=%s): q12Edit → %s", self, parent, q12Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q12Edit → %s", parent, q12Edit, extra={"event.action": "__init__"})
            q12Edit.setFixedWidth(400)
            q12Edit.setFont(QFont("Arial",10))
            q12Edit.textChanged.connect(self.q12Changed)
         
            self.Categorie = QLabel()
            logger.debug("__init__(parent=%s): self.Categorie → %s", parent, self.Categorie, extra={"event.action": "__init__"})
            q13Edit = QComboBox()
            logger.debug("__init__(self=%s,parent=%s): q13Edit → %s", self, parent, q13Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q13Edit → %s", parent, q13Edit, extra={"event.action": "__init__"})
            q13Edit.setFixedWidth(320)
            q13Edit.setFont(QFont("Arial",10))
            q13Edit.setStyleSheet("color: black;  background-color: #D9E1D")
            q13Edit.addItem('                    Make your choice')
            q13Edit.addItem('1. Stock controlled < 3 weeks')
            q13Edit.addItem('2. Stock controlled < 12 weeks')
            q13Edit.addItem('3. Stock controlled < 26 weeks')
            q13Edit.addItem('4. Stock controlled < 52 weeks')
            q13Edit.addItem('5. Reservation < 3 weeks')
            q13Edit.addItem('6. Reservation < 6 weeks')
            q13Edit.addItem('7. Reservation < 12 weeks')
            q13Edit.addItem('8. Reservation < 24 weeks')
            q13Edit.addItem('9. Reservation < 52 weeks')
            q13Edit.activated[str].connect(self.q13Changed)     
                    
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
            
            logo = QLabel()
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 1, 2, 1, 1, Qt.AlignRight)
    
            self.setFont(QFont('Arial', 10))
            grid.addWidget(QLabel('Insert New Article'), 1, 1)
    
            grid.addWidget(QLabel('                                *'),2 , 0)
            grid.addWidget(QLabel('Required fields  '), 2, 1)
    
            grid.addWidget(QLabel('Article number'), 3, 0)
            grid.addWidget(q1Edit, 3, 1)
    
            grid.addWidget(QLabel('ArticleDescription       *'), 4, 0)
            grid.addWidget(q2Edit, 4, 1)
    
            grid.addWidget(QLabel('Article price                *'), 5, 0)
            grid.addWidget(q3Edit, 5 , 1) 
    
            grid.addWidget(QLabel('Article stock   '), 6, 0)
            grid.addWidget(q4Edit, 6, 1)
    
            grid.addWidget(QLabel('Article Unit                  *'), 7, 0)
            grid.addWidget(q5Edit, 7, 1)
    
            grid.addWidget(QLabel('Minimum stock           *'), 8, 0)
            grid.addWidget(q6Edit, 8, 1)
    
            grid.addWidget(QLabel('Order size                  *'), 9, 0)
            grid.addWidget(q7Edit, 9, 1)
    
            grid.addWidget(QLabel('WarehouseLocation    *'), 10, 0)
            grid.addWidget(q8Edit, 10, 1)
    
            grid.addWidget(QLabel('ArticleGroup               *'), 11, 0)
            grid.addWidget(q9Edit, 11, 1) 
    
            grid.addWidget(QLabel('Barcode'), 12, 0)
            grid.addWidget(q10Edit, 12, 1)
    
            grid.addWidget(QLabel('ArticleThumbnail'), 13, 0)
            grid.addWidget(q11Edit, 13, 1)
    
            grid.addWidget(QLabel('ArticlePhoto'), 14, 0)
            grid.addWidget(q12Edit, 14, 1)
            
            grid.addWidget(QLabel('Category                     *'), 15, 0)
            grid.addWidget(q13Edit, 15, 1)
    
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 16, 1)

            applyBtn = QPushButton('Insert')
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn, extra={"event.action": "__init__"})
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 15, 2)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Close')
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn, extra={"event.action": "__init__"})
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
            
            grid.addWidget(cancelBtn, 14, 2)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
    
            self.setLayout(grid)
            self.setGeometry(500, 100, 150, 100)
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
    
        def q1Changed(self, text):
            logger.warning(">>> Entering q1Changed(text=%s)", text, extra={"event.action": "q1Changed", "logrite.text": text})
            self.Artikelnummer.setText(text)
            logger.debug("<<< Exiting q1Changed(text=%s)", text, extra={"event.action": "q1Changed", "logrite.text": text})
    
        def q2Changed(self, text):
            logger.warning(">>> Entering q2Changed(text=%s)", text, extra={"event.action": "q2Changed", "logrite.text": text})
            self.Artikelomschrijving.setText(text)
            logger.debug("<<< Exiting q2Changed(text=%s)", text, extra={"event.action": "q2Changed", "logrite.text": text})
    
        def q3Changed(self, text):
            logger.warning(">>> Entering q3Changed(text=%s)", text, extra={"event.action": "q3Changed", "logrite.text": text})
            self.Artikelprijs.setText(text)
            logger.debug("<<< Exiting q3Changed(text=%s)", text, extra={"event.action": "q3Changed", "logrite.text": text})
    
        def q4Changed(self, text):
            logger.warning(">>> Entering q4Changed(text=%s)", text, extra={"event.action": "q4Changed", "logrite.text": text})
            self.Artikelvoorraad.setText(text)
            logger.debug("<<< Exiting q4Changed(text=%s)", text, extra={"event.action": "q4Changed", "logrite.text": text})
    
        def q5Changed(self, text):
            logger.warning(">>> Entering q5Changed(text=%s)", text, extra={"event.action": "q5Changed", "logrite.text": text})
            self.Artikeleenheid.setText(text)
            logger.debug("<<< Exiting q5Changed(text=%s)", text, extra={"event.action": "q5Changed", "logrite.text": text})
    
        def q6Changed(self, text):
            logger.warning(">>> Entering q6Changed(text=%s)", text, extra={"event.action": "q6Changed", "logrite.text": text})
            self.Minimumvoorraad.setText(text)
            logger.debug("<<< Exiting q6Changed(text=%s)", text, extra={"event.action": "q6Changed", "logrite.text": text})
    
        def q7Changed(self, text):
            logger.warning(">>> Entering q7Changed(text=%s)", text, extra={"event.action": "q7Changed", "logrite.text": text})
            self.Bestelgrootte.setText(text)
            logger.debug("<<< Exiting q7Changed(text=%s)", text, extra={"event.action": "q7Changed", "logrite.text": text})
    
        def q8Changed(self, text):
            logger.warning(">>> Entering q8Changed(text=%s)", text, extra={"event.action": "q8Changed", "logrite.text": text})
            self.Magazijnlocatie.setText(text)
            logger.debug("<<< Exiting q8Changed(text=%s)", text, extra={"event.action": "q8Changed", "logrite.text": text})
    
        def q9Changed(self, text):
            logger.warning(">>> Entering q9Changed(text=%s)", text, extra={"event.action": "q9Changed", "logrite.text": text})
            self.Artikelgroep.setText(text)
            logger.debug("<<< Exiting q9Changed(text=%s)", text, extra={"event.action": "q9Changed", "logrite.text": text})
    
        def q10Changed(self, text):
            logger.warning(">>> Entering q10Changed(text=%s)", text, extra={"event.action": "q10Changed", "logrite.text": text})
            self.Barcode.setText(text)
            logger.debug("<<< Exiting q10Changed(text=%s)", text, extra={"event.action": "q10Changed", "logrite.text": text})
    
        def q11Changed(self, text):
            logger.warning(">>> Entering q11Changed(text=%s)", text, extra={"event.action": "q11Changed", "logrite.text": text})
            self.Artikelthumbnail.setText(text)
            logger.debug("<<< Exiting q11Changed(text=%s)", text, extra={"event.action": "q11Changed", "logrite.text": text})
    
        def q12Changed(self, text):
            logger.warning(">>> Entering q12Changed(text=%s)", text, extra={"event.action": "q12Changed", "logrite.text": text})
            self.Artikelfoto.setText(text)
            logger.debug("<<< Exiting q12Changed(text=%s)", text, extra={"event.action": "q12Changed", "logrite.text": text})
            
        def q13Changed(self, text):
            logger.warning(">>> Entering q13Changed(text=%s)", text, extra={"event.action": "q13Changed", "logrite.text": text})
            self.Categorie.setText(text)
            logger.debug("<<< Exiting q13Changed(text=%s)", text, extra={"event.action": "q13Changed", "logrite.text": text})
    
        def returnArtikelnummer(self):
            logger.warning(">>> Entering returnArtikelnummer()", extra={"event.action": "returnArtikelnummer"})
            logger.debug("<<< Exiting returnArtikelnummer()", extra={"event.action": "returnArtikelnummer"})
            return self.Artikelnummer.text()
    
        def returnArtikelomschrijving(self):
            logger.warning(">>> Entering returnArtikelomschrijving()", extra={"event.action": "returnArtikelomschrijving"})
            logger.debug("<<< Exiting returnArtikelomschrijving()", extra={"event.action": "returnArtikelomschrijving"})
            return self.Artikelomschrijving.text()
    
        def returnArtikelprijs(self):
            logger.warning(">>> Entering returnArtikelprijs()", extra={"event.action": "returnArtikelprijs"})
            logger.debug("<<< Exiting returnArtikelprijs()", extra={"event.action": "returnArtikelprijs"})
            return self.Artikelprijs.text()
    
        def returnArtikelvoorraad(self):
            logger.warning(">>> Entering returnArtikelvoorraad()", extra={"event.action": "returnArtikelvoorraad"})
            logger.debug("<<< Exiting returnArtikelvoorraad()", extra={"event.action": "returnArtikelvoorraad"})
            return self.Artikelvoorraad.text()
    
        def returnArtikeleenheid(self):
            logger.warning(">>> Entering returnArtikeleenheid()", extra={"event.action": "returnArtikeleenheid"})
            logger.debug("<<< Exiting returnArtikeleenheid()", extra={"event.action": "returnArtikeleenheid"})
            return self.Artikeleenheid.text()
    
        def returnMinimumvoorraad(self):
            logger.warning(">>> Entering returnMinimumvoorraad()", extra={"event.action": "returnMinimumvoorraad"})
            logger.debug("<<< Exiting returnMinimumvoorraad()", extra={"event.action": "returnMinimumvoorraad"})
            return self.Minimumvoorraad.text()
    
        def returnBestelgrootte(self):
            logger.warning(">>> Entering returnBestelgrootte()", extra={"event.action": "returnBestelgrootte"})
            logger.debug("<<< Exiting returnBestelgrootte()", extra={"event.action": "returnBestelgrootte"})
            return self.Bestelgrootte.text()
    
        def returnMagazijnlocatie(self):
            logger.warning(">>> Entering returnMagazijnlocatie()", extra={"event.action": "returnMagazijnlocatie"})
            logger.debug("<<< Exiting returnMagazijnlocatie()", extra={"event.action": "returnMagazijnlocatie"})
            return self.Magazijnlocatie.text()
    
        def returnArtikelgroep(self):
            logger.warning(">>> Entering returnArtikelgroep()", extra={"event.action": "returnArtikelgroep"})
            logger.debug("<<< Exiting returnArtikelgroep()", extra={"event.action": "returnArtikelgroep"})
            return self.Artikelgroep.text()
    
        def returnBarcode(self):
            logger.warning(">>> Entering returnBarcode()", extra={"event.action": "returnBarcode"})
            logger.debug("<<< Exiting returnBarcode()", extra={"event.action": "returnBarcode"})
            return self.Barcode.text()
    
        def returnArtikelthumbnail(self):
            logger.warning(">>> Entering returnArtikelthumbnail()", extra={"event.action": "returnArtikelthumbnail"})
            logger.debug("<<< Exiting returnArtikelthumbnail()", extra={"event.action": "returnArtikelthumbnail"})
            return self.Artikelthumbnail.text()
    
        def returnArtikelfoto(self):
            logger.warning(">>> Entering returnArtikelfoto()", extra={"event.action": "returnArtikelfoto"})
            logger.debug("<<< Exiting returnArtikelfoto()", extra={"event.action": "returnArtikelfoto"})
            return self.Artikelfoto.text()
        
        def returnCategorie(self):
            logger.warning(">>> Entering returnCategorie()", extra={"event.action": "returnCategorie"})
            logger.debug("<<< Exiting returnCategorie()", extra={"event.action": "returnCategorie"})
            return self.Categorie.text()
    
        @staticmethod
        def getData(parent=None):
            logger.warning(">>> Entering getData(parent=%s)", parent, extra={"event.action": "getData"})
            dialog = Widget(parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog, extra={"event.action": "getData"})
            dialog.exec_()
            logger.debug("<<< Exiting getData(parent=%s)", parent, extra={"event.action": "getData"})
            return [dialog.returnArtikelnummer(),dialog.returnArtikelomschrijving(),\
                    dialog.returnArtikelprijs(), dialog.returnArtikelvoorraad(),\
                    dialog.returnArtikeleenheid(), dialog.returnMinimumvoorraad(),\
                    dialog.returnBestelgrootte(), dialog.returnMagazijnlocatie(),\
                    dialog.returnArtikelgroep(), dialog.returnBarcode(),\
                    dialog.returnArtikelthumbnail(),dialog.returnArtikelfoto(),\
                    dialog.returnCategorie()]
    
    window = Widget()
    data = window.getData()
    martomschr = data[1]
    martprijs = data[2] 
    if data[2]:
        martprijs = float(martprijs)
    else:
        martprijs = float(0)
    martvrd = data[3]
    if data[3]:
        martvrd = float(martvrd)
    else:
        martvrd = float(0)
    marteenh = data[4]
    martminvrd = data[5]
    if data[5]:
        martminvrd = float(martminvrd)
    else:
        martminvrd = float(0)
    martbestgr = data[6]
    if data[6]:
        martbestgr = float(martbestgr)
    else:
        martbestgr = float(0)
    mlocmag = data[7]
    martgr = data[8]
    mbarc = data[9]
    if data[9]:
        mbarc = int(mbarc)
    else:
        mbarc = int(0)
    mthumb = data[10]
    mfotoart = data[11]
    mcat = 0
    if data[12]:
        mcat = data[12]
        mcat = int(mcat[0])
    if martomschr and martprijs and marteenh and martminvrd and martbestgr and \
               mlocmag and martgr and mcat:
 
        metadata = MetaData()

        artikelen = Table('artikelen', metadata,
            Column('artikelID', Integer(), primary_key=True),
            Column('artikelomschrijving', String),
            Column('artikelprijs', Float),
            Column('art_voorraad', Float),
            Column('art_eenheid', String(20)),
            Column('art_min_voorraad', Float),
            Column('art_bestelgrootte', Float),
            Column('locatie_magazijn', String(10)),
            Column('artikelgroep', String),
            Column('barcode', Integer),
            Column('thumb_artikel', String(70)),
            Column('foto_artikel', String(70)),
            Column('categorie', String(10)),
            Column('afmeting', String),
            Column('mutatiedatum', String))
    
        engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
        martikelnr=bepaalArtikelnr()
        metadata.create_all(engine)
        insart = artikelen.insert().values(
        artikelID = martikelnr,
        barcode = mbarcode,
        artikelomschrijving = martomschr,
        artikelprijs = martprijs,
        art_voorraad = martvrd,
        art_eenheid = marteenh,
        art_min_voorraad = martminvrd,
        art_bestelgrootte = martbestgr,
        locatie_magazijn = mlocmag,
        artikelgroep = martgr,
        thumb_artikel = mthumb,
        foto_artikel = mfotoart,
        categorie = mcat,
        mutatiedatum = str(date.today())[0:10])
    
        conn = engine.connect()
        conn.execute(insart)
        conn.close
        ean = barcode.get('ean13', '800'+str(martikelnr), writer=ImageWriter()) # for barcode as png
        if platform == 'win32':
            ean.save('.\\forms\\Barcodelabels\\'+str(martikelnr))
        else:
            ean.save('./forms/Barcodelabels/'+str(martikelnr))
        Invoer()
        invArtikel(m_email)
    else:
        geenGegevens()
        invArtikel(m_email)
    hoofdMenu(m_email)