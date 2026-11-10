from login import hoofdMenu
from PyQt5.QtWidgets import QLabel, QLineEdit, QGridLayout, QPushButton,\
                            QDialog, QMessageBox, QComboBox
from PyQt5.QtGui import QRegExpValidator, QFont, QPixmap, QIcon
from PyQt5.QtCore import  QRegExp, Qt
from sqlalchemy import (Table, Column, Integer, String, MetaData,\
                                create_engine, Float)
from sqlalchemy.sql import select, update
import logging
logger = logging.getLogger(__name__)

def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    
def wijzSluit(self, m_email):
    logger.warning(">>> Entering wijzSluit(m_email=%s)", m_email, extra={"event.action": "wijzSluit"})
    self.close()
    zoekArtikel(m_email)
    logger.debug("<<< Exiting wijzSluit(m_email=%s)", m_email, extra={"event.action": "wijzSluit"})
   
def foutArtnr():
    logger.warning(">>> Entering foutArtnr()", extra={"event.action": "foutArtnr"})
    msg = QMessageBox()
    logger.debug("foutArtnr(): msg → %s", msg, extra={"event.action": "foutArtnr"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Critical)
    msg.setText('Artikelnummer\nNiet aanwezig!')
    msg.setWindowTitle('Artikel bestaat niet')
    logger.debug("<<< Exiting foutArtnr()", extra={"event.action": "foutArtnr"})
    msg.exec_()
       
def progSluit():
    logger.warning(">>> Entering progSluit()", extra={"event.action": "progSluit"})
    msg = QMessageBox()
    logger.debug("progSluit(): msg → %s", msg, extra={"event.action": "progSluit"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Information)
    msg.setText('Programma Afgesloten\nTot ziens!')
    msg.setWindowTitle('SLUITEN')
    logger.debug("<<< Exiting progSluit()", extra={"event.action": "progSluit"})
    msg.exec_()
    
def updateOK():
    logger.warning(">>> Entering updateOK()", extra={"event.action": "updateOK"})
    msg = QMessageBox()
    logger.debug("updateOK(): msg → %s", msg, extra={"event.action": "updateOK"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Information)
    msg.setText('Je gegevens zijn aangepast!')
    msg.setWindowTitle('Gegevens!')
    logger.debug("<<< Exiting updateOK()", extra={"event.action": "updateOK"})
    msg.exec_()
           
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
    
def zoekArtikel(m_email):     
    logger.warning(">>> Entering zoekArtikel(m_email=%s)", m_email, extra={"event.action": "zoekArtikel"})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            self.setWindowTitle("Artikelen Wijzigen.")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
    
            self.Artikelnummer = QLabel()
            logger.debug("__init__(parent=%s): self.Artikelnummer → %s", parent, self.Artikelnummer, extra={"event.action": "__init__"})
            artEdit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): artEdit → %s", self, parent, artEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): artEdit → %s", parent, artEdit, extra={"event.action": "__init__"})
            artEdit.setFixedWidth(100)
            artEdit.setFont(QFont("Arial",10))
            artEdit.textChanged.connect(self.artChanged)
            reg_ex = QRegExp('^[2]{1}[0-9]{8}$')
            logger.debug("__init__(parent=%s): reg_ex → %s", parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): reg_ex → %s", self, parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): grid → %s", parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid, extra={"event.action": "__init__"})
            input_validator = QRegExpValidator(reg_ex, artEdit)
            logger.debug("__init__(self=%s,parent=%s): input_validator → %s", self, parent, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): input_validator → %s", parent, input_validator, extra={"event.action": "__init__"})
            artEdit.setValidator(input_validator)
                            
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
            
            logo = QLabel()
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 2, 1, 1, Qt.AlignRight) 
        
    
            self.setFont(QFont('Arial', 10))
    
            grid.addWidget(QLabel('Artikelnummer'), 1, 1)
            grid.addWidget(artEdit, 1, 2)
       
            cancelBtn = QPushButton('Sluiten')
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn, extra={"event.action": "__init__"})
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
         
            applyBtn = QPushButton('Zoeken')
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn, extra={"event.action": "__init__"})
            applyBtn.clicked.connect(self.accept)
                  
            grid.addWidget(applyBtn, 2, 2, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
        
            grid.addWidget(cancelBtn, 2, 1, 1, 1, Qt.AlignRight)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 3, 0, 1, 3, Qt.AlignCenter)
            
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            logger.warning(">>> Entering __init__()", extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Artikelnummer → %s", self.Artikelnummer, extra={"event.action": "__init__"})
            logger.debug("__init__(): q1Edit → %s", q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q1Edit → %s", self, q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Artikelomschrijving → %s", self.Artikelomschrijving, extra={"event.action": "__init__"})
            logger.debug("__init__(): q2Edit → %s", q2Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q2Edit → %s", self, q2Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Artikelprijs → %s", self.Artikelprijs, extra={"event.action": "__init__"})
            logger.debug("__init__(): q3Edit → %s", q3Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q3Edit → %s", self, q3Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): reg_ex → %s", reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): reg_ex → %s", self, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(): input_validator → %s", input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): input_validator → %s", self, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Artikelvoorraad → %s", self.Artikelvoorraad, extra={"event.action": "__init__"})
            logger.debug("__init__(): q4Edit → %s", q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q4Edit → %s", self, q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Artikeleenheid → %s", self.Artikeleenheid, extra={"event.action": "__init__"})
            logger.debug("__init__(): q5Edit → %s", q5Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q5Edit → %s", self, q5Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Minimumvoorraad → %s", self.Minimumvoorraad, extra={"event.action": "__init__"})
            logger.debug("__init__(): q6Edit → %s", q6Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q6Edit → %s", self, q6Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Bestelgrootte → %s", self.Bestelgrootte, extra={"event.action": "__init__"})
            logger.debug("__init__(): q7Edit → %s", q7Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q7Edit → %s", self, q7Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Magazijnlocatie → %s", self.Magazijnlocatie, extra={"event.action": "__init__"})
            logger.debug("__init__(): q8Edit → %s", q8Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q8Edit → %s", self, q8Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Artikelgroep → %s", self.Artikelgroep, extra={"event.action": "__init__"})
            logger.debug("__init__(): q9Edit → %s", q9Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q9Edit → %s", self, q9Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Barcode → %s", self.Barcode, extra={"event.action": "__init__"})
            logger.debug("__init__(): q10Edit → %s", q10Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q10Edit → %s", self, q10Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Artikelthumbnail → %s", self.Artikelthumbnail, extra={"event.action": "__init__"})
            logger.debug("__init__(): q11Edit → %s", q11Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q11Edit → %s", self, q11Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Artikelfoto → %s", self.Artikelfoto, extra={"event.action": "__init__"})
            logger.debug("__init__(): q12Edit → %s", q12Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q12Edit → %s", self, q12Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Categorie → %s", self.Categorie, extra={"event.action": "__init__"})
            logger.debug("__init__(): q13Edit → %s", q13Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q13Edit → %s", self, q13Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): grid → %s", grid, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): grid → %s", self, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl → %s", lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl → %s", self, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(): pixmap → %s", pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): pixmap → %s", self, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(): logo → %s", logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): logo → %s", self, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(): applyBtn → %s", applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): applyBtn → %s", self, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(): cancelBtn → %s", cancelBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): cancelBtn → %s", self, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("<<< Exiting __init__()", extra={"event.action": "__init__"})
    
        def artChanged(self, text):
            logger.warning(">>> Entering artChanged(text=%s)", text, extra={"event.action": "artChanged", "logrite.text": text})
            self.Artikelnummer.setText(text)
            logger.debug("<<< Exiting artChanged(text=%s)", text, extra={"event.action": "artChanged", "logrite.text": text})
    
        def returnArtikelnummer(self):
            return self.Artikelnummer.text()
    
        logger.warning(">>> Entering returnArtikelnummer()", extra={"event.action": "returnArtikelnummer"})
        logger.debug("<<< Exiting returnArtikelnummer()", extra={"event.action": "returnArtikelnummer"})
        @staticmethod
        def getData(parent=None):
            dialog = Widget(parent)
            dialog.exec_()
            logger.warning(">>> Entering getData(parent=%s)", parent, extra={"event.action": "getData"})
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog, extra={"event.action": "getData"})
            logger.debug("<<< Exiting getData(parent=%s)", parent, extra={"event.action": "getData"})
            return [dialog.returnArtikelnummer()]
       
    window = Widget()
    data = window.getData()
    if data[0]:
        martikelnr = data[0]
    else:
        martikelnr = 0
    
    metadata = MetaData()
    artikelen = Table('artikelen', metadata,
        Column('artikelID', Integer(), primary_key=True))
  
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    conn = engine.connect()
   
    s = select([artikelen]).where(artikelen.c.artikelID == int(martikelnr))
    rp = conn.execute(s).first()
    if len(martikelnr) == 9 and _11check(martikelnr) and rp:
        martikelnr = int(martikelnr)
    else:
        foutArtnr()
        zoekArtikel(m_email)
    wijzArt(m_email, martikelnr)
        
        
def wijzArt(m_email, martikelnr):
    logger.warning(">>> Entering wijzArt(m_email=%s,martikelnr=%s)", m_email, martikelnr, extra={"event.action": "wijzArt", "logrite.martikelnr": martikelnr})
    metadata = MetaData()
    logger.debug("wijzArt(m_email=%s,martikelnr=%s): metadata → %s", m_email, martikelnr, metadata, extra={"event.action": "wijzArt", "logrite.martikelnr": martikelnr})
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
        Column('afmeting', String))

    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("wijzArt(m_email=%s,martikelnr=%s): engine → %s", m_email, martikelnr, engine, extra={"event.action": "wijzArt", "logrite.martikelnr": martikelnr})
    conn = engine.connect()
    logger.debug("wijzArt(m_email=%s,martikelnr=%s): conn → %s", m_email, martikelnr, conn, extra={"event.action": "wijzArt", "logrite.martikelnr": martikelnr})
    sel = select([artikelen]).where(artikelen.c.artikelID == martikelnr)
    rpartikel = conn.execute(sel).first()
    logger.debug("wijzArt(m_email=%s,martikelnr=%s): sel → %s", m_email, martikelnr, sel, extra={"event.action": "wijzArt", "logrite.martikelnr": martikelnr})
    logger.debug("wijzArt(m_email=%s,martikelnr=%s): rpartikel → %s", m_email, martikelnr, rpartikel, extra={"event.action": "wijzArt", "logrite.martikelnr": martikelnr})
    conn.close()
                
    class Widget(QDialog):
        logger.debug("<<< Exiting wijzArt(m_email=%s,martikelnr=%s)", m_email, martikelnr, extra={"event.action": "wijzArt", "logrite.martikelnr": martikelnr})
        def __init__(self):
            super(Widget, self).__init__()
        
            self.setWindowTitle("Artikelen wijzigen")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
                        
            self.setFont(QFont('Arial', 10))
                       
            self.Artikelnummer = QLabel()
            q1Edit = QLineEdit(str(rpartikel[0]))
            q1Edit.setFixedWidth(100)
            q1Edit.setDisabled(True)
            q1Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
            q1Edit.textChanged.connect(self.q1Changed)
        
            self.Artikelomschrijving = QLabel()
            q2Edit = QLineEdit(str(rpartikel[1]))
            q2Edit.setFixedWidth(400)
            q2Edit.setFont(QFont("Arial",10))
            q2Edit.textChanged.connect(self.q2Changed)
            
            self.Artikelprijs = QLabel()
            q3Edit = QLineEdit(str(rpartikel[2]))
            q3Edit.setFixedWidth(100)
            q3Edit.setFont(QFont("Arial",10))
            q3Edit.setAlignment(Qt.AlignRight)
            q3Edit.textChanged.connect(self.q3Changed)
            reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q3Edit)
            q3Edit.setValidator(input_validator)
                           
            self.Artikelvoorraad = QLabel()
            q4Edit = QLineEdit(str(round(rpartikel[3],2)))
            q4Edit.setFixedWidth(100)
            q4Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
            q4Edit.setDisabled(True)
            q4Edit.setAlignment(Qt.AlignRight)
            q4Edit.textChanged.connect(self.q4Changed)
            reg_ex = QRegExp("[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q4Edit)
            q4Edit.setValidator(input_validator)
            
            self.Artikeleenheid = QLabel()
            q5Edit = QComboBox()
            q5Edit.setFixedWidth(140)
            q5Edit.setFont(QFont("Arial",10))
            q5Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            q5Edit.addItem('stuk')
            q5Edit.addItem('100')
            q5Edit.addItem('meter')
            q5Edit.addItem('kg')
            q5Edit.addItem('liter')
            q5Edit.addItem('m²')
            q5Edit.addItem('m³')
            q5Edit.setCurrentIndex(q5Edit.findText(rpartikel[4]))
            q5Edit.activated[str].connect(self.q5Changed)        
                    
            self.Minimumvoorraad = QLabel()
            q6Edit = QLineEdit(str(round(rpartikel[5],2)))
            q6Edit.setFixedWidth(100)
            q6Edit.setFont(QFont("Arial",10))
            q6Edit.setAlignment(Qt.AlignRight)
            q6Edit.textChanged.connect(self.q6Changed)
            reg_ex = QRegExp("^[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q6Edit)
            q6Edit.setValidator(input_validator)
          
            self.Bestelgrootte = QLabel()
            q7Edit = QLineEdit(str(round(rpartikel[6],2)))
            q7Edit.setFixedWidth(100)
            q7Edit.setFont(QFont("Arial",10))
            q7Edit.setAlignment(Qt.AlignRight)
            q7Edit.textChanged.connect(self.q7Changed)
            reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q7Edit)
            q7Edit.setValidator(input_validator)
                         
            self.Magazijnlocatie = QLabel()
            q8Edit = QLineEdit(str(rpartikel[7]))
            q8Edit.setFixedWidth(100)
            q8Edit.setFont(QFont("Arial",10))
            q8Edit.textChanged.connect(self.q8Changed)
            
            self.Artikelgroep = QLabel()
            q9Edit = QLineEdit(str(rpartikel[8]))
            q9Edit.setFixedWidth(200)
            q9Edit.setFont(QFont("Arial",10))
            q9Edit.textChanged.connect(self.q9Changed)
            
            self.Barcode = QLabel()
            q10Edit = QLineEdit(str(rpartikel[9]))
            q10Edit.setFixedWidth(130)
            q10Edit.setFont(QFont("Arial",10))
            q10Edit.textChanged.connect(self.q10Changed)
            reg_ex = QRegExp('^[1-9]{1,13}$')
            input_validator = QRegExpValidator(reg_ex, q10Edit)
            q10Edit.setValidator(input_validator)
        
            self.Artikelthumbnail = QLabel()
            q11Edit = QLineEdit(str(rpartikel[10]))
            q11Edit.setFixedWidth(400)
            q11Edit.setFont(QFont("Arial",10))
            q11Edit.textChanged.connect(self.q11Changed)
                    
            self.Artikelfoto = QLabel()
            q12Edit = QLineEdit(str(rpartikel[11]))
            q12Edit.setFixedWidth(400)
            q12Edit.setFont(QFont("Arial",10))
            q12Edit.textChanged.connect(self.q12Changed)
         
            self.Categorie = QLabel()
            q13Edit = QComboBox()
            q13Edit.setFixedWidth(320)
            q13Edit.setFont(QFont("Arial",10))
            q13Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
            q13Edit.addItem('1. Voorraadgestuurd < 3 weken.')
            q13Edit.addItem('2. Voorraadgestuurd < 12 weken')
            q13Edit.addItem('3. Voorraadgestuurd < 26 weken')
            q13Edit.addItem('4. Voorraadgestuurd < 52 weken')
            q13Edit.addItem('5. Reservering < 3 weken')
            q13Edit.addItem('6. Reservering < 6 weken')
            q13Edit.addItem('7. Reservering < 12 weken')
            q13Edit.addItem('8. Reservering < 24 weken')
            q13Edit.addItem('9. Reservering < 52 weken')            
            q13Edit.setCurrentIndex(rpartikel[12]-1)
            q13Edit.activated[str].connect(self.q13Changed)        
                    
            grid = QGridLayout()
            grid.setSpacing(20)
        
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 0, 0)
        
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 2, 1, 1, Qt.AlignRight) 
        
            self.setFont(QFont('Arial', 10))
            grid.addWidget(QLabel('Wijzigen artikel'), 1, 1)
        
            grid.addWidget(QLabel('                                *'), 2, 0)
            grid.addWidget(QLabel('Verplichte velden'), 2, 1)
        
            grid.addWidget(QLabel('Artikelnummer'), 3, 0)
            grid.addWidget(q1Edit, 3, 1)
        
            grid.addWidget(QLabel('Artikelomschrijving     *'), 4, 0)
            grid.addWidget(q2Edit, 4, 1)
        
            grid.addWidget(QLabel('Artikelprijs                 *'), 5, 0)
            grid.addWidget(q3Edit, 5 , 1) 
        
            grid.addWidget(QLabel('Artikelvoorraad'), 6, 0)
            grid.addWidget(q4Edit, 6, 1)
          
            grid.addWidget(QLabel('Eenheid                    *'), 7, 0)
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
            
            grid.addWidget(QLabel('Categorie                   *'),15,0)
            grid.addWidget(q13Edit, 15, 1)
        
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 16, 1)
                
            applyBtn = QPushButton('Wijzigen')
            applyBtn.clicked.connect(self.accept)
        
            grid.addWidget(applyBtn, 15, 2)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Sluiten')
            cancelBtn.clicked.connect(lambda: wijzSluit(self, m_email))
        
            grid.addWidget(cancelBtn, 14, 2)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
                                          
            self.setLayout(grid)
            self.setGeometry(500, 100, 350, 300)
        
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
            dialog = Widget()
            dialog.exec_()
            return [dialog.returnArtikelnummer(),dialog.returnArtikelomschrijving(),\
                    dialog.returnArtikelprijs(), dialog.returnArtikelvoorraad(),\
                    dialog.returnArtikeleenheid(), dialog.returnMinimumvoorraad(),\
                    dialog.returnBestelgrootte(), dialog.returnMagazijnlocatie(),\
                    dialog.returnArtikelgroep(), dialog.returnBarcode(),\
                    dialog.returnArtikelthumbnail(),dialog.returnArtikelfoto(),\
                    dialog.returnCategorie()]
            
    window = Widget()
    data = window.getData()
    if data[1]:
        martomschr = data[1]
    else:
        martomschr = rpartikel[1]
    if data[2]:
        martprijs = str(data[2])
    else:
        martprijs = str(rpartikel[2])
    if data[3]:
        martvrd = str(data[3])
    else:
        martvrd = str(rpartikel[3])
    if data[4]:
        marteenh = data[4]
    else:
        marteenh = rpartikel[4]
    if data[5]:
        martminvrd = str(data[5])
    else:
        martminvrd = str(rpartikel[5])
    if data[6]:
        martbestgr = str(data[6])
    else:
        martbestgr = str(rpartikel[6])
    if data[7]:
        mlocmag = data[7]
    else:
        mlocmag = rpartikel[7]
    if data[8]:
        martgr = data[8]
    else:
        martgr = rpartikel[8]
    if data[9]:
        mbarc = int(data[9])
    else:
        mbarc = int(rpartikel[9])
    if data[10]:
        mthumb = data[10]
    else:
        mthumb = rpartikel[10]                             
    if data[11]:
        mfotoart = data[11]
    else:
        mfotoart = rpartikel[11]
    if data[12]:
        mcat = str(data[12])[0]
    else:
        mcat = str(rpartikel[12])
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    conn = engine.connect()    
        
    u = update(artikelen).where(artikelen.c.artikelID == martikelnr).\
    values(artikelomschrijving = martomschr, artikelprijs = martprijs,\
    art_voorraad = martvrd, art_eenheid = marteenh, art_min_voorraad = \
    martminvrd, art_bestelgrootte = martbestgr, locatie_magazijn = mlocmag,\
    artikelgroep = martgr, barcode = mbarc, thumb_artikel = mthumb,\
    foto_artikel = mfotoart, categorie = mcat)  
    conn.execute(u)
    conn.close()
    updateOK()
    zoekArtikel(m_email)