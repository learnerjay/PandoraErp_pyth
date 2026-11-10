import datetime
from login import hoofdMenu
from PyQt5.QtCore import Qt, QAbstractTableModel, QRegExp
from PyQt5.QtGui import QFont, QPixmap, QRegExpValidator, QIcon
from PyQt5.QtWidgets import QWidget, QTableView, QVBoxLayout, QComboBox,\
     QDialog, QLabel, QGridLayout, QPushButton, QMessageBox, QLineEdit
    
from sqlalchemy import (Table, Column, Integer, String, Float,\
                        MetaData, create_engine, ForeignKey)
from sqlalchemy.sql import select, insert, func, update, delete, and_
import logging
logger = logging.getLogger(__name__)

def info():
    logger.warning(">>> Entering info()", extra={"event.action": "info"})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle("Informatie ERP Systeem Pandora")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            self.setFont(QFont('Arial', 10))
            grid = QGridLayout()
            grid.setSpacing(20)
            
            lblinfo = QLabel('Informatie ERP Pandora')
            grid.addWidget(lblinfo, 0, 0, 1, 2, Qt.AlignCenter)
            lblinfo.setStyleSheet("color:rgba(45, 83, 115, 255); font: 20pt Comic Sans MS")
            
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 0, 1, 1, Qt.AlignRight)
        
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl, 0, 0)
            
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            infolbl = QLabel(
      '''

        Informatie over clustercalculatie maken en koppelen naar werknummer.
        
        De volgorde van het aanmaken en koppelen van een calculatie is:
                      
        Menu Calculatie externe werken
        6. Calculatie maken of wijzigen.
           Accepteer het eerste vrije nummer hetgeen door het systeem wordt ingevuld.\t
           Wijzigen is alleen mogelijk indien de calculatie nog niet is gekoppeld
           aan een werknummer. Kies in dit geval een bestaand calculatienummer.
        7. Calculatie/Artikellijst - opvragen/berekenen/printen
           Hiermee worden de calculatiegegevens en /of de artikelgegevens opgevraagd
           berekend of geprint. De berekening geschiedt na starten van de module. 
                  
        Menu Externe Werken
        1. Invoeren Werknummers
           Indien werknummer nog niet bestaat, eerst werknummer invoeren, anders koppelen. 
           
        Menu Calculatie externe werken   
        8. Calculatie koppelen produktie.
           De koppeling van de calculatie met het werknummer wordt gemaakt en de
           artikelgegevens en werktarieven worden overgezet naar het werknummer.
           
        7. Print hierna de calculatie en de artikellijst uit voor produktie.
            Printen van de order lijst voor inkoop van "Diensten en Materiëel" 
            is alleen mogelijk als de order voor het werknummer is verkregen. 
            Hiervoor dient de box "order' van het werknummer te worden geactiveerd.
           
     ''')
            grid.addWidget(infolbl, 1, 0)
                           
            infolbl.setStyleSheet("font: 10pt Comic Sans MS; color: black ; background-color: #D9E1DF")   
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 2, 0, 1, 2, Qt.AlignCenter)
            
            cancelBtn = QPushButton('Sluiten')
            cancelBtn.clicked.connect(self.close)  
            
            grid.addWidget(cancelBtn, 2, 0, 1, 1,  Qt.AlignRight)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(90)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            self.setLayout(grid)
            self.setGeometry(350, 50, 150, 100)
            
    window = Widget()
    window.exec_()

def gerCalnr(mcalnr):
    logger.warning(">>> Entering gerCalnr(mcalnr=%s)", mcalnr, extra={"event.action": "gerCalnr", "logrite.mcalnr": mcalnr})
    msg = QMessageBox()
    logger.debug("gerCalnr(mcalnr=%s): msg → %s", mcalnr, msg, extra={"event.action": "gerCalnr", "logrite.mcalnr": mcalnr})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Information)
    msg.setText('Calculatienummer '+str(mcalnr)+'  is aangemaakt!')
    msg.setWindowTitle('Clustercalculatie invoeren')               
    logger.debug("<<< Exiting gerCalnr(mcalnr=%s)", mcalnr, extra={"event.action": "gerCalnr", "logrite.mcalnr": mcalnr})
    msg.exec_()

def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})

def ongInvoer():
    logger.warning(">>> Entering ongInvoer()", extra={"event.action": "ongInvoer"})
    msg = QMessageBox()
    logger.debug("ongInvoer(): msg → %s", msg, extra={"event.action": "ongInvoer"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Foutieve invoer\nzoekterm opnieuw invoeren s.v.p.!')
    msg.setWindowTitle('Clustercalculatie invoeren')               
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
    msg.setWindowTitle('Clustercalculatie invoeren')               
    logger.debug("<<< Exiting geenRecord()", extra={"event.action": "geenRecord"})
    msg.exec_() 

def invoerOK():
    logger.warning(">>> Entering invoerOK()", extra={"event.action": "invoerOK"})
    msg = QMessageBox()
    logger.debug("invoerOK(): msg → %s", msg, extra={"event.action": "invoerOK"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Information)
    msg.setText('Invoer gelukt')
    msg.setWindowTitle('Clustercalculatie invoeren')
    logger.debug("<<< Exiting invoerOK()", extra={"event.action": "invoerOK"})
    msg.exec_()

def calcBestaat():
    logger.warning(">>> Entering calcBestaat()", extra={"event.action": "calcBestaat"})
    msg = QMessageBox()
    logger.debug("calcBestaat(): msg → %s", msg, extra={"event.action": "calcBestaat"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Information)
    msg.setText('Calculatieregel bestaat al\nen is verrekend met\ningebrachte hoeveelheid!')
    msg.setWindowTitle('Clustercalculatie invoeren')
    logger.debug("<<< Exiting calcBestaat()", extra={"event.action": "calcBestaat"})
    msg.exec_() 
    
def calcGekoppeld():
    logger.warning(">>> Entering calcGekoppeld()", extra={"event.action": "calcGekoppeld"})
    msg = QMessageBox()
    logger.debug("calcGekoppeld(): msg → %s", msg, extra={"event.action": "calcGekoppeld"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Critical)
    msg.setText('Calculatie is al gekoppeld aan werk\nwijzigen is niet meer mogelijk!')
    msg.setWindowTitle('Clustercalculatie invoeren')
    logger.debug("<<< Exiting calcGekoppeld()", extra={"event.action": "calcGekoppeld"})
    msg.exec_() 
    
def schoonCalculatie(mcalnr, m_email):
    logger.warning(">>> Entering schoonCalculatie(mcalnr=%s,m_email=%s)", mcalnr, m_email, extra={"event.action": "schoonCalculatie", "logrite.mcalnr": mcalnr})
    msgBox=QMessageBox()
    logger.debug("schoonCalculatie(mcalnr=%s,m_email=%s): msgBox → %s", mcalnr, m_email, msgBox, extra={"event.action": "schoonCalculatie", "logrite.mcalnr": mcalnr})
    msgBox.setStyleSheet("color: black;  background-color: gainsboro")
    msgBox.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msgBox.setWindowTitle("Calculatie Aanpassen")
    msgBox.setIcon(QMessageBox.Warning)
    msgBox.setText("Deze calculatie bestaat al\nwilt u deze calculatie aanpassen?");
    msgBox.setStandardButtons(QMessageBox.Yes)
    msgBox.addButton(QMessageBox.No)
    msgBox.setDefaultButton(QMessageBox.Yes)
    if(msgBox.exec_() == QMessageBox.Yes):
       metadata = MetaData()
       logger.debug("schoonCalculatie(mcalnr=%s,m_email=%s): metadata → %s", mcalnr, m_email, metadata, extra={"event.action": "schoonCalculatie", "logrite.mcalnr": mcalnr})
       calculaties = Table('calculaties', metadata,
           Column('calcID', Integer(), primary_key=True),
           Column('calculatie', Integer),
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
           Column('werkomschrijving', String),
           Column('verwerkt', Integer))
       materiaallijsten = Table('materiaallijsten', metadata,
           Column('matlijstID', Integer, primary_key=True),
           Column('calculatie', Integer))
        
       engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
       logger.debug("schoonCalculatie(mcalnr=%s,m_email=%s): engine → %s", mcalnr, m_email, engine, extra={"event.action": "schoonCalculatie", "logrite.mcalnr": mcalnr})
       con = engine.connect()
       logger.debug("schoonCalculatie(mcalnr=%s,m_email=%s): con → %s", mcalnr, m_email, con, extra={"event.action": "schoonCalculatie", "logrite.mcalnr": mcalnr})
       updcal = update(calculaties).where(calculaties.c.calculatie == mcalnr).values\
         (prijs=0, materialen=0, lonen=0,diensten=0,materieel=0,inhuur=0,uren_constr=0,\
         uren_mont=0,uren_retourlas=0,uren_telecom=0,uren_bfi=0,uren_voeding=0,\
         uren_bvl=0,uren_spoorleg=0,uren_spoorlas=0,uren_inhuur=0,sleuvengraver=0,\
         persapparaat=0,atlaskraan=0,kraan_groot=0,mainliner=0,hormachine=0,\
         wagon=0,locomotor=0,locomotief=0,montagewagen=0,stormobiel=0,robeltrein=0,\
         verwerkt=0)
       logger.debug("schoonCalculatie(mcalnr=%s,m_email=%s): updcal → %s", mcalnr, m_email, updcal, extra={"event.action": "schoonCalculatie", "logrite.mcalnr": mcalnr})
       con.execute(updcal)
       delmat = delete(materiaallijsten).where(materiaallijsten.c.calculatie==mcalnr)
       logger.debug("schoonCalculatie(mcalnr=%s,m_email=%s): delmat → %s", mcalnr, m_email, delmat, extra={"event.action": "schoonCalculatie", "logrite.mcalnr": mcalnr})
       con.execute(delmat)
    else:
        zoeken(m_email)
        logger.debug("<<< Exiting schoonCalculatie(mcalnr=%s,m_email=%s)", mcalnr, m_email, extra={"event.action": "schoonCalculatie", "logrite.mcalnr": mcalnr})
    
def zoeken(m_email):
    logger.warning(">>> Entering zoeken(m_email=%s)", m_email, extra={"event.action": "zoeken"})
    metadata = MetaData()
    logger.debug("zoeken(m_email=%s): metadata → %s", m_email, metadata, extra={"event.action": "zoeken"})
    calculaties = Table('calculaties', metadata,
       Column('calcID', Integer(), primary_key=True),
       Column('calculatie', Integer),
       Column('verwerkt', Integer))
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("zoeken(m_email=%s): engine → %s", m_email, engine, extra={"event.action": "zoeken"})
    con = engine.connect()
    try:
        logger.debug("zoeken(m_email=%s): con → %s", m_email, con, extra={"event.action": "zoeken"})
        mcalnr = con.execute(select([func.max(calculaties.c.calculatie,\
            type_=Integer)])).scalar()
    except:
        logger.error("Exception in zoeken(m_email=%s)", m_email, exc_info=True, extra={"event.action": "zoeken", "event.category": "process"})
        logger.debug("zoeken(m_email=%s): type_ → %s", m_email, type_, extra={"event.action": "zoeken"})
        mcalnr = 0
        logger.debug("zoeken(m_email=%s): mcalnr → %s", m_email, mcalnr, extra={"event.action": "zoeken"})

    class Widget(QDialog):
        logger.debug("<<< Exiting zoeken(m_email=%s)", m_email, extra={"event.action": "zoeken"})
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            self.setWindowTitle("Calculatie extern werk maken / wijzigen")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
            
            self.Calculatie = QLabel()
            logger.debug("__init__(parent=%s): self.Calculatie → %s", parent, self.Calculatie, extra={"event.action": "__init__"})
            kEdit = QLineEdit(str(mcalnr+1))
            logger.debug("__init__(self=%s,parent=%s): kEdit → %s", self, parent, kEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): kEdit → %s", parent, kEdit, extra={"event.action": "__init__"})
            kEdit.setFixedWidth(100)
            kEdit.setFont(QFont("Arial",10))
            reg_ex = QRegExp('^[1-9]{1}[0-9]{0,9}$')
            logger.debug("__init__(parent=%s): reg_ex → %s", parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): reg_ex → %s", self, parent, reg_ex, extra={"event.action": "__init__"})
            input_validator = QRegExpValidator(reg_ex, kEdit)
            logger.debug("__init__(self=%s,parent=%s): input_validator → %s", self, parent, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): input_validator → %s", parent, input_validator, extra={"event.action": "__init__"})
            kEdit.setValidator(input_validator)
            kEdit.textChanged.connect(self.kChanged)

            self.Werkomschrijving = QLabel()
            logger.debug("__init__(parent=%s): self.Werkomschrijving → %s", parent, self.Werkomschrijving, extra={"event.action": "__init__"})
            k1Edit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): k1Edit → %s", self, parent, k1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): k1Edit → %s", parent, k1Edit, extra={"event.action": "__init__"})
            k1Edit.setFixedWidth(300)
            k1Edit.setFont(QFont("Arial", 10))
            reg_ex = QRegExp('^.{45}$')
            input_validator = QRegExpValidator(reg_ex, k1Edit)
            k1Edit.setValidator(input_validator)
            k1Edit.textChanged.connect(self.k1Changed)
                   
            self.Keuze = QLabel()
            logger.debug("__init__(parent=%s): self.Keuze → %s", parent, self.Keuze, extra={"event.action": "__init__"})
            k0Edit = QComboBox()
            logger.debug("__init__(self=%s,parent=%s): k0Edit → %s", self, parent, k0Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): k0Edit → %s", parent, k0Edit, extra={"event.action": "__init__"})
            k0Edit.setFixedWidth(340)
            k0Edit.setFont(QFont("Arial",10))
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.addItem('         Sorteersleutel Clustergroepen')
            k0Edit.addItem('0. Alle Clusters')
            k0Edit.addItem('AA-AK. Spoorstaven + lasmiddelen')
            k0Edit.addItem('BA-BK. Liggers + bevestiging')
            k0Edit.addItem('CA-CK. Overwegen + overwegbeveiliging')
            k0Edit.addItem('DA-DK. Steenslag + grond aanvulling')
            k0Edit.addItem('EA-EK. Wissel + baanconstrukties')
            k0Edit.addItem('FA-FK. Ondergrondse infrastruktuur')
            k0Edit.addItem('GA-GK. Treinbeheersing + seinen')
            k0Edit.addItem('HA-HK. Bovenleiding + draagconstruktie')
            k0Edit.addItem('JA-JK. Voedingen + Onderstations')
            k0Edit.activated[str].connect(self.k0Changed)
           
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
            grid.addWidget(lbl , 0, 0, 1, 2)

            lbl2 = QLabel('Calculatie')
            logger.debug("__init__(parent=%s): lbl2 → %s", parent, lbl2, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl2 → %s", self, parent, lbl2, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl3 → %s", parent, lbl3, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl3 → %s", self, parent, lbl3, extra={"event.action": "__init__"})
            lbl2.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            lbl3 = QLabel('Omschrijving')
            lbl3.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl2, 1, 0)
            grid.addWidget(kEdit, 1, 1, )
            grid.addWidget(lbl3, 2, 0)
            grid.addWidget(k1Edit, 2, 1)

            grid.addWidget(k0Edit, 3, 0, 1, 2, Qt.AlignRight)

            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 5, 0, 1, 3, Qt.AlignCenter)
            
            logo = QLabel()
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 1, 1, 1, Qt.AlignRight)
              
            applyBtn = QPushButton('Zoeken')
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn, extra={"event.action": "__init__"})
            applyBtn.clicked.connect(self.accept)
   
            grid.addWidget(applyBtn, 4, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Sluiten')
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn, extra={"event.action": "__init__"})
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
    
            grid.addWidget(cancelBtn, 4, 0, 1, 2,Qt.AlignCenter)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            infoBtn = QPushButton('Informatie')
            logger.debug("__init__(parent=%s): infoBtn → %s", parent, infoBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): infoBtn → %s", self, parent, infoBtn, extra={"event.action": "__init__"})
            infoBtn.clicked.connect(lambda: info())
    
            grid.addWidget(infoBtn, 4, 0)
            infoBtn.setFont(QFont("Arial",10))
            infoBtn.setFixedWidth(100)
            infoBtn.setStyleSheet("color: black;  background-color: gainsboro")

        def kChanged(self, text):
            logger.warning(">>> Entering kChanged(text=%s)", text, extra={"event.action": "kChanged", "logrite.text": text})
            self.Calculatie.setText(text)
            logger.debug("<<< Exiting kChanged(text=%s)", text, extra={"event.action": "kChanged", "logrite.text": text})

        def k0Changed(self, text):
            logger.warning(">>> Entering k0Changed(text=%s)", text, extra={"event.action": "k0Changed", "logrite.text": text})
            self.Keuze.setText(text)
            logger.debug("<<< Exiting k0Changed(text=%s)", text, extra={"event.action": "k0Changed", "logrite.text": text})

        def k1Changed(self, text):
            logger.warning(">>> Entering k1Changed(text=%s)", text, extra={"event.action": "k1Changed", "logrite.text": text})
            self.Werkomschrijving.setText(text)
            logger.debug("<<< Exiting k1Changed(text=%s)", text, extra={"event.action": "k1Changed", "logrite.text": text})

        def returnk(self):
            logger.warning(">>> Entering returnk()", extra={"event.action": "returnk"})
            logger.debug("<<< Exiting returnk()", extra={"event.action": "returnk"})
            return self.Calculatie.text()

        def returnk0(self):
            logger.warning(">>> Entering returnk0()", extra={"event.action": "returnk0"})
            logger.debug("<<< Exiting returnk0()", extra={"event.action": "returnk0"})
            return self.Keuze.text()

        def returnk1(self):
            logger.warning(">>> Entering returnk1()", extra={"event.action": "returnk1"})
            logger.debug("<<< Exiting returnk1()", extra={"event.action": "returnk1"})
            return self.Werkomschrijving.text()

        @staticmethod
        def getData(parent=None):
            logger.warning(">>> Entering getData(parent=%s)", parent, extra={"event.action": "getData"})
            dialog = Widget(parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog, extra={"event.action": "getData"})
            dialog.exec_()
            logger.debug("<<< Exiting getData(parent=%s)", parent, extra={"event.action": "getData"})
            return [dialog.returnk0(), dialog.returnk(), dialog.returnk1()]

    window = Widget()
    data = window.getData()
    keuze = ''
    if not data[0] or data[0][0] == ' ':
        ongInvoer()
        zoeken(m_email)
    elif data[0]:
        keuze = data[0][0]
    if data[1] == '' or int(data[1]) > mcalnr:
        mcalnr += 1
        gerCalnr(mcalnr)
    elif data[1]:
        mcalnr = int(data[1])
    if data[2]:
        mwerkomschr = data[2]
    scontr = select([calculaties]).where(calculaties.c.calculatie == mcalnr)
    rpcontr = con.execute(scontr).first()

    if rpcontr and rpcontr[2] == 2:
        calcGekoppeld()
        zoeken(m_email)
    elif rpcontr and rpcontr[2] == 1:
        schoonCalculatie(mcalnr, m_email)
    toonClusters(m_email, keuze, mcalnr, mwerkomschr)
    
def toonClusters(m_email, keuze, mcalnr, mwerkomschr):
    logger.warning(">>> Entering toonClusters(m_email=%s,keuze=%s,mcalnr=%s,mwerkomschr=%s)", m_email, keuze, mcalnr, mwerkomschr, extra={"event.action": "toonClusters", "logrite.keuze": keuze, "logrite.mcalnr": mcalnr, "logrite.mwerkomschr": mwerkomschr})
    class MyWindow(QDialog):
        def __init__(self, data_list, header, *args):
            logger.warning(">>> Entering __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})
            QWidget.__init__(self, *args,)
            self.setGeometry(100, 50, 900, 900)
            self.setWindowTitle('Clustercalculatie extern werk')
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
            table_view.resizeColumnsToContents()
            table_view.setSelectionBehavior(QTableView.SelectRows)
            table_view.clicked.connect(showSelection)
            layout = QVBoxLayout(self)
            logger.debug("__init__(data_list=%s,header=%s): layout → %s", data_list, header, layout, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): layout → %s", self, data_list, header, layout, extra={"event.action": "__init__", "logrite.data_list": data_list})
            layout.addWidget(table_view)
            self.setLayout(layout)
            logger.debug("<<< Exiting __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})
    
    class MyTableModel(QAbstractTableModel):
        def __init__(self, parent, mylist, header, *args):
            logger.warning(">>> Entering __init__(parent=%s,mylist=%s,header=%s)", parent, mylist, header, extra={"event.action": "__init__", "logrite.mylist": mylist})
            logger.debug("__init__(self=%s,parent=%s,mylist=%s,header=%s): self.mylist → %s", self, parent, mylist, header, self.mylist, extra={"event.action": "__init__", "logrite.mylist": mylist})
            logger.debug("__init__(self=%s,parent=%s,mylist=%s,header=%s): self.header → %s", self, parent, mylist, header, self.header, extra={"event.action": "__init__", "logrite.mylist": mylist})
            QAbstractTableModel.__init__(self, parent, *args)
            logger.debug("<<< Exiting __init__(parent=%s,mylist=%s,header=%s)", parent, mylist, header, extra={"event.action": "__init__", "logrite.mylist": mylist})
            self.mylist = mylist
            logger.warning(">>> Entering __init__()", extra={"event.action": "__init__"})
            logger.debug("__init__(): grid → %s", grid, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): grid → %s", self, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.lbl → %s", self.lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.pixmap → %s", self.pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl → %s", self, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.logo → %s", self.logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): logo → %s", self, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Hoeveelheid → %s", self.Hoeveelheid, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.hoev → %s", self.hoev, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): hoev → %s", self, hoev, extra={"event.action": "__init__"})
            logger.debug("__init__(): reg_ex → %s", reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): reg_ex → %s", self, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(): input_validator → %s", input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): input_validator → %s", self, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.cancelBtn → %s", self.cancelBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): cancelBtn → %s", self, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.applyBtn → %s", self.applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): applyBtn → %s", self, applyBtn, extra={"event.action": "__init__"})
            logger.debug("<<< Exiting __init__()", extra={"event.action": "__init__"})
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
            logger.warning(">>> Entering headerData(col=%s,orientation=%s,role=%s)", col, orientation, role, extra={"event.action": "headerData", "logrite.col": col, "logrite.orientation": orientation, "logrite.role": role})
            if orientation == Qt.Horizontal and role == Qt.DisplayRole:
                return self.header[col]
            logger.debug("<<< Exiting headerData(col=%s,orientation=%s,role=%s)", col, orientation, role, extra={"event.action": "headerData", "logrite.col": col, "logrite.orientation": orientation, "logrite.role": role})
            return None
             
    header = ['Clusternr', 'Omschrijving', 'Prijs', 'Eenheid', 'Materialen', 'Lonen',\
              'Diensten', 'Materiëel', 'Inhuur']
    
    metadata = MetaData()
    
    clusters = Table('clusters', metadata,
        Column('clusterID', Integer(), primary_key=True),
        Column('omschrijving', String),
        Column('prijs', Float),
        Column('eenheid', String),
        Column('materialen', Float),
        Column('lonen', Float),
        Column('diensten', Float),
        Column('materieel', Float),
        Column('inhuur', Float))
     
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()

    if keuze == '0':
        sel = select([clusters]).order_by(clusters.c.clusterID)
    elif keuze:
        sel = select([clusters]).where(clusters.c.clusterID.ilike(keuze+'%'))\
                              .order_by(clusters.c.clusterID)
  
    if con.execute(sel).fetchone():
        rp = con.execute(sel)
    else:
        geenRecord()
     
    data_list=[]
    for row in rp:
        data_list += [(row)]
        
    def showSelection(idx):
        logger.warning(">>> Entering showSelection(idx=%s)", idx, extra={"event.action": "showSelection", "logrite.idx": idx})
        clusternr = str(idx.data())
        logger.debug("showSelection(idx=%s): clusternr → %s", idx, clusternr, extra={"event.action": "showSelection", "logrite.idx": idx})
        if idx.column() == 0:
            metadata = MetaData()
            logger.debug("showSelection(idx=%s): metadata → %s", idx, metadata, extra={"event.action": "showSelection", "logrite.idx": idx})
            clusters = Table('clusters', metadata,
                Column('clusterID', Integer(), primary_key=True),
                Column('omschrijving', String))
            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            logger.debug("showSelection(idx=%s): engine → %s", idx, engine, extra={"event.action": "showSelection", "logrite.idx": idx})
            con = engine.connect()
            selcl = select([clusters]).where(clusters.c.clusterID == clusternr.upper())
            logger.debug("showSelection(idx=%s): con → %s", idx, con, extra={"event.action": "showSelection", "logrite.idx": idx})
            rpcl = con.execute(selcl).first()
            class MainWindow(QDialog):
                logger.debug("showSelection(idx=%s): selcl → %s", idx, selcl, extra={"event.action": "showSelection", "logrite.idx": idx})
                def __init__(self):
                    logger.debug("<<< Exiting showSelection(idx=%s)", idx, extra={"event.action": "showSelection", "logrite.idx": idx})
                    QDialog.__init__(self)
                    logger.warning(">>> Entering __init__()", extra={"event.action": "__init__"})
                    
                    grid = QGridLayout()
                    grid.setSpacing(20)
                    
                    self.lbl = QLabel()
                    self.pixmap = QPixmap('./images/logos/verbinding.jpg')
                    self.lbl.setPixmap(self.pixmap)
                    grid.addWidget(self.lbl , 0, 1)
            
                    self.logo = QLabel()
                    self.pixmap = QPixmap('./images/logos/logo.jpg')
                    self.logo.setPixmap(self.pixmap)
                    grid.addWidget(self.logo , 0, 2, 1, 1, Qt.AlignRight)
                      
                    self.setFont(QFont('Arial', 10))
                    grid.addWidget(QLabel('Calculatienummer:          '+str(mcalnr)), 1, 1, 1, 3)
                    self.setFont(QFont('Arial', 10))
                    grid.addWidget(QLabel('Clusternummer               '+str(clusternr)+\
                           '\n'+rpcl[1]), 2, 1, 1, 3)
                               
                    self.setWindowTitle("Clustercalculatie  extern werk maken") 
                    self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
                    self.setFont(QFont('Arial', 10))
                                       
                    self.Hoeveelheid = QLabel(self)
                    self.Hoeveelheid.setText('Hoeveelheid ')
                    self.hoev = QLineEdit(self)
                    self.hoev.setFixedWidth(100)
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, self.hoev)
                    self.hoev.setValidator(input_validator)
                    
                    grid.addWidget(self.Hoeveelheid, 3, 1)
                    grid.addWidget(self.hoev, 3, 2)
                    
                    grid.addWidget(QLabel(' \u00A9 2017 all rights reserved\n     dj.jansen@casema.nl'), 5, 0, 1, 3, Qt.AlignCenter)
                    
                    self.cancelBtn = QPushButton('Sluiten')
                    self.cancelBtn.clicked.connect(self.close)
                    grid.addWidget(self.cancelBtn, 4, 1, 1, 1, Qt.AlignRight)
                    self.cancelBtn.setFont(QFont("Arial",10))
                    self.cancelBtn.setFixedWidth(100)
                    self.cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
                                                             
                    self.applyBtn = QPushButton('Invoeren', self)
                    self.applyBtn.clicked.connect(self.clickMethod)
                    grid.addWidget(self.applyBtn, 4, 2, 1, 1, Qt.AlignRight)
                    self.applyBtn.setFont(QFont("Arial",10))
                    self.applyBtn.setFixedWidth(100)
                    self.applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
                    
                    self.setLayout(grid)
                    self.setGeometry(500, 100, 150, 150)
                    logger.debug("<<< Exiting __init__()", extra={"event.action": "__init__"})

                def clickMethod(self):
                    logger.warning(">>> Entering clickMethod()", extra={"event.action": "clickMethod"})
                    mhoev = self.hoev.text()
                    logger.debug("clickMethod(): mhoev → %s", mhoev, extra={"event.action": "clickMethod"})
                    if mhoev == '' or mhoev == ' ':
                        logger.debug("<<< Exiting clickMethod()", extra={"event.action": "clickMethod"})
                        return
                    mhoev = float(str(mhoev))

                    metadata = MetaData()
                    logger.debug("clickMethod(self=%s): metadata → %s", self, metadata, extra={"event.action": "clickMethod"})
                    clusters = Table('clusters', metadata,
                         Column('clusterID', Integer(), primary_key=True),
                         Column('omschrijving', String),
                         Column('eenheid', String),
                         Column('prijs', Float))
                    calculaties = Table('calculaties', metadata,
                         Column('calcID', Integer(), primary_key=True),
                         Column('clusterID', None, ForeignKey('clusters.clusterID')),
                         Column('omschrijving', String),
                         Column('hoeveelheid', Float),
                         Column('eenheid', String),
                         Column('prijs', Float),
                         Column('calculatie', Integer),
                         Column('calculatiedatum', String),
                         Column('werkomschrijving', String))

                    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
                    logger.debug("clickMethod(self=%s): engine → %s", self, engine, extra={"event.action": "clickMethod"})
                    con = engine.connect()
                    logger.debug("clickMethod(self=%s): con → %s", self, con, extra={"event.action": "clickMethod"})
                    sel = select([clusters.c.clusterID, clusters.c.omschrijving, clusters.c.eenheid, \
                                  clusters.c.prijs]).where(clusters.c.clusterID == clusternr)
                    rpsel = con.execute(sel).first()
                    logger.debug("clickMethod(self=%s): rpsel → %s", self, rpsel, extra={"event.action": "clickMethod"})
                    momschr = rpsel[1]
                    logger.debug("clickMethod(self=%s): momschr → %s", self, momschr, extra={"event.action": "clickMethod"})
                    meenh = rpsel[2]
                    logger.debug("clickMethod(self=%s): meenh → %s", self, meenh, extra={"event.action": "clickMethod"})
                    mprijs = rpsel[3]
                    logger.debug("clickMethod(self=%s): mprijs → %s", self, mprijs, extra={"event.action": "clickMethod"})
                    mcaldat = str(datetime.datetime.now())[0:10]
                    logger.debug("clickMethod(self=%s): mcaldat → %s", self, mcaldat, extra={"event.action": "clickMethod"})

                    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
                    con = engine.connect()
                    selcalc = select([calculaties.c.clusterID, calculaties.c.calculatie])\
                        .where(and_(calculaties.c.clusterID == clusternr, calculaties.c.calculatie == mcalnr))
                    logger.debug("clickMethod(self=%s): selcalc → %s", self, selcalc, extra={"event.action": "clickMethod"})
                    rpcalc = con.execute(selcalc).first()
                    logger.debug("clickMethod(self=%s): rpcalc → %s", self, rpcalc, extra={"event.action": "clickMethod"})
                    if rpcalc:
                        calcBestaat()
                        upd = update(calculaties) \
                            .where(and_(calculaties.c.clusterID == clusternr, calculaties.c.calculatie == mcalnr)).values\
                            (hoeveelheid=calculaties.c.hoeveelheid + mhoev,calculatiedatum=mcaldat, werkomschrijving=mwerkomschr)
                        logger.debug("clickMethod(self=%s): upd → %s", self, upd, extra={"event.action": "clickMethod"})
                        con.execute(upd)
                    else:
                        mcalnrnr = (con.execute(select([func.max(calculaties.c.calcID, \
                                 type_=Integer).label('mcalnrnr')])).scalar())
                        mcalnrnr += 1
                        logger.debug("clickMethod(self=%s): mcalnrnr → %s", self, mcalnrnr, extra={"event.action": "clickMethod"})
                        ins = insert(calculaties).values(calcID=mcalnrnr, \
                             clusterID=clusternr, hoeveelheid=mhoev, omschrijving=momschr, eenheid=meenh, prijs=mprijs, \
                                 calculatie=mcalnr, calculatiedatum=mcaldat, werkomschrijving=mwerkomschr)
                        con.execute(ins)
                        invoerOK()
                    self.accept()
                    
            mainWin = MainWindow()
            mainWin.exec_()

    win = MyWindow(data_list, header)
    win.exec_()
    zoeken(m_email)