from login import hoofdMenu
import  datetime
from PyQt5.QtWidgets import QLabel, QLineEdit, QGridLayout, QPushButton,\
     QDialog, QMessageBox
from PyQt5.QtGui import QFont, QIcon, QRegExpValidator, QPixmap
from PyQt5.QtCore import Qt,  QRegExp
from sqlalchemy import (Table, Column, Integer, String, Float, Boolean,\
                        MetaData, create_engine)
from sqlalchemy.sql import select, insert, func
import logging
logger = logging.getLogger(__name__)

def windowSluit(self, m_email):
    logger.debug(">>> Entering windowSluit(m_email=%s)", m_email)
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email)

def eindProgram():
    logger.debug(">>> Entering eindProgram()")
    msg = QMessageBox()
    logger.debug("eindProgram(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Information)
    msg.setText('Program closed.\nGoodbye!')
    msg.setWindowTitle('Orders')
    logger.debug("<<< Exiting eindProgram()")
    msg.exec_() 
    
def invoerOK(mloonnr, momschr):
    logger.debug(">>> Entering invoerOK(mloonnr=%s,momschr=%s)", mloonnr, momschr)
    msg = QMessageBox()
    logger.debug("invoerOK(mloonnr=%s,momschr=%s): msg → %s", mloonnr, momschr, msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Information)
    msg.setText('Insert of pay scale: '+mloonnr+' '+momschr+' successful!')
    msg.setWindowTitle('Pay scale')
    logger.debug("<<< Exiting invoerOK(mloonnr=%s,momschr=%s)", mloonnr, momschr)
    msg.exec_()
    
def invoerVerpl():
    logger.debug(">>> Entering invoerVerpl()")
    msg = QMessageBox()
    logger.debug("invoerVerpl(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Input all fields required\nStart again with enter\nOr end the program!')
    msg.setWindowTitle('Pay scale')
    logger.debug("<<< Exiting invoerVerpl()")
    msg.exec_()

def invoerSchaal(m_email):
    logger.debug(">>> Entering invoerSchaal(m_email=%s)", m_email)
    metadata = MetaData()   
    logger.debug("invoerSchaal(m_email=%s): metadata → %s", m_email, metadata)
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
    logger.debug("invoerSchaal(m_email=%s): engine → %s", m_email, engine)
    con = engine.connect()
    try:
        logger.debug("invoerSchaal(m_email=%s): con → %s", m_email, con)
        mloonnr = (con.execute(select([func.max(lonen.c.loonID,\
                        type_=Integer)])).scalar())
        mloonnr += 1
        logger.debug("invoerSchaal(m_email=%s): mloonnr → %s", m_email, mloonnr)
        logger.debug("invoerSchaal(m_email=%s): type_ → %s", m_email, type_)
    except:
        mloonnr = 1
    mboekd = str(datetime.datetime.now())[0:10] 
    
    logger.debug("invoerSchaal(m_email=%s): mboekd → %s", m_email, mboekd)
    class Widget(QDialog):
        logger.debug("<<< Exiting invoerSchaal(m_email=%s)", m_email)
        def __init__(self):
            logger.debug(">>> Entering __init__()")
            QDialog.__init__(self)
            
            grid = QGridLayout()
            logger.debug("__init__(self=%s): grid → %s", self, grid)
            logger.debug("__init__(): grid → %s", grid)
            grid.setSpacing(12)
            
            self.setWindowTitle("Input wage table")
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
            
            logger.debug("__init__(): input_validator → %s", input_validator)
            grid.addWidget(QLabel('        Entering pay scales'), 0, 0, 1, 3, Qt.AlignCenter)
                
            self.Loontabelnummer = QLabel()
            logger.debug("__init__(): self.Loontabelnummer → %s", self.Loontabelnummer)
            q1Edit = QLineEdit(str(mloonnr))
            logger.debug("__init__(self=%s): q1Edit → %s", self, q1Edit)
            logger.debug("__init__(): q1Edit → %s", q1Edit)
            q1Edit.setAlignment(Qt.AlignRight)
            q1Edit.setStyleSheet("color: black")
            q1Edit.setFixedWidth(100)
            q1Edit.setDisabled(True)
            q1Edit.setFont(QFont("Arial",10))
         
            self.Omschrijving = QLabel()
            logger.debug("__init__(): self.Omschrijving → %s", self.Omschrijving)
            q2Edit = QLineEdit()
            logger.debug("__init__(self=%s): q2Edit → %s", self, q2Edit)
            logger.debug("__init__(): q2Edit → %s", q2Edit)
            q2Edit.setFixedWidth(320)
            q2Edit.setFont(QFont("Arial",10))
            q2Edit.textChanged.connect(self.q2Changed)
            
            self.Maandloon = QLabel()
            logger.debug("__init__(): self.Maandloon → %s", self.Maandloon)
            q3Edit = QLineEdit()
            logger.debug("__init__(self=%s): q3Edit → %s", self, q3Edit)
            logger.debug("__init__(): q3Edit → %s", q3Edit)
            q3Edit.setFixedWidth(100)
            q3Edit.setFont(QFont("Arial",10))
            q3Edit.textChanged.connect(self.q3Changed)
            reg_ex = QRegExp("^[0-9]*\\.?[0-9]+$")
            logger.debug("__init__(self=%s): reg_ex → %s", self, reg_ex)
            logger.debug("__init__(): reg_ex → %s", reg_ex)
            input_validator = QRegExpValidator(reg_ex, q3Edit)
            logger.debug("__init__(self=%s): input_validator → %s", self, input_validator)
            q3Edit.setValidator(input_validator)
                                       
            self.Tabelloon = QLabel()
            logger.debug("__init__(): self.Tabelloon → %s", self.Tabelloon)
            q4Edit = QLineEdit()
            logger.debug("__init__(self=%s): q4Edit → %s", self, q4Edit)
            logger.debug("__init__(): q4Edit → %s", q4Edit)
            q4Edit.setFixedWidth(100)
            q4Edit.setFont(QFont("Arial",10))
            q4Edit.textChanged.connect(self.q4Changed)
            reg_ex = QRegExp("^[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q4Edit)
            q4Edit.setValidator(input_validator)

            self.Reisuurloon = QLabel()
            logger.debug("__init__(): self.Reisuurloon → %s", self.Reisuurloon)
            q6Edit = QLineEdit()
            logger.debug("__init__(self=%s): q6Edit → %s", self, q6Edit)
            logger.debug("__init__(): q6Edit → %s", q6Edit)
            q6Edit.setFixedWidth(100)
            q6Edit.setFont(QFont("Arial",10))
            q6Edit.textChanged.connect(self.q6Changed)
            reg_ex = QRegExp("^[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q6Edit)
            q6Edit.setValidator(input_validator)
       
            lbl1 = QLabel('Wage table number')
            logger.debug("__init__(self=%s): lbl1 → %s", self, lbl1)
            logger.debug("__init__(): lbl1 → %s", lbl1)
            grid.addWidget(lbl1, 1, 0)
            grid.addWidget(q1Edit, 1, 1)
            
            lbl2 = QLabel('Job description')
            logger.debug("__init__(self=%s): lbl2 → %s", self, lbl2)
            logger.debug("__init__(): lbl2 → %s", lbl2)
            grid.addWidget(lbl2, 2, 0)
            grid.addWidget(q2Edit, 2, 1, 1, 2)
            
            lbl3 = QLabel('Monthly salary')
            logger.debug("__init__(self=%s): lbl3 → %s", self, lbl3)
            logger.debug("__init__(): lbl3 → %s", lbl3)
            grid.addWidget(lbl3, 3, 0)
            grid.addWidget(q3Edit, 3, 1)
                      
            lbl5 = QLabel('Tabular wages')
            logger.debug("__init__(self=%s): lbl5 → %s", self, lbl5)
            logger.debug("__init__(): lbl5 → %s", lbl5)
            grid.addWidget(lbl5, 4, 0)
            grid.addWidget(q4Edit, 4, 1)
           
            lbl7 = QLabel('Travel hourly wage')
            logger.debug("__init__(self=%s): lbl7 → %s", self, lbl7)
            logger.debug("__init__(): lbl7 → %s", lbl7)
            grid.addWidget(lbl7, 5, 0)
            grid.addWidget(q6Edit, 5, 1)
            
            lbl8 = QLabel('Modification date')
            logger.debug("__init__(self=%s): lbl8 → %s", self, lbl8)
            logger.debug("__init__(): lbl8 → %s", lbl8)
            lbl9 = QLabel(mboekd)
            logger.debug("__init__(self=%s): lbl9 → %s", self, lbl9)
            logger.debug("__init__(): lbl9 → %s", lbl9)
            grid.addWidget(lbl8, 6 ,0)
            grid.addWidget(lbl9, 6, 1)
       
            wijzig = QPushButton('Insert')
            logger.debug("__init__(self=%s): wijzig → %s", self, wijzig)
            logger.debug("__init__(): wijzig → %s", wijzig)
            wijzig.clicked.connect(self.accept)
    
            grid.addWidget(wijzig, 7, 1, 1 , 2, Qt.AlignRight)
            wijzig.setFont(QFont("Arial",10))
            wijzig.setFixedWidth(100)  
            
            sluit = QPushButton('Close')
            logger.debug("__init__(self=%s): sluit → %s", self, sluit)
            logger.debug("__init__(): sluit → %s", sluit)
            sluit.clicked.connect(lambda: windowSluit(self, m_email))
    
            grid.addWidget(sluit, 7, 1, 1, 2, Qt.AlignCenter)
            sluit.setFont(QFont("Arial",10))
            sluit.setFixedWidth(100)  
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 8, 0, 1, 3, Qt.AlignCenter)
                                                                    
            self.setLayout(grid)
            self.setGeometry(100, 50, 150, 150)
            logger.debug("<<< Exiting __init__()")
            
        def q2Changed(self,text):
            logger.debug(">>> Entering q2Changed(text=%s)", text)
            logger.debug("q2Changed(self=%s,text=%s): Omschrijving → %s", self, text, Omschrijving)
            self.Omschrijving.setText(text)
            logger.debug("<<< Exiting q2Changed(text=%s)", text)
    
        def q3Changed(self,text):
            logger.debug(">>> Entering q3Changed(text=%s)", text)
            logger.debug("q3Changed(self=%s,text=%s): Maandloon → %s", self, text, Maandloon)
            self.Maandloon.setText(text)
            logger.debug("<<< Exiting q3Changed(text=%s)", text)
    
        def q4Changed(self,text):
            logger.debug(">>> Entering q4Changed(text=%s)", text)
            logger.debug("q4Changed(self=%s,text=%s): Tabelloon → %s", self, text, Tabelloon)
            self.Tabelloon.setText(text)
            logger.debug("<<< Exiting q4Changed(text=%s)", text)
                        
        def q6Changed(self,text):
            logger.debug(">>> Entering q6Changed(text=%s)", text)
            logger.debug("q6Changed(self=%s,text=%s): Reisuurloon → %s", self, text, Reisuurloon)
            self.Reisuurloon.setText(text)
            logger.debug("<<< Exiting q6Changed(text=%s)", text)
      
        def returnq2(self):
            logger.debug(">>> Entering returnq2()")
            logger.debug("<<< Exiting returnq2()")
            return self.Omschrijving.text()
        
        def returnq3(self):
            logger.debug(">>> Entering returnq3()")
            logger.debug("<<< Exiting returnq3()")
            return self.Maandloon.text()
        
        def returnq4(self):
            logger.debug(">>> Entering returnq4()")
            logger.debug("<<< Exiting returnq4()")
            return self.Tabelloon.text()
       
        def returnq6(self):
            logger.debug(">>> Entering returnq6()")
            logger.debug("<<< Exiting returnq6()")
            return self.Reisuurloon.text()
        
        @staticmethod
        def getData(parent=None):
            logger.debug(">>> Entering getData(parent=%s)", parent)
            dialog = Widget()
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog)
            dialog.exec_()
            logger.debug("<<< Exiting getData(parent=%s)", parent)
            return [dialog.returnq2(), dialog.returnq3(), dialog.returnq4(),\
                    dialog.returnq6()]  
                    
    window = Widget()
    data = window.getData()
    
    if data[0]:
        momschr = data[0]
    else:
        invoerVerpl()
        return
    if data[1]:
        mmndloon = float(data[1])
    else:
        invoerVerpl()
        return
    if data[2]:
        mtabelloon = float(data[2])
    else:
        invoerVerpl()
        return
    if data[3]:
        mreisuurloon = float(data[3])
    else:
        invoerVerpl()
        return
    
    inslon = insert(lonen).values(loonID = mloonnr,functieomschr=momschr,\
            maandloon = mmndloon, tabelloon = mtabelloon,\
            reisuur=mreisuurloon, boekdatum = mboekd)
    con.execute(inslon)
    invoerOK(str(mloonnr), momschr)
