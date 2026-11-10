from login import hoofdMenu
from bestelOrder import artKeuze
from PyQt5.QtWidgets import QLabel, QLineEdit, QGridLayout, QPushButton,\
                            QDialog, QMessageBox
from PyQt5.QtGui import  QFont, QPixmap, QIcon
from PyQt5.QtCore import Qt
from sqlalchemy import (Table, Column, Integer, String, MetaData,\
                                create_engine)
from sqlalchemy.sql import select
import logging
logger = logging.getLogger(__name__)

def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})

def foutEmail():
    logger.warning(">>> Entering foutEmail()", extra={"event.action": "foutEmail"})
    msg = QMessageBox()
    logger.debug("foutEmail(): msg → %s", msg, extra={"event.action": "foutEmail"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Incorrect e-mail address!')
    msg.setWindowTitle('Incorrect email address')
    logger.debug("<<< Exiting foutEmail()", extra={"event.action": "foutEmail"})
    msg.exec_()

def zoekEmailadres(m_email, klmail):
    logger.warning(">>> Entering zoekEmailadres(m_email=%s,klmail=%s)", m_email, klmail, extra={"event.action": "zoekEmailadres", "logrite.klmail": klmail})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            self.setWindowTitle("Web articles return items.")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
    
            self.Email = QLabel()
            logger.debug("__init__(parent=%s): self.Email → %s", parent, self.Email, extra={"event.action": "__init__"})
            emailEdit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): emailEdit → %s", self, parent, emailEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): emailEdit → %s", parent, emailEdit, extra={"event.action": "__init__"})
            emailEdit.setFixedWidth(220)
            emailEdit.setFont(QFont("Arial",10))
            emailEdit.textChanged.connect(self.emailChanged)
                                        
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
            
            logo = QLabel()
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 1, 1, 1, Qt.AlignRight)
    
            self.setFont(QFont('Arial', 10))
    
            grid.addWidget(QLabel('Email address customer\nor Customer number'), 1, 0)
            grid.addWidget(emailEdit, 1, 1)
           
            applyBtn = QPushButton('Search')
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn, extra={"event.action": "__init__"})
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 2, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro") 

            closeBtn = QPushButton('Close')
            logger.debug("__init__(parent=%s): closeBtn → %s", parent, closeBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): closeBtn → %s", self, parent, closeBtn, extra={"event.action": "__init__"})
            closeBtn.clicked.connect(lambda: windowSluit(self, m_email))
    
            grid.addWidget(closeBtn, 2, 1)
            closeBtn.setFont(QFont("Arial",10))
            closeBtn.setFixedWidth(100) 
            closeBtn.setStyleSheet("color: black;  background-color: gainsboro") 
     
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 3, 0, 1, 3, Qt.AlignCenter)
                  
            self.setLayout(grid)
            self.setGeometry(500, 100, 150, 150)
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
    
        def emailChanged(self, text):
            logger.warning(">>> Entering emailChanged(text=%s)", text, extra={"event.action": "emailChanged", "logrite.text": text})
            self.Email.setText(text)
            logger.debug("<<< Exiting emailChanged(text=%s)", text, extra={"event.action": "emailChanged", "logrite.text": text})
    
        def returnEmail(self):
            logger.warning(">>> Entering returnEmail()", extra={"event.action": "returnEmail"})
            logger.debug("<<< Exiting returnEmail()", extra={"event.action": "returnEmail"})
            return self.Email.text()
    
        @staticmethod
        def getData(parent=None):
            logger.warning(">>> Entering getData(parent=%s)", parent, extra={"event.action": "getData"})
            dialog = Widget(parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog, extra={"event.action": "getData"})
            dialog.exec_()
            logger.debug("<<< Exiting getData(parent=%s)", parent, extra={"event.action": "getData"})
            return [dialog.returnEmail()]
       
    window = Widget()
    data = window.getData()
    metadata = MetaData()
    accounts = Table('accounts', metadata,
        Column('accountID', Integer(), primary_key=True),
        Column('email', String))
  
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    conn = engine.connect()
    
    if data[0] and '@' in data[0]:
        klmail = data[0]
        s = select([accounts]).where(accounts.c.email == klmail)
        rp = conn.execute(s).first()
    elif data[0][0] == '1' and len(data[0]) == 9:
        klantnr = data[0]
        s = select([accounts]).where(accounts.c.accountID == klantnr)
        rp = conn.execute(s).first()
        klmail = rp[1]
    else:
        klmail = '' 
        foutEmail()
        zoekEmailadres(m_email, klmail)
          
    if rp:
        artKeuze(m_email, 1, klmail)
    zoekEmailadres(m_email, klmail)