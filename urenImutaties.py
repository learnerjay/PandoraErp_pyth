from login import hoofdMenu
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QFont, QPixmap, QRegExpValidator, QIcon
from PyQt5.QtWidgets import QLabel, QPushButton,\
     QLineEdit, QGridLayout, QDialog, QCheckBox, QComboBox
from sqlalchemy import (Table, Column, Integer, String, Float, MetaData, \
                            ForeignKey, create_engine, Boolean)
from sqlalchemy.sql import select, update, func, and_
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
            self.setWindowTitle("Information ERP System Pandora")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            self.setFont(QFont('Arial', 10))
            grid = QGridLayout()
            logger.debug("__init__(parent=%s): grid → %s", parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid, extra={"event.action": "__init__"})
            grid.setSpacing(20)
            
            lblinfo = QLabel('ERP System Pandora')
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
                                        Information about hours to mutate.  
        
        The module starts with the following variable data:
        Account number: blank field to be filled in with the employee's account number.
        Work order number: blank field to be filled in with the work order number,
        for which is being worked on. 
        Present/Absent: choose here the type of hours for which the booking must be made,
        e.g. 100% regular hours, 125% overtime, 150% overtime, 200% overtime,
        or one of the various hours of absence mentioned for sick leave etc.
        Number of hours: Hours worked on the day of work.
        The label for the actual total hours indicates the professional discipline,
        for which the hours are booked. 
        Date of work: date of the current day in the format yyyy-mm-dd
        
        When modifying or filling in the fields 'Account number', 'Work order number' 
        and 'Date of work', the system will remember the last used key data 
        when the fields arise so that a quick entry is possible.
        The option Present/Absent will be filled in by default with 100% hours, 
        Because this will be the most common choice. 
        When entering the data, if entered correctly, the button Mutate' turn green. 
        In the event of an incorrect or unsuccessful entry, the button 'Mutate' turn red,
        in this case a correction should be created, because the entry was not booked!
        In the status field below the input fields, the status and information of 
        the absence hours is showed, e.g. in the case of leave hours the leave balance is showed. 
        This status field also displays the error messages, in the case of a invalid entry.
          
     ''')
            grid.addWidget(infolbl, 1, 0)
                           
            infolbl.setStyleSheet("font: 10pt Comic Sans MS; color: black ; background-color: #D9E1DF")   
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 2, 0, 1, 2, Qt.AlignCenter)
            
            cancelBtn = QPushButton('Close')
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
        Column('werknummerID', Integer),
        Column('loonID', None, ForeignKey('lonen.loonID')),
        Column('boekdatum', String),
        Column('aantaluren', Float),
        Column('tabelloon', Float),
        Column('reisloon', Float),
        Column('bruto_loonbedrag', Float),
        Column('meerwerkstatus', Boolean),
        Column('soort', String))
    logger.debug("urenBoeking(m_email=%s): selwnr → %s", m_email, selwnr, extra={"event.action": "urenBoeking"})
    werknemers = Table('werknemers', metadata,
        Column('werknemerID', Integer(), primary_key=True),
        Column('accountID', None, ForeignKey('accounts.accountID')),
        Column('loonID', None, ForeignKey('lonen.loonID')),
        Column('verlofsaldo', Float),
        Column('extraverlof', Float),
        Column('wnrloonID', Integer))
    orders_intern = Table('orders_intern', metadata,
        Column('werkorderID', Integer(), primary_key=True),
        Column('werkomschrijving', String),
        Column('voortgangstatus', String),
        Column('statusweek', String),
        Column('boekdatum', String),
        Column('begroot_totaal', Float),
        Column('werk_totaal', Float),
        Column('begr_materialen', Float),
        Column('werk_materialen', Float),
        Column('begr_lonen', Float),
        Column('werk_lonen', Float),
        Column('bzagen', Float),
        Column('wzagen', Float),
        Column('bschaven', Float),
        Column('wschaven', Float),
        Column('bsteken', Float),
        Column('wsteken', Float),
        Column('bboren', Float),
        Column('wboren', Float),
        Column('bfrezen', Float),
        Column('wfrezen', Float),
        Column('bdraaien_klein', Float),
        Column('wdraaien_klein', Float),
        Column('bdraaien_groot', Float),
        Column('wdraaien_groot', Float),
        Column('btappen', Float),
        Column('wtappen', Float),
        Column('bnube_draaien', Float),
        Column('wnube_draaien', Float),
        Column('bnube_bewerken', Float),
        Column('wnube_bewerken', Float),
        Column('bknippen', Float),
        Column('wknippen', Float),
        Column('bkanten', Float),
        Column('wkanten', Float),
        Column('bstansen', Float),
        Column('wstansen', Float),
        Column('blassen_co2', Float),
        Column('wlassen_co2', Float),
        Column('blassen_hand', Float),
        Column('wlassen_hand', Float),
        Column('bverpakken', Float),
        Column('wverpakken', Float),
        Column('bverzinken', Float),
        Column('wverzinken', Float),
        Column('bmoffelen', Float),
        Column('wmoffelen', Float),
        Column('bschilderen', Float),
        Column('wschilderen', Float),
        Column('bspuiten', Float),
        Column('wspuiten', Float),
        Column('bponsen', Float),
        Column('wponsen', Float),
        Column('bpersen', Float),
        Column('wpersen', Float),
        Column('bgritstralen', Float),
        Column('wgritstralen', Float),
        Column('bmontage', Float),
        Column('wmontage', Float),
        Column('werk_reis_uren', Float),
        Column('meerminderwerk', Float))
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
                    werknemers.c.loonID > 52))
    rpwnr = con.execute(selwnr).first()
    if rpwnr:
        maccountnr = int(maccountnr)
    else:
       self.urenEdit.setText('0')
       logger.debug("urenBoeking(self=%s,m_email=%s): urenEdit → %s", self, m_email, urenEdit, extra={"event.action": "urenBoeking"})
       logger.debug("urenBoeking(self=%s,m_email=%s): lblt → %s", self, m_email, lblt, extra={"event.action": "urenBoeking"})
       self.lblt.setStyleSheet("font: bold; color: red")
       self.lblt.setText('Person is not in this labor pool!')
       self.applyBtn.setStyleSheet("color: black; background-color: #FF3333")
       logger.debug("urenBoeking(self=%s,m_email=%s): applyBtn → %s", self, m_email, applyBtn, extra={"event.action": "urenBoeking"})
       return('', mwerknr, mboekd, m_email)
    selwerk = select([orders_intern]).where(orders_intern.c.werkorderID == mwerknr)
    if mwerknr and len(mwerknr)== 9  and _11check(mwerknr) and con.execute(selwerk).first():
        mwerknr = int(mwerknr)
    else:
       self.urenEdit.setText('0')
       self.lblt.setStyleSheet("font: bold; color: red")
       self.lblt.setText('This is not a valid work order number!')
       self.applyBtn.setStyleSheet("color: black; background-color: #FF3333")
       return(maccountnr, '', mboekd, m_email)

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
    
    mlist = ['100%','125%','150%','200%','Travel','Leaf','Extra leaf','Illness',\
            'Holiday','Doctor','Permitted default','Not permitted default']
    
    if rpwerk[2] == 'H':
        self.urenEdit.setText('0')
        self.lblt.setStyleSheet("font: bold; color: red")
        self.lblt.setText('Work is ready and closed!')
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
        self.lblt.setText('No hours inserted!')
        self.applyBtn.setStyleSheet("color: black; background-color: #FF3333")
        return(maccountnr, mwerknr, mboekd, m_email)
            
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
    try:
        mwrkwnruren=(con.execute(select([func.max(wrkwnrln.c.wrkwnrurenID,\
                type_=Integer)])).scalar())
    except:
        logger.error("Exception in urenBoeking(m_email=%s)", m_email, exc_info=True, extra={"event.action": "urenBoeking", "event.category": "process"})
        logger.debug("urenBoeking(self=%s,m_email=%s): wrkgr2 → %s", self, m_email, wrkgr2, extra={"event.action": "urenBoeking"})
        mwrkwnruren = 1
        logger.debug("urenBoeking(self=%s,m_email=%s): mwrkwnruren → %s", self, m_email, mwrkwnruren, extra={"event.action": "urenBoeking"})
    wrkgr = rpwnr[2]
    logger.debug("urenBoeking(self=%s,m_email=%s): wrkgr → %s", self, m_email, wrkgr, extra={"event.action": "urenBoeking"})
    wrkgr2 = rpwnr[5]
    loonsel = select([lonen]).where(lonen.c.loonID == wrkgr)    #loonID
    loonsel2 = select([lonen]).where(lonen.c.loonID == wrkgr2)
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
                
    if wrkgr > 52 and wrkgr < 56 and msoort < 5:
        stmt = update(orders_intern).where(orders_intern.c.werkorderID == mwerknr).\
               values(werk_lonen = orders_intern.c.werk_lonen+loonk,
               wzagen = orders_intern.c.wzagen+muren+mu125+mu150+mu200\
               +mmeerw100+mmeerw125+mmeerw150+mmeerw200,\
               werk_reis_uren = orders_intern.c.werk_reis_uren+mreis,\
               meerminderwerk = orders_intern.c.meerminderwerk + meerk)
        con.execute(stmt)
        sel = select([orders_intern]).where(orders_intern.c.werkorderID == mwerknr)
        rpsel = con.execute(sel).first()
        logger.debug("urenBoeking(self=%s,m_email=%s): rpsel → %s", self, m_email, rpsel, extra={"event.action": "urenBoeking"})
        logger.debug("urenBoeking(self=%s,m_email=%s): urenbegrEdit → %s", self, m_email, urenbegrEdit, extra={"event.action": "urenBoeking"})
        logger.debug("urenBoeking(self=%s,m_email=%s): urentotEdit → %s", self, m_email, urentotEdit, extra={"event.action": "urenBoeking"})
        logger.debug("urenBoeking(self=%s,m_email=%s): lblptext → %s", self, m_email, lblptext, extra={"event.action": "urenBoeking"})
        logger.debug("urenBoeking(self=%s,m_email=%s): lbltext → %s", self, m_email, lbltext, extra={"event.action": "urenBoeking"})
        logger.debug("urenBoeking(self=%s,m_email=%s): lblprof → %s", self, m_email, lblprof, extra={"event.action": "urenBoeking"})
        self.urenbegrEdit.setText('{:<12.2f}'.format(rpsel[11]))
        self.urentotEdit.setText('{:<12.2f}'.format(rpsel[12]))
        lblptext = 'Totals: Realised / Budgeted\nhours Sawing'
        lbltext = 'Mutate hours (works - wages) not cumulative'
        self.lblprof.setText(lblptext)
        self.lblt.setStyleSheet("color: black")
        self.lblt.setText(lbltext)
    elif wrkgr > 55 and wrkgr < 59 and msoort < 5:   
        stmt = update(orders_intern).where(orders_intern.c.werkorderID == mwerknr).\
            values(werk_lonen = orders_intern.c.werk_lonen+loonk,
           wschaven = orders_intern.c.wschaven+mu125+mu150+mu200\
           +mmeerw100+mmeerw125+mmeerw150+mmeerw200,\
           werk_reis_uren = orders_intern.c.werk_reis_uren+mreis,\
           meerminderwerk = orders_intern.c.meerminderwerk + meerk)
        con.execute(stmt)
        sel = select([orders_intern]).where(orders_intern.c.werkorderID == mwerknr)
        rpsel = con.execute(sel).first()
        self.urenbegrEdit.setText('{:<12.2f}'.format(rpsel[13]))
        self.urentotEdit.setText('{:<12.2f}'.format(rpsel[14]))
        lblptext = 'Totals: Realised / Budgeted\nhours planing'
        lbltext = 'Mutate hours (works - wages) not cumulative'
        self.lblprof.setText(lblptext)
        self.lblt.setStyleSheet("color: black")
        self.lblt.setText(lbltext)
    elif wrkgr > 58 and wrkgr < 62 and msoort < 5:
        stmt = update(orders_intern).where(orders_intern.c.werkorderID == mwerknr).\
           values(werk_lonen = orders_intern.c.werk_lonen+loonk,
           wsteken = orders_intern.c.wsteken+muren+mu125+mu150+mu200\
           +mmeerw100+mmeerw125+mmeerw150+mmeerw200,\
           werk_reis_uren = orders_intern.c.werk_reis_uren+mreis,\
           meerminderwerk = orders_intern.c.meerminderwerk + meerk)
        con.execute(stmt)
        sel = select([orders_intern]).where(orders_intern.c.werkorderID == mwerknr)
        rpsel = con.execute(sel).first()
        self.urenbegrEdit.setText('{:<12.2f}'.format(rpsel[15]))
        self.urentotEdit.setText('{:<12.2f}'.format(rpsel[16]))
        lblptext = 'Totals: Realised / Budgeted\nhours stabbing'
        lbltext = 'Mutate hours (works - wages) not cumulative'
        self.lblprof.setText(lblptext)
        self.lblt.setStyleSheet("color: black")
        self.lblt.setText(lbltext)
    elif wrkgr > 61 and wrkgr < 65 and msoort < 5:
        stmt = update(orders_intern).where(orders_intern.c.werkorderID == mwerknr).\
          values(werk_lonen = orders_intern.c.werk_lonen+loonk,
           wboren = orders_intern.c.wboren+muren+mu125+mu150+mu200\
           +mmeerw100+mmeerw125+mmeerw150+mmeerw200,\
           werk_reis_uren = orders_intern.c.werk_reis_uren+mreis,\
            meerminderwerk = orders_intern.c.meerminderwerk + meerk)
        con.execute(stmt)
        sel = select([orders_intern]).where(orders_intern.c.werkorderID == mwerknr)
        rpsel = con.execute(sel).first()
        self.urenbegrEdit.setText('{:<12.2f}'.format(rpsel[17]))
        self.urentotEdit.setText('{:<12.2f}'.format(rpsel[18]))
        lblptext = 'Totals: Realised / Budgeted\nhours drilling'
        lbltext = 'Mutate hours (works - wages) not cumulative'
        self.lblprof.setText(lblptext)
        self.lblt.setStyleSheet("color: black")
        self.lblt.setText(lbltext)
    elif wrkgr > 64 and wrkgr < 68 and msoort < 5:
        stmt = update(orders_intern).where(orders_intern.c.werkorderID == mwerknr).\
          values(werk_lonen = orders_intern.c.werk_lonen+loonk,
           wfrezen = orders_intern.c.wfrezen+muren+mu125+mu150+mu200\
           +mmeerw100+mmeerw125+mmeerw150+mmeerw200,\
           werk_reis_uren = orders_intern.c.werk_reis_uren+mreis,\
           meerminderwerk = orders_intern.c.meerminderwerk + meerk)
        con.execute(stmt)
        sel = select([orders_intern]).where(orders_intern.c.werkorderID == mwerknr)
        rpsel = con.execute(sel).first()
        self.urenbegrEdit.setText('{:<12.2f}'.format(rpsel[19]))
        self.urentotEdit.setText('{:<12.2f}'.format(rpsel[20]))
        lblptext = 'Totals: Realised / Budgeted\nhours milling'
        lbltext = 'Mutate hours (works - wages) not cumulative'
        self.lblprof.setText(lblptext)
        self.lblt.setStyleSheet("color: black")
        self.lblt.setText(lbltext)
    elif wrkgr > 67 and wrkgr < 71 and msoort < 5:
        stmt = update(orders_intern).where(orders_intern.c.werkorderID == mwerknr).\
          values(werk_lonen = orders_intern.c.werk_lonen+loonk,
           wdraaien_klein = orders_intern.c.wdraaien_klein+muren+mu125+mu150+mu200\
           +mmeerw100+mmeerw125+mmeerw150+mmeerw200,\
           werk_reis_uren = orders_intern.c.werk_reis_uren+mreis,\
            meerminderwerk = orders_intern.c.meerminderwerk + meerk)
        con.execute(stmt)
        sel = select([orders_intern]).where(orders_intern.c.werkorderID == mwerknr)
        rpsel = con.execute(sel).first()
        self.urenbegrEdit.setText('{:<12.2f}'.format(rpsel[21]))
        self.urentotEdit.setText('{:<12.2f}'.format(rpsel[22]))
        lblptext = 'Totals: Realised / Budgeted\nhours turning small'
        lbltext = 'Mutate hours (works - wages) not cumulative'
        self.lblprof.setText(lblptext)
        self.lblt.setStyleSheet("color: black")
        self.lblt.setText(lbltext)
    elif wrkgr > 70 and wrkgr < 74 and msoort < 5:
        stmt = update(orders_intern).where(orders_intern.c.werkorderID == mwerknr).\
           values(werk_lonen = orders_intern.c.werk_lonen+loonk,
           wdraaien_groot = orders_intern.c.wdraaien_groot+muren+mu125+mu150+mu200\
           +mmeerw100+mmeerw125+mmeerw150+mmeerw200,\
           werk_reis_uren = orders_intern.c.werk_reis_uren+mreis,\
           meerminderwerk = orders_intern.c.meerminderwerk + meerk)
        con.execute(stmt)
        sel = select([orders_intern]).where(orders_intern.c.werkorderID == mwerknr)
        rpsel = con.execute(sel).first()
        self.urenbegrEdit.setText('{:<12.2f}'.format(rpsel[23]))
        self.urentotEdit.setText('{:<12.2f}'.format(rpsel[24]))
        lblptext = 'Totals: Realised / Budgeted\nhours turning big'
        lbltext = 'Mutate hours (works - wages) not cumulative'
        self.lblprof.setText(lblptext)
        self.lblt.setStyleSheet("color: black")
        self.lblt.setText(lbltext)
    elif wrkgr > 73 and wrkgr < 77 and msoort < 5:
        stmt = update(orders_intern).where(orders_intern.c.werkorderID == mwerknr).\
           values(werk_lonen = orders_intern.c.werk_lonen+loonk,
           wtappen = orders_intern.c.wtappen+muren+mu125+mu150+mu200\
           +mmeerw100+mmeerw125+mmeerw150+mmeerw200,\
           werk_reis_uren = orders_intern.c.werk_reis_uren+mreis,\
           meerminderwerk = orders_intern.c.meerminderwerk + meerk)
        con.execute(stmt)
        sel = select([orders_intern]).where(orders_intern.c.werkorderID == mwerknr)
        rpsel = con.execute(sel).first()
        self.urenbegrEdit.setText('{:<12.2f}'.format(rpsel[25]))
        self.urentotEdit.setText('{:<12.2f}'.format(rpsel[26]))
        lblptext = 'TTotals: Realised / Budgeted\nhours threading'
        lbltext = 'Mutate hours (works - wages) not cumulative'
        self.lblprof.setText(lblptext)
        self.lblt.setStyleSheet("color: black")
        self.lblt.setText(lbltext)
    elif wrkgr > 76 and wrkgr < 80 and msoort < 5:
        stmt = update(orders_intern).where(orders_intern.c.werkorderID == mwerknr).\
            values(werk_lonen = orders_intern.c.werk_lonen+loonk,
           wnube_draaien = orders_intern.c.wnube_draaien+muren+mu125+mu150+mu200\
           +mmeerw100+mmeerw125+mmeerw150+mmeerw200,\
           werk_reis_uren = orders_intern.c.werk_reis_uren+mreis,\
           meerminderwerk = orders_intern.c.meerminderwerk + meerk)
        con.execute(stmt)
        sel = select([orders_intern]).where(orders_intern.c.werkorderID == mwerknr)
        rpsel = con.execute(sel).first()
        self.urenbegrEdit.setText('{:<12.2f}'.format(rpsel[27]))
        self.urentotEdit.setText('{:<12.2f}'.format(rpsel[28]))
        lblptext = 'Totals: Realised / Budgeted\nhours CNC turning'
        lbltext = 'Mutate hours (works - wages) not cumulative'
        self.lblprof.setText(lblptext)
        self.lblt.setStyleSheet("color: black")
        self.lblt.setText(lbltext)
    elif wrkgr > 79 and wrkgr < 83 and msoort < 5:
        stmt = update(orders_intern).where(orders_intern.c.werkorderID == mwerknr).\
            values(werk_lonen = orders_intern.c.werk_lonen+loonk,
           wnube_bewerken = orders_intern.c.wnube_bewerken+muren+mu125+mu150+mu200\
           +mmeerw100+mmeerw125+mmeerw150+mmeerw200,\
           werk_reis_uren = orders_intern.c.werk_reis_uren+mreis,\
           meerminderwerk = orders_intern.c.meerminderwerk + meerk)
        con.execute(stmt)
        sel = select([orders_intern]).where(orders_intern.c.werkorderID == mwerknr)
        rpsel = con.execute(sel).first()
        self.urenbegrEdit.setText('{:<12.2f}'.format(rpsel[29]))
        self.urentotEdit.setText('{:<12.2f}'.format(rpsel[30]))
        lblptext = 'Totals: Realised / Budgeted\nhours CNC milling'
        lbltext = 'Mutate hours (works - wages) not cumulative'
        self.lblprof.setText(lblptext)
        self.lblt.setStyleSheet("color: black")
        self.lblt.setText(lbltext)
    elif wrkgr > 72 and wrkgr < 86 and msoort < 5:
        stmt = update(orders_intern).where(orders_intern.c.werkorderID == mwerknr).\
            values(werk_lonen = orders_intern.c.werk_lonen+loonk,
           wknippen = orders_intern.c.wknippen+muren+mu125+mu150+mu200\
           +mmeerw100+mmeerw125+mmeerw150+mmeerw200,\
           werk_reis_uren = orders_intern.c.werk_reis_uren+mreis,\
           meerminderwerk = orders_intern.c.meerminderwerk + meerk)
        con.execute(stmt)
        sel = select([orders_intern]).where(orders_intern.c.werkorderID == mwerknr)
        rpsel = con.execute(sel).first()
        self.urenbegrEdit.setText('{:<12.2f}'.format(rpsel[31]))
        self.urentotEdit.setText('{:<12.2f}'.format(rpsel[32]))
        lblptext = 'Totals: Realised / Budgeted\nhours cutting'
        lbltext = 'Mutate hours (works - wages) not cumulative'
        self.lblprof.setText(lblptext)
        self.lblt.setStyleSheet("color: black")
        self.lblt.setText(lbltext)
    elif wrkgr > 75 and wrkgr < 89 and msoort < 5:
        stmt = update(orders_intern).where(orders_intern.c.werkorderID == mwerknr).\
            values(werk_lonen = orders_intern.c.werk_lonen+loonk,
           wkanten = orders_intern.c.wkanten+muren+mu125+mu150+mu200\
           +mmeerw100+mmeerw125+mmeerw150+mmeerw200,\
           werk_reis_uren = orders_intern.c.werk_reis_uren+mreis,\
           meerminderwerk = orders_intern.c.meerminderwerk + meerk)
        con.execute(stmt)
        sel = select([orders_intern]).where(orders_intern.c.werkorderID == mwerknr)
        rpsel = con.execute(sel).first()
        self.urenbegrEdit.setText('{:<12.2f}'.format(rpsel[33]))
        self.urentotEdit.setText('{:<12.2f}'.format(rpsel[34]))
        lblptext = 'Totals: Realised / Budgeted\nhours bending'
        lbltext = 'Mutate hours (works - wages) not cumulative'
        self.lblprof.setText(lblptext)
        self.lblt.setStyleSheet("color: black")
        self.lblt.setText(lbltext)
    elif wrkgr > 88 and wrkgr < 92 and msoort < 5:
        stmt = update(orders_intern).where(orders_intern.c.werkorderID == mwerknr).\
            values(werk_lonen = orders_intern.c.werk_lonen+loonk,
           wstansen = orders_intern.c.wstansen+muren+mu125+mu150+mu200\
           +mmeerw100+mmeerw125+mmeerw150+mmeerw200,\
           werk_reis_uren = orders_intern.c.werk_reis_uren+mreis,\
           meerminderwerk = orders_intern.c.meerminderwerk + meerk)
        con.execute(stmt)
        sel = select([orders_intern]).where(orders_intern.c.werkorderID == mwerknr)
        rpsel = con.execute(sel).first()
        self.urenbegrEdit.setText('{:<12.2f}'.format(rpsel[35]))
        self.urentotEdit.setText('{:<12.2f}'.format(rpsel[36]))
        lblptext = 'Totals: Realised / Budgeted\nhours sizing'
        lbltext = 'Mutate hours (works - wages) not cumulative'
        self.lblprof.setText(lblptext)
        self.lblt.setStyleSheet("color: black")
        self.lblt.setText(lbltext)
    elif wrkgr > 91 and wrkgr < 95 and msoort < 5:
        stmt = update(orders_intern).where(orders_intern.c.werkorderID == mwerknr).\
           values(werk_lonen = orders_intern.c.werk_lonen+loonk,
           wlassen_co2 = orders_intern.c.wlassen_co2+muren+mu125+mu150+mu200\
           +mmeerw100+mmeerw125+mmeerw150+mmeerw200,\
           werk_reis_uren = orders_intern.c.werk_reis_uren+mreis,\
           meerminderwerk = orders_intern.c.meerminderwerk + meerk)
        con.execute(stmt)
        sel = select([orders_intern]).where(orders_intern.c.werkorderID == mwerknr)
        rpsel = con.execute(sel).first()
        self.urenbegrEdit.setText('{:<12.2f}'.format(rpsel[37]))
        self.urentotEdit.setText('{:<12.2f}'.format(rpsel[38]))
        lblptext = 'Totals: Realised / Budgeted\nhours welding co2'
        lbltext = 'Mutate hours (works - wages) not cumulative'
        self.lblprof.setText(lblptext)
        self.lblt.setStyleSheet("color: black")
        self.lblt.setText(lbltext)
    elif wrkgr > 94 and wrkgr < 98 and msoort < 5:
        stmt = update(orders_intern).where(orders_intern.c.werkorderID == mwerknr).\
            values(werk_lonen = orders_intern.c.werk_lonen+loonk,
           wlassen_hand = orders_intern.c.wlassen_hand+muren+mu125+mu150+mu200\
           +mmeerw100+mmeerw125+mmeerw150+mmeerw200,\
           werk_reis_uren = orders_intern.c.werk_reis_uren+mreis,\
           meerminderwerk = orders_intern.c.meerminderwerk + meerk)
        con.execute(stmt)
        sel = select([orders_intern]).where(orders_intern.c.werkorderID == mwerknr)
        rpsel = con.execute(sel).first()
        self.urenbegrEdit.setText('{:<12.2f}'.format(rpsel[39]))
        self.urentotEdit.setText('{:<12.2f}'.format(rpsel[40]))
        lblptext = 'Totals: Realised / Budgeted\nhours welding hand'
        lbltext = 'Mutate hours (works - wages) not cumulative'
        self.lblprof.setText(lblptext)
        self.lblt.setStyleSheet("color: black")
        self.lblt.setText(lbltext)
    elif wrkgr > 97 and wrkgr < 101 and msoort < 5:
        stmt = update(orders_intern).where(orders_intern.c.werkorderID == mwerknr).\
            values(werk_lonen = orders_intern.c.werk_lonen+loonk,
           wverpakken = orders_intern.c.wverpakken+muren+mu125+mu150+mu200\
           +mmeerw100+mmeerw125+mmeerw150+mmeerw200,\
           werk_reis_uren = orders_intern.c.werk_reis_uren+mreis,\
           meerminderwerk = orders_intern.c.meerminderwerk + meerk)
        con.execute(stmt)
        sel = select([orders_intern]).where(orders_intern.c.werkorderID == mwerknr)
        rpsel = con.execute(sel).first()
        self.urenbegrEdit.setText('{:<12.2f}'.format(rpsel[41]))
        self.urentotEdit.setText('{:<12.2f}'.format(rpsel[42]))
        lblptext = 'Totals: Realised / Budgeted\nhours packing'
        lbltext = 'Mutate hours (works - wages) not cumulative'
        self.lblprof.setText(lblptext)
        self.lblt.setStyleSheet("color: black")
        self.lblt.setText(lbltext)
    elif wrkgr > 100 and wrkgr < 104 and msoort < 5:
        stmt = update(orders_intern).where(orders_intern.c.werkorderID == mwerknr).\
            values(werk_lonen = orders_intern.c.werk_lonen+loonk,
           wverzinken = orders_intern.c.wverzinken+muren+mu125+mu150+mu200\
           +mmeerw100+mmeerw125+mmeerw150+mmeerw200,\
           werk_reis_uren = orders_intern.c.werk_reis_uren+mreis,\
           meerminderwerk = orders_intern.c.meerminderwerk + meerk)
        con.execute(stmt)
        sel = select([orders_intern]).where(orders_intern.c.werkorderID == mwerknr)
        rpsel = con.execute(sel).first()
        self.urenbegrEdit.setText('{:<12.2f}'.format(rpsel[43]))
        self.urentotEdit.setText('{:<12.2f}'.format(rpsel[44]))
        lblptext = 'Totals: Realised / Budgeted\nhours galvanize'
        lbltext = 'Mutate hours (works - wages) not cumulative'
        self.lblprof.setText(lblptext)
        self.lblt.setStyleSheet("color: black")
        self.lblt.setText(lbltext)
    elif wrkgr > 103 and wrkgr < 107 and msoort < 5:
        stmt = update(orders_intern).where(orders_intern.c.werkorderID == mwerknr).\
            values(werk_lonen = orders_intern.c.werk_lonen+loonk,
           wmoffelen = orders_intern.c.wmoffelen+muren+mu125+mu150+mu200\
           +mmeerw100+mmeerw125+mmeerw150+mmeerw200,\
           werk_reis_uren = orders_intern.c.werk_reis_uren+mreis,\
           meerminderwerk = orders_intern.c.meerminderwerk + meerk)
        con.execute(stmt)
        sel = select([orders_intern]).where(orders_intern.c.werkorderID == mwerknr)
        rpsel = con.execute(sel).first()
        self.urenbegrEdit.setText('{:<12.2f}'.format(rpsel[45]))
        self.urentotEdit.setText('{:<12.2f}'.format(rpsel[46]))
        lblptext = 'Totals: Realised / Budgeted\nhours smuffling'
        lbltext = 'Mutate hours (works - wages) not cumulative'
        self.lblprof.setText(lblptext)
        self.lblt.setStyleSheet("color: black")
        self.lblt.setText(lbltext)
    elif wrkgr > 106 and wrkgr < 110 and msoort < 5:
        stmt = update(orders_intern).where(orders_intern.c.werkorderID == mwerknr).\
            values(werk_lonen = orders_intern.c.werk_lonen+loonk,
           wschilderen = orders_intern.c.wschilderen+muren+mu125+mu150+mu200\
           +mmeerw100+mmeerw125+mmeerw150+mmeerw200,\
           werk_reis_uren = orders_intern.c.werk_reis_uren+mreis,\
           meerminderwerk = orders_intern.c.meerminderwerk + meerk)
        con.execute(stmt)
        sel = select([orders_intern]).where(orders_intern.c.werkorderID == mwerknr)
        rpsel = con.execute(sel).first()
        self.urenbegrEdit.setText('{:<12.2f}'.format(rpsel[47]))
        self.urentotEdit.setText('{:<12.2f}'.format(rpsel[48]))
        lblptext = 'Totals: Realised / Budgeted\nhours painting'
        lbltext = 'Mutate hours (works - wages) not cumulative'
        self.lblprof.setText(lblptext)
        self.lblt.setStyleSheet("color: black")
        self.lblt.setText(lbltext)
    elif wrkgr > 109 and wrkgr < 113 and msoort < 5:
        stmt = update(orders_intern).where(orders_intern.c.werkorderID == mwerknr).\
            values(werk_lonen = orders_intern.c.werk_lonen+loonk,
           wspuiten = orders_intern.c.wspuiten+muren+mu125+mu150+mu200\
           +mmeerw100+mmeerw125+mmeerw150+mmeerw200,\
           werk_reis_uren = orders_intern.c.werk_reis_uren+mreis,\
           meerminderwerk = orders_intern.c.meerminderwerk + meerk)
        con.execute(stmt)
        sel = select([orders_intern]).where(orders_intern.c.werkorderID == mwerknr)
        rpsel = con.execute(sel).first()
        self.urenbegrEdit.setText('{:<12.2f}'.format(rpsel[49]))
        self.urentotEdit.setText('{:<12.2f}'.format(rpsel[50]))
        lblptext = 'Totals: Realised / Budgeted\nhours spraying'
        lbltext = 'Mutate hours (works - wages) not cumulative'
        self.lblprof.setText(lblptext)
        self.lblt.setStyleSheet("color: black")
        self.lblt.setText(lbltext)
    elif wrkgr > 112 and wrkgr < 116 and msoort < 5:
        stmt = update(orders_intern).where(orders_intern.c.werkorderID == mwerknr).\
            values(werk_lonen = orders_intern.c.werk_lonen+loonk,
           wponsen = orders_intern.c.wponsen+muren+mu125+mu150+mu200\
           +mmeerw100+mmeerw125+mmeerw150+mmeerw200,\
           werk_reis_uren = orders_intern.c.werk_reis_uren+mreis,\
           meerminderwerk = orders_intern.c.meerminderwerk + meerk)
        con.execute(stmt)
        sel = select([orders_intern]).where(orders_intern.c.werkorderID == mwerknr)
        rpsel = con.execute(sel).first()
        self.urenbegrEdit.setText('{:<12.2f}'.format(rpsel[51]))
        self.urentotEdit.setText('{:<12.2f}'.format(rpsel[52]))
        lblptext = 'Totals: Realised / Budgeted\nhours punching'
        lbltext = 'Mutate hours (works - wages) not cumulative'
        self.lblprof.setText(lblptext)
        self.lblt.setStyleSheet("color: black")
        self.lblt.setText(lbltext)
    elif wrkgr > 115 and wrkgr < 119 and msoort < 5:
        stmt = update(orders_intern).where(orders_intern.c.werkorderID == mwerknr).\
            values(werk_lonen = orders_intern.c.werk_lonen+loonk,
           wpersen = orders_intern.c.wpersen+muren+mu125+mu150+mu200\
           +mmeerw100+mmeerw125+mmeerw150+mmeerw200,\
           werk_reis_uren = orders_intern.c.werk_reis_uren+mreis,\
           meerminderwerk = orders_intern.c.meerminderwerk + meerk)
        con.execute(stmt)
        sel = select([orders_intern]).where(orders_intern.c.werkorderID == mwerknr)
        rpsel = con.execute(sel).first()
        self.urenbegrEdit.setText('{:<12.2f}'.format(rpsel[53]))
        self.urentotEdit.setText('{:<12.2f}'.format(rpsel[54]))
        lblptext = 'Totals: Realised / Budgeted\nhours pressing'
        lbltext = 'Mutate hours (works - wages) not cumulative'
        self.lblprof.setText(lblptext)
        self.lblt.setStyleSheet("color: black")
        self.lblt.setText(lbltext)
    elif wrkgr > 118 and wrkgr < 122 and msoort < 5:
        stmt = update(orders_intern).where(orders_intern.c.werkorderID == mwerknr).\
           values(werk_lonen = orders_intern.c.werk_lonen+loonk,
           wgritstralen = orders_intern.c.wgritstralen+muren+mu125+mu150+mu200\
           +mmeerw100+mmeerw125+mmeerw150+mmeerw200,\
           werk_reis_uren = orders_intern.c.werk_reis_uren+mreis,\
           meerminderwerk = orders_intern.c.meerminderwerk + meerk)
        con.execute(stmt)
        sel = select([orders_intern]).where(orders_intern.c.werkorderID == mwerknr)
        rpsel = con.execute(sel).first()
        self.urenbegrEdit.setText('{:<12.2f}'.format(rpsel[55]))
        self.urentotEdit.setText('{:<12.2f}'.format(rpsel[56]))
        lblptext = 'Totals: Realised / Budgeted\nhours gritblasting'
        lbltext = 'Mutate hours (works - wages) not cumulative'
        self.lblprof.setText(lblptext)
        self.lblt.setStyleSheet("color: black")
        self.lblt.setText(lbltext)
    elif wrkgr > 121 and wrkgr < 125 and msoort < 5:
        stmt = update(orders_intern).where(orders_intern.c.werkorderID == mwerknr).\
            values(werk_lonen = orders_intern.c.werk_lonen+loonk,
           wmontage = orders_intern.c.wmontage+muren+mu125+mu150+mu200\
           +mmeerw100+mmeerw125+mmeerw150+mmeerw200,\
           werk_reis_uren = orders_intern.c.werk_reis_uren+mreis,\
           meerminderwerk = orders_intern.c.meerminderwerk + meerk)
        con.execute(stmt)
        sel = select([orders_intern]).where(orders_intern.c.werkorderID == mwerknr)
        rpsel = con.execute(sel).first()
        self.urenbegrEdit.setText('{:<12.2f}'.format(rpsel[57]))
        self.urentotEdit.setText('{:<12.2f}'.format(rpsel[58]))
        lblptext = 'Totals: Realised / Budgeted\nhours mounting'
        lbltext = 'Mutate hours (works - wages) not cumulative'
        self.lblprof.setText(lblptext)
        self.lblt.setStyleSheet("color: black")
        self.lblt.setText(lbltext)
    else:
        msaldo = ''
        logger.debug("urenBoeking(self=%s,m_email=%s): msaldo → %s", self, m_email, msaldo, extra={"event.action": "urenBoeking"})
        mboekuren = str(mboekuren)
        if msoort == 5 and wrkgr > 52:
            selsal = select([werknemers]).where(werknemers.c.accountID == maccountnr)
            rpsal = con.execute(selsal).first()
            logger.debug("urenBoeking(self=%s,m_email=%s): rpsal → %s", self, m_email, rpsal, extra={"event.action": "urenBoeking"})
            msaldo = str(rpsal[3])
            lbltext = mboekuren+' Leave hours entered, Balance = '+msaldo+' hours.'
            lblptext = '\n'
            self.lblt.setStyleSheet("color: navy")
            self.lblt.setText(lbltext)
            self.lblprof.setText(lblptext)
        elif msoort == 6 and wrkgr > 52:
            lbltext = mboekuren+' Extra leave hours entered'
            lblptext = '\n'
            self.lblt.setStyleSheet("color: navy")
            self.lblt.setText(lbltext)
            self.lblprof.setText(lblptext)
        elif msoort == 7 and wrkgr > 52:
            lbltext = mboekuren+' Illness hours entered'
            lblptext = '\n'
            self.lblt.setStyleSheet("color: navy")
            self.lblt.setText(lbltext)
            self.lblprof.setText(lblptext)
        elif msoort == 8 and wrkgr > 52:
            lbltext = mboekuren+' Hours holiday entered'
            lblptext = '\n'
            self.lblt.setStyleSheet("color: navy")
            self.lblt.setText(lbltext)
            self.lblprof.setText(lblptext)
        elif msoort == 9 and wrkgr > 52:
            lbltext = mboekuren+' Hours doctor visit entered'
            lblptext = '\n'
            self.lblt.setStyleSheet("color: navy")
            self.lblt.setText(lbltext)
            self.lblprof.setText(lblptext)
        elif msoort == 10 and wrkgr > 52:
            lbltext = mboekuren+' Hours allowed absence entered'
            lblptext = '\n'
            self.lblt.setStyleSheet("color: navy")
            self.lblt.setText(lbltext)
            self.lblprof.setText(lblptext)
        elif msoort == 11 and wrkgr > 52:
            lbltext = mboekuren+' Hours illegal absence entered'
            lblptext = '\n'
            self.lblt.setStyleSheet("color: navy")
            self.lblt.setText(lbltext)
            self.lblprof.setText(lblptext)
        else:
            self.urenEdit.setText('0')
            self.lblt.setStyleSheet("font: bold;color: red")
            self.lblt.setText('Person not in this labor pool!')
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
            
            self.setWindowTitle("Entering hours of internal work - wages")
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
            reg_ex = QRegExp("^[7]{1}[0-9]{8}$")
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
            self.k0Edit.addItem('Travel')
            self.k0Edit.addItem('Leave')
            self.k0Edit.addItem('Extra leave')
            self.k0Edit.addItem('Illness')
            self.k0Edit.addItem('Holiday')
            self.k0Edit.addItem('Doctor')
            self.k0Edit.addItem('Allowed absence')
            self.k0Edit.addItem('Illegal absence')
  
            self.cBox = QCheckBox('More/less work')
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
                logger.warning(">>> Entering k0Changed()", extra={"event.action": "k0Changed"})
                self.k0Edit.setCurrentText(self.k0Edit.currentText())
            self.k0Edit.currentTextChanged.connect(k0Changed)
            '''
            
            def k0Changed():
                logger.debug("k0Changed(): k0Edit → %s", k0Edit, extra={"event.action": "k0Changed"})
                self.k0Edit.setCurrentIndex(self.k0Edit.currentIndex())
            self.k0Edit.currentIndexChanged.connect(k0Changed)
                        
            def  cboxChanged():
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

            self.lblt = QLabel('Mutate hours (works - wages) not cumulative')
            self.lblt.setStyleSheet("color: black")
            self.lblt.setFont(QFont("Arial", 10))
            grid.addWidget(self.lblt , 12, 0, 1, 4, Qt.AlignCenter)
            
            lbl1 = QLabel('Account number')
            lbl1.setFont(QFont("Arial", 10))
            grid.addWidget(lbl1, 6, 1, 1, 1, Qt.AlignRight)
            grid.addWidget(self.zkaccEdit , 6, 2, 1, 1, Qt.AlignRight)
            
            lbl2 = QLabel('Work order number')
            lbl2.setFont(QFont("Arial", 10))
            grid.addWidget(lbl2, 7, 1, 1, 1, Qt.AlignRight)
            grid.addWidget(self.zkwerknEdit, 7, 2, 1, 1, Qt.AlignRight)
                
            lbl3 = QLabel('Type of hours')
            lbl3.setFont(QFont("Arial", 10))
            grid.addWidget(lbl3, 8, 1, 1, 1, Qt.AlignRight)
            grid.addWidget(self.k0Edit, 8, 2, 1, 1, Qt.AlignRight)
                        
            grid.addWidget(self.cBox, 8, 3)
            
            self.lblprof = QLabel('Totals:Realised/Budgeted Hours')
            self.lblprof.setFont(QFont("Arial", 10))
            self.lblprof.setFixedWidth(200)
            self.lblprof.setAlignment(Qt.AlignRight)
            grid.addWidget(self.lblprof, 9, 1, 1, 1, Qt.AlignRight | Qt.AlignTop)
            grid.addWidget(self.urentotEdit, 9, 2, 1, 1, Qt.AlignRight)
            grid.addWidget(self.urenbegrEdit, 9, 3, 1, 1)
            
            lbl4 = QLabel('Hours mutation')
            lbl4.setFont(QFont("Arial", 10))
            grid.addWidget(lbl4, 10, 1, 1, 1, Qt.AlignRight)
            grid.addWidget(self.urenEdit, 10, 2, 1, 1, Qt.AlignRight)
                                       
            lbl5 = QLabel('Book date')
            lbl5.setFont(QFont("Arial", 10))
            grid.addWidget(lbl5, 11, 1, 1, 1, Qt.AlignRight)
            grid.addWidget(self.boekdatumEdit, 11, 2, 1, 1, Qt.AlignRight)
            
            self.applyBtn = QPushButton('Mutate')
            self.applyBtn.clicked.connect(lambda: urenBoeking(self, m_email))
               
            self.applyBtn.setFont(QFont("Arial",10))
            self.applyBtn.setFixedWidth(100)
            self.applyBtn.setStyleSheet("color: black;  background-color: gainsboro") 
               
            grid.addWidget(self.applyBtn,13, 3 , 1 , 1, Qt.AlignRight)
                
            cancelBtn = QPushButton('Close')
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email)) 
    
            grid.addWidget(cancelBtn, 13, 2, 1 , 1, Qt.AlignRight)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black; background-color: gainsboro") 
                   
            infoBtn = QPushButton('Information')
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