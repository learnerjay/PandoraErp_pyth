from login import hoofdMenu
import os, datetime
from PyQt5.QtCore import Qt, QRegExp, QAbstractTableModel
from PyQt5.QtGui import QFont, QPixmap, QRegExpValidator, QIcon
from PyQt5.QtWidgets import QLabel, QPushButton,\
     QMessageBox, QLineEdit, QGridLayout, QDialog, QWidget,QTableView, QComboBox
from sqlalchemy import (Table, Column, Integer, String, Float, Boolean,\
                     MetaData, create_engine, CheckConstraint, ForeignKey)
from sqlalchemy.sql import select, update, insert, func, and_
from sqlalchemy.exc import IntegrityError
import logging
logger = logging.getLogger(__name__)

def refresh(keuze, zoekterm, m_email, route, self):
    logger.debug(">>> Entering refresh(keuze=%s,zoekterm=%s,m_email=%s,route=%s)", keuze, zoekterm, m_email, route)
    self.close()
    raapLijst(keuze, zoekterm, m_email, route)   
    logger.debug("<<< Exiting refresh(keuze=%s,zoekterm=%s,m_email=%s,route=%s)", keuze, zoekterm, m_email, route)

def windowSluit(self, m_email):
    logger.debug(">>> Entering windowSluit(m_email=%s)", m_email)
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email)
 
def ongInvoer():
    logger.debug(">>> Entering ongInvoer()")
    msg = QMessageBox()
    logger.debug("ongInvoer(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Foutieve invoer\nzoekterm opnieuw invoeren s.v.p.!')
    msg.setWindowTitle('Materialen uitgeven/ printen')               
    logger.debug("<<< Exiting ongInvoer()")
    msg.exec_() 
    
def geenRecord():
    logger.debug(">>> Entering geenRecord()")
    msg = QMessageBox()
    logger.debug("geenRecord(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Geen record gevonden\nmaak een andere selektie s.v.p.!')
    msg.setWindowTitle('Materialen uitgeven/ printen')               
    logger.debug("<<< Exiting geenRecord()")
    msg.exec_() 
 
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
    
def printing():
    logger.debug(">>> Entering printing()")
    msg = QMessageBox()
    logger.debug("printing(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Information)
    msg.setText('Ogenblik afdrukken wordt gestart!')
    msg.setWindowTitle('AFDRUKKEN')
    logger.debug("<<< Exiting printing()")
    msg.exec_()
    
def printGeg(filename):
    logger.debug(">>> Entering printGeg(filename=%s)", filename)
    from sys import platform
    msgBox=QMessageBox()
    logger.debug("printGeg(filename=%s): msgBox → %s", filename, msgBox)
    msgBox.setStyleSheet("color: black;  background-color: gainsboro")
    msgBox.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msgBox.setWindowTitle("Printen raaplijst")
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Wilt U de raaplijst uitprinten?")
    msgBox.setStandardButtons(QMessageBox.Yes)
    msgBox.addButton(QMessageBox.No)
    msgBox.setStyleSheet("color: black;  background-color: gainsboro")
    msgBox.setDefaultButton(QMessageBox.Yes)
    if(msgBox.exec_() == QMessageBox.Yes):
        if platform == 'win32':
            os.startfile(filename, "print")
        else:
            os.system("lpr "+filename)
        printing()
        logger.debug("<<< Exiting printGeg(filename=%s)", filename)
    
def foutWerknr():
    logger.debug(">>> Entering foutWerknr()")
    msg = QMessageBox()
    logger.debug("foutWerknr(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Critical)
    msg.setText('Werknummer niet gevonden\nWerknummer bestaat niet!')
    msg.setWindowTitle('Gegevens!')
    logger.debug("<<< Exiting foutWerknr()")
    msg.exec_()
        
def invoerOK():
    logger.debug(">>> Entering invoerOK()")
    msg = QMessageBox()
    logger.debug("invoerOK(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Information)
    msg.setText('Invoer gelukt!')
    msg.setWindowTitle('RAAPLIJST')
    logger.debug("<<< Exiting invoerOK()")
    msg.exec_()
    
def negVoorraad():
        logger.debug(">>> Entering negVoorraad()")
        msg = QMessageBox()
        logger.debug("negVoorraad(): msg → %s", msg)
        msg.setStyleSheet("color: black;  background-color: gainsboro")
        msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
        msg.setIcon(QMessageBox.Critical)
        msg.setText('Te weinig voorraad\nvoor de transactie!')
        msg.setWindowTitle('VOORRAAD ONVOLDOENDE')
        logger.debug("<<< Exiting negVoorraad()")
        msg.exec_()
        
def foutHoev():
        logger.debug(">>> Entering foutHoev()")
        msg = QMessageBox()
        logger.debug("foutHoev(): msg → %s", msg)
        msg.setStyleSheet("color: black;  background-color: gainsboro")
        msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
        msg.setIcon(QMessageBox.Warning)
        msg.setText('Geen wijzigingen\ndoorgevoerd!')
        msg.setWindowTitle('INVOERFOUT')
        logger.debug("<<< Exiting foutHoev()")
        msg.exec_()

def werkGereed():
    logger.debug(">>> Entering werkGereed()")
    msg = QMessageBox()
    logger.debug("werkGereed(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Werknummer is afgemeld,\nboekingen niet meer mogelijk!')
    msg.setWindowTitle('Gegevens!')
    logger.debug("<<< Exiting werkGereed()")
    msg.exec_()
          
def eindProgram():
    logger.debug(">>> Entering eindProgram()")
    msg = QMessageBox()
    logger.debug("eindProgram(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Information)
    msg.setText('Programma afgesloten.\nTot ziens!')
    msg.setWindowTitle('BESTELLINGEN')               
    logger.debug("<<< Exiting eindProgram()")
    msg.exec_() 
				            
def printRaaplijst(keuze, zoekterm, m_email, route):
    logger.debug(">>> Entering printRaaplijst(keuze=%s,zoekterm=%s,m_email=%s,route=%s)", keuze, zoekterm, m_email, route)
    import validZt
    metadata = MetaData()
    logger.debug("printRaaplijst(keuze=%s,zoekterm=%s,m_email=%s,route=%s): metadata → %s", keuze, zoekterm, m_email, route, metadata)
    raaplijst = Table('raaplijst', metadata,
        Column('lijstID', Integer,primary_key=True),
        Column('artikelID', Integer),
        Column('werkorder', Integer),
        Column('afroep', Float),
        Column('leverdatum', String),
        Column('geleverd', Float),
        Column('meerwerk', Boolean),
        Column('postcode', String),
        Column('huisnummer', Integer),
        Column('toevoeging', String),
        Column('alternatief', String),
        Column('boekdatum', String),
        Column('straat', String),
        Column('woonplaats', String))
    artikelen = Table('artikelen', metadata,
        Column('artikelID', Integer(), primary_key=True),
        Column('artikelomschrijving', String),
        Column('locatie_magazijn', String))
    
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("printRaaplijst(keuze=%s,zoekterm=%s,m_email=%s,route=%s): engine → %s", keuze, zoekterm, m_email, route, engine)
    con = engine.connect()
    logger.debug("printRaaplijst(keuze=%s,zoekterm=%s,m_email=%s,route=%s): con → %s", keuze, zoekterm, m_email, route, con)
    if route < 2:
        if keuze == 1:
            selrl = select([raaplijst, artikelen]).where(and_(raaplijst.c.geleverd < raaplijst.c.afroep,\
                 raaplijst.c.artikelID == artikelen.c.artikelID)).order_by(raaplijst.c.werkorder, raaplijst.c.leverdatum)
            kop1 = 'Raaplijst Alle Afroepen '
            logger.debug("printRaaplijst(keuze=%s,zoekterm=%s,m_email=%s,route=%s): kop1 → %s", keuze, zoekterm, m_email, route, kop1)
            tekst1 = ''
            logger.debug("printRaaplijst(keuze=%s,zoekterm=%s,m_email=%s,route=%s): tekst1 → %s", keuze, zoekterm, m_email, route, tekst1)
        elif keuze == 2:
            selrl = select([raaplijst, artikelen]).where(and_(raaplijst.c.werkorder < 800000000,\
              raaplijst.c.geleverd < raaplijst.c.afroep, raaplijst.c.artikelID ==\
              artikelen.c.artikelID)).order_by(raaplijst.c.leverdatum)
            kop1 = ''
            tekst1 = 'Raaplijst Werkorders '
        elif keuze == 3:
            selrl = select([raaplijst, artikelen]).where(and_(raaplijst.c.werkorder > 800000000,\
              raaplijst.c.geleverd < raaplijst.c.afroep, raaplijst.c.artikelID ==\
              artikelen.c.artikelID)).order_by(raaplijst.c.leverdatum)
            kop1 = ''
            tekst1 = 'Raaplijst Werknummers '
        elif keuze == 4 and validZt.zt(zoekterm, 15):
            selrl = select([raaplijst, artikelen]).where(and_(raaplijst.c.werkorder == int(zoekterm),\
              raaplijst.c.geleverd < raaplijst.c.afroep, raaplijst.c.artikelID ==\
              artikelen.c.artikelID)).order_by(raaplijst.c.leverdatum)
            kop1 = ''
            tekst1 = 'Raaplijst Ordernummer '
        elif keuze == 5 and validZt.zt(zoekterm, 2):
            selrl = select([raaplijst, artikelen]).where(and_(raaplijst.c.artikelID == int(zoekterm),\
              raaplijst.c.geleverd < raaplijst.c.afroep, raaplijst.c.artikelID ==\
              artikelen.c.artikelID)).order_by(raaplijst.c.leverdatum)
            kop1 = ''
            tekst1 = 'Raaplijst Artikelnummer '       
        elif keuze == 6 and validZt.zt(zoekterm, 10):
            selrl = select([raaplijst, artikelen]).where(and_(raaplijst.c.leverdatum.like(zoekterm+'%'),
                raaplijst.c.geleverd < raaplijst.c.afroep, raaplijst.c.artikelID ==\
                artikelen.c.artikelID)).order_by(raaplijst.c.leverdatum, raaplijst.c.werkorder)
            kop1 = ''
            tekst1 = 'Raaplijst Leverdatum '
        elif keuze == 7 and validZt.zt(zoekterm, 9):
            selrl = select([raaplijst, artikelen]).where(and_(raaplijst.c.postcode.ilike(zoekterm+'%'),\
                 raaplijst.c.geleverd < raaplijst.c.afroep, raaplijst.c.artikelID ==\
                 artikelen.c.artikelID)).order_by(raaplijst.c.leverdatum, raaplijst.c.werkorder)
            kop1 = ''
            tekst1 = 'Raaplijst Postcode '
        elif keuze == 8:
            selrl = select([raaplijst, artikelen]).where(and_(raaplijst.c.geleverd >= raaplijst.c.afroep,\
               raaplijst.c.afroep > 0, raaplijst.c.artikelID == artikelen.c.artikelID))\
               .order_by(raaplijst.c.werkorder, raaplijst.c.leverdatum)
            kop1 = 'Uitgeleverd ' 
            tekst1 = ''
        else:
            ongInvoer()
            kiesSelektie(route, m_email)
    elif route == 2:
        if keuze == 2:
            selrl = select([raaplijst, artikelen]).where(and_(raaplijst.c.werkorder < 800000000,\
              raaplijst.c.geleverd < raaplijst.c.afroep, raaplijst.c.artikelID ==\
              artikelen.c.artikelID)).order_by(raaplijst.c.leverdatum)
            kop1 = ''
            tekst1 = 'Raaplijst Werkorders '
        elif keuze == 4 and validZt.zt(zoekterm, 15):
            selrl = select([raaplijst, artikelen]).where(and_(raaplijst.c.werkorder < 800000000,\
              raaplijst.c.werkorder == int(zoekterm), raaplijst.c.geleverd < raaplijst.c.afroep,\
              raaplijst.c.artikelID == artikelen.c.artikelID)).order_by(raaplijst.c.leverdatum)
            kop1 = ''
            tekst1 = 'Raaplijst Werkorder '
        elif keuze == 5 and validZt.zt(zoekterm, 2):
            selrl = select([raaplijst, artikelen]).where(and_(raaplijst.c.werkorder < 800000000,\
              raaplijst.c.artikelID == int(zoekterm), raaplijst.c.geleverd < raaplijst.c.afroep,\
              raaplijst.c.artikelID == artikelen.c.artikelID)).order_by(raaplijst.c.leverdatum)
            kop1 = ''
            tekst1 = 'Raaplijst Artikelnummer '       
        elif keuze == 6 and validZt.zt(zoekterm, 10):
            selrl = select([raaplijst, artikelen]).where(and_(raaplijst.c.werkorder < 800000000,\
                raaplijst.c.leverdatum.like(zoekterm+'%'), raaplijst.c.geleverd < raaplijst.c.afroep,\
                raaplijst.c.artikelID == artikelen.c.artikelID)).order_by(raaplijst.c.leverdatum,\
                raaplijst.c.werkorder)
            kop1 = ''
            tekst1 = 'Raaplijst Leverdatum '
        elif keuze == 7 and validZt.zt(zoekterm, 9):
            selrl = select([raaplijst, artikelen]).where(and_(raaplijst.c.werkorder < 800000000,\
                 raaplijst.c.postcode.ilike(zoekterm+'%'),raaplijst.c.geleverd < raaplijst.c.afroep,\
                 raaplijst.c.artikelID == artikelen.c.artikelID)).order_by(raaplijst.c.leverdatum,\
                 raaplijst.c.werkorder)
            kop1 = ''
            tekst1 = 'Raaplijst Postcode '
        elif keuze == 8:
            selrl = select([raaplijst, artikelen]).where(and_(raaplijst.c.werkorder < 800000000,\
               raaplijst.c.geleverd >= raaplijst.c.afroep, raaplijst.c.afroep > 0,\
               raaplijst.c.artikelID == artikelen.c.artikelID)).order_by(raaplijst.c.werkorder,\
                raaplijst.c.leverdatum)
            kop1 = 'Uitgeleverd ' 
            tekst1 = ''
        else:
            ongInvoer()
            kiesSelektie(route, m_email)
    elif route == 3:
        if keuze == 3:
            selrl = select([raaplijst, artikelen]).where(and_(raaplijst.c.werkorder > 800000000,\
              raaplijst.c.geleverd < raaplijst.c.afroep, raaplijst.c.artikelID ==\
              artikelen.c.artikelID)).order_by(raaplijst.c.leverdatum)
            kop1 = ''
            tekst1 = 'Raaplijst Werknummers '
        elif keuze == 4 and validZt.zt(zoekterm, 15):
            selrl = select([raaplijst, artikelen]).where(and_(raaplijst.c.werkorder > 800000000,\
              raaplijst.c.werkorder == int(zoekterm), raaplijst.c.geleverd < raaplijst.c.afroep,\
              raaplijst.c.artikelID == artikelen.c.artikelID)).order_by(raaplijst.c.leverdatum)
            kop1 = ''
            tekst1 = 'Raaplijst Werknummer '
        elif keuze == 5 and validZt.zt(zoekterm, 2):
            selrl = select([raaplijst, artikelen]).where(and_(raaplijst.c.werkorder > 800000000,\
              raaplijst.c.artikelID == int(zoekterm), raaplijst.c.geleverd < raaplijst.c.afroep,\
              raaplijst.c.artikelID == artikelen.c.artikelID)).order_by(raaplijst.c.leverdatum)
            kop1 = ''
            tekst1 = 'Raaplijst Artikelnummer '       
        elif keuze == 6 and validZt.zt(zoekterm, 10):
            selrl = select([raaplijst, artikelen]).where(and_(raaplijst.c.werkorder > 800000000,\
                raaplijst.c.leverdatum.like(zoekterm+'%'), raaplijst.c.geleverd < raaplijst.c.afroep,\
                raaplijst.c.artikelID == artikelen.c.artikelID)).order_by(raaplijst.c.leverdatum,\
                raaplijst.c.werkorder)
            kop1 = ''
            tekst1 = 'Raaplijst Leverdatum '
        elif keuze ==7 and validZt.zt(zoekterm, 9):
            selrl = select([raaplijst, artikelen]).where(and_(raaplijst.c.werkorder > 800000000,\
                 raaplijst.c.postcode.ilike(zoekterm+'%'), raaplijst.c.geleverd < raaplijst.c.afroep,\
                 raaplijst.c.artikelID == artikelen.c.artikelID)).order_by(raaplijst.c.leverdatum,\
                 raaplijst.c.werkorder)
            kop1 = ''
            tekst1 = 'Raaplijst Postcode '
        elif keuze == 8:
            selrl = select([raaplijst, artikelen]).where(and_(raaplijst.c.werkorder > 800000000,\
                raaplijst.c.geleverd >= raaplijst.c.afroep, raaplijst.c.afroep > 0,\
                raaplijst.c.artikelID == artikelen.c.artikelID)).order_by(raaplijst.c.werkorder,\
                raaplijst.c.leverdatum)
            kop1 = 'Uitgeleverd ' 
            tekst1 = ''
        else:
            ongInvoer()
            kiesSelektie(route, m_email)
    
    if con.execute(selrl).fetchone():
       rprl = con.execute(selrl)
    else:
       geenRecord()
       kiesSelektie(route, m_email)
       logger.debug("printRaaplijst(keuze=%s,zoekterm=%s,m_email=%s,route=%s): rprl → %s", keuze, zoekterm, m_email, route, rprl)
    
    mblad = 1
    logger.debug("printRaaplijst(keuze=%s,zoekterm=%s,m_email=%s,route=%s): mblad → %s", keuze, zoekterm, m_email, route, mblad)
    rgl = 0

    for row in rprl:
        from sys import platform
        if rgl == 0 or rgl%57 == 0:
            kop4=\
    (tekst1+str(kop1)+' Datum: '+str(datetime.datetime.now())[0:10]+'  Blad :  '+str(mblad)+' '+
     'Afleveradres '+row[12]+' '+str(row[8])+row[9]+', '+row[7]+' '+row[13]+'.\n'+
    '=============================================================================================\n'+
    'Artikelnr  Omschrijving                       Afroep Geleverd Leverdatum Werkorder  Locatie  \n'+
    '=============================================================================================\n')
            kop5=\
    (tekst1+str(kop1)+' Datum: '+str(datetime.datetime.now())[0:10]+'  Blad :  '+str(mblad)+'\n'+
    '=============================================================================================\n'+
    'Artikelnr  Omschrijving                       Afroep Geleverd Leverdatum Werkorder  Locatie  \n'+
    '=============================================================================================\n')
  
            if keuze == 2:
                kop1 = row[2]
                kop = kop5
                logger.debug("printRaaplijst(keuze=%s,zoekterm=%s,m_email=%s,route=%s): kop → %s", keuze, zoekterm, m_email, route, kop)
            elif keuze == 3:
                kop1 = row[2]
                kop = kop5
            elif keuze == 4:
                kop1 = row[2]
                kop = kop4
            elif keuze == 5:
                kop1 = row[1]
                kop = kop5
            elif keuze == 6:
                kop1 = row[4]
                kop = kop5
            elif keuze == 7:
                kop1 = row[7]
                kop = kop4
            else:
                kop = kop5
            if platform == 'win32':
                filename = '.\\forms\\Raaplijsten\\raaplijst-'+str(kop1)+'-'+str(datetime.datetime.now())[0:10]+'.txt'
            else:
                filename = './forms/Raaplijsten/raaplijst-'+str(kop1)+'-'+str(datetime.datetime.now())[0:10]+'.txt'
                logger.debug("printRaaplijst(keuze=%s,zoekterm=%s,m_email=%s,route=%s): filename → %s", keuze, zoekterm, m_email, route, filename)

            if rgl == 0:
                open(filename, 'w').write(kop)
            elif rgl%57 == 0:
                open(filename, 'a').write(kop)
            mblad += 1
            
        open(filename,'a').write('{:<11d}'.format(row[1])+'{:<37.35s}'.format(row[15])\
            +'{:>6.2f}'.format(row[3])+'{:>6.2f}'.format(row[5])+'  '+\
            '{:10s}'.format(row[4])+' '+'{:<10d}'.format(row[2])+' '+'{:<10s}'.format(row[16])+'\n')
        rgl += 1
    printGeg(filename)
    kiesSelektie(route, m_email)
    logger.debug("<<< Exiting printRaaplijst(keuze=%s,zoekterm=%s,m_email=%s,route=%s)", keuze, zoekterm, m_email, route)
 
def kiesSelektie(route, m_email):
    logger.debug(">>> Entering kiesSelektie(route=%s,m_email=%s)", route, m_email)
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            if route == 0:
                self.setWindowTitle("Raaplijst materialen uitgifte")
            else:
                self.setWindowTitle("Raaplijst printen") 
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
            
            if route < 2:
                self.Keuze = QLabel()
                k0Edit = QComboBox()
                k0Edit.setFixedWidth(240)
                k0Edit.setFont(QFont("Arial",10))
                k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
                k0Edit.addItem('  Sorteersleutel voor zoeken')
                k0Edit.addItem('1. Alle afroepen')
                k0Edit.addItem('2. Interne werkorders')
                k0Edit.addItem('3. Externe werknummers')
                k0Edit.addItem('4. Per ordernummer')
                k0Edit.addItem('5. Per artikelnummer')           
                k0Edit.addItem('6. Op leverdatum')
                k0Edit.addItem('7. Op Poscode ivm Transport')
                k0Edit.addItem('8. Uitgeleverde afroepen')
                k0Edit.activated[str].connect(self.k0Changed)
            elif route == 2:
                self.Keuze = QLabel()
                k0Edit = QComboBox()
                k0Edit.setFixedWidth(240)
                k0Edit.setFont(QFont("Arial",10))
                k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
                k0Edit.addItem('  Sorteersleutel voor zoeken')
                k0Edit.addItem('2. Interne werkorders')
                k0Edit.addItem('4. Per ordernummer')
                k0Edit.addItem('5. Per artikelnummer')           
                k0Edit.addItem('6. Op leverdatum')
                k0Edit.addItem('7. Op Poscode ivm Transport')
                k0Edit.addItem('8. Uitgeleverde afroepen')
                k0Edit.activated[str].connect(self.k0Changed)
            elif route == 3:
                self.Keuze = QLabel()
                k0Edit = QComboBox()
                k0Edit.setFixedWidth(240)
                k0Edit.setFont(QFont("Arial",10))
                k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
                k0Edit.addItem('  Sorteersleutel voor zoeken')
                k0Edit.addItem('3. Externe werknummers')
                k0Edit.addItem('4. Per ordernummer')
                k0Edit.addItem('5. Per artikelnummer')           
                k0Edit.addItem('6. Op leverdatum')
                k0Edit.addItem('7. Op Poscode ivm Transport')
                k0Edit.addItem('8. Uitgeleverde afroepen')
                k0Edit.activated[str].connect(self.k0Changed)  
                
            self.Zoekterm = QLabel()
            zktermEdit = QLineEdit()
            zktermEdit.setFixedWidth(240)
            zktermEdit.setFont(QFont("Arial",10))
            zktermEdit.textChanged.connect(self.zktermChanged)
     
            grid = QGridLayout()
            grid.setSpacing(20)
                          
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 0, 0, 1, 2)
            
            if route == 0:
                grid.addWidget(QLabel('Keuzemenu voor het uitgeven van materialen'), 1, 0, 1, 3, Qt.AlignCenter)
            else:
                grid.addWidget(QLabel('Keuzemenu voor het printen van raaplijsten'), 1, 0, 1, 3, Qt.AlignCenter)
             
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 1, 1, 1, Qt.AlignRight)
                                  
            grid.addWidget(k0Edit, 2, 1)
            lbl1 = QLabel('Zoekterm')  
            lbl1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl1, 3, 0)
            grid.addWidget(zktermEdit, 3, 1)
            
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved  dj.jansen@casema.nl'), 5, 0, 1, 3, Qt.AlignCenter)
                      
            applyBtn = QPushButton('Zoeken')
            applyBtn.clicked.connect(self.accept)
                                       
            grid.addWidget(applyBtn, 4, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Sluiten')
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
    
            grid.addWidget(cancelBtn, 4, 1)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
            logger.debug(">>> Entering __init__(data_list=%s,header=%s)", data_list, header)
            logger.debug("__init__(data_list=%s,header=%s): font → %s", data_list, header, font)
            logger.debug("__init__(data_list=%s,header=%s): table_view → %s", data_list, header, table_view)
            logger.debug("__init__(data_list=%s,header=%s): grid → %s", data_list, header, grid)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): grid → %s", self, data_list, header, grid)
            logger.debug("__init__(data_list=%s,header=%s): table_model → %s", data_list, header, table_model)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): table_model → %s", self, data_list, header, table_model)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): table_view → %s", self, data_list, header, table_view)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): font → %s", self, data_list, header, font)
            logger.debug("__init__(data_list=%s,header=%s): pixmap → %s", data_list, header, pixmap)
            logger.debug("__init__(data_list=%s,header=%s): lbl → %s", data_list, header, lbl)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): lbl → %s", self, data_list, header, lbl)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): pixmap → %s", self, data_list, header, pixmap)
            logger.debug("__init__(data_list=%s,header=%s): logo → %s", data_list, header, logo)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): logo → %s", self, data_list, header, logo)
            logger.debug("__init__(data_list=%s,header=%s): freshBtn → %s", data_list, header, freshBtn)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): freshBtn → %s", self, data_list, header, freshBtn)
            logger.debug("__init__(data_list=%s,header=%s): sluitBtn → %s", data_list, header, sluitBtn)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): sluitBtn → %s", self, data_list, header, sluitBtn)
            logger.debug("<<< Exiting __init__(data_list=%s,header=%s)", data_list, header)

        def k0Changed(self, text):
            logger.debug(">>> Entering k0Changed(text=%s)", text)
            logger.debug("k0Changed(self=%s,text=%s): Keuze → %s", self, text, Keuze)
            self.Keuze.setText(text)
            logger.debug("<<< Exiting k0Changed(text=%s)", text)
            
        def zktermChanged(self, text):
            logger.debug(">>> Entering zktermChanged(text=%s)", text)
            logger.debug("zktermChanged(self=%s,text=%s): Zoekterm → %s", self, text, Zoekterm)
            self.Zoekterm.setText(text)
            logger.debug("<<< Exiting zktermChanged(text=%s)", text)
 
        def returnk0(self):
            logger.debug(">>> Entering returnk0()")
            logger.debug("<<< Exiting returnk0()")
            return self.Keuze.text()
        
        def returnzkterm(self):
            logger.debug(">>> Entering returnzkterm()")
            logger.debug("<<< Exiting returnzkterm()")
            return self.Zoekterm.text()
        
        @staticmethod
        def getData(parent=None):
            dialog = Widget(parent)
            dialog.exec_()
            logger.debug(">>> Entering getData(parent=%s)", parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog)
            logger.debug("<<< Exiting getData(parent=%s)", parent)
            return [dialog.returnk0(), dialog.returnzkterm()] 
    
    window = Widget()
    data = window.getData()
    if not data[0] or data[0][0] == ' ':
        keuze = 0
    elif data[0]:
        keuze = int(data[0][0])
    else:
        keuze = 0
    if data[1]:
        zoekterm = data[1].upper()
    else:
        zoekterm = ''
    if route == 0:
        raapLijst(keuze,zoekterm, m_email, route)
    else:
        printRaaplijst(keuze, zoekterm, m_email, route)

def raapLijst(keuze, zoekterm, m_email, route):
    logger.debug(">>> Entering raapLijst(keuze=%s,zoekterm=%s,m_email=%s,route=%s)", keuze, zoekterm, m_email, route)
    class MyWindow(QDialog):
        logger.error("Exception in raapLijst(keuze=%s,zoekterm=%s,m_email=%s,route=%s)", keuze, zoekterm, m_email, route, exc_info=True)
        def __init__(self, data_list, header, *args):
            QWidget.__init__(self, *args,)
            self.setWindowTitle('Raaplijst Opvragen / Muteren')
            self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
            self.setWindowFlags(self.windowFlags()| Qt.WindowSystemMenuHint |
                              Qt.WindowMinMaxButtonsHint)
            self.setFont(QFont('Arial', 10))
            grid = QGridLayout()
            grid.setSpacing(20)
            
            table_model = MyTableModel(self, data_list, header)
            table_view = QTableView()
            table_view.setModel(table_model)
            font = QFont("Arial", 10)
            table_view.setFont(font)
            table_view.resizeColumnsToContents()
            table_view.setSelectionBehavior(QTableView.SelectRows)
            table_view.clicked.connect(boekAfroep)
            grid.addWidget(table_view, 0, 0, 1, 13)
            
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl, 1, 0, 1, 2)
       
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 1, 12, 1, 1, Qt.AlignRight)
            
            freshBtn = QPushButton('Verversen')
            freshBtn.clicked.connect(lambda: refresh(keuze, zoekterm, m_email, route, self))

            freshBtn.setFont(QFont("Arial",10))
            freshBtn.setFixedWidth(100) 
            freshBtn.setStyleSheet("color: black;  background-color: gainsboro")
   
            grid.addWidget(freshBtn, 1, 11, 1, 1, Qt.AlignRight)
            
            sluitBtn = QPushButton('Sluiten')
            sluitBtn.clicked.connect(self.close)

            sluitBtn.setFont(QFont("Arial",10))
            sluitBtn.setFixedWidth(100) 
            sluitBtn.setStyleSheet("color: black;  background-color: gainsboro") 
            
            grid.addWidget(sluitBtn, 1, 10)
          
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 1, 0, 1, 13, Qt.AlignCenter)
            
            self.setLayout(grid)
            self.setGeometry(50, 50, 1500, 900)
            logger.debug(">>> Entering __init__(parent=%s,mylist=%s,header=%s)", parent, mylist, header)
            logger.debug("<<< Exiting __init__(parent=%s,mylist=%s,header=%s)", parent, mylist, header)
            logger.debug("__init__(self=%s,parent=%s,mylist=%s,header=%s): self.mylist → %s", self, parent, mylist, header, self.mylist)
            
    class MyTableModel(QAbstractTableModel):
        def __init__(self, parent, mylist, header, *args):
            logger.debug("__init__(self=%s,parent=%s,mylist=%s,header=%s): self.header → %s", self, parent, mylist, header, self.header)
            QAbstractTableModel.__init__(self, parent, *args)
            self.mylist = mylist
            logger.debug(">>> Entering __init__(parent=%s)", parent)
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap)
            logger.debug("__init__(parent=%s): input_validator → %s", parent, input_validator)
            logger.debug("__init__(parent=%s): zkwerknEdit → %s", parent, zkwerknEdit)
            logger.debug("__init__(parent=%s): self.Werknummer → %s", parent, self.Werknummer)
            logger.debug("__init__(self=%s,parent=%s): zkwerknEdit → %s", self, parent, zkwerknEdit)
            logger.debug("__init__(parent=%s): reg_ex → %s", parent, reg_ex)
            logger.debug("__init__(self=%s,parent=%s): reg_ex → %s", self, parent, reg_ex)
            logger.debug("__init__(self=%s,parent=%s): input_validator → %s", self, parent, input_validator)
            logger.debug("__init__(parent=%s): artEdit → %s", parent, artEdit)
            logger.debug("__init__(parent=%s): self.Artikelnummer → %s", parent, self.Artikelnummer)
            logger.debug("__init__(self=%s,parent=%s): artEdit → %s", self, parent, artEdit)
            logger.debug("__init__(parent=%s): hoevEdit → %s", parent, hoevEdit)
            logger.debug("__init__(parent=%s): self.Hoeveelheid → %s", parent, self.Hoeveelheid)
            logger.debug("__init__(self=%s,parent=%s): hoevEdit → %s", self, parent, hoevEdit)
            logger.debug("__init__(parent=%s): grid → %s", parent, grid)
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid)
            logger.debug("__init__(parent=%s): lbl → %s", parent, lbl)
            logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl)
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap)
            logger.debug("__init__(parent=%s): logo → %s", parent, logo)
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo)
            logger.debug("__init__(parent=%s): lbl1 → %s", parent, lbl1)
            logger.debug("__init__(self=%s,parent=%s): lbl1 → %s", self, parent, lbl1)
            logger.debug("__init__(parent=%s): lbl2 → %s", parent, lbl2)
            logger.debug("__init__(self=%s,parent=%s): lbl2 → %s", self, parent, lbl2)
            logger.debug("__init__(parent=%s): lbl4 → %s", parent, lbl4)
            logger.debug("__init__(self=%s,parent=%s): lbl4 → %s", self, parent, lbl4)
            logger.debug("__init__(parent=%s): lbl3 → %s", parent, lbl3)
            logger.debug("__init__(self=%s,parent=%s): lbl3 → %s", self, parent, lbl3)
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn)
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn)
            logger.debug("__init__(parent=%s): sluitBtn → %s", parent, sluitBtn)
            logger.debug("__init__(self=%s,parent=%s): sluitBtn → %s", self, parent, sluitBtn)
            logger.debug("<<< Exiting __init__(parent=%s)", parent)
            self.header = header
        def rowCount(self, parent):
            logger.debug(">>> Entering rowCount(parent=%s)", parent)
            return len(self.mylist)
        def columnCount(self, parent):
            logger.debug(">>> Entering columnCount(parent=%s)", parent)
            return len(self.mylist[0])
        def data(self, index, role):
            logger.debug(">>> Entering data(index=%s,role=%s)", index, role)
            veld = self.mylist[index.row()][index.column()]
            logger.debug("data(index=%s,role=%s): veld → %s", index, role, veld)
            logger.debug("data(self=%s,index=%s,role=%s): veld → %s", self, index, role, veld)
            if not index.isValid():
                return None
            elif role == Qt.TextAlignmentRole and (type(veld) == float or type(veld) == int):
                return Qt.AlignRight | Qt.AlignVCenter
            elif role != Qt.DisplayRole:
                return None
            if type(veld) == float:
                return '{:12.2f}'.format(veld)
            else:
                logger.debug("<<< Exiting data(index=%s,role=%s)", index, role)
                return veld
        def headerData(self, col, orientation, role):
            logger.debug(">>> Entering headerData(col=%s,orientation=%s,role=%s)", col, orientation, role)
            if orientation == Qt.Horizontal and role == Qt.DisplayRole:
                return self.header[col]
            logger.debug("<<< Exiting headerData(col=%s,orientation=%s,role=%s)", col, orientation, role)
            return None
       
    metadata = MetaData()
    raaplijst = Table('raaplijst', metadata,
        Column('lijstID', Integer,primary_key=True),
        Column('artikelID', Integer),
        Column('werkorder', Integer),
        Column('afroep', Float),
        Column('leverdatum', String),
        Column('geleverd', Float),
        Column('meerwerk', Boolean),
        Column('postcode', String),
        Column('huisnummer', Integer),
        Column('toevoeging', String),
        Column('alternatief', String),
        Column('boekdatum', String),
        Column('straat', String),
        Column('woonplaats', String))
       
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
 
    header = ['LijstID','Artikelnr','Werkorder','Afroep','Leverdatum','Geleverd',\
          'Meerwerk','Postcode', 'Huisnummer','Toevoeging', 'Alternatief Adres',\
          'Boekdatum','Straat','Woonplaats']
    
    import validZt 
    if keuze == 1:
        selafr = select([raaplijst]).where(raaplijst.c.geleverd < raaplijst.c.afroep)\
           .order_by(raaplijst.c.werkorder, raaplijst.c.leverdatum)
    elif keuze == 2: 
        selafr = select([raaplijst]).where(and_(raaplijst.c.werkorder < 800000000,\
             raaplijst.c.geleverd < raaplijst.c.afroep)).order_by(raaplijst.c.leverdatum)
    elif keuze == 3:
        selafr = select([raaplijst]).where(and_(raaplijst.c.werkorder > 800000000,
        raaplijst.c.geleverd < raaplijst.c.afroep)).order_by(raaplijst.c.leverdatum)
    elif keuze == 4 and validZt.zt(zoekterm, 15):
        selafr = select([raaplijst]).where(and_(raaplijst.c.werkorder == int(zoekterm),\
          raaplijst.c.geleverd < raaplijst.c.afroep)).order_by(raaplijst.c.leverdatum.desc())
    elif keuze == 5 and validZt.zt(zoekterm, 2):
        selafr = select([raaplijst]).where(and_(raaplijst.c.artikelID == int(zoekterm),\
          raaplijst.c.geleverd < raaplijst.c.afroep)).order_by(raaplijst.c.leverdatum.desc())
    elif keuze == 6 and validZt.zt(zoekterm, 10):
        selafr = select([raaplijst]).where(and_(raaplijst.c.leverdatum.like(zoekterm+'%'),
                raaplijst.c.geleverd < raaplijst.c.afroep))\
            .order_by(raaplijst.c.leverdatum, raaplijst.c.werkorder)
    elif keuze == 7 and validZt.zt(zoekterm, 9):
        selafr = select([raaplijst]).where(and_(raaplijst.c.postcode.ilike(zoekterm+'%'),\
             raaplijst.c.geleverd < raaplijst.c.afroep))\
            .order_by(raaplijst.c.leverdatum, raaplijst.c.werkorder)
    elif keuze == 8:
        selafr = select([raaplijst]).where(and_(raaplijst.c.geleverd >= raaplijst.c.afroep,\
                       raaplijst.c.afroep > 0))\
           .order_by(raaplijst.c.werkorder, raaplijst.c.leverdatum)
    else:
        ongInvoer()
        kiesSelektie(0, m_email)
   
    if con.execute(selafr).fetchone():
       rpafr = con.execute(selafr)
    else:
       geenRecord()
       kiesSelektie(0, m_email)
       
    data_list=[]
    for row in rpafr:
        data_list += [(row)]
        
    def boekAfroep(idx):
        logger.debug(">>> Entering boekAfroep(idx=%s)", idx)
        mlijstnr = idx.data()
        logger.debug("boekAfroep(idx=%s): mlijstnr → %s", idx, mlijstnr)
        if idx.column() == 0 :
            metadata = MetaData()
            logger.debug("boekAfroep(idx=%s): metadata → %s", idx, metadata)
            raaplijst = Table('raaplijst', metadata,
                Column('lijstID', Integer,primary_key=True),
                Column('artikelID', Integer),
                Column('werkorder', Integer),
                Column('afroep', Float),
                Column('leverdatum', String),
                Column('geleverd', Float),
                Column('meerwerk', Boolean),
                Column('postcode', String),
                Column('huisnummer', Integer),
                Column('toevoeging', String),
                Column('alternatief', String),
                Column('boekdatum', String),
                Column('straat', String),
                Column('woonplaats', String))
            
            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            logger.debug("boekAfroep(idx=%s): engine → %s", idx, engine)
            con = engine.connect()
      
            logger.debug("boekAfroep(idx=%s): con → %s", idx, con)
            selrlr = select([raaplijst]).where(raaplijst.c.lijstID == mlijstnr)                           
            rprlr = con.execute(selrlr).first()
            logger.debug("boekAfroep(idx=%s): selrlr → %s", idx, selrlr)
            logger.debug("boekAfroep(idx=%s): rprlr → %s", idx, rprlr)
           
            mwerknr = rprlr[2]
            martnr = rprlr[1]
            logger.debug("boekAfroep(idx=%s): mwerknr → %s", idx, mwerknr)
            logger.debug("boekAfroep(idx=%s): martnr → %s", idx, martnr)
            mleverdat = rprlr[4]
            logger.debug("boekAfroep(idx=%s): mleverdat → %s", idx, mleverdat)
            mmmstatus = rprlr[6]
            logger.debug("boekAfroep(idx=%s): mmmstatus → %s", idx, mmmstatus)
            mafroep = rprlr[3]
            logger.debug("boekAfroep(idx=%s): mafroep → %s", idx, mafroep)
            mgeleverd = rprlr[5]
            logger.debug("boekAfroep(idx=%s): mgeleverd → %s", idx, mgeleverd)
            
            class Widget(QDialog):
                logger.debug("<<< Exiting boekAfroep(idx=%s)", idx)
                def __init__(self, parent=None):
                    super(Widget, self).__init__(parent)
                    logger.debug(">>> Entering __init__(parent=%s)", parent)
                    self.setWindowTitle("Materiaaluitgifte muteren")
                    self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            
                    self.setFont(QFont('Arial', 10))
                               
                    self.Werknummer = QLabel()
                    zkwerknEdit = QLineEdit(str(mwerknr))
                    zkwerknEdit.setFont(QFont("Arial",10))
                    zkwerknEdit.setDisabled(True)
                    zkwerknEdit.setStyleSheet("color:black")
                    zkwerknEdit.setAlignment(Qt.AlignRight)
                    zkwerknEdit.textChanged.connect(self.zkwerknChanged) 
                    reg_ex = QRegExp("^[8]{1}[0-9]{8}$")
                    input_validator = QRegExpValidator(reg_ex, zkwerknEdit)
                    zkwerknEdit.setValidator(input_validator)
                                
                    self.Artikelnummer = QLabel()
                    artEdit = QLineEdit(str(martnr))
                    artEdit.setFixedWidth(150)
                    artEdit.setFont(QFont("Arial",10))
                    artEdit.setDisabled(True)
                    artEdit.setStyleSheet("color:black")
                    artEdit.setAlignment(Qt.AlignRight)
                    artEdit.textChanged.connect(self.artChanged) 
                    reg_ex = QRegExp("^[2]{1}[0-9]{8}$")
                    input_validator = QRegExpValidator(reg_ex, artEdit)
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
                    grid.setSpacing(20)
                                  
                    lbl = QLabel()
                    pixmap = QPixmap('./images/logos/verbinding.jpg')
                    lbl.setPixmap(pixmap)
                    grid.addWidget(lbl ,0, 0)
                    
                    logo = QLabel()
                    pixmap = QPixmap('./images/logos/logo.jpg')
                    logo.setPixmap(pixmap)
                    grid.addWidget(logo , 0, 2, 1, 1, Qt.AlignRight) 
                                 
                    lbl1 = QLabel('Werknummer')  
                    lbl1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl1, 1, 0)
                    grid.addWidget(zkwerknEdit, 1, 1)
                                                  
                    lbl2 = QLabel('Artikelnummer')  
                    lbl2.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl2, 2, 0)
                    grid.addWidget(artEdit, 2, 1)
                    
                    lbl4 = QLabel('Afroep: '+ str(mafroep)+ ' - Reeds geleverd: '+str(mgeleverd))
                    grid.addWidget(lbl4, 3, 0, 1, 3, Qt.AlignCenter)
                    lbl3 = QLabel('Uitgifte')  
                    lbl3.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl3, 4, 0)
                    grid.addWidget(hoevEdit, 4 , 1)
                    
                    if mmmstatus:
                        grid.addWidget(QLabel('Meerwerk'), 4, 2)
                        
                    grid.addWidget(QLabel('Leverdatum'), 5, 0, Qt.AlignRight)
                    grid.addWidget(QLabel(mleverdat), 5, 1)                     
                    
                    self.setLayout(grid)
                    self.setGeometry(500, 300, 150, 150)
              
                    applyBtn = QPushButton('Muteren')
                    applyBtn.clicked.connect(self.accept)
            
                    grid.addWidget(applyBtn, 6, 2, 1 , 1, Qt.AlignRight)
                    applyBtn.setFont(QFont("Arial",10))
                    applyBtn.setFixedWidth(100)
                    applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
                    
                    sluitBtn = QPushButton('Sluiten')
                    sluitBtn.clicked.connect(self.close)
            
                    grid.addWidget(sluitBtn, 6, 0, 1, 2, Qt.AlignRight)
                    sluitBtn.setFont(QFont("Arial",10))
                    sluitBtn.setFixedWidth(100)
                    sluitBtn.setStyleSheet("color: black;  background-color: gainsboro")
                                
                    grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 7, 0, 1, 3, Qt.AlignCenter)     
                    logger.debug("<<< Exiting __init__(parent=%s)", parent)
                                                                              
                def zkwerknChanged(self, text):
                    logger.debug(">>> Entering zkwerknChanged(text=%s)", text)
                    logger.debug("zkwerknChanged(self=%s,text=%s): Werknummer → %s", self, text, Werknummer)
                    self.Werknummer.setText(text)
                    logger.debug("<<< Exiting zkwerknChanged(text=%s)", text)
                    
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
                                                            
                def returnzkwerkn(self):
                    logger.debug(">>> Entering returnzkwerkn()")
                    logger.debug("<<< Exiting returnzkwerkn()")
                    return self.Werknummer.text()
                
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
                    dialog.exec_()
                    return [dialog.returnzkwerkn(), dialog.returnart(), dialog.returnhoev()]
               
            window = Widget()
            data = window.getData()
            mhoev = 0
            if data[0] and len(data[0]) == 9 and _11check(data[0]):
                mwerknr = int(data[0])
            elif not data[0] and len(str(mwerknr)) == 9 and _11check(mwerknr):
                mwerknr = int(mwerknr)
            else:
                foutWerknr()
                return('')
     
            if str(mwerknr)[0] == '7':
                metadata = MetaData()   
                orders_intern = Table('orders_intern', metadata,
                    Column('werkorderID', Integer(), primary_key=True),
                    Column('voortgangstatus', String))
                engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
                con = engine.connect()
                selwerk = select([orders_intern]).where(orders_intern.c.werkorderID == mwerknr)
                rpwerk = con.execute(selwerk).first()
                metadata = MetaData()
                orders_intern = Table('orders_intern', metadata,
                    Column('werkorderID',Integer(), primary_key=True),
                    Column('werk_materialen', Float),
                    Column('meerminderwerk', Float))
                artikelmutaties = Table('artikelmutaties', metadata,
                    Column('mutatieID', Integer, primary_key=True),
                    Column('artikelID', None, ForeignKey('artikelen.artikelID')),
                    Column('werkorderID', None, ForeignKey('orders_intern.werkorderID')),
                    Column('orderinkoopID', None, ForeignKey('orders_inkoop.orderinkoopID')),
                    Column('hoeveelheid', Float),
                    Column('boekdatum', String),
                    Column('tot_mag_prijs', Float),
                    Column('btw_hoog', Float),
                    Column('mmstatus', Boolean))
            elif str(mwerknr)[0] == '8':
                metadata = MetaData()   
                werken = Table('werken', metadata,
                    Column('werknummerID', Integer, primary_key=True),
                    Column('voortgangstatus', String),
                    Column('kosten_materialen', Float),
                    Column('meerminderwerk', Float))
                artikelmutaties = Table('artikelmutaties', metadata,
                    Column('mutatieID', Integer, primary_key=True),
                    Column('artikelID', None, ForeignKey('artikelen.artikelID')),
                    Column('werknummerID', None, ForeignKey('werken.werknoID')),
                    Column('orderinkoopID', None, ForeignKey('orders_inkoop.orderinkoopID')),
                    Column('hoeveelheid', Float),
                    Column('boekdatum', String),
                    Column('tot_mag_prijs', Float),
                    Column('btw_hoog', Float),
                    Column('mmstatus', Boolean))
    
                engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
                con = engine.connect()
                selwerk = select([werken]).where(werken.c.werknummerID == mwerknr)
                rpwerk = con.execute(selwerk).first()
                      
            if rpwerk[1] == 'H':
                werkGereed()
                return(mwerknr)
            if data[2]:
                mhoev = float(data[2])
            else:
                return(mwerknr)
              
            metadata = MetaData()
            artikelen = Table('artikelen', metadata,
                Column('artikelID', Integer(), primary_key=True),
                Column('artikelomschrijving', String),
                Column('artikelprijs', Float),
                Column('art_voorraad', Float, CheckConstraint('art_voorraad >= 0')),
                Column('art_min_voorraad', Float),
                Column('art_bestelgrootte', Float),
                Column('bestelstatus', Boolean),
                Column('mutatiedatum', String),
                Column('reserveringsaldo', Float),
                Column('jaarverbruik_1', Float),
                Column('jaarverbruik_2', Float))
                      
            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            con = engine.connect()
            sel = select([artikelen]).where(artikelen.c.artikelID == martnr)
            transaction = con.begin()
            result = con.execute(sel).first()
            martprijs = result[2]
            martvrd = result[3]
            martminvrd = result[4]
            mboekd = str(datetime.datetime.now())[0:10]
            mjaar = int(str(datetime.datetime.now())[0:4])

            if martvrd - mhoev <= martminvrd:
                martbestst = False
            else:
                martbestst = True
            if mhoev <= 0:
                foutHoev()
                return('')
            try:
                if mjaar%2 == 0:            #even jaartal
                    stmt = update(artikelen).where(artikelen.c.artikelID == martnr).values(\
                     art_voorraad = artikelen.c.art_voorraad - mhoev, bestelstatus = martbestst,\
                     mutatiedatum = mboekd, reserveringsaldo = artikelen.c.reserveringsaldo - mhoev,\
                     jaarverbruik_1 = artikelen.c.jaarverbruik_1 + mhoev)
                    con.execute(stmt)
                    mwaarde = martprijs*1.1*mhoev
                    con = engine.connect()
                elif mjaar%2 == 1:                     #oneven jaartal
                    stmt = update(artikelen).where(artikelen.c.artikelID == martnr).values(\
                     art_voorraad = artikelen.c.art_voorraad - mhoev, bestelstatus = martbestst,\
                     mutatiedatum = mboekd, reserveringsaldo = artikelen.c.reserveringsaldo - mhoev,\
                     jaarverbruik_2 = artikelen.c.jaarverbruik_2 + mhoev)
                    con.execute(stmt)
                    mwaarde = martprijs*1.1*mhoev
                    con = engine.connect()
                if mmmstatus:
                    mmeerminder = mwaarde
                else:
                    mmeerminder = 0

                if str(mwerknr)[0] == '8':
                    stmt = update(werken).where(werken.c.werknummerID == mwerknr).values(\
                     kosten_materialen = werken.c.kosten_materialen + mwaarde,\
                     meerminderwerk = werken.c.meerminderwerk + mmeerminder)
                    con.execute(stmt)
                    try:
                        mutatienr=(con.execute(select([func.max(artikelmutaties.c.mutatieID,\
                            type_=Integer)])).scalar())
                        mutatienr += 1
                    except:
                        mutatienr = 1
                    ins = insert(artikelmutaties).values(mutatieID = mutatienr, artikelID =\
                        martnr, werknummerID = mwerknr, hoeveelheid = -mhoev, boekdatum = mboekd,\
                        tot_mag_prijs = mhoev*martprijs, btw_hoog = .21*mhoev*martprijs,\
                        mmstatus = mmmstatus) 
                    con.execute(ins)
                elif str(mwerknr)[0] == '7':
                    stmt = update(orders_intern).where(orders_intern.c.werkorderID == mwerknr).values(\
                     werk_materialen = orders_intern.c.werk_materialen + mwaarde,\
                     meerminderwerk = orders_intern.c.meerminderwerk + mmeerminder)
                    con.execute(stmt)
                    try:
                        mutatienr=(con.execute(select([func.max(artikelmutaties.c.mutatieID,\
                          type_=Integer)])).scalar())
                        mutatienr += 1
                    except:
                        mutatienr = 1
                    ins = insert(artikelmutaties).values(mutatieID = mutatienr, artikelID =\
                        martnr, werkorderID = mwerknr, hoeveelheid = -mhoev, boekdatum = mboekd,\
                        tot_mag_prijs = mhoev*martprijs, btw_hoog = .21*mhoev*martprijs,\
                        mmstatus = mmmstatus)
                    con.execute(ins)
                updrl = update(raaplijst).where(raaplijst.c.lijstID == mlijstnr).\
                values(geleverd = raaplijst.c.geleverd+mhoev, boekdatum = mboekd )
                con.execute(updrl)
                transaction.commit()
                invoerOK()
            except IntegrityError:
                transaction.rollback()
                negVoorraad()
            con.close 
            return(mwerknr)
    
    win = MyWindow(data_list, header)
    win.exec_() 
    kiesSelektie(route, m_email)