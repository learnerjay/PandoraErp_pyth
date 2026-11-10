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
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})

def eindProgram():
    logger.warning(">>> Entering eindProgram()", extra={"event.action": "eindProgram"})
    msg = QMessageBox()
    logger.debug("eindProgram(): msg → %s", msg, extra={"event.action": "eindProgram"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Information)
    msg.setText('Programma afgesloten.\nTot ziens!')
    msg.setWindowTitle('BESTELLINGEN')               
    logger.debug("<<< Exiting eindProgram()", extra={"event.action": "eindProgram"})
    msg.exec_() 
    
def invoerOK(mloonnr, momschr):
    logger.warning(">>> Entering invoerOK(mloonnr=%s,momschr=%s)", mloonnr, momschr, extra={"event.action": "invoerOK", "logrite.mloonnr": mloonnr, "logrite.momschr": momschr})
    msg = QMessageBox()
    logger.debug("invoerOK(mloonnr=%s,momschr=%s): msg → %s", mloonnr, momschr, msg, extra={"event.action": "invoerOK", "logrite.mloonnr": mloonnr, "logrite.momschr": momschr})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Information)
    msg.setText('Invoer van loonschaal: '+mloonnr+' '+momschr+' gelukt!')
    msg.setWindowTitle('LOONTABEL')
    logger.debug("<<< Exiting invoerOK(mloonnr=%s,momschr=%s)", mloonnr, momschr, extra={"event.action": "invoerOK", "logrite.mloonnr": mloonnr, "logrite.momschr": momschr})
    msg.exec_()
    
def invoerVerpl():
    logger.warning(">>> Entering invoerVerpl()", extra={"event.action": "invoerVerpl"})
    msg = QMessageBox()
    logger.debug("invoerVerpl(): msg → %s", msg, extra={"event.action": "invoerVerpl"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Invoer alle velden verplicht\nBegin opnieuw met invoeren\nOf beëindig het programma!')
    msg.setWindowTitle('LOONTABEL')
    logger.debug("<<< Exiting invoerVerpl()", extra={"event.action": "invoerVerpl"})
    msg.exec_()

def invoerSchaal(m_email):
    logger.warning(">>> Entering invoerSchaal(m_email=%s)", m_email, extra={"event.action": "invoerSchaal"})
    metadata = MetaData()   
    logger.debug("invoerSchaal(m_email=%s): metadata → %s", m_email, metadata, extra={"event.action": "invoerSchaal"})
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
    logger.debug("invoerSchaal(m_email=%s): engine → %s", m_email, engine, extra={"event.action": "invoerSchaal"})
    con = engine.connect()
    logger.debug("invoerSchaal(m_email=%s): con → %s", m_email, con, extra={"event.action": "invoerSchaal"})
    try:
        mloonnr = (con.execute(select([func.max(lonen.c.loonID,\
                        type_=Integer)])).scalar())
        mloonnr += 1
    except:
        logger.debug("invoerSchaal(m_email=%s): type_ → %s", m_email, type_, extra={"event.action": "invoerSchaal"})
        mloonnr = 1
        logger.debug("invoerSchaal(m_email=%s): mloonnr → %s", m_email, mloonnr, extra={"event.action": "invoerSchaal"})
    mboekd = str(datetime.datetime.now())[0:10] 
    logger.debug("invoerSchaal(m_email=%s): mboekd → %s", m_email, mboekd, extra={"event.action": "invoerSchaal"})
    
    class Widget(QDialog):
        logger.debug("<<< Exiting invoerSchaal(m_email=%s)", m_email, extra={"event.action": "invoerSchaal"})
        def __init__(self):
            logger.warning(">>> Entering __init__()", extra={"event.action": "__init__"})
            QDialog.__init__(self)
            
            grid = QGridLayout()
            logger.debug("__init__(): grid → %s", grid, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): grid → %s", self, grid, extra={"event.action": "__init__"})
            grid.setSpacing(12)
            
            self.setWindowTitle("Invoeren Loontabel")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
            
            self.setFont(QFont('Arial', 10))   
                                              
            self.lbl = QLabel()
            logger.debug("__init__(): self.lbl → %s", self.lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl → %s", self, lbl, extra={"event.action": "__init__"})
            self.pixmap = QPixmap('./images/logos/verbinding.jpg')
            logger.debug("__init__(): self.pixmap → %s", self.pixmap, extra={"event.action": "__init__"})
            self.lbl.setPixmap(self.pixmap)
            grid.addWidget(self.lbl , 0, 0)
            
            self.logo = QLabel()
            logger.debug("__init__(): self.logo → %s", self.logo, extra={"event.action": "__init__"})
            self.pixmap = QPixmap('./images/logos/logo.jpg')
            self.logo.setPixmap(self.pixmap)
            logger.debug("__init__(self=%s): logo → %s", self, logo, extra={"event.action": "__init__"})
            grid.addWidget(self.logo , 0, 1, 1, 2, Qt.AlignRight) 
            
            grid.addWidget(QLabel('        Invoeren Loonschalen'), 0, 0, 1, 3, Qt.AlignCenter)
                
            self.Loontabelnummer = QLabel()
            logger.debug("__init__(): self.Loontabelnummer → %s", self.Loontabelnummer, extra={"event.action": "__init__"})
            q1Edit = QLineEdit(str(mloonnr))
            logger.debug("__init__(self=%s): q1Edit → %s", self, q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): q1Edit → %s", q1Edit, extra={"event.action": "__init__"})
            q1Edit.setAlignment(Qt.AlignRight)
            q1Edit.setStyleSheet("color: black")
            q1Edit.setFixedWidth(100)
            q1Edit.setDisabled(True)
            q1Edit.setFont(QFont("Arial",10))
         
            self.Omschrijving = QLabel()
            logger.debug("__init__(): self.Omschrijving → %s", self.Omschrijving, extra={"event.action": "__init__"})
            q2Edit = QLineEdit()
            logger.debug("__init__(self=%s): q2Edit → %s", self, q2Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): q2Edit → %s", q2Edit, extra={"event.action": "__init__"})
            q2Edit.setFixedWidth(320)
            q2Edit.setFont(QFont("Arial",10))
            q2Edit.textChanged.connect(self.q2Changed)
            
            self.Maandloon = QLabel()
            logger.debug("__init__(): self.Maandloon → %s", self.Maandloon, extra={"event.action": "__init__"})
            q3Edit = QLineEdit()
            logger.debug("__init__(self=%s): q3Edit → %s", self, q3Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): q3Edit → %s", q3Edit, extra={"event.action": "__init__"})
            q3Edit.setFixedWidth(100)
            q3Edit.setFont(QFont("Arial",10))
            q3Edit.textChanged.connect(self.q3Changed)
            reg_ex = QRegExp("^[0-9]*\\.?[0-9]+$")
            logger.debug("__init__(): reg_ex → %s", reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): reg_ex → %s", self, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Tabelloon → %s", self.Tabelloon, extra={"event.action": "__init__"})
            logger.debug("__init__(): q4Edit → %s", q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q4Edit → %s", self, q4Edit, extra={"event.action": "__init__"})
            input_validator = QRegExpValidator(reg_ex, q3Edit)
            logger.debug("__init__(self=%s): input_validator → %s", self, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(): input_validator → %s", input_validator, extra={"event.action": "__init__"})
            q3Edit.setValidator(input_validator)
                                       
            self.Tabelloon = QLabel()
            q4Edit = QLineEdit()
            q4Edit.setFixedWidth(100)
            q4Edit.setFont(QFont("Arial",10))
            q4Edit.textChanged.connect(self.q4Changed)
            reg_ex = QRegExp("^[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q4Edit)
            q4Edit.setValidator(input_validator)

            self.Reisuurloon = QLabel()
            logger.debug("__init__(): self.Reisuurloon → %s", self.Reisuurloon, extra={"event.action": "__init__"})
            q6Edit = QLineEdit()
            logger.debug("__init__(self=%s): q6Edit → %s", self, q6Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): q6Edit → %s", q6Edit, extra={"event.action": "__init__"})
            q6Edit.setFixedWidth(100)
            q6Edit.setFont(QFont("Arial",10))
            q6Edit.textChanged.connect(self.q6Changed)
            reg_ex = QRegExp("^[0-9]*\\.?[0-9]+$")
            input_validator = QRegExpValidator(reg_ex, q6Edit)
            q6Edit.setValidator(input_validator)
       
            lbl1 = QLabel('Loontabelnummer')
            logger.debug("__init__(): lbl1 → %s", lbl1, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl1 → %s", self, lbl1, extra={"event.action": "__init__"})
            grid.addWidget(lbl1, 1, 0)
            grid.addWidget(q1Edit, 1, 1)
            
            lbl2 = QLabel('Functieomschrijving')
            logger.debug("__init__(): lbl2 → %s", lbl2, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl2 → %s", self, lbl2, extra={"event.action": "__init__"})
            grid.addWidget(lbl2, 2, 0)
            grid.addWidget(q2Edit, 2, 1, 1, 2)
            
            lbl3 = QLabel('Maandloon')
            logger.debug("__init__(): lbl3 → %s", lbl3, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl3 → %s", self, lbl3, extra={"event.action": "__init__"})
            grid.addWidget(lbl3, 3, 0)
            grid.addWidget(q3Edit, 3, 1)
                      
            lbl5 = QLabel('Tabeluurloon')
            logger.debug("__init__(): lbl5 → %s", lbl5, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl5 → %s", self, lbl5, extra={"event.action": "__init__"})
            grid.addWidget(lbl5, 4, 0)
            grid.addWidget(q4Edit, 4, 1)
           
            lbl7 = QLabel('Reisuurloon')
            logger.debug("__init__(): lbl7 → %s", lbl7, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl7 → %s", self, lbl7, extra={"event.action": "__init__"})
            grid.addWidget(lbl7, 5, 0)
            grid.addWidget(q6Edit, 5, 1)
            
            lbl8 = QLabel('Wijzigingsdatum')
            logger.debug("__init__(): lbl8 → %s", lbl8, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl8 → %s", self, lbl8, extra={"event.action": "__init__"})
            lbl9 = QLabel(mboekd)
            logger.debug("__init__(self=%s): lbl9 → %s", self, lbl9, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl9 → %s", lbl9, extra={"event.action": "__init__"})
            grid.addWidget(lbl8, 6 ,0)
            grid.addWidget(lbl9, 6, 1)
       
            wijzig = QPushButton('Invoer')
            logger.debug("__init__(): wijzig → %s", wijzig, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): wijzig → %s", self, wijzig, extra={"event.action": "__init__"})
            wijzig.clicked.connect(self.accept)
    
            grid.addWidget(wijzig, 7, 1, 1 , 2, Qt.AlignRight)
            wijzig.setFont(QFont("Arial",10))
            wijzig.setFixedWidth(100)  
            
            sluit = QPushButton('Sluit')
            logger.debug("__init__(): sluit → %s", sluit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): sluit → %s", self, sluit, extra={"event.action": "__init__"})
            sluit.clicked.connect(lambda: windowSluit(self, m_email))
    
            grid.addWidget(sluit, 7, 1, 1, 2, Qt.AlignCenter)
            sluit.setFont(QFont("Arial",10))
            sluit.setFixedWidth(100)  
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 8, 0, 1, 3, Qt.AlignCenter)
                                                                    
            self.setLayout(grid)
            self.setGeometry(100, 50, 150, 150)
            logger.debug("<<< Exiting __init__()", extra={"event.action": "__init__"})
            
        def q2Changed(self,text):
            logger.warning(">>> Entering q2Changed(text=%s)", text, extra={"event.action": "q2Changed", "logrite.text": text})
            self.Omschrijving.setText(text)
            logger.debug("<<< Exiting q2Changed(text=%s)", text, extra={"event.action": "q2Changed", "logrite.text": text})
    
        def q3Changed(self,text):
            logger.warning(">>> Entering q3Changed(text=%s)", text, extra={"event.action": "q3Changed", "logrite.text": text})
            self.Maandloon.setText(text)
            logger.debug("<<< Exiting q3Changed(text=%s)", text, extra={"event.action": "q3Changed", "logrite.text": text})
    
        def q4Changed(self,text):
            logger.warning(">>> Entering q4Changed(text=%s)", text, extra={"event.action": "q4Changed", "logrite.text": text})
            self.Tabelloon.setText(text)
            logger.debug("<<< Exiting q4Changed(text=%s)", text, extra={"event.action": "q4Changed", "logrite.text": text})
                        
        def q6Changed(self,text):
            logger.warning(">>> Entering q6Changed(text=%s)", text, extra={"event.action": "q6Changed", "logrite.text": text})
            self.Reisuurloon.setText(text)
            logger.debug("<<< Exiting q6Changed(text=%s)", text, extra={"event.action": "q6Changed", "logrite.text": text})
      
        def returnq2(self):
            logger.warning(">>> Entering returnq2()", extra={"event.action": "returnq2"})
            logger.debug("<<< Exiting returnq2()", extra={"event.action": "returnq2"})
            return self.Omschrijving.text()
        
        def returnq3(self):
            logger.warning(">>> Entering returnq3()", extra={"event.action": "returnq3"})
            logger.debug("<<< Exiting returnq3()", extra={"event.action": "returnq3"})
            return self.Maandloon.text()
        
        def returnq4(self):
            logger.warning(">>> Entering returnq4()", extra={"event.action": "returnq4"})
            logger.debug("<<< Exiting returnq4()", extra={"event.action": "returnq4"})
            return self.Tabelloon.text()
       
        def returnq6(self):
            logger.warning(">>> Entering returnq6()", extra={"event.action": "returnq6"})
            logger.debug("<<< Exiting returnq6()", extra={"event.action": "returnq6"})
            return self.Reisuurloon.text()
        
        @staticmethod
        def getData(parent=None):
            logger.warning(">>> Entering getData(parent=%s)", parent, extra={"event.action": "getData"})
            dialog = Widget()
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog, extra={"event.action": "getData"})
            dialog.exec_()
            logger.debug("<<< Exiting getData(parent=%s)", parent, extra={"event.action": "getData"})
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
