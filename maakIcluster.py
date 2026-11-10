from login import hoofdMenu
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QDialog, QLabel,\
         QGridLayout, QPushButton, QMessageBox, QComboBox
from sqlalchemy import (Table, Column, String, Integer, MetaData, create_engine, insert, select)
import logging
logger = logging.getLogger(__name__)

def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    
def insGelukt(mclusternr, momschr, m_email):
    logger.warning(">>> Entering insGelukt(mclusternr=%s,momschr=%s,m_email=%s)", mclusternr, momschr, m_email, extra={"event.action": "insGelukt", "logrite.mclusternr": mclusternr, "logrite.momschr": momschr})
    msg = QMessageBox()
    logger.debug("insGelukt(mclusternr=%s,momschr=%s,m_email=%s): msg → %s", mclusternr, momschr, m_email, msg, extra={"event.action": "insGelukt", "logrite.mclusternr": mclusternr, "logrite.momschr": momschr})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Information)
    msg.setText('Cluster number: '+mclusternr+'\n"'+momschr+'" is created')
    msg.setFont(QFont("Arial",10))
    msg.setWindowTitle('Create clusters')
    logger.debug("<<< Exiting insGelukt(mclusternr=%s,momschr=%s,m_email=%s)", mclusternr, momschr, m_email, extra={"event.action": "insGelukt", "logrite.mclusternr": mclusternr, "logrite.momschr": momschr})
    msg.exec_()

def insMislukt(mclusternr, momschr, m_email):
    logger.warning(">>> Entering insMislukt(mclusternr=%s,momschr=%s,m_email=%s)", mclusternr, momschr, m_email, extra={"event.action": "insMislukt", "logrite.mclusternr": mclusternr, "logrite.momschr": momschr})
    msg = QMessageBox()
    logger.debug("insMislukt(mclusternr=%s,momschr=%s,m_email=%s): msg → %s", mclusternr, momschr, m_email, msg, extra={"event.action": "insMislukt", "logrite.mclusternr": mclusternr, "logrite.momschr": momschr})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Critical)
    msg.setText('Creation of cluster '+mclusternr+'\n"'+momschr+'" has failed!\nCluster number already exist!')
    msg.setFont(QFont("Arial",10))
    msg.setWindowTitle('Create clusters')
    logger.debug("<<< Exiting insMislukt(mclusternr=%s,momschr=%s,m_email=%s)", mclusternr, momschr, m_email, extra={"event.action": "insMislukt", "logrite.mclusternr": mclusternr, "logrite.momschr": momschr})
    msg.exec_()

def ongKeuze():
    logger.warning(">>> Entering ongKeuze()", extra={"event.action": "ongKeuze"})
    msg = QMessageBox()
    logger.debug("ongKeuze(): msg → %s", msg, extra={"event.action": "ongKeuze"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Invalid choice')
    msg.setFont(QFont("Arial",10))
    msg.setWindowTitle('Insert clusters')
    logger.debug("<<< Exiting ongKeuze()", extra={"event.action": "ongKeuze"})
    msg.exec_()

metadata = MetaData()
cluster_structure_internal = Table('cluster_structure_internal', metadata,
    Column('structID', Integer() , primary_key =True),
    Column('overall_heading', String),
    Column('heading_level1', String),
    Column('line_level0', String),
    Column('line1', String),
    Column('line2', String),
    Column('line3', String),
    Column('line4', String),
    Column('line5', String),
    Column('line6', String),
    Column('line7', String),
    Column('line8', String),
    Column('line9', String),
    Column('line10', String),
    Column('line11', String),
    Column('line12', String),
    Column('line13', String),
    Column('line14', String),
    Column('line15', String))

engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
con = engine.connect()
sel = select([cluster_structure_internal]).order_by(cluster_structure_internal.c.line_level0)
rpa = con.execute(sel).fetchall()

def kiesCluster(m_email):
    logger.warning(">>> Entering kiesCluster(m_email=%s)", m_email, extra={"event.action": "kiesCluster"})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle("Cluster selection")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
                              
            self.Keuze = QLabel()
            k0Edit = QComboBox()
            k0Edit.setFixedWidth(320)
            k0Edit.setFont(QFont("Arial",10))
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.addItem(rpa[0][1])
            k0Edit.addItem(rpa[0][3])
            k0Edit.addItem(rpa[1][3])
            k0Edit.addItem(rpa[2][3])
            k0Edit.addItem(rpa[3][3])
            k0Edit.addItem(rpa[4][3])
            k0Edit.addItem(rpa[5][3])
            k0Edit.addItem(rpa[6][3])
            k0Edit.addItem(rpa[7][3])
            k0Edit.activated[str].connect(self.k0Changed)
 
            grid = QGridLayout()
            grid.setSpacing(20)
                          
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 0, 0, 1, 2)
                        
            grid.addWidget(k0Edit, 1, 1)
            
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 3, 0, 1, 2, Qt.AlignCenter)
            
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 1, 1, 1, Qt.AlignRight)
   
            applyBtn = QPushButton('Subgroup')
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 2, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Close')
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
    
            grid.addWidget(cancelBtn, 2, 1, 1, 1, Qt.AlignCenter)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.Keuze → %s", parent, self.Keuze, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): k0Edit → %s", parent, k0Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): k0Edit → %s", self, parent, k0Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): grid → %s", parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl → %s", parent, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
           
        def k0Changed(self, text):
            logger.warning(">>> Entering k0Changed(text=%s)", text, extra={"event.action": "k0Changed", "logrite.text": text})
            self.Keuze.setText(text)
            logger.debug("<<< Exiting k0Changed(text=%s)", text, extra={"event.action": "k0Changed", "logrite.text": text})
            
        def returnk0(self):
            logger.warning(">>> Entering returnk0()", extra={"event.action": "returnk0"})
            logger.debug("<<< Exiting returnk0()", extra={"event.action": "returnk0"})
            return self.Keuze.text()
                 
        @staticmethod
        def getData(parent=None):
            logger.warning(">>> Entering getData(parent=%s)", parent, extra={"event.action": "getData"})
            dialog = Widget(parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog, extra={"event.action": "getData"})
            dialog.exec_()
            logger.debug("<<< Exiting getData(parent=%s)", parent, extra={"event.action": "getData"})
            return [dialog.returnk0()]       

    window = Widget()
    data = window.getData()
    keuze = ''
    if not data[0]:
        ongKeuze()
        kiesCluster(m_email)
    elif data[0][0] == '0':
        keuze = ''
    elif data[0]:
        keuze = data[0][0]
        if keuze == 'L': 
            kiesSubClusterL(keuze, m_email) 
        elif keuze == 'M':
            kiesSubClusterM(keuze, m_email) 
        elif keuze == 'N':
            kiesSubClusterN(keuze, m_email) 
        elif keuze == 'O':
            kiesSubClusterO(keuze, m_email) 
        elif keuze == 'P':
            kiesSubClusterP(keuze, m_email) 
        elif keuze == 'R':
            kiesSubClusterR(keuze, m_email) 
        elif keuze == 'S':
            kiesSubClusterS(keuze, m_email) 
        elif keuze == 'T':
            kiesSubClusterT(keuze, m_email) 
  
def kiesSubClusterL(keuze, m_email):
    logger.warning(">>> Entering kiesSubClusterL(keuze=%s,m_email=%s)", keuze, m_email, extra={"event.action": "kiesSubClusterL", "logrite.keuze": keuze})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle("Cluster selection")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
                              
            self.Keuze = QLabel()
            k0Edit = QComboBox()
            k0Edit.setFixedWidth(340)
            k0Edit.setFont(QFont("Arial",10))
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.addItem(rpa[0][2])
            k0Edit.addItem(rpa[0][4])
            k0Edit.addItem(rpa[0][5])
            k0Edit.addItem(rpa[0][6])
            k0Edit.addItem(rpa[0][7])
            k0Edit.addItem(rpa[0][8])
            k0Edit.addItem(rpa[0][9])
            k0Edit.addItem(rpa[0][10])
            k0Edit.addItem(rpa[0][11])
            k0Edit.addItem(rpa[0][12])
            k0Edit.addItem(rpa[0][13])
            k0Edit.addItem(rpa[0][14])
            
            k0Edit.activated[str].connect(self.k0Changed)
 
            grid = QGridLayout()
            grid.setSpacing(20)
                          
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 0, 0, 1, 2)
                        
            grid.addWidget(k0Edit, 1, 1)
            
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 3, 0, 1, 2, Qt.AlignCenter)
            
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 1, 1, 1, Qt.AlignRight)
   
            applyBtn = QPushButton('Create cluster')
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 2, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(110)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Close')
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
    
            grid.addWidget(cancelBtn, 2, 1, 1, 1,Qt.AlignCenter)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
           
        def k0Changed(self, text):
            self.Keuze.setText(text)
            
        def returnk0(self):
            return self.Keuze.text()
                 
        @staticmethod
        def getData(parent=None):
            dialog = Widget(parent)
            dialog.exec_()
            return [dialog.returnk0()]       

    window = Widget()
    data = window.getData()
    keuze1 = ''
    momschr = ''
    if not data[0]:
        ongKeuze()
        kiesCluster(m_email)
    elif data[0][0] == '0':
        keuze1 = ''
    elif data[0]:
        keuze1 = data[0][1]
        momschr = data[0][4:]
    keuze = keuze+keuze1
    maakCluster(keuze, momschr, m_email)
    
def kiesSubClusterM(keuze, m_email):
    logger.warning(">>> Entering kiesSubClusterM(keuze=%s,m_email=%s)", keuze, m_email, extra={"event.action": "kiesSubClusterM", "logrite.keuze": keuze})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle("Cluster selektie")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
                              
            self.Keuze = QLabel()
            k0Edit = QComboBox()
            k0Edit.setFixedWidth(340)
            k0Edit.setFont(QFont("Arial",10))
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.addItem(rpa[1][2])
            k0Edit.addItem(rpa[1][4])
            k0Edit.addItem(rpa[1][5])
            k0Edit.addItem(rpa[1][6])
            k0Edit.addItem(rpa[1][7])
            k0Edit.addItem(rpa[1][8])
            k0Edit.addItem(rpa[1][9])
            k0Edit.addItem(rpa[1][10])
            k0Edit.addItem(rpa[1][11])
            k0Edit.addItem(rpa[1][12])
            k0Edit.addItem(rpa[1][13])
            k0Edit.addItem(rpa[1][14])
            k0Edit.activated[str].connect(self.k0Changed)
 
            grid = QGridLayout()
            grid.setSpacing(20)
                          
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 0, 0, 1, 2)
                        
            grid.addWidget(k0Edit, 1, 1)
            
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 3, 0, 1, 2, Qt.AlignCenter)
            
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 1, 1, 1, Qt.AlignRight)
   
            applyBtn = QPushButton('Create cluster')
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 2, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(110)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Close')
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
    
            grid.addWidget(cancelBtn, 2, 1, 1, 1,Qt.AlignCenter)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
           
        def k0Changed(self, text):
            self.Keuze.setText(text)
            
        def returnk0(self):
            return self.Keuze.text()
                 
        @staticmethod
        def getData(parent=None):
            dialog = Widget(parent)
            dialog.exec_()
            return [dialog.returnk0()]       

    window = Widget()
    data = window.getData()
    keuze1 = ''
    momschr = ''
    if not data[0]:
        ongKeuze()
        kiesCluster(m_email)
    elif data[0][0] == '0':
        keuze1 = ''
    elif data[0]:
        keuze1 = data[0][1]
        momschr = data[0][4:]
    keuze = keuze+keuze1
    maakCluster(keuze, momschr, m_email)

def kiesSubClusterN(keuze, m_email):
    logger.warning(">>> Entering kiesSubClusterN(keuze=%s,m_email=%s)", keuze, m_email, extra={"event.action": "kiesSubClusterN", "logrite.keuze": keuze})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle("Cluster selection")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
                              
            self.Keuze = QLabel()
            k0Edit = QComboBox()
            k0Edit.setFixedWidth(340)
            k0Edit.setFont(QFont("Arial",10))
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.addItem(rpa[2][2])
            k0Edit.addItem(rpa[2][4])
            k0Edit.addItem(rpa[2][5])
            k0Edit.addItem(rpa[2][6])
            k0Edit.addItem(rpa[2][7])
            k0Edit.addItem(rpa[2][8])
            k0Edit.addItem(rpa[2][9])
            k0Edit.addItem(rpa[2][10])
            k0Edit.addItem(rpa[2][11])
            k0Edit.addItem(rpa[2][12])
            k0Edit.addItem(rpa[2][13])
            k0Edit.addItem(rpa[2][14])
            k0Edit.activated[str].connect(self.k0Changed)
 
            grid = QGridLayout()
            grid.setSpacing(20)
                          
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 0, 0, 1, 2)
                        
            grid.addWidget(k0Edit, 1, 1)
            
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 3, 0, 1, 2, Qt.AlignCenter)
            
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 1, 1, 1, Qt.AlignRight)
   
            applyBtn = QPushButton('Create cluster')
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 2, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(110)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Close')
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
    
            grid.addWidget(cancelBtn, 2, 1, 1, 1,Qt.AlignCenter)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
           
        def k0Changed(self, text):
            self.Keuze.setText(text)
            
        def returnk0(self):
            return self.Keuze.text()
                 
        @staticmethod
        def getData(parent=None):
            dialog = Widget(parent)
            dialog.exec_()
            return [dialog.returnk0()]       

    window = Widget()
    data = window.getData()
    keuze1 = ''
    momschr = ''
    if not data[0]:
        ongKeuze()
        kiesCluster(m_email)
    elif data[0][0] == '0':
        keuze1 = ''
    elif data[0]:
        keuze1 = data[0][1]
        momschr = data[0][4:]
    keuze = keuze+keuze1
    maakCluster(keuze, momschr, m_email)

def kiesSubClusterO(keuze, m_email):
    logger.warning(">>> Entering kiesSubClusterO(keuze=%s,m_email=%s)", keuze, m_email, extra={"event.action": "kiesSubClusterO", "logrite.keuze": keuze})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle("Cluster selection")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
                              
            self.Keuze = QLabel()
            k0Edit = QComboBox()
            k0Edit.setFixedWidth(340)
            k0Edit.setFont(QFont("Arial",10))
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.addItem(rpa[3][2])
            k0Edit.addItem(rpa[3][4])
            k0Edit.addItem(rpa[3][5])
            k0Edit.addItem(rpa[3][6])
            k0Edit.addItem(rpa[3][7])
            k0Edit.addItem(rpa[3][8])
            k0Edit.addItem(rpa[3][9])
            k0Edit.addItem(rpa[3][10])
            k0Edit.addItem(rpa[3][11])
            k0Edit.addItem(rpa[3][12])
            k0Edit.addItem(rpa[3][13])
            k0Edit.addItem(rpa[3][14])
            k0Edit.activated[str].connect(self.k0Changed)
 
            grid = QGridLayout()
            grid.setSpacing(20)
                          
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 0, 0, 1, 2)
                        
            grid.addWidget(k0Edit, 1, 1)
            
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 3, 0, 1, 2, Qt.AlignCenter)
            
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 1, 1, 1, Qt.AlignRight)
   
            applyBtn = QPushButton('Create cluster')
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 2, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(110)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Close')
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
    
            grid.addWidget(cancelBtn, 2, 1, 1, 1,Qt.AlignCenter)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
           
        def k0Changed(self, text):
            self.Keuze.setText(text)
            
        def returnk0(self):
            return self.Keuze.text()
                 
        @staticmethod
        def getData(parent=None):
            dialog = Widget(parent)
            dialog.exec_()
            return [dialog.returnk0()]       

    window = Widget()
    data = window.getData()
    keuze1 = ''
    momschr = ''
    if not data[0]:
        ongKeuze()
        kiesCluster(m_email)
    elif data[0][0] == '0':
        keuze1 = ''
    elif data[0]:
        keuze1 = data[0][1]
        momschr = data[0][4:]
    keuze = keuze+keuze1
    maakCluster(keuze, momschr, m_email)

def kiesSubClusterP(keuze, m_email):
    logger.warning(">>> Entering kiesSubClusterP(keuze=%s,m_email=%s)", keuze, m_email, extra={"event.action": "kiesSubClusterP", "logrite.keuze": keuze})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle("Cluster selection")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
                              
            self.Keuze = QLabel()
            k0Edit = QComboBox()
            k0Edit.setFixedWidth(340)
            k0Edit.setFont(QFont("Arial",10))
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.addItem(rpa[4][2])
            k0Edit.addItem(rpa[4][4])
            k0Edit.addItem(rpa[4][5])
            k0Edit.addItem(rpa[4][6])
            k0Edit.addItem(rpa[4][7])
            k0Edit.addItem(rpa[4][8])
            k0Edit.addItem(rpa[4][9])
            k0Edit.addItem(rpa[4][10])
            k0Edit.addItem(rpa[4][11])
            k0Edit.addItem(rpa[4][12])
            k0Edit.addItem(rpa[4][13])
            k0Edit.addItem(rpa[4][14])
            k0Edit.activated[str].connect(self.k0Changed)
 
            grid = QGridLayout()
            grid.setSpacing(20)
                          
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 0, 0, 1, 2)
                        
            grid.addWidget(k0Edit, 1, 1)
            
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 3, 0, 1, 2, Qt.AlignCenter)
            
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 1, 1, 1, Qt.AlignRight)
   
            applyBtn = QPushButton('Create cluster')
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 2, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(110)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Close')
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
    
            grid.addWidget(cancelBtn, 2, 1, 1, 1,Qt.AlignCenter)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
           
        def k0Changed(self, text):
            self.Keuze.setText(text)
            
        def returnk0(self):
            return self.Keuze.text()
                 
        @staticmethod
        def getData(parent=None):
            dialog = Widget(parent)
            dialog.exec_()
            return [dialog.returnk0()]       

    window = Widget()
    data = window.getData()
    keuze1 = ''
    momschr = ''
    if not data[0]:
        ongKeuze()
        kiesCluster(m_email)
    elif data[0][0] == '0':
        keuze1 = ''
    elif data[0]:
        keuze1 = data[0][1]
        momschr = data[0][4:]
    keuze = keuze+keuze1
    maakCluster(keuze, momschr, m_email)

def kiesSubClusterR(keuze, m_email):
    logger.warning(">>> Entering kiesSubClusterR(keuze=%s,m_email=%s)", keuze, m_email, extra={"event.action": "kiesSubClusterR", "logrite.keuze": keuze})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle("Cluster selection")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
                              
            self.Keuze = QLabel()
            k0Edit = QComboBox()
            k0Edit.setFixedWidth(340)
            k0Edit.setFont(QFont("Arial",10))
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.addItem(rpa[5][2])
            k0Edit.addItem(rpa[5][4])
            k0Edit.addItem(rpa[5][5])
            k0Edit.addItem(rpa[5][6])
            k0Edit.addItem(rpa[5][7])
            k0Edit.addItem(rpa[5][8])
            k0Edit.addItem(rpa[5][9])
            k0Edit.addItem(rpa[5][10])
            k0Edit.addItem(rpa[5][11])
            k0Edit.addItem(rpa[5][12])
            k0Edit.addItem(rpa[5][13])
            k0Edit.addItem(rpa[5][14])
            k0Edit.activated[str].connect(self.k0Changed)
 
            grid = QGridLayout()
            grid.setSpacing(20)
                          
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 0, 0, 1, 2)
                        
            grid.addWidget(k0Edit, 1, 1)
            
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 3, 0, 1, 2, Qt.AlignCenter)
            
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 1, 1, 1, Qt.AlignRight)
   
            applyBtn = QPushButton('Create cluster')
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 2, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(110)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Close')
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
    
            grid.addWidget(cancelBtn, 2, 1, 1, 1,Qt.AlignCenter)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
           
        def k0Changed(self, text):
            self.Keuze.setText(text)
            
        def returnk0(self):
            return self.Keuze.text()
                 
        @staticmethod
        def getData(parent=None):
            dialog = Widget(parent)
            dialog.exec_()
            return [dialog.returnk0()]       

    window = Widget()
    data = window.getData()
    keuze1 = ''
    momschr = ''
    if not data[0]:
        ongKeuze()
        kiesCluster(m_email)
    elif data[0][0] == '0':
        keuze1 = ''
    elif data[0]:
        keuze1 = data[0][1]
        momschr = data[0][4:]
    keuze = keuze+keuze1
    maakCluster(keuze, momschr, m_email)

def kiesSubClusterS(keuze, m_email):
    logger.warning(">>> Entering kiesSubClusterS(keuze=%s,m_email=%s)", keuze, m_email, extra={"event.action": "kiesSubClusterS", "logrite.keuze": keuze})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle("Cluster selection")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
                              
            self.Keuze = QLabel()
            k0Edit = QComboBox()
            k0Edit.setFixedWidth(340)
            k0Edit.setFont(QFont("Arial",10))
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.addItem(rpa[6][2])
            k0Edit.addItem(rpa[6][4])
            k0Edit.addItem(rpa[6][5])
            k0Edit.addItem(rpa[6][6])
            k0Edit.addItem(rpa[6][7])
            k0Edit.addItem(rpa[6][8])
            k0Edit.addItem(rpa[6][9])
            k0Edit.addItem(rpa[6][10])
            k0Edit.addItem(rpa[6][11])
            k0Edit.addItem(rpa[6][12])
            k0Edit.addItem(rpa[6][13])
            k0Edit.addItem(rpa[6][14])
            k0Edit.activated[str].connect(self.k0Changed)
 
            grid = QGridLayout()
            grid.setSpacing(20)
                          
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 0, 0, 1, 2)
                        
            grid.addWidget(k0Edit, 1, 1)
            
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 3, 0, 1, 2, Qt.AlignCenter)
            
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 1, 1, 1, Qt.AlignRight)
   
            applyBtn = QPushButton('Create cluster')
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 2, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(110)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Close')
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
    
            grid.addWidget(cancelBtn, 2, 1, 1, 1,Qt.AlignCenter)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
           
        def k0Changed(self, text):
            self.Keuze.setText(text)
            
        def returnk0(self):
            return self.Keuze.text()
                 
        @staticmethod
        def getData(parent=None):
            dialog = Widget(parent)
            dialog.exec_()
            return [dialog.returnk0()]       

    window = Widget()
    data = window.getData()
    keuze1 = ''
    momschr = ''
    if not data[0]:
        ongKeuze()
        kiesCluster(m_email)
    elif data[0][0] == '0':
        keuze1 = ''
    elif data[0]:
        keuze1 = data[0][1]
        momschr = data[0][4:]
    keuze = keuze+keuze1
    maakCluster(keuze, momschr, m_email)

def kiesSubClusterT(keuze, m_email):
    logger.warning(">>> Entering kiesSubClusterT(keuze=%s,m_email=%s)", keuze, m_email, extra={"event.action": "kiesSubClusterT", "logrite.keuze": keuze})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle("Cluster selektie")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
                              
            self.Keuze = QLabel()
            k0Edit = QComboBox()
            k0Edit.setFixedWidth(340)
            k0Edit.setFont(QFont("Arial",10))
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.addItem(rpa[7][2])
            k0Edit.addItem(rpa[7][4])
            k0Edit.addItem(rpa[7][5])
            k0Edit.addItem(rpa[7][6])
            k0Edit.addItem(rpa[7][7])
            k0Edit.addItem(rpa[7][8])
            k0Edit.addItem(rpa[7][9])
            k0Edit.addItem(rpa[7][10])
            k0Edit.addItem(rpa[7][11])
            k0Edit.addItem(rpa[7][12])
            k0Edit.addItem(rpa[7][13])
            k0Edit.addItem(rpa[7][14])
            k0Edit.activated[str].connect(self.k0Changed)
 
            grid = QGridLayout()
            grid.setSpacing(20)
                          
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 0, 0, 1, 2)
                        
            grid.addWidget(k0Edit, 1, 1)
            
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 3, 0, 1, 2, Qt.AlignCenter)
            
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 1, 1, 1, Qt.AlignRight)
   
            applyBtn = QPushButton('Create cluster')
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 2, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(110)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Close')
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
    
            grid.addWidget(cancelBtn, 2, 1, 1, 1,Qt.AlignCenter)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
           
        def k0Changed(self, text):
            self.Keuze.setText(text)
            
        def returnk0(self):
            return self.Keuze.text()
                 
        @staticmethod
        def getData(parent=None):
            dialog = Widget(parent)
            dialog.exec_()
            return [dialog.returnk0()]       

    window = Widget()
    data = window.getData()
    keuze1 = ''
    momschr = ''
    if not data[0]:
        ongKeuze()
        kiesCluster(m_email)
    elif data[0][0] == '0':
        keuze1 = ''
    elif data[0]:
        keuze1 = data[0][1]
        momschr = data[0][4:]
    keuze = keuze+keuze1
    maakCluster(keuze, momschr, m_email)

def maakCluster(keuze, momschr, m_email):
    logger.warning(">>> Entering maakCluster(keuze=%s,momschr=%s,m_email=%s)", keuze, momschr, m_email, extra={"event.action": "maakCluster", "logrite.keuze": keuze, "logrite.momschr": momschr})
    metadata = MetaData()
    logger.debug("maakCluster(keuze=%s,momschr=%s,m_email=%s): metadata → %s", keuze, momschr, m_email, metadata, extra={"event.action": "maakCluster", "logrite.keuze": keuze, "logrite.momschr": momschr})
    iclusters = Table('iclusters', metadata,
        Column('iclusterID', String, primary_key=True),
        Column('omschrijving', String))
 
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("maakCluster(keuze=%s,momschr=%s,m_email=%s): engine → %s", keuze, momschr, m_email, engine, extra={"event.action": "maakCluster", "logrite.keuze": keuze, "logrite.momschr": momschr})
    con = engine.connect()
    logger.debug("maakCluster(keuze=%s,momschr=%s,m_email=%s): con → %s", keuze, momschr, m_email, con, extra={"event.action": "maakCluster", "logrite.keuze": keuze, "logrite.momschr": momschr})

    try:
        selcllast = select([iclusters]).where(iclusters.c.iclusterID.like(keuze+'%')).order_by(iclusters.c.iclusterID.desc())
        logger.debug("maakCluster(keuze=%s,momschr=%s,m_email=%s): selcllast → %s", keuze, momschr, m_email, selcllast, extra={"event.action": "maakCluster", "logrite.keuze": keuze, "logrite.momschr": momschr})
        rpcllast = con.execute(selcllast).first()
        logger.debug("maakCluster(keuze=%s,momschr=%s,m_email=%s): rpcllast → %s", keuze, momschr, m_email, rpcllast, extra={"event.action": "maakCluster", "logrite.keuze": keuze, "logrite.momschr": momschr})
        mclusternr = keuze+('00000'+str(int(rpcllast[0][2:7])+1))[-5:]
    except Exception:
        mclusternr = keuze+'00001'
        logger.debug("maakCluster(keuze=%s,momschr=%s,m_email=%s): mclusternr → %s", keuze, momschr, m_email, mclusternr, extra={"event.action": "maakCluster", "logrite.keuze": keuze, "logrite.momschr": momschr})
        logger.error("Exception in maakCluster(keuze=%s,momschr=%s,m_email=%s)", keuze, momschr, m_email, exc_info=True, extra={"event.action": "maakCluster", "event.category": "process", "logrite.keuze": keuze, "logrite.momschr": momschr})
  
    try:
        inscl = insert(iclusters).values(iclusterID=mclusternr, omschrijving=momschr)
        con.execute(inscl)
        logger.debug("maakCluster(keuze=%s,momschr=%s,m_email=%s): inscl → %s", keuze, momschr, m_email, inscl, extra={"event.action": "maakCluster", "logrite.keuze": keuze, "logrite.momschr": momschr})
        insGelukt(mclusternr, momschr, m_email)
        kiesCluster(m_email)
    except Exception:
        insMislukt(mclusternr, momschr, m_email)
        logger.debug("<<< Exiting maakCluster(keuze=%s,momschr=%s,m_email=%s)", keuze, momschr, m_email, extra={"event.action": "maakCluster", "logrite.keuze": keuze, "logrite.momschr": momschr})
        kiesCluster(m_email)