from login import hoofdMenu
import datetime
from PyQt5.QtWidgets import QLabel, QLineEdit, QGridLayout, QPushButton,\
                QDialog, QMessageBox ,QComboBox 
from PyQt5.QtGui import QRegExpValidator, QFont, QPixmap, QIcon
from PyQt5.QtCore import Qt, QRegExp
from sqlalchemy import (Table, Column, Integer, String, Float, ForeignKey, \
                        MetaData, create_engine, func)
from sqlalchemy.sql import select, insert, and_
import logging
logger = logging.getLogger(__name__)

def invoerGelukt():
    logger.debug(">>> Entering invoerGelukt()")
    msg = QMessageBox()
    logger.debug("invoerGelukt(): msg → %s", msg)
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))        
    msg.setIcon(QMessageBox.Information)
    msg.setText('Imvoer stelpost order gelukt!')
    msg.setWindowTitle('Inkoop order stelposten')
    logger.debug("<<< Exiting invoerGelukt()")
    msg.exec_()
    
def foutInvoer():
    logger.debug(">>> Entering foutInvoer()")
    msg = QMessageBox()
    logger.debug("foutInvoer(): msg → %s", msg)
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))        
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Foutieve invoer. Voer opnieuw in!')
    msg.setWindowTitle('Inkoop order stelposten')
    logger.debug("<<< Exiting foutInvoer()")
    msg.exec_() 
    
def invoerBestaat():
    logger.debug(">>> Entering invoerBestaat()")
    msg = QMessageBox()
    logger.debug("invoerBestaat(): msg → %s", msg)
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))        
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Deze stelpost is al verwerkt!')
    msg.setWindowTitle('Inkoop order stelposten')
    logger.debug("<<< Exiting invoerBestaat()")
    msg.exec_() 

def geenRegels():
    logger.debug(">>> Entering geenRegels()")
    msg = QMessageBox()
    logger.debug("geenRegels(): msg → %s", msg)
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))        
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Geen calculatie regels voor deze stelpost aanwezig!')
    msg.setWindowTitle('Inkoop order stelposten')
    logger.debug("<<< Exiting geenRegels()")
    msg.exec_()     
    
def sluitRegels(m_email, mlevnr, mwerknr, mregel, self):
    logger.debug(">>> Entering sluitRegels(m_email=%s,mlevnr=%s,mwerknr=%s,mregel=%s)", m_email, mlevnr, mwerknr, mregel)
    self.close()
    zoekLeverancier(m_email, mlevnr, mwerknr, mregel)
    logger.debug("<<< Exiting sluitRegels(m_email=%s,mlevnr=%s,mwerknr=%s,mregel=%s)", m_email, mlevnr, mwerknr, mregel)

def foutLeverancier():
    logger.debug(">>> Entering foutLeverancier()")
    msg = QMessageBox()
    logger.debug("foutLeverancier(): msg → %s", msg)
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))        
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Leverancier/Werknummer\nniet gevonden!')
    msg.setWindowTitle('Inkoop order stelposten')
    logger.debug("<<< Exiting foutLeverancier()")
    msg.exec_()
        
def windowSluit(self, m_email):
    logger.debug(">>> Entering windowSluit(m_email=%s)", m_email)
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email)
                 
def _11check(mlevnr):
    logger.debug(">>> Entering _11check(mlevnr=%s)", mlevnr)
    number = str(mlevnr)
    logger.debug("_11check(mlevnr=%s): number → %s", mlevnr, number)
    total = 0       
    fullnumber = number                       
    logger.debug("_11check(mlevnr=%s): total → %s", mlevnr, total)
    for i in range(8):
        total += int(fullnumber[i])*(9-i)
        logger.debug("_11check(mlevnr=%s): fullnumber → %s", mlevnr, fullnumber)
        checkdigit = total % 11 % 10
    if checkdigit == int(fullnumber[8]):
        return True
    else:
        logger.debug("<<< Exiting _11check(mlevnr=%s)", mlevnr)
        return False
 
def maak11proef(basisnr):
   logger.debug(">>> Entering maak11proef(basisnr=%s)", basisnr)
   basisnr = str(basisnr)
   basisnr = str((int(basisnr[0:8]))+int(1))
   logger.debug("maak11proef(basisnr=%s): basisnr → %s", basisnr, basisnr)
   total = 0                       
   logger.debug("maak11proef(basisnr=%s): total → %s", basisnr, total)
   for i in range(int(8)):
       total += int(basisnr[i])*(int(9)-i)
   checkdigit = total % 11 % 10
   logger.debug("maak11proef(basisnr=%s): checkdigit → %s", basisnr, checkdigit)
   basisuitnr = basisnr+str(checkdigit)
   logger.debug("maak11proef(basisnr=%s): basisuitnr → %s", basisnr, basisuitnr)
   logger.debug("<<< Exiting maak11proef(basisnr=%s)", basisnr)
   logger.debug("zoekLeverancier(m_email=%s,mlevnr=%s,mwerknr=%s,mregel=%s): leveranciers → %s", m_email, mlevnr, mwerknr, mregel, leveranciers)
   logger.debug("zoekLeverancier(m_email=%s,mlevnr=%s,mwerknr=%s,mregel=%s): werken → %s", m_email, mlevnr, mwerknr, mregel, werken)
   logger.debug("zoekLeverancier(m_email=%s,mlevnr=%s,mwerknr=%s,mregel=%s): engine → %s", m_email, mlevnr, mwerknr, mregel, engine)
   return basisuitnr

def zoekLeverancier(m_email, mlevnr, mwerknr, mregel):
    logger.debug(">>> Entering zoekLeverancier(m_email=%s,mlevnr=%s,mwerknr=%s,mregel=%s)", m_email, mlevnr, mwerknr, mregel)
    metadata = MetaData()
    logger.debug("zoekLeverancier(m_email=%s,mlevnr=%s,mwerknr=%s,mregel=%s): metadata → %s", m_email, mlevnr, mwerknr, mregel, metadata)
    leveranciers = Table('leveranciers', metadata,
        Column('leverancierID', Integer(), primary_key=True),
        Column('bedrijfsnaam', String),
        Column('rechtsvorm', String),
        Column('postcode', String),
        Column('huisnummer', String),
        Column('toevoeging', String))
    werken = Table('werken', metadata,
        Column('werknummerID', Integer, primary_key=True))
            
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    conn = engine.connect()

    logger.debug("zoekLeverancier(m_email=%s,mlevnr=%s,mwerknr=%s,mregel=%s): conn → %s", m_email, mlevnr, mwerknr, mregel, conn)
    class Widget(QDialog):
        logger.debug("<<< Exiting zoekLeverancier(m_email=%s,mlevnr=%s,mwerknr=%s,mregel=%s)", m_email, mlevnr, mwerknr, mregel)
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle("Invoer inkooporders stelposten")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
                            
            self.Leveranciernummer = QLabel()
            levEdit = QLineEdit(str(mlevnr))
            levEdit.setFixedWidth(100)
            levEdit.setFont(QFont("Arial",10))
            levEdit.textChanged.connect(self.levChanged)
            reg_ex = QRegExp('^[3]{1}[0-9]{8}$')
            input_validator = QRegExpValidator(reg_ex, levEdit)
            levEdit.setValidator(input_validator)
                            
            self.Werknummer = QLabel()
            werknEdit = QLineEdit(str(mwerknr))
            werknEdit.setFixedWidth(100)
            werknEdit.setFont(QFont("Arial",10))
            werknEdit.textChanged.connect(self.werknChanged)
            reg_ex = QRegExp('^[8]{1}[0-9]{8}$')
            input_validator = QRegExpValidator(reg_ex, levEdit)
            werknEdit.setValidator(input_validator)
            
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
            grid.addWidget(QLabel('Leverancier\nWerknummer\nStelposten'), 0, 1)
    
            grid.addWidget(QLabel('Leverancier'), 1, 0)
            grid.addWidget(levEdit, 1, 1)
            
            grid.addWidget(QLabel('Werknummer'), 2, 0)
            grid.addWidget(werknEdit, 2, 1)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved - dj.jansen@casema.nl'), 3, 0, 1 ,3, Qt.AlignCenter)
       
            cancelBtn = QPushButton('Sluiten')
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
         
            applyBtn = QPushButton('Zoeken')
            applyBtn.clicked.connect(self.accept)
                  
            grid.addWidget(applyBtn, 2, 2)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(120)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
        
            grid.addWidget(cancelBtn, 1, 2)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(120)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            self.setLayout(grid)
            self.setGeometry(600, 400, 150, 150)
            logger.debug(">>> Entering __init__(parent=%s)", parent)
            logger.debug("__init__(parent=%s): inkorderEdit → %s", parent, inkorderEdit)
            logger.debug("__init__(parent=%s): self.Inkoopordernummer → %s", parent, self.Inkoopordernummer)
            logger.debug("__init__(self=%s,parent=%s): inkorderEdit → %s", self, parent, inkorderEdit)
            logger.debug("__init__(parent=%s): werknEdit → %s", parent, werknEdit)
            logger.debug("__init__(parent=%s): self.Werknummer → %s", parent, self.Werknummer)
            logger.debug("__init__(self=%s,parent=%s): werknEdit → %s", self, parent, werknEdit)
            logger.debug("__init__(parent=%s): k0Edit → %s", parent, k0Edit)
            logger.debug("__init__(parent=%s): self.Diensten → %s", parent, self.Diensten)
            logger.debug("__init__(self=%s,parent=%s): k0Edit → %s", self, parent, k0Edit)
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap)
            logger.debug("__init__(parent=%s): input_validator → %s", parent, input_validator)
            logger.debug("__init__(parent=%s): q1Edit → %s", parent, q1Edit)
            logger.debug("__init__(parent=%s): self.OrderregelPrijs → %s", parent, self.OrderregelPrijs)
            logger.debug("__init__(self=%s,parent=%s): q1Edit → %s", self, parent, q1Edit)
            logger.debug("__init__(parent=%s): reg_ex → %s", parent, reg_ex)
            logger.debug("__init__(self=%s,parent=%s): reg_ex → %s", self, parent, reg_ex)
            logger.debug("__init__(self=%s,parent=%s): input_validator → %s", self, parent, input_validator)
            logger.debug("__init__(parent=%s): q2Edit → %s", parent, q2Edit)
            logger.debug("__init__(parent=%s): self.Omschrijving → %s", parent, self.Omschrijving)
            logger.debug("__init__(self=%s,parent=%s): q2Edit → %s", self, parent, q2Edit)
            logger.debug("__init__(parent=%s): q3Edit → %s", parent, q3Edit)
            logger.debug("__init__(parent=%s): self.GeplandeStart → %s", parent, self.GeplandeStart)
            logger.debug("__init__(self=%s,parent=%s): q3Edit → %s", self, parent, q3Edit)
            logger.debug("__init__(parent=%s): q4Edit → %s", parent, q4Edit)
            logger.debug("__init__(parent=%s): self.GeplandGereed → %s", parent, self.GeplandGereed)
            logger.debug("__init__(self=%s,parent=%s): q4Edit → %s", self, parent, q4Edit)
            logger.debug("__init__(parent=%s): grid → %s", parent, grid)
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid)
            logger.debug("__init__(parent=%s): lbl → %s", parent, lbl)
            logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl)
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap)
            logger.debug("__init__(parent=%s): lbl1 → %s", parent, lbl1)
            logger.debug("__init__(self=%s,parent=%s): lbl1 → %s", self, parent, lbl1)
            logger.debug("__init__(parent=%s): lbl8 → %s", parent, lbl8)
            logger.debug("__init__(self=%s,parent=%s): lbl8 → %s", self, parent, lbl8)
            logger.debug("__init__(parent=%s): lbl4 → %s", parent, lbl4)
            logger.debug("__init__(self=%s,parent=%s): lbl4 → %s", self, parent, lbl4)
            logger.debug("__init__(parent=%s): lbl5 → %s", parent, lbl5)
            logger.debug("__init__(self=%s,parent=%s): lbl5 → %s", self, parent, lbl5)
            logger.debug("__init__(parent=%s): lbl6 → %s", parent, lbl6)
            logger.debug("__init__(self=%s,parent=%s): lbl6 → %s", self, parent, lbl6)
            logger.debug("__init__(parent=%s): lbl7 → %s", parent, lbl7)
            logger.debug("__init__(self=%s,parent=%s): lbl7 → %s", self, parent, lbl7)
            logger.debug("__init__(parent=%s): logo → %s", parent, logo)
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo)
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn)
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn)
            logger.debug("__init__(parent=%s): sluitBtn → %s", parent, sluitBtn)
            logger.debug("__init__(self=%s,parent=%s): sluitBtn → %s", self, parent, sluitBtn)
            logger.debug("<<< Exiting __init__(parent=%s)", parent)
    
        def levChanged(self, text):
            logger.debug(">>> Entering levChanged(text=%s)", text)
            logger.debug("levChanged(self=%s,text=%s): Leveranciernummer → %s", self, text, Leveranciernummer)
            self.Leveranciernummer.setText(text)
            logger.debug("<<< Exiting levChanged(text=%s)", text)
            
        def werknChanged(self, text):
            self.Werknummer.setText(text)
            logger.debug(">>> Entering werknChanged(text=%s)", text)
            logger.debug("<<< Exiting werknChanged(text=%s)", text)
    
        def returnLeveranciernummer(self):
            logger.debug(">>> Entering returnLeveranciernummer()")
            logger.debug("<<< Exiting returnLeveranciernummer()")
            return self.Leveranciernummer.text()
        
        def returnWerknummer(self):
            return self.Werknummer.text()
    
        logger.debug(">>> Entering returnWerknummer()")
        logger.debug("<<< Exiting returnWerknummer()")
        @staticmethod
        def getData(parent=None):
            dialog = Widget(parent)
            dialog.exec_()
            logger.debug(">>> Entering getData(parent=%s)", parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog)
            logger.debug("<<< Exiting getData(parent=%s)", parent)
            return [dialog.returnLeveranciernummer(), dialog.returnWerknummer()]
       
    window = Widget()
    data = window.getData()
    if data[0] and data[1] and len(data[0]) == 9 and len(data[1]) == 9\
           and _11check(data[0]) and  _11check(data[1]):
        mlevnr = int(data[0])
        mwerknr = int(data[1])
    sel = select([leveranciers, werken]).where(and_(leveranciers.c.leverancierID\
                == mlevnr, werken.c.werknummerID == mwerknr))
    rplev = conn.execute(sel).first()
    mregel = 1
    if rplev:
        inkoopRegels(m_email, rplev, mregel)
    else:
        foutLeverancier()
        zoekLeverancier(m_email, mlevnr, mwerknr , mregel)
            
def bepaalInkoopOrdernr(mregel):
    logger.debug(">>> Entering bepaalInkoopOrdernr(mregel=%s)", mregel)
    metadata = MetaData()
    logger.debug("bepaalInkoopOrdernr(mregel=%s): metadata → %s", mregel, metadata)
    orders_inkoop = Table('orders_inkoop', metadata,
        Column('orderinkoopID', Integer, primary_key=True),
        Column('leverancierID', None, ForeignKey('leveranciers.c.leverancierID')))
    
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("bepaalInkoopOrdernr(mregel=%s): engine → %s", mregel, engine)
    conn = engine.connect()
    
    logger.debug("bepaalInkoopOrdernr(mregel=%s): conn → %s", mregel, conn)
    morderinkoopnr=(conn.execute(select([func.max(orders_inkoop.c.orderinkoopID, type_=Integer)\
                                   .label('morderinkoopnr')])).scalar())
    if mregel == 1:
       morderinkoopnr=int(maak11proef(morderinkoopnr))
       logger.debug("bepaalInkoopOrdernr(mregel=%s): morderinkoopnr → %s", mregel, morderinkoopnr)
    logger.debug("<<< Exiting bepaalInkoopOrdernr(mregel=%s)", mregel)
    return(morderinkoopnr)
   
def Inkooporder(m_email, rplev, mregel):
    logger.debug(">>> Entering Inkooporder(m_email=%s,rplev=%s,mregel=%s)", m_email, rplev, mregel)
    mlevnr = int(rplev[0])
    logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mlevnr → %s", m_email, rplev, mregel, mlevnr)
    mwerknr = int(rplev[6])
    mbedrnaam = rplev[1]
    logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mwerknr → %s", m_email, rplev, mregel, mwerknr)
    mrechtsvorm = rplev[2]
    mpostcode = rplev[3]
    logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mbedrnaam → %s", m_email, rplev, mregel, mbedrnaam)
    logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mrechtsvorm → %s", m_email, rplev, mregel, mrechtsvorm)
    logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mpostcode → %s", m_email, rplev, mregel, mpostcode)
    mhuisnr = int(rplev[4])
    logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mhuisnr → %s", m_email, rplev, mregel, mhuisnr)
    if rplev[5]:
        mtoev = rplev[5]
    else:
        mtoev=''
        logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mtoev → %s", m_email, rplev, mregel, mtoev)
    import postcode
    mstrplts = postcode.checkpostcode(mpostcode, mhuisnr)
    mstraat = mstrplts[0]
    mplaats = mstrplts[1]
    logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mstrplts → %s", m_email, rplev, mregel, mstrplts)
    logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mplaats → %s", m_email, rplev, mregel, mplaats)
    minkordnr = bepaalInkoopOrdernr(mregel)
    logger.debug("Inkooporder(m_email=%s,rplev=%s,mregel=%s): mstraat → %s", m_email, rplev, mregel, mstraat)
    logger.debug("<<< Exiting Inkooporder(m_email=%s,rplev=%s,mregel=%s)", m_email, rplev, mregel)
    return(minkordnr, mlevnr, mbedrnaam, mrechtsvorm, mstraat, mhuisnr,\
               mtoev, mpostcode, mplaats, mwerknr)
      
def inkoopRegels(m_email, rplev, mregel):
    logger.debug(">>> Entering inkoopRegels(m_email=%s,rplev=%s,mregel=%s)", m_email, rplev, mregel)
    minkgeg = Inkooporder(m_email, rplev, mregel)
    logger.debug("inkoopRegels(m_email=%s,rplev=%s,mregel=%s): minkgeg → %s", m_email, rplev, mregel, minkgeg)
    minkordnr = minkgeg[0]
    mlevnr = minkgeg[1]
    logger.debug("inkoopRegels(m_email=%s,rplev=%s,mregel=%s): minkordnr → %s", m_email, rplev, mregel, minkordnr)
    logger.debug("inkoopRegels(m_email=%s,rplev=%s,mregel=%s): mlevnr → %s", m_email, rplev, mregel, mlevnr)
    mwerknr = minkgeg[9]
    logger.debug("inkoopRegels(m_email=%s,rplev=%s,mregel=%s): mwerknr → %s", m_email, rplev, mregel, mwerknr)
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.debug("<<< Exiting inkoopRegels(m_email=%s,rplev=%s,mregel=%s)", m_email, rplev, mregel)
            self.setWindowTitle("Invoer inkooporder stelposten werk")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
                       
            self.Inkoopordernummer = QLabel()
            inkorderEdit = QLineEdit(str(minkordnr))
            inkorderEdit.setDisabled(True)
            inkorderEdit.setAlignment(Qt.AlignRight)
            inkorderEdit.setFixedWidth(100)
            inkorderEdit.setFont(QFont("Arial",10))
            inkorderEdit.textChanged.connect(self.inkorderChanged) 
        
            self.Werknummer = QLabel()
            werknEdit = QLineEdit(str(mwerknr))
            werknEdit.setFixedWidth(100)
            werknEdit.setAlignment(Qt.AlignRight)
            werknEdit.setDisabled(True)
            werknEdit.setFont(QFont("Arial",10))
            werknEdit.textChanged.connect(self.werknChanged)
                            
            self.Diensten= QLabel()
            k0Edit = QComboBox()
            k0Edit.setFixedWidth(300)
            k0Edit.setFont(QFont("Arial",10))
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.addItem('          Provisional items work')
            k0Edit.addItem('1. Inhuur')
            k0Edit.addItem('2. Leiding')
            k0Edit.addItem('3. Huisvesting')
            k0Edit.addItem('5. Grondverzet')
            k0Edit.addItem('7. Transport')
            k0Edit.addItem('8. Overig')
            k0Edit.activated[str].connect(self.k0Changed)
            
            self.OrderregelPrijs = QLabel()
            q1Edit = QLineEdit()
            q1Edit.setFixedWidth(130)
            q1Edit.setFont(QFont("Arial",10))
            q1Edit.textChanged.connect(self.q1Changed) 
            q1Edit.setDisabled(True)
            reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q1Edit)
            q1Edit.setValidator(input_validator)
             
            self.Omschrijving = QLabel()
            q2Edit = QLineEdit()
            q2Edit.setFixedWidth(400)
            q2Edit.setFont(QFont("Arial",10))
            q2Edit.textChanged.connect(self.q2Changed) 
            reg_ex = QRegExp("^.{0,50}$")
            input_validator = QRegExpValidator(reg_ex,q2Edit)
            q2Edit.setValidator(input_validator)    
        
            self.GeplandeStart = QLabel()
            q3Edit = QLineEdit()
            q3Edit.setCursorPosition(0)
            q3Edit.setFixedWidth(130)
            q3Edit.setFont(QFont("Arial",10))
            q3Edit.textChanged.connect(self.q3Changed) 
            reg_ex = QRegExp('^[2]{1}[0]{1}[0-9]{2}[-]{1}[0-1]{1}[0-9]{1}[-]{1}[0-3]{1}[0-9]{1}$')
            input_validator = QRegExpValidator(reg_ex, q3Edit)
            q3Edit.setValidator(input_validator)  
            
            self.GeplandGereed = QLabel()
            q4Edit = QLineEdit()
            q4Edit.setCursorPosition(0)
            q4Edit.setFixedWidth(130)
            q4Edit.setFont(QFont("Arial",10))
            q4Edit.textChanged.connect(self.q4Changed) 
            reg_ex = QRegExp('^[2]{1}[0]{1}[0-9]{2}[-]{1}[0-1]{1}[0-9]{1}[-]{1}[0-3]{1}[0-9]{1}$')
            input_validator = QRegExpValidator(reg_ex, q4Edit)
            q4Edit.setValidator(input_validator)  
                        
            grid = QGridLayout()
            grid.setSpacing(20)
                          
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl ,1, 0)
            
            self.setFont(QFont('Arial', 10))
            grid.addWidget(QLabel('Order voor\nLeverancier: '+str(minkgeg[1])\
            +',\n'+minkgeg[2]+' '+minkgeg[3]+',\n'+minkgeg[4]+' '+str(minkgeg[5])\
            +minkgeg[6]+',\n'+minkgeg[7]+' '+minkgeg[8]+'.\nOrderregel '+str(mregel)), 1, 1, 1, 3)
                                             
            lbl1 = QLabel('Ordernummer')
            lbl1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl1, 5, 0)
            grid.addWidget(inkorderEdit, 5, 1)
            
            grid.addWidget(QLabel('Werknummer'), 6, 0, 1, 1, Qt.AlignRight)
            grid.addWidget(werknEdit, 6, 1)  
 
            lbl8 = QLabel('Type order     *')
            lbl8.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl8, 7, 0)
            grid.addWidget(k0Edit, 7, 1)
             
            '''
            lbl4 = QLabel('Aanneemsom')  
            lbl4.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl4, 8, 0)
            grid.addWidget(q1Edit, 8, 1)
            '''
            
            lbl5 = QLabel('Omschrijving *')
            lbl5.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl5, 9, 0)
            grid.addWidget(q2Edit, 9, 1, 1 , 3)
            
            lbl6 = QLabel('Geplande start yyyy-mm-dd *')
            lbl6.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl6, 10, 0)
            grid.addWidget(q3Edit, 10, 1)
            
            lbl7 = QLabel('Gepland gereed yyyy-mm-dd*')
            lbl7.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl7, 11, 0)
            grid.addWidget(q4Edit, 11, 1)
            grid.addWidget(QLabel('* Verplichte invoer'), 11, 2, 1, 2)
                   
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved - dj.jansen@casema.nl'), 13, 0, 1, 4, Qt.AlignCenter)
         
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 1, 3, 1 , 1, Qt.AlignRight)
                       
            self.setLayout(grid)
            self.setGeometry(600, 150, 150, 150)
    
            applyBtn = QPushButton('Invoer')
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 12, 3, 1 , 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            sluitBtn = QPushButton('Sluiten')
            sluitBtn.clicked.connect(lambda: sluitRegels(m_email, mlevnr, mwerknr, mregel, self))
    
            grid.addWidget(sluitBtn, 12, 2)
            sluitBtn.setFont(QFont("Arial",10))
            sluitBtn.setFixedWidth(100)
            sluitBtn.setStyleSheet("color: black;  background-color: gainsboro")
                                                                                                        
        def inkorderChanged(self, text):
            logger.debug(">>> Entering inkorderChanged(text=%s)", text)
            logger.debug("inkorderChanged(self=%s,text=%s): Inkoopordernummer → %s", self, text, Inkoopordernummer)
            self.Inkoopordernummer.setText(text)
            logger.debug("<<< Exiting inkorderChanged(text=%s)", text)
            
        def werknChanged(self, text):
            logger.debug("werknChanged(self=%s,text=%s): Werknummer → %s", self, text, Werknummer)
            self.Werknummer.setText(text)
         
        def q1Changed(self,text):
            logger.debug(">>> Entering q1Changed(text=%s)", text)
            logger.debug("q1Changed(self=%s,text=%s): OrderregelPrijs → %s", self, text, OrderregelPrijs)
            self.OrderregelPrijs.setText(text)
            logger.debug("<<< Exiting q1Changed(text=%s)", text)
            
        def q2Changed(self,text):
            logger.debug(">>> Entering q2Changed(text=%s)", text)
            logger.debug("q2Changed(self=%s,text=%s): Omschrijving → %s", self, text, Omschrijving)
            self.Omschrijving.setText(text)
            logger.debug("<<< Exiting q2Changed(text=%s)", text)
        
        def q3Changed(self,text):
            logger.debug(">>> Entering q3Changed(text=%s)", text)
            logger.debug("q3Changed(self=%s,text=%s): GeplandeStart → %s", self, text, GeplandeStart)
            self.GeplandeStart.setText(text)
            logger.debug("<<< Exiting q3Changed(text=%s)", text)
            
        def q4Changed(self,text):
            logger.debug(">>> Entering q4Changed(text=%s)", text)
            logger.debug("q4Changed(self=%s,text=%s): GeplandGereed → %s", self, text, GeplandGereed)
            self.GeplandGereed.setText(text)
            logger.debug("<<< Exiting q4Changed(text=%s)", text)
                  
        def k0Changed(self,text):
            logger.debug(">>> Entering k0Changed(text=%s)", text)
            logger.debug("k0Changed(self=%s,text=%s): Diensten → %s", self, text, Diensten)
            self.Diensten.setText(text)  
            logger.debug("<<< Exiting k0Changed(text=%s)", text)
                       
        def returninkorder(self):
            logger.debug(">>> Entering returninkorder()")
            logger.debug("<<< Exiting returninkorder()")
            return self.Inkoopordernummer.text()
        
        def returnWerknummer(self):
            logger.debug(">>> Entering returnWerknummer()")
            return self.Werknummer.text()    
                 
        def returnq1(self):
            logger.debug(">>> Entering returnq1()")
            logger.debug("<<< Exiting returnq1()")
            return self.Omschrijving.text()
        
        def returnq2(self):
            logger.debug(">>> Entering returnq2()")
            logger.debug("<<< Exiting returnq2()")
            return self.OrderregelPrijs.text()
        
        def returnq3(self):
            logger.debug(">>> Entering returnq3()")
            logger.debug("<<< Exiting returnq3()")
            return self.GeplandeStart.text()
        
        def returnq4(self):
            logger.debug(">>> Entering returnq4()")
            logger.debug("<<< Exiting returnq4()")
            return self.GeplandGereed.text()
                      
        def returnk0(self):
            logger.debug(">>> Entering returnk0()")
            logger.debug("<<< Exiting returnk0()")
            return self.Diensten.text() 
       
        @staticmethod
        def getData(parent=None):
            dialog = Widget(parent)
            dialog.exec_()
            return [dialog.returnk0(), dialog.returnq1(),\
                    dialog.returnq2(), dialog.returnq3(), dialog.returnq4()]  
   
    window = Widget()
    data = window.getData()
         
    if data[0] and data[1] and data[3] and data[4]:
        soort = data[0]
        momschr = data[1]
        geplstart = data[3]
        geplgereed = data[4]
    else:
        foutInvoer()
        inkoopRegels(m_email, rplev, mregel)
          
    metadata = MetaData()
    orders_inkoop_diensten = Table('orders_inkoop_diensten', metadata,
        Column('orddienstlevID', Integer(), primary_key=True),
        Column('orderinkoopID', None, ForeignKey('orders_inkoop.orderinkoopID')),
        Column('werknummerID', None, ForeignKey('werken.werknummerID')),
        Column('werkomschr', String),
        Column('omschrijving', String),
        Column('aanneemsom', Float),
        Column('plan_start', String),
        Column('werk_start', String),
        Column('plan_gereed', String),
        Column('werk_gereed', String),
        Column('acceptatie_gereed', Float),
        Column('acceptatie_datum', String),
        Column('regel', Integer))
    calculaties = Table('calculaties', metadata,
        Column('calcID', Integer(), primary_key=True), 
        Column('koppelnummer', Integer),
        Column('inhuur', Float),            
        Column('uren_inhuur', Float),
        Column('leiding', Float),
        Column('huisvesting', Float),
        Column('kabelwerk', Float),
        Column('grondverzet', Float),
        Column('betonwerk', Float),
        Column('vervoer', Float),
        Column('overig', Float),
        Column('verwerkt', Integer))
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    conn = engine.connect()

    selcal = select([calculaties]).where(calculaties.c.koppelnummer == mwerknr)
    seldienst = select([orders_inkoop_diensten]).where(and_(orders_inkoop_diensten.c.werknummerID == mwerknr,\
      orders_inkoop_diensten.c.werkomschr.like(soort+'%')))
    rpdienst = conn.execute(seldienst).first()
    rpcal = conn.execute(selcal)

    if mregel == 1 and data[0] and not rpdienst:
        datum = str(datetime.datetime.now())
        mbestdatum = (datum[0:4]+'-'+datum[8:10]+'-'+datum[5:7])
        metadata = MetaData()
        orders_inkoop = Table('orders_inkoop', metadata,
            Column('orderinkoopID', Integer(), primary_key=True),
            Column('leverancierID', None, ForeignKey('leveranciers.c.leverancierID')),
            Column('besteldatum', String),
            Column('status', Integer))
        engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
        conn = engine.connect()
        mbestdatum = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))[0:10]
        ins = insert(orders_inkoop).values(orderinkoopID = minkordnr, leverancierID =\
                    mlevnr, besteldatum = mbestdatum, status = 1)
        conn.execute(ins)

    flag = 0    
    if soort[0] == '1' and not rpdienst:
        minh_uren = 0
        minhuur = 0
        for row in rpcal:
            if row[2]:
                minh_uren += row[3]
                minhuur += row[2]
                flag = 1
        if flag:
            mdienstnr=(conn.execute(select([func.max(orders_inkoop_diensten.c.orddienstlevID,\
                type_=Integer).label('mdienstnr')])).scalar())
            mdienstnr += 1
            insrgl = insert(orders_inkoop_diensten).values(orddienstlevID = mdienstnr,\
                 orderinkoopID = minkordnr, werknummerID = mwerknr,\
                 werkomschr = soort+' '+str(round(minh_uren,2))+' uren', omschrijving = momschr,\
                 aanneemsom = minhuur, plan_start = geplstart, plan_gereed = geplgereed, regel = mregel)
            conn.execute(insrgl)
            mregel += 1
            invoerGelukt()
    elif soort[0] == '2' and not rpdienst: 
        mleiding = 0
        for row in rpcal:
            if row[4]:
                mleiding += row[4]
                flag = 1
        if flag:
            mdienstnr=(conn.execute(select([func.max(orders_inkoop_diensten.c.orddienstlevID,\
                type_=Integer).label('mdienstnr')])).scalar())
            mdienstnr += 1
            insrgl = insert(orders_inkoop_diensten).values(orddienstlevID = mdienstnr,\
                 orderinkoopID = minkordnr, werknummerID = mwerknr,\
                 werkomschr = soort, omschrijving = momschr, aanneemsom = mleiding,\
                 plan_start = geplstart, plan_gereed = geplgereed, regel = mregel)
            conn.execute(insrgl)
            mregel += 1
            invoerGelukt()
    elif soort[0] == '3' and not rpdienst:
        mhuisvesting = 0
        for row in rpcal:
            if row[5]:
                mhuisvesting += row[5]
                flag = 1
        if flag:
            mdienstnr=(conn.execute(select([func.max(orders_inkoop_diensten.c.orddienstlevID,\
                type_=Integer).label('mdienstnr')])).scalar())
            mdienstnr += 1
            insrgl = insert(orders_inkoop_diensten).values(orddienstlevID = mdienstnr,\
                 orderinkoopID = minkordnr, werknummerID = mwerknr,\
                 werkomschr = soort, omschrijving = momschr, aanneemsom = mhuisvesting,\
                 plan_start = geplstart, plan_gereed = geplgereed, regel = mregel)
            conn.execute(insrgl)
            mregel += 1
            invoerGelukt()
    elif soort[0] == '5' and not rpdienst:
        mgrondverzet = 0
        for row in rpcal:
            if row[7]:
                mgrondverzet += row[7]
                flag = 1
        if flag:
            mdienstnr=(conn.execute(select([func.max(orders_inkoop_diensten.c.orddienstlevID,\
                type_=Integer).label('mdienstnr')])).scalar())
            mdienstnr += 1
            insrgl = insert(orders_inkoop_diensten).values(orddienstlevID = mdienstnr,\
                 orderinkoopID = minkordnr, werknummerID = mwerknr,\
                 werkomschr = soort , omschrijving = momschr, aanneemsom = mgrondverzet,\
                 plan_start = geplstart, plan_gereed = geplgereed, regel = mregel)
            conn.execute(insrgl)
            mregel += 1
            invoerGelukt()
    elif soort[0] == '7' and not rpdienst:
        mvervoer = 0
        for row in rpcal:
            if row[9]:
                mvervoer += row[9]
                flag = 1
        if flag:
            mdienstnr=(conn.execute(select([func.max(orders_inkoop_diensten.c.orddienstlevID,\
                type_=Integer).label('mdienstnr')])).scalar())
            mdienstnr += 1
            insrgl = insert(orders_inkoop_diensten).values(orddienstlevID = mdienstnr,\
                 orderinkoopID = minkordnr, werknummerID = mwerknr,\
                 werkomschr = soort, omschrijving = momschr, aanneemsom = mvervoer,\
                 plan_start = geplstart, plan_gereed = geplgereed, regel = mregel)
            conn.execute(insrgl)
            mregel += 1
            invoerGelukt()
    elif soort[0] == '8' and not rpdienst:
        moverig = 0
        for row in rpcal:
            if row[10]:
                moverig += row[10]
                flag = 1
        if flag:
            mdienstnr=(conn.execute(select([func.max(orders_inkoop_diensten.c.orddienstlevID,\
                type_=Integer).label('mdienstnr')])).scalar())
            mdienstnr += 1
            insrgl = insert(orders_inkoop_diensten).values(orddienstlevID = mdienstnr,\
                 orderinkoopID = minkordnr, werknummerID = mwerknr,\
                 werkomschr = soort, omschrijving = momschr, aanneemsom = moverig,\
                 plan_start = geplstart, plan_gereed = geplgereed, regel = mregel)
            conn.execute(insrgl)
            mregel += 1
            invoerGelukt()
    elif rpdienst:
        invoerBestaat()
    if flag == 0 and not rpdienst:
        geenRegels()
    inkoopRegels(m_email, rplev, mregel)