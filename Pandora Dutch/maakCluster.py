from login import hoofdMenu
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QDialog, QLabel,\
         QGridLayout, QPushButton, QMessageBox, QComboBox
from sqlalchemy import (Table, Column, String, MetaData, create_engine, insert, select)
import logging
logger = logging.getLogger(__name__)

def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    
def insGelukt(mclusternr, momschr):
    logger.warning(">>> Entering insGelukt(mclusternr=%s,momschr=%s)", mclusternr, momschr, extra={"event.action": "insGelukt", "logrite.mclusternr": mclusternr, "logrite.momschr": momschr})
    msg = QMessageBox()
    logger.debug("insGelukt(mclusternr=%s,momschr=%s): msg → %s", mclusternr, momschr, msg, extra={"event.action": "insGelukt", "logrite.mclusternr": mclusternr, "logrite.momschr": momschr})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Information)
    msg.setText('Clusternummer: '+mclusternr+'\n"'+momschr+'" is aangemaakt!')
    msg.setFont(QFont("Arial",10))
    msg.setWindowTitle('Clusters aanmaken')               
    logger.debug("<<< Exiting insGelukt(mclusternr=%s,momschr=%s)", mclusternr, momschr, extra={"event.action": "insGelukt", "logrite.mclusternr": mclusternr, "logrite.momschr": momschr})
    msg.exec_() 
    
def insMislukt():
    logger.warning(">>> Entering insMislukt()", extra={"event.action": "insMislukt"})
    msg = QMessageBox()
    logger.debug("insMislukt(): msg → %s", msg, extra={"event.action": "insMislukt"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Critical)
    msg.setText('Aanmaak van clusternummer is mislukt!')
    msg.setFont(QFont("Arial",10))
    msg.setWindowTitle('Clusters aanmaken')               
    logger.debug("<<< Exiting insMislukt()", extra={"event.action": "insMislukt"})
    msg.exec_() 

def ongKeuze():
    logger.warning(">>> Entering ongKeuze()", extra={"event.action": "ongKeuze"})
    msg = QMessageBox()
    logger.debug("ongKeuze(): msg → %s", msg, extra={"event.action": "ongKeuze"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Ongeldige keuze')
    msg.setFont(QFont("Arial",10))
    msg.setWindowTitle('Clusters invoeren')               
    logger.debug("<<< Exiting ongKeuze()", extra={"event.action": "ongKeuze"})
    msg.exec_() 

def kiesCluster(m_email):
    logger.warning(">>> Entering kiesCluster(m_email=%s)", m_email, extra={"event.action": "kiesCluster"})
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
            k0Edit.addItem('                   Keuze Clustergroepen')
            k0Edit.addItem('AA-AL. Spoorstaven + lasmiddelen')
            k0Edit.addItem('BA-BK. Telecominstallaties')
            k0Edit.addItem('CA-CK. Overwegen + overwegbeveiliging')
            k0Edit.addItem('DA-DK. Steenslag + grond aanvulling')
            k0Edit.addItem('EA-EK. Wissel + baanconstrukties')
            k0Edit.addItem('FA-FK. Ondergrondse infrastruktuur')
            k0Edit.addItem('GA-GK. Treinbeheersing + seinen')
            k0Edit.addItem('HA-HK. Bovenleiding + draagconstruktie')
            k0Edit.addItem('JA-JK. Voedingen + Onderstations')
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
   
            applyBtn = QPushButton('Subgroep')
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 2, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Sluiten')
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
        if keuze == 'A': 
            kiesSubClusterA(keuze, m_email) 
        elif keuze == 'B':
            kiesSubClusterB(keuze, m_email) 
        elif keuze == 'C':
            kiesSubClusterC(keuze, m_email) 
        elif keuze == 'D':
            kiesSubClusterD(keuze, m_email) 
        elif keuze == 'E':
            kiesSubClusterE(keuze, m_email) 
        elif keuze == 'F':
            kiesSubClusterF(keuze, m_email) 
        elif keuze == 'G':
            kiesSubClusterG(keuze, m_email) 
        elif keuze == 'H':
            kiesSubClusterH(keuze, m_email) 
        elif keuze == 'J':
            kiesSubClusterJ(keuze, m_email)        
    
def kiesSubClusterA(keuze, m_email):
    logger.warning(">>> Entering kiesSubClusterA(keuze=%s,m_email=%s)", keuze, m_email, extra={"event.action": "kiesSubClusterA", "logrite.keuze": keuze})
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
            k0Edit.addItem('         Subgroep Spoorstaven-lasmiddelen')
            k0Edit.addItem('AA. Spoorbaan UIC54 recht op hout')
            k0Edit.addItem('AB. Spoorbaan UIC54 recht op beton')
            k0Edit.addItem('AC. Spoorbaan UIC60 recht op hout')
            k0Edit.addItem('AD. Spoorbaan UIC60 recht op beton')
            k0Edit.addItem('AE. Spoorbaan NP46 recht op hout')
            k0Edit.addItem('AF. Spoorbaan NP46 recht op beton')
            k0Edit.addItem('AG. Spoorbaan UIC54 verk. op hout')
            k0Edit.addItem('AH. Spoorbaan UIC54 veranting op beton')
            k0Edit.addItem('AI. Spoorbaan UIC60 verkanting op hout')
            k0Edit.addItem('AJ. Spoorbaan UIC60 verkanting op beton')
            k0Edit.addItem('AK. Spoorbaan NP46 verkanting op hout')
            k0Edit.addItem('AL. Spoorbaan NP46 verkanting op beton')
            
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
   
            applyBtn = QPushButton('Maak cluster')
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 2, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(110)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Sluiten')
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
    maakCluster(keuze, momschr) 
    
def kiesSubClusterB(keuze, m_email):
    logger.warning(">>> Entering kiesSubClusterB(keuze=%s,m_email=%s)", keuze, m_email, extra={"event.action": "kiesSubClusterB", "logrite.keuze": keuze})
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
            k0Edit.addItem('           Subgroep Telecominstallaties')
            k0Edit.addItem('BA. Treininformatie telecom')
            k0Edit.addItem('BB. Verkeersleiding telecom')
            k0Edit.addItem('BC. Perron informatie telecom')
            k0Edit.addItem('BD. Lassen en pupiniseren telecomkabels')
            k0Edit.addItem('BE. Relaishuis telecomrekken bedraden')
            k0Edit.addItem('BF. Vrije baan telecominstallaties')
            k0Edit.addItem('BG. Treinbeheersing telecom ATB')
            k0Edit.addItem('BH. Omroepinformatie telecom')
            k0Edit.addItem('BI. Onderhoud telecom stations')
            k0Edit.addItem('BJ. Subgroep 10 telecom')
            k0Edit.addItem('BK. Subgroep 11 telecom')
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
   
            applyBtn = QPushButton('Maak cluster')
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 2, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(110)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Sluiten')
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
    maakCluster(keuze, momschr) 

def kiesSubClusterC(keuze, m_email):
    logger.warning(">>> Entering kiesSubClusterC(keuze=%s,m_email=%s)", keuze, m_email, extra={"event.action": "kiesSubClusterC", "logrite.keuze": keuze})
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
            k0Edit.addItem('   Subgroep Overwegen-overwegbeveiliging')
            k0Edit.addItem('CA. AHOB installatie overwegen')
            k0Edit.addItem('CB. AKI installatie overwegen')
            k0Edit.addItem('CC. Relaiskasten overweg')
            k0Edit.addItem('CD. Borden en bebakening overwegen')
            k0Edit.addItem('CE. Voeding overwegen')
            k0Edit.addItem('CF. Aankondiging overwegen')
            k0Edit.addItem('CG. Overweg beplating')
            k0Edit.addItem('CH. Sugroep overwegen H')
            k0Edit.addItem('CI. Subgroep overwegen I')
            k0Edit.addItem('CJ. Subgroep overwegen J')
            k0Edit.addItem('CK. Subgroep overwegen K')
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
   
            applyBtn = QPushButton('Maak cluster')
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 2, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(110)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Sluiten')
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
    maakCluster(keuze, momschr) 

def kiesSubClusterD(keuze, m_email):
    logger.warning(">>> Entering kiesSubClusterD(keuze=%s,m_email=%s)", keuze, m_email, extra={"event.action": "kiesSubClusterD", "logrite.keuze": keuze})
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
            k0Edit.addItem('              Subgroep Onderbouw')
            k0Edit.addItem('DA. Subgroep Onderbouw A')
            k0Edit.addItem('DB. Subgroep Onderbouw B')
            k0Edit.addItem('DC. Subgroep Onderbouw C')
            k0Edit.addItem('DD. Subgroep Onderbouw D')
            k0Edit.addItem('DE. Subgroep Onderbouw E')
            k0Edit.addItem('DF. Subgroep Onderbouw F')
            k0Edit.addItem('DG. Subgroep Onderbouw G')
            k0Edit.addItem('DH. Subgroep Onderbouw H')
            k0Edit.addItem('DI. Subgroep Onderbouw I')
            k0Edit.addItem('DJ. Subgroep Onderbouw J')
            k0Edit.addItem('DK. Subgroep Onderbouw K')
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
   
            applyBtn = QPushButton('Maak cluster')
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 2, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(110)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Sluiten')
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
    maakCluster(keuze, momschr) 

def kiesSubClusterE(keuze, m_email):
    logger.warning(">>> Entering kiesSubClusterE(keuze=%s,m_email=%s)", keuze, m_email, extra={"event.action": "kiesSubClusterE", "logrite.keuze": keuze})
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
            k0Edit.addItem('       Subgroep Wissel-Baanconstrukties')
            k0Edit.addItem('EA. Subgroep Wissels + baan A')
            k0Edit.addItem('EB. Subgroep Wissels + baan B')
            k0Edit.addItem('EC. Subgroep Wissels + baan C')
            k0Edit.addItem('ED. Subgroep Wissels + baan D')
            k0Edit.addItem('EE. Subgroep Wissels + baan E')
            k0Edit.addItem('EF. Subgroep Wissels + baan F')
            k0Edit.addItem('EG. Subgroep Wissels + baan G')
            k0Edit.addItem('EH. Subgroep Wissels + baan H')
            k0Edit.addItem('EI. Subgroep Wissels + baan I')
            k0Edit.addItem('EJ. Subgroep Wissels + baan J')
            k0Edit.addItem('EK. Subgroep Wissels + baan K')
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
   
            applyBtn = QPushButton('Maak cluster')
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 2, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(110)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Sluiten')
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
    maakCluster(keuze, momschr) 

def kiesSubClusterF(keuze, m_email):
    logger.warning(">>> Entering kiesSubClusterF(keuze=%s,m_email=%s)", keuze, m_email, extra={"event.action": "kiesSubClusterF", "logrite.keuze": keuze})
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
            k0Edit.addItem(' Subgroep Ondergrondse Infrastruktuur')
            k0Edit.addItem('FA. Subgroep Ondergr. infra A')
            k0Edit.addItem('FB. Subgroep Ondergr. infra B')
            k0Edit.addItem('FC. Subgroep Ondergr. infra C')
            k0Edit.addItem('FD. Subgroep Ondergr. infra D')
            k0Edit.addItem('FE. Subgroep Ondergr. infra E')
            k0Edit.addItem('FF. Subgroep Ondergr. infra F')
            k0Edit.addItem('FG. Subgroep Ondergr. infra G')
            k0Edit.addItem('FH. Subgroep Ondergr. infra H')
            k0Edit.addItem('FI. Subgroep Ondergr. infra I')
            k0Edit.addItem('FJ. Subgroep Ondergr. infra J')
            k0Edit.addItem('FK. Subgroep Ondergr. infra K')
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
   
            applyBtn = QPushButton('Maak cluster')
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 2, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(110)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Sluiten')
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
    maakCluster(keuze, momschr) 

def kiesSubClusterG(keuze, m_email):
    logger.warning(">>> Entering kiesSubClusterG(keuze=%s,m_email=%s)", keuze, m_email, extra={"event.action": "kiesSubClusterG", "logrite.keuze": keuze})
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
            k0Edit.addItem('     Subgroep Treinbeheersing-Seinen')
            k0Edit.addItem('GA. Subgroep treinbeheersing + seinen A')
            k0Edit.addItem('GB. Subgroep treinbeheersing + seinen B')
            k0Edit.addItem('GC. Subgroep treinbeheersing + seinen C')
            k0Edit.addItem('GD. Subgroep treinbeheersing + seinen D')
            k0Edit.addItem('GE. Subgroep treinbeheersing + seinen E')
            k0Edit.addItem('GF. Subgroep treinbeheersing + seinen F')
            k0Edit.addItem('GG. Subgroep treinbeheersing + seinen G')
            k0Edit.addItem('GH. Subgroep treinbeheersing + seinen H')
            k0Edit.addItem('GI. Subgroep treinbeheersing + seinen I')
            k0Edit.addItem('GJ. Subgroep treinbeheersing + seinen J')
            k0Edit.addItem('GK. Subgroep treinbeheersing + seinen K')
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
   
            applyBtn = QPushButton('Maak cluster')
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 2, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(110)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Sluiten')
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
    maakCluster(keuze, momschr) 

def kiesSubClusterH(keuze, m_email):
    logger.warning(">>> Entering kiesSubClusterH(keuze=%s,m_email=%s)", keuze, m_email, extra={"event.action": "kiesSubClusterH", "logrite.keuze": keuze})
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
            k0Edit.addItem('   Subgroep Bovenleiding-Draagconstruktie')
            k0Edit.addItem('HA. Subgroep Bvl + draagconstruktie A')
            k0Edit.addItem('HB. Subgroep Bvl + draagconstruktie B')
            k0Edit.addItem('HC. Subgroep Bvl + draagconstruktie C')
            k0Edit.addItem('HD. Subgroep Bvl + draagconstruktie D')
            k0Edit.addItem('HE. Subgroep Bvl + draagconstruktie E')
            k0Edit.addItem('HF. Subgroep Bvl + draagconstruktie F')
            k0Edit.addItem('HG. Subgroep Bvl + draagconstruktie G')
            k0Edit.addItem('HH. Subgroep Bvl + draagconstruktie H')
            k0Edit.addItem('HI. Subgroep Bvl + draagconstruktie I')
            k0Edit.addItem('HJ. Subgroep Bvl + draagconstruktie J')
            k0Edit.addItem('HK. Subgroep Bvl + draagconstruktie K')
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
   
            applyBtn = QPushButton('Maak cluster')
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 2, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(110)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Sluiten')
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
    maakCluster(keuze, momschr) 

def kiesSubClusterJ(keuze, m_email):
    logger.warning(">>> Entering kiesSubClusterJ(keuze=%s,m_email=%s)", keuze, m_email, extra={"event.action": "kiesSubClusterJ", "logrite.keuze": keuze})
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
            k0Edit.addItem('    Subgroep Voedingen + Onderstations')
            k0Edit.addItem('JA  Subgroep Voedingen + Onderstations A')
            k0Edit.addItem('JB. Subgroep Voedingen + Onderstations B')
            k0Edit.addItem('JC. Subgroep Voedingen + Onderstations C')
            k0Edit.addItem('JD. Subgroep Voedingen + Onderstations D')
            k0Edit.addItem('JE. Subgroep Voedingen + Onderstations E')
            k0Edit.addItem('JF. Subgroep Voedingen + Onderstations F')
            k0Edit.addItem('JG. Subgroep Voedingen + Onderstations G')
            k0Edit.addItem('JH. Subgroep Voedingen + Onderstations H')
            k0Edit.addItem('JI. Subgroep Voedingen + Onderstations I')
            k0Edit.addItem('JJ. Subgroep Voedingen + Onderstations J')
            k0Edit.addItem('JK. Subgroep Voedingen + Onderstations K')
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
   
            applyBtn = QPushButton('Maak cluster')
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 2, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(110)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Sluiten')
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
    maakCluster(keuze, momschr) 

def maakCluster(keuze, momschr):
    logger.warning(">>> Entering maakCluster(keuze=%s,momschr=%s)", keuze, momschr, extra={"event.action": "maakCluster", "logrite.keuze": keuze, "logrite.momschr": momschr})
    metadata = MetaData()
    logger.debug("maakCluster(keuze=%s,momschr=%s): metadata → %s", keuze, momschr, metadata, extra={"event.action": "maakCluster", "logrite.keuze": keuze, "logrite.momschr": momschr})
    clusters = Table('clusters', metadata,
        Column('clusterID', String, primary_key=True),
        Column('omschrijving', String))
 
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("maakCluster(keuze=%s,momschr=%s): engine → %s", keuze, momschr, engine, extra={"event.action": "maakCluster", "logrite.keuze": keuze, "logrite.momschr": momschr})
    con = engine.connect()
    logger.debug("maakCluster(keuze=%s,momschr=%s): con → %s", keuze, momschr, con, extra={"event.action": "maakCluster", "logrite.keuze": keuze, "logrite.momschr": momschr})
    
    selcllast = select([clusters]).where(clusters.c.clusterID.like(keuze+'%')).order_by(clusters.c.clusterID.desc())
    logger.debug("maakCluster(keuze=%s,momschr=%s): selcllast → %s", keuze, momschr, selcllast, extra={"event.action": "maakCluster", "logrite.keuze": keuze, "logrite.momschr": momschr})
    rpcllast = con.execute(selcllast).first()
    if rpcllast:
        logger.debug("maakCluster(keuze=%s,momschr=%s): rpcllast → %s", keuze, momschr, rpcllast, extra={"event.action": "maakCluster", "logrite.keuze": keuze, "logrite.momschr": momschr})
        mclusternr = keuze+('00000'+str(int(rpcllast[0][2:7])+1))[-5:]
    else:
        mclusternr = keuze+'00001'
        logger.debug("maakCluster(keuze=%s,momschr=%s): mclusternr → %s", keuze, momschr, mclusternr, extra={"event.action": "maakCluster", "logrite.keuze": keuze, "logrite.momschr": momschr})
  
    inscl = insert(clusters).values(clusterID = mclusternr, omschrijving = momschr)
    if mclusternr:       
        logger.debug("maakCluster(keuze=%s,momschr=%s): inscl → %s", keuze, momschr, inscl, extra={"event.action": "maakCluster", "logrite.keuze": keuze, "logrite.momschr": momschr})
        con.execute(inscl)
        insGelukt(mclusternr, momschr)
    else:
        logger.debug("<<< Exiting maakCluster(keuze=%s,momschr=%s)", keuze, momschr, extra={"event.action": "maakCluster", "logrite.keuze": keuze, "logrite.momschr": momschr})
        insMislukt()