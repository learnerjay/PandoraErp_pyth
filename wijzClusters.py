from login import hoofdMenu
from PyQt5.QtCore import Qt, QAbstractTableModel, QRegExp
from PyQt5.QtGui import QFont, QPixmap, QRegExpValidator, QIcon
from PyQt5.QtWidgets import QWidget, QTableView, QDialog, QLabel,\
       QGridLayout, QPushButton, QMessageBox, QLineEdit, QComboBox
from sqlalchemy import (Table, Column, Integer, String, Float, MetaData,\
                         create_engine, select, update)
import logging
logger = logging.getLogger(__name__)

def refresh(keuze, m_email, self):
    logger.debug(">>> Entering refresh(keuze=%s,m_email=%s)", keuze, m_email)
    self.close()
    toonClusters(keuze, m_email)
    logger.debug("<<< Exiting refresh(keuze=%s,m_email=%s)", keuze, m_email)
    
def updateOK():
    logger.debug(">>> Entering updateOK()")
    msg = QMessageBox()
    logger.debug("updateOK(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Information)
    msg.setText('Your data have been adjusted!')
    msg.setWindowTitle('Modify clusters')
    logger.debug("<<< Exiting updateOK()")
    msg.exec_()

def invoerOK():
    logger.debug(">>> Entering invoerOK()")
    msg = QMessageBox()
    logger.debug("invoerOK(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Information)
    msg.setText('Insert successful!')
    msg.setWindowTitle('Modify clusters')
    logger.debug("<<< Exiting invoerOK()")
    msg.exec_()
    
def calcBestaat():
    logger.debug(">>> Entering calcBestaat()")
    msg = QMessageBox()
    logger.debug("calcBestaat(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Information)
    msg.setText('Calculation line already exists\nen is settled with\nentered quantity!')
    msg.setWindowTitle('Modify clusters')
    logger.debug("<<< Exiting calcBestaat()")
    msg.exec_()   

def windowSluit(self, m_email):
    logger.debug(">>> Entering windowSluit(m_email=%s)", m_email)
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email)
    
def geenRecord():
    logger.debug(">>> Entering geenRecord()")
    msg = QMessageBox()
    logger.debug("geenRecord(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('No cluster found\ncreate another selection\nof create a new cluster please!')
    msg.setFont(QFont("Arial",10))
    msg.setWindowTitle('Modify clusters')
    logger.debug("<<< Exiting geenRecord()")
    msg.exec_() 
    
def ongKeuze():
    logger.debug(">>> Entering ongKeuze()")
    msg = QMessageBox()
    logger.debug("ongKeuze(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Invalid choice!')
    msg.setWindowTitle('Modify clusters')
    logger.debug("<<< Exiting ongKeuze()")
    msg.exec_() 
                
def zoeken(m_email):
    logger.debug(">>> Entering zoeken(m_email=%s)", m_email)
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.debug(">>> Entering __init__(parent=%s)", parent)
            self.setWindowTitle("Cluster selektion")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
                              
            self.Keuze = QLabel()
            logger.debug("__init__(parent=%s): self.Keuze → %s", parent, self.Keuze)
            k0Edit = QComboBox()
            logger.debug("__init__(self=%s,parent=%s): k0Edit → %s", self, parent, k0Edit)
            logger.debug("__init__(parent=%s): k0Edit → %s", parent, k0Edit)
            k0Edit.setFixedWidth(400)
            k0Edit.setFont(QFont("Arial",10))
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.addItem('                    Cluster Groups Sort Key')
            k0Edit.addItem('0. All clusters')
            k0Edit.addItem('AA-AL. Rails + welding assets')
            k0Edit.addItem('BA-BK. Beams + mounting')
            k0Edit.addItem('CA-CK. Level crossing + level crossing protection')
            k0Edit.addItem('DA-DK. Crushed stone + earth moving')
            k0Edit.addItem('EA-EK. Switch + track constructions')
            k0Edit.addItem('FA-FK. Underground infrastructure')
            k0Edit.addItem('GA-GK. Train control + signals')
            k0Edit.addItem('HA-HK. OCL + support structure')
            k0Edit.addItem('JA-JK. Power supplies + substations')
            k0Edit.activated[str].connect(self.k0Changed)
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap)

            grid = QGridLayout()
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid)
            logger.debug("__init__(parent=%s): grid → %s", parent, grid)
            grid.setSpacing(20)
                          
            lbl = QLabel()
            logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl)
            logger.debug("__init__(parent=%s): lbl → %s", parent, lbl)
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap)
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 0, 0, 1, 2)
                        
            grid.addWidget(k0Edit, 1, 1)
            
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 3, 0, 1, 2, Qt.AlignCenter)
            
            logo = QLabel()
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo)
            logger.debug("__init__(parent=%s): logo → %s", parent, logo)
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 1, 1, 1, Qt.AlignRight)
   
            applyBtn = QPushButton('Search')
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn)
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn)
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 2, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            cancelBtn = QPushButton('Close')
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn)
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn)
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
    
            grid.addWidget(cancelBtn, 2, 1, 1, 1,Qt.AlignCenter)
            logger.debug("<<< Exiting __init__(parent=%s)", parent)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
            logger.debug(">>> Entering __init__(data_list=%s,header=%s)", data_list, header)
            logger.debug("__init__(data_list=%s,header=%s): font → %s", data_list, header, font)
            logger.debug("__init__(data_list=%s,header=%s): table_view → %s", data_list, header, table_view)
            logger.debug("__init__(data_list=%s,header=%s): grid → %s", data_list, header, grid)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): grid → %s", self, data_list, header, grid)
            logger.debug("__init__(data_list=%s,header=%s): table_model → %s", data_list, header, table_model)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): table_model → %s", self, data_list, header, table_model)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): table_view → %s", self, data_list, header, table_view)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): font → %s", self, data_list, header, font)
            logger.debug("__init__(data_list=%s,header=%s): pixmap → %s", data_list, header, pixmap)
            logger.debug("__init__(data_list=%s,header=%s): lbl → %s", data_list, header, lbl)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): lbl → %s", self, data_list, header, lbl)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): pixmap → %s", self, data_list, header, pixmap)
            logger.debug("__init__(data_list=%s,header=%s): logo → %s", data_list, header, logo)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): logo → %s", self, data_list, header, logo)
            logger.debug("__init__(data_list=%s,header=%s): freshBtn → %s", data_list, header, freshBtn)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): freshBtn → %s", self, data_list, header, freshBtn)
            logger.debug("__init__(data_list=%s,header=%s): sluitBtn → %s", data_list, header, sluitBtn)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): sluitBtn → %s", self, data_list, header, sluitBtn)
            logger.debug("<<< Exiting __init__(data_list=%s,header=%s)", data_list, header)
           
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
            dialog = Widget(parent)
            dialog.exec_()
            logger.debug(">>> Entering getData(parent=%s)", parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog)
            logger.debug("<<< Exiting getData(parent=%s)", parent)
            return [dialog.returnk0()]       

    window = Widget()
    data = window.getData()
    keuze = ''
    if not data[0]:
        ongKeuze()
        zoeken(m_email)
    elif data[0][0] == '0':
        keuze = ''
    elif data[0]:
        keuze = data[0][0]
    toonClusters(keuze, m_email)  
  
def toonClusters(keuze, m_email):              
    logger.debug(">>> Entering toonClusters(keuze=%s,m_email=%s)", keuze, m_email)
    class MyWindow(QDialog):
        def __init__(self, data_list, header, *args):
            QWidget.__init__(self, *args,)
            self.setWindowTitle('Cluster Calculation')
            self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
            self.setWindowFlags(self.windowFlags()| Qt.WindowSystemMenuHint |
                              Qt.WindowMinMaxButtonsHint)
            self.setFont(QFont('Arial', 10))
            
            grid = QGridLayout()
            grid.setSpacing(20)
            
            table_model = MyTableModel(self, data_list, header)
            table_view = QTableView()
            table_view.setModel(table_model)
            font = QFont("Arial", 10)
            table_view.setFont(font)
            table_view.resizeColumnsToContents()
            table_view.hideColumn(31)
            table_view.hideColumn(32)
            table_view.hideColumn(33)
            table_view.hideColumn(34)
            table_view.hideColumn(35)
            table_view.hideColumn(36)
            table_view.hideColumn(37)
            table_view.setSelectionBehavior(QTableView.SelectRows)
            table_view.clicked.connect(showSelection)
            grid.addWidget(table_view, 0, 0, 1, 16)
            
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl, 1, 0, 1, 2)
       
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 1, 15, 1, 1, Qt.AlignRight)
            
            freshBtn = QPushButton('Refresh')
            freshBtn.clicked.connect(lambda: refresh(keuze, m_email, self))

            freshBtn.setFont(QFont("Arial",10))
            freshBtn.setFixedWidth(100) 
            freshBtn.setStyleSheet("color: black;  background-color: gainsboro")
   
            grid.addWidget(freshBtn, 1, 14, 1, 1, Qt.AlignRight)
        
            sluitBtn = QPushButton('Close')
            sluitBtn.clicked.connect(self.close)

            sluitBtn.setFont(QFont("Arial",10))
            sluitBtn.setFixedWidth(100) 
            sluitBtn.setStyleSheet("color: black;  background-color: gainsboro") 
            
            grid.addWidget(sluitBtn, 1, 13, 1, 1, Qt.AlignRight)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 1, 0, 1, 16, Qt.AlignCenter)
            
            self.setLayout(grid)
            self.setGeometry(50, 50, 1800, 900)
            self.setLayout(grid)
            logger.debug(">>> Entering __init__(parent=%s,mylist=%s,header=%s)", parent, mylist, header)
            logger.debug("<<< Exiting __init__(parent=%s,mylist=%s,header=%s)", parent, mylist, header)
            logger.debug("__init__(self=%s,parent=%s,mylist=%s,header=%s): self.mylist → %s", self, parent, mylist, header, self.mylist)

    class MyTableModel(QAbstractTableModel):
        def __init__(self, parent, mylist, header, *args):
            logger.debug("__init__(self=%s,parent=%s,mylist=%s,header=%s): self.header → %s", self, parent, mylist, header, self.header)
            QAbstractTableModel.__init__(self, parent, *args)
            self.mylist = mylist
            logger.debug(">>> Entering __init__()")
            logger.debug("__init__(): input_validator → %s", input_validator)
            logger.debug("__init__(): grid → %s", grid)
            logger.debug("__init__(self=%s): grid → %s", self, grid)
            logger.debug("__init__(): q1Edit → %s", q1Edit)
            logger.debug("__init__(): self.Omschrijving → %s", self.Omschrijving)
            logger.debug("__init__(self=%s): q1Edit → %s", self, q1Edit)
            logger.debug("__init__(): reg_ex → %s", reg_ex)
            logger.debug("__init__(self=%s): reg_ex → %s", self, reg_ex)
            logger.debug("__init__(self=%s): input_validator → %s", self, input_validator)
            logger.debug("__init__(): q2Edit → %s", q2Edit)
            logger.debug("__init__(): self.Prijs → %s", self.Prijs)
            logger.debug("__init__(self=%s): q2Edit → %s", self, q2Edit)
            logger.debug("__init__(): q3Edit → %s", q3Edit)
            logger.debug("__init__(): self.Eenheid → %s", self.Eenheid)
            logger.debug("__init__(self=%s): q3Edit → %s", self, q3Edit)
            logger.debug("__init__(): q4Edit → %s", q4Edit)
            logger.debug("__init__(): self.Materialen → %s", self.Materialen)
            logger.debug("__init__(self=%s): q4Edit → %s", self, q4Edit)
            logger.debug("__init__(): q5Edit → %s", q5Edit)
            logger.debug("__init__(): self.Lonen → %s", self.Lonen)
            logger.debug("__init__(self=%s): q5Edit → %s", self, q5Edit)
            logger.debug("__init__(): q6Edit → %s", q6Edit)
            logger.debug("__init__(): self.Diensten → %s", self.Diensten)
            logger.debug("__init__(self=%s): q6Edit → %s", self, q6Edit)
            logger.debug("__init__(): q7Edit → %s", q7Edit)
            logger.debug("__init__(self=%s): q7Edit → %s", self, q7Edit)
            logger.debug("__init__(): q8Edit → %s", q8Edit)
            logger.debug("__init__(): self.Inhuur → %s", self.Inhuur)
            logger.debug("__init__(self=%s): q8Edit → %s", self, q8Edit)
            logger.debug("__init__(): q9Edit → %s", q9Edit)
            logger.debug("__init__(): self.Construktieuren → %s", self.Construktieuren)
            logger.debug("__init__(self=%s): q9Edit → %s", self, q9Edit)
            logger.debug("__init__(): q10Edit → %s", q10Edit)
            logger.debug("__init__(): self.Montageuren → %s", self.Montageuren)
            logger.debug("__init__(self=%s): q10Edit → %s", self, q10Edit)
            logger.debug("__init__(): q11Edit → %s", q11Edit)
            logger.debug("__init__(): self.Retourlasuren → %s", self.Retourlasuren)
            logger.debug("__init__(self=%s): q11Edit → %s", self, q11Edit)
            logger.debug("__init__(): q12Edit → %s", q12Edit)
            logger.debug("__init__(): self.BFIuren → %s", self.BFIuren)
            logger.debug("__init__(self=%s): q12Edit → %s", self, q12Edit)
            logger.debug("__init__(): q29Edit → %s", q29Edit)
            logger.debug("__init__(): self.Telecomuren → %s", self.Telecomuren)
            logger.debug("__init__(self=%s): q29Edit → %s", self, q29Edit)
            logger.debug("__init__(): self.Voedinguren → %s", self.Voedinguren)
            logger.debug("__init__(self=%s): q13Edit → %s", self, q13Edit)
            logger.debug("__init__(): q13Edit → %s", q13Edit)
            logger.debug("__init__(): self.Bvluren → %s", self.Bvluren)
            logger.debug("__init__(self=%s): q14Edit → %s", self, q14Edit)
            logger.debug("__init__(): q14Edit → %s", q14Edit)
            logger.debug("__init__(): self.Spoorleguren → %s", self.Spoorleguren)
            logger.debug("__init__(self=%s): q15Edit → %s", self, q15Edit)
            logger.debug("__init__(): q15Edit → %s", q15Edit)
            logger.debug("__init__(): self.Spoorlasuren → %s", self.Spoorlasuren)
            logger.debug("__init__(self=%s): q16Edit → %s", self, q16Edit)
            logger.debug("__init__(): q16Edit → %s", q16Edit)
            logger.debug("__init__(): self.Inhuururen → %s", self.Inhuururen)
            logger.debug("__init__(self=%s): q17Edit → %s", self, q17Edit)
            logger.debug("__init__(): q17Edit → %s", q17Edit)
            logger.debug("__init__(): self.Sleuvengraver → %s", self.Sleuvengraver)
            logger.debug("__init__(self=%s): q18Edit → %s", self, q18Edit)
            logger.debug("__init__(): q18Edit → %s", q18Edit)
            logger.debug("__init__(): self.Persapparaat → %s", self.Persapparaat)
            logger.debug("__init__(self=%s): q19Edit → %s", self, q19Edit)
            logger.debug("__init__(): q19Edit → %s", q19Edit)
            logger.debug("__init__(): self.Atlaskraan → %s", self.Atlaskraan)
            logger.debug("__init__(self=%s): q20Edit → %s", self, q20Edit)
            logger.debug("__init__(): q20Edit → %s", q20Edit)
            logger.debug("__init__(): self.Kraan_groot → %s", self.Kraan_groot)
            logger.debug("__init__(self=%s): q21Edit → %s", self, q21Edit)
            logger.debug("__init__(): q21Edit → %s", q21Edit)
            logger.debug("__init__(): self.Mainliner → %s", self.Mainliner)
            logger.debug("__init__(self=%s): q22Edit → %s", self, q22Edit)
            logger.debug("__init__(): q22Edit → %s", q22Edit)
            logger.debug("__init__(): self.Hormachine → %s", self.Hormachine)
            logger.debug("__init__(self=%s): q23Edit → %s", self, q23Edit)
            logger.debug("__init__(): q23Edit → %s", q23Edit)
            logger.debug("__init__(): self.Wagon → %s", self.Wagon)
            logger.debug("__init__(self=%s): q24Edit → %s", self, q24Edit)
            logger.debug("__init__(): q24Edit → %s", q24Edit)
            logger.debug("__init__(): self.Locomotor → %s", self.Locomotor)
            logger.debug("__init__(self=%s): q25Edit → %s", self, q25Edit)
            logger.debug("__init__(): q25Edit → %s", q25Edit)
            logger.debug("__init__(): self.Locomotief → %s", self.Locomotief)
            logger.debug("__init__(self=%s): q26Edit → %s", self, q26Edit)
            logger.debug("__init__(): q26Edit → %s", q26Edit)
            logger.debug("__init__(): self.Stormobiel → %s", self.Stormobiel)
            logger.debug("__init__(self=%s): q27Edit → %s", self, q27Edit)
            logger.debug("__init__(): q27Edit → %s", q27Edit)
            logger.debug("__init__(): self.Montagewagen → %s", self.Montagewagen)
            logger.debug("__init__(self=%s): q28Edit → %s", self, q28Edit)
            logger.debug("__init__(): q28Edit → %s", q28Edit)
            logger.debug("__init__(): self.Robeltrein → %s", self.Robeltrein)
            logger.debug("__init__(self=%s): q30Edit → %s", self, q30Edit)
            logger.debug("__init__(): q30Edit → %s", q30Edit)
            logger.debug("__init__(): self.Leiding → %s", self.Leiding)
            logger.debug("__init__(self=%s): q31Edit → %s", self, q31Edit)
            logger.debug("__init__(): q31Edit → %s", q31Edit)
            logger.debug("__init__(): self.Huisvesting → %s", self.Huisvesting)
            logger.debug("__init__(self=%s): q32Edit → %s", self, q32Edit)
            logger.debug("__init__(): q32Edit → %s", q32Edit)
            logger.debug("__init__(): self.Kabelwerk → %s", self.Kabelwerk)
            logger.debug("__init__(self=%s): q33Edit → %s", self, q33Edit)
            logger.debug("__init__(): q33Edit → %s", q33Edit)
            logger.debug("__init__(): self.Grondverzet → %s", self.Grondverzet)
            logger.debug("__init__(self=%s): q34Edit → %s", self, q34Edit)
            logger.debug("__init__(): q34Edit → %s", q34Edit)
            logger.debug("__init__(): self.Betonwerk → %s", self.Betonwerk)
            logger.debug("__init__(self=%s): q35Edit → %s", self, q35Edit)
            logger.debug("__init__(): q35Edit → %s", q35Edit)
            logger.debug("__init__(): self.Vervoer → %s", self.Vervoer)
            logger.debug("__init__(self=%s): q36Edit → %s", self, q36Edit)
            logger.debug("__init__(): q36Edit → %s", q36Edit)
            logger.debug("__init__(): self.Overig → %s", self.Overig)
            logger.debug("__init__(self=%s): q37Edit → %s", self, q37Edit)
            logger.debug("__init__(): q37Edit → %s", q37Edit)
            logger.debug("__init__(self=%s): lbl1 → %s", self, lbl1)
            logger.debug("__init__(): lbl1 → %s", lbl1)
            logger.debug("__init__(self=%s): lbl2 → %s", self, lbl2)
            logger.debug("__init__(): lbl2 → %s", lbl2)
            logger.debug("__init__(self=%s): lbl3 → %s", self, lbl3)
            logger.debug("__init__(): lbl3 → %s", lbl3)
            logger.debug("__init__(self=%s): lbl4 → %s", self, lbl4)
            logger.debug("__init__(): lbl4 → %s", lbl4)
            logger.debug("__init__(self=%s): lbl5 → %s", self, lbl5)
            logger.debug("__init__(): lbl5 → %s", lbl5)
            logger.debug("__init__(self=%s): lbl6 → %s", self, lbl6)
            logger.debug("__init__(): lbl6 → %s", lbl6)
            logger.debug("__init__(self=%s): lbl7 → %s", self, lbl7)
            logger.debug("__init__(): lbl7 → %s", lbl7)
            logger.debug("__init__(self=%s): lbl8 → %s", self, lbl8)
            logger.debug("__init__(): lbl8 → %s", lbl8)
            logger.debug("__init__(self=%s): lbl9 → %s", self, lbl9)
            logger.debug("__init__(): lbl9 → %s", lbl9)
            logger.debug("__init__(self=%s): lbl10 → %s", self, lbl10)
            logger.debug("__init__(): lbl10 → %s", lbl10)
            logger.debug("__init__(): lbl20 → %s", lbl20)
            logger.debug("__init__(self=%s): lbl20 → %s", self, lbl20)
            logger.debug("__init__(): lbl21 → %s", lbl21)
            logger.debug("__init__(self=%s): lbl21 → %s", self, lbl21)
            logger.debug("__init__(): lbl22 → %s", lbl22)
            logger.debug("__init__(self=%s): lbl22 → %s", self, lbl22)
            logger.debug("__init__(): lbl23 → %s", lbl23)
            logger.debug("__init__(self=%s): lbl23 → %s", self, lbl23)
            logger.debug("__init__(): lbl24 → %s", lbl24)
            logger.debug("__init__(self=%s): lbl24 → %s", self, lbl24)
            logger.debug("__init__(): lbl25 → %s", lbl25)
            logger.debug("__init__(self=%s): lbl25 → %s", self, lbl25)
            logger.debug("__init__(): lbl26 → %s", lbl26)
            logger.debug("__init__(self=%s): lbl26 → %s", self, lbl26)
            logger.debug("__init__(): lbl27 → %s", lbl27)
            logger.debug("__init__(self=%s): lbl27 → %s", self, lbl27)
            logger.debug("__init__(): lbl28 → %s", lbl28)
            logger.debug("__init__(self=%s): lbl28 → %s", self, lbl28)
            logger.debug("__init__(): lbl29 → %s", lbl29)
            logger.debug("__init__(self=%s): lbl29 → %s", self, lbl29)
            logger.debug("__init__(): lbl30 → %s", lbl30)
            logger.debug("__init__(self=%s): lbl30 → %s", self, lbl30)
            logger.debug("__init__(): lbl31 → %s", lbl31)
            logger.debug("__init__(self=%s): lbl31 → %s", self, lbl31)
            logger.debug("__init__(): lbl19 → %s", lbl19)
            logger.debug("__init__(self=%s): lbl19 → %s", self, lbl19)
            logger.debug("__init__(): lbl11 → %s", lbl11)
            logger.debug("__init__(self=%s): lbl11 → %s", self, lbl11)
            logger.debug("__init__(): lbl12 → %s", lbl12)
            logger.debug("__init__(self=%s): lbl12 → %s", self, lbl12)
            logger.debug("__init__(): lbl13 → %s", lbl13)
            logger.debug("__init__(self=%s): lbl13 → %s", self, lbl13)
            logger.debug("__init__(): lbl14 → %s", lbl14)
            logger.debug("__init__(self=%s): lbl14 → %s", self, lbl14)
            logger.debug("__init__(): lbl15 → %s", lbl15)
            logger.debug("__init__(self=%s): lbl15 → %s", self, lbl15)
            logger.debug("__init__(): lbl16 → %s", lbl16)
            logger.debug("__init__(self=%s): lbl16 → %s", self, lbl16)
            logger.debug("__init__(): lbl17 → %s", lbl17)
            logger.debug("__init__(self=%s): lbl17 → %s", self, lbl17)
            logger.debug("__init__(): lbl18 → %s", lbl18)
            logger.debug("__init__(self=%s): lbl18 → %s", self, lbl18)
            logger.debug("__init__(): pixmap → %s", pixmap)
            logger.debug("__init__(): lbl → %s", lbl)
            logger.debug("__init__(self=%s): lbl → %s", self, lbl)
            logger.debug("__init__(self=%s): pixmap → %s", self, pixmap)
            logger.debug("__init__(): logo → %s", logo)
            logger.debug("__init__(self=%s): logo → %s", self, logo)
            logger.debug("__init__(): applyBtn → %s", applyBtn)
            logger.debug("__init__(self=%s): applyBtn → %s", self, applyBtn)
            logger.debug("__init__(): closeBtn → %s", closeBtn)
            logger.debug("__init__(self=%s): closeBtn → %s", self, closeBtn)
            logger.debug("<<< Exiting __init__()")
            self.header = header
        def rowCount(self, parent):
            logger.debug(">>> Entering rowCount(parent=%s)", parent)
            return len(self.mylist)
        def columnCount(self, parent):
            logger.debug(">>> Entering columnCount(parent=%s)", parent)
            return len(self.mylist[0])
        def data(self, index, role):
            logger.debug(">>> Entering data(index=%s,role=%s)", index, role)
            veld = self.mylist[index.row()][index.column()]
            logger.debug("data(index=%s,role=%s): veld → %s", index, role, veld)
            logger.debug("data(self=%s,index=%s,role=%s): veld → %s", self, index, role, veld)
            if not index.isValid():
                return None
            elif role == Qt.TextAlignmentRole and (type(veld) == float or type(veld) == int):
                return Qt.AlignRight | Qt.AlignVCenter
            elif role != Qt.DisplayRole:
                return None
            if type(veld) == float:
                return '{:12.2f}'.format(veld)
            else:
                logger.debug("<<< Exiting data(index=%s,role=%s)", index, role)
                return veld
        def headerData(self, col, orientation, role):
            logger.debug(">>> Entering headerData(col=%s,orientation=%s,role=%s)", col, orientation, role)
            if orientation == Qt.Horizontal and role == Qt.DisplayRole:
                return self.header[col]
            logger.debug("<<< Exiting headerData(col=%s,orientation=%s,role=%s)", col, orientation, role)
            return None
             
    header = ['Cluster number', 'Description', 'Price', 'Unit', 'Materials', 'Wages',\
              'Services', 'Equipment', 'Hiring', 'hours\nconstruction', 'hours mounting','hours\nreturn welding',\
              'hours\nchief mechanic', 'hours\npower-supply', 'hours\nOCL', 'hours\ntrack laying', 'hours\ntrack welding',\
              'hours\nhiring', 'Trencher', 'Press machine', 'Atlas crane',\
              'Crane big', 'Mainliner', 'Ballast scrape\nmachine', 'Wagon', 'Locomotor',\
              'Locomotive', 'Assembly\ntrolley', 'Stormobiel', 'hours\ntelecom', 'Robel train',\
              '', '', '', '', '', '', '']
    
    metadata = MetaData()
    clusters = Table('clusters', metadata,
        Column('clusterID', String, primary_key=True),
        Column('omschrijving', String),
        Column('prijs', Float),
        Column('eenheid', String),
        Column('materialen', Float),
        Column('lonen', Float),
        Column('diensten', Float),
        Column('materieel', Float),
        Column('inhuur', Float),
        Column('uren_constr', Float),
        Column('uren_mont', Float),
        Column('uren_retourlas', Float),
        Column('uren_bfi', Float),
        Column('uren_voeding', Float),
        Column('uren_bvl', Float),
        Column('uren_spoorleg', Float),
        Column('uren_spoorlas', Float),
        Column('uren_inhuur', Float),
        Column('sleuvengraver', Float),
        Column('persapparaat', Float),
        Column('atlaskraan', Float),
        Column('kraan_groot', Float),
        Column('mainliner', Float),
        Column('hormachine', Float),
        Column('wagon', Float),
        Column('locomotor', Float),
        Column('locomotief', Float),
        Column('montagewagen', Float),
        Column('stormobiel', Float),
        Column('uren_telecom', Float),
        Column('robeltrein', Float),
        Column('leiding', Float),
        Column('huisvesting', Float),
        Column('kabelwerk', Float),
        Column('grondverzet', Float),
        Column('betonwerk', Float),
        Column('vervoer', Float),
        Column('overig', Float))
       
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
        
    sel = select([clusters]).where(clusters.c.clusterID.ilike(keuze+'%'))\
                              .order_by(clusters.c.clusterID)

    if con.execute(sel).fetchone():
        rp = con.execute(sel)
    else:
        geenRecord()
        zoeken(m_email)
      
    data_list=[]
    for row in rp:
        data_list += [(row)]

    def showSelection(idx):
        logger.debug(">>> Entering showSelection(idx=%s)", idx)
        clusternr = idx.data()
        logger.debug("showSelection(idx=%s): clusternr → %s", idx, clusternr)
        if idx.column() == 0:
            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            logger.debug("showSelection(idx=%s): engine → %s", idx, engine)
            con = engine.connect()
            selcl = select([clusters]).where(clusters.c.clusterID == clusternr)
            logger.debug("showSelection(idx=%s): con → %s", idx, con)
            rpsel = con.execute(selcl).first()
            
            logger.debug("showSelection(idx=%s): selcl → %s", idx, selcl)
            logger.debug("showSelection(idx=%s): rpsel → %s", idx, rpsel)
            class MainWindow(QDialog):
                def __init__(self):
                    logger.debug("<<< Exiting showSelection(idx=%s)", idx)
                    QDialog.__init__(self)
                    
                    grid = QGridLayout()
                    grid.setSpacing(20)
                    self.setWindowTitle("Modify Cluster")
                    self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
                    
                    self.setFont(QFont('Arial', 10))   
                    
                    self.Omschrijving = QLabel()
                    q1Edit = QLineEdit(rpsel[1])
                    q1Edit.setFont(QFont("Arial",10))
                    q1Edit.textChanged.connect(self.q1Changed) 
                    reg_ex = QRegExp("^.{0,49}$")
                    input_validator = QRegExpValidator(reg_ex, q1Edit)
                    q1Edit.setValidator(input_validator)
                                    
                    self.Prijs = QLabel()
                    q2Edit = QLineEdit(('{:12.2f}'.format(rpsel[2])))
                    q2Edit.setFixedWidth(150)
                    q2Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q2Edit.setAlignment(Qt.AlignRight)
                    q2Edit.setDisabled(True)
                     
                    self.Eenheid = QLabel()
                    q3Edit = QLineEdit(str(rpsel[3]))
                    q3Edit.setFixedWidth(150)
                    q3Edit.setFont(QFont("Arial",10))
                    q3Edit.textChanged.connect(self.q3Changed) 
                    reg_ex = QRegExp("^.{0,10}$")
                    input_validator = QRegExpValidator(reg_ex, q3Edit)
                    q3Edit.setValidator(input_validator)
                    
                    self.Materialen = QLabel()
                    q4Edit = QLineEdit('{:12.2f}'.format(rpsel[4]))
                    q4Edit.setFixedWidth(150)
                    q4Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q4Edit.setAlignment(Qt.AlignRight)
                    q4Edit.setDisabled(True)
                    
                    self.Lonen = QLabel()
                    q5Edit = QLineEdit('{:12.2f}'.format(rpsel[5]))
                    q5Edit.setFixedWidth(150)
                    q5Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q5Edit.setAlignment(Qt.AlignRight)
                    q5Edit.setDisabled(True)
                    
                    self.Diensten = QLabel()
                    q6Edit = QLineEdit('{:12.2f}'.format(rpsel[6]))
                    q6Edit.setFixedWidth(150)
                    q6Edit.setAlignment(Qt.AlignRight)
                    q6Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q6Edit.setDisabled(True)
                    
                    self.Materiëel = QLabel()
                    q7Edit = QLineEdit('{:12.2f}'.format(rpsel[7]))
                    q7Edit.setFixedWidth(150)
                    q7Edit.setAlignment(Qt.AlignRight)
                    q7Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q7Edit.setValidator(input_validator)
                    q7Edit.setDisabled(True)
                    
                    self.Inhuur = QLabel()
                    q8Edit = QLineEdit('{:12.2f}'.format(rpsel[8]))
                    q8Edit.setFixedWidth(150)
                    q8Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q8Edit.setAlignment(Qt.AlignRight)
                    q8Edit.setDisabled(True)
                                   
                    self.Construktieuren = QLabel()
                    q9Edit = QLineEdit(str(round(float(rpsel[9]),2)))
                    q9Edit.setFixedWidth(150)
                    q9Edit.setFont(QFont("Arial",10))
                    q9Edit.setAlignment(Qt.AlignRight)
                    q9Edit.textChanged.connect(self.q9Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q9Edit)
                    q9Edit.setValidator(input_validator)
                    
                    self.Montageuren = QLabel()
                    q10Edit = QLineEdit(str(round(float(rpsel[10]),2)))
                    q10Edit.setFixedWidth(150)
                    q10Edit.setAlignment(Qt.AlignRight)
                    q10Edit.setFont(QFont("Arial",10))
                    q10Edit.textChanged.connect(self.q10Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q10Edit)
                    q10Edit.setValidator(input_validator)
                    
                    self.Retourlasuren = QLabel()
                    q11Edit = QLineEdit(str(round(float(rpsel[11]),2)))
                    q11Edit.setFixedWidth(150)
                    q11Edit.setAlignment(Qt.AlignRight)
                    q11Edit.setFont(QFont("Arial",10))
                    q11Edit.textChanged.connect(self.q11Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q11Edit)
                    q11Edit.setValidator(input_validator)
                    
                    self.BFIuren = QLabel()
                    q12Edit = QLineEdit(str(round(float(rpsel[12]),2)))
                    q12Edit.setFixedWidth(150)
                    q12Edit.setAlignment(Qt.AlignRight)
                    q12Edit.setFont(QFont("Arial",10))
                    q12Edit.textChanged.connect(self.q12Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q12Edit)
                    q12Edit.setValidator(input_validator)
                    
                    self.Telecomuren = QLabel()
                    q29Edit = QLineEdit(str(round(float(rpsel[29]),2)))
                    q29Edit.setFixedWidth(150)
                    q29Edit.setAlignment(Qt.AlignRight)
                    q29Edit.setFont(QFont("Arial",10))
                    q29Edit.textChanged.connect(self.q29Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q29Edit)
                    q29Edit.setValidator(input_validator)      
                         
                    self.Voedinguren = QLabel()
                    q13Edit = QLineEdit(str(round(float(rpsel[13]),2)))
                    q13Edit.setFixedWidth(150)
                    q13Edit.setAlignment(Qt.AlignRight)
                    q13Edit.setFont(QFont("Arial",10))
                    q13Edit.textChanged.connect(self.q13Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q13Edit)
                    q13Edit.setValidator(input_validator)
                    
                    self.Bvluren = QLabel()
                    q14Edit = QLineEdit(str(round(float(rpsel[14]),2)))
                    q14Edit.setFixedWidth(150)
                    q14Edit.setFont(QFont("Arial",10))
                    q14Edit.setAlignment(Qt.AlignRight)
                    q14Edit.textChanged.connect(self.q14Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q14Edit)
                    q14Edit.setValidator(input_validator)
                       
                    self.Spoorleguren = QLabel()
                    q15Edit = QLineEdit(str(round(float(rpsel[15]),2)))
                    q15Edit.setFixedWidth(150)
                    q15Edit.setAlignment(Qt.AlignRight)
                    q15Edit.setFont(QFont("Arial",10))
                    q15Edit.textChanged.connect(self.q15Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q15Edit)
                    q15Edit.setValidator(input_validator)
                    
                    self.Spoorlasuren = QLabel()
                    q16Edit = QLineEdit(str(round(float(rpsel[16]),2)))
                    q16Edit.setFixedWidth(150)
                    q16Edit.setAlignment(Qt.AlignRight)
                    q16Edit.setFont(QFont("Arial",10))
                    q16Edit.textChanged.connect(self.q16Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q16Edit)
                    q16Edit.setValidator(input_validator)
                    
                    self.Inhuururen = QLabel()
                    q17Edit = QLineEdit(str(round(float(rpsel[17]),2)))
                    q17Edit.setFixedWidth(150)
                    q17Edit.setAlignment(Qt.AlignRight)
                    q17Edit.setFont(QFont("Arial",10))
                    q17Edit.textChanged.connect(self.q17Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q17Edit)
                    q17Edit.setValidator(input_validator)
                       
                    self.Sleuvengraver = QLabel()
                    q18Edit = QLineEdit(str(round(float(rpsel[18]),2)))
                    q18Edit.setFixedWidth(150)
                    q18Edit.setAlignment(Qt.AlignRight)
                    q18Edit.setFont(QFont("Arial",10))
                    q18Edit.textChanged.connect(self.q18Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q18Edit)
                    q18Edit.setValidator(input_validator)
                            
                    self.Persapparaat = QLabel()
                    q19Edit = QLineEdit(str(round(float(rpsel[19]),2)))
                    q19Edit.setFixedWidth(150)
                    q19Edit.setAlignment(Qt.AlignRight)
                    q19Edit.setFont(QFont("Arial",10))
                    q19Edit.textChanged.connect(self.q19Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q19Edit)
                    q19Edit.setValidator(input_validator)
                    
                    self.Atlaskraan = QLabel()
                    q20Edit = QLineEdit(str(round(float(rpsel[20]),2)))
                    q20Edit.setFixedWidth(150)
                    q20Edit.setFont(QFont("Arial",10))
                    q20Edit.setAlignment(Qt.AlignRight)
                    q20Edit.textChanged.connect(self.q20Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q20Edit)
                    q20Edit.setValidator(input_validator)
                    
                    self.Kraan_groot = QLabel()
                    q21Edit = QLineEdit(str(round(float(rpsel[21]),2)))
                    q21Edit.setFixedWidth(150)
                    q21Edit.setFont(QFont("Arial",10))
                    q21Edit.setAlignment(Qt.AlignRight)
                    q21Edit.textChanged.connect(self.q21Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q21Edit)
                    q21Edit.setValidator(input_validator)
                    
                    self.Mainliner = QLabel()
                    q22Edit = QLineEdit(str(round(float(rpsel[22]),2)))
                    q22Edit.setFixedWidth(150)
                    q22Edit.setFont(QFont("Arial",10))
                    q22Edit.setAlignment(Qt.AlignRight)
                    q22Edit.textChanged.connect(self.q22Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q22Edit)
                    q22Edit.setValidator(input_validator)
                    
                    self.Hormachine = QLabel()
                    q23Edit = QLineEdit(str(round(float(rpsel[23]),2)))
                    q23Edit.setFixedWidth(150)
                    q23Edit.setAlignment(Qt.AlignRight)
                    q23Edit.setFont(QFont("Arial",10))
                    q23Edit.textChanged.connect(self.q23Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q23Edit)
                    q23Edit.setValidator(input_validator)
                    
                    self.Wagon = QLabel()
                    q24Edit = QLineEdit(str(round(float(rpsel[24]),2)))
                    q24Edit.setAlignment(Qt.AlignRight)
                    q24Edit.setFixedWidth(150)
                    q24Edit.setFont(QFont("Arial",10))
                    q24Edit.textChanged.connect(self.q24Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q24Edit)
                    q24Edit.setValidator(input_validator)
                    
                    self.Locomotor = QLabel()
                    q25Edit = QLineEdit(str(round(float(rpsel[25]),2)))
                    q25Edit.setFixedWidth(150)
                    q25Edit.setAlignment(Qt.AlignRight)
                    q25Edit.setFont(QFont("Arial",10))
                    q25Edit.textChanged.connect(self.q25Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q25Edit)
                    q25Edit.setValidator(input_validator)
        
                    self.Locomotief = QLabel()
                    q26Edit = QLineEdit(str(round(float(rpsel[26]),2)))
                    q26Edit.setFixedWidth(150)
                    q26Edit.setAlignment(Qt.AlignRight)
                    q26Edit.setFont(QFont("Arial",10))
                    q26Edit.textChanged.connect(self.q26Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q26Edit)
                    q26Edit.setValidator(input_validator)
                    
                    self.Stormobiel = QLabel()
                    q27Edit = QLineEdit(str(round(float(rpsel[27]),2)))
                    q27Edit.setFixedWidth(150)
                    q27Edit.setAlignment(Qt.AlignRight)
                    q27Edit.setFont(QFont("Arial",10))
                    q27Edit.textChanged.connect(self.q27Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q27Edit)
                    q27Edit.setValidator(input_validator)
                    
                    self.Montagewagen = QLabel()
                    q28Edit = QLineEdit(str(round(float(rpsel[28]),2)))
                    q28Edit.setFixedWidth(150)
                    q28Edit.setAlignment(Qt.AlignRight)
                    q28Edit.setFont(QFont("Arial",10))
                    q28Edit.textChanged.connect(self.q28Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q28Edit)
                    q28Edit.setValidator(input_validator)
                    
                    self.Robeltrein = QLabel()
                    q30Edit = QLineEdit(str(round(float(rpsel[30]),2)))
                    q30Edit.setFixedWidth(150)
                    q30Edit.setFont(QFont("Arial",10))
                    q30Edit.setAlignment(Qt.AlignRight)
                    q30Edit.textChanged.connect(self.q30Changed) 
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q30Edit)
                    q30Edit.setValidator(input_validator)
                    
                    self.Leiding = QLabel()
                    q31Edit = QLineEdit(str(round(float(rpsel[31]),2)))
                    q31Edit.setFixedWidth(150)
                    q31Edit.setFont(QFont("Arial",10))
                    q31Edit.setAlignment(Qt.AlignRight)

                    self.Huisvesting = QLabel()
                    q32Edit = QLineEdit(str(round(float(rpsel[32]),2)))
                    q32Edit.setFixedWidth(150)
                    q32Edit.setFont(QFont("Arial",10))
                    q32Edit.setAlignment(Qt.AlignRight)

                    self.Kabelwerk = QLabel()
                    q33Edit = QLineEdit(str(round(float(rpsel[33]),2)))
                    q33Edit.setFixedWidth(150)
                    q33Edit.setFont(QFont("Arial",10))
                    q33Edit.setAlignment(Qt.AlignRight)

                    self.Grondverzet = QLabel()
                    q34Edit = QLineEdit(str(round(float(rpsel[34]),2)))
                    q34Edit.setFixedWidth(150)
                    q34Edit.setFont(QFont("Arial",10))
                    q34Edit.setAlignment(Qt.AlignRight)

                    self.Betonwerk = QLabel()
                    q35Edit = QLineEdit(str(round(float(rpsel[35]),2)))
                    q35Edit.setFixedWidth(150)
                    q35Edit.setFont(QFont("Arial",10))
                    q35Edit.setAlignment(Qt.AlignRight)

                    self.Vervoer = QLabel()
                    q36Edit = QLineEdit(str(round(float(rpsel[36]),2)))
                    q36Edit.setFixedWidth(150)
                    q36Edit.setFont(QFont("Arial",10))
                    q36Edit.setAlignment(Qt.AlignRight)

                    self.Overig = QLabel()
                    q37Edit = QLineEdit(str(round(float(rpsel[37]),2)))
                    q37Edit.setFixedWidth(150)
                    q37Edit.setFont(QFont("Arial",10))
                    q37Edit.setAlignment(Qt.AlignRight)

                    grid = QGridLayout()
                    grid.setSpacing(10)
                    
                    lbl1 = QLabel('Cluster number')
                    lbl1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl1, 1, 0)
                    
                    lbl2 = QLabel(clusternr)
                    grid.addWidget(lbl2, 1, 1)
                           
                    lbl3 = QLabel('Description')
                    lbl3.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl3, 2, 0)
                    grid.addWidget(q1Edit, 2, 1, 1, 3) # RowSpan 1 ,ColumnSpan 3
                                                         
                    lbl4 = QLabel('Price')
                    lbl4.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl4, 3, 0)
                    grid.addWidget(q2Edit, 3, 1)
                    
                    lbl5 = QLabel('Unit')
                    lbl5.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl5, 4, 0)
                    grid.addWidget(q3Edit, 4, 1)
                    
                    lbl6 = QLabel('Materials')
                    lbl6.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl6, 5, 0)
                    grid.addWidget(q4Edit, 5, 1)
                    
                    lbl7 = QLabel('Wages')
                    lbl7.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl7, 6, 0)
                    grid.addWidget(q5Edit, 6, 1)
                    
                    lbl8 = QLabel('Services')
                    lbl8.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl8, 7, 0)
                    grid.addWidget(q6Edit, 7, 1)
                    
                    lbl9 = QLabel('Equipment')
                    lbl9.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl9, 8, 0)
                    grid.addWidget(q7Edit, 8, 1)
                    
                    lbl10 = QLabel('Hiring')
                    lbl10.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl10, 9, 0)
                    grid.addWidget(q8Edit, 9, 1)
                    
                    lbl20 = QLabel('Trenching hours')
                    lbl20.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl20, 10, 0)
                    grid.addWidget(q18Edit, 10, 1)
                      
                    lbl21 = QLabel('Pressing machine hours')
                    lbl21.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl21, 11, 0)
                    grid.addWidget(q19Edit, 11, 1)
                    
                    lbl22 = QLabel('Atlas crane hours')
                    lbl22.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl22, 12, 0)
                    grid.addWidget(q20Edit, 12, 1)
                    
                    lbl23 = QLabel('Crane big hours')
                    lbl23.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl23, 13, 0)
                    grid.addWidget(q21Edit, 13, 1)
                    
                    lbl24 = QLabel('Mainliner hours')
                    lbl24.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl24, 14, 0)
                    grid.addWidget(q22Edit, 14, 1)
                    
                    lbl25 = QLabel('Ballast clearing hours')
                    lbl25.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl25, 15, 0)
                    grid.addWidget(q23Edit, 15, 1)
                    
                    lbl26 = QLabel('Wagon hours')
                    lbl26.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl26, 16, 0)
                    grid.addWidget(q24Edit, 16, 1)
                    
                    lbl27 = QLabel('Locomotor hours')
                    lbl27.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl27, 3, 2)
                    grid.addWidget(q25Edit, 3, 3)
                    
                    lbl28 = QLabel('Locomotive hours')
                    lbl28.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl28, 4, 2)
                    grid.addWidget(q26Edit, 4, 3)
                    
                    lbl29 = QLabel('Stormobiel hours')
                    lbl29.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl29, 5, 2)
                    grid.addWidget(q27Edit, 5, 3)
                    
                    lbl30 = QLabel('Assembly trolley hours')
                    lbl30.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl30, 6, 2)
                    grid.addWidget(q28Edit, 6, 3)
                    
                    lbl31 = QLabel('Robel train hours')
                    lbl31.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl31, 7, 2)
                    grid.addWidget(q30Edit, 7, 3)
                    
                    lbl19 = QLabel('Hiring hours')
                    lbl19.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl19, 8, 2)
                    grid.addWidget(q17Edit, 8, 3)      
                    
                    lbl11 = QLabel('Construction hours')
                    lbl11.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl11, 9, 2)
                    grid.addWidget(q9Edit, 9, 3)
                        
                    lbl12 = QLabel('Mounting hours')
                    lbl12.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl12, 10, 2)
                    grid.addWidget(q10Edit, 10, 3)
                    
                    lbl13 = QLabel('Return welding hours')
                    lbl13.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl13, 11, 2)
                    grid.addWidget(q11Edit, 11, 3)
                    
                    lbl14 = QLabel('Chief mechanic hours')
                    lbl14.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl14, 12, 2)
                    grid.addWidget(q12Edit, 12, 3)
                    
                    lbl19 = QLabel('Telecom hours')
                    lbl19.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl19, 13, 2)
                    grid.addWidget(q29Edit, 13, 3)
                                                              
                    lbl15 = QLabel('Power-supply hours')
                    lbl15.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl15, 14, 2)
                    grid.addWidget(q13Edit, 14, 3)
                 
                    lbl16 = QLabel('OCL hours')
                    lbl16.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl16, 15, 2)
                    grid.addWidget(q14Edit, 15, 3)
                    
                    lbl17 = QLabel('Track laying hours')
                    lbl17.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl17, 16, 2)
                    grid.addWidget(q15Edit, 16, 3)
                    
                    lbl18 = QLabel('Track welding hours')
                    lbl18.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl18, 17, 2)
                    grid.addWidget(q16Edit, 17, 3)

                    lbl = QLabel()
                    pixmap = QPixmap('./images/logos/verbinding.jpg')
                    lbl.setPixmap(pixmap)
                    grid.addWidget(lbl, 0, 0, 1, 1, Qt.AlignRight)
                                     
                    logo = QLabel()
                    pixmap = QPixmap('./images/logos/logo.jpg')
                    logo.setPixmap(pixmap)
                    grid.addWidget(logo , 0, 3, 1 , 1, Qt.AlignRight)
                    
                    grid.addWidget(QLabel('Modify cluster'), 0, 1, 1, 2, Qt.AlignCenter)
                                                    
                    grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 22, 1, 1, 3)
                      
                    self.setLayout(grid)
                    self.setGeometry(400, 50, 150, 150)
            
                    applyBtn = QPushButton('Modify')
                    applyBtn.clicked.connect(self.accept)
            
                    grid.addWidget(applyBtn, 21, 3, 1, 1, Qt.AlignRight)
                    applyBtn.setFont(QFont("Arial",10))
                    applyBtn.setFixedWidth(100)
                    applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
                    
                    closeBtn = QPushButton('Close')
                    closeBtn.clicked.connect(self.close)
            
                    grid.addWidget(closeBtn, 21, 2, 1, 2, Qt.AlignCenter)
                    closeBtn.setFont(QFont("Arial",10))
                    closeBtn.setFixedWidth(100)
                    closeBtn.setStyleSheet("color: black;  background-color: gainsboro")
                                             
                def q1Changed(self,text):
                    logger.debug(">>> Entering q1Changed(text=%s)", text)
                    logger.debug("q1Changed(self=%s,text=%s): Omschrijving → %s", self, text, Omschrijving)
                    self.Omschrijving.setText(text)
                    logger.debug("<<< Exiting q1Changed(text=%s)", text)
            
                def q3Changed(self,text):
                    logger.debug(">>> Entering q3Changed(text=%s)", text)
                    logger.debug("q3Changed(self=%s,text=%s): Eenheid → %s", self, text, Eenheid)
                    self.Eenheid.setText(text)
                    logger.debug("<<< Exiting q3Changed(text=%s)", text)
                             
                def q9Changed(self,text):
                    logger.debug(">>> Entering q9Changed(text=%s)", text)
                    logger.debug("q9Changed(self=%s,text=%s): Construktieuren → %s", self, text, Construktieuren)
                    self.Construktieuren.setText(text)
                    logger.debug("<<< Exiting q9Changed(text=%s)", text)
                    
                def q10Changed(self,text):
                    logger.debug(">>> Entering q10Changed(text=%s)", text)
                    logger.debug("q10Changed(self=%s,text=%s): Montageuren → %s", self, text, Montageuren)
                    self.Montageuren.setText(text)
                    logger.debug("<<< Exiting q10Changed(text=%s)", text)
                       
                def q11Changed(self,text):
                    logger.debug(">>> Entering q11Changed(text=%s)", text)
                    logger.debug("q11Changed(self=%s,text=%s): Retourlasuren → %s", self, text, Retourlasuren)
                    self.Retourlasuren.setText(text)
                    logger.debug("<<< Exiting q11Changed(text=%s)", text)
                    
                def q12Changed(self,text):
                    logger.debug(">>> Entering q12Changed(text=%s)", text)
                    logger.debug("q12Changed(self=%s,text=%s): BFIuren → %s", self, text, BFIuren)
                    self.BFIuren.setText(text)
                    logger.debug("<<< Exiting q12Changed(text=%s)", text)
                    
                def q13Changed(self,text):
                    logger.debug(">>> Entering q13Changed(text=%s)", text)
                    logger.debug("q13Changed(self=%s,text=%s): Voedinguren → %s", self, text, Voedinguren)
                    self.Voedinguren.setText(text)
                    logger.debug("<<< Exiting q13Changed(text=%s)", text)
                    
                def q14Changed(self,text):
                    logger.debug(">>> Entering q14Changed(text=%s)", text)
                    logger.debug("q14Changed(self=%s,text=%s): Bvluren → %s", self, text, Bvluren)
                    self.Bvluren.setText(text)
                    logger.debug("<<< Exiting q14Changed(text=%s)", text)
                    
                def q15Changed(self,text):
                    logger.debug(">>> Entering q15Changed(text=%s)", text)
                    logger.debug("q15Changed(self=%s,text=%s): Spoorleguren → %s", self, text, Spoorleguren)
                    self.Spoorleguren.setText(text)
                    logger.debug("<<< Exiting q15Changed(text=%s)", text)
                    
                def q16Changed(self,text):
                    logger.debug(">>> Entering q16Changed(text=%s)", text)
                    logger.debug("q16Changed(self=%s,text=%s): Spoorlasuren → %s", self, text, Spoorlasuren)
                    self.Spoorlasuren.setText(text)
                    logger.debug("<<< Exiting q16Changed(text=%s)", text)
                    
                def q17Changed(self,text):
                    logger.debug(">>> Entering q17Changed(text=%s)", text)
                    logger.debug("q17Changed(self=%s,text=%s): Inhuururen → %s", self, text, Inhuururen)
                    self.Inhuururen.setText(text)
                    logger.debug("<<< Exiting q17Changed(text=%s)", text)
                    
                def q18Changed(self,text):
                    logger.debug(">>> Entering q18Changed(text=%s)", text)
                    logger.debug("q18Changed(self=%s,text=%s): Sleuvengraver → %s", self, text, Sleuvengraver)
                    self.Sleuvengraver.setText(text)
                    logger.debug("<<< Exiting q18Changed(text=%s)", text)
                    
                def q19Changed(self,text):
                    logger.debug(">>> Entering q19Changed(text=%s)", text)
                    logger.debug("q19Changed(self=%s,text=%s): Persapparaat → %s", self, text, Persapparaat)
                    self.Persapparaat.setText(text)
                    logger.debug("<<< Exiting q19Changed(text=%s)", text)
                    
                def q20Changed(self,text):
                    logger.debug(">>> Entering q20Changed(text=%s)", text)
                    logger.debug("q20Changed(self=%s,text=%s): Atlaskraan → %s", self, text, Atlaskraan)
                    self.Atlaskraan.setText(text)
                    logger.debug("<<< Exiting q20Changed(text=%s)", text)
                    
                def q21Changed(self,text):
                    logger.debug(">>> Entering q21Changed(text=%s)", text)
                    logger.debug("q21Changed(self=%s,text=%s): Kraan_groot → %s", self, text, Kraan_groot)
                    self.Kraan_groot.setText(text)
                    logger.debug("<<< Exiting q21Changed(text=%s)", text)
                    
                def q22Changed(self,text):
                    logger.debug(">>> Entering q22Changed(text=%s)", text)
                    logger.debug("q22Changed(self=%s,text=%s): Mainliner → %s", self, text, Mainliner)
                    self.Mainliner.setText(text)
                    logger.debug("<<< Exiting q22Changed(text=%s)", text)
                    
                def q23Changed(self,text):
                    logger.debug(">>> Entering q23Changed(text=%s)", text)
                    logger.debug("q23Changed(self=%s,text=%s): Hormachine → %s", self, text, Hormachine)
                    self.Hormachine.setText(text)
                    logger.debug("<<< Exiting q23Changed(text=%s)", text)
                    
                def q24Changed(self,text):
                    logger.debug(">>> Entering q24Changed(text=%s)", text)
                    logger.debug("q24Changed(self=%s,text=%s): Wagon → %s", self, text, Wagon)
                    self.Wagon.setText(text)
                    logger.debug("<<< Exiting q24Changed(text=%s)", text)
                    
                def q25Changed(self,text):
                    logger.debug(">>> Entering q25Changed(text=%s)", text)
                    logger.debug("q25Changed(self=%s,text=%s): Locomotor → %s", self, text, Locomotor)
                    self.Locomotor.setText(text)
                    logger.debug("<<< Exiting q25Changed(text=%s)", text)
                    
                def q26Changed(self,text):
                    logger.debug(">>> Entering q26Changed(text=%s)", text)
                    logger.debug("q26Changed(self=%s,text=%s): Locomotief → %s", self, text, Locomotief)
                    self.Locomotief.setText(text)
                    logger.debug("<<< Exiting q26Changed(text=%s)", text)
                    
                def q27Changed(self,text):
                    logger.debug(">>> Entering q27Changed(text=%s)", text)
                    logger.debug("q27Changed(self=%s,text=%s): Stormobiel → %s", self, text, Stormobiel)
                    self.Stormobiel.setText(text)
                    logger.debug("<<< Exiting q27Changed(text=%s)", text)
                    
                def q28Changed(self,text):
                    logger.debug(">>> Entering q28Changed(text=%s)", text)
                    logger.debug("q28Changed(self=%s,text=%s): Montagewagen → %s", self, text, Montagewagen)
                    self.Montagewagen.setText(text)
                    logger.debug("<<< Exiting q28Changed(text=%s)", text)
                    
                def q29Changed(self,text):
                    logger.debug(">>> Entering q29Changed(text=%s)", text)
                    logger.debug("q29Changed(self=%s,text=%s): Telecomuren → %s", self, text, Telecomuren)
                    self.Telecomuren.setText(text)
                    logger.debug("<<< Exiting q29Changed(text=%s)", text)
                    
                def q30Changed(self,text):
                    logger.debug(">>> Entering q30Changed(text=%s)", text)
                    logger.debug("q30Changed(self=%s,text=%s): Robeltrein → %s", self, text, Robeltrein)
                    self.Robeltrein.setText(text)
                    logger.debug("<<< Exiting q30Changed(text=%s)", text)

                def returnq1(self):
                    logger.debug(">>> Entering returnq1()")
                    logger.debug("<<< Exiting returnq1()")
                    return self.Omschrijving.text()
                                
                def returnq3(self):
                    logger.debug(">>> Entering returnq3()")
                    logger.debug("<<< Exiting returnq3()")
                    return self.Eenheid.text()
                                
                def returnq9(self):
                    logger.debug(">>> Entering returnq9()")
                    logger.debug("<<< Exiting returnq9()")
                    return self.Construktieuren.text()
                
                def returnq10(self):
                    logger.debug(">>> Entering returnq10()")
                    logger.debug("<<< Exiting returnq10()")
                    return self.Montageuren.text()
                
                def returnq11(self):
                    logger.debug(">>> Entering returnq11()")
                    logger.debug("<<< Exiting returnq11()")
                    return self.Retourlasuren.text()
                
                def returnq12(self):
                    logger.debug(">>> Entering returnq12()")
                    logger.debug("<<< Exiting returnq12()")
                    return self.BFIuren.text()
                
                def returnq13(self):
                    logger.debug(">>> Entering returnq13()")
                    logger.debug("<<< Exiting returnq13()")
                    return self.Voedinguren.text()
                
                def returnq14(self):
                    logger.debug(">>> Entering returnq14()")
                    logger.debug("<<< Exiting returnq14()")
                    return self.Bvluren.text()
                
                def returnq15(self):
                    logger.debug(">>> Entering returnq15()")
                    logger.debug("<<< Exiting returnq15()")
                    return self.Spoorleguren.text()
                
                def returnq16(self):
                    logger.debug(">>> Entering returnq16()")
                    logger.debug("<<< Exiting returnq16()")
                    return self.Spoorlasuren.text()
                
                def returnq17(self):
                    logger.debug(">>> Entering returnq17()")
                    logger.debug("<<< Exiting returnq17()")
                    return self.Inhuururen.text()
                
                def returnq18(self):
                    logger.debug(">>> Entering returnq18()")
                    logger.debug("<<< Exiting returnq18()")
                    return self.Sleuvengraver.text()
                
                def returnq19(self):
                    logger.debug(">>> Entering returnq19()")
                    logger.debug("<<< Exiting returnq19()")
                    return self.Persapparaat.text()
                
                def returnq20(self):
                    logger.debug(">>> Entering returnq20()")
                    logger.debug("<<< Exiting returnq20()")
                    return self.Atlaskraan.text()
                
                def returnq21(self):
                    logger.debug(">>> Entering returnq21()")
                    logger.debug("<<< Exiting returnq21()")
                    return self.Kraan_groot.text()
                
                def returnq22(self):
                    logger.debug(">>> Entering returnq22()")
                    logger.debug("<<< Exiting returnq22()")
                    return self.Mainliner.text()
                
                def returnq23(self):
                    logger.debug(">>> Entering returnq23()")
                    logger.debug("<<< Exiting returnq23()")
                    return self.Hormachine.text()
              
                def returnq24(self):
                    logger.debug(">>> Entering returnq24()")
                    logger.debug("<<< Exiting returnq24()")
                    return self.Wagon.text()
                
                def returnq25(self):
                    logger.debug(">>> Entering returnq25()")
                    logger.debug("<<< Exiting returnq25()")
                    return self.Locomotor.text()
                
                def returnq26(self):
                    logger.debug(">>> Entering returnq26()")
                    logger.debug("<<< Exiting returnq26()")
                    return self.Locomotief.text()
              
                def returnq27(self):
                    logger.debug(">>> Entering returnq27()")
                    logger.debug("<<< Exiting returnq27()")
                    return self.Stormobiel.text()
                
                def returnq28(self):
                    logger.debug(">>> Entering returnq28()")
                    logger.debug("<<< Exiting returnq28()")
                    return self.Montagewagen.text()
                
                def returnq29(self):
                    logger.debug(">>> Entering returnq29()")
                    logger.debug("<<< Exiting returnq29()")
                    return self.Telecomuren.text()
        
                def returnq30(self):
                    logger.debug(">>> Entering returnq30()")
                    logger.debug("<<< Exiting returnq30()")
                    return self.Robeltrein.text()

                @staticmethod
                def getData(parent=None):
                    logger.debug(">>> Entering getData(parent=%s)", parent)
                    dialog = MainWindow()
                    dialog.exec_()
                    logger.debug("<<< Exiting getData(parent=%s)", parent)
                    return [dialog.returnq1(), dialog.returnq3(), dialog.returnq9(),\
                            dialog.returnq10(), dialog.returnq11(), dialog.returnq12(),\
                            dialog.returnq13(), dialog.returnq14(), dialog.returnq15(),\
                            dialog.returnq16(), dialog.returnq17(), dialog.returnq18(),\
                            dialog.returnq19(), dialog.returnq20(), dialog.returnq21(),\
                            dialog.returnq22(), dialog.returnq23(), dialog.returnq24(),\
                            dialog.returnq25(), dialog.returnq26(), dialog.returnq27(),\
                            dialog.returnq28(), dialog.returnq29(), dialog.returnq30()]
                                       
            mainWin = MainWindow()
            data = mainWin.getData()
     
            chflag = 0
            for k in range(0,24):
                if data[k]:
                    chflag = 1
            if chflag == 0:
                return
            if data[0]:
                ms0 = str(data[0])
            else:
                ms0 = rpsel[1]
            if data[1]:
                mf1 = data[1]
            else:
                mf1 = rpsel[3]  
            if data[2]:
                mf2 = float(data[2])
            else:
                mf2= rpsel[9]
            if data[3]:
                mf3 = data[3]
            else:
                mf3 = rpsel[10]
            if data[4]:
                mf4 = float(data[4])
            else:
                mf4= rpsel[11]
            if data[5]:
                mf5 = float(data[5])
            else:
                mf5 = rpsel[12]
            if data[6]:
                mf6 = float(data[6])
            else:
                mf6 = rpsel[13]
            if data[7]:
                mf7 = float(data[7])
            else:
                mf7 = rpsel[14]
            if data[8]:
                mf8 = float(data[8])
            else:
                mf8= rpsel[15]
            if data[9]:
                mf9 = float(data[9])
            else:
                mf9= rpsel[16]
            if data[10]:
                mf10 = float(data[10])
            else:
                mf10= rpsel[17]     
            if data[11]:
                mf11 = float(data[11])
            else:
                mf11= rpsel[18]     
            if data[12]:
                mf12 = float(data[12])
            else:
                mf12= rpsel[19]
            if data[13]:
                mf13 = float(data[13])
            else:
                mf13= rpsel[20]
            if data[14]:
                mf14 = float(data[14])
            else:
                mf14= rpsel[21]
            if data[15]:
                mf15 = float(data[15])
            else:
                mf15= rpsel[22]
            if data[16]:
                mf16 = float(data[16])
            else:
                mf16= rpsel[23]
            if data[17]:
                mf17 = float(data[17])
            else:
                mf17 = rpsel[24]
            if data[18]:
                mf18 = float(data[18])
            else:
                mf18= rpsel[25]
            if data[19]:
                mf19 = float(data[19])
            else:
                mf19= rpsel[26]
            if data[20]:
                mf20 = float(data[20])
            else:
                mf20= rpsel[27]
            if data[21]:
                mf21 = float(data[21])
            else:
                mf21= rpsel[28]
            if data[22]:
                mf22 = data[22]
            else:
                mf22= rpsel[29]
            if data[23]:
                mf23 = float(data[23])
            else:
                mf23= rpsel[30]

            metadata = MetaData()
            params_hours = Table('params_hours', metadata,
                Column('rateID', Integer, primary_key=True),
                Column('hourly_tariff', Float),
                Column('item', String))
            
            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            con = engine.connect()
            selpar = select([params_hours]).order_by(params_hours.c.rateID)
            rppar = con.execute(selpar).fetchall()

            metadata = MetaData()
            params_services = Table('params_services', metadata,
                                 Column('servicesID', Integer, primary_key=True),
                                 Column('hourly_tariff', Float),
                                 Column('item', String))

            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            con = engine.connect()
            selpar1 = select([params_services]).order_by(params_services.c.servicesID)
            rppar1 = con.execute(selpar1).fetchall()

            upd1 = update(clusters).where(clusters.c.clusterID == clusternr).values(
                omschrijving=ms0, eenheid=mf1, uren_constr = mf2,\
                uren_mont=mf3, uren_retourlas=mf4, uren_bfi=mf5, uren_voeding=mf6,\
                uren_bvl=mf7, uren_spoorleg=mf8, uren_spoorlas=mf9, uren_inhuur=mf10,\
                sleuvengraver=mf11, persapparaat=mf12, atlaskraan=mf13, kraan_groot=mf14,\
                mainliner=mf15, hormachine=mf16, wagon=mf17,locomotor=mf18,locomotief=mf19,\
                montagewagen=mf20, stormobiel=mf21, uren_telecom=mf22, robeltrein=mf23)
            con.execute(upd1)
            upd2 = update(clusters).where(clusters.c.clusterID == clusternr).values(\
                lonen=clusters.c.uren_constr*rppar[1][1]+clusters.c.uren_mont*rppar[2][1]\
                 +clusters.c.uren_retourlas*rppar[8][1]+clusters.c.uren_bfi*rppar[3][1]\
                 +clusters.c.uren_voeding*rppar[4][1]+clusters.c.uren_bvl*rppar[5][1]\
                 +clusters.c.uren_spoorleg*rppar[6][1]+clusters.c.uren_spoorlas*rppar[7][1]\
                 +clusters.c.uren_telecom*rppar[10][1],\
                materieel=clusters.c.sleuvengraver*rppar1[0][1]+clusters.c.persapparaat\
                 *rppar1[1][1]+clusters.c.atlaskraan*rppar1[2][1]+clusters.c.kraan_groot\
                 *rppar1[3][1]+clusters.c.mainliner*rppar1[4][1]+clusters.c.hormachine\
                 *rppar1[5][1]+clusters.c.wagon*rppar1[6][1]+clusters.c.locomotor\
                 *rppar1[7][1]+clusters.c.locomotief*rppar1[8][1]+clusters.c.montagewagen\
                 *rppar1[9][1]+clusters.c.stormobiel*rppar1[10][1]+clusters.c.robeltrein\
                 *rppar1[11][1], inhuur=clusters.c.uren_inhuur*rppar[0][1])
            con.execute(upd2)
            upd4 = update(clusters).where(clusters.c.clusterID == clusternr).values(\
                    prijs = clusters.c.lonen+clusters.c.materialen+clusters.c.materieel)
            con.execute(upd4)
            invoerOK()
        
    win = MyWindow(data_list, header)
    win.exec_()
    zoeken(m_email)