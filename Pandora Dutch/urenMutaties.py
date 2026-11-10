from login import hoofdMenu
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QIcon, QFont, QPixmap, QRegExpValidator
from PyQt5.QtWidgets import QLineEdit, QGridLayout, QDialog, QLabel,\
            QPushButton, QComboBox, QCheckBox
from sqlalchemy import (Table, Column, Integer, String, MetaData, create_engine,\
                        ForeignKey, Float, select, update, func, and_, Boolean)
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
    
def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    
def info():
    logger.warning(">>> Entering info()", extra={"event.action": "info"})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            self.setWindowTitle("Informatie ERP Systeem Pandora")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            self.setFont(QFont('Arial', 10))
            grid = QGridLayout()
            logger.debug("__init__(parent=%s): grid → %s", parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid, extra={"event.action": "__init__"})
            grid.setSpacing(20)
            
            lblinfo = QLabel('Informatie ERP Pandora')
            logger.debug("__init__(parent=%s): lblinfo → %s", parent, lblinfo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lblinfo → %s", self, parent, lblinfo, extra={"event.action": "__init__"})
            grid.addWidget(lblinfo, 0, 0, 1, 2, Qt.AlignCenter)
            lblinfo.setStyleSheet("color:rgba(45, 83, 115, 255); font: 25pt Comic Sans MS")
            
            logo = QLabel()
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            pixmap = QPixmap('./images/logos/logo.jpg')
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap, extra={"event.action": "__init__"})
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 0, 1, 1, Qt.AlignRight)
        
            lbl = QLabel()
            logger.debug("__init__(parent=%s): lbl → %s", parent, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl, extra={"event.action": "__init__"})
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl, 0, 0)
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            
            logger.warning(">>> Entering __init__()", extra={"event.action": "__init__"})
            logger.debug("__init__(): self.zkaccEdit → %s", self.zkaccEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): zkaccEdit → %s", self, zkaccEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(): reg_ex → %s", reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): reg_ex → %s", self, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(): input_validator → %s", input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): input_validator → %s", self, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.zkwerknEdit → %s", self.zkwerknEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): zkwerknEdit → %s", self, zkwerknEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.k0Edit → %s", self.k0Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): k0Edit → %s", self, k0Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.cBox → %s", self.cBox, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): cBox → %s", self, cBox, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.urenEdit → %s", self.urenEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): urenEdit → %s", self, urenEdit, extra={"event.action": "__init__"})
            logger.debug("<<< Exiting __init__()", extra={"event.action": "__init__"})
            logger.debug("__init__(): self.urentotEdit → %s", self.urentotEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): urentotEdit → %s", self, urentotEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.urenbegrEdit → %s", self.urenbegrEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): urenbegrEdit → %s", self, urenbegrEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.boekdatumEdit → %s", self.boekdatumEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): boekdatumEdit → %s", self, boekdatumEdit, extra={"event.action": "__init__"})
            infolbl = QLabel(
      '''
        \t\t\t\t\t\t\t\t\t\t 
                                        Informatie over te muteren uren.  
                                         
        De module start met de volgende variabele gegevens:
        Accountnummer: leeg veld in te vullen met accountnummer van de werknemer.
        Werknummer: leeg veld in te vullen met het werknummer, waarvoor wordt gewerkt.
        Aanwezig/Afwezig: kies hier de soort uren, waarvoor de boeking moet worden gedaan,
        bv. 100% reguliere uren, 125% overwerk, 150% overwerk, 200% overwerk, 
        of een van de diverse genoemde afwezigheidsuren voor verlof ziekte enz.
        Aantal uren: Uren die zijn gewerkt op de dag van de werkzaamheden.
        Bij het label voor de werkelijke totaaluren wordt de vakdiscipline aangegeven,
        waarvoor de uren zijn geboekt.
        Datum werkzaamheden:  datum van de huidige dag in het formaat jjjj-mm-dd
        Button 'Muteren' Standaard button met tekst 'Muteren'
        Bij het aanpassen of invullen van de velden 'Accountnummer', 'Werknummer' en
        'Datum werkzaamheden', zal het systeem bij opkomen van de velden de laatst
        ingetoetste gegevens onthouden, zodat een snelle invoer mogelijk is.
        De keuze Aanwezig/Afwezig zal standaard ingevuld worden met 100% uren,
        omdat dit de meest voorkomende keuze zal zijn.
        Bij het intoetsen van de gegevens zal  bij een juiste invoer de knop
        'Muteren' groen kleuren. Bij een foutieve of niet gelukte invoer zal de 
        knop 'Muteren' rood kleuren, in dit geval dient een korrektie te worden 
        gemaakt, omdat de invoer niet is geboekt!
        In het statusveld onder de invulvelden, wordt de status en informatie
        van de afwezigheidsuren getoond, b.v. bij verlofuren het verlofsaldo.
        Tevens worden in dit statusveld de foutmeldingen weergegeven, bij een
        ongeldige invoer.
   
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

def urenBoeking(self, m_email):
    logger.warning(">>> Entering urenBoeking(m_email=%s)", m_email, extra={"event.action": "urenBoeking"})
    maccountnr = self.zkaccEdit.text()
    logger.debug("urenBoeking(m_email=%s): maccountnr → %s", m_email, maccountnr, extra={"event.action": "urenBoeking"})
    logger.debug("urenBoeking(self=%s,m_email=%s): maccountnr → %s", self, m_email, maccountnr, extra={"event.action": "urenBoeking"})
    mwerknr = self.zkwerknEdit.text()
    logger.debug("urenBoeking(m_email=%s): mwerknr → %s", m_email, mwerknr, extra={"event.action": "urenBoeking"})
    logger.debug("urenBoeking(self=%s,m_email=%s): mwerknr → %s", self, m_email, mwerknr, extra={"event.action": "urenBoeking"})
    mboekd = self.boekdatumEdit.text()
    logger.debug("urenBoeking(self=%s,m_email=%s): mboekd → %s", self, m_email, mboekd, extra={"event.action": "urenBoeking"})
    mstatus = self.cBox.checkState()
    if mstatus == 0:
        mstatus = False
    else:
        logger.debug("urenBoeking(m_email=%s): mboekd → %s", m_email, mboekd, extra={"event.action": "urenBoeking"})
        mstatus = True
    metadata = MetaData()
    logger.debug("urenBoeking(m_email=%s): metadata → %s", m_email, metadata, extra={"event.action": "urenBoeking"})
    logger.debug("urenBoeking(self=%s,m_email=%s): metadata → %s", self, m_email, metadata, extra={"event.action": "urenBoeking"})
    wrkwnrln = Table('wrkwnrln', metadata,
        Column('wrkwnrurenID', Integer, primary_key=True),
        Column('werknemerID', None, ForeignKey('werknemers.werknemerID')),
        Column('werknummerID',Integer),       
        Column('loonID', None, ForeignKey('lonen.loonID')),
        Column('boekdatum', String),
        Column('aantaluren', Float),
        Column('tabelloon', Float),
        Column('reisloon', Float),
        Column('bruto_loonbedrag', Float),
        Column('meerwerkstatus', Boolean),
        Column('soort', String))
    werknemers = Table('werknemers', metadata,
        Column('werknemerID', Integer(), primary_key=True),
        Column('accountID', None, ForeignKey('accounts.accountID')),
        Column('loonID', None, ForeignKey('lonen.loonID')),
        Column('verlofsaldo', Float),
        Column('extraverlof', Float),
        Column('wnrloonID', Integer))
    logger.debug("urenBoeking(m_email=%s): selwnr → %s", m_email, selwnr, extra={"event.action": "urenBoeking"})
    werken = Table('werken', metadata,
        Column('werknummerID', Integer, primary_key=True),
        Column('kosten_lonen', Float),
        Column('voortgangstatus', String),
        Column('statusweek', String(6)),
        Column('begr_constr_uren', Float),
        Column('werk_constr_uren', Float),
        Column('begr_mont_uren', Float),
        Column('werk_mont_uren', Float),
        Column('begr_retourlas_uren', Float),
        Column('werk_retourlas_uren', Float),
        Column('begr_telecom_uren', Float),
        Column('werk_telecom_uren', Float),
        Column('begr_bfi_uren', Float),
        Column('werk_bfi_uren', Float),
        Column('begr_bvl_uren', Float),
        Column('werk_bvl_uren', Float),
        Column('begr_spoorleg_uren', Float),
        Column('werk_spoorleg_uren', Float),
        Column('begr_spoorlas_uren', Float),
        Column('werk_spoorlas_uren', Float),
        Column('begr_reis_uren', Float),
        Column('werk_reis_uren', Float),
        Column('meerminderwerk', Float),
        Column('begr_voeding_uren', Float),
        Column('werk_voeding_uren', Float))
    lonen = Table('lonen', metadata,
        Column('loonID', Integer, primary_key=True),
        Column('tabelloon', Float),
        Column('werkuur', Float),
        Column('reisuur', Float))
     
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("urenBoeking(m_email=%s): engine → %s", m_email, engine, extra={"event.action": "urenBoeking"})
    logger.debug("urenBoeking(self=%s,m_email=%s): engine → %s", self, m_email, engine, extra={"event.action": "urenBoeking"})
    logger.debug("urenBoeking(m_email=%s): rpwnr → %s", m_email, rpwnr, extra={"event.action": "urenBoeking"})
    logger.debug("urenBoeking(self=%s,m_email=%s): rpwnr → %s", self, m_email, rpwnr, extra={"event.action": "urenBoeking"})
    con = engine.connect()
    logger.debug("urenBoeking(self=%s,m_email=%s): con → %s", self, m_email, con, extra={"event.action": "urenBoeking"})
    logger.debug("urenBoeking(m_email=%s): con → %s", m_email, con, extra={"event.action": "urenBoeking"})
    selwnr = select([werknemers]).where(and_(werknemers.c.accountID==int(maccountnr),\
                     werknemers.c.loonID < 37))
    rpwnr = con.execute(selwnr).first()
    if rpwnr:
        maccountnr = int(maccountnr)
    else:
       self.urenEdit.setText('0')
       logger.debug("urenBoeking(self=%s,m_email=%s): urenEdit → %s", self, m_email, urenEdit, extra={"event.action": "urenBoeking"})
       logger.debug("urenBoeking(self=%s,m_email=%s): lblt → %s", self, m_email, lblt, extra={"event.action": "urenBoeking"})
       self.lblt.setStyleSheet("font: bold ; color: red")
       self.lblt.setText('Persoon niet in deze arbeidspool!')
       self.applyBtn.setStyleSheet("color: black; background-color: #FF3333")
       logger.debug("urenBoeking(self=%s,m_email=%s): applyBtn → %s", self, m_email, applyBtn, extra={"event.action": "urenBoeking"})
       return('', mwerknr, mboekd, m_email)
    if mwerknr and len(mwerknr)== 9  and _11check(mwerknr):
        mwerknr = int(mwerknr)
    else:
       self.urenEdit.setText('0')
       self.lblt.setStyleSheet("font: bold ; color: red")
       self.lblt.setText('Dit is geen geldig werknummer!')
       self.applyBtn.setStyleSheet("color: black; background-color: #FF3333")
       return(maccountnr, '', mboekd, m_email)
                
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
    selwerk = select([werken]).where(werken.c.werknummerID == mwerknr)
    rpwerk = con.execute(selwerk).first()
    logger.debug("urenBoeking(self=%s,m_email=%s): rpwerk → %s", self, m_email, rpwerk, extra={"event.action": "urenBoeking"})
   
    muren = 0
    logger.debug("urenBoeking(self=%s,m_email=%s): muren → %s", self, m_email, muren, extra={"event.action": "urenBoeking"})
    mu125 = 0
    logger.debug("urenBoeking(self=%s,m_email=%s): mu125 → %s", self, m_email, mu125, extra={"event.action": "urenBoeking"})
    mu150 = 0
    logger.debug("urenBoeking(self=%s,m_email=%s): mu150 → %s", self, m_email, mu150, extra={"event.action": "urenBoeking"})
    mu200 = 0
    logger.debug("urenBoeking(self=%s,m_email=%s): mu200 → %s", self, m_email, mu200, extra={"event.action": "urenBoeking"})
    mreis = 0
    logger.debug("urenBoeking(self=%s,m_email=%s): mreis → %s", self, m_email, mreis, extra={"event.action": "urenBoeking"})
    mmeerw100 = 0
    logger.debug("urenBoeking(self=%s,m_email=%s): mmeerw100 → %s", self, m_email, mmeerw100, extra={"event.action": "urenBoeking"})
    mmeerw125 = 0
    logger.debug("urenBoeking(self=%s,m_email=%s): mmeerw125 → %s", self, m_email, mmeerw125, extra={"event.action": "urenBoeking"})
    mmeerw150 = 0
    logger.debug("urenBoeking(self=%s,m_email=%s): mmeerw150 → %s", self, m_email, mmeerw150, extra={"event.action": "urenBoeking"})
    mmeerw200 = 0
    logger.debug("urenBoeking(self=%s,m_email=%s): mmeerw200 → %s", self, m_email, mmeerw200, extra={"event.action": "urenBoeking"})
    mverlof = 0
    logger.debug("urenBoeking(self=%s,m_email=%s): mverlof → %s", self, m_email, mverlof, extra={"event.action": "urenBoeking"})
    mextraverlof = 0
    logger.debug("urenBoeking(self=%s,m_email=%s): mextraverlof → %s", self, m_email, mextraverlof, extra={"event.action": "urenBoeking"})
    mziek = 0
    logger.debug("urenBoeking(self=%s,m_email=%s): mziek → %s", self, m_email, mziek, extra={"event.action": "urenBoeking"})
    mfeest = 0
    logger.debug("urenBoeking(self=%s,m_email=%s): mfeest → %s", self, m_email, mfeest, extra={"event.action": "urenBoeking"})
    mdokter = 0
    logger.debug("urenBoeking(self=%s,m_email=%s): mdokter → %s", self, m_email, mdokter, extra={"event.action": "urenBoeking"})
    mgverzuim = 0
    logger.debug("urenBoeking(self=%s,m_email=%s): mgverzuim → %s", self, m_email, mgverzuim, extra={"event.action": "urenBoeking"})
    moverzuim = 0
    logger.debug("urenBoeking(self=%s,m_email=%s): moverzuim → %s", self, m_email, moverzuim, extra={"event.action": "urenBoeking"})
            
    msoort = self.k0Edit.currentIndex()
    
    mboekuren = float(self.urenEdit.text())
    logger.debug("urenBoeking(self=%s,m_email=%s): mboekuren → %s", self, m_email, mboekuren, extra={"event.action": "urenBoeking"})
    
    mlist = ['100%','125%','150%','200%','Reis','Verlof','Extra verlof','Ziekte',\
            'Feestdag','Dokter','Geoorl. verzuim','Ong. verzuim']
    
    if rpwerk[2] == 'H':
        self.urenEdit.setText('0')
        self.lblt.setStyleSheet("font: bold ; color: red")
        self.lblt.setText('Werk is gereed en afgemeld!')
        self.applyBtn.setStyleSheet("color: black; background-color: #FF3333")
        return(maccountnr, mwerknr, mboekd, m_email)
    elif mboekuren and msoort == 0 and mstatus:
        mmeerw100 = mboekuren
    elif mboekuren and msoort == 0:
        muren = mboekuren
    elif mboekuren and msoort == 1 and mstatus:
        mmeerw125 = mboekuren
    elif mboekuren and msoort  == 1:
        mu125 = mboekuren 
    elif mboekuren and msoort == 2 and mstatus:
        mmeerw150 = mboekuren
    elif mboekuren and msoort == 2:
        mu150 = mboekuren
    elif mboekuren and msoort == 3 and mstatus:
        mmeerw200 = mboekuren
    elif mboekuren and msoort == 3:
        mu200 = mboekuren
    elif mboekuren and msoort == 4:
        mreis = mboekuren
    elif mboekuren and msoort == 5:
        mverlof = mboekuren
        upd = update(werknemers).where(werknemers.c.accountID ==\
            maccountnr).values(verlofsaldo = werknemers.c.verlofsaldo - mboekuren)
        con.execute(upd) 
    elif mboekuren and msoort == 6:
        mextraverlof = mboekuren
        upd = update(werknemers).where(werknemers.c.accountID ==\
            maccountnr).values(extraverlof = werknemers.c.extraverlof - mextraverlof)
        con.execute(upd) 
    elif mboekuren and msoort == 7:
        mziek = mboekuren
    elif mboekuren and msoort == 8:
        mfeest = mboekuren
    elif mboekuren and msoort == 9:
        mdokter = mboekuren
    elif mboekuren and msoort == 10:
        mgverzuim = mboekuren 
    elif mboekuren and msoort == 11:
        moverzuim = mboekuren  
    else:
        self.urenEdit.setText('0')
        self.lblt.setStyleSheet("font: bold;color: red")
        self.lblt.setText('Geen uren ingevoerd!')
        self.applyBtn.setStyleSheet("color: black; background-color: #FF3333")
        return(maccountnr, mwerknr, mboekd, m_email)
            
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
    try:
        mwrkwnruren=(con.execute(select([func.max(wrkwnrln.c.wrkwnrurenID,\
            type_=Integer)])).scalar())
    except:
        logger.error("Exception in urenBoeking(m_email=%s)", m_email, exc_info=True, extra={"event.action": "urenBoeking", "event.category": "process"})
        mwrkwnruren = 1
        logger.debug("urenBoeking(self=%s,m_email=%s): mwrkwnruren → %s", self, m_email, mwrkwnruren, extra={"event.action": "urenBoeking"})

    wrkgr = rpwnr[2]
    logger.debug("urenBoeking(self=%s,m_email=%s): wrkgr → %s", self, m_email, wrkgr, extra={"event.action": "urenBoeking"})
    wrkgr2 = rpwnr[5]
    logger.debug("urenBoeking(self=%s,m_email=%s): wrkgr2 → %s", self, m_email, wrkgr2, extra={"event.action": "urenBoeking"})
    loonsel = select([lonen]).where(lonen.c.loonID == wrkgr)    #tijd loonID voor werken
    loonsel2 = select([lonen]).where(lonen.c.loonID == wrkgr2)  #loonID voor lonen
    loonres = con.execute(loonsel).first()
    logger.debug("urenBoeking(self=%s,m_email=%s): loonres → %s", self, m_email, loonres, extra={"event.action": "urenBoeking"})
    loonres2 = con.execute(loonsel2).first()
    logger.debug("urenBoeking(self=%s,m_email=%s): loonres2 → %s", self, m_email, loonres2, extra={"event.action": "urenBoeking"})
    muurloon = loonres2[1]
    logger.debug("urenBoeking(self=%s,m_email=%s): muurloon → %s", self, m_email, muurloon, extra={"event.action": "urenBoeking"})
    mwerkuur = loonres[2]
    logger.debug("urenBoeking(self=%s,m_email=%s): mwerkuur → %s", self, m_email, mwerkuur, extra={"event.action": "urenBoeking"})
    mreisuur = loonres[3]
    logger.debug("urenBoeking(self=%s,m_email=%s): mreisuur → %s", self, m_email, mreisuur, extra={"event.action": "urenBoeking"})
    mwrku125 = mwerkuur*1.25
    logger.debug("urenBoeking(self=%s,m_email=%s): mwrku125 → %s", self, m_email, mwrku125, extra={"event.action": "urenBoeking"})
    mwrku150 = mwerkuur*1.5
    logger.debug("urenBoeking(self=%s,m_email=%s): mwrku150 → %s", self, m_email, mwrku150, extra={"event.action": "urenBoeking"})
    mwrku200 = mwerkuur*2
    logger.debug("urenBoeking(self=%s,m_email=%s): mwrku200 → %s", self, m_email, mwrku200, extra={"event.action": "urenBoeking"})
 
    loonk = (muren*mwerkuur)+(mreis*mreisuur)+(mu125*mwrku125)+(mu150*mwrku150)+\
             (mu200*mwrku200)+(mmeerw100*mwerkuur)+(mmeerw125*mwerkuur)+(mmeerw150*\
             mwerkuur)+(mmeerw200*mwerkuur)
    logger.debug("urenBoeking(self=%s,m_email=%s): loonk → %s", self, m_email, loonk, extra={"event.action": "urenBoeking"})
    meerk = (mmeerw100*mwerkuur)+(mmeerw125*mwrku125)+\
            (mmeerw150*mwrku150)+(mmeerw200*mwrku200)
    lonen = (muren*muurloon)+(mu125*muurloon*1.25)+(mu150*muurloon*1.5)+(mu200\
             *muurloon*2)+(mreis*mreisuur)+(mmeerw100*muurloon)+\
             (mmeerw125*muurloon*1.25)+(mmeerw150*muurloon*1.5)+\
             (mmeerw200*muurloon*2)+(mverlof*muurloon)+(mextraverlof*muurloon)+\
             (mziek*muurloon)+(mfeest*muurloon)+(mdokter*muurloon)+\
             (mgverzuim*muurloon)+(moverzuim*muurloon)
     
    inswrkwnrln = wrkwnrln.insert().values(
    wrkwnrurenID = mwrkwnruren+1,
    werknemerID = rpwnr[0],
    boekdatum = mboekd,
    aantaluren = muren+mu125+mu150+mu200+mreis+mmeerw100+mmeerw125+mmeerw150+\
      mmeerw200+mverlof+mextraverlof+mziek+mfeest+mdokter+mgverzuim+moverzuim,
    soort = mlist[msoort],
    werknummerID = mwerknr,
    tabelloon = muurloon,
    reisloon = mreisuur,
    bruto_loonbedrag = lonen,
    meerwerkstatus = mstatus,
    loonID = wrkgr2)
    if con.execute(inswrkwnrln):
        self.applyBtn.setStyleSheet("color: black; background-color: #00CC66")
    else:
        self.urenEdit.setText('0')
        self.applyBtn.setStyleSheet("color: black; background-color: #FF3333")
        return(maccountnr, mwerknr, mboekd, m_email) 
                 
    if wrkgr < 5 and msoort < 5:
        stmt = update(werken).where(werken.c.werknummerID == mwerknr).\
        values(kosten_lonen = werken.c.kosten_lonen+loonk,
               werk_constr_uren = werken.c.werk_constr_uren+muren+mu125+mu150+mu200\
               +mmeerw100+mmeerw125+mmeerw150+mmeerw200,\
               werk_reis_uren = werken.c.werk_reis_uren+mreis,\
               meerminderwerk = werken.c.meerminderwerk + meerk)
        con.execute(stmt)
        sel = select([werken]).where(werken.c.werknummerID == mwerknr)
        rpsel = con.execute(sel).first()
        logger.debug("urenBoeking(self=%s,m_email=%s): rpsel → %s", self, m_email, rpsel, extra={"event.action": "urenBoeking"})
        logger.debug("urenBoeking(self=%s,m_email=%s): urentotEdit → %s", self, m_email, urentotEdit, extra={"event.action": "urenBoeking"})
        logger.debug("urenBoeking(self=%s,m_email=%s): urenbegrEdit → %s", self, m_email, urenbegrEdit, extra={"event.action": "urenBoeking"})
        logger.debug("urenBoeking(self=%s,m_email=%s): lblptext → %s", self, m_email, lblptext, extra={"event.action": "urenBoeking"})
        logger.debug("urenBoeking(self=%s,m_email=%s): lbltext → %s", self, m_email, lbltext, extra={"event.action": "urenBoeking"})
        logger.debug("urenBoeking(self=%s,m_email=%s): lblprof → %s", self, m_email, lblprof, extra={"event.action": "urenBoeking"})
        self.urentotEdit.setText('{:<12.2f}'.format(rpsel[5]))
        self.urenbegrEdit.setText('{:<12.2f}'.format(rpsel[4]))
        lblptext = 'Totalen: Werkelijk / Begroot\nUren Constructie'
        lbltext = 'Muteren uren (werken - lonen) niet cumulatief'
        self.lblprof.setText(lblptext)
        self.lblt.setStyleSheet("color: black")
        self.lblt.setText(lbltext)
    elif wrkgr < 9 and msoort < 5: 
        stmt = update(werken).where(werken.c.werknummerID == mwerknr).\
              values(kosten_lonen = werken.c.kosten_lonen+loonk,
               werk_mont_uren = werken.c.werk_mont_uren+muren+mu125+mu150+mu200\
               +mmeerw100+mmeerw125+mmeerw150+mmeerw200,\
               werk_reis_uren = werken.c.werk_reis_uren+mreis,\
               meerminderwerk = werken.c.meerminderwerk + meerk)
        con.execute(stmt)
        sel = select([werken]).where(werken.c.werknummerID == mwerknr)
        rpsel = con.execute(sel).first()
        self.urenbegrEdit.setText('{:<12.2f}'.format(rpsel[6]))
        self.urentotEdit.setText('{:<12.2f}'.format(rpsel[7]))
        lblptext = 'Totalen: Werkelijk / Begroot\nUren Montage'
        lbltext = 'Muteren uren (werken - lonen) niet cumulatief'
        self.lblprof.setText(lblptext)
        self.lblt.setStyleSheet("color: black")
        self.lblt.setText(lbltext)
    elif wrkgr < 13 and msoort < 5:
          stmt = update(werken).where(werken.c.werknummerID == mwerknr).\
              values(kosten_lonen = werken.c.kosten_lonen+loonk,
               werk_retourlas_uren = werken.c.werk_retourlas_uren+muren+mu125+mu150+mu200\
               +mmeerw100+mmeerw125+mmeerw150+mmeerw200,\
               werk_reis_uren = werken.c.werk_reis_uren+mreis,\
               meerminderwerk = werken.c.meerminderwerk + meerk)
          con.execute(stmt)
          sel = select([werken]).where(werken.c.werknummerID == mwerknr)
          rpsel = con.execute(sel).first()
          self.urenbegrEdit.setText('{:<12.2f}'.format(rpsel[8]))
          self.urentotEdit.setText('{:<12.2f}'.format(rpsel[9]))
          lblptext = 'Totalen: Werkelijk / Begroot\nUren Retourlas'
          lbltext = 'Muteren uren (werken - lonen) niet cumulatief'
          self.lblprof.setText(lblptext)
          self.lblt.setStyleSheet("color: black")
          self.lblt.setText(lbltext)
    elif wrkgr < 17 and msoort < 5:
          stmt = update(werken).where(werken.c.werknummerID == mwerknr).\
              values(kosten_lonen = werken.c.kosten_lonen+loonk,
               werk_telecom_uren = werken.c.werk_telecom_uren+muren+mu125+mu150+mu200\
               +mmeerw100+mmeerw125+mmeerw150+mmeerw200,\
               werk_reis_uren = werken.c.werk_reis_uren+mreis,\
                meerminderwerk = werken.c.meerminderwerk + meerk)
          con.execute(stmt)
          sel = select([werken]).where(werken.c.werknummerID == mwerknr)
          rpsel = con.execute(sel).first()
          self.urenbegrEdit.setText('{:<12.2f}'.format(rpsel[10]))
          self.urentotEdit.setText('{:<12.2f}'.format(rpsel[11]))
          lblptext = 'Totalen: Werkelijk / Begroot\nUren Telecom'
          lbltext = 'Muteren uren (werken - lonen) niet cumulatief'
          self.lblprof.setText(lblptext)
          self.lblt.setStyleSheet("color: black")
          self.lblt.setText(lbltext)
    elif wrkgr < 21 and msoort < 5:
          stmt = update(werken).where(werken.c.werknummerID == mwerknr).\
              values(kosten_lonen = werken.c.kosten_lonen+loonk,
               werk_bfi_uren = werken.c.werk_bfi_uren+muren+mu125+mu150+mu200\
               +mmeerw100+mmeerw125+mmeerw150+mmeerw200,\
               werk_reis_uren = werken.c.werk_reis_uren+mreis,\
               meerminderwerk = werken.c.meerminderwerk + meerk)
          con.execute(stmt)
          sel = select([werken]).where(werken.c.werknummerID == mwerknr)
          rpsel = con.execute(sel).first()
          self.urenbegrEdit.setText('{:<12.2f}'.format(rpsel[12]))
          self.urentotEdit.setText('{:<12.2f}'.format(rpsel[13]))
          lblptext = 'Totalen: Werkelijk / Begroot\nUren BFI'
          lbltext = 'Muteren uren (werken - lonen) niet cumulatief'
          self.lblprof.setText(lblptext)
          self.lblt.setStyleSheet("color: black")
          self.lblt.setText(lbltext)
    elif wrkgr < 25 and msoort < 5:
          stmt = update(werken).where(werken.c.werknummerID == mwerknr).\
              values(kosten_lonen = werken.c.kosten_lonen+loonk,
               werk_bvl_uren = werken.c.werk_bvl_uren+muren+mu125+mu150+mu200\
               +mmeerw100+mmeerw125+mmeerw150+mmeerw200,\
               werk_reis_uren = werken.c.werk_reis_uren+mreis,\
                meerminderwerk = werken.c.meerminderwerk + meerk)
          con.xecute(stmt)
          sel = select([werken]).where(werken.c.werknummerID == mwerknr)
          rpsel = con.execute(sel).first()
          self.urenbegrEdit.setText('{:<12.2f}'.format(rpsel[14]))
          self.urentotEdit.setText('{:<12.2f}'.format(rpsel[15]))
          lblptext = 'Totalen: Werkelijk / Begroot\nUren Bovenleiding'
          lbltext = 'Muteren uren (werken - lonen) niet cumulatief'
          self.lblprof.setText(lblptext)
          self.lblt.setStyleSheet("color: black")
          self.lblt.setText(lbltext)
    elif wrkgr < 29 and msoort < 5:
          stmt = update(werken).where(werken.c.werknummerID == mwerknr).\
              values(kosten_lonen = werken.c.kosten_lonen+loonk,
               werk_spoorleg_uren = werken.c.werk_spoorleg_uren+muren+mu125+mu150+mu200\
               +mmeerw100+mmeerw125+mmeerw150+mmeerw200,\
               werk_reis_uren = werken.c.werk_reis_uren+mreis,\
               meerminderwerk = werken.c.meerminderwerk + meerk)
          con.execute(stmt)
          sel = select([werken]).where(werken.c.werknummerID == mwerknr)
          rpsel = con.execute(sel).first()
          self.urenbegrEdit.setText('{:<12.2f}'.format(rpsel[16]))
          self.urentotEdit.setText('{:>12.2f}'.format(rpsel[17]))
          lblptext = 'Totalen: Werkelijk / Begroot\nUren Spoorleg'
          lbltext = 'Muteren uren (werken - lonen) niet cumulatief'
          self.lblprof.setText(lblptext)
          self.lblt.setStyleSheet("color: black")
          self.lblt.setText(lbltext)
    elif wrkgr < 33 and msoort < 5:
          stmt = update(werken).where(werken.c.werknummerID == mwerknr).\
              values(kosten_lonen = werken.c.kosten_lonen+loonk,
               werk_mont_uren = werken.c.werk_spoorlas_uren+muren+mu125+mu150+mu200\
               +mmeerw100+mmeerw125+mmeerw150+mmeerw200,\
               werk_reis_uren = werken.c.werk_reis_uren+mreis,\
               meerminderwerk = werken.c.meerminderwerk + meerk)
          con.execute(stmt)
          sel = select([werken]).where(werken.c.werknummerID == mwerknr)
          rpsel = con.execute(sel).first()
          self.urenbegrEdit.setText('{:<12.2f}'.format(rpsel[18]))
          self.urentotEdit.setText('{:<12.2f}'.format(rpsel[19]))
          lblptext = 'Totalen: Werkelijk / Begroot\nUren Spoorlas'
          lbltext = 'Muteren uren (werken - lonen) niet cumulatief'
          self.lblprof.setText(lblptext)
          self.lblt.setStyleSheet("color: black")
          self.lblt.setText(lbltext)
    elif wrkgr < 37 and msoort < 5:
          stmt = update(werken).where(werken.c.werknummerID == mwerknr).\
                values(kosten_lonen = werken.c.kosten_lonen+loonk,
               werk_voeding_uren = werken.c.werk_voeding_uren+muren+mu125+mu150+mu200\
               +mmeerw100+mmeerw125+mmeerw150+mmeerw200,\
               werk_reis_uren = werken.c.werk_reis_uren+mreis,\
               meerminderwerk = werken.c.meerminderwerk + meerk)
          con.execute(stmt)
          sel = select([werken]).where(werken.c.werknummerID == mwerknr)
          rpsel = con.execute(sel).first()
          self.urenbegrEdit.setText('{:<12.2f}'.format(rpsel[23]))
          self.urentotEdit.setText('{:<12.2f}'.format(rpsel[24]))
          lblptext = 'Totalen: Werkelijk / Begroot\nUren Voeding'
          lbltext = 'Muteren uren (werken - lonen) niet cumulatief'
          self.lblprof.setText(lblptext)
          self.lblt.setStyleSheet("color: black")
          self.lblt.setText(lbltext)
    else:
        msaldo = ''
        logger.debug("urenBoeking(self=%s,m_email=%s): msaldo → %s", self, m_email, msaldo, extra={"event.action": "urenBoeking"})
        mboekuren = str(mboekuren)
        if msoort == 5 and wrkgr < 37:
            selsal = select([werknemers]).where(werknemers.c.accountID == maccountnr)
            rpsal = con.execute(selsal).first()
            logger.debug("urenBoeking(self=%s,m_email=%s): rpsal → %s", self, m_email, rpsal, extra={"event.action": "urenBoeking"})
            msaldo = str(rpsal[3])
            lbltext = mboekuren+' Verlofuren ingevoerd, Saldo = '+msaldo+' uren.'
            lblptext = '\n'
            self.lblt.setStyleSheet("color: navy")
            self.lblt.setText(lbltext)
            self.lblprof.setText(lblptext)
        elif msoort == 6 and wrkgr < 37:
            lbltext = mboekuren+' Extra verlofuren ingevoerd'
            lblptext = '\n'
            self.lblt.setStyleSheet("color: navy")
            self.lblt.setText(lbltext)
            self.lblprof.setText(lblptext)
        elif msoort == 7 and wrkgr < 37:
            lbltext = mboekuren+' Uren ziekte ingevoerd'
            lblptext = '\n'
            self.lblt.setStyleSheet("color: navy")
            self.lblt.setText(lbltext)
            self.lblprof.setText(lblptext)
        elif msoort == 8 and wrkgr < 37:
            lbltext = mboekuren+' Uren feestdagen ingevoerd'
            lblptext = '\n'
            self.lblt.setStyleSheet("color: navy")
            self.lblt.setText(lbltext)
            self.lblprof.setText(lblptext)
        elif msoort == 9  and wrkgr < 37:
            lbltext = mboekuren+' Uren dokterbezoek ingevoerd'
            lblptext = '\n'
            self.lblt.setStyleSheet("color: navy")
            self.lblt.setText(lbltext)
            self.lblprof.setText(lblptext)
        elif msoort == 10 and wrkgr < 37:
            lbltext = mboekuren+' Uren geoorloofd verzuim ingevoerd'
            lblptext = '\n'
            self.lblt.setStyleSheet("color: navy")
            self.lblt.setText(lbltext)
            self.lblprof.setText(lblptext)
        elif msoort == 11 and wrkgr < 37:
            lbltext = mboekuren+' Uren ongeoorloofd verzuim ingevoerd'
            lblptext = '\n'
            self.lblt.setStyleSheet("color: navy")
            self.lblt.setText(lbltext)
            self.lblprof.setText(lblptext)
        else:
            self.urenEdit.setText('0')
            self.lblt.setStyleSheet("font: bold;color: red")
            self.lblt.setText('Persoon niet in deze arbeidspool!')
            self.applyBtn.setStyleSheet("color: black; background-color: #FF3333")
            return(maccountnr, mwerknr, mboekd, m_email) 
        
    self.urenEdit.setText('0')
    self.k0Edit.setCurrentIndex(0)
    logger.debug("urenBoeking(self=%s,m_email=%s): k0Edit → %s", self, m_email, k0Edit, extra={"event.action": "urenBoeking"})
    logger.debug("<<< Exiting urenBoeking(m_email=%s)", m_email, extra={"event.action": "urenBoeking"})
    return(maccountnr, mwerknr, mboekd, m_email) 
    
def urenMut(maccountnr, mwerknr, mboekd, m_email):
    logger.warning(">>> Entering urenMut(maccountnr=%s,mwerknr=%s,mboekd=%s,m_email=%s)", maccountnr, mwerknr, mboekd, m_email, extra={"event.action": "urenMut", "logrite.maccountnr": maccountnr, "logrite.mwerknr": mwerknr, "logrite.mboekd": mboekd})
    class Widget(QDialog):
        def __init__(self):
            super(Widget,self).__init__()
            
            self.setWindowTitle("Uren invoeren externe werken - lonen")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            self.setWindowFlags(self.windowFlags()| Qt.WindowSystemMenuHint |
                                Qt.WindowMinMaxButtonsHint)
            
            self.setStyleSheet("background-color: #D9E1DF")
            self.setFont(QFont('Arial', 10))
               
            self.zkaccEdit = QLineEdit(str(maccountnr))
            self.zkaccEdit.setFixedWidth(150)
            self.zkaccEdit.setFont(QFont("Arial",10))
            self.zkaccEdit.setStyleSheet('color: black; background-color: #F8F7EE')
            reg_ex = QRegExp("^[1]{1}[0-9]{8}$")
            input_validator = QRegExpValidator(reg_ex, self.zkaccEdit)
            self.zkaccEdit.setValidator(input_validator)
            
            self.zkwerknEdit = QLineEdit(str(mwerknr))
            self.zkwerknEdit.setFixedWidth(150)
            self.zkwerknEdit.setFont(QFont("Arial",10))
            self.zkwerknEdit.setStyleSheet('color: black; background-color: #F8F7EE')
            reg_ex = QRegExp("^[8]{1}[0-9]{8}$")
            input_validator = QRegExpValidator(reg_ex, self.zkwerknEdit)
            self.zkwerknEdit.setValidator(input_validator)
     
            self.k0Edit = QComboBox()
            self.k0Edit.setFixedWidth(150)
            self.k0Edit.setFont(QFont("Arial",10))
            self.k0Edit.setStyleSheet('color: black; background-color: #F8F7EE')
            self.k0Edit.addItem('100%')
            self.k0Edit.addItem('125%')
            self.k0Edit.addItem('150%')
            self.k0Edit.addItem('200%')
            self.k0Edit.addItem('Reis')
            self.k0Edit.addItem('Verlof')
            self.k0Edit.addItem('Extra verlof')
            self.k0Edit.addItem('Ziekte')
            self.k0Edit.addItem('Feestdag')
            self.k0Edit.addItem('Dokter')
            self.k0Edit.addItem('Geoorl. verzuim')
            self.k0Edit.addItem('Ong. verzuim')
  
            self.cBox = QCheckBox('Meerwerk')
            self.cBox.setFont(QFont("Arial",10))
            self.cBox.setStyleSheet('color: black; background-color: #F8F7EE')
                                                                     
            self.urenEdit = QLineEdit('0')
            self.urenEdit.setFixedWidth(150)
            self.urenEdit.setFont(QFont("Arial",10))
            self.urenEdit.setStyleSheet('color: black; background-color: #F8F7EE')
            reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, self.urenEdit)
            self.urenEdit.setValidator(input_validator)
            
            self.urentotEdit = QLineEdit('0')
            self.urentotEdit.setFixedWidth(150)
            self.urentotEdit.setDisabled(True)
            self.urentotEdit.setFont(QFont("Arial",10))
            self.urentotEdit.setStyleSheet("color: black")
    
            self.urenbegrEdit = QLineEdit('0')
            self.urenbegrEdit.setFixedWidth(150)
            self.urenbegrEdit.setDisabled(True)
            self.urenbegrEdit.setFont(QFont("Arial",10))
            self.urenbegrEdit.setStyleSheet("color: black")        
                                                         
            self.boekdatumEdit = QLineEdit(mboekd)
            self.boekdatumEdit.setFixedWidth(150)
            self.boekdatumEdit.setFont(QFont("Arial",10))
            self.boekdatumEdit.setStyleSheet('color: black; background-color: #F8F7EE')
            reg_ex = QRegExp("^[2]{1}[0-1]{1}[0-9]{2}[-]{1}[0-1]{1}[0-9]{1}[-]{1}[0-3]{1}[0-9]{1}$")
            input_validator = QRegExpValidator(reg_ex, self.boekdatumEdit)
            self.boekdatumEdit.setValidator(input_validator)
                                            
            def accChanged():
                logger.warning(">>> Entering accChanged()", extra={"event.action": "accChanged"})
                logger.debug("accChanged(): zkaccEdit → %s", zkaccEdit, extra={"event.action": "accChanged"})
                self.zkaccEdit.setText(self.zkaccEdit.text())
            self.zkaccEdit.textChanged.connect(accChanged)
             
            def werknChanged():
                logger.warning(">>> Entering werknChanged()", extra={"event.action": "werknChanged"})
                logger.debug("werknChanged(): zkwerknEdit → %s", zkwerknEdit, extra={"event.action": "werknChanged"})
                self.zkwerknEdit.setText(self.zkwerknEdit.text())
            self.zkwerknEdit.textChanged.connect(werknChanged)
             
            '''
            def k0Changed():
                self.k0Edit.setCurrentText(self.k0Edit.currentText())
            self.k0Edit.currentTextChanged.connect(k0Changed)
                        
            def k0Changed():
                logger.warning(">>> Entering k0Changed()", extra={"event.action": "k0Changed"})
                self.k0Edit.setCurrentIndex(self.k0Edit.currentIndex())
            self.k0Edit.activated[str].connect(k0Changed)
            '''
            
            def k0Changed():
                logger.debug("k0Changed(): k0Edit → %s", k0Edit, extra={"event.action": "k0Changed"})
                self.k0Edit.setCurrentIndex(self.k0Edit.currentIndex())
            self.k0Edit.currentIndexChanged.connect(k0Changed)
                       
            def cboxChanged():
                logger.warning(">>> Entering cboxChanged()", extra={"event.action": "cboxChanged"})
                logger.debug("cboxChanged(): cBox → %s", cBox, extra={"event.action": "cboxChanged"})
                self.cBox.setCheckState(self.cBox.checkState())
            self.cBox.stateChanged.connect(cboxChanged)
            
            def urenChanged():
                logger.warning(">>> Entering urenChanged()", extra={"event.action": "urenChanged"})
                logger.debug("urenChanged(): urenEdit → %s", urenEdit, extra={"event.action": "urenChanged"})
                self.urenEdit.setText(self.urenEdit.text())
            self.urenEdit.textChanged.connect(urenChanged)
            
            def boekdatumChanged():
                logger.warning(">>> Entering boekdatumChanged()", extra={"event.action": "boekdatumChanged"})
                logger.debug("boekdatumChanged(): boekdatumEdit → %s", boekdatumEdit, extra={"event.action": "boekdatumChanged"})
                self.boekdatumEdit.setText(self.boekdatumEdit.text())
            self.boekdatumEdit.textChanged.connect(boekdatumChanged)
            
            grid = QGridLayout()
            grid.setSpacing(20)
            
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl ,0 , 1)
            
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 3, 1, 1, Qt.AlignRight)       

            self.lblt = QLabel('Muteren uren (werken - lonen) niet cumulatief')
            self.lblt.setStyleSheet("color: black")
            self.lblt.setFont(QFont("Arial", 10))
            grid.addWidget(self.lblt , 12, 0, 1, 4, Qt.AlignCenter)
            
            lbl1 = QLabel('Accountnummer')
            lbl1.setFont(QFont("Arial", 10))
            grid.addWidget(lbl1, 6, 1, 1, 1, Qt.AlignRight)
            grid.addWidget(self.zkaccEdit , 6, 2, 1, 1, Qt.AlignRight)
            
            lbl2 = QLabel('Werknummer')
            lbl2.setFont(QFont("Arial", 10))
            grid.addWidget(lbl2, 7, 1, 1, 1, Qt.AlignRight)
            grid.addWidget(self.zkwerknEdit, 7, 2, 1, 1, Qt.AlignRight)
                
            lbl3 = QLabel('Soort Uren')
            lbl3.setFont(QFont("Arial", 10))
            grid.addWidget(lbl3, 8, 1, 1, 1, Qt.AlignRight)
            grid.addWidget(self.k0Edit, 8, 2, 1, 1, Qt.AlignRight)
                        
            grid.addWidget(self.cBox, 8, 3)
            
            self.lblprof = QLabel('Totalen: Werkelijk / Begroot\nUren')
            self.lblprof.setFont(QFont("Arial", 10))
            self.lblprof.setFixedWidth(200)
            self.lblprof.setAlignment(Qt.AlignRight)
            grid.addWidget(self.lblprof, 9, 1, 1, 1, Qt.AlignRight | Qt.AlignTop)
            grid.addWidget(self.urentotEdit, 9, 2, 1, 1, Qt.AlignRight)
            grid.addWidget(self.urenbegrEdit, 9, 3, 1, 1)
            
            lbl4 = QLabel('Urenmutatie')
            lbl4.setFont(QFont("Arial", 10))
            grid.addWidget(lbl4, 10, 1, 1, 1, Qt.AlignRight)
            grid.addWidget(self.urenEdit, 10, 2, 1, 1, Qt.AlignRight)
                                       
            lbl5 = QLabel('Boekdatum')
            lbl5.setFont(QFont("Arial", 10))
            grid.addWidget(lbl5, 11, 1, 1, 1, Qt.AlignRight)
            grid.addWidget(self.boekdatumEdit, 11, 2, 1, 1, Qt.AlignRight)
            
            self.applyBtn = QPushButton('Muteren')
            self.applyBtn.clicked.connect(lambda: urenBoeking(self, m_email))
               
            self.applyBtn.setFont(QFont("Arial",10))
            self.applyBtn.setFixedWidth(100)
            self.applyBtn.setStyleSheet("color: black;  background-color: gainsboro") 
                
            grid.addWidget(self.applyBtn,13, 3 , 1 , 1, Qt.AlignRight)
                
            cancelBtn = QPushButton('Sluiten')
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email)) 
    
            grid.addWidget(cancelBtn, 13, 2, 1 , 1, Qt.AlignRight)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black; background-color: gainsboro") 
                   
            infoBtn = QPushButton('Informatie')
            infoBtn.clicked.connect(lambda: info()) 
    
            grid.addWidget(infoBtn, 13, 1, 1, 1, Qt.AlignRight)
            infoBtn.setFont(QFont("Arial",10))
            infoBtn.setFixedWidth(100)
            infoBtn.setStyleSheet("color: black; background-color: gainsboro") 
            
            rightslbl = QLabel('\u00A9 2017 all rights reserved - dj.jansen@casema.nl')
            rightslbl.setFont(QFont("Arial", 10))
            grid.addWidget(rightslbl, 14, 1, 1, 4, Qt.AlignCenter)
            
            self.setLayout(grid)
            self.setGeometry(600, 200, 150, 100)
                
    window = Widget()
    window.exec_()  