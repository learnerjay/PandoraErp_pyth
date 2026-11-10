from login import hoofdMenu
import datetime
from PyQt5.QtWidgets import QLabel, QLineEdit, QGridLayout, QPushButton,\
             QDialog, QMessageBox 
from PyQt5.QtGui import QRegExpValidator, QFont, QPixmap, QIcon, QMovie
from PyQt5.QtCore import Qt, QRegExp, QSize
from sqlalchemy import (Table, Column, Integer, String, Float, ForeignKey, \
                        MetaData, create_engine, and_, func)
from sqlalchemy.sql import select, update, insert
import logging
logger = logging.getLogger(__name__)

metadata = MetaData()
orders_inkoop = Table('orders_inkoop', metadata,
    Column('orderinkoopID', Integer(), primary_key=True),
    Column('leverancierID', None, ForeignKey('leveranciers.leverancierID')),
    Column('besteldatum', String),
    Column('goedgekeurd', String),
    Column('betaald', String),
    Column('afgemeld', String))
leveranciers = Table('leveranciers', metadata,
    Column('leverancierID', Integer(), primary_key=True),
    Column('bedrijfsnaam', String),
    Column('rechtsvorm', String),
    Column('postcode', String),
    Column('huisnummer', String),
    Column('toevoeging', String))
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
    Column('meerminderwerk', Float),
    Column('regel', Integer))
werken = Table('werken', metadata,
    Column('werknummerID', Integer, primary_key=True))

def closeRegels(m_email, minkordernr, mregel, self):
    logger.warning(">>> Entering closeRegels(m_email=%s,minkordernr=%s,mregel=%s)", m_email, minkordernr, mregel, extra={"event.action": "closeRegels", "logrite.minkordernr": minkordernr, "logrite.mregel": mregel})
    self.close()
    dienstenOrder(m_email, minkordernr, mregel)
    logger.debug("<<< Exiting closeRegels(m_email=%s,minkordernr=%s,mregel=%s)", m_email, minkordernr, mregel, extra={"event.action": "closeRegels", "logrite.minkordernr": minkordernr, "logrite.mregel": mregel})

def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    
def wijzSluit(m_email, minkordernr, mregel ,self):
    logger.warning(">>> Entering wijzSluit(m_email=%s,minkordernr=%s,mregel=%s)", m_email, minkordernr, mregel, extra={"event.action": "wijzSluit", "logrite.minkordernr": minkordernr, "logrite.mregel": mregel})
    self.close()
    zoekInkooporder(m_email, minkordernr, mregel)
    logger.debug("<<< Exiting wijzSluit(m_email=%s,minkordernr=%s,mregel=%s)", m_email, minkordernr, mregel, extra={"event.action": "wijzSluit", "logrite.minkordernr": minkordernr, "logrite.mregel": mregel})

def invoerOK(message):
    logger.warning(">>> Entering invoerOK(message=%s)", message, extra={"event.action": "invoerOK", "logrite.message": message})
    msg = QMessageBox()
    logger.debug("invoerOK(message=%s): msg → %s", message, msg, extra={"event.action": "invoerOK", "logrite.message": message})
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Information)
    msg.setText('Invoer gelukt!' + message)
    msg.setWindowTitle('Wijzig orders stelposten')
    logger.debug("<<< Exiting invoerOK(message=%s)", message, extra={"event.action": "invoerOK", "logrite.message": message})
    msg.exec_()
        
def foutCombinatie():
    logger.warning(">>> Entering foutCombinatie()", extra={"event.action": "foutCombinatie"})
    msg = QMessageBox()
    logger.debug("foutCombinatie(): msg → %s", msg, extra={"event.action": "foutCombinatie"})
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Dir is geen inkoop order voor stelposten!')
    msg.setWindowTitle('Wijzig orders stelposten')
    logger.debug("<<< Exiting foutCombinatie()", extra={"event.action": "foutCombinatie"})
    msg.exec_()   
       
def foutDienstorder():
    logger.warning(">>> Entering foutDienstorder()", extra={"event.action": "foutDienstorder"})
    msg = QMessageBox()
    logger.debug("foutDienstorder(): msg → %s", msg, extra={"event.action": "foutDienstorder"})
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Order voor stelpost niet gevonden!')
    msg.setWindowTitle('Wijzig orders stelposten')
    logger.debug("<<< Exiting foutDienstorder()", extra={"event.action": "foutDienstorder"})
    msg.exec_()
                
def zoekInkooporder(m_email, minkordernr, mregel):
    logger.warning(">>> Entering zoekInkooporder(m_email=%s,minkordernr=%s,mregel=%s)", m_email, minkordernr, mregel, extra={"event.action": "zoekInkooporder", "logrite.minkordernr": minkordernr, "logrite.mregel": mregel})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle('Wijzig order voor stelposten')
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            self.setFont(QFont('Arial', 10))
                            
            self.Inkoopordernummer = QLabel()
            inkordEdit = QLineEdit(str(minkordernr))
            inkordEdit.setFixedWidth(100)
            inkordEdit.setFont(QFont("Arial",10))
            inkordEdit.textChanged.connect(self.inkordChanged)
            reg_ex = QRegExp('^[4]{1}[0-9]{8}$')
            input_validator = QRegExpValidator(reg_ex, inkordEdit)
            inkordEdit.setValidator(input_validator)
                            
            grid = QGridLayout()
            grid.setSpacing(20)
    
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 0, 0)
            
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 1, 1, 1, Qt.AlignRight)
    
            self.setFont(QFont('Arial', 10))
   
            grid.addWidget(QLabel('Inkoop order voor stelposten'), 1, 0, 1, 2)
            grid.addWidget(inkordEdit, 1, 1)
       
            cancelBtn = QPushButton('Sluiten')
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
        
            applyBtn = QPushButton('Zoeken')
            applyBtn.clicked.connect(self.accept)
                  
            grid.addWidget(applyBtn, 2, 1, 1 , 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
        
            grid.addWidget(cancelBtn, 2, 0, 1, 1, Qt.AlignRight)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'),3 , 0, 1, 2, Qt.AlignCenter)
            
            self.setLayout(grid)
            self.setGeometry(600, 350, 150, 150)
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
    
        def inkordChanged(self, text):
            self.Inkoopordernummer.setText(text)
            logger.warning(">>> Entering inkordChanged(text=%s)", text, extra={"event.action": "inkordChanged", "logrite.text": text})
            logger.debug("<<< Exiting inkordChanged(text=%s)", text, extra={"event.action": "inkordChanged", "logrite.text": text})
    
        def returnInkoopordernummer(self):
            return self.Inkoopordernummer.text()
    
        logger.warning(">>> Entering returnInkoopordernummer()", extra={"event.action": "returnInkoopordernummer"})
        logger.debug("<<< Exiting returnInkoopordernummer()", extra={"event.action": "returnInkoopordernummer"})
        @staticmethod
        def getData(parent=None):
            dialog = Widget(parent)
            dialog.exec_()
            logger.debug("<<< Exiting getData(parent=%s)", parent, extra={"event.action": "getData"})
            return [dialog.returnInkoopordernummer()]
       
    window = Widget()
    data = window.getData()
    if data[0]:
        minkordernr = data[0]

    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    conn = engine.connect()
    s = select([orders_inkoop]).where(orders_inkoop.c.orderinkoopID == minkordernr)
    rp1 = conn.execute(s).first()
    mregel = 0
    if rp1:
        dienstenOrder(m_email, minkordernr, mregel)
    else:
        foutDienstorder()
        zoekInkooporder(m_email, minkordernr, mregel)

def dienstenOrder(m_email, minkordernr, mregel):
    logger.warning(">>> Entering dienstenOrder(m_email=%s,minkordernr=%s,mregel=%s)", m_email, minkordernr, mregel, extra={"event.action": "dienstenOrder", "logrite.minkordernr": minkordernr, "logrite.mregel": mregel})

    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("dienstenOrder(m_email=%s,minkordernr=%s,mregel=%s): engine → %s", m_email, minkordernr, mregel, engine, extra={"event.action": "dienstenOrder", "logrite.minkordernr": minkordernr, "logrite.mregel": mregel})
    conn = engine.connect()  
    logger.debug("dienstenOrder(m_email=%s,minkordernr=%s,mregel=%s): conn → %s", m_email, minkordernr, mregel, conn, extra={"event.action": "dienstenOrder", "logrite.minkordernr": minkordernr, "logrite.mregel": mregel})
    
    sel1 = select([orders_inkoop]).where(orders_inkoop.c.orderinkoopID == minkordernr)
    logger.debug("dienstenOrder(m_email=%s,minkordernr=%s,mregel=%s): sel1 → %s", m_email, minkordernr, mregel, sel1, extra={"event.action": "dienstenOrder", "logrite.minkordernr": minkordernr, "logrite.mregel": mregel})
    sel2 = select([leveranciers]).where(and_(leveranciers.c.leverancierID ==\
        orders_inkoop.c.leverancierID, orders_inkoop.c.orderinkoopID == minkordernr))
    logger.debug("dienstenOrder(m_email=%s,minkordernr=%s,mregel=%s): sel2 → %s", m_email, minkordernr, mregel, sel2, extra={"event.action": "dienstenOrder", "logrite.minkordernr": minkordernr, "logrite.mregel": mregel})
    sel3 = select([orders_inkoop_diensten]).where(orders_inkoop_diensten.\
                c.orderinkoopID == minkordernr).order_by(orders_inkoop_diensten.c.regel)
    logger.debug("dienstenOrder(m_email=%s,minkordernr=%s,mregel=%s): sel3 → %s", m_email, minkordernr, mregel, sel3, extra={"event.action": "dienstenOrder", "logrite.minkordernr": minkordernr, "logrite.mregel": mregel})
    sel4 = select([werken]).where(and_(werken.c.werknummerID==\
             orders_inkoop_diensten.c.werknummerID, orders_inkoop_diensten.c.orderinkoopID == minkordernr))
    rp1 = conn.execute(sel1).first()
    logger.debug("dienstenOrder(m_email=%s,minkordernr=%s,mregel=%s): sel4 → %s", m_email, minkordernr, mregel, sel4, extra={"event.action": "dienstenOrder", "logrite.minkordernr": minkordernr, "logrite.mregel": mregel})
    logger.debug("dienstenOrder(m_email=%s,minkordernr=%s,mregel=%s): rp1 → %s", m_email, minkordernr, mregel, rp1, extra={"event.action": "dienstenOrder", "logrite.minkordernr": minkordernr, "logrite.mregel": mregel})
    rp2 = conn.execute(sel2).first()
    rp3 = conn.execute(sel3)
    rp3a = conn.execute(sel3).first()
    logger.debug("dienstenOrder(m_email=%s,minkordernr=%s,mregel=%s): rp2 → %s", m_email, minkordernr, mregel, rp2, extra={"event.action": "dienstenOrder", "logrite.minkordernr": minkordernr, "logrite.mregel": mregel})
    rp4 = conn.execute(sel4).first()
    mpostcode = rp2[3]
    logger.debug("dienstenOrder(m_email=%s,minkordernr=%s,mregel=%s): rp3 → %s", m_email, minkordernr, mregel, rp3, extra={"event.action": "dienstenOrder", "logrite.minkordernr": minkordernr, "logrite.mregel": mregel})
    mhuisnr = int(rp2[4])
    if conn.execute(sel3).fetchone():
        logger.debug("dienstenOrder(m_email=%s,minkordernr=%s,mregel=%s): rp3a → %s", m_email, minkordernr, mregel, rp3a, extra={"event.action": "dienstenOrder", "logrite.minkordernr": minkordernr, "logrite.mregel": mregel})
        mwerknr = rp4[0]
        rp3 = conn.execute(sel3)
    else:
        logger.debug("dienstenOrder(m_email=%s,minkordernr=%s,mregel=%s): rp4 → %s", m_email, minkordernr, mregel, rp4, extra={"event.action": "dienstenOrder", "logrite.minkordernr": minkordernr, "logrite.mregel": mregel})
        logger.debug("dienstenOrder(m_email=%s,minkordernr=%s,mregel=%s): mpostcode → %s", m_email, minkordernr, mregel, mpostcode, extra={"event.action": "dienstenOrder", "logrite.minkordernr": minkordernr, "logrite.mregel": mregel})
        logger.debug("dienstenOrder(m_email=%s,minkordernr=%s,mregel=%s): mhuisnr → %s", m_email, minkordernr, mregel, mhuisnr, extra={"event.action": "dienstenOrder", "logrite.minkordernr": minkordernr, "logrite.mregel": mregel})
        foutCombinatie()
        zoekInkooporder(m_email, minkordernr, mregel)
    import postcode
    mstrpls = postcode.checkpostcode(mpostcode, mhuisnr)
    logger.debug("dienstenOrder(m_email=%s,minkordernr=%s,mregel=%s): mwerknr → %s", m_email, minkordernr, mregel, mwerknr, extra={"event.action": "dienstenOrder", "logrite.minkordernr": minkordernr, "logrite.mregel": mregel})
    mstraat = mstrpls[0]
    mplaats = mstrpls[1]
                    
    logger.debug("dienstenOrder(m_email=%s,minkordernr=%s,mregel=%s): mstrpls → %s", m_email, minkordernr, mregel, mstrpls, extra={"event.action": "dienstenOrder", "logrite.minkordernr": minkordernr, "logrite.mregel": mregel})
    class Widget(QDialog):
        logger.debug("<<< Exiting dienstenOrder(m_email=%s,minkordernr=%s,mregel=%s)", m_email, minkordernr, mregel, extra={"event.action": "dienstenOrder", "logrite.minkordernr": minkordernr, "logrite.mregel": mregel})
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle('Wijzig order voor stelposten')
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))

            self.Sum = QLabel()
            provEdit = QLineEdit(str(rp3a[12]))
            provEdit.setCursorPosition(0)
            provEdit.setFixedWidth(110)
            provEdit.setFont(QFont("Arial", 10))
            provEdit.setDisabled(True)

            # Type of provisional sum
            typelist = ['inhuur', 'leiding', 'huisvesting', 'grondverzet','transport', 'overig']
            typeEdit = QLineEdit(typelist[int(rp3a[3][0])-1])
            typeEdit.setCursorPosition(0)
            typeEdit.setFixedWidth(110)
            typeEdit.setFont(QFont("Arial", 10))
            typeEdit.setDisabled(True)

            self.Inkoopordernummer = QLabel()
            inkordEdit = QLineEdit(str(minkordernr))
            inkordEdit.setFixedWidth(110)
            inkordEdit.setAlignment(Qt.AlignRight)
            inkordEdit.setDisabled(True)
            inkordEdit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
            inkordEdit.textChanged.connect(self.inkordChanged)
 
            self.Werknummer = QLabel()
            werknEdit = QLineEdit(str(mwerknr))
            werknEdit.setFixedWidth(110)
            werknEdit.setAlignment(Qt.AlignRight)
            werknEdit.setDisabled(True)
            werknEdit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
            werknEdit.textChanged.connect(self.werknChanged)
       
            self.Besteldatum = QLabel()
            q3Edit = QLineEdit()
            datum = str(datetime.datetime.now())
            q3Edit.setText((datum[8:10]+'-'+datum[5:8]+datum[0:4]))
            q3Edit.setDisabled(True)
            q3Edit.setFixedWidth(110)
            q3Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
            
            self.Goedgekeurd = QLabel()
            q4Edit = QLineEdit(rp1[3])
            q4Edit.setCursorPosition(0)
            q4Edit.setFixedWidth(110)
            q4Edit.setFont(QFont("Arial",10))
            q4Edit.textChanged.connect(self.q4Changed)
            reg_ex = QRegExp('^[2]{1}[0]{1}[0-9]{2}[-]{1}[0-1]{1}[0-9]{1}[-]{1}[0-3]{1}[0-9]{1}$')
            input_validator = QRegExpValidator(reg_ex, q4Edit)
            q4Edit.setValidator(input_validator)  
                    
            self.Betaald = QLabel()
            q5Edit = QLineEdit(rp1[4])
            q5Edit.setCursorPosition(0)
            q5Edit.setFixedWidth(110)
            q5Edit.setFont(QFont("Arial",10))
            q5Edit.textChanged.connect(self.q5Changed)
            reg_ex = QRegExp('^[2]{1}[0]{1}[0-9]{2}[-]{1}[0-1]{1}[0-9]{1}[-]{1}[0-3]{1}[0-9]{1}$')
            input_validator = QRegExpValidator(reg_ex, q5Edit)
            q5Edit.setValidator(input_validator)  

            self.Afgemeld = QLabel()
            q6Edit = QLineEdit(rp1[5])
            q6Edit.setCursorPosition(0)
            q6Edit.setFixedWidth(110)
            q6Edit.setFont(QFont("Arial",10))
            q6Edit.textChanged.connect(self.q6Changed)
            reg_ex = QRegExp('^[2]{1}[0]{1}[0-9]{2}[-]{1}[0-1]{1}[0-9]{1}[-]{1}[0-3]{1}[0-9]{1}$')
            input_validator = QRegExpValidator(reg_ex, q6Edit)
            q6Edit.setValidator(input_validator) 
                                 
            grid = QGridLayout()
            grid.setSpacing(20)

            pyqt = QLabel()
            movie = QMovie('./images/logos/pyqt.gif')
            pyqt.setMovie(movie)
            movie.setScaledSize(QSize(180, 60))
            movie.start()
            grid.addWidget(pyqt, 1, 0, 1, 2)
                    
            self.setFont(QFont('Arial', 10))
            grid.addWidget(QLabel('Order voor\nLeverancier: '+str(rp2[0])+\
              ',\n'+rp2[1]+' '+rp2[2]+',\n'+mstraat+' '+str(rp2[4])+\
              rp2[5]+',\n'+rp2[3]+' '+mplaats+'.'), 1, 1, 1 , 2)

            grid.addWidget(QLabel('Stelpost bedrag'), 3, 0, 1, 1, Qt.AlignRight)
            grid.addWidget(provEdit, 3, 1)

            grid.addWidget(QLabel('Stelpost\nType'), 3, 2)
            grid.addWidget(typeEdit, 3, 2, 1, 2, Qt.AlignRight)

            grid.addWidget(QLabel('Inkoop ordernummer'), 4, 0, 1, 1, Qt.AlignRight)
            grid.addWidget(inkordEdit, 4, 1)
            
            grid.addWidget(QLabel('Werknummer'), 5, 0, 1, 1, Qt.AlignRight)
            grid.addWidget(werknEdit, 5, 1)           
        
            grid.addWidget(QLabel('Order datum'),6, 0, 1, 1, Qt.AlignRight)
            grid.addWidget(q3Edit, 6, 1)  
                   
            grid.addWidget(QLabel('Goedgekeurd jjjj-mm-dd'), 7, 0, 1, 1, Qt.AlignRight)
            grid.addWidget(q4Edit, 7, 1) 
            
            grid.addWidget(QLabel('Betaald jjjj-mm-dd'), 8, 0, 1, 1, Qt.AlignRight)
            grid.addWidget(q5Edit, 8, 1)  
            
            grid.addWidget(QLabel('Afgesloten jjjj-mm-dd'), 9, 0, 1, 1, Qt.AlignRight)
            grid.addWidget(q6Edit, 9, 1)  
          
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 10, 0, 1, 3, Qt.AlignCenter)
            
            applyBtn = QPushButton('Orderregels')
            applyBtn.clicked.connect(self.accept)
                          
            cancelBtn = QPushButton('Sluiten')
            cancelBtn.clicked.connect(lambda: wijzSluit(m_email, minkordernr, 0 ,self))
                       
            grid.addWidget(applyBtn, 9, 2, 1 , 2, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(200)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")

            insertBtn = QPushButton('Invoer nieuwe orderregel')
            insertBtn.clicked.connect(lambda: insertRegels(m_email, minkordernr, self))

            grid.addWidget(insertBtn, 8, 2, 1, 2, Qt.AlignRight)
            insertBtn.setFont(QFont("Arial", 10))
            insertBtn.setFixedWidth(200)
            insertBtn.setStyleSheet("color: black;  background-color: gainsboro")
       
            grid.addWidget(cancelBtn, 7, 2, 1 , 2, Qt.AlignRight)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(200)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            self.setLayout(grid)
            self.setGeometry(600, 300, 350, 300)
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Inkoopordernummer → %s", parent, self.Inkoopordernummer, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q1Edit → %s", parent, q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q1Edit → %s", self, parent, q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Werknummer → %s", parent, self.Werknummer, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q2Edit → %s", parent, q2Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q2Edit → %s", self, parent, q2Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Werkomschrijving → %s", parent, self.Werkomschrijving, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q3Edit → %s", parent, q3Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q3Edit → %s", self, parent, q3Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Omschrijving → %s", parent, self.Omschrijving, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q4Edit → %s", parent, q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q4Edit → %s", self, parent, q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): reg_ex → %s", parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): reg_ex → %s", self, parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): input_validator → %s", parent, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): input_validator → %s", self, parent, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Aanneemsom → %s", parent, self.Aanneemsom, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q5Edit → %s", parent, q5Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q5Edit → %s", self, parent, q5Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.GeplandeStart → %s", parent, self.GeplandeStart, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q6Edit → %s", parent, q6Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q6Edit → %s", self, parent, q6Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.WerkelijkeStart → %s", parent, self.WerkelijkeStart, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q7Edit → %s", parent, q7Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q7Edit → %s", self, parent, q7Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.GeplandGereed → %s", parent, self.GeplandGereed, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q8Edit → %s", parent, q8Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q8Edit → %s", self, parent, q8Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.WerkelijkGereed → %s", parent, self.WerkelijkGereed, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q9Edit → %s", parent, q9Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q9Edit → %s", self, parent, q9Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.BedragAcceptatie → %s", parent, self.BedragAcceptatie, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q10Edit → %s", parent, q10Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q10Edit → %s", self, parent, q10Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Sum → %s", parent, self.Sum, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q12Edit → %s", parent, q12Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q12Edit → %s", self, parent, q12Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.DatumAcceptatie → %s", parent, self.DatumAcceptatie, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): q11Edit → %s", parent, q11Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q11Edit → %s", self, parent, q11Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): grid → %s", parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl → %s", parent, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl1 → %s", parent, lbl1, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl1 → %s", self, parent, lbl1, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl2 → %s", parent, lbl2, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl2 → %s", self, parent, lbl2, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl3 → %s", parent, lbl3, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl3 → %s", self, parent, lbl3, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl4 → %s", parent, lbl4, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl4 → %s", self, parent, lbl4, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl5 → %s", parent, lbl5, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl5 → %s", self, parent, lbl5, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl6 → %s", parent, lbl6, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl6 → %s", self, parent, lbl6, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl7 → %s", parent, lbl7, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl7 → %s", self, parent, lbl7, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl8 → %s", parent, lbl8, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl8 → %s", self, parent, lbl8, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl9 → %s", parent, lbl9, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl9 → %s", self, parent, lbl9, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl10 → %s", parent, lbl10, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl10 → %s", self, parent, lbl10, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl11 → %s", parent, lbl11, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl11 → %s", self, parent, lbl11, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl12 → %s", parent, lbl12, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl12 → %s", self, parent, lbl12, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn, extra={"event.action": "__init__"})

        def inkordChanged(self, text):
            self.Inkoopordernummer.setText(text)
            
        def werknChanged(self, text):
            logger.warning(">>> Entering werknChanged(text=%s)", text, extra={"event.action": "werknChanged", "logrite.text": text})
            self.Werknummer.setText(text)
            logger.debug("<<< Exiting werknChanged(text=%s)", text, extra={"event.action": "werknChanged", "logrite.text": text})
          
        def q3Changed(self, text):
            self.Besteldatum.setText(text)
            logger.warning(">>> Entering q3Changed(text=%s)", text, extra={"event.action": "q3Changed", "logrite.text": text})
            logger.debug("<<< Exiting q3Changed(text=%s)", text, extra={"event.action": "q3Changed", "logrite.text": text})
            
        def q4Changed(self, text):
            self.Goedgekeurd.setText(text)
            logger.warning(">>> Entering q4Changed(text=%s)", text, extra={"event.action": "q4Changed", "logrite.text": text})
            logger.debug("<<< Exiting q4Changed(text=%s)", text, extra={"event.action": "q4Changed", "logrite.text": text})
            
        def q5Changed(self, text):
            self.Betaald.setText(text)
            logger.warning(">>> Entering q5Changed(text=%s)", text, extra={"event.action": "q5Changed", "logrite.text": text})
            logger.debug("<<< Exiting q5Changed(text=%s)", text, extra={"event.action": "q5Changed", "logrite.text": text})
            
        def q6Changed(self, text):
            logger.warning(">>> Entering q6Changed(text=%s)", text, extra={"event.action": "q6Changed", "logrite.text": text})
            self.Afgemeld.setText(text)
            logger.debug("<<< Exiting q6Changed(text=%s)", text, extra={"event.action": "q6Changed", "logrite.text": text})
                                                          
        def returnInkoopordernummer(self):
            logger.warning(">>> Entering returnInkoopordernummer()", extra={"event.action": "returnInkoopordernummer"})
            return self.Inkoopordernummer.text()
        
        def returnWerknummer(self):
            logger.warning(">>> Entering returnWerknummer()", extra={"event.action": "returnWerknummer"})
            logger.debug("<<< Exiting returnWerknummer()", extra={"event.action": "returnWerknummer"})
            return self.Werknummer.text()     
        
        def returnBesteldatum(self):
            logger.warning(">>> Entering returnBesteldatum()", extra={"event.action": "returnBesteldatum"})
            logger.debug("<<< Exiting returnBesteldatum()", extra={"event.action": "returnBesteldatum"})
            return self.Besteldatum.text()
        
        def returnGoedgekeurd(self):
            logger.warning(">>> Entering returnGoedgekeurd()", extra={"event.action": "returnGoedgekeurd"})
            logger.debug("<<< Exiting returnGoedgekeurd()", extra={"event.action": "returnGoedgekeurd"})
            return self.Goedgekeurd.text()
        
        def returnBetaald(self):
            logger.warning(">>> Entering returnBetaald()", extra={"event.action": "returnBetaald"})
            logger.debug("<<< Exiting returnBetaald()", extra={"event.action": "returnBetaald"})
            return self.Betaald.text()

        def returnAfgemeld(self):
            logger.warning(">>> Entering returnAfgemeld()", extra={"event.action": "returnAfgemeld"})
            logger.debug("<<< Exiting returnAfgemeld()", extra={"event.action": "returnAfgemeld"})
            return self.Afgemeld.text()
                                 
        @staticmethod
        def getData(parent=None):
            dialog = Widget(parent)
            dialog.exec_()
            return [dialog.returnGoedgekeurd(), dialog.returnBetaald(),\
                    dialog.returnAfgemeld()]
            logger.warning(">>> Entering getData(parent=%s)", parent, extra={"event.action": "getData"})
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog, extra={"event.action": "getData"})
    
    window = Widget()
    data = window.getData()
    if data[0]:
        mgoedgek = data[0]
    else:
        mgoedgek = rp1[3]
    if data[1]:
        mbetaald = data[1]
    else:
        mbetaald = rp1[4]
    if data[2]:
        mafgemeld = data[2]
    else:
        mafgemeld = rp1[5]
             
    sel1 = select([orders_inkoop]).where(orders_inkoop.c.orderinkoopID == minkordernr)
    rp1 = conn.execute(sel1).first()
   
    if data[0] or data[1] or data[2]:
        u = update(orders_inkoop).where(orders_inkoop.c.orderinkoopID == minkordernr).\
           values(goedgekeurd=mgoedgek, betaald = mbetaald, afgemeld = mafgemeld)  
        conn.execute(u)
        invoerOK('')
        conn.close()
    mregel = 0
    dienstenRegels(m_email, rp1,rp2, rp3, mstraat, mplaats, mregel)
             
def dienstenRegels(m_email, rp1,rp2, rp3, mstraat, mplaats, mregel):
    logger.warning(">>> Entering dienstenRegels(m_email=%s,rp1=%s,rp2=%s,rp3=%s,mstraat=%s,mplaats=%s,mregel=%s)", m_email, rp1, rp2, rp3, mstraat, mplaats, mregel, extra={"event.action": "dienstenRegels", "logrite.rp1": rp1, "logrite.rp2": rp2, "logrite.rp3": rp3, "logrite.mstraat": mstraat, "logrite.mplaats": mplaats, "logrite.mregel": mregel})
    minkordernr = rp1[0]
    logger.debug("dienstenRegels(m_email=%s,rp1=%s,rp2=%s,rp3=%s,mstraat=%s,mplaats=%s,mregel=%s): minkordernr → %s", m_email, rp1, rp2, rp3, mstraat, mplaats, mregel, minkordernr, extra={"event.action": "dienstenRegels", "logrite.rp1": rp1, "logrite.rp2": rp2, "logrite.rp3": rp3, "logrite.mstraat": mstraat, "logrite.mplaats": mplaats, "logrite.mregel": mregel})
    for row in rp3:
        mregel += 1
        class Widget(QDialog):
            logger.debug("<<< Exiting dienstenRegels(m_email=%s,rp1=%s,rp2=%s,rp3=%s,mstraat=%s,mplaats=%s,mregel=%s)", m_email, rp1, rp2, rp3, mstraat, mplaats, mregel, extra={"event.action": "dienstenRegels", "logrite.rp1": rp1, "logrite.rp2": rp2, "logrite.rp3": rp3, "logrite.mstraat": mstraat, "logrite.mplaats": mplaats, "logrite.mregel": mregel})
            def __init__(self, parent=None):
                super(Widget, self).__init__(parent)
                logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
        
                self.setFont(QFont('Arial', 10))
                self.setWindowTitle('Wijzig stelposten orderregels')
                self.setFont(QFont('Arial', 10))
                                                          
                self.Inkoopordernummer = QLabel()
                q1Edit = QLineEdit(str(minkordernr))
                q1Edit.setDisabled(True)
                q1Edit.setFixedWidth(130)
                q1Edit.setAlignment(Qt.AlignRight)
                q1Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                q1Edit.textChanged.connect(self.q1Changed) 
                
                self.Werknummer = QLabel()
                q2Edit = QLineEdit(str(row[2]))
                q2Edit.setDisabled(True)
                q2Edit.setFixedWidth(130)
                q2Edit.setAlignment(Qt.AlignRight)
                q2Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                q2Edit.textChanged.connect(self.q2Changed) 
                 
                self.Werkomschrijving = QLabel()
                q3Edit = QLineEdit(row[3])
                q3Edit.setFixedWidth(400)
                q3Edit.setDisabled(True)
                q3Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                q3Edit.textChanged.connect(self.q3Changed) 
                
                self.Omschrijving = QLabel()
                q4Edit = QLineEdit(str(row[4]))
                q4Edit.setFixedWidth(400)
                q4Edit.setFont(QFont("Arial",10))
                q4Edit.textChanged.connect(self.q4Changed) 
                reg_ex = QRegExp("^.{0,50}$")
                input_validator = QRegExpValidator(reg_ex, q4Edit)
                q4Edit.setValidator(input_validator)    
            
                self.Aanneemsom = QLabel()
                q5Edit = QLineEdit(str(round(row[5],2)))
                q5Edit.setFixedWidth(130)
                q5Edit.setFont(QFont("Arial",10))
                q5Edit.setAlignment(Qt.AlignRight)
                q5Edit.textChanged.connect(self.q5Changed) 
                reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                input_validator = QRegExpValidator(reg_ex, q5Edit)
                q5Edit.setValidator(input_validator)  
    
                self.GeplandeStart = QLabel()
                q6Edit = QLineEdit(str(row[6]))
                q5Edit.setCursorPosition(0)
                q6Edit.setFixedWidth(130)
                q6Edit.setFont(QFont("Arial",10))
                q6Edit.textChanged.connect(self.q6Changed) 
                reg_ex = QRegExp('^[2]{1}[0]{1}[0-9]{2}[-]{1}[0-1]{1}[0-9]{1}[-]{1}[0-3]{1}[0-9]{1}$')
                input_validator = QRegExpValidator(reg_ex, q6Edit)
                q6Edit.setValidator(input_validator)  
                
                self.WerkelijkeStart = QLabel()
                q7Edit = QLineEdit(str(row[7]))
                q7Edit.setFixedWidth(130)
                q7Edit.setFont(QFont("Arial",10))
                q7Edit.textChanged.connect(self.q7Changed) 
                reg_ex = QRegExp('^[2]{1}[0]{1}[0-9]{2}[-]{1}[0-1]{1}[0-9]{1}[-]{1}[0-3]{1}[0-9]{1}$')
                input_validator = QRegExpValidator(reg_ex, q7Edit)
                q7Edit.setValidator(input_validator)
                
                self.GeplandGereed = QLabel()
                q8Edit = QLineEdit(str(row[8]))
                q5Edit.setCursorPosition(0)
                q8Edit.setFixedWidth(130)
                q8Edit.setFont(QFont("Arial",10))
                q8Edit.textChanged.connect(self.q8Changed) 
                reg_ex = QRegExp('^[2]{1}[0]{1}[0-9]{2}[-]{1}[0-1]{1}[0-9]{1}[-]{1}[0-3]{1}[0-9]{1}$')
                input_validator = QRegExpValidator(reg_ex, q8Edit)
                q8Edit.setValidator(input_validator)  
                
                self.WerkelijkGereed= QLabel()
                q9Edit = QLineEdit(str(row[9]))
                q9Edit.setFixedWidth(130)
                q9Edit.setFont(QFont("Arial",10))
                q9Edit.textChanged.connect(self.q9Changed) 
                reg_ex = QRegExp('^[2]{1}[0]{1}[0-9]{2}[-]{1}[0-1]{1}[0-9]{1}[-]{1}[0-3]{1}[0-9]{1}$')
                input_validator = QRegExpValidator(reg_ex, q9Edit)
                q9Edit.setValidator(input_validator) 
                
                self.BedragAcceptatie = QLabel()
                q10Edit = QLineEdit(str(round(row[10],2)))
                q10Edit.setFixedWidth(130)
                q10Edit.setDisabled(True)
                q10Edit.setAlignment(Qt.AlignRight)
                q10Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                q10Edit.textChanged.connect(self.q10Changed) 
                
                self.Sum = QLabel()
                q12Edit = QLineEdit('{:12.2f}'.format(row[12]))
                q12Edit.setFixedWidth(130)
                q12Edit.setDisabled(True)
                q12Edit.setAlignment(Qt.AlignRight)
                q12Edit.setFont(QFont("Arial",10))

                self.DatumAcceptatie = QLabel()
                q11Edit = QLineEdit(str(row[11]))
                q11Edit.setFixedWidth(130)
                q11Edit.setDisabled(True)
                q11Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                q11Edit.textChanged.connect(self.q11Changed) 
                                                                            
                grid = QGridLayout()
                grid.setSpacing(20)
                              
                lbl = QLabel()
                pixmap = QPixmap('./images/logos/verbinding.jpg')
                lbl.setPixmap(pixmap)
                grid.addWidget(lbl ,1, 0,)
                
                logo = QLabel()
                pixmap = QPixmap('./images/logos/logo.jpg')
                logo.setPixmap(pixmap)
                grid.addWidget(logo , 1, 2, 1, 1, Qt.AlignRight)
           
                self.setFont(QFont('Arial', 10))
                grid.addWidget(QLabel('Order voor\nLeverancier: '+str(rp2[0])+\
                 ',\n'+rp2[1]+' '+rp2[2]+',\n'+mstraat+' '+str(rp2[4])+\
                 rp2[5]+',\n'+rp2[3]+' '+mplaats+'.\nOrder line '+str(mregel)), 1, 1, 1, 2)
                             
                lbl1 = QLabel('Ordernummer')
                lbl1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                grid.addWidget(lbl1, 5, 0)
                grid.addWidget(q1Edit, 5, 1)
                                              
                lbl2 = QLabel('Werknummer')
                lbl2.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                grid.addWidget(lbl2, 6, 0)
                grid.addWidget(q2Edit, 6, 1)
                
                lbl3 = QLabel('Werkomschrijving')
                lbl3.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                grid.addWidget(lbl3, 7, 0)
                grid.addWidget(q3Edit,7, 1, 1, 2)
                           
                lbl4 = QLabel('Omschrijving')
                lbl4.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                grid.addWidget(lbl4, 8, 0)
                grid.addWidget(q4Edit, 8, 1, 1, 2)
                
                lbl5 = QLabel('Aanneemsom')
                lbl5.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                grid.addWidget(lbl5, 9, 0)
                grid.addWidget(q5Edit, 9, 1)
                                        
                lbl6 = QLabel('Geplande start')
                lbl6.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                grid.addWidget(lbl6, 10, 0)  
                grid.addWidget(q6Edit, 10, 1)
                
                lbl7 = QLabel('Werkelijke start')
                lbl7.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                grid.addWidget(lbl7, 11, 0)
                grid.addWidget(q7Edit, 11, 1)
    
                lbl8 = QLabel('Gepland gereed')
                lbl8.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                grid.addWidget(lbl8, 12, 0)
                grid.addWidget(q8Edit, 12, 1)
                
                lbl9 = QLabel('Werkelijk gereed')
                lbl9.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                grid.addWidget(lbl9, 13, 0)
                grid.addWidget(q9Edit, 13, 1)
                
                lbl10 = QLabel('Hoeveelheid goegekeurd')
                lbl10.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                grid.addWidget(lbl10, 14, 0)
                grid.addWidget(q10Edit, 14, 1)
                
                lbl11 = QLabel('Datum goedgekeurd')
                lbl11.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                grid.addWidget(lbl11, 15, 0)
                grid.addWidget(q11Edit, 15, 1)

                lbl12 = QLabel('Stelposten bedrag')
                lbl12.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                grid.addWidget(lbl12, 16, 0)
                grid.addWidget(q12Edit, 16, 1)

                self.setLayout(grid)
                self.setGeometry(600, 150, 150, 150)
        
                applyBtn = QPushButton('Wijzig of volgende regel')
                applyBtn.clicked.connect(self.accept)
                
                grid.addWidget(applyBtn, 16, 2, 1 , 1, Qt.AlignRight)
                applyBtn.setFont(QFont("Arial",10))
                applyBtn.setFixedWidth(200)
                applyBtn.setStyleSheet("color: black;  background-color: gainsboro")

                cancelBtn = QPushButton('Sluiten')
                cancelBtn.clicked.connect(lambda: closeRegels(m_email, minkordernr, mregel, self))
                
                grid.addWidget(cancelBtn, 15, 2, 1, 1, Qt.AlignRight)
                cancelBtn.setFont(QFont("Arial",10))
                cancelBtn.setFixedWidth(200)
                cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
                
                grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 17 , 0, 1, 3, Qt.AlignCenter)
                logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
                                                                         
            def q1Changed(self, text):
                logger.warning(">>> Entering q1Changed(text=%s)", text, extra={"event.action": "q1Changed", "logrite.text": text})
                self.Inkoopordernummer.setText(text)
                logger.debug("<<< Exiting q1Changed(text=%s)", text, extra={"event.action": "q1Changed", "logrite.text": text})
                
            def q2Changed(self,text):
                logger.warning(">>> Entering q2Changed(text=%s)", text, extra={"event.action": "q2Changed", "logrite.text": text})
                self.Werknummer.setText(text)
                logger.debug("<<< Exiting q2Changed(text=%s)", text, extra={"event.action": "q2Changed", "logrite.text": text})
                
            def q3Changed(self,text):
                logger.warning(">>> Entering q3Changed(text=%s)", text, extra={"event.action": "q3Changed", "logrite.text": text})
                self.Werkomschrijving.setText(text)
                logger.debug("<<< Exiting q3Changed(text=%s)", text, extra={"event.action": "q3Changed", "logrite.text": text})
                
            def q4Changed(self,text):
                logger.warning(">>> Entering q4Changed(text=%s)", text, extra={"event.action": "q4Changed", "logrite.text": text})
                self.Omschrijving.setText(text)
                logger.debug("<<< Exiting q4Changed(text=%s)", text, extra={"event.action": "q4Changed", "logrite.text": text})
            
            def q5Changed(self,text):
                logger.warning(">>> Entering q5Changed(text=%s)", text, extra={"event.action": "q5Changed", "logrite.text": text})
                self.Aanneemsom.setText(text)
                logger.debug("<<< Exiting q5Changed(text=%s)", text, extra={"event.action": "q5Changed", "logrite.text": text})
                
            def q6Changed(self,text):
                self.GeplandeStart.setText(text)  
              
            def q7Changed(self,text):
                logger.warning(">>> Entering q7Changed(text=%s)", text, extra={"event.action": "q7Changed", "logrite.text": text})
                self.WerkelijkeStart.setText(text)
                logger.debug("<<< Exiting q7Changed(text=%s)", text, extra={"event.action": "q7Changed", "logrite.text": text})
                
            def q8Changed(self,text):
                logger.warning(">>> Entering q8Changed(text=%s)", text, extra={"event.action": "q8Changed", "logrite.text": text})
                self.GeplandGereed.setText(text)
                logger.debug("<<< Exiting q8Changed(text=%s)", text, extra={"event.action": "q8Changed", "logrite.text": text})
                
            def q9Changed(self,text):
                logger.warning(">>> Entering q9Changed(text=%s)", text, extra={"event.action": "q9Changed", "logrite.text": text})
                self.WerkelijkGereed.setText(text)
                logger.debug("<<< Exiting q9Changed(text=%s)", text, extra={"event.action": "q9Changed", "logrite.text": text})
                
            def q10Changed(self,text):
                logger.warning(">>> Entering q10Changed(text=%s)", text, extra={"event.action": "q10Changed", "logrite.text": text})
                self.BedragAcceptatie.setText(text)
                logger.debug("<<< Exiting q10Changed(text=%s)", text, extra={"event.action": "q10Changed", "logrite.text": text})
                
            def q11Changed(self,text):
                logger.warning(">>> Entering q11Changed(text=%s)", text, extra={"event.action": "q11Changed", "logrite.text": text})
                self.DatumAcceptatie.setText(text)
                logger.debug("<<< Exiting q11Changed(text=%s)", text, extra={"event.action": "q11Changed", "logrite.text": text})

            def returnq1(self):
                logger.warning(">>> Entering returnq1()", extra={"event.action": "returnq1"})
                logger.debug("<<< Exiting returnq1()", extra={"event.action": "returnq1"})
                return self.Inkoopordernummer.text()
            
            def returnq2(self):
                logger.warning(">>> Entering returnq2()", extra={"event.action": "returnq2"})
                logger.debug("<<< Exiting returnq2()", extra={"event.action": "returnq2"})
                return self.Werknummer.text()
            
            def returnq3(self):
                logger.warning(">>> Entering returnq3()", extra={"event.action": "returnq3"})
                logger.debug("<<< Exiting returnq3()", extra={"event.action": "returnq3"})
                return self.Werkomschrijving.text()
            
            def returnq4(self):
                logger.warning(">>> Entering returnq4()", extra={"event.action": "returnq4"})
                logger.debug("<<< Exiting returnq4()", extra={"event.action": "returnq4"})
                return self.Omschrijving.text()
            
            def returnq5(self):
                logger.warning(">>> Entering returnq5()", extra={"event.action": "returnq5"})
                logger.debug("<<< Exiting returnq5()", extra={"event.action": "returnq5"})
                return self.Aanneemsom.text()
            
            def returnq6(self):
                logger.warning(">>> Entering returnq6()", extra={"event.action": "returnq6"})
                logger.debug("<<< Exiting returnq6()", extra={"event.action": "returnq6"})
                return self.GeplandeStart.text()
            
            def returnq7(self):
                logger.warning(">>> Entering returnq7()", extra={"event.action": "returnq7"})
                logger.debug("<<< Exiting returnq7()", extra={"event.action": "returnq7"})
                return self.WerkelijkeStart.text()
            
            def returnq8(self):
                logger.warning(">>> Entering returnq8()", extra={"event.action": "returnq8"})
                logger.debug("<<< Exiting returnq8()", extra={"event.action": "returnq8"})
                return self.GeplandGereed.text()
            
            def returnq9(self):
                logger.warning(">>> Entering returnq9()", extra={"event.action": "returnq9"})
                logger.debug("<<< Exiting returnq9()", extra={"event.action": "returnq9"})
                return self.WerkelijkGereed.text()
            
            def returnq10(self):
                logger.warning(">>> Entering returnq10()", extra={"event.action": "returnq10"})
                logger.debug("<<< Exiting returnq10()", extra={"event.action": "returnq10"})
                return self.BedragAcceptatie.text()
            
            def returnq11(self):
                logger.warning(">>> Entering returnq11()", extra={"event.action": "returnq11"})
                logger.debug("<<< Exiting returnq11()", extra={"event.action": "returnq11"})
                return self.DatumAcceptatie.text()

            @staticmethod
            def getData(parent=None):
                logger.warning(">>> Entering getData(parent=%s)", parent, extra={"event.action": "getData"})
                dialog = Widget(parent)
                dialog.exec_()
                logger.debug("<<< Exiting getData(parent=%s)", parent, extra={"event.action": "getData"})
                return [dialog.returnq1(), dialog.returnq2(), dialog.returnq3(),\
                        dialog.returnq4(), dialog.returnq5(), dialog.returnq6(),\
                        dialog.returnq7(), dialog.returnq8(), dialog.returnq9(),
                        dialog.returnq10(), dialog.returnq11()]
         
        window = Widget()
        data = window.getData()
        mID = row[0]
        mordnr = row[1]
        mwerknr = row[2]
        if data[2]:
            mwerkomschr = data[2]
        else:
            mwerkomschr = row[3]
        if data[3]:
            momschr = data[3]
        else:
            momschr = row[4]
        if data[4]:
            maannsom = float(data[4])
        else:
            maannsom = row[5]
        if data[5]:
            mplstart = data[5]
        else:
            mplstart = row[6]
        if data[6]:
            mwerkstart = data[6]
        else:
            mwerkstart = row[7]
        if data[7]:
            mplgereed = data[7]
        else:
            mplgereed = row[8]
        if data[8]:
            mwerkgereed = data[8]
        else:
            mwerkgereed = row[9]
        macctbedr = float(row[10])
        if data[10]:
            maccptdat = data[10]
        else:
            maccptdat = row[11]


        engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
        conn = engine.connect()
                      
        u = update(orders_inkoop_diensten).where(and_(orders_inkoop_diensten.c.\
           orddienstlevID == mID, orders_inkoop_diensten.c.orderinkoopID == mordnr,\
           orders_inkoop_diensten.c.werknummerID == mwerknr, \
           orders_inkoop_diensten.c.regel == mregel)).values(werkomschr =\
           mwerkomschr, omschrijving = momschr, aanneemsom = maannsom, plan_start = mplstart,\
           plan_gereed = mplgereed, werk_start = mwerkstart, werk_gereed =  mwerkgereed,\
           acceptatie_gereed =  macctbedr, acceptatie_datum = maccptdat)
        
        conn.execute(u)
   
        y = 0
        for x in range(2,11):
            if data[x]:
                y = 1
        if y:
            invoerOK('')
          
    mregel = 0
    dienstenOrder(m_email, minkordernr, mregel)

def insertRegels(m_email, minkordernr, self):
    logger.warning(">>> Entering insertRegels(m_email=%s,minkordernr=%s)", m_email, minkordernr, extra={"event.action": "insertRegels", "logrite.minkordernr": minkordernr})
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("insertRegels(m_email=%s,minkordernr=%s): engine → %s", m_email, minkordernr, engine, extra={"event.action": "insertRegels", "logrite.minkordernr": minkordernr})
    logger.debug("insertRegels(m_email=%s,minkordernr=%s,self=%s): engine → %s", m_email, minkordernr, self, engine, extra={"event.action": "insertRegels", "logrite.minkordernr": minkordernr})
    conn = engine.connect()
    logger.debug("insertRegels(m_email=%s,minkordernr=%s,self=%s): conn → %s", m_email, minkordernr, self, conn, extra={"event.action": "insertRegels", "logrite.minkordernr": minkordernr})

    sel = select([orders_inkoop_diensten]).where(orders_inkoop_diensten.\
                c.orderinkoopID == minkordernr).order_by(orders_inkoop_diensten.c.regel.desc())
    logger.debug("insertRegels(m_email=%s,minkordernr=%s): conn → %s", m_email, minkordernr, conn, extra={"event.action": "insertRegels", "logrite.minkordernr": minkordernr})
    logger.debug("insertRegels(m_email=%s,minkordernr=%s,self=%s): sel → %s", m_email, minkordernr, self, sel, extra={"event.action": "insertRegels", "logrite.minkordernr": minkordernr})
    logger.debug("insertRegels(m_email=%s,minkordernr=%s): sel → %s", m_email, minkordernr, sel, extra={"event.action": "insertRegels", "logrite.minkordernr": minkordernr})
    rpsel = conn.execute(sel).first()
    logger.debug("insertRegels(m_email=%s,minkordernr=%s): rpsel → %s", m_email, minkordernr, rpsel, extra={"event.action": "insertRegels", "logrite.minkordernr": minkordernr})
    logger.debug("insertRegels(m_email=%s,minkordernr=%s,self=%s): rpsel → %s", m_email, minkordernr, self, rpsel, extra={"event.action": "insertRegels", "logrite.minkordernr": minkordernr})

    try:
        midnr = conn.execute(select([func.max(orders_inkoop_diensten.c.orddienstlevID, type_=Integer)])).scalar()
        midnr += 1
    except:
        logger.debug("insertRegels(m_email=%s,minkordernr=%s,self=%s): ins → %s", m_email, minkordernr, self, ins, extra={"event.action": "insertRegels", "logrite.minkordernr": minkordernr})
        midnr = 1
        logger.debug("insertRegels(m_email=%s,minkordernr=%s,self=%s): midnr → %s", m_email, minkordernr, self, midnr, extra={"event.action": "insertRegels", "logrite.minkordernr": minkordernr})
        logger.error("Exception in insertRegels(m_email=%s,minkordernr=%s)", m_email, minkordernr, exc_info=True, extra={"event.action": "insertRegels", "event.category": "process", "logrite.minkordernr": minkordernr})

    mregel = rpsel[13]+1
    logger.debug("insertRegels(m_email=%s,minkordernr=%s,self=%s): mregel → %s", m_email, minkordernr, self, mregel, extra={"event.action": "insertRegels", "logrite.minkordernr": minkordernr})
    ins = insert(orders_inkoop_diensten).values(orddienstlevID = midnr, regel = mregel, orderinkoopID = rpsel[1],\
          werknummerID = rpsel[2], werkomschr = rpsel[3], meerminderwerk = rpsel[12])
    logger.debug("insertRegels(m_email=%s,minkordernr=%s): ins → %s", m_email, minkordernr, ins, extra={"event.action": "insertRegels", "logrite.minkordernr": minkordernr})
    conn.execute(ins)
    message = '\nlinenumber: '+ str(mregel) + ' has been added'
    logger.debug("insertRegels(m_email=%s,minkordernr=%s): message → %s", m_email, minkordernr, message, extra={"event.action": "insertRegels", "logrite.minkordernr": minkordernr})
    logger.debug("insertRegels(m_email=%s,minkordernr=%s,self=%s): message → %s", m_email, minkordernr, self, message, extra={"event.action": "insertRegels", "logrite.minkordernr": minkordernr})
    invoerOK(message)
    logger.debug("<<< Exiting insertRegels(m_email=%s,minkordernr=%s)", m_email, minkordernr, extra={"event.action": "insertRegels", "logrite.minkordernr": minkordernr})
    closeRegels(m_email, rpsel[1], mregel,self)