import datetime
from login import hoofdMenu
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QFont, QPixmap, QIcon, QRegExpValidator
from PyQt5.QtWidgets import QDialog, QLabel, QGridLayout,\
                             QPushButton, QMessageBox, QLineEdit
from sqlalchemy import (Table, Column, Integer, String, Float,\
                        MetaData, create_engine, ForeignKey)
from sqlalchemy.sql import select, update,  and_
import logging
logger = logging.getLogger(__name__)

def windowSluit(self, m_email):
    logger.debug(">>> Entering windowSluit(m_email=%s)", m_email)
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email)
    
def foutWerknr():
    logger.debug(">>> Entering foutWerknr()")
    msg = QMessageBox()
    logger.debug("foutWerknr(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Werknummer niet aanwezig!')
    msg.setWindowTitle('Koppel begroting')
    logger.debug("<<< Exiting foutWerknr()")
    msg.exec_()
    
def gekoppeld():
    logger.debug(">>> Entering gekoppeld()")
    msg = QMessageBox()
    logger.debug("gekoppeld(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Critical)
    msg.setText('Werknummer is reeds gekoppeld!')
    msg.setWindowTitle('Koppel begroting')
    logger.debug("<<< Exiting gekoppeld()")
    msg.exec_()
    
def verwFout(mwerknr):
    logger.debug(">>> Entering verwFout(mwerknr=%s)", mwerknr)
    msg = QMessageBox()
    logger.debug("verwFout(mwerknr=%s): msg → %s", mwerknr, msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Koppeling heeft al plaatsgevonden\nde begrote gegevens zijn eerder\nnaar werk '+str(mwerknr)+' overgezet!')
    msg.setWindowTitle('Koppel begroting')
    logger.debug("<<< Exiting verwFout(mwerknr=%s)", mwerknr)
    msg.exec_()
    
def foutCalc():
    logger.debug(">>> Entering foutCalc()")
    msg = QMessageBox()
    logger.debug("foutCalc(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Calculatie niet aanwezig!')
    msg.setWindowTitle('Koppel begroting')
    logger.debug("<<< Exiting foutCalc()")
    msg.exec_()
        
def geenOpdracht():
    logger.debug(">>> Entering geenOpdracht()")
    msg = QMessageBox()
    logger.debug("geenOpdracht(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Nog geen opdracht aanwezig!')
    msg.setWindowTitle('Koppel begroting')
    logger.debug("<<< Exiting geenOpdracht()")
    msg.exec_()

def gegevensOk():
    logger.debug(">>> Entering gegevensOk()")
    msg = QMessageBox()
    logger.debug("gegevensOk(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Information)
    msg.setText('Transfer is gelukt!')
    msg.setWindowTitle('Koppel begroting')
    logger.debug("<<< Exiting gegevensOk()")
    msg.exec_()

def noLinking():
    logger.debug(">>> Entering noLinking()")
    msg = QMessageBox()
    logger.debug("noLinking(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Critical)
    msg.setText('Geen koppeling mogelijk, verwerf eerst de opdracht!')
    msg.setWindowTitle('Koppel calculatie')
    logger.debug("<<< Exiting noLinking()")
    msg.exec_()

def zoekBegroting(m_email):
    logger.debug(">>> Entering zoekBegroting(m_email=%s)", m_email)
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.debug(">>> Entering __init__(parent=%s)", parent)
            self.setWindowTitle("Calculatie koppelen")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap)
            logger.debug("__init__(parent=%s): input_validator → %s", parent, input_validator)
    
            self.setFont(QFont('Arial', 10))
                                      
            self.Calculatie = QLabel()
            logger.debug("__init__(parent=%s): self.Calculatie → %s", parent, self.Calculatie)
            zkcalcEdit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): zkcalcEdit → %s", self, parent, zkcalcEdit)
            logger.debug("__init__(parent=%s): zkcalcEdit → %s", parent, zkcalcEdit)
            zkcalcEdit.setFixedWidth(100)
            zkcalcEdit.setFont(QFont("Arial",10))
            zkcalcEdit.textChanged.connect(self.zkcalcChanged)
            reg_ex = QRegExp('^[1-9]{1}[0-9]{0,8}$')
            logger.debug("__init__(self=%s,parent=%s): reg_ex → %s", self, parent, reg_ex)
            logger.debug("__init__(parent=%s): reg_ex → %s", parent, reg_ex)
            input_validator = QRegExpValidator(reg_ex, zkcalcEdit)
            logger.debug("__init__(self=%s,parent=%s): input_validator → %s", self, parent, input_validator)
            zkcalcEdit.setValidator(input_validator)  
            
            self.Werknummer = QLabel()
            logger.debug("__init__(parent=%s): self.Werknummer → %s", parent, self.Werknummer)
            zkwerknrEdit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): zkwerknrEdit → %s", self, parent, zkwerknrEdit)
            logger.debug("__init__(parent=%s): zkwerknrEdit → %s", parent, zkwerknrEdit)
            zkwerknrEdit.setFixedWidth(100)
            zkwerknrEdit.setFont(QFont("Arial",10))
            zkwerknrEdit.textChanged.connect(self.zkwerknrChanged)
            reg_ex = QRegExp('^[8]{1}[0-9]{8}$')
            input_validator = QRegExpValidator(reg_ex, zkwerknrEdit)
            zkwerknrEdit.setValidator(input_validator)

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
            grid.addWidget(lbl , 0, 0)
            
            lbl1 = QLabel('Calculatienummer')  
            logger.debug("__init__(self=%s,parent=%s): lbl1 → %s", self, parent, lbl1)
            logger.debug("__init__(parent=%s): lbl1 → %s", parent, lbl1)
            lbl1.setAlignment(Qt.AlignRight)
            grid.addWidget(lbl1, 3, 0)
            grid.addWidget(zkcalcEdit, 3, 1)
            
            lbl2 = QLabel('Werknummer')
            logger.debug("__init__(self=%s,parent=%s): lbl2 → %s", self, parent, lbl2)
            logger.debug("__init__(parent=%s): lbl2 → %s", parent, lbl2)
            lbl2.setAlignment(Qt.AlignRight)
            grid.addWidget(lbl2, 4, 0)
            grid.addWidget(zkwerknrEdit, 4, 1)

            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 7, 0, 1, 2, Qt.AlignRight)
             
            logo = QLabel()
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo)
            logger.debug("__init__(parent=%s): logo → %s", parent, logo)
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 0, 1, 2, Qt.AlignRight)
   
            applyBtn = QPushButton('Zoeken')
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn)
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn)
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 6, 1)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Sluiten')
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn)
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn)
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
    
            grid.addWidget(cancelBtn, 6, 0, 1, 1,Qt.AlignRight)
            logger.debug("<<< Exiting __init__(parent=%s)", parent)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
             
        def zkcalcChanged(self, text):
            logger.debug(">>> Entering zkcalcChanged(text=%s)", text)
            logger.debug("zkcalcChanged(self=%s,text=%s): Calculatie → %s", self, text, Calculatie)
            self.Calculatie.setText(text)
            logger.debug("<<< Exiting zkcalcChanged(text=%s)", text)
            
        def zkwerknrChanged(self, text):
            logger.debug(">>> Entering zkwerknrChanged(text=%s)", text)
            logger.debug("zkwerknrChanged(self=%s,text=%s): Werknummer → %s", self, text, Werknummer)
            self.Werknummer.setText(text)
            logger.debug("<<< Exiting zkwerknrChanged(text=%s)", text)

        def returnCalculatie(self):
            logger.debug(">>> Entering returnCalculatie()")
            logger.debug("<<< Exiting returnCalculatie()")
            return self.Calculatie.text()
        
        def returnWerknummer(self):
            logger.debug(">>> Entering returnWerknummer()")
            logger.debug("<<< Exiting returnWerknummer()")
            return self.Werknummer.text()

        @staticmethod
        def getData(parent=None):
            logger.debug(">>> Entering getData(parent=%s)", parent)
            dialog = Widget(parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog)
            dialog.exec_()
            logger.debug("<<< Exiting getData(parent=%s)", parent)
            return [dialog.returnCalculatie(), dialog.returnWerknummer()]

    window = Widget()
    data = window.getData()
    if not data[0] or not data[1]:
        zoekBegroting(m_email)
    mcalnr = int(data[0])
    mwerknr = int(data[1])

    metadata = MetaData()
    calculaties = Table('calculaties', metadata,
        Column('calculatie', Integer),
        Column('werkomschrijving', String),
        Column('verwerkt', Integer))
    werken = Table('werken', metadata,
        Column('werknummerID', Integer, primary_key=True),
        Column('opdracht_datum', String),
        Column('calculatienummer', String))
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
    selcl = select([calculaties]).where(calculaties.c.calculatie == mcalnr)
    rpcl = con.execute(selcl).first()
    selwrk = select([werken]).where(werken.c.werknummerID == mwerknr)
    rpwerk = con.execute(selwrk).first()
    if not rpcl:
        foutCalc()
        zoekBegroting(m_email)
    if not rpwerk:
        foutWerknr()
        zoekBegroting(m_email)
    mcalnr = rpcl[0]
    mwerknr = data[1]
    mwerkomschr = rpcl[1]
    if rpwerk[1]:
        mverw = 1
    else:
        noLinking()
        zoekBegroting(m_email)
    verder = False
    if rpcl and mverw == 1:
        verder = True
    elif rpcl and mverw > 1:
        verwFout(mwerknr)
        zoekBegroting(m_email)
    if rpwerk and rpwerk[1] == '':
        geenOpdracht()
        zoekBegroting(m_email)
    elif rpwerk[2] > 0:
        gekoppeld()
        zoekBegroting(m_email)
    elif rpwerk and rpwerk[1] and verder:
        koppelCalc(mcalnr, mwerknr, mwerkomschr, m_email)

def koppelCalc(mcalnr, mwerknr, mwerkomschr, m_email):
    logger.debug(">>> Entering koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s)", mcalnr, mwerknr, mwerkomschr, m_email)
    msgBox=QMessageBox()
    logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): msgBox → %s", mcalnr, mwerknr, mwerkomschr, m_email, msgBox)
    msgBox.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msgBox.setWindowTitle("Begroting Koppelen")
    msgBox.setIcon(QMessageBox.Warning)
    msgBox.setText('Omschrijving: '+mwerkomschr+'\nDeze calculatie alleen koppelen\nindien gegevens definitief zijn\nDoorgaan?')
    msgBox.setStandardButtons(QMessageBox.Yes)
    msgBox.addButton(QMessageBox.No)
    msgBox.setDefaultButton(QMessageBox.Yes)
    if(msgBox.exec_() == QMessageBox.Yes):
        metadata = MetaData()
        logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): metadata → %s", mcalnr, mwerknr, mwerkomschr, m_email, metadata)
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
            Column('verwerkt', Integer),
            Column('leiding', Float),
            Column('huisvesting', Float),
            Column('kabelwerk', Float),
            Column('grondverzet', Float),
            Column('betonwerk', Float),
            Column('vervoer', Float),
            Column('overig', Float))
        werken = Table('werken', metadata,
            Column('werknummerID', Integer(), primary_key=True),
            Column('aanneemsom', Float),
            Column('begr_materialen', Float),
            Column('begr_materieel', Float),
            Column('begr_inhuur', Float),
            Column('begr_constr_uren', Float),
            Column('begr_mont_uren', Float),
            Column('begr_retourlas_uren', Float),
            Column('begr_telecom_uren', Float),
            Column('begr_bfi_uren', Float),
            Column('begr_voeding_uren', Float),
            Column('begr_bvl_uren', Float),
            Column('begr_spoorleg_uren', Float),
            Column('begr_spoorlas_uren', Float),
            Column('begr_lonen', Float),
            Column('werkomschrijving', String),
            Column('calculatienummer', Integer),
            Column('begr_leiding', Float),
            Column('begr_huisv', Float),
            Column('begr_kabelwerk', Float),
            Column('begr_grondverzet', Float),
            Column('begr_beton_bvl', Float),
            Column('begr_vervoer', Float),
            Column('begr_overig', Float),
            Column('begr_sleuvengraver_uren', Float),
            Column('begr_persapparaat_uren', Float),
            Column('begr_atlaskraan_uren', Float),
            Column('begr_kraan_groot_uren', Float),
            Column('begr_mainliner_uren', Float),
            Column('begr_hormachine_uren', Float),
            Column('begr_wagon_uren', Float),
            Column('begr_locomotor_uren', Float),
            Column('begr_locomotief_uren', Float),
            Column('begr_montagewagen_uren', Float),
            Column('begr_stormobiel_uren', Float),
            Column('begr_robeltrein_uren', Float))
        engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
        logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): engine → %s", mcalnr, mwerknr, mwerkomschr, m_email, engine)
        con = engine.connect()
        selcal = select([calculaties]).where(calculaties.c.calculatie == mcalnr)
        logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): con → %s", mcalnr, mwerknr, mwerkomschr, m_email, con)
        rpcal = con.execute(selcal)

        logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): selcal → %s", mcalnr, mwerknr, mwerkomschr, m_email, selcal)
        logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): rpcal → %s", mcalnr, mwerknr, mwerkomschr, m_email, rpcal)
        for regel in rpcal:
            updwerk = update(werken).where(werken.c.werknummerID == mwerknr)\
              .values(aanneemsom = werken.c.aanneemsom+regel[7],\
              begr_materialen = werken.c.begr_materialen+regel[8],\
              begr_materieel = werken.c.begr_materieel+regel[11],\
              begr_lonen = werken.c.begr_lonen+regel[9],\
              begr_inhuur = werken.c.begr_inhuur+regel[12],\
              begr_constr_uren = werken.c.begr_constr_uren+regel[13],\
              begr_mont_uren = werken.c.begr_mont_uren+regel[14],\
              begr_retourlas_uren = werken.c.begr_retourlas_uren+regel[15],\
              begr_telecom_uren = werken.c.begr_telecom_uren + regel[16],\
              begr_bfi_uren = werken.c.begr_bfi_uren + regel[17],\
              begr_voeding_uren = werken.c.begr_voeding_uren + regel[18],\
              begr_bvl_uren = werken.c.begr_bvl_uren + regel[19] ,\
              begr_spoorleg_uren = werken.c.begr_spoorleg_uren + regel[20],\
              begr_spoorlas_uren = werken.c.begr_spoorlas_uren + regel[21],\
              begr_leiding = werken.c.begr_leiding + regel[37],\
              begr_huisv = werken.c.begr_huisv + regel[38],\
              begr_kabelwerk = werken.c.begr_kabelwerk + regel[39],\
              begr_grondverzet = werken.c.begr_grondverzet + regel[40],\
              begr_beton_bvl = werken.c.begr_beton_bvl + regel[41],\
              begr_vervoer = werken.c.begr_vervoer + regel[42],\
              begr_overig = werken.c.begr_overig + regel[43],\
              calculatienummer = mcalnr, \
              begr_sleuvengraver_uren=werken.c.begr_sleuvengraver_uren + regel[23], \
              begr_persapparaat_uren=werken.c.begr_persapparaat_uren + regel[24], \
              begr_atlaskraan_uren=werken.c.begr_atlaskraan_uren + regel[25], \
              begr_kraan_groot_uren=werken.c.begr_kraan_groot_uren + regel[26], \
              begr_mainliner_uren=werken.c.begr_mainliner_uren + regel[27], \
              begr_hormachine_uren=werken.c.begr_hormachine_uren + regel[28], \
              begr_locomotor_uren=werken.c.begr_locomotor_uren + regel[29], \
              begr_locomotief_uren=werken.c.begr_locomotief_uren + regel[30], \
              begr_montagewagen_uren=werken.c.begr_montagewagen_uren + regel[31], \
              begr_stormobiel_uren=werken.c.begr_stormobiel_uren + regel[32], \
              begr_robeltrein_uren=werken.c.begr_robeltrein_uren + regel[33])
            logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): updwerk → %s", mcalnr, mwerknr, mwerkomschr, m_email, updwerk)
            logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): begr_materialen → %s", mcalnr, mwerknr, mwerkomschr, m_email, begr_materialen)
            logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): begr_materieel → %s", mcalnr, mwerknr, mwerkomschr, m_email, begr_materieel)
            con.execute(updwerk)

        updcal = update(calculaties).where(calculaties.c.calculatie == mcalnr) \
            .values(koppelnummer=mwerknr, werkomschrijving=mwerkomschr, verwerkt=1)
        logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): begr_inhuur → %s", mcalnr, mwerknr, mwerkomschr, m_email, begr_inhuur)
        logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): begr_lonen → %s", mcalnr, mwerknr, mwerkomschr, m_email, begr_lonen)
        logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): begr_constr_uren → %s", mcalnr, mwerknr, mwerkomschr, m_email, begr_constr_uren)
        logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): begr_mont_uren → %s", mcalnr, mwerknr, mwerkomschr, m_email, begr_mont_uren)
        con.execute(updcal)

        materiaallijsten = Table('materiaallijsten', metadata,
            Column('matlijstID', Integer, primary_key=True),
            Column('calculatie', Integer),
            Column('hoeveelheid', Float),
            Column('artikelID', None, ForeignKey('artikelen.artikelID')),
            Column('werknummerID', Integer),
            Column('orderinkoopID', Integer),
            Column('reserverings_datum', String),
            Column('levertijd_begin', String),
            Column('levertijd_end', String),
            Column('categorie', Integer))
        artikelen = Table('artikelen', metadata,
            Column('artikelID', Integer(), primary_key=True),
            Column('reserveringsaldo', Float),
            Column('categorie', Integer),
            Column('bestelsaldo', Float))
   
        engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
        con = engine.connect()
        selmat = select([materiaallijsten, artikelen]).where(and_(materiaallijsten.\
            c.calculatie == mcalnr, materiaallijsten.c.artikelID == artikelen.c.artikelID))
        logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): begr_spoorleg_uren → %s", mcalnr, mwerknr, mwerkomschr, m_email, begr_spoorleg_uren)
        logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): begr_spoorlas_uren → %s", mcalnr, mwerknr, mwerkomschr, m_email, begr_spoorlas_uren)
        logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): begr_leiding → %s", mcalnr, mwerknr, mwerkomschr, m_email, begr_leiding)
        logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): begr_huisv → %s", mcalnr, mwerknr, mwerkomschr, m_email, begr_huisv)
        rpmat = con.execute(selmat)
        mboekd = str(datetime.datetime.now())[0:10]
        for row in rpmat:
           updres = update(materiaallijsten).where(and_(materiaallijsten.c.calculatie == mcalnr,\
             materiaallijsten.c.artikelID == artikelen.c.artikelID)).values(werknummerID = mwerknr,\
             reserverings_datum = mboekd, categorie = artikelen.c.categorie)
           logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): begr_kabelwerk → %s", mcalnr, mwerknr, mwerkomschr, m_email, begr_kabelwerk)
           logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): begr_grondverzet → %s", mcalnr, mwerknr, mwerkomschr, m_email, begr_grondverzet)
           con.execute(updres)
           updart = update(artikelen).where(and_(materiaallijsten.c.artikelID ==\
                artikelen.c.artikelID, materiaallijsten.c.calculatie == mcalnr))\
                .values(reserveringsaldo = artikelen.c.reserveringsaldo + materiaallijsten.c.hoeveelheid)
           logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): begr_vervoer → %s", mcalnr, mwerknr, mwerkomschr, m_email, begr_vervoer)
           logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): begr_beton_bvl → %s", mcalnr, mwerknr, mwerkomschr, m_email, begr_beton_bvl)
           logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): begr_overig → %s", mcalnr, mwerknr, mwerkomschr, m_email, begr_overig)
           logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): calculatienummer → %s", mcalnr, mwerknr, mwerkomschr, m_email, calculatienummer)
           logger.debug("koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s): begr_sleuvengraver_uren → %s", mcalnr, mwerknr, mwerkomschr, m_email, begr_sleuvengraver_uren)
           con.execute(updart)
        gegevensOk()
        zoekBegroting(m_email)
    else:
        logger.debug("<<< Exiting koppelCalc(mcalnr=%s,mwerknr=%s,mwerkomschr=%s,m_email=%s)", mcalnr, mwerknr, mwerkomschr, m_email)
        hoofdMenu(m_email)