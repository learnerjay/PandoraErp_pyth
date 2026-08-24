from login import hoofdMenu
from datetime import date
from sys import platform
import barcode
from barcode.writer import ImageWriter #for barcode as png
from PyQt5.QtWidgets import QLabel, QLineEdit, QGridLayout, QPushButton,\
                            QDialog, QComboBox, QMessageBox
from PyQt5.QtGui import QRegExpValidator, QFont, QPixmap, QIcon
from PyQt5.QtCore import  QRegExp, Qt
from sqlalchemy import (Table, Column, Integer, String, MetaData,\
                            create_engine, func, Float)
from sqlalchemy.sql import select
import logging
logger = logging.getLogger(__name__)

def windowSluit(self, m_email):
    logger.debug(">>> Entering windowSluit(m_email=%s)", m_email)
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email)

def Invoer():
    logger.debug(">>> Entering Invoer()")
    msg = QMessageBox()
    logger.debug("Invoer(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Information)
    msg.setText('Invoer gelukt!')
    msg.setWindowTitle('Artikelen')
    msg.exec_()
    logger.debug("<<< Exiting Invoer()")
    return

def geenGegevens():
    logger.debug(">>> Entering geenGegevens()")
    msg = QMessageBox()
    logger.debug("geenGegevens(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Critical)
    msg.setText('Niet (alle) vereiste gegevens ingevuld!')
    msg.setWindowTitle('Gegevens!')
    logger.debug("<<< Exiting geenGegevens()")
    msg.exec_()
    
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
   logger.debug("bepaalArtikelnr(): artikelen → %s", artikelen)
   logger.debug("bepaalArtikelnr(): engine → %s", engine)
   return basisuitnr

def bepaalArtikelnr():
    logger.debug(">>> Entering bepaalArtikelnr()")
    metadata = MetaData()
    logger.debug("bepaalArtikelnr(): metadata → %s", metadata)
    artikelen = Table('artikelen', metadata,
        Column('artikelID', Integer(), primary_key=True))
    
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    conn = engine.connect()
    
    logger.debug("bepaalArtikelnr(): conn → %s", conn)
    import time; __log_start = time.time()
    try:
        martikelnr=(conn.execute(select([func.max(artikelen.c.artikelID,\
                type_=Integer)])).scalar())
        martikelnr=int(maak11proef(martikelnr))
        logger.debug("bepaalArtikelnr(): martikelnr → %s", martikelnr)
        logger.info("bepaalArtikelnr()=: find operation took %s ms", int((time.time() - __log_start) * 1000))
        logger.debug("bepaalArtikelnr(): type_ → %s", type_)
    except:
        martikelnr = 200000019
        
    conn.close
    return(martikelnr)
    logger.error("Exception in bepaalArtikelnr()", exc_info=True)
    logger.debug("<<< Exiting bepaalArtikelnr()")
 
def invArtikel(m_email): 
    logger.debug(">>> Entering invArtikel(m_email=%s)", m_email)
    martikelnr = bepaalArtikelnr()
    logger.debug("invArtikel(m_email=%s): martikelnr → %s", m_email, martikelnr)
    ean = barcode.get('ean13', '800'+str(martikelnr), writer=ImageWriter()) # for barcode as png
    mbarcode = ean.get_fullcode()  
    logger.debug("invArtikel(m_email=%s): ean → %s", m_email, ean)
    
    class Widget(QDialog):
        logger.debug("invArtikel(m_email=%s): mbarcode → %s", m_email, mbarcode)
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.debug("<<< Exiting invArtikel(m_email=%s)", m_email)
            self.setWindowTitle("Artikelen Invoeren")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            logger.debug("__init__(parent=%s): input_validator → %s", parent, input_validator)
            self.setFont(QFont('Arial', 10))
    
            self.Artikelnummer = QLabel()
            logger.debug("__init__(parent=%s): self.Artikelnummer → %s", parent, self.Artikelnummer)
            q1Edit = QLineEdit(str(martikelnr))
            logger.debug("__init__(self=%s,parent=%s): q1Edit → %s", self, parent, q1Edit)
            logger.debug("__init__(parent=%s): q1Edit → %s", parent, q1Edit)
            q1Edit.setFixedWidth(100)
            q1Edit.setDisabled(True)
            q1Edit.setFont(QFont("Arial",10))
            q1Edit.textChanged.connect(self.q1Changed)
            
            self.Artikelomschrijving = QLabel()
            logger.debug("__init__(parent=%s): self.Artikelomschrijving → %s", parent, self.Artikelomschrijving)
            q2Edit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): q2Edit → %s", self, parent, q2Edit)
            logger.debug("__init__(parent=%s): q2Edit → %s", parent, q2Edit)
            q2Edit.setFixedWidth(400)
            q2Edit.setFont(QFont("Arial",10))
            q2Edit.textChanged.connect(self.q2Changed)
            reg_ex = QRegExp("^.{1,50}$")
            logger.debug("__init__(self=%s,parent=%s): reg_ex → %s", self, parent, reg_ex)
            logger.debug("__init__(parent=%s): reg_ex → %s", parent, reg_ex)
            input_validator = QRegExpValidator(reg_ex, q2Edit)
            logger.debug("__init__(self=%s,parent=%s): input_validator → %s", self, parent, input_validator)
            q2Edit.setValidator(input_validator)
            
            self.Artikelprijs = QLabel()
            logger.debug("__init__(parent=%s): self.Artikelprijs → %s", parent, self.Artikelprijs)
            q3Edit = QLineEdit('0')
            logger.debug("__init__(self=%s,parent=%s): q3Edit → %s", self, parent, q3Edit)
            logger.debug("__init__(parent=%s): q3Edit → %s", parent, q3Edit)
            q3Edit.setFixedWidth(100)
            q3Edit.setFont(QFont("Arial",10))
            q3Edit.textChanged.connect(self.q3Changed)
            reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q3Edit)
            q3Edit.setValidator(input_validator)
                           
            self.Artikelvoorraad = QLabel()
            logger.debug("__init__(parent=%s): self.Artikelvoorraad → %s", parent, self.Artikelvoorraad)
            q4Edit = QLineEdit('0')
            logger.debug("__init__(self=%s,parent=%s): q4Edit → %s", self, parent, q4Edit)
            logger.debug("__init__(parent=%s): q4Edit → %s", parent, q4Edit)
            q4Edit.setFixedWidth(100)
            q4Edit.setFont(QFont("Arial",10))
            q4Edit.setDisabled(True)
            q4Edit.textChanged.connect(self.q4Changed)
            reg_ex = QRegExp("^[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q4Edit)
            q4Edit.setValidator(input_validator)
            
            self.Artikeleenheid = QLabel()
            logger.debug("__init__(parent=%s): self.Artikeleenheid → %s", parent, self.Artikeleenheid)
            q5Edit = QComboBox()
            logger.debug("__init__(self=%s,parent=%s): q5Edit → %s", self, parent, q5Edit)
            logger.debug("__init__(parent=%s): q5Edit → %s", parent, q5Edit)
            q5Edit.setFixedWidth(160)
            q5Edit.setStyleSheet("color: black;  background-color: #D9E1D")
            q5Edit.setFont(QFont("Arial",10))
            q5Edit.addItem(' Maak uw keuze')
            q5Edit.addItem('stuk')
            q5Edit.addItem('100')
            q5Edit.addItem('meter')
            q5Edit.addItem('kg')
            q5Edit.addItem('liter')
            q5Edit.addItem('m²')
            q5Edit.addItem('m³')
            q5Edit.activated[str].connect(self.q5Changed)      
                    
            self.Minimumvoorraad = QLabel()
            logger.debug("__init__(parent=%s): self.Minimumvoorraad → %s", parent, self.Minimumvoorraad)
            q6Edit = QLineEdit('0')
            logger.debug("__init__(self=%s,parent=%s): q6Edit → %s", self, parent, q6Edit)
            logger.debug("__init__(parent=%s): q6Edit → %s", parent, q6Edit)
            q6Edit.setFixedWidth(100)
            q6Edit.setFont(QFont("Arial",10))
            q6Edit.textChanged.connect(self.q6Changed)
            reg_ex = QRegExp("^[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q6Edit)
            q6Edit.setValidator(input_validator)
          
            self.Bestelgrootte = QLabel()
            logger.debug("__init__(parent=%s): self.Bestelgrootte → %s", parent, self.Bestelgrootte)
            q7Edit = QLineEdit('0')
            logger.debug("__init__(self=%s,parent=%s): q7Edit → %s", self, parent, q7Edit)
            logger.debug("__init__(parent=%s): q7Edit → %s", parent, q7Edit)
            q7Edit.setFixedWidth(100)
            q7Edit.setFont(QFont("Arial",10))
            q7Edit.textChanged.connect(self.q7Changed)
            reg_ex = QRegExp("^[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q7Edit)
            q7Edit.setValidator(input_validator)
                         
            self.Magazijnlocatie = QLabel()
            logger.debug("__init__(parent=%s): self.Magazijnlocatie → %s", parent, self.Magazijnlocatie)
            q8Edit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): q8Edit → %s", self, parent, q8Edit)
            logger.debug("__init__(parent=%s): q8Edit → %s", parent, q8Edit)
            q8Edit.setFixedWidth(100)
            q8Edit.setFont(QFont("Arial",10))
            q8Edit.textChanged.connect(self.q8Changed)
            
            self.Artikelgroep = QLabel()
            logger.debug("__init__(parent=%s): self.Artikelgroep → %s", parent, self.Artikelgroep)
            q9Edit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): q9Edit → %s", self, parent, q9Edit)
            logger.debug("__init__(parent=%s): q9Edit → %s", parent, q9Edit)
            q9Edit.setFixedWidth(200)
            q9Edit.setFont(QFont("Arial",10))
            q9Edit.textChanged.connect(self.q9Changed)
            
            self.Barcode = QLabel()
            logger.debug("__init__(parent=%s): self.Barcode → %s", parent, self.Barcode)
            q10Edit = QLineEdit(mbarcode)
            logger.debug("__init__(self=%s,parent=%s): q10Edit → %s", self, parent, q10Edit)
            logger.debug("__init__(parent=%s): q10Edit → %s", parent, q10Edit)
            q10Edit.setFixedWidth(130)
            q10Edit.setFont(QFont("Arial",10))
            q10Edit.textChanged.connect(self.q10Changed)
            reg_ex = QRegExp('^[1-9]{1,13}$')
            input_validator = QRegExpValidator(reg_ex, q10Edit)
            q10Edit.setValidator(input_validator)
    
            self.Artikelthumbnail = QLabel()
            logger.debug("__init__(parent=%s): self.Artikelthumbnail → %s", parent, self.Artikelthumbnail)
            q11Edit = QLineEdit('./images/thumbs/')
            logger.debug("__init__(self=%s,parent=%s): q11Edit → %s", self, parent, q11Edit)
            logger.debug("__init__(parent=%s): q11Edit → %s", parent, q11Edit)
            q11Edit.setFixedWidth(400)
            q11Edit.setFont(QFont("Arial",10))
            q11Edit.textChanged.connect(self.q11Changed)
                    
            self.Artikelfoto = QLabel()
            logger.debug("__init__(parent=%s): self.Artikelfoto → %s", parent, self.Artikelfoto)
            q12Edit = QLineEdit('./images/')
            logger.debug("__init__(self=%s,parent=%s): q12Edit → %s", self, parent, q12Edit)
            logger.debug("__init__(parent=%s): q12Edit → %s", parent, q12Edit)
            q12Edit.setFixedWidth(400)
            q12Edit.setFont(QFont("Arial",10))
            q12Edit.textChanged.connect(self.q12Changed)
         
            self.Categorie = QLabel()
            logger.debug("__init__(parent=%s): self.Categorie → %s", parent, self.Categorie)
            q13Edit = QComboBox()
            logger.debug("__init__(self=%s,parent=%s): q13Edit → %s", self, parent, q13Edit)
            logger.debug("__init__(parent=%s): q13Edit → %s", parent, q13Edit)
            q13Edit.setFixedWidth(320)
            q13Edit.setFont(QFont("Arial",10))
            q13Edit.setStyleSheet("color: black;  background-color: #D9E1D")
            q13Edit.addItem('                    Maak uw keuze')
            q13Edit.addItem('1. Voorraadgestuurd < 3 weken.')
            q13Edit.addItem('2. Voorraadgestuurd < 12 weken')
            q13Edit.addItem('3. Voorraadgestuurd < 26 weken')
            q13Edit.addItem('4. Voorraadgestuurd < 52 weken')
            q13Edit.addItem('5. Reservering < 3 weken')
            q13Edit.addItem('6. Reservering < 6 weken')
            q13Edit.addItem('7. Reservering < 12 weken')
            q13Edit.addItem('8. Reservering < 24 weken')
            q13Edit.addItem('9. Reservering < 52 weken')
            q13Edit.activated[str].connect(self.q13Changed)     
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap)
                    
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
            grid.addWidget(lbl , 1, 0)
            
            logo = QLabel()
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo)
            logger.debug("__init__(parent=%s): logo → %s", parent, logo)
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 1, 2, 1, 1, Qt.AlignRight)
    
            self.setFont(QFont('Arial', 10))
            grid.addWidget(QLabel('Nieuw artikel invoeren'), 1, 1)
    
            grid.addWidget(QLabel('                                *'),2 , 0)
            grid.addWidget(QLabel('Verplichte velden'), 2, 1)
    
            grid.addWidget(QLabel('Artikelnummer'), 3, 0)
            grid.addWidget(q1Edit, 3, 1)
    
            grid.addWidget(QLabel('Artikelomschrijving     *'), 4, 0)
            grid.addWidget(q2Edit, 4, 1)
    
            grid.addWidget(QLabel('Artikelprijs                 *'), 5, 0)
            grid.addWidget(q3Edit, 5 , 1) 
    
            grid.addWidget(QLabel('Artikelvoorraad'), 6, 0)
            grid.addWidget(q4Edit, 6, 1)
    
            grid.addWidget(QLabel('Artikeleenheid           *'), 7, 0)
            grid.addWidget(q5Edit, 7, 1)
    
            grid.addWidget(QLabel('Minimumvoorraad      *'), 8, 0)
            grid.addWidget(q6Edit, 8, 1)
    
            grid.addWidget(QLabel('Bestelgrootte             *'), 9, 0)
            grid.addWidget(q7Edit, 9, 1)
    
            grid.addWidget(QLabel('Magazijnlocatie         *'), 10, 0)
            grid.addWidget(q8Edit, 10, 1)
    
            grid.addWidget(QLabel('Artikelgroep              *'), 11, 0)
            grid.addWidget(q9Edit, 11, 1) 
    
            grid.addWidget(QLabel('Barcode'), 12, 0)
            grid.addWidget(q10Edit, 12, 1)
    
            grid.addWidget(QLabel('Artikelthumbnail'), 13, 0)
            grid.addWidget(q11Edit, 13, 1)
    
            grid.addWidget(QLabel('Artikelfoto'), 14, 0)
            grid.addWidget(q12Edit, 14, 1)
            
            grid.addWidget(QLabel('Categorie                *'), 15, 0)
            grid.addWidget(q13Edit, 15, 1)
    
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 16, 1)

            applyBtn = QPushButton('Invoeren')
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn)
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn)
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 15, 2)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Sluiten')
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn)
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn)
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
            
            grid.addWidget(cancelBtn, 14, 2)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
    
            self.setLayout(grid)
            self.setGeometry(500, 100, 150, 100)
            logger.debug("<<< Exiting __init__(parent=%s)", parent)
    
        def q1Changed(self, text):
            logger.debug(">>> Entering q1Changed(text=%s)", text)
            logger.debug("q1Changed(self=%s,text=%s): Artikelnummer → %s", self, text, Artikelnummer)
            self.Artikelnummer.setText(text)
            logger.debug("<<< Exiting q1Changed(text=%s)", text)
    
        def q2Changed(self, text):
            logger.debug(">>> Entering q2Changed(text=%s)", text)
            logger.debug("q2Changed(self=%s,text=%s): Artikelomschrijving → %s", self, text, Artikelomschrijving)
            self.Artikelomschrijving.setText(text)
            logger.debug("<<< Exiting q2Changed(text=%s)", text)
    
        def q3Changed(self, text):
            logger.debug(">>> Entering q3Changed(text=%s)", text)
            logger.debug("q3Changed(self=%s,text=%s): Artikelprijs → %s", self, text, Artikelprijs)
            self.Artikelprijs.setText(text)
            logger.debug("<<< Exiting q3Changed(text=%s)", text)
    
        def q4Changed(self, text):
            logger.debug(">>> Entering q4Changed(text=%s)", text)
            logger.debug("q4Changed(self=%s,text=%s): Artikelvoorraad → %s", self, text, Artikelvoorraad)
            self.Artikelvoorraad.setText(text)
            logger.debug("<<< Exiting q4Changed(text=%s)", text)
    
        def q5Changed(self, text):
            logger.debug(">>> Entering q5Changed(text=%s)", text)
            logger.debug("q5Changed(self=%s,text=%s): Artikeleenheid → %s", self, text, Artikeleenheid)
            self.Artikeleenheid.setText(text)
            logger.debug("<<< Exiting q5Changed(text=%s)", text)
    
        def q6Changed(self, text):
            logger.debug(">>> Entering q6Changed(text=%s)", text)
            logger.debug("q6Changed(self=%s,text=%s): Minimumvoorraad → %s", self, text, Minimumvoorraad)
            self.Minimumvoorraad.setText(text)
            logger.debug("<<< Exiting q6Changed(text=%s)", text)
    
        def q7Changed(self, text):
            logger.debug(">>> Entering q7Changed(text=%s)", text)
            logger.debug("q7Changed(self=%s,text=%s): Bestelgrootte → %s", self, text, Bestelgrootte)
            self.Bestelgrootte.setText(text)
            logger.debug("<<< Exiting q7Changed(text=%s)", text)
    
        def q8Changed(self, text):
            logger.debug(">>> Entering q8Changed(text=%s)", text)
            logger.debug("q8Changed(self=%s,text=%s): Magazijnlocatie → %s", self, text, Magazijnlocatie)
            self.Magazijnlocatie.setText(text)
            logger.debug("<<< Exiting q8Changed(text=%s)", text)
    
        def q9Changed(self, text):
            logger.debug(">>> Entering q9Changed(text=%s)", text)
            logger.debug("q9Changed(self=%s,text=%s): Artikelgroep → %s", self, text, Artikelgroep)
            self.Artikelgroep.setText(text)
            logger.debug("<<< Exiting q9Changed(text=%s)", text)
    
        def q10Changed(self, text):
            logger.debug(">>> Entering q10Changed(text=%s)", text)
            logger.debug("q10Changed(self=%s,text=%s): Barcode → %s", self, text, Barcode)
            self.Barcode.setText(text)
            logger.debug("<<< Exiting q10Changed(text=%s)", text)
    
        def q11Changed(self, text):
            logger.debug(">>> Entering q11Changed(text=%s)", text)
            logger.debug("q11Changed(self=%s,text=%s): Artikelthumbnail → %s", self, text, Artikelthumbnail)
            self.Artikelthumbnail.setText(text)
            logger.debug("<<< Exiting q11Changed(text=%s)", text)
    
        def q12Changed(self, text):
            logger.debug(">>> Entering q12Changed(text=%s)", text)
            logger.debug("q12Changed(self=%s,text=%s): Artikelfoto → %s", self, text, Artikelfoto)
            self.Artikelfoto.setText(text)
            logger.debug("<<< Exiting q12Changed(text=%s)", text)
            
        def q13Changed(self, text):
            logger.debug(">>> Entering q13Changed(text=%s)", text)
            logger.debug("q13Changed(self=%s,text=%s): Categorie → %s", self, text, Categorie)
            self.Categorie.setText(text)
            logger.debug("<<< Exiting q13Changed(text=%s)", text)
    
        def returnArtikelnummer(self):
            logger.debug(">>> Entering returnArtikelnummer()")
            logger.debug("<<< Exiting returnArtikelnummer()")
            return self.Artikelnummer.text()
    
        def returnArtikelomschrijving(self):
            logger.debug(">>> Entering returnArtikelomschrijving()")
            logger.debug("<<< Exiting returnArtikelomschrijving()")
            return self.Artikelomschrijving.text()
    
        def returnArtikelprijs(self):
            logger.debug(">>> Entering returnArtikelprijs()")
            logger.debug("<<< Exiting returnArtikelprijs()")
            return self.Artikelprijs.text()
    
        def returnArtikelvoorraad(self):
            logger.debug(">>> Entering returnArtikelvoorraad()")
            logger.debug("<<< Exiting returnArtikelvoorraad()")
            return self.Artikelvoorraad.text()
    
        def returnArtikeleenheid(self):
            logger.debug(">>> Entering returnArtikeleenheid()")
            logger.debug("<<< Exiting returnArtikeleenheid()")
            return self.Artikeleenheid.text()
    
        def returnMinimumvoorraad(self):
            logger.debug(">>> Entering returnMinimumvoorraad()")
            logger.debug("<<< Exiting returnMinimumvoorraad()")
            return self.Minimumvoorraad.text()
    
        def returnBestelgrootte(self):
            logger.debug(">>> Entering returnBestelgrootte()")
            logger.debug("<<< Exiting returnBestelgrootte()")
            return self.Bestelgrootte.text()
    
        def returnMagazijnlocatie(self):
            logger.debug(">>> Entering returnMagazijnlocatie()")
            logger.debug("<<< Exiting returnMagazijnlocatie()")
            return self.Magazijnlocatie.text()
    
        def returnArtikelgroep(self):
            logger.debug(">>> Entering returnArtikelgroep()")
            logger.debug("<<< Exiting returnArtikelgroep()")
            return self.Artikelgroep.text()
    
        def returnBarcode(self):
            logger.debug(">>> Entering returnBarcode()")
            logger.debug("<<< Exiting returnBarcode()")
            return self.Barcode.text()
    
        def returnArtikelthumbnail(self):
            logger.debug(">>> Entering returnArtikelthumbnail()")
            logger.debug("<<< Exiting returnArtikelthumbnail()")
            return self.Artikelthumbnail.text()
    
        def returnArtikelfoto(self):
            logger.debug(">>> Entering returnArtikelfoto()")
            logger.debug("<<< Exiting returnArtikelfoto()")
            return self.Artikelfoto.text()
        
        def returnCategorie(self):
            logger.debug(">>> Entering returnCategorie()")
            logger.debug("<<< Exiting returnCategorie()")
            return self.Categorie.text()
    
        @staticmethod
        def getData(parent=None):
            logger.debug(">>> Entering getData(parent=%s)", parent)
            dialog = Widget(parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog)
            dialog.exec_()
            logger.debug("<<< Exiting getData(parent=%s)", parent)
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