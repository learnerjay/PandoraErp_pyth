from login import hoofdMenu #dutch
import os, datetime
from PyQt5.QtCore import Qt, QAbstractTableModel, QRegExp
from PyQt5.QtGui import QFont, QPixmap, QIcon, QRegExpValidator
from PyQt5.QtWidgets import  QDialog, QLabel, QGridLayout,\
                             QPushButton, QMessageBox, QLineEdit, QWidget,\
                             QTableView, QVBoxLayout
from sqlalchemy import (Table, Column, Integer, String, Float,\
                        MetaData, create_engine, ForeignKey)
from sqlalchemy.sql import select, update, insert, and_, func
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
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Opdracht is nog niet verkregen voor deze calculatie\nBestelling voor Inkoop kan nog niet worden geprint!')
    msg.setWindowTitle('Werknummer')
    logger.debug("<<< Exiting foutWerknr()", extra={"event.action": "foutWerknr"})
    msg.exec_()
    
def calcBestaatniet():
    logger.warning(">>> Entering calcBestaatniet()", extra={"event.action": "calcBestaatniet"})
    msg = QMessageBox()
    logger.debug("calcBestaatniet(): msg → %s", msg, extra={"event.action": "calcBestaatniet"})
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Calculatie is niet aanwezig!')
    msg.setWindowTitle('INVOEREN')
    logger.debug("<<< Exiting calcBestaatniet()", extra={"event.action": "calcBestaatniet"})
    msg.exec_()
    
def printing():
    logger.warning(">>> Entering printing()", extra={"event.action": "printing"})
    msg = QMessageBox()
    logger.debug("printing(): msg → %s", msg, extra={"event.action": "printing"})
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Information)
    msg.setText('Ogenblik afdrukken wordt gestart!')
    msg.setWindowTitle('AFDRUKKEN')
    logger.debug("<<< Exiting printing()", extra={"event.action": "printing"})
    msg.exec_()
     
def zoekCalculatie(m_email):
    logger.warning(">>> Entering zoekCalculatie(m_email=%s)", m_email, extra={"event.action": "zoekCalculatie"})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle("Calculeren / Opvragen / Printen")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
  
            self.Calculatie = QLabel()
            zkcalcEdit = QLineEdit()
            zkcalcEdit.setFixedWidth(100)
            zkcalcEdit.setFont(QFont("Arial",10))
            zkcalcEdit.textChanged.connect(self.zkcalcChanged)
            reg_ex = QRegExp('^[1-9]{1}[0-9]{0,8}$')
            input_validator = QRegExpValidator(reg_ex, zkcalcEdit)
            zkcalcEdit.setValidator(input_validator)  
            
            grid = QGridLayout()
            grid.setSpacing(20)
                          
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 0, 0, 1, 2)
            
            lbl1 = QLabel('Calculatienummer\nof Werknummer.')  
            lbl1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl1, 1, 0)
            grid.addWidget(zkcalcEdit, 1, 1)
            
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 4, 0, 1, 2, Qt.AlignCenter)
             
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 1, 1, 1, Qt.AlignRight)
   
            applyBtn = QPushButton('Zoeken')
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 3, 1)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Sluiten')
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
    
            grid.addWidget(cancelBtn, 3, 0, 1, 1,Qt.AlignRight)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
            logger.debug("<<< Exiting __init__(parent=%s,mylist=%s,header=%s)", parent, mylist, header, extra={"event.action": "__init__", "logrite.mylist": mylist})
             
        def zkcalcChanged(self, text):
            logger.warning(">>> Entering zkcalcChanged(text=%s)", text, extra={"event.action": "zkcalcChanged", "logrite.text": text})
            self.Calculatie.setText(text)
            logger.debug("<<< Exiting zkcalcChanged(text=%s)", text, extra={"event.action": "zkcalcChanged", "logrite.text": text})
             
        def returnCalculatie(self):
            logger.warning(">>> Entering returnCalculatie()", extra={"event.action": "returnCalculatie"})
            logger.debug("<<< Exiting returnCalculatie()", extra={"event.action": "returnCalculatie"})
            return self.Calculatie.text()
        
        @staticmethod
        def getData(parent=None):
            logger.warning(">>> Entering getData(parent=%s)", parent, extra={"event.action": "getData"})
            dialog = Widget(parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog, extra={"event.action": "getData"})
            dialog.exec_()
            logger.debug("<<< Exiting getData(parent=%s)", parent, extra={"event.action": "getData"})
            return [dialog.returnCalculatie()]       

    window = Widget()
    data = window.getData()
    
    metadata = MetaData()
    calculaties = Table('calculaties', metadata,
        Column('calculatie', Integer),
        Column('werkomschrijving', String),
        Column('verwerkt', Integer),
        Column('koppelnummer', Integer))
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
    if not data[0]:
       return(0)
    elif data[0][0] == '8' and len(data[0]) == 9:
        mcalnr = data[0]
        selcl = select([calculaties]).where(calculaties.c.koppelnummer == int(mcalnr))
        rpcl = con.execute(selcl).first()
    elif data[0] and len(data[0]) <9:
        mcalnr = data[0]
        selcl = select([calculaties]).where(calculaties.c.calculatie == int(mcalnr))
        rpcl = con.execute(selcl).first()
    else:
        calcBestaatniet()
        zoekCalculatie(m_email)
    if not rpcl:
        calcBestaatniet()
        zoekCalculatie(m_email)
    elif rpcl and (not rpcl[2]):
        opbouwRp(rpcl[0], rpcl[1], rpcl[2], rpcl[3], m_email)
    elif rpcl and rpcl[2]:
        opvragenCalc(rpcl[0], rpcl[1], rpcl[2], rpcl[3], m_email)
    
def opvragenCalc(mcalnr, mwerkomschr,mverw, mwerknr, m_email):
    logger.warning(">>> Entering opvragenCalc(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s)", mcalnr, mwerkomschr, mverw, mwerknr, m_email, extra={"event.action": "opvragenCalc", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
    class MainWindow(QDialog):
        def __init__(self):
            QDialog.__init__(self)
            
            grid = QGridLayout()
            grid.setSpacing(20)
            
            self.lbl = QLabel()
            self.pixmap = QPixmap('./images/logos/verbinding.jpg')
            self.lbl.setPixmap(self.pixmap)
            grid.addWidget(self.lbl , 0, 1)
    
            self.logo = QLabel()
            self.pixmap = QPixmap('./images/logos/logo.jpg')
            self.logo.setPixmap(self.pixmap)
            grid.addWidget(self.logo , 0, 3, 1, 1, Qt.AlignRight)
              
            self.setFont(QFont('Arial', 10))
            grid.addWidget(QLabel('Calculatie:      '+str(mcalnr)+'\nWerknummer: '+str(mwerknr)), 1, 1, 1, 3)
            grid.addWidget(QLabel(mwerkomschr[0:35]), 2 , 1, 1, 3)
                                    
            self.setWindowTitle("Calculatie opvragen / printen") 
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
                                                      
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved\n   dj.jansen@casema.nl'), 7, 0, 2, 4, Qt.AlignCenter)
            
            self.toonBtn = QPushButton('Calculatie\nOpvragen')
            self.toonBtn.clicked.connect(lambda: toonCalculatie(mcalnr, mwerknr))
            grid.addWidget(self.toonBtn, 5, 3)
            self.toonBtn.setFont(QFont("Arial",10))
            self.toonBtn.setFixedWidth(110)           
            self.toonBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            self.artlijstBtn = QPushButton('Artikellijst\nOpvragen')
            self.artlijstBtn.clicked.connect(lambda: toonArtikellijst(mcalnr, mwerknr))
            grid.addWidget(self.artlijstBtn,5, 1, 1, 1, Qt.AlignRight)
            self.artlijstBtn.setFont(QFont("Arial",10))
            self.artlijstBtn.setFixedWidth(110)
            self.artlijstBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            self.dienstenBtn = QPushButton('Materiëel\nBestellijst Opvragen')
            self.dienstenBtn.clicked.connect(lambda: toonDienstenlijst(mcalnr, mwerknr))
            grid.addWidget(self.dienstenBtn, 5, 2)
            self.dienstenBtn.setFont(QFont("Arial",10))
            self.dienstenBtn.setFixedWidth(200)
            self.dienstenBtn.setStyleSheet("color: black;  background-color: gainsboro")
                             
            self.printBtn = QPushButton('Calculatie\nPrinten')
            self.printBtn.clicked.connect(lambda: printCalculatie(mcalnr, mwerknr))
            grid.addWidget(self.printBtn, 4, 3)
            self.printBtn.setFont(QFont("Arial",10))
            self.printBtn.setFixedWidth(110)
            self.printBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            self.artprintBtn = QPushButton('Artikellijst\nPrinten')
            self.artprintBtn.clicked.connect(lambda: printArtikellijst(mcalnr, mwerknr))
            grid.addWidget(self.artprintBtn, 4, 1, 1, 1, Qt.AlignRight)
            self.artprintBtn.setFont(QFont("Arial",10))
            self.artprintBtn.setFixedWidth(110)
            self.artprintBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            self.dienstenprintBtn = QPushButton('Materiëel\nBestellijst Printen')
            self.dienstenprintBtn.clicked.connect(lambda: printDienstenlijst(mcalnr, mwerknr))
            grid.addWidget(self.dienstenprintBtn, 4, 2)
            self.dienstenprintBtn.setFont(QFont("Arial",10))
            self.dienstenprintBtn.setFixedWidth(200)
            self.dienstenprintBtn.setStyleSheet("color: black;  background-color: gainsboro")
           
            self.terugBtn = QPushButton('T\ne\nr\nu\ng')
            self.terugBtn.clicked.connect(self.close)
            grid.addWidget(self.terugBtn, 4, 1, 5, 1, Qt.AlignTop)
            self.terugBtn.setFont(QFont("Arial", 10))
            self.terugBtn.setFixedWidth(40)
            self.terugBtn.setFixedHeight(125)
            self.terugBtn.setStyleSheet("color: black;  background-color: gainsboro")
                                             
            self.setLayout(grid)
            self.setGeometry(600, 300, 150, 150)
     
    mainWin = MainWindow()
    mainWin.exec_()
    zoekCalculatie(m_email)
    
def opbouwRp(mcalnr, mwerkomschr, mverw, mwerknr, m_email):
    logger.warning(">>> Entering opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s)", mcalnr, mwerkomschr, mverw, mwerknr, m_email, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
    metadata = MetaData()
    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): metadata → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, metadata, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
    calculaties = Table('calculaties', metadata,
        Column('calcID', Integer(), primary_key=True),
        Column('clusterID', None, ForeignKey('clusters.clusterID')),
        Column('hoeveelheid', Float),
        Column('calculatie', Integer),
        Column('materialen', Float))
    cluster_artikelen = Table('cluster_artikelen', metadata,
        Column('cluster_artID',Integer, primary_key=True),
        Column('artikelID', None, ForeignKey('artikelen.artikelID')),
        Column('clusterID', None, ForeignKey('clusters.clusterID')),
        Column('hoeveelheid', Float))
    artikelen = Table('artikelen', metadata,
        Column('artikelID', Integer(), primary_key=True),
        Column('artikelprijs', Float))

    params_finance = Table('params_finance', metadata,
        Column('financeID', Integer, primary_key=True),
        Column('factor', Float),
        Column('amount', Float))
    params_hours = Table('params_hours', metadata,
        Column('rateID', Integer, primary_key=True),
        Column('hourly_tariff', Float),
        Column('overhead_factor', Float),
        Column('wageID', None, ForeignKey('lonen.loonID')),
        Column('travel_time', Float))
    params_services = Table('params_services', metadata,
        Column('servicesID', Integer, primary_key=True),
        Column('hourly_tariff', Float),
        Column('overhead_factor', Float))

    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): engine → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, engine, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
    con = engine.connect()
    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): con → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, con, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
    selpar = select([params_finance]).order_by(params_finance.c.financeID)
    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): selpar → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, selpar, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
    rppar = con.execute(selpar).fetchall()
    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): rppar → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, rppar, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})

    selpar1 = select([params_hours]).order_by(params_hours.c.rateID)
    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): selpar1 → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, selpar1, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
    rppar1 = con.execute(selpar1).fetchall()
    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): rppar1 → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, rppar1, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})

    selpar2 = select([params_services]).order_by(params_services.c.servicesID)
    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): selpar2 → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, selpar2, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
    rppar2 = con.execute(selpar2).fetchall()
    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): rppar2 → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, rppar2, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})

    selmat=select([calculaties, cluster_artikelen, artikelen]).where(and_(\
            calculaties.c.calculatie == mcalnr,\
            calculaties.c.clusterID == cluster_artikelen.c.clusterID,\
            cluster_artikelen.c.artikelID == artikelen.c.artikelID))
    rpmat = con.execute(selmat)
    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): rpmat → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, rpmat, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): updcalmat → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, updcalmat, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
    for rij in rpmat:
        updcalmat = update(calculaties).where(and_(calculaties.c.calculatie ==\
           mcalnr, calculaties.c.clusterID == rij[1],\
           cluster_artikelen.c.artikelID == rij[9])).values(\
           materialen = calculaties.c.materialen+rij[2]*rij[8]*rij[10]*(1+rppar[6][1]))
        logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): materialen → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, materialen, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
        logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): uren_telecom → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, uren_telecom, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
        con.execute(updcalmat)
   
    metadata = MetaData()
    calculaties = Table('calculaties', metadata,
        Column('omschrijving', String),
        Column('werkomschrijving', String),
        Column('calcID', Integer(), primary_key=True),
        Column('calculatie', Integer),
        Column('clusterID', None, ForeignKey('clusters.clusterID')),
        Column('verwerkt', Integer),
        Column('hoeveelheid', Float),
        Column('eenheid', String),
        Column('koppelnummer', Integer),
        Column('prijs', Float),
        Column('materialen', Float),
        Column('lonen', Float),
        Column('diensten', Float),
        Column('materieel', Float),
        Column('inhuur', Float),
        Column('uren_constr', Float),
        Column('uren_mont', Float),
        Column('uren_retourlas', Float),
        Column('uren_telecom', Float),
        Column('uren_bfi', Float),
        Column('uren_voeding', Float),
        Column('uren_bvl', Float),
        Column('uren_inhuur', Float),
        Column('uren_spoorleg', Float),
        Column('uren_spoorlas', Float),
        Column('uren_inhuur', Float),
        Column('sleuvengraver', Float),
        Column('persapparaat', Float),
        Column('atlaskraan', Float),
        Column('kraan_groot', Float),
        Column('mainliner', Float),
        Column('hormachine', Float),
        Column('wagon', Float),
        Column('locomotor', Float),
        Column('locomotief', Float),
        Column('montagewagen', Float),
        Column('stormobiel', Float),
        Column('robeltrein', Float),
        Column('leiding', Float),
        Column('huisvesting', Float),
        Column('kabelwerk', Float),
        Column('grondverzet', Float),
        Column('betonwerk', Float),
        Column('vervoer', Float),
        Column('overig', Float))
    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): uren_retourlas → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, uren_retourlas, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
    clusters = Table('clusters', metadata,
        Column('clusterID', Integer(), primary_key=True),
        Column('omschrijving', String),
        Column('prijs', Float),
        Column('eenheid', String),
        Column('materialen', Float),
        Column('lonen', Float),
        Column('diensten', Float),
        Column('materieel', Float),
        Column('inhuur', Float),
        Column('uren_constr', Float),
        Column('uren_mont', Float),
        Column('uren_retourlas', Float),
        Column('uren_telecom', Float),
        Column('uren_bfi', Float),
        Column('uren_voeding', Float),
        Column('uren_bvl', Float),
        Column('uren_spoorleg', Float),
        Column('uren_spoorlas', Float),
        Column('uren_inhuur', Float),
        Column('sleuvengraver', Float),
        Column('persapparaat', Float),
        Column('atlaskraan', Float),
        Column('kraan_groot', Float),
        Column('mainliner', Float),
        Column('hormachine', Float),
        Column('wagon', Float),
        Column('locomotor', Float),
        Column('locomotief', Float),
        Column('montagewagen', Float),
        Column('stormobiel', Float),
        Column('robeltrein', Float),
        Column('leiding', Float),
        Column('huisvesting', Float),
        Column('kabelwerk', Float),
        Column('grondverzet', Float),
        Column('betonwerk', Float),
        Column('vervoer', Float),
        Column('overig', Float))
    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): uren_mont → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, uren_mont, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
    cluster_artikelen = Table('cluster_artikelen', metadata,
        Column('cluster_artID',Integer, primary_key=True),
        Column('artikelID', None, ForeignKey('artikelen.artikelID')),
        Column('clusterID', None, ForeignKey('clusters.clusterID')),
        Column('hoeveelheid', Float))
    artikelen = Table('artikelen', metadata,
        Column('artikelID', Integer(), primary_key=True),
        Column('artikelomschrijving', String),
        Column('artikelprijs', Float),
        Column('art_eenheid', String))
    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): selclart → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, selclart, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
    materiaallijsten = Table('materiaallijsten', metadata,
        Column('matlijstID', Integer, primary_key=True),
        Column('calculatie', Integer),
        Column('hoeveelheid', Float),
        Column('artikelID', None, ForeignKey('artikelen.artikelID')),
        Column('artikelprijs', Float),
        Column('subtotaal', Float),
        Column('resterend', Float))

    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
    
    selcalc = select([calculaties, clusters]).where(and_(calculaties.c.calculatie == int(mcalnr),\
                    calculaties.c.clusterID == clusters.c.clusterID))
    rpcalc = con.execute(selcalc)
    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): rpcalc → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, rpcalc, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
    selclart = select([cluster_artikelen,artikelen]).where(and_(cluster_artikelen.c.\
      artikelID == artikelen.c.artikelID, calculaties.c.clusterID ==\
      cluster_artikelen.c.clusterID, calculaties.c.calculatie == (int(mcalnr))))\
      .order_by(cluster_artikelen.c.clusterID, cluster_artikelen.c.artikelID)
    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): uren_constr → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, uren_constr, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): updcalc → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, updcalc, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
    rpclart = con.execute(selclart)
    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): rpclart → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, rpclart, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
    for record in rpcalc:
        updcalc = update(calculaties).where(and_(calculaties.c.calculatie == record[3],\
           calculaties.c.clusterID == clusters.c.clusterID)).values(verwerkt = 1, \
           uren_constr = calculaties.c.uren_constr+(clusters.c.uren_constr*calculaties.c.hoeveelheid),\
           uren_mont = calculaties.c.uren_mont+(clusters.c.uren_mont*calculaties.c.hoeveelheid),\
           uren_retourlas = calculaties.c.uren_retourlas+(clusters.c.uren_retourlas*calculaties.c.hoeveelheid),\
           uren_telecom = calculaties.c.uren_telecom+(clusters.c.uren_telecom*calculaties.c.hoeveelheid),\
           uren_bfi = calculaties.c.uren_bfi+(clusters.c.uren_bfi*calculaties.c.hoeveelheid),\
           uren_voeding = calculaties.c.uren_voeding+(clusters.c.uren_voeding*calculaties.c.hoeveelheid),\
           uren_bvl = calculaties.c.uren_bvl+(clusters.c.uren_bvl*calculaties.c.hoeveelheid),\
           uren_spoorleg = calculaties.c.uren_spoorleg+(clusters.c.uren_spoorleg*calculaties.c.hoeveelheid),\
           uren_spoorlas = calculaties.c.uren_spoorlas+(clusters.c.uren_spoorlas*calculaties.c.hoeveelheid),\
           uren_inhuur = calculaties.c.uren_inhuur+(clusters.c.uren_inhuur*calculaties.c.hoeveelheid),\
           sleuvengraver = calculaties.c.sleuvengraver+(clusters.c.sleuvengraver*calculaties.c.hoeveelheid),\
           persapparaat = calculaties.c.persapparaat+(clusters.c.persapparaat*calculaties.c.hoeveelheid),\
           atlaskraan = calculaties.c.atlaskraan+(clusters.c.atlaskraan*calculaties.c.hoeveelheid),\
           kraan_groot = calculaties.c.kraan_groot+(clusters.c.kraan_groot*calculaties.c.hoeveelheid),\
           mainliner = calculaties.c.mainliner+(clusters.c.mainliner*calculaties.c.hoeveelheid),\
           hormachine = calculaties.c.hormachine+(clusters.c.hormachine*calculaties.c.hoeveelheid),\
           wagon = calculaties.c.wagon+(clusters.c.wagon*calculaties.c.hoeveelheid),\
           locomotor = calculaties.c.locomotor+(clusters.c.locomotor*calculaties.c.hoeveelheid),\
           locomotief = calculaties.c.locomotief+(clusters.c.locomotief*calculaties.c.hoeveelheid),\
           montagewagen = calculaties.c.montagewagen+(clusters.c.montagewagen*calculaties.c.hoeveelheid),\
           stormobiel = calculaties.c.stormobiel+(clusters.c.stormobiel*calculaties.c.hoeveelheid),\
           robeltrein = calculaties.c.robeltrein+(clusters.c.robeltrein*calculaties.c.hoeveelheid))
        logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): uren_bfi → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, uren_bfi, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
        logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): uren_voeding → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, uren_voeding, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
        con.execute(updcalc)
        updcal1 = update(calculaties).where(and_(calculaties.c.calculatie == record[3], \
                         calculaties.c.clusterID == clusters.c.clusterID)).values( \
          lonen=calculaties.c.uren_constr*rppar1[1][1] * rppar1[1][2] + \
            calculaties.c.uren_mont * rppar1[2][1] * rppar1[2][2]+ \
            calculaties.c.uren_retourlas * rppar1[8][1] * rppar1[8][2] + \
            calculaties.c.uren_telecom * rppar1[10][1] * rppar1[10][2] + \
            calculaties.c.uren_bfi * rppar1[3][1] * rppar1[3][2] + \
            calculaties.c.uren_voeding * rppar1[4][1] * rppar1[4][2] + \
            calculaties.c.uren_bvl * rppar1[5][1] * rppar1[5][2] + \
            calculaties.c.uren_spoorleg * rppar1[6][1]  * rppar1[6][2]+ \
            calculaties.c.uren_spoorlas * rppar1[7][1] * rppar1[7][2],\
         inhuur=calculaties.c.uren_inhuur * rppar1[0][1] * rppar[0][2],
         materieel=calculaties.c.sleuvengraver * rppar2[0][1] * rppar2[0][2] + \
              calculaties.c.persapparaat * rppar2[1][1] * rppar2[1][2] + \
              calculaties.c.atlaskraan * rppar2[2][1] * rppar2[2][2] + \
              calculaties.c.kraan_groot * rppar2[3][1] * rppar2[3][2] + \
              calculaties.c.mainliner  * rppar2[4][1] * rppar2[4][1] + \
              calculaties.c.hormachine * rppar2[5][1] * rppar2[5][2] +
              calculaties.c.wagon * rppar2[6][1] * rppar2[6][2] + \
              calculaties.c.locomotor * rppar2[7][1] * rppar2[7][2] + \
              calculaties.c.locomotief * rppar2[8][1] * rppar2[8][2] + \
              calculaties.c.montagewagen * rppar2[9][1] * rppar2[9][2] + \
              calculaties.c.stormobiel * rppar2[10][1] * rppar2[10][2] + \
              calculaties.c.robeltrein * rppar2[11][1] * rppar2[11][2], \
         diensten=calculaties.c.leiding + clusters.c.leiding + \
              calculaties.c.huisvesting + clusters.c.huisvesting + \
              calculaties.c.kabelwerk + clusters.c.kabelwerk + \
              calculaties.c.grondverzet + clusters.c.grondverzet + \
              calculaties.c.betonwerk + clusters.c.betonwerk + \
              calculaties.c.vervoer + clusters.c.vervoer + \
              calculaties.c.overig + clusters.c.overig)
        logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): uren_bvl → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, uren_bvl, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
        logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): uren_spoorleg → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, uren_spoorleg, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
        logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): uren_spoorlas → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, uren_spoorlas, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
        con.execute(updcal1)
        for row in rpclart:
            selart = select([materiaallijsten.c.artikelID, materiaallijsten.c.calculatie]).where(and_(materiaallijsten.\
                c.artikelID == row[1], materiaallijsten.c.calculatie == record[3]))
            logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): uren_inhuur → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, uren_inhuur, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
            logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): sleuvengraver → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, sleuvengraver, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
            logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): persapparaat → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, persapparaat, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
            rpart = con.execute(selart).first()
            if rpart:
                updmatlijst = update(materiaallijsten).where(and_(materiaallijsten.c.\
                  artikelID == row[1], materiaallijsten.c.calculatie == record[3]))\
                 .values(hoeveelheid = materiaallijsten.c.hoeveelheid+(record[6]*row[3]),\
                artikelprijs = row[6]*(1+rppar[6][1]), subtotaal = materiaallijsten.\
                c.subtotaal+record[6]*row[3]*row[6]*(1+rppar[6][1]))
                logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): kraan_groot → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, kraan_groot, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
                logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): atlaskraan → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, atlaskraan, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
                logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): mainliner → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, mainliner, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
                logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): hormachine → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, hormachine, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
                logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): wagon → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, wagon, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
                logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): locomotor → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, locomotor, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
                con.execute(updmatlijst)
            elif not rpart:
                try:
                    mmatlijstnr = (con.execute(select([func.max(materiaallijsten.c.matlijstID,\
                        type_=Integer)])).scalar())
                    mmatlijstnr += 1
                except:
                    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): montagewagen → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, montagewagen, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
                    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): locomotief → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, locomotief, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
                    logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): stormobiel → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, stormobiel, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
                    mmatlijstnr = 1
                insmatlijst = insert(materiaallijsten).values(matlijstID = mmatlijstnr,\
                    calculatie = record[3], artikelID = row[1],\
                    hoeveelheid = record[6]*row[3], resterend = record[6]*row[3],\
                    artikelprijs = row[6]*(1+rppar[6][1]),\
                    subtotaal = record[6]*row[3]*row[6]*(1+rppar[6][1]))
                logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): robeltrein → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, robeltrein, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
                logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): updcal1 → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, updcal1, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
                con.execute(insmatlijst)
        selber = select([calculaties.c.calcID, calculaties.c.calculatie])\
                           .where(calculaties.c.calculatie == mcalnr)
        logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): selart → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, selart, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
        logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): rpart → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, rpart, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
        rpselber = con.execute(selber)
        for regel in rpselber:
            updber = update(calculaties).where(calculaties.c.calculatie==mcalnr)\
             .values(prijs=calculaties.c.materialen+calculaties.c.materieel+\
              calculaties.c.lonen+calculaties.c.diensten, werkomschrijving = mwerkomschr)
            logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): updmatlijst → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, updmatlijst, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
            logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): type_ → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, type_, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
            logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): artikelprijs → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, artikelprijs, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
            logger.debug("opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s): mmatlijstnr → %s", mcalnr, mwerkomschr, mverw, mwerknr, m_email, mmatlijstnr, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})
            con.execute(updber)
    opvragenCalc(mcalnr, mwerkomschr, mverw, mwerknr, m_email)
    logger.debug("<<< Exiting opbouwRp(mcalnr=%s,mwerkomschr=%s,mverw=%s,mwerknr=%s,m_email=%s)", mcalnr, mwerkomschr, mverw, mwerknr, m_email, extra={"event.action": "opbouwRp", "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr, "logrite.mverw": mverw, "logrite.mwerknr": mwerknr})

def printCalculatie(mcalnr, mwerknr):
    from sys import platform
    logger.warning(">>> Entering printCalculatie(mcalnr=%s,mwerknr=%s)", mcalnr, mwerknr, extra={"event.action": "printCalculatie", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    metadata = MetaData()
    logger.debug("printCalculatie(mcalnr=%s,mwerknr=%s): metadata → %s", mcalnr, mwerknr, metadata, extra={"event.action": "printCalculatie", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    calculaties = Table('calculaties', metadata,
        Column('calcID', Integer(), primary_key=True),
        Column('clusterID', None, ForeignKey('clusters.clusterID')),
        Column('koppelnummer', Integer),
        Column('calculatie', Integer),
        Column('omschrijving', String),
        Column('hoeveelheid', Float),
        Column('eenheid', String),
        Column('prijs', Float),
        Column('materialen', Float),
        Column('lonen', Float),
        Column('diensten', Float),
        Column('materieel', Float),
        Column('werkomschrijving', String))
    
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("printCalculatie(mcalnr=%s,mwerknr=%s): engine → %s", mcalnr, mwerknr, engine, extra={"event.action": "printCalculatie", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    con = engine.connect()
    logger.debug("printCalculatie(mcalnr=%s,mwerknr=%s): con → %s", mcalnr, mwerknr, con, extra={"event.action": "printCalculatie", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    
    selcal = select([calculaties]).where(calculaties.c.calculatie == mcalnr)
    logger.debug("printCalculatie(mcalnr=%s,mwerknr=%s): selcal → %s", mcalnr, mwerknr, selcal, extra={"event.action": "printCalculatie", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    rpcal = con.execute(selcal)
    logger.debug("printCalculatie(mcalnr=%s,mwerknr=%s): rpcal → %s", mcalnr, mwerknr, rpcal, extra={"event.action": "printCalculatie", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})

    mblad = 1
    logger.debug("printCalculatie(mcalnr=%s,mwerknr=%s): mblad → %s", mcalnr, mwerknr, mblad, extra={"event.action": "printCalculatie", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    rgl = 0
    mmat = 0
    logger.debug("printCalculatie(mcalnr=%s,mwerknr=%s): mmat → %s", mcalnr, mwerknr, mmat, extra={"event.action": "printCalculatie", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    mlon = 0
    logger.debug("printCalculatie(mcalnr=%s,mwerknr=%s): mlon → %s", mcalnr, mwerknr, mlon, extra={"event.action": "printCalculatie", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    mmater = 0
    logger.debug("printCalculatie(mcalnr=%s,mwerknr=%s): mmater → %s", mcalnr, mwerknr, mmater, extra={"event.action": "printCalculatie", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    minh = 0
    logger.debug("printCalculatie(mcalnr=%s,mwerknr=%s): minh → %s", mcalnr, mwerknr, minh, extra={"event.action": "printCalculatie", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    mtotaal = 0
    logger.debug("printCalculatie(mcalnr=%s,mwerknr=%s): mtotaal → %s", mcalnr, mwerknr, mtotaal, extra={"event.action": "printCalculatie", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    for row in rpcal:
        if rgl == 0 or rgl%55 == 0:
            if platform == 'win32':
                filename = '.\\forms\\Extern_Clustercalculaties\\clustercalculatie-'+str(row[3])+'-'+str(row[2])+'.txt'
            else:
                filename = './forms/Extern_Clustercalculaties/clustercalculatie-'+str(row[3])+'-'+str(row[2])+'.txt'
                logger.debug("printCalculatie(mcalnr=%s,mwerknr=%s): filename → %s", mcalnr, mwerknr, filename, extra={"event.action": "printCalculatie", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
            kop=\
    ('Werknummer: '+str(mwerknr)+' '+'{:<24.24s}'.format(str(row[12]))+'  Calculatie: '+str(row[3])+'  Datum: '+str(datetime.datetime.now())[0:10]+'  Blad : '+str(mblad)+'\n'+
    '=====================================================================================================\n'+
    'Cluster  Cluster             Eenheid Aantal  Materialen      Lonen  Materieel     Diensten   Bedrag  \n'+
    '=====================================================================================================\n')
            logger.debug("printCalculatie(mcalnr=%s,mwerknr=%s): kop → %s", mcalnr, mwerknr, kop, extra={"event.action": "printCalculatie", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
            if rgl == 0:
                open(filename, 'w').write(kop)
            elif rgl%55 == 0:
                open(filename, 'a').write(kop)
            mblad += 1
        open(filename,'a').write('{:<9s}'.format(row[1])+'{:<22.21s}'.format(row[4])+'{:<6s}'.format(row[6])+'{:5.2f}'.format(row[5])+'  '+'{:11.2f}'.format(row[8])+'{:11.2f}'.format(row[9])+'{:11.2f}'.format(row[11])+'{:11.2f}'.format(row[10])+'{:12.2f}'.format(row[7])+'\n')
        mmat = mmat+row[8]
        mlon = mlon+row[9]
        mmater = mmater+row[11]
        minh = minh+row[10]
        mtotaal = mtotaal+row[7]
        rgl += 1
    tail =(\
    '-------------------------------------------------------------------------------------------------------\n'+
    'Totalen                                     '+'{:11.2f}'.format(mmat)+'{:11.2f}'.format(mlon)+'{:11.2f}'.format(mmater)+'{:11.2f}'.format(minh)+'{:12.2f}'.format(mtotaal)+'\n'
    '=======================================================================================================\n')
    open(filename,'a').write(tail)
    if platform == 'win32':
        os.startfile(filename, "print")
    else:
        os.system("lpr "+filename)
    printing()
    logger.debug("<<< Exiting printCalculatie(mcalnr=%s,mwerknr=%s)", mcalnr, mwerknr, extra={"event.action": "printCalculatie", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})

def printArtikellijst(mcalnr, mwerknr):
    logger.warning(">>> Entering printArtikellijst(mcalnr=%s,mwerknr=%s)", mcalnr, mwerknr, extra={"event.action": "printArtikellijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    from sys import platform
    metadata = MetaData()
    logger.debug("printArtikellijst(mcalnr=%s,mwerknr=%s): metadata → %s", mcalnr, mwerknr, metadata, extra={"event.action": "printArtikellijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    materiaallijsten = Table('materiaallijsten', metadata,
         Column('matlijstID', Integer, primary_key=True),
         Column('calculatie', Integer),
         Column('artikelID', None, ForeignKey('artikelen.artikelID')),
         Column('artikelprijs', Float),
         Column('hoeveelheid', Float),
         Column('subtotaal', Float))
    artikelen = Table('artikelen', metadata,
         Column('artikelID', Integer(), primary_key=True),
         Column('artikelomschrijving', String),
         Column('art_eenheid', String),
         Column('locatie_magazijn', String))
    calculaties = Table('calculaties', metadata,
        Column('calculatie', Integer),
        Column('koppelnummer', Integer))
                                    
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("printArtikellijst(mcalnr=%s,mwerknr=%s): engine → %s", mcalnr, mwerknr, engine, extra={"event.action": "printArtikellijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    con = engine.connect()
    logger.debug("printArtikellijst(mcalnr=%s,mwerknr=%s): con → %s", mcalnr, mwerknr, con, extra={"event.action": "printArtikellijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    
    selmat = select([materiaallijsten, artikelen])\
      .where(and_(materiaallijsten.c.artikelID == artikelen.c.artikelID,\
      materiaallijsten.c.artikelID == artikelen.c.artikelID,\
      materiaallijsten.c.calculatie == mcalnr)).order_by(materiaallijsten.c.artikelID)
    logger.debug("printArtikellijst(mcalnr=%s,mwerknr=%s): selmat → %s", mcalnr, mwerknr, selmat, extra={"event.action": "printArtikellijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    rpmat = con.execute(selmat)
    logger.debug("printArtikellijst(mcalnr=%s,mwerknr=%s): rpmat → %s", mcalnr, mwerknr, rpmat, extra={"event.action": "printArtikellijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    selkop = select([calculaties]).where(calculaties.c.calculatie == mcalnr)
    logger.debug("printArtikellijst(mcalnr=%s,mwerknr=%s): selkop → %s", mcalnr, mwerknr, selkop, extra={"event.action": "printArtikellijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    rpkop = con.execute(selkop).first()
    logger.debug("printArtikellijst(mcalnr=%s,mwerknr=%s): rpkop → %s", mcalnr, mwerknr, rpkop, extra={"event.action": "printArtikellijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    mblad = 1
    logger.debug("printArtikellijst(mcalnr=%s,mwerknr=%s): mblad → %s", mcalnr, mwerknr, mblad, extra={"event.action": "printArtikellijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    rgl = 0
    for row in rpmat:
        if rgl == 0 or rgl%55 == 0:
            if platform == 'win32':
                filename = '.\\forms\\Extern_Clustercalculaties\\materiaallijst-'+str(rpkop[0])+'-'+str(rpkop[1])+'.txt'
            else:
                filename = './forms/Extern_Clustercalculaties/materiaallijst-'+str(rpkop[0])+'-'+str(rpkop[1])+'.txt'
                logger.debug("printArtikellijst(mcalnr=%s,mwerknr=%s): filename → %s", mcalnr, mwerknr, filename, extra={"event.action": "printArtikellijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
            kop=\
    ('Werknummer:   '+str(mwerknr)+'  Calculatie: '+str(rpkop[0])+'   Datum: '+str(datetime.datetime.now())[0:10]+'  Blad :  '+str(mblad)+'\n'+
    '=============================================================================================\n'+
    'Artikelnr  Cluster                             Eenheid       Prijs      Aantal               \n'+
    '=============================================================================================\n')
            logger.debug("printArtikellijst(mcalnr=%s,mwerknr=%s): kop → %s", mcalnr, mwerknr, kop, extra={"event.action": "printArtikellijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
            if rgl == 0:
                open(filename, 'w').write(kop)
            elif rgl%55 == 0:
                open(filename, 'a').write(kop)
            mblad += 1
            
        open(filename,'a').write('{:<11d}'.format(row[6])+'{:<37.35s}'.format(row[7])+'{:<8.6s}'.format(row[8])+'{:10.2f}'.format(row[3])+'  '+'{:10.2f}'.format(row[4])+'\n')
        rgl += 1
    if platform == 'win32':
        os.startfile(filename, "print")
    else:
        os.system("lpr "+filename)
    printing()
    logger.debug("<<< Exiting printArtikellijst(mcalnr=%s,mwerknr=%s)", mcalnr, mwerknr, extra={"event.action": "printArtikellijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    
def printDienstenlijst(mcalnr, mwerknr):
    logger.warning(">>> Entering printDienstenlijst(mcalnr=%s,mwerknr=%s)", mcalnr, mwerknr, extra={"event.action": "printDienstenlijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    if mwerknr == 0:
        foutWerknr()
        return
    from sys import platform
    metadata = MetaData()               
    logger.debug("printDienstenlijst(mcalnr=%s,mwerknr=%s): metadata → %s", mcalnr, mwerknr, metadata, extra={"event.action": "printDienstenlijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    calculaties = Table('calculaties', metadata,
        Column('calcID', Integer(), primary_key=True),
        Column('omschrijving', String),
        Column('werkomschrijving', String),
        Column('calculatie', Integer),
        Column('clusterID', None, ForeignKey('clusters.clusterID')),
        Column('hoeveelheid', Float),
        Column('eenheid', String),
        Column('koppelnummer', Integer),
        Column('prijs', Float),
        Column('materialen', Float),
        Column('lonen', Float),
        Column('diensten', Float),
        Column('materieel', Float),
        Column('inhuur', Float), 
        Column('uren_inhuur', Float),
        Column('sleuvengraver', Float),
        Column('persapparaat', Float),
        Column('atlaskraan', Float),
        Column('kraan_groot', Float),
        Column('mainliner', Float),
        Column('hormachine', Float),
        Column('wagon', Float),
        Column('locomotor', Float),
        Column('locomotief', Float),
        Column('montagewagen', Float),
        Column('stormobiel', Float),
        Column('robeltrein', Float),
        Column('leiding', Float),
        Column('huisvesting', Float),
        Column('kabelwerk', Float),
        Column('grondverzet', Float),
        Column('betonwerk', Float),
        Column('vervoer', Float),
        Column('overig', Float))
    params_finance = Table('params_finance', metadata,
        Column('financeID', Integer, primary_key=True),
        Column('factor', Float),
        Column('amount', Float))
    params_hours = Table('params_hours', metadata,
        Column('rateID', Integer, primary_key=True),
        Column('hourly_tariff', Float),
        Column('overhead_factor', Float),
        Column('wageID', None, ForeignKey('lonen.loonID')),
        Column('travel_time', Float))
    params_services = Table('params_services', metadata,
        Column('servicesID', Integer, primary_key=True),
        Column('hourly_tariff', Float),
        Column('overhead_factor', Float))

    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("printDienstenlijst(mcalnr=%s,mwerknr=%s): engine → %s", mcalnr, mwerknr, engine, extra={"event.action": "printDienstenlijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    con = engine.connect()
    logger.debug("printDienstenlijst(mcalnr=%s,mwerknr=%s): con → %s", mcalnr, mwerknr, con, extra={"event.action": "printDienstenlijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    selpar = select([params_finance]).order_by(params_finance.c.financeID)
    logger.debug("printDienstenlijst(mcalnr=%s,mwerknr=%s): selpar → %s", mcalnr, mwerknr, selpar, extra={"event.action": "printDienstenlijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    rppar = con.execute(selpar).fetchall()
    logger.debug("printDienstenlijst(mcalnr=%s,mwerknr=%s): rppar → %s", mcalnr, mwerknr, rppar, extra={"event.action": "printDienstenlijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})

    selpar1 = select([params_hours]).order_by(params_hours.c.rateID)
    logger.debug("printDienstenlijst(mcalnr=%s,mwerknr=%s): selpar1 → %s", mcalnr, mwerknr, selpar1, extra={"event.action": "printDienstenlijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    rppar1 = con.execute(selpar1).fetchall()
    logger.debug("printDienstenlijst(mcalnr=%s,mwerknr=%s): rppar1 → %s", mcalnr, mwerknr, rppar1, extra={"event.action": "printDienstenlijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})

    selpar2 = select([params_services]).order_by(params_services.c.servicesID)
    logger.debug("printDienstenlijst(mcalnr=%s,mwerknr=%s): selpar2 → %s", mcalnr, mwerknr, selpar2, extra={"event.action": "printDienstenlijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    rppar2 = con.execute(selpar2).fetchall()
    logger.debug("printDienstenlijst(mcalnr=%s,mwerknr=%s): rppar2 → %s", mcalnr, mwerknr, rppar2, extra={"event.action": "printDienstenlijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})

    selcal = select([calculaties]).where(calculaties.c.koppelnummer == mwerknr).\
    order_by(calculaties.c.clusterID)
    rpcal = con.execute(selcal)
    logger.debug("printDienstenlijst(mcalnr=%s,mwerknr=%s): rpcal → %s", mcalnr, mwerknr, rpcal, extra={"event.action": "printDienstenlijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    
    mblad = 1
    logger.debug("printDienstenlijst(mcalnr=%s,mwerknr=%s): mblad → %s", mcalnr, mwerknr, mblad, extra={"event.action": "printDienstenlijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    rgl = 0
    m_uren = 0
    logger.debug("printDienstenlijst(mcalnr=%s,mwerknr=%s): m_uren → %s", mcalnr, mwerknr, m_uren, extra={"event.action": "printDienstenlijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    mtotaal = 0
    logger.debug("printDienstenlijst(mcalnr=%s,mwerknr=%s): mtotaal → %s", mcalnr, mwerknr, mtotaal, extra={"event.action": "printDienstenlijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    
    header = ['Inhuur','Sleuvengraver','Persapparaat','Atlaskraan','Kraan Groot',\
          'Mainliner','Hormachine','Wagon','Locomotor','Locomotief','Montagewagen',\
          'Stormobiel','Robeltrein','Leiding','Huisvesting','Kabelwerk',\
          'Grondverzet','Betonwerk','Vervoer','Overig']   
    
    for row in rpcal:
        if row[7] == 0:
            foutWerknr()
            logger.debug("<<< Exiting printDienstenlijst(mcalnr=%s,mwerknr=%s)", mcalnr, mwerknr, extra={"event.action": "printDienstenlijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
            return
        if rgl == 0 or rgl%55 == 0:
            if platform == 'win32':
                filename = '.\\forms\\Extern_Clustercalculaties_Diensten\\clustercalculatie_'+str(row[2]).replace(' ', '_')+'.txt'
            else:
                filename = './forms/Extern_Clustercalculaties_Diensten/clustercalculatie_'+str(row[2]).replace(' ', '_')+'.txt'
                logger.debug("printDienstenlijst(mcalnr=%s,mwerknr=%s): filename → %s", mcalnr, mwerknr, filename, extra={"event.action": "printDienstenlijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
            kop=\
    ('Bestellijst intern voor Inkooporders bestellingen / reserveringen Diensten en Materiëel,\nWerknummer: '+str(mwerknr)+' '+'{:<24.24s}'.format(str(row[2]))+' Calculatie: '+str(row[3])+\
     '  Datum: '+str(datetime.datetime.now())[0:10]+'  Blad : '+str(mblad)+'\n'+
    '=====================================================================================================\n'+
    'Cluster Clusteromschrijving     Aantal Eenheid Omschrijving-Dienst   Uren-Sub  Bedrag-Sub Levertermijn\n'+
    '=====================================================================================================\n')
            logger.debug("printDienstenlijst(mcalnr=%s,mwerknr=%s): kop → %s", mcalnr, mwerknr, kop, extra={"event.action": "printDienstenlijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
            if rgl == 0:                 
                open(filename, 'w').write(kop)
            elif rgl%55 == 0:
                open(filename, 'a').write(kop)
            mblad += 1
        for k in range(14, 34):
            dienst = header[k - 14]
            logger.debug("printDienstenlijst(mcalnr=%s,mwerknr=%s): dienst → %s", mcalnr, mwerknr, dienst, extra={"event.action": "printDienstenlijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
            if k == 14:
                uren = row[k]
                logger.debug("printDienstenlijst(mcalnr=%s,mwerknr=%s): uren → %s", mcalnr, mwerknr, uren, extra={"event.action": "printDienstenlijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
                bedrag = row[k] * rppar1[0][1] * rppar1[0][2]
            elif k < 27:
                uren = row[k]
                bedrag = row[k] * rppar2[k-15][1] * rppar2[k-15][2]
                logger.debug("printDienstenlijst(mcalnr=%s,mwerknr=%s): bedrag → %s", mcalnr, mwerknr, bedrag, extra={"event.action": "printDienstenlijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
            else:
                bedrag = row[k]

            if row[k]:
                open(filename, 'a').write('{:<8s}'.format(row[4]) + '{:<23.20s}'.format(row[1]) + \
                                          '{:>8.2f}'.format(row[5]) + ' {:>6s}'.format(row[6]) + '  {:<18s}'.format(
                    dienst) + \
                                          '{:>12.2f}'.format(uren) + '{:>12.2f}'.format(bedrag) + ' {:>10s}'.format(
                    'Agree' + '\n'))
                if k < 27:
                    m_uren = m_uren + row[k]
                    mtotaal = mtotaal + row[k] * rppar2[k-15][1]
                else:
                    mtotaal = mtotaal + row[k]
        rgl += 1
    tail =(\
     '-----------------------------------------------------------------------------------------------------\n'+
    'Totalen                                                           '+'{:11.2f}'.format(m_uren)+'{:12.2f}'.format(mtotaal)+'\n'+
    '=====================================================================================================\n')    
    open(filename,'a').write(tail)
    if platform == 'win32':
        os.startfile(filename, "print")
    else:
        os.system("lpr "+filename)
    printing()

def toonCalculatie(mcalnr, mwerknr):
    logger.warning(">>> Entering toonCalculatie(mcalnr=%s,mwerknr=%s)", mcalnr, mwerknr, extra={"event.action": "toonCalculatie", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    class MyWindow(QDialog):
        def __init__(self, data_list, header, *args):
            QWidget.__init__(self, *args,)
            self.setGeometry(50, 50, 1500, 900)
            self.setWindowTitle('Clustercalculatie')
            self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
            self.setWindowFlags(self.windowFlags()| Qt.WindowSystemMenuHint |
                              Qt.WindowMinMaxButtonsHint)
            table_model = MyTableModel(self, data_list, header)
            table_view = QTableView()
            table_view.setModel(table_model)
            font = QFont("Arial", 10)
            table_view.setFont(font)
            table_view.hideColumn(1)
            table_view.resizeColumnsToContents()
            table_view.setSelectionBehavior(QTableView.SelectRows)
            #table_view.clicked.connect(selectRow)
            table_view.clicked.connect(ShowSelection)
            layout = QVBoxLayout(self)
            layout.addWidget(table_view)
            self.setLayout(layout)
    
    class MyTableModel(QAbstractTableModel):
        def __init__(self, parent, mylist, header, *args):
            logger.warning(">>> Entering __init__(parent=%s,mylist=%s,header=%s)", parent, mylist, header, extra={"event.action": "__init__", "logrite.mylist": mylist})
            logger.debug("__init__(self=%s,parent=%s,mylist=%s,header=%s): self.mylist → %s", self, parent, mylist, header, self.mylist, extra={"event.action": "__init__", "logrite.mylist": mylist})
            logger.debug("__init__(self=%s,parent=%s,mylist=%s,header=%s): self.header → %s", self, parent, mylist, header, self.header, extra={"event.action": "__init__", "logrite.mylist": mylist})
            QAbstractTableModel.__init__(self, parent, *args)
            self.mylist = mylist
            self.header = header
        def rowCount(self, parent):
            logger.warning(">>> Entering rowCount(parent=%s)", parent, extra={"event.action": "rowCount"})
            return len(self.mylist)
        def columnCount(self, parent):
            logger.warning(">>> Entering columnCount(parent=%s)", parent, extra={"event.action": "columnCount"})
            return len(self.mylist[0])
        def data(self, index, role):
            logger.warning(">>> Entering data(index=%s,role=%s)", index, role, extra={"event.action": "data", "logrite.index": index, "logrite.role": role})
            veld = self.mylist[index.row()][index.column()]
            logger.debug("data(index=%s,role=%s): veld → %s", index, role, veld, extra={"event.action": "data", "logrite.index": index, "logrite.role": role})
            logger.debug("data(self=%s,index=%s,role=%s): veld → %s", self, index, role, veld, extra={"event.action": "data", "logrite.index": index, "logrite.role": role})
            if not index.isValid():
                return None
            elif role == Qt.TextAlignmentRole and (type(veld) == float or type(veld) == int):
                return Qt.AlignRight | Qt.AlignVCenter
            elif role != Qt.DisplayRole:
                return None
            if type(veld) == float:
                return '{:12.2f}'.format(veld)
            else:
                logger.debug("<<< Exiting data(index=%s,role=%s)", index, role, extra={"event.action": "data", "logrite.index": index, "logrite.role": role})
                return veld
        def headerData(self, col, orientation, role):
            if orientation == Qt.Horizontal and role == Qt.DisplayRole:
                return self.header[col]
            return None
             
    header = ['ID','Cluster','Werkomschrijving','Calculatie','Clusternr',\
              'Verwerkt','Hoeveelheid','Eenheid', 'Koppelnr', 'Totaalprijs','Materialen',\
              'Lonen','Diensten','Materieel', 'Inhuur','Uren\nConstruktie','Uren\nMontage',\
              'Uren\nRetourlas', 'Uren\nTelecom', 'Uren\nBFI','Uren\nVoeding',\
              'Uren\nBovenleiding','Uren\nSpoorleg','Uren\nSpoorlas','Uren\nInhuur',\
              'Uren\nSleuvengraver','Uren\nPersapparaat', 'Uren\nAtlaskraan',\
              'Uren\nKraan_groot','Uren\nMainliner','Uren\nHormachine','Uren\nWagon',\
              'Uren\nLocomotor','Uren\nLocomotief','Uren\nMontagewagen','Uren\nStormobiel',\
              'Uren\nRobeltrein','Leiding', 'Huisvesting','Kabelwerk', 'Grondverzet',\
              'Betonwerk', 'Vervoer', 'Overig']

    metadata = MetaData()               
    calculaties = Table('calculaties', metadata,
        Column('calcID', Integer(), primary_key=True),
        Column('omschrijving', String),
        Column('werkomschrijving', String),
        Column('calculatie', Integer),
        Column('clusterID', None, ForeignKey('clusters.clusterID')),
        Column('verwerkt', Integer),
        Column('hoeveelheid', Float),
        Column('eenheid', String),
        Column('koppelnummer', Integer),
        Column('prijs', Float),
        Column('materialen', Float),
        Column('lonen', Float),
        Column('diensten', Float),
        Column('materieel', Float),
        Column('inhuur', Float),
        Column('uren_constr', Float),
        Column('uren_mont', Float),
        Column('uren_retourlas', Float),
        Column('uren_telecom', Float),
        Column('uren_bfi', Float),
        Column('uren_voeding', Float),
        Column('uren_bvl', Float),
        Column('uren_inhuur', Float),
        Column('uren_spoorleg', Float),
        Column('uren_spoorlas', Float),
        Column('uren_inhuur', Float),
        Column('sleuvengraver', Float),
        Column('persapparaat', Float),
        Column('atlaskraan', Float),
        Column('kraan_groot', Float),
        Column('mainliner', Float),
        Column('hormachine', Float),
        Column('wagon', Float),
        Column('locomotor', Float),
        Column('locomotief', Float),
        Column('montagewagen', Float),
        Column('stormobiel', Float),
        Column('robeltrein', Float),
        Column('leiding', Float),
        Column('huisvesting', Float),
        Column('kabelwerk', Float),
        Column('grondverzet', Float),
        Column('betonwerk', Float),
        Column('vervoer', Float),
        Column('overig', Float))
                                               
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
    
    selcal = select([calculaties]).where(calculaties.c.calculatie == mcalnr).\
     order_by(calculaties.c.clusterID)
    rpcal = con.execute(selcal)
      
    data_list=[]
    for row in rpcal:
        data_list += [(row)]
        
    def ShowSelection(idx):
        logger.warning(">>> Entering ShowSelection(idx=%s)", idx, extra={"event.action": "ShowSelection", "logrite.idx": idx})
        mcalnr = idx.data()
        logger.debug("ShowSelection(idx=%s): mcalnr → %s", idx, mcalnr, extra={"event.action": "ShowSelection", "logrite.idx": idx})
        if  idx.column() == 0:

            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            logger.debug("ShowSelection(idx=%s): engine → %s", idx, engine, extra={"event.action": "ShowSelection", "logrite.idx": idx})
            con = engine.connect()
            logger.debug("ShowSelection(idx=%s): con → %s", idx, con, extra={"event.action": "ShowSelection", "logrite.idx": idx})
            selcal = select([calculaties]).where(calculaties.c.calcID == mcalnr)
            rpcal = con.execute(selcal).first()
            logger.debug("ShowSelection(idx=%s): selcal → %s", idx, selcal, extra={"event.action": "ShowSelection", "logrite.idx": idx})
            logger.debug("ShowSelection(idx=%s): rpcal → %s", idx, rpcal, extra={"event.action": "ShowSelection", "logrite.idx": idx})
                                                      
            class MainWindow(QDialog):
                logger.debug("<<< Exiting ShowSelection(idx=%s)", idx, extra={"event.action": "ShowSelection", "logrite.idx": idx})
                def __init__(self):
                    QDialog.__init__(self)
                    
                    grid = QGridLayout()
                    grid.setSpacing(10)
                    
                    self.setWindowTitle("Opvragen Clustercalculatie")
                    self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
                    
                    self.setFont(QFont('Arial', 10))   
                                                      
                    self.lbl = QLabel()
                    self.pixmap = QPixmap('./images/logos/verbinding.jpg')
                    self.lbl.setPixmap(self.pixmap)
                    grid.addWidget(self.lbl , 0, 0)
                    
                    grid.addWidget(QLabel('Opvragen Clustercalculatie'),0, 0, 1, 6, Qt.AlignCenter)
            
                    self.logo = QLabel()
                    self.pixmap = QPixmap('./images/logos/logo.jpg')
                    self.logo.setPixmap(self.pixmap)
                    grid.addWidget(self.logo , 0, 5, 1, 1, Qt.AlignRight)                
                    index = 3
                    for item in header:
                        horpos = index%3
                        verpos = index
                        if index%3 == 1:
                            verpos = index - 1
                        elif index%3 == 2:
                            verpos = index -2
                        self.lbl = QLabel(header[index-3])
                        
                        self.Gegevens = QLabel()
                        if type(rpcal[index-3]) == float:
                            q1Edit = QLineEdit('{:12.2f}'.format(rpcal[index-3]))
                            q1Edit.setAlignment(Qt.AlignRight)
                        elif type(rpcal[index-3]) == int:
                            q1Edit = QLineEdit(str(rpcal[index-3]))
                            q1Edit.setAlignment(Qt.AlignRight)
                        else:
                            q1Edit = QLineEdit(str(rpcal[index-3]))
                        q1Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                        if verpos == 3 and horpos > 0:
                            q1Edit.setFixedWidth(300)
                        else:
                            q1Edit.setFixedWidth(120)
                        q1Edit.setDisabled(True)
                        grid.addWidget(self.lbl, verpos, horpos+horpos%3)
                        grid.addWidget(q1Edit, verpos, horpos+horpos%3+1)
                        
                        index +=1
                        
                    terugBtn = QPushButton('Sluiten')
                    terugBtn.clicked.connect(self.accept)
            
                    grid.addWidget(terugBtn, verpos+1, 5, 1 , 1, Qt.AlignRight)
                    terugBtn.setFont(QFont("Arial",10))
                    terugBtn.setFixedWidth(100) 
                    terugBtn.setStyleSheet("color: black;  background-color: gainsboro")
                    
                    grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), verpos+2, 0, 1, 6, Qt.AlignCenter)
                                                                            
                    self.setLayout(grid)
                    self.setGeometry(300, 100, 150, 150)
                            
            mainWin = MainWindow()
            mainWin.exec_()
            mainWin.raise_()
            mainWin.activateWindow()
            
    win = MyWindow(data_list, header)
    win.exec_()
    
def toonDienstenlijst(mcalnr, mwerknr):
    logger.warning(">>> Entering toonDienstenlijst(mcalnr=%s,mwerknr=%s)", mcalnr, mwerknr, extra={"event.action": "toonDienstenlijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    class MyWindow(QDialog):
        def __init__(self, data_list, header, *args):
            logger.warning(">>> Entering __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})
            QWidget.__init__(self, *args,)
            self.setGeometry(50, 50, 1500, 900)
            self.setWindowTitle('Clustercalculatie')
            self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
            self.setWindowFlags(self.windowFlags()| Qt.WindowSystemMenuHint |
                              Qt.WindowMinMaxButtonsHint)
            table_model = MyTableModel(self, data_list, header)
            logger.debug("__init__(data_list=%s,header=%s): table_model → %s", data_list, header, table_model, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): table_model → %s", self, data_list, header, table_model, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(data_list=%s,header=%s): font → %s", data_list, header, font, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): font → %s", self, data_list, header, font, extra={"event.action": "__init__", "logrite.data_list": data_list})
            table_view = QTableView()
            logger.debug("__init__(self=%s,data_list=%s,header=%s): table_view → %s", self, data_list, header, table_view, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(data_list=%s,header=%s): table_view → %s", data_list, header, table_view, extra={"event.action": "__init__", "logrite.data_list": data_list})
            table_view.setModel(table_model)
            font = QFont("Arial", 10)
            table_view.setFont(font)
            table_view.hideColumn(1)
            table_view.hideColumn(12)
            table_view.hideColumn(15)
            table_view.hideColumn(16)
            table_view.hideColumn(17)
            table_view.hideColumn(18)
            table_view.hideColumn(19)
            table_view.hideColumn(20)
            table_view.hideColumn(21)
            table_view.resizeColumnsToContents()
            table_view.setSelectionBehavior(QTableView.SelectRows)
            #table_view.clicked.connect(selectRow)
            table_view.clicked.connect(showDienst)
            layout = QVBoxLayout(self)
            logger.debug("__init__(data_list=%s,header=%s): layout → %s", data_list, header, layout, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): layout → %s", self, data_list, header, layout, extra={"event.action": "__init__", "logrite.data_list": data_list})
            layout.addWidget(table_view)
            self.setLayout(layout)
            logger.debug("<<< Exiting __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})
    
    class MyTableModel(QAbstractTableModel):
        def __init__(self, parent, mylist, header, *args):
            QAbstractTableModel.__init__(self, parent, *args)
            self.mylist = mylist
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q1Edit → %s", parent, q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q1Edit → %s", self, parent, q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q2Edit → %s", parent, q2Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q2Edit → %s", self, parent, q2Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q3Edit → %s", parent, q3Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q3Edit → %s", self, parent, q3Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q4Edit → %s", parent, q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q4Edit → %s", self, parent, q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q5Edit → %s", parent, q5Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q5Edit → %s", self, parent, q5Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q8Edit → %s", parent, q8Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q8Edit → %s", self, parent, q8Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q9Edit → %s", parent, q9Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q9Edit → %s", self, parent, q9Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q11Edit → %s", parent, q11Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q11Edit → %s", self, parent, q11Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q12Edit → %s", parent, q12Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q12Edit → %s", self, parent, q12Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q13Edit → %s", parent, q13Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q13Edit → %s", self, parent, q13Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q19Edit → %s", parent, q19Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q19Edit → %s", self, parent, q19Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q14Edit → %s", parent, q14Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q14Edit → %s", self, parent, q14Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q15Edit → %s", parent, q15Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q15Edit → %s", self, parent, q15Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q16Edit → %s", parent, q16Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q16Edit → %s", self, parent, q16Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q17Edit → %s", parent, q17Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q17Edit → %s", self, parent, q17Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q20Edit → %s", parent, q20Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q20Edit → %s", self, parent, q20Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q21Edit → %s", parent, q21Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q21Edit → %s", self, parent, q21Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q22Edit → %s", parent, q22Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q22Edit → %s", self, parent, q22Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q23Edit → %s", parent, q23Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q23Edit → %s", self, parent, q23Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q24Edit → %s", parent, q24Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q24Edit → %s", self, parent, q24Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q26Edit → %s", parent, q26Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q26Edit → %s", self, parent, q26Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q27Edit → %s", parent, q27Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q27Edit → %s", self, parent, q27Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q28Edit → %s", parent, q28Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q28Edit → %s", self, parent, q28Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q29Edit → %s", parent, q29Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q29Edit → %s", self, parent, q29Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q30Edit → %s", parent, q30Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q30Edit → %s", self, parent, q30Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q31Edit → %s", parent, q31Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q31Edit → %s", self, parent, q31Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q32Edit → %s", parent, q32Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q32Edit → %s", self, parent, q32Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q33Edit → %s", parent, q33Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q33Edit → %s", self, parent, q33Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q34Edit → %s", parent, q34Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q34Edit → %s", self, parent, q34Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q35Edit → %s", parent, q35Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q35Edit → %s", self, parent, q35Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q36Edit → %s", parent, q36Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q36Edit → %s", self, parent, q36Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q37Edit → %s", parent, q37Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q37Edit → %s", self, parent, q37Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q38Edit → %s", parent, q38Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q38Edit → %s", self, parent, q38Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q39Edit → %s", parent, q39Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q39Edit → %s", self, parent, q39Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): grid → %s", parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl → %s", parent, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lblsoort → %s", parent, lblsoort, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lblsoort → %s", self, parent, lblsoort, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbluren → %s", parent, lbluren, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbluren → %s", self, parent, lbluren, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lblbedrag → %s", parent, lblbedrag, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lblbedrag → %s", self, parent, lblbedrag, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            self.header = header
        def rowCount(self, parent):
            return len(self.mylist)
        def columnCount(self, parent):
            return len(self.mylist[0])
        def data(self, index, role):
            veld = self.mylist[index.row()][index.column()]
            if not index.isValid():
                return None
            elif role == Qt.TextAlignmentRole and (type(veld) == float or type(veld) == int):
                return Qt.AlignRight | Qt.AlignVCenter
            elif role != Qt.DisplayRole:
                return None
            if type(veld) == float:
                return '{:12.2f}'.format(veld)
            else:
                return veld
        def headerData(self, col, orientation, role):
            if orientation == Qt.Horizontal and role == Qt.DisplayRole:
                return self.header[col]
            logger.warning(">>> Entering headerData(col=%s,orientation=%s,role=%s)", col, orientation, role, extra={"event.action": "headerData", "logrite.col": col, "logrite.orientation": orientation, "logrite.role": role})
            logger.debug("<<< Exiting headerData(col=%s,orientation=%s,role=%s)", col, orientation, role, extra={"event.action": "headerData", "logrite.col": col, "logrite.orientation": orientation, "logrite.role": role})
            return None
        
    header = ['ID','Cluster','Werkomschrijving','Calculatie','Clusternr',\
      'Verwerkt','Hoeveelheid','Eenheid', 'Koppelnr', 'Totaalprijs','Materialen',\
      'Lonen','','Materieel', 'Inhuur','', '','',\
      '','', 'r', '', 'Inhuur uren','Persapparaat',\
      'Sleuvengraver', 'Atlaskraan', 'Kraan Groot', 'Mainliner', 'Hormachine',\
      'Wagon', 'Locomotor', 'Locomotief', 'Montagewagen', 'Stormobiel', 'Robeltrein']

    metadata = MetaData()               
    calculaties = Table('calculaties', metadata,
        Column('calcID', Integer(), primary_key=True),
        Column('omschrijving', String),
        Column('werkomschrijving', String),
        Column('calculatie', Integer),
        Column('clusterID', None, ForeignKey('clusters.clusterID')),
        Column('verwerkt', Integer),
        Column('hoeveelheid', Float),
        Column('eenheid', String),
        Column('koppelnummer', Integer),
        Column('prijs', Float),
        Column('materialen', Float),
        Column('lonen', Float),
        Column('diensten', Float),
        Column('materieel', Float),
        Column('inhuur', Float),
        Column('leiding', Float),
        Column('huisvesting', Float),
        Column('kabelwerk', Float),
        Column('grondverzet', Float),
        Column('betonwerk', Float),
        Column('vervoer', Float),
        Column('overig', Float),
        Column('uren_inhuur', Float),
        Column('sleuvengraver', Float),
        Column('persapparaat', Float),
        Column('atlaskraan', Float),
        Column('kraan_groot', Float),
        Column('mainliner', Float),
        Column('hormachine', Float),
        Column('wagon', Float),
        Column('locomotor', Float),
        Column('locomotief', Float),
        Column('montagewagen', Float),
        Column('stormobiel', Float),
        Column('robeltrein', Float))
    params_finance = Table('params_finance', metadata,
        Column('financeID', Integer, primary_key=True),
        Column('factor', Float),
        Column('amount', Float))
    params_hours = Table('params_hours', metadata,
        Column('rateID', Integer, primary_key=True),
        Column('hourly_tariff', Float),
        Column('overhead_factor', Float),
        Column('wageID', None, ForeignKey('lonen.loonID')),
        Column('travel_time', Float))
    params_services = Table('params_services', metadata,
        Column('servicesID', Integer, primary_key=True),
        Column('hourly_tariff', Float),
        Column('overhead_factor', Float))

    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
    selpar = select([params_finance]).order_by(params_finance.c.financeID)
    rppar = con.execute(selpar).fetchall()

    selpar1 = select([params_hours]).order_by(params_hours.c.rateID)
    rppar1 = con.execute(selpar1).fetchall()

    selpar2 = select([params_services]).order_by(params_services.c.servicesID)
    rppar2 = con.execute(selpar2).fetchall()

    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
    
    selcal = select([calculaties]).where(calculaties.c.calculatie == mcalnr).\
     order_by(calculaties.c.clusterID)
    rpcal = con.execute(selcal)
      
    data_list=[]
    for row in rpcal:
        data_list += [(row)]
    
    def showDienst(idx):
        logger.warning(">>> Entering showDienst(idx=%s)", idx, extra={"event.action": "showDienst", "logrite.idx": idx})
        calcnr = idx.data()
        logger.debug("showDienst(idx=%s): calcnr → %s", idx, calcnr, extra={"event.action": "showDienst", "logrite.idx": idx})
        if idx.column() == 0:
            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            logger.debug("showDienst(idx=%s): engine → %s", idx, engine, extra={"event.action": "showDienst", "logrite.idx": idx})
            con = engine.connect()
            seldienst = select([calculaties]).where(calculaties.c.calcID==calcnr)
            logger.debug("showDienst(idx=%s): con → %s", idx, con, extra={"event.action": "showDienst", "logrite.idx": idx})
            rpcalc = con.execute(seldienst).first()
            class Widget(QDialog):
                 logger.debug("showDienst(idx=%s): seldienst → %s", idx, seldienst, extra={"event.action": "showDienst", "logrite.idx": idx})
                 def __init__(self, parent=None):
                    super(Widget, self).__init__(parent)
                    logger.debug("<<< Exiting showDienst(idx=%s)", idx, extra={"event.action": "showDienst", "logrite.idx": idx})
                    self.setWindowTitle("Werken extern calculatiegegevens van diensten opvragen")
                    self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
                                         
                    self.setFont(QFont('Arial', 10))
                       
                    q1Edit = QLineEdit(str(rpcalc[0]))
                    q1Edit.setFixedWidth(100)
                    q1Edit.setAlignment(Qt.AlignRight)
                    q1Edit.setDisabled(True)
                    q1Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    
                    q2Edit = QLineEdit(rpcalc[1])
                    q2Edit.setDisabled(True)
                    q2Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                        
                    q3Edit = QLineEdit(rpcalc[2])
                    q3Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q3Edit.setDisabled(True)
                    
                    q4Edit = QLineEdit(str(rpcalc[3]))
                    q4Edit.setFixedWidth(100)
                    q4Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q4Edit.setDisabled(True)
           
                    q5Edit = QLineEdit(str(rpcalc[4]))
                    q5Edit.setFixedWidth(100)
                    q5Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q5Edit.setDisabled(True)                              
                    
                    q8Edit = QLineEdit(str(rpcalc[5]))
                    q8Edit.setFixedWidth(100)
                    q8Edit.setAlignment(Qt.AlignRight)
                    q8Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q8Edit.setDisabled(True)
                    
                    q9Edit = QLineEdit('{:12.2f}'.format(rpcalc[6]))
                    q9Edit.setFixedWidth(100)
                    q9Edit.setAlignment(Qt.AlignRight)
                    q9Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q9Edit.setDisabled(True)
                                                         
                    q11Edit = QLineEdit(rpcalc[7])
                    q11Edit.setFixedWidth(100)
                    q11Edit.setAlignment(Qt.AlignRight)
                    q11Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q11Edit.setDisabled(True)
                      
                    q12Edit = QLineEdit(str(rpcalc[8]))
                    q12Edit.setFixedWidth(100)
                    q12Edit.setAlignment(Qt.AlignRight)
                    q12Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q12Edit.setDisabled(True)
                     
                    q13Edit = QLineEdit('{:12.2f}'.format(rpcalc[9]))
                    q13Edit.setFixedWidth(100)
                    q13Edit.setAlignment(Qt.AlignRight)
                    q13Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q13Edit.setDisabled(True)
             
                    q19Edit = QLineEdit('{:12.2f}'.format(rpcalc[10]))
                    q19Edit.setFixedWidth(100)
                    q19Edit.setAlignment(Qt.AlignRight)
                    q19Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q19Edit.setDisabled(True)
             
                    q14Edit = QLineEdit('{:12.2f}'.format(rpcalc[11]))
                    q14Edit.setFixedWidth(100)
                    q14Edit.setAlignment(Qt.AlignRight)
                    q14Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q14Edit.setDisabled(True)
                                    
                    q15Edit = QLineEdit('{:12.2f}'.format(rpcalc[12]))
                    q15Edit.setDisabled(True)
                    q15Edit.setAlignment(Qt.AlignRight)
                    q15Edit.setFixedWidth(100)
                    q15Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")

                    q16Edit = QLineEdit('{:12.2f}'.format(rpcalc[13]))
                    q16Edit.setFixedWidth(100)
                    q16Edit.setAlignment(Qt.AlignRight)
                    q16Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q16Edit.setDisabled(True)
                                            
                    q17Edit = QLineEdit('{:12.2f}'.format(rpcalc[15]))
                    q17Edit.setFixedWidth(100)
                    q17Edit.setAlignment(Qt.AlignRight)
                    q17Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q17Edit.setDisabled(True)
                    
                    q20Edit = QLineEdit('{:12.2f}'.format(rpcalc[16]))
                    q20Edit.setFixedWidth(100)
                    q20Edit.setAlignment(Qt.AlignRight)
                    q20Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q20Edit.setDisabled(True)
                    
                    q21Edit = QLineEdit('{:12.2f}'.format(rpcalc[17]))
                    q21Edit.setFixedWidth(100)
                    q21Edit.setAlignment(Qt.AlignRight)
                    q21Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q21Edit.setDisabled(True)
    
                    q22Edit = QLineEdit('{:12.2f}'.format(rpcalc[18]))
                    q22Edit.setFixedWidth(100)
                    q22Edit.setAlignment(Qt.AlignRight)
                    q22Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q22Edit.setDisabled(True)
    
                    q23Edit = QLineEdit('{:12.2f}'.format(rpcalc[19]))
                    q23Edit.setFixedWidth(100)
                    q23Edit.setAlignment(Qt.AlignRight)
                    q23Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q23Edit.setDisabled(True)
                    
                    q24Edit = QLineEdit('{:12.2f}'.format(rpcalc[20]))
                    q24Edit.setFixedWidth(100)
                    q24Edit.setAlignment(Qt.AlignRight)
                    q24Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q24Edit.setDisabled(True)
                                                  
                    q26Edit = QLineEdit('{:12.2f}'.format(rpcalc[21]))
                    q26Edit.setFixedWidth(100)
                    q26Edit.setAlignment(Qt.AlignRight)
                    q26Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q26Edit.setDisabled(True)
                    
                    q27Edit = QLineEdit('{:12.2f}'.format(rpcalc[14]))
                    q27Edit.setFixedWidth(100)
                    q27Edit.setAlignment(Qt.AlignRight)
                    q27Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q27Edit.setDisabled(True)

                    q28Edit = QLineEdit('{:12.2f}'.format(rpcalc[23] * rppar[0][1]))
                    q28Edit.setFixedWidth(100)
                    q28Edit.setAlignment(Qt.AlignRight)
                    q28Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q28Edit.setDisabled(True)

                    q29Edit = QLineEdit('{:12.2f}'.format(rpcalc[24] * rppar2[1][1]))
                    q29Edit.setFixedWidth(100)
                    q29Edit.setAlignment(Qt.AlignRight)
                    q29Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q29Edit.setDisabled(True)

                    q30Edit = QLineEdit('{:12.2f}'.format(rpcalc[25] * rppar2[2][1]))
                    q30Edit.setFixedWidth(100)
                    q30Edit.setAlignment(Qt.AlignRight)
                    q30Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q30Edit.setDisabled(True)

                    q31Edit = QLineEdit('{:12.2f}'.format(rpcalc[26] * rppar2[3][1]))
                    q31Edit.setFixedWidth(100)
                    q31Edit.setAlignment(Qt.AlignRight)
                    q31Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q31Edit.setDisabled(True)

                    q32Edit = QLineEdit('{:12.2f}'.format(rpcalc[27] * rppar2[4][1]))
                    q32Edit.setFixedWidth(100)
                    q32Edit.setAlignment(Qt.AlignRight)
                    q32Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q32Edit.setDisabled(True)

                    q33Edit = QLineEdit('{:12.2f}'.format(rpcalc[28] * rppar2[5][1]))
                    q33Edit.setFixedWidth(100)
                    q33Edit.setAlignment(Qt.AlignRight)
                    q33Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q33Edit.setDisabled(True)

                    q34Edit = QLineEdit('{:12.2f}'.format(rpcalc[29] * rppar2[6][1]))
                    q34Edit.setFixedWidth(100)
                    q34Edit.setAlignment(Qt.AlignRight)
                    q34Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q34Edit.setDisabled(True)

                    q35Edit = QLineEdit('{:12.2f}'.format(rpcalc[30] * rppar2[7][1]))
                    q35Edit.setFixedWidth(100)
                    q35Edit.setAlignment(Qt.AlignRight)
                    q35Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q35Edit.setDisabled(True)

                    q36Edit = QLineEdit('{:12.2f}'.format(rpcalc[31] * rppar2[8][1]))
                    q36Edit.setFixedWidth(100)
                    q36Edit.setAlignment(Qt.AlignRight)
                    q36Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q36Edit.setDisabled(True)

                    q37Edit = QLineEdit('{:12.2f}'.format(rpcalc[32] * rppar2[9][1]))
                    q37Edit.setFixedWidth(100)
                    q37Edit.setAlignment(Qt.AlignRight)
                    q37Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q37Edit.setDisabled(True)

                    q38Edit = QLineEdit('{:12.2f}'.format(rpcalc[33] * rppar2[10][1]))
                    q38Edit.setFixedWidth(100)
                    q38Edit.setAlignment(Qt.AlignRight)
                    q38Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q38Edit.setDisabled(True)

                    q39Edit = QLineEdit('{:12.2f}'.format(rpcalc[34] * rppar2[11][1]))
                    q39Edit.setFixedWidth(100)
                    q39Edit.setAlignment(Qt.AlignRight)
                    q39Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q39Edit.setDisabled(True)

                    grid = QGridLayout()
                    grid.setSpacing(20)
                    
                    lbl = QLabel()
                    pixmap = QPixmap('./images/logos/verbinding.jpg')
                    lbl.setPixmap(pixmap)
                    grid.addWidget(lbl ,0 , 0)
                    
                    grid.addWidget(QLabel('Calculatiegegevens van\nDiensten externe werken opvragen'), 0, 1, 1, 3)
                    
                    logo = QLabel()
                    pixmap = QPixmap('./images/logos/logo.jpg')
                    logo.setPixmap(pixmap)
                    grid.addWidget(logo , 0, 6, 1, 1, Qt.AlignRight)
            
                    self.setFont(QFont('Arial', 10))
                     
                    grid.addWidget(QLabel('CalcID'), 1, 0)
                    grid.addWidget(q1Edit, 1, 1) 
                    
                    grid.addWidget(QLabel('Clusteromschrijving'), 2, 0)
                    grid.addWidget(q3Edit, 2, 1, 1, 3)
                    
                    grid.addWidget(QLabel('Cluster'), 3, 0)
                    grid.addWidget(q2Edit, 3, 1, 1, 3) 
               
                    grid.addWidget(QLabel('Calculatie'), 4, 0)
                    grid.addWidget(q4Edit, 4, 1) 
                     
                    grid.addWidget(QLabel('ClusterID'), 4, 2)
                    grid.addWidget(q5Edit, 4, 3)
                                                              
                    grid.addWidget(QLabel('Verwerkt'), 5, 0)
                    grid.addWidget(q8Edit, 5, 1)
                    
                    grid.addWidget(QLabel('Hoeveelheid'), 5, 2)
                    grid.addWidget(q9Edit, 5, 3)
                                                
                    grid.addWidget(QLabel('Eenheid'), 6, 0)
                    grid.addWidget(q11Edit, 6, 1)
                    
                    grid.addWidget(QLabel('Werknummer'), 6, 2)
                    grid.addWidget(q12Edit, 6, 3)
                    
                    grid.addWidget(QLabel('Prijs'), 7, 0)
                    grid.addWidget(q13Edit, 7, 1)
                    
                    grid.addWidget(QLabel('Materialen'), 7,  2)
                    grid.addWidget(q19Edit, 7, 3)
                                
                    grid.addWidget(QLabel('Lonen'), 8, 0)
                    grid.addWidget(q14Edit, 8, 1) 

                    grid.addWidget(QLabel('Materieel'), 9, 0)
                    grid.addWidget(q16Edit, 9, 1)                           

                    lblsoort = QLabel('Materieelsoort')
                    lbluren = QLabel('Uren')
                    lblbedrag = QLabel('Bedrag')
                    
                    grid.addWidget(lblsoort, 1, 4)
                    grid.addWidget(lbluren, 1, 5)
                    grid.addWidget(lblbedrag, 1, 6)
                    
                    grid.addWidget(QLabel('Inhuur'), 2, 4)
                    grid.addWidget(QLabel('{:12.2f}'.format(rpcalc[22])), 2, 5, 1, 1, Qt.AlignRight)
                    grid.addWidget(q27Edit, 2, 6)
                    
                    grid.addWidget(QLabel('Sleuvengraver'), 3, 4)
                    grid.addWidget(QLabel('{:12.2f}'.format(rpcalc[23])), 3, 5, 1, 1, Qt.AlignRight)
                    grid.addWidget(q28Edit, 3, 6)
                    
                    grid.addWidget(QLabel('Persapparaat'), 4, 4)
                    grid.addWidget(QLabel('{:12.2f}'.format(rpcalc[24])), 4, 5, 1, 1, Qt.AlignRight)
                    grid.addWidget(q29Edit, 4, 6)
                    
                    grid.addWidget(QLabel('Atlaskraan'), 5, 4)
                    grid.addWidget(QLabel('{:12.2f}'.format(rpcalc[25])), 5, 5, 1, 1, Qt.AlignRight)
                    grid.addWidget(q30Edit, 5, 6)
                    
                    grid.addWidget(QLabel('Kraan groot'), 6, 4)
                    grid.addWidget(QLabel('{:12.2f}'.format(rpcalc[26])), 6, 5, 1, 1, Qt.AlignRight)
                    grid.addWidget(q31Edit, 6, 6)
                    
                    grid.addWidget(QLabel('Mainliner'), 7, 4)
                    grid.addWidget(QLabel('{:12.2f}'.format(rpcalc[27])), 7, 5, 1, 1, Qt.AlignRight)
                    grid.addWidget(q32Edit, 7, 6)
                    
                    grid.addWidget(QLabel('Hormachine'), 8, 4)
                    grid.addWidget(QLabel('{:12.2f}'.format(rpcalc[28])), 8, 5, 1, 1, Qt.AlignRight)
                    grid.addWidget(q33Edit, 8, 6)
                    
                    grid.addWidget(QLabel('Wagon'), 9, 4)
                    grid.addWidget(QLabel('{:12.2f}'.format(rpcalc[29])), 9, 5, 1, 1, Qt.AlignRight)
                    grid.addWidget(q34Edit, 9, 6)
                    
                    grid.addWidget(QLabel('Locomotor'), 10, 4)
                    grid.addWidget(QLabel('{:12.2f}'.format(rpcalc[30])), 10, 5, 1, 1, Qt.AlignRight)
                    grid.addWidget(q35Edit, 10, 6)
                    
                    grid.addWidget(QLabel('Locomotief'), 11, 4)
                    grid.addWidget(QLabel('{:12.2f}'.format(rpcalc[31])), 11, 5, 1, 1, Qt.AlignRight)
                    grid.addWidget(q36Edit, 11, 6)
                    
                    grid.addWidget(QLabel('Montagewagen'), 12, 4)
                    grid.addWidget(QLabel('{:12.2f}'.format(rpcalc[32])), 12, 5, 1, 1, Qt.AlignRight)
                    grid.addWidget(q37Edit, 12, 6)
                    
                    grid.addWidget(QLabel('Stormobiel'), 13, 4)
                    grid.addWidget(QLabel('{:12.2f}'.format(rpcalc[33])), 13, 5, 1, 1, Qt.AlignRight)
                    grid.addWidget(q38Edit, 13, 6)
                    
                    grid.addWidget(QLabel('Robeltrein'), 14, 4)
                    grid.addWidget(QLabel('{:12.2f}'.format(rpcalc[34])), 14, 5, 1, 1, Qt.AlignRight)
                    grid.addWidget(q39Edit, 14, 6)
                                                                              
                    grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 15, 0, 1, 7, Qt.AlignCenter)
                    self.setLayout(grid)
                    self.setGeometry(500, 50, 350, 300)
                                                                            
                    cancelBtn = QPushButton('Sluiten')
                    cancelBtn.clicked.connect(self.close)
                
                    grid.addWidget(cancelBtn, 15, 6, 1, 1, Qt.AlignRight)
                    logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
                    cancelBtn.setFont(QFont("Arial",10))
                    cancelBtn.setFixedWidth(100)
                    cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            window = Widget()
            window.exec_() 
            
    win = MyWindow(data_list, header)
    win.exec_()
            
def toonArtikellijst(mcalnr, mwerknr):
    logger.warning(">>> Entering toonArtikellijst(mcalnr=%s,mwerknr=%s)", mcalnr, mwerknr, extra={"event.action": "toonArtikellijst", "logrite.mcalnr": mcalnr, "logrite.mwerknr": mwerknr})
    class MyWindow(QDialog):
        def __init__(self, data_list, header, *args):
            QWidget.__init__(self, *args,)
            self.setGeometry(100, 50, 1200, 900)
            self.setWindowTitle('Materiaallijst')
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            self.setWindowFlags(self.windowFlags()| Qt.WindowSystemMenuHint |
                                                    Qt.WindowMinMaxButtonsHint)
            table_model = MyTableModel(self, data_list, header)
            table_view = QTableView()
            table_view.setModel(table_model)
            font = QFont("Arial", 10)
            table_view.setFont(font)
            table_view.setColumnHidden(6, True)
            table_view.resizeColumnsToContents()
            table_view.setSelectionBehavior(QTableView.SelectRows)
            #table_view.clicked.connect(selectRow)
            table_view.clicked.connect(showSelart)
            layout = QVBoxLayout(self)
            layout.addWidget(table_view)
            self.setLayout(layout)
    
    class MyTableModel(QAbstractTableModel):
        def __init__(self, parent, mylist, header, *args):
            QAbstractTableModel.__init__(self, parent, *args)
            self.mylist = mylist
            logger.warning(">>> Entering __init__()", extra={"event.action": "__init__"})
            logger.debug("__init__(): grid → %s", grid, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): grid → %s", self, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.lbl → %s", self.lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.pixmap → %s", self.pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl → %s", self, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.logo → %s", self.logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): logo → %s", self, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Gegevens → %s", self.Gegevens, extra={"event.action": "__init__"})
            logger.debug("__init__(): q1Edit → %s", q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q1Edit → %s", self, q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): terugBtn → %s", terugBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): terugBtn → %s", self, terugBtn, extra={"event.action": "__init__"})
            logger.debug("<<< Exiting __init__()", extra={"event.action": "__init__"})
            self.header = header
        def rowCount(self, parent):
            return len(self.mylist)
        def columnCount(self, parent):
            return len(self.mylist[0])
        def data(self, index, role):
            veld = self.mylist[index.row()][index.column()]
            if not index.isValid():
                return None
            elif role == Qt.TextAlignmentRole and (type(veld) == float or type(veld) == int):
                return Qt.AlignRight | Qt.AlignVCenter
            elif role != Qt.DisplayRole:
                return None
            if type(veld) == float:
                return '{:12.2f}'.format(veld)
            else:
                return veld
        def headerData(self, col, orientation, role):
            if orientation == Qt.Horizontal and role == Qt.DisplayRole:
                return self.header[col]
            return None
              
    header = ['Artikelnr','Cluster','Reserveringsaldo','LijstID','Calculatie',\
              'Werknummer','Orderinkoopnummer', 'Artikelnr','ArtikelPrijs',\
              'Hoeveelheid','Afroep','Resterend','Subtotaal','Reserveringdatum',\
              'Levering eind','Levering begin','Categorie']
                   
    metadata = MetaData()
    materiaallijsten = Table('materiaallijsten', metadata,
         Column('matlijstID', Integer, primary_key=True),
         Column('calculatie', Integer),
         Column('werknummerID', Integer),
         Column('orderinkoopID', Integer),
         Column('artikelID', None, ForeignKey('artikelen.artikelID')),
         Column('artikelprijs', Float),
         Column('hoeveelheid', Float),
         Column('afroep', Float),
         Column('resterend', Float),
         Column('subtotaal', Float),
         Column('reserverings_datum', String),
         Column('levertijd_end', String),
         Column('levertijd_begin', String),
         Column('categorie', Integer))
    artikelen = Table('artikelen', metadata,
         Column('artikelID', Integer(), primary_key=True),
         Column('artikelomschrijving', String),
         Column('reserveringsaldo', Float))
                                    
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
    
    selmat = select([artikelen,materiaallijsten]).where(and_(materiaallijsten.c.artikelID == artikelen.c.artikelID,\
          materiaallijsten.c.calculatie == mcalnr))\
         .order_by(materiaallijsten.c.artikelID)
    rpmat = con.execute(selmat)
    
    data_list=[]
    for row in rpmat:
        data_list += [(row)]
        
    def showSelart(idx):
        logger.warning(">>> Entering showSelart(idx=%s)", idx, extra={"event.action": "showSelart", "logrite.idx": idx})
        martnr = idx.data()
        logger.debug("showSelart(idx=%s): martnr → %s", idx, martnr, extra={"event.action": "showSelart", "logrite.idx": idx})
        if idx.column() == 0:
            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            logger.debug("showSelart(idx=%s): engine → %s", idx, engine, extra={"event.action": "showSelart", "logrite.idx": idx})
            con = engine.connect()
                
            logger.debug("showSelart(idx=%s): con → %s", idx, con, extra={"event.action": "showSelart", "logrite.idx": idx})
            selmat = select([artikelen, materiaallijsten]).where(\
                 and_(materiaallijsten.c.artikelID == artikelen.c.artikelID,\
                 materiaallijsten.c.artikelID == int(martnr),\
                 materiaallijsten.c.calculatie == mcalnr))\
                 .order_by(materiaallijsten.c.artikelID)
            logger.debug("showSelart(idx=%s): selmat → %s", idx, selmat, extra={"event.action": "showSelart", "logrite.idx": idx})
            rpmat = con.execute(selmat).first()
             
            logger.debug("showSelart(idx=%s): rpmat → %s", idx, rpmat, extra={"event.action": "showSelart", "logrite.idx": idx})
            header = ['Artikelnr','Cluster','Reserveringsaldo','LijstID','Calculatie',\
              'Werknummer','Orderinkoopnummer', 'Artikelnr','ArtikelPrijs',\
              'Hoeveelheid','Afroep','Resterend','Subtotaal','Reserveringdatum',\
              'Levering eind','Levering begin', 'Categorie']
 
            logger.debug("showSelart(idx=%s): header → %s", idx, header, extra={"event.action": "showSelart", "logrite.idx": idx})
            class MainWindow(QDialog):
                logger.debug("<<< Exiting showSelart(idx=%s)", idx, extra={"event.action": "showSelart", "logrite.idx": idx})
                def __init__(self):
                    logger.warning(">>> Entering __init__()", extra={"event.action": "__init__"})
                    QDialog.__init__(self)
                    
                    grid = QGridLayout()
                    grid.setSpacing(20)
                    
                    self.setWindowTitle("Opvragen Artikelen Clustercalculatie")
                    self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
                    
                    self.setFont(QFont('Arial', 10))   
                                                      
                    self.lbl = QLabel()
                    self.pixmap = QPixmap('./images/logos/verbinding.jpg')
                    self.lbl.setPixmap(self.pixmap)
                    grid.addWidget(self.lbl , 0, 0)
                    
                    grid.addWidget(QLabel('Opvragen Artikelen Calculatie'),0, 1, 1, 2)
            
                    self.logo = QLabel()
                    self.pixmap = QPixmap('./images/logos/logo.jpg')
                    self.logo.setPixmap(self.pixmap)
                    grid.addWidget(self.logo , 0, 3, 1, 1, Qt.AlignRight)                
                    index = 1
                    for item in header:
                        self.lbl = QLabel(header[index-1])
                        self.Gegevens = QLabel()
                        if index == 1:
                            if type(rpmat[index-1]) == float:
                                q1Edit = QLineEdit('{:12.2f}'.format(rpmat[index-1]))
                                q1Edit.setAlignment(Qt.AlignRight)
                            elif type(rpmat[index-1]) == int:
                                q1Edit = QLineEdit(str(rpmat[index-1]))
                                q1Edit.setAlignment(Qt.AlignRight)
                            else:
                                q1Edit = QLineEdit(str(rpmat[index-1]))
                            q1Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                            q1Edit.setFixedWidth(100)
                            q1Edit.setDisabled(True)
                            grid.addWidget(self.lbl, 1, 0)
                            grid.addWidget(q1Edit, index, 1, 1, 2)
                        elif index == 2:
                            q1Edit = QLineEdit(str(rpmat[index-1]))
                            q1Edit.setFixedWidth(400)
                            q1Edit.setDisabled(True)
                            q1Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                            grid.addWidget(self.lbl, 2, 0)
                            grid.addWidget(q1Edit, index, 1, 1, 3)
                        elif index%2 == 0:
                            if type(rpmat[index-1]) == float:
                                q1Edit = QLineEdit('{:12.2f}'.format(rpmat[index-1]))
                                q1Edit.setAlignment(Qt.AlignRight)
                            elif type(rpmat[index-1]) == int:
                                q1Edit = QLineEdit(str(rpmat[index-1]))
                                q1Edit.setAlignment(Qt.AlignRight)
                            else:
                                q1Edit = QLineEdit(str(rpmat[index-1]))
                            q1Edit.setFixedWidth(100)
                            q1Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                            q1Edit.setDisabled(True)
                            grid.addWidget(self.lbl, index, 0)
                            grid.addWidget(q1Edit, index, 1)
                        else:
                            if type(rpmat[index-1]) == float:
                                q1Edit = QLineEdit('{:12.2f}'.format(rpmat[index-1]))
                                q1Edit.setAlignment(Qt.AlignRight)
                            elif type(rpmat[index-1]) == int:
                                q1Edit = QLineEdit(str(rpmat[index-1]))
                                q1Edit.setAlignment(Qt.AlignRight)
                            else:
                                q1Edit = QLineEdit(str(rpmat[index-1]))
                            q1Edit.setFixedWidth(100)
                            q1Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                            q1Edit.setDisabled(True)
                            grid.addWidget(self.lbl, index+1, 2)
                            grid.addWidget(q1Edit, index+1, 3)
                        index += 1
                        
                    terugBtn = QPushButton('Sluiten')
                    terugBtn.clicked.connect(self.accept)
            
                    grid.addWidget(terugBtn, index+1, 3, 1, 1, Qt.AlignRight)
                    terugBtn.setFont(QFont("Arial",10))
                    terugBtn.setFixedWidth(100)
                    terugBtn.setStyleSheet("color: black;  background-color: gainsboro")
                    
                    grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), index+2, 0, 1, 4, Qt.AlignCenter)
                                                                            
                    self.setLayout(grid)
                    self.setGeometry(400, 200, 150, 150)
                    logger.debug("<<< Exiting __init__()", extra={"event.action": "__init__"})
                            
            mainWin = MainWindow()
            mainWin.exec_()
            
    win = MyWindow(data_list, header)
    win.exec_()   