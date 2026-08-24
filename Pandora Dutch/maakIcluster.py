from login import hoofdMenu
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QDialog, QLabel,\
         QGridLayout, QPushButton, QMessageBox, QComboBox
from sqlalchemy import (Table, Column, String, MetaData, create_engine, insert, select)
import logging
logger = logging.getLogger(__name__)

def windowSluit(self, m_email):
    logger.debug(">>> Entering windowSluit(m_email=%s)", m_email)
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email)
    
def insGelukt(mclusternr, momschr):
    logger.debug(">>> Entering insGelukt(mclusternr=%s,momschr=%s)", mclusternr, momschr)
    msg = QMessageBox()
    logger.debug("insGelukt(mclusternr=%s,momschr=%s): msg → %s", mclusternr, momschr, msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Information)
    msg.setText('Clusternummer: '+mclusternr+'\n"'+momschr+'" is aangemaakt!')
    msg.setFont(QFont("Arial",10))
    msg.setWindowTitle('Clusters aanmaken')               
    logger.debug("<<< Exiting insGelukt(mclusternr=%s,momschr=%s)", mclusternr, momschr)
    msg.exec_() 
    
def insMislukt():
    logger.debug(">>> Entering insMislukt()")
    msg = QMessageBox()
    logger.debug("insMislukt(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Critical)
    msg.setText('Aanmaak van clusternummer is mislukt!')
    msg.setFont(QFont("Arial",10))
    msg.setWindowTitle('Clusters aanmaken')               
    logger.debug("<<< Exiting insMislukt()")
    msg.exec_() 

def ongKeuze():
    logger.debug(">>> Entering ongKeuze()")
    msg = QMessageBox()
    logger.debug("ongKeuze(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Ongeldige keuze')
    msg.setFont(QFont("Arial",10))
    msg.setWindowTitle('Clusters invoeren')               
    logger.debug("<<< Exiting ongKeuze()")
    msg.exec_() 

def kiesCluster(m_email):
    logger.debug(">>> Entering kiesCluster(m_email=%s)", m_email)
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle("Cluster selektie")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
                              
            self.Keuze = QLabel()
            k0Edit = QComboBox()
            k0Edit.setFixedWidth(320)
            k0Edit.setFont(QFont("Arial",10))
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.addItem('          Sorteersleutel Clustergroepen')
            k0Edit.addItem('LA-LK. Bewerkte onderdelen')
            k0Edit.addItem('MA-MK. Bouten en Moeren')
            k0Edit.addItem('NA-NK. Gietwerk bewerking')
            k0Edit.addItem('OA-OK. Laswerk samengesteld')
            k0Edit.addItem('PA-PK. Plaatwerk samengesteld')
            k0Edit.addItem('RA-RK. Kunstof onderdelen')
            k0Edit.addItem('SA-SK. Prefab Montagedelen')
            k0Edit.addItem('TA-TK. Samengestelde Onderdelen')
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
           
        def k0Changed(self, text):
            logger.debug(">>> Entering k0Changed(text=%s)", text)
            logger.debug("k0Changed(self=%s,text=%s): Keuze → %s", self, text, Keuze)
            self.Keuze.setText(text)
            logger.debug("<<< Exiting k0Changed(text=%s)", text)
            
        def returnk0(self):
            logger.debug(">>> Entering returnk0()")
            logger.debug("<<< Exiting returnk0()")
            return self.Keuze.text()
                 
        @staticmethod
        def getData(parent=None):
            logger.debug(">>> Entering getData(parent=%s)", parent)
            dialog = Widget(parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog)
            dialog.exec_()
            logger.debug("<<< Exiting getData(parent=%s)", parent)
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
    logger.debug(">>> Entering kiesSubClusterL(keuze=%s,m_email=%s)", keuze, m_email)
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
            k0Edit.addItem('      Subgroep Bewerkte Onderdelen')
            k0Edit.addItem('LA. Draaien non ferro')
            k0Edit.addItem('LB. Frezen non ferro')
            k0Edit.addItem('LC. Draaien ferro')
            k0Edit.addItem('LD. Frezen non fero')
            k0Edit.addItem('LE. Nube draaien ferro')
            k0Edit.addItem('LF. Nube draaien non ferro')
            k0Edit.addItem('LG. Nube bewerken ferro')
            k0Edit.addItem('LH. Nube bewerken non ferro')
            k0Edit.addItem('LI. Subgroep bewerkte onderdelen I')
            k0Edit.addItem('LJ. Subgroep bewerkte onderdelen J')
            k0Edit.addItem('LK. Subgroep bewerkte onderdelen K')
            
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
    
def kiesSubClusterM(keuze, m_email):
    logger.debug(">>> Entering kiesSubClusterM(keuze=%s,m_email=%s)", keuze, m_email)
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
            k0Edit.addItem('         Subgroep Bevestigingmaterialen')
            k0Edit.addItem('MA. Subgroep bevestigingmaterialen A')
            k0Edit.addItem('MB. Subgroep bevestigingmaterialen B')
            k0Edit.addItem('MC. Subgroep bevestigingmaterialen C')
            k0Edit.addItem('MD. Subgroep bevestigingmaterialen D')
            k0Edit.addItem('ME. Subgroep bevestigingmaterialen E')
            k0Edit.addItem('MF. Subgroep bevestigingmaterialen F')
            k0Edit.addItem('MG. Subgroep bevestigingmaterialen G')
            k0Edit.addItem('MH. Subgroep bevestigingmaterialen H')
            k0Edit.addItem('MI. Subgroep bevestigingmaterialen I')
            k0Edit.addItem('MJ. Subgroep bevestigingmaterialen J')
            k0Edit.addItem('MK. Subgroep bevestigingmaterialen K')
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

def kiesSubClusterN(keuze, m_email):
    logger.debug(">>> Entering kiesSubClusterN(keuze=%s,m_email=%s)", keuze, m_email)
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
            k0Edit.addItem('        Subgroep Gietwerk Bewerking')
            k0Edit.addItem('NA. Subgroep gietwerk bewerking A')
            k0Edit.addItem('NB. Subgroep gietwerk bewerking B')
            k0Edit.addItem('NC. Subgroep gietwerk bewerking C')
            k0Edit.addItem('ND. Subgroep gietwerk bewerking D')
            k0Edit.addItem('NE. Subgroep gietwerk bewerking E')
            k0Edit.addItem('NF. Subgroep gietwerk bewerking F')
            k0Edit.addItem('NG. Subgroep gietwerk bewerking G')
            k0Edit.addItem('NH. Subgroep gietwerk bewerking H')
            k0Edit.addItem('NI. Subgroep gietwerk bewerking I')
            k0Edit.addItem('NJ. Subgroep gietwerk bewerking J')
            k0Edit.addItem('NK. Subgroep gietwerk bewerking K')
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

def kiesSubClusterO(keuze, m_email):
    logger.debug(">>> Entering kiesSubClusterO(keuze=%s,m_email=%s)", keuze, m_email)
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
            k0Edit.addItem('         Subgroep Laswerk Samengesteld')
            k0Edit.addItem('OA. Subgroep laswerk samengesteld A')
            k0Edit.addItem('OB. Subgroep laswerk samengesteld B')
            k0Edit.addItem('OC. Subgroep laswerk samengesteld C')
            k0Edit.addItem('OD. Subgroep laswerk samengesteld D')
            k0Edit.addItem('OE. Subgroep laswerk samengesteld E')
            k0Edit.addItem('OF. Subgroep laswerk samengesteld F')
            k0Edit.addItem('OG. Subgroep laswerk samengesteld G')
            k0Edit.addItem('OH. Subgroep laswerk samengesteld H')
            k0Edit.addItem('OI. Subgroep laswerk samengesteld I')
            k0Edit.addItem('OJ. Subgroep laswerk samengesteld J')
            k0Edit.addItem('OK. Subgroep laswerk samengesteld K')
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

def kiesSubClusterP(keuze, m_email):
    logger.debug(">>> Entering kiesSubClusterP(keuze=%s,m_email=%s)", keuze, m_email)
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
            k0Edit.addItem('       Subgroep Plaatwerk Samengesteld')
            k0Edit.addItem('PA. Subgroep plaatwerk samengesteld A')
            k0Edit.addItem('PB. Subgroep plaatwerk samengesteld B')
            k0Edit.addItem('PC. Subgroep plaatwerk samengesteld C')
            k0Edit.addItem('PD. Subgroep plaatwerk samengesteld D')
            k0Edit.addItem('PE. Subgroep plaatwerk samengesteld E')
            k0Edit.addItem('PF. Subgroep plaatwerk samengesteld F')
            k0Edit.addItem('PG. Subgroep plaatwerk samengesteld G')
            k0Edit.addItem('PH. Subgroep plaatwerk samengesteld H')
            k0Edit.addItem('PI. Subgroep plaatwerk samengesteld I')
            k0Edit.addItem('PJ. Subgroep plaatwerk samengesteld J')
            k0Edit.addItem('PK. Subgroep plaatwerk samengesteld K')
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

def kiesSubClusterR(keuze, m_email):
    logger.debug(">>> Entering kiesSubClusterR(keuze=%s,m_email=%s)", keuze, m_email)
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
            k0Edit.addItem('           Subgroep Kunstof Onderdelen')
            k0Edit.addItem('RA. Subgroep kunstof onderdelen A')
            k0Edit.addItem('RB. Subgroep kunstof onderdelen B')
            k0Edit.addItem('RC. Subgroep kunstof onderdelen C')
            k0Edit.addItem('RD. Subgroep kunstof onderdelen D')
            k0Edit.addItem('RE. Subgroep kunstof onderdelen E')
            k0Edit.addItem('RF. Subgroep kunstof onderdelen F')
            k0Edit.addItem('RG. Subgroep kunstof onderdelen G')
            k0Edit.addItem('RH. Subgroep kunstof onderdelen H')
            k0Edit.addItem('RI. Subgroep kunstof onderdelen I')
            k0Edit.addItem('RJ. Subgroep kunstof onderdelen J')
            k0Edit.addItem('RK. Subgroep kunstof onderdelen K')
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
            logger.debug(">>> Entering __init__(parent=%s)", parent)
            logger.debug("__init__(parent=%s): k0Edit → %s", parent, k0Edit)
            logger.debug("__init__(parent=%s): self.Keuze → %s", parent, self.Keuze)
            logger.debug("__init__(self=%s,parent=%s): k0Edit → %s", self, parent, k0Edit)
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap)
            logger.debug("__init__(parent=%s): grid → %s", parent, grid)
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid)
            logger.debug("__init__(parent=%s): lbl → %s", parent, lbl)
            logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl)
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap)
            logger.debug("__init__(parent=%s): logo → %s", parent, logo)
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo)
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn)
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn)
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn)
            logger.debug("<<< Exiting __init__(parent=%s)", parent)
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn)
           
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

def kiesSubClusterS(keuze, m_email):
    logger.debug(">>> Entering kiesSubClusterS(keuze=%s,m_email=%s)", keuze, m_email)
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
            k0Edit.addItem('      Subgroep Samengestelde Onderdelen')
            k0Edit.addItem('SA. Subgroep samengestelde onderdelen A')
            k0Edit.addItem('SB. Subgroep samengestelde onderdelen B')
            k0Edit.addItem('SC. Subgroep samengestelde onderdelen C')
            k0Edit.addItem('SD. Subgroep samengestelde onderdelen D')
            k0Edit.addItem('SE. Subgroep samengestelde onderdelen E')
            k0Edit.addItem('SF. Subgroep samengestelde onderdelen F')
            k0Edit.addItem('SG. Subgroep samengestelde onderdelen G')
            k0Edit.addItem('SH. Subgroep samengestelde onderdelen H')
            k0Edit.addItem('SI. Subgroep samengestelde onderdelen I')
            k0Edit.addItem('SJ. Subgroep samengestelde onderdelen J')
            k0Edit.addItem('SK. Subgroep samengestelde onderdelen K')
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

def kiesSubClusterT(keuze, m_email):
    logger.debug(">>> Entering kiesSubClusterT(keuze=%s,m_email=%s)", keuze, m_email)
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
            k0Edit.addItem('           Subgroep Prefab Montagedelen')
            k0Edit.addItem('TA. Subgroep prefab montagedelen A')
            k0Edit.addItem('TB. Subgroep prefab montagedelen B')
            k0Edit.addItem('TC. Subgroep prefab montagedelen C')
            k0Edit.addItem('TD. Subgroep prefab montagedelen D')
            k0Edit.addItem('TE. Subgroep prefab montagedelen E')
            k0Edit.addItem('TF. Subgroep prefab montagedelen F')
            k0Edit.addItem('TG. Subgroep prefab montagedelen G')
            k0Edit.addItem('TH. Subgroep prefab montagedelen H')
            k0Edit.addItem('TI. Subgroep prefab montagedelen I')
            k0Edit.addItem('TJ. Subgroep prefab montagedelen J')
            k0Edit.addItem('TK. Subgroep prefab montagedelen K')
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
    logger.debug(">>> Entering maakCluster(keuze=%s,momschr=%s)", keuze, momschr)
    metadata = MetaData()
    logger.debug("maakCluster(keuze=%s,momschr=%s): metadata → %s", keuze, momschr, metadata)
    iclusters = Table('iclusters', metadata,
        Column('iclusterID', String, primary_key=True),
        Column('omschrijving', String))
 
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("maakCluster(keuze=%s,momschr=%s): engine → %s", keuze, momschr, engine)
    con = engine.connect()
    
    logger.debug("maakCluster(keuze=%s,momschr=%s): con → %s", keuze, momschr, con)
    selcllast = select([iclusters]).where(iclusters.c.iclusterID.like(keuze+'%')).order_by(iclusters.c.iclusterID.desc())
    rpcllast = con.execute(selcllast).first()
    logger.debug("maakCluster(keuze=%s,momschr=%s): selcllast → %s", keuze, momschr, selcllast)
    if rpcllast:
        mclusternr = keuze+('00000'+str(int(rpcllast[0][2:7])+1))[-5:]
        logger.debug("maakCluster(keuze=%s,momschr=%s): rpcllast → %s", keuze, momschr, rpcllast)
    else:
        mclusternr = keuze+'00001'
        logger.debug("maakCluster(keuze=%s,momschr=%s): mclusternr → %s", keuze, momschr, mclusternr)
  
    inscl = insert(iclusters).values(iclusterID = mclusternr, omschrijving = momschr)
    if mclusternr:       
        con.execute(inscl)
        logger.debug("maakCluster(keuze=%s,momschr=%s): inscl → %s", keuze, momschr, inscl)
        insGelukt(mclusternr, momschr)
    else:
        logger.debug("<<< Exiting maakCluster(keuze=%s,momschr=%s)", keuze, momschr)
        insMislukt()