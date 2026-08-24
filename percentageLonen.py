import datetime
from login import hoofdMenu
from PyQt5.QtWidgets import QLabel, QLineEdit, QGridLayout, QPushButton,\
      QDialog, QMessageBox
from PyQt5.QtGui import QFont, QIcon, QRegExpValidator, QPixmap
from PyQt5.QtCore import Qt,  QRegExp
from sqlalchemy import (Table, Column, Integer, String, Float, Boolean,\
                        MetaData, create_engine)
from sqlalchemy.sql import select, update
import logging
logger = logging.getLogger(__name__)
   
def eindModule(self,m_email):
    logger.debug(">>> Entering eindModule(m_email=%s)", m_email)
    msg = QMessageBox()
    logger.debug("eindModule(m_email=%s): msg → %s", m_email, msg)
    logger.debug("eindModule(self=%s,m_email=%s): msg → %s", self, m_email, msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Information)
    msg.setText('Input aborted.')
    msg.setWindowTitle('Wages')
    msg.exec_()
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting eindModule(m_email=%s)", m_email)
    
def invoerOK(m_email):
    logger.debug(">>> Entering invoerOK(m_email=%s)", m_email)
    msg = QMessageBox()
    logger.debug("invoerOK(m_email=%s): msg → %s", m_email, msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Information)
    msg.setText('Input successful!')
    msg.setWindowTitle('Wages')
    msg.exec_()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting invoerOK(m_email=%s)", m_email)
    
def invoerVerpl():
    logger.debug(">>> Entering invoerVerpl()")
    msg = QMessageBox()
    logger.debug("invoerVerpl(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Input required\nor close the program!')
    msg.setWindowTitle('Wage table')
    logger.debug("<<< Exiting invoerVerpl()")
    msg.exec_()

def percLoonschaal(m_email):
    logger.debug(">>> Entering percLoonschaal(m_email=%s)", m_email)
    class Widget(QDialog):
        def __init__(self):
            logger.debug(">>> Entering __init__()")
            QDialog.__init__(self)
            
            grid = QGridLayout()
            logger.debug("__init__(self=%s): grid → %s", self, grid)
            logger.debug("__init__(): grid → %s", grid)
            grid.setSpacing(12)
            
            self.setWindowTitle("Percentage adjustment of wages")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
            
            self.setFont(QFont('Arial', 10))   
                                              
            self.lbl = QLabel()
            logger.debug("__init__(): self.lbl → %s", self.lbl)
            logger.debug("__init__(self=%s): lbl → %s", self, lbl)
            self.pixmap = QPixmap('./images/logos/verbinding.jpg')
            logger.debug("__init__(): self.pixmap → %s", self.pixmap)
            self.lbl.setPixmap(self.pixmap)
            grid.addWidget(self.lbl , 0, 0)
            
            self.logo = QLabel()
            logger.debug("__init__(): self.logo → %s", self.logo)
            self.pixmap = QPixmap('./images/logos/logo.jpg')
            self.logo.setPixmap(self.pixmap)
            logger.debug("__init__(self=%s): logo → %s", self, logo)
            grid.addWidget(self.logo , 0, 1, 1, 2, Qt.AlignRight) 
            
            grid.addWidget(QLabel('     Adjust wages in percentage terms'), 1, 0, 1, 3, Qt.AlignCenter)
            logger.debug("__init__(): input_validator → %s", input_validator)
                
            self.Percentage = QLabel()
            logger.debug("__init__(): self.Percentage → %s", self.Percentage)
            q1Edit = QLineEdit()
            logger.debug("__init__(self=%s): q1Edit → %s", self, q1Edit)
            logger.debug("__init__(): q1Edit → %s", q1Edit)
            q1Edit.setFixedWidth(100)
            q1Edit.setFont(QFont("Arial",10))
            q1Edit.textChanged.connect(self.q1Changed)
            reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
            logger.debug("__init__(self=%s): reg_ex → %s", self, reg_ex)
            logger.debug("__init__(): reg_ex → %s", reg_ex)
            input_validator = QRegExpValidator(reg_ex, q1Edit)
            logger.debug("__init__(self=%s): input_validator → %s", self, input_validator)
            q1Edit.setValidator(input_validator)
                          
            lbl1 = QLabel('Percentage increase')
            logger.debug("__init__(self=%s): lbl1 → %s", self, lbl1)
            logger.debug("__init__(): lbl1 → %s", lbl1)
            grid.addWidget(lbl1, 2, 0, 1, 2, Qt.AlignRight)
            grid.addWidget(q1Edit, 2, 2)
                 
            wijzig = QPushButton('Modify')
            logger.debug("__init__(self=%s): wijzig → %s", self, wijzig)
            logger.debug("__init__(): wijzig → %s", wijzig)
            wijzig.clicked.connect(self.accept)
    
            grid.addWidget(wijzig, 3, 1, 1 , 2, Qt.AlignRight)
            wijzig.setFont(QFont("Arial",10))           
            wijzig.setStyleSheet("color: black;  background-color: gainsboro; selection-background-color: gainsboro; selection-color: black")
            wijzig.setFixedWidth(100)  
            
            sluit = QPushButton('Close')
            logger.debug("__init__(self=%s): sluit → %s", self, sluit)
            logger.debug("__init__(): sluit → %s", sluit)
            sluit.clicked.connect(lambda: eindModule(self, m_email))
    
            grid.addWidget(sluit, 3, 0, 1 , 2, Qt.AlignRight)
            sluit.setFont(QFont("Arial",10))
            sluit.setStyleSheet("color: black;  background-color: gainsboro; selection-background-color: gainsboro; selection-color: black")
            sluit.setFixedWidth(100)  
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 4, 0, 1, 3, Qt.AlignCenter)
                                                                    
            self.setLayout(grid)
            self.setGeometry(100, 50, 150, 150)
            logger.debug("<<< Exiting __init__()")
            
        def q1Changed(self,text):
            logger.debug(">>> Entering q1Changed(text=%s)", text)
            logger.debug("q1Changed(self=%s,text=%s): Percentage → %s", self, text, Percentage)
            self.Percentage.setText(text)
            logger.debug("<<< Exiting q1Changed(text=%s)", text)
    
        def returnq1(self):
            logger.debug(">>> Entering returnq1()")
            logger.debug("<<< Exiting returnq1()")
            return self.Percentage.text()
     
        @staticmethod
        def getData(parent=None):
            logger.debug(">>> Entering getData(parent=%s)", parent)
            dialog = Widget()
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog)
            dialog.exec_()
            logger.debug("<<< Exiting getData(parent=%s)", parent)
            return [dialog.returnq1()]  
                    
    window = Widget()
    data = window.getData()
    
    if data[0]:
        mperc = float(data[0])
    else:
        invoerVerpl()
        return
    
    metadata = MetaData()   
    lonen = Table('lonen', metadata,
       Column('loonID', Integer(), primary_key=True),
       Column('tabelloon', Float),
       Column('werkuur',Float),
       Column('reisuur', Float),
       Column('direct', Boolean),
       Column('maandloon', Float),
       Column('functieomschr', String),
       Column('boekdatum', String))
                   
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
    sellon = select([lonen])
    rplon = con.execute(sellon)
      
    mboekd = str(datetime.datetime.now())[0:10] 
    for row in rplon:
        updlon = update(lonen).where(lonen.c.loonID==row[0]).values(maandloon = row[5]*1+mperc/100, tabelloon = row[1]*1+mperc/100,\
                werkuur =row[2]*1+mperc/100, reisuur = row[3]*1+mperc/100, boekdatum = mboekd)
        con.execute(updlon)
    invoerOK(m_email)