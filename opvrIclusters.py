from login import hoofdMenu
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QWidget, QTableView, QVBoxLayout, QComboBox,\
    QDialog, QLabel, QGridLayout, QPushButton, QMessageBox, QLineEdit
from sqlalchemy import (Table, Column, String, Float, MetaData,\
                         create_engine)
from sqlalchemy.sql import select
import logging
logger = logging.getLogger(__name__)

def geenRecord():
    logger.debug(">>> Entering geenRecord()")
    msg = QMessageBox()
    logger.debug("geenRecord(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('No record found\ncreate another selection please!')
    msg.setWindowTitle('Request clusters')
    logger.debug("<<< Exiting geenRecord()")
    msg.exec_() 
 
def windowSluit(self,m_email):
    logger.debug(">>> Entering windowSluit(m_email=%s)", m_email)
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email)
   
def ongKeuze():
    logger.debug(">>> Entering ongKeuze()")
    msg = QMessageBox()
    logger.debug("ongKeuze(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Invalid choice')
    msg.setWindowTitle('Insert clusters')
    logger.debug("<<< Exiting ongKeuze()")
    msg.exec_() 

def zoeken(m_email):
    logger.debug(">>> Entering zoeken(m_email=%s)", m_email)
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.debug(">>> Entering __init__(parent=%s)", parent)
            self.setWindowTitle("Cluster selection")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
                              
            self.Keuze = QLabel()
            logger.debug("__init__(parent=%s): self.Keuze → %s", parent, self.Keuze)
            k0Edit = QComboBox()
            logger.debug("__init__(self=%s,parent=%s): k0Edit → %s", self, parent, k0Edit)
            logger.debug("__init__(parent=%s): k0Edit → %s", parent, k0Edit)
            k0Edit.setFixedWidth(340)
            k0Edit.setFont(QFont("Arial",10))
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.addItem('              Sort key cluster groups')
            k0Edit.addItem('0. All clusters')
            k0Edit.addItem('LA-LK. Machined parts')
            k0Edit.addItem('MA-MK. Bolts and nuts')
            k0Edit.addItem('NA-NK. Casting machining')
            k0Edit.addItem('OA-OK. Welding composite')
            k0Edit.addItem('PA-PK. Sheet metal assembled')
            k0Edit.addItem('RA-RK. Plastic parts')
            k0Edit.addItem('SA-SK. Prefab mounting parts')
            k0Edit.addItem('TA-TK. Assembly parts')
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
                        
            grid.addWidget(k0Edit, 1, 0, 1, 2, Qt.AlignRight)
            
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 3, 0, 1, 3, Qt.AlignCenter)
            
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
            cancelBtn.clicked.connect(lambda: windowSluit(self,m_email))
    
            grid.addWidget(cancelBtn, 2, 0, 1 , 2, Qt.AlignCenter)
            logger.debug("<<< Exiting __init__(parent=%s)", parent)
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
            logger.debug(">>> Entering __init__(data_list=%s,header=%s)", data_list, header)
            logger.debug("__init__(data_list=%s,header=%s): font → %s", data_list, header, font)
            logger.debug("__init__(data_list=%s,header=%s): table_view → %s", data_list, header, table_view)
            logger.debug("__init__(data_list=%s,header=%s): table_model → %s", data_list, header, table_model)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): table_model → %s", self, data_list, header, table_model)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): table_view → %s", self, data_list, header, table_view)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): font → %s", self, data_list, header, font)
            logger.debug("__init__(data_list=%s,header=%s): layout → %s", data_list, header, layout)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): layout → %s", self, data_list, header, layout)
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
        zoeken(m_email)
    elif data[0][0] == '0':
        keuze = ''
    elif data[0]:
        keuze = data[0][0]
    toonIclusters(keuze, m_email)

def toonIclusters(keuze, m_email):
    logger.debug(">>> Entering toonIclusters(keuze=%s,m_email=%s)", keuze, m_email)
    class MyWindow(QDialog):
        def __init__(self, data_list, header, *args):
            QWidget.__init__(self, *args,)
            self.setGeometry(100, 50, 1700, 900)
            self.setWindowTitle('Internal cluster calculation')
            self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
            self.setWindowFlags(self.windowFlags()| Qt.WindowSystemMenuHint |
                              Qt.WindowMinMaxButtonsHint)
            table_model = MyTableModel(self, data_list, header)
            table_view = QTableView()
            table_view.setModel(table_model)
            font = QFont("Arial", 10)
            table_view.setFont(font)
            table_view.resizeColumnsToContents()
            table_view.setSelectionBehavior(QTableView.SelectRows)
            table_view.clicked.connect(showSelection)
            layout = QVBoxLayout(self)
            layout.addWidget(table_view)
            self.setLayout(layout)
            logger.debug(">>> Entering __init__(parent=%s,mylist=%s,header=%s)", parent, mylist, header)
            logger.debug("<<< Exiting __init__(parent=%s,mylist=%s,header=%s)", parent, mylist, header)
            logger.debug("__init__(self=%s,parent=%s,mylist=%s,header=%s): self.mylist → %s", self, parent, mylist, header, self.mylist)
    
    class MyTableModel(QAbstractTableModel):
        def __init__(self, parent, mylist, header, *args):
            logger.debug("__init__(self=%s,parent=%s,mylist=%s,header=%s): self.header → %s", self, parent, mylist, header, self.header)
            QAbstractTableModel.__init__(self, parent, *args)
            self.mylist = mylist
            logger.debug(">>> Entering __init__()")
            logger.debug("__init__(): grid → %s", grid)
            logger.debug("__init__(self=%s): grid → %s", self, grid)
            logger.debug("__init__(): q1Edit → %s", q1Edit)
            logger.debug("__init__(): self.Omschrijving → %s", self.Omschrijving)
            logger.debug("__init__(self=%s): q1Edit → %s", self, q1Edit)
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
            logger.debug("__init__(): self.Szagen → %s", self.Szagen)
            logger.debug("__init__(self=%s): q9Edit → %s", self, q9Edit)
            logger.debug("__init__(): q10Edit → %s", q10Edit)
            logger.debug("__init__(): self.Zagen → %s", self.Zagen)
            logger.debug("__init__(self=%s): q10Edit → %s", self, q10Edit)
            logger.debug("__init__(): q11Edit → %s", q11Edit)
            logger.debug("__init__(): self.Sschaven → %s", self.Sschaven)
            logger.debug("__init__(self=%s): q11Edit → %s", self, q11Edit)
            logger.debug("__init__(): q12Edit → %s", q12Edit)
            logger.debug("__init__(): self.Schaven → %s", self.Schaven)
            logger.debug("__init__(self=%s): q12Edit → %s", self, q12Edit)
            logger.debug("__init__(): q13Edit → %s", q13Edit)
            logger.debug("__init__(): self.Ssteken → %s", self.Ssteken)
            logger.debug("__init__(self=%s): q13Edit → %s", self, q13Edit)
            logger.debug("__init__(): q14Edit → %s", q14Edit)
            logger.debug("__init__(): self.Steken → %s", self.Steken)
            logger.debug("__init__(self=%s): q14Edit → %s", self, q14Edit)
            logger.debug("__init__(): q15Edit → %s", q15Edit)
            logger.debug("__init__(): self.Sboren → %s", self.Sboren)
            logger.debug("__init__(self=%s): q15Edit → %s", self, q15Edit)
            logger.debug("__init__(): q16Edit → %s", q16Edit)
            logger.debug("__init__(): self.Boren → %s", self.Boren)
            logger.debug("__init__(self=%s): q16Edit → %s", self, q16Edit)
            logger.debug("__init__(): q17Edit → %s", q17Edit)
            logger.debug("__init__(): self.Sfrezen → %s", self.Sfrezen)
            logger.debug("__init__(self=%s): q17Edit → %s", self, q17Edit)
            logger.debug("__init__(): q18Edit → %s", q18Edit)
            logger.debug("__init__(): self.Frezen → %s", self.Frezen)
            logger.debug("__init__(self=%s): q18Edit → %s", self, q18Edit)
            logger.debug("__init__(): q19Edit → %s", q19Edit)
            logger.debug("__init__(): self.Sdraaien_klein → %s", self.Sdraaien_klein)
            logger.debug("__init__(self=%s): q19Edit → %s", self, q19Edit)
            logger.debug("__init__(): q20Edit → %s", q20Edit)
            logger.debug("__init__(): self.Draaien_klein → %s", self.Draaien_klein)
            logger.debug("__init__(self=%s): q20Edit → %s", self, q20Edit)
            logger.debug("__init__(): q21Edit → %s", q21Edit)
            logger.debug("__init__(): self.SDraaien_groot → %s", self.SDraaien_groot)
            logger.debug("__init__(self=%s): q21Edit → %s", self, q21Edit)
            logger.debug("__init__(): q22Edit → %s", q22Edit)
            logger.debug("__init__(): self.Draaien_groot → %s", self.Draaien_groot)
            logger.debug("__init__(self=%s): q22Edit → %s", self, q22Edit)
            logger.debug("__init__(): q23Edit → %s", q23Edit)
            logger.debug("__init__(): self.Stappen → %s", self.Stappen)
            logger.debug("__init__(self=%s): q23Edit → %s", self, q23Edit)
            logger.debug("__init__(): q24Edit → %s", q24Edit)
            logger.debug("__init__(): self.Tappen → %s", self.Tappen)
            logger.debug("__init__(self=%s): q24Edit → %s", self, q24Edit)
            logger.debug("__init__(): q25Edit → %s", q25Edit)
            logger.debug("__init__(): self.Snube_draaien → %s", self.Snube_draaien)
            logger.debug("__init__(self=%s): q25Edit → %s", self, q25Edit)
            logger.debug("__init__(): q26Edit → %s", q26Edit)
            logger.debug("__init__(): self.Nube_draaien → %s", self.Nube_draaien)
            logger.debug("__init__(self=%s): q26Edit → %s", self, q26Edit)
            logger.debug("__init__(): q27Edit → %s", q27Edit)
            logger.debug("__init__(): self.Snube_bewerken → %s", self.Snube_bewerken)
            logger.debug("__init__(self=%s): q27Edit → %s", self, q27Edit)
            logger.debug("__init__(): q28Edit → %s", q28Edit)
            logger.debug("__init__(): self.Nube_bewerken → %s", self.Nube_bewerken)
            logger.debug("__init__(self=%s): q28Edit → %s", self, q28Edit)
            logger.debug("__init__(): q29Edit → %s", q29Edit)
            logger.debug("__init__(): self.Sknippen → %s", self.Sknippen)
            logger.debug("__init__(self=%s): q29Edit → %s", self, q29Edit)
            logger.debug("__init__(): q30Edit → %s", q30Edit)
            logger.debug("__init__(): self.Knippen → %s", self.Knippen)
            logger.debug("__init__(self=%s): q30Edit → %s", self, q30Edit)
            logger.debug("__init__(): q31Edit → %s", q31Edit)
            logger.debug("__init__(): self.Skanten → %s", self.Skanten)
            logger.debug("__init__(self=%s): q31Edit → %s", self, q31Edit)
            logger.debug("__init__(): q32Edit → %s", q32Edit)
            logger.debug("__init__(): self.Kanten → %s", self.Kanten)
            logger.debug("__init__(self=%s): q32Edit → %s", self, q32Edit)
            logger.debug("__init__(): q33Edit → %s", q33Edit)
            logger.debug("__init__(): self.Sstansen → %s", self.Sstansen)
            logger.debug("__init__(self=%s): q33Edit → %s", self, q33Edit)
            logger.debug("__init__(): q34Edit → %s", q34Edit)
            logger.debug("__init__(): self.Stansen → %s", self.Stansen)
            logger.debug("__init__(self=%s): q34Edit → %s", self, q34Edit)
            logger.debug("__init__(): q35Edit → %s", q35Edit)
            logger.debug("__init__(): self.Slassen_CO2 → %s", self.Slassen_CO2)
            logger.debug("__init__(self=%s): q35Edit → %s", self, q35Edit)
            logger.debug("__init__(): q36Edit → %s", q36Edit)
            logger.debug("__init__(): self.Lassen_CO2 → %s", self.Lassen_CO2)
            logger.debug("__init__(self=%s): q36Edit → %s", self, q36Edit)
            logger.debug("__init__(): q37Edit → %s", q37Edit)
            logger.debug("__init__(): self.Slassen_hand → %s", self.Slassen_hand)
            logger.debug("__init__(self=%s): q37Edit → %s", self, q37Edit)
            logger.debug("__init__(): q38Edit → %s", q38Edit)
            logger.debug("__init__(): self.Lassen_hand → %s", self.Lassen_hand)
            logger.debug("__init__(self=%s): q38Edit → %s", self, q38Edit)
            logger.debug("__init__(): q39Edit → %s", q39Edit)
            logger.debug("__init__(): self.Sverpakken → %s", self.Sverpakken)
            logger.debug("__init__(self=%s): q39Edit → %s", self, q39Edit)
            logger.debug("__init__(): q40Edit → %s", q40Edit)
            logger.debug("__init__(): self.Verpakken → %s", self.Verpakken)
            logger.debug("__init__(self=%s): q40Edit → %s", self, q40Edit)
            logger.debug("__init__(): q41Edit → %s", q41Edit)
            logger.debug("__init__(): self.Sverzinken → %s", self.Sverzinken)
            logger.debug("__init__(self=%s): q41Edit → %s", self, q41Edit)
            logger.debug("__init__(): q42Edit → %s", q42Edit)
            logger.debug("__init__(): self.Verzinken → %s", self.Verzinken)
            logger.debug("__init__(self=%s): q42Edit → %s", self, q42Edit)
            logger.debug("__init__(): q43Edit → %s", q43Edit)
            logger.debug("__init__(): self.Smoffelen → %s", self.Smoffelen)
            logger.debug("__init__(self=%s): q43Edit → %s", self, q43Edit)
            logger.debug("__init__(): q44Edit → %s", q44Edit)
            logger.debug("__init__(): self.Moffelen → %s", self.Moffelen)
            logger.debug("__init__(self=%s): q44Edit → %s", self, q44Edit)
            logger.debug("__init__(): q45Edit → %s", q45Edit)
            logger.debug("__init__(): self.Sschilderen → %s", self.Sschilderen)
            logger.debug("__init__(self=%s): q45Edit → %s", self, q45Edit)
            logger.debug("__init__(): q46Edit → %s", q46Edit)
            logger.debug("__init__(): self.Schilderen → %s", self.Schilderen)
            logger.debug("__init__(self=%s): q46Edit → %s", self, q46Edit)
            logger.debug("__init__(): q47Edit → %s", q47Edit)
            logger.debug("__init__(): self.Sspuiten → %s", self.Sspuiten)
            logger.debug("__init__(self=%s): q47Edit → %s", self, q47Edit)
            logger.debug("__init__(): q48Edit → %s", q48Edit)
            logger.debug("__init__(): self.Spuiten → %s", self.Spuiten)
            logger.debug("__init__(self=%s): q48Edit → %s", self, q48Edit)
            logger.debug("__init__(): q49Edit → %s", q49Edit)
            logger.debug("__init__(): self.Sponsen → %s", self.Sponsen)
            logger.debug("__init__(self=%s): q49Edit → %s", self, q49Edit)
            logger.debug("__init__(): q50Edit → %s", q50Edit)
            logger.debug("__init__(): self.Ponsen → %s", self.Ponsen)
            logger.debug("__init__(self=%s): q50Edit → %s", self, q50Edit)
            logger.debug("__init__(): q51Edit → %s", q51Edit)
            logger.debug("__init__(): self.Spersen → %s", self.Spersen)
            logger.debug("__init__(self=%s): q51Edit → %s", self, q51Edit)
            logger.debug("__init__(): q52Edit → %s", q52Edit)
            logger.debug("__init__(): self.Persen → %s", self.Persen)
            logger.debug("__init__(self=%s): q52Edit → %s", self, q52Edit)
            logger.debug("__init__(): q53Edit → %s", q53Edit)
            logger.debug("__init__(): self.Sgritstralen → %s", self.Sgritstralen)
            logger.debug("__init__(self=%s): q53Edit → %s", self, q53Edit)
            logger.debug("__init__(): q54Edit → %s", q54Edit)
            logger.debug("__init__(): self.Gritstralen → %s", self.Gritstralen)
            logger.debug("__init__(self=%s): q54Edit → %s", self, q54Edit)
            logger.debug("__init__(): q55Edit → %s", q55Edit)
            logger.debug("__init__(): self.Smontage → %s", self.Smontage)
            logger.debug("__init__(self=%s): q55Edit → %s", self, q55Edit)
            logger.debug("__init__(): q56Edit → %s", q56Edit)
            logger.debug("__init__(): self.Montage → %s", self.Montage)
            logger.debug("__init__(self=%s): q56Edit → %s", self, q56Edit)
            logger.debug("__init__(): lbl1 → %s", lbl1)
            logger.debug("__init__(self=%s): lbl1 → %s", self, lbl1)
            logger.debug("__init__(): lbl2 → %s", lbl2)
            logger.debug("__init__(self=%s): lbl2 → %s", self, lbl2)
            logger.debug("__init__(): lbl3 → %s", lbl3)
            logger.debug("__init__(self=%s): lbl3 → %s", self, lbl3)
            logger.debug("__init__(): lbl4 → %s", lbl4)
            logger.debug("__init__(self=%s): lbl4 → %s", self, lbl4)
            logger.debug("__init__(): lbl5 → %s", lbl5)
            logger.debug("__init__(self=%s): lbl5 → %s", self, lbl5)
            logger.debug("__init__(): lbl6 → %s", lbl6)
            logger.debug("__init__(self=%s): lbl6 → %s", self, lbl6)
            logger.debug("__init__(): lbl7 → %s", lbl7)
            logger.debug("__init__(self=%s): lbl7 → %s", self, lbl7)
            logger.debug("__init__(): lbl8 → %s", lbl8)
            logger.debug("__init__(self=%s): lbl8 → %s", self, lbl8)
            logger.debug("__init__(): lbl9 → %s", lbl9)
            logger.debug("__init__(self=%s): lbl9 → %s", self, lbl9)
            logger.debug("__init__(): lbl10 → %s", lbl10)
            logger.debug("__init__(self=%s): lbl10 → %s", self, lbl10)
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
            logger.debug("__init__(): lbl19 → %s", lbl19)
            logger.debug("__init__(self=%s): lbl19 → %s", self, lbl19)
            logger.debug("__init__(): lbl20 → %s", lbl20)
            logger.debug("__init__(self=%s): lbl20 → %s", self, lbl20)
            logger.debug("__init__(): lbl21 → %s", lbl21)
            logger.debug("__init__(self=%s): lbl21 → %s", self, lbl21)
            logger.debug("__init__(): lbl22 → %s", lbl22)
            logger.debug("__init__(self=%s): lbl22 → %s", self, lbl22)
            logger.debug("__init__(): lbl23 → %s", lbl23)
            logger.debug("__init__(self=%s): lbl23 → %s", self, lbl23)
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
            logger.debug("__init__(): lbl32 → %s", lbl32)
            logger.debug("__init__(self=%s): lbl32 → %s", self, lbl32)
            logger.debug("__init__(): lbl33 → %s", lbl33)
            logger.debug("__init__(self=%s): lbl33 → %s", self, lbl33)
            logger.debug("__init__(): lbl34 → %s", lbl34)
            logger.debug("__init__(self=%s): lbl34 → %s", self, lbl34)
            logger.debug("__init__(): lbl35 → %s", lbl35)
            logger.debug("__init__(self=%s): lbl35 → %s", self, lbl35)
            logger.debug("__init__(): lbl36 → %s", lbl36)
            logger.debug("__init__(self=%s): lbl36 → %s", self, lbl36)
            logger.debug("__init__(): lbl37 → %s", lbl37)
            logger.debug("__init__(self=%s): lbl37 → %s", self, lbl37)
            logger.debug("__init__(): lbl38 → %s", lbl38)
            logger.debug("__init__(self=%s): lbl38 → %s", self, lbl38)
            logger.debug("__init__(): lbl39 → %s", lbl39)
            logger.debug("__init__(self=%s): lbl39 → %s", self, lbl39)
            logger.debug("__init__(): lbl40 → %s", lbl40)
            logger.debug("__init__(self=%s): lbl40 → %s", self, lbl40)
            logger.debug("__init__(): lbl41 → %s", lbl41)
            logger.debug("__init__(self=%s): lbl41 → %s", self, lbl41)
            logger.debug("__init__(): lbl42 → %s", lbl42)
            logger.debug("__init__(self=%s): lbl42 → %s", self, lbl42)
            logger.debug("__init__(): lbl43 → %s", lbl43)
            logger.debug("__init__(self=%s): lbl43 → %s", self, lbl43)
            logger.debug("__init__(): lbl44 → %s", lbl44)
            logger.debug("__init__(self=%s): lbl44 → %s", self, lbl44)
            logger.debug("__init__(): lbl45 → %s", lbl45)
            logger.debug("__init__(self=%s): lbl45 → %s", self, lbl45)
            logger.debug("__init__(): lbl46 → %s", lbl46)
            logger.debug("__init__(self=%s): lbl46 → %s", self, lbl46)
            logger.debug("__init__(): lbl47 → %s", lbl47)
            logger.debug("__init__(self=%s): lbl47 → %s", self, lbl47)
            logger.debug("__init__(): lbl48 → %s", lbl48)
            logger.debug("__init__(self=%s): lbl48 → %s", self, lbl48)
            logger.debug("__init__(): lbl49 → %s", lbl49)
            logger.debug("__init__(self=%s): lbl49 → %s", self, lbl49)
            logger.debug("__init__(): lbl50 → %s", lbl50)
            logger.debug("__init__(self=%s): lbl50 → %s", self, lbl50)
            logger.debug("__init__(): lbl51 → %s", lbl51)
            logger.debug("__init__(self=%s): lbl51 → %s", self, lbl51)
            logger.debug("__init__(): lbl52 → %s", lbl52)
            logger.debug("__init__(self=%s): lbl52 → %s", self, lbl52)
            logger.debug("__init__(): lbl53 → %s", lbl53)
            logger.debug("__init__(self=%s): lbl53 → %s", self, lbl53)
            logger.debug("__init__(): lbl54 → %s", lbl54)
            logger.debug("__init__(self=%s): lbl54 → %s", self, lbl54)
            logger.debug("__init__(): lbl55 → %s", lbl55)
            logger.debug("__init__(self=%s): lbl55 → %s", self, lbl55)
            logger.debug("__init__(): lbl56 → %s", lbl56)
            logger.debug("__init__(self=%s): lbl56 → %s", self, lbl56)
            logger.debug("__init__(): lbl57 → %s", lbl57)
            logger.debug("__init__(self=%s): lbl57 → %s", self, lbl57)
            logger.debug("__init__(): lbl58 → %s", lbl58)
            logger.debug("__init__(self=%s): lbl58 → %s", self, lbl58)
            logger.debug("__init__(): pixmap → %s", pixmap)
            logger.debug("__init__(): lbl → %s", lbl)
            logger.debug("__init__(self=%s): lbl → %s", self, lbl)
            logger.debug("__init__(self=%s): pixmap → %s", self, pixmap)
            logger.debug("__init__(): logo → %s", logo)
            logger.debug("__init__(self=%s): logo → %s", self, logo)
            logger.debug("__init__(): sluitBtn → %s", sluitBtn)
            logger.debug("__init__(self=%s): sluitBtn → %s", self, sluitBtn)
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
             
    header = ['Cluster number','Description','Price','Unit','Materials','Wages',\
              'Services','Equipment','Hiring','Set costs\nsawing','Sawing','Set costs\nplaning','Planing',\
              'Set costs\nstabbing','Stabbing','Set costs\ndrilling','Drilling','Set costs\nmilling','Milling','Set costs\nturning small',\
              'Turning small','Set costs\nturning big','Turning big','Set costs\nthreading','Threading',\
              'Set costs\nCNC turning','CNC turning','Set costs\nCNC milling','CNC milling',\
              'Set costs\ncutting','Cutting','Set costs\nfolding','Folding','Set costs\ndie-cutting','Die-cutting',\
              'Set costs\nwelding co2','Welding co2','Set costs\nwelding hand','Welding hand','Set costs\npacking',\
              'Packing','Set costs\ngalvanise','Galvanise','Set costs\nmuffling','Muffling','Set costs\npainting',\
              'Painting','Set costs\nspraying','Spraying','Set costs\nstam[ping','Stamping','Set costs\npressing',\
              'Pressing','Set costs\ngrit blasting','Grit blasting','Set costs\nmounting','Mounting']
     
    metadata = MetaData()
    iclusters = Table('iclusters', metadata,
        Column('iclusterID', String, primary_key=True),
        Column('omschrijving', String),
        Column('prijs', Float),
        Column('eenheid', String),
        Column('materialen', Float),
        Column('lonen', Float),
        Column('diensten', Float),
        Column('materieel', Float),
        Column('inhuur', Float),
        Column('szagen', Float),
        Column('zagen', Float),
        Column('sschaven', Float),
        Column('schaven', Float),
        Column('ssteken', Float),
        Column('steken', Float),
        Column('sboren', Float),
        Column('boren', Float),
        Column('sfrezen', Float),
        Column('frezen', Float),
        Column('sdraaien_klein', Float),
        Column('draaien_klein', Float),
        Column('sdraaien_groot', Float),
        Column('draaien_groot', Float),
        Column('stappen', Float),
        Column('tappen', Float),
        Column('snube_draaien', Float),
        Column('nube_draaien', Float),
        Column('snube_bewerken', Float),
        Column('nube_bewerken', Float),
        Column('sknippen', Float),
        Column('knippen', Float),
        Column('skanten', Float),
        Column('kanten', Float),
        Column('sstansen', Float),
        Column('stansen', Float),
        Column('slassen_co2', Float),
        Column('lassen_co2', Float),
        Column('slassen_hand', Float),
        Column('lassen_hand', Float),
        Column('sverpakken', Float),
        Column('verpakken', Float),
        Column('sverzinken', Float),
        Column('verzinken', Float),
        Column('smoffelen', Float),
        Column('moffelen', Float),
        Column('sschilderen', Float),
        Column('schilderen', Float),
        Column('sspuiten', Float),
        Column('spuiten', Float),
        Column('sponsen', Float),
        Column('ponsen', Float),
        Column('spersen', Float),
        Column('persen', Float),
        Column('sgritstralen', Float),
        Column('gritstralen', Float),
        Column('smontage', Float),
        Column('montage', Float))
               
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
        
    sel = select([iclusters]).where(iclusters.c.iclusterID.ilike(keuze+'%'))\
                              .order_by(iclusters.c.iclusterID)
       
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
            logger.debug("showSelection(idx=%s): con → %s", idx, con)
            selcl = select([iclusters]).where(iclusters.c.iclusterID == clusternr)
            rpsel = con.execute(selcl).first()
            logger.debug("showSelection(idx=%s): selcl → %s", idx, selcl)
            logger.debug("showSelection(idx=%s): rpsel → %s", idx, rpsel)
            
            class MainWindow(QDialog):
                logger.debug("<<< Exiting showSelection(idx=%s)", idx)
                def __init__(self):
                    QDialog.__init__(self)
                    
                    grid = QGridLayout()
                    grid.setSpacing(20)
                    self.setWindowTitle("Request cluster")
                    self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
                    
                    self.setFont(QFont('Arial', 10))   
  
                    self.Omschrijving = QLabel()
                    q1Edit = QLineEdit(rpsel[1])
                    q1Edit.setFixedWidth(400)
                    q1Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q1Edit.setDisabled(True)
                                    
                    self.Prijs = QLabel()
                    q2Edit = QLineEdit('{:12.2f}'.format(rpsel[2]))
                    q2Edit.setAlignment(Qt.AlignRight)
                    q2Edit.setFixedWidth(150)
                    q2Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q2Edit.setDisabled(True)
                    
                    self.Eenheid = QLabel()
                    q3Edit = QLineEdit(str(rpsel[3]))
                    q3Edit.setFixedWidth(150)
                    q3Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q3Edit.setDisabled(True)
                      
                    self.Materialen = QLabel()
                    q4Edit = QLineEdit('{:12.2f}'.format(rpsel[4]))
                    q4Edit.setFixedWidth(150)
                    q4Edit.setAlignment(Qt.AlignRight)
                    q4Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q4Edit.setDisabled(True)
                    
                    self.Lonen = QLabel()
                    q5Edit = QLineEdit('{:12.2f}'.format(rpsel[5]))
                    q5Edit.setFixedWidth(150)
                    q5Edit.setAlignment(Qt.AlignRight)
                    q5Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
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
                    q7Edit.setDisabled(True)
                    
                    self.Inhuur = QLabel()
                    q8Edit = QLineEdit('{:12.2f}'.format(rpsel[8]))
                    q8Edit.setFixedWidth(150)
                    q8Edit.setAlignment(Qt.AlignRight)
                    q8Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q8Edit.setDisabled(True)
                      
                    self.Szagen = QLabel()
                    q9Edit = QLineEdit('{:12.2f}'.format(rpsel[9]))
                    q9Edit.setFixedWidth(150)
                    q9Edit.setAlignment(Qt.AlignRight)
                    q9Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q9Edit.setDisabled(True)
                    
                    self.Zagen = QLabel()
                    q10Edit = QLineEdit('{:12.2f}'.format(rpsel[10]))
                    q10Edit.setFixedWidth(150)
                    q10Edit.setAlignment(Qt.AlignRight)
                    q10Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q10Edit.setDisabled(True)
                    
                    self.Sschaven = QLabel()
                    q11Edit = QLineEdit('{:12.2f}'.format(rpsel[11]))
                    q11Edit.setFixedWidth(150)
                    q11Edit.setAlignment(Qt.AlignRight)
                    q11Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q11Edit.setDisabled(True)
                    
                    self.Schaven = QLabel()
                    q12Edit = QLineEdit('{:12.2f}'.format(rpsel[12]))
                    q12Edit.setFixedWidth(150)
                    q12Edit.setAlignment(Qt.AlignRight)
                    q12Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q12Edit.setDisabled(True)
                    
                    self.Ssteken = QLabel()
                    q13Edit = QLineEdit('{:12.2f}'.format(rpsel[13]))
                    q13Edit.setFixedWidth(150)
                    q13Edit.setAlignment(Qt.AlignRight)
                    q13Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q13Edit.setDisabled(True)
                    
                    self.Steken = QLabel()
                    q14Edit = QLineEdit('{:12.2f}'.format(rpsel[14]))
                    q14Edit.setFixedWidth(150)
                    q14Edit.setAlignment(Qt.AlignRight)
                    q14Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q14Edit.setDisabled(True)
                    
                    self.Sboren = QLabel()
                    q15Edit = QLineEdit('{:12.2f}'.format(rpsel[15]))
                    q15Edit.setFixedWidth(150)
                    q15Edit.setAlignment(Qt.AlignRight)
                    q15Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q15Edit.setDisabled(True)
                                   
                    self.Boren = QLabel()
                    q16Edit = QLineEdit('{:12.2f}'.format(rpsel[16]))
                    q16Edit.setFixedWidth(150)
                    q16Edit.setAlignment(Qt.AlignRight)
                    q16Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q16Edit.setDisabled(True)
                    
                    self.Sfrezen = QLabel()
                    q17Edit = QLineEdit('{:12.2f}'.format(rpsel[17]))
                    q17Edit.setFixedWidth(150)
                    q17Edit.setAlignment(Qt.AlignRight)
                    q17Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q17Edit.setDisabled(True)
                    
                    self.Frezen = QLabel()
                    q18Edit = QLineEdit('{:12.2f}'.format(rpsel[18]))
                    q18Edit.setFixedWidth(150)
                    q18Edit.setAlignment(Qt.AlignRight)
                    q18Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q18Edit.setDisabled(True)
                    
                    self.Sdraaien_klein = QLabel()
                    q19Edit = QLineEdit('{:12.2f}'.format(rpsel[19]))
                    q19Edit.setFixedWidth(150)
                    q19Edit.setAlignment(Qt.AlignRight)
                    q19Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q19Edit.setDisabled(True)

                    self.Draaien_klein = QLabel()
                    q20Edit = QLineEdit('{:12.2f}'.format(rpsel[20]))
                    q20Edit.setFixedWidth(150)
                    q20Edit.setAlignment(Qt.AlignRight)
                    q20Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q20Edit.setDisabled(True)
                    
                    self.SDraaien_groot = QLabel()
                    q21Edit = QLineEdit('{:12.2f}'.format(rpsel[21]))
                    q21Edit.setFixedWidth(150)
                    q21Edit.setAlignment(Qt.AlignRight)
                    q21Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q21Edit.setDisabled(True)
                  
                    self.Draaien_groot = QLabel()
                    q22Edit = QLineEdit('{:12.2f}'.format(rpsel[22]))
                    q22Edit.setFixedWidth(150)
                    q22Edit.setAlignment(Qt.AlignRight)
                    q22Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q22Edit.setDisabled(True)
                 
                    self.Stappen = QLabel()
                    q23Edit = QLineEdit('{:12.2f}'.format(rpsel[23]))
                    q23Edit.setFixedWidth(150)
                    q23Edit.setAlignment(Qt.AlignRight)
                    q23Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q23Edit.setDisabled(True)
                       
                    self.Tappen = QLabel()
                    q24Edit = QLineEdit('{:12.2f}'.format(rpsel[24]))
                    q24Edit.setFixedWidth(150)
                    q24Edit.setAlignment(Qt.AlignRight)
                    q24Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q24Edit.setDisabled(True)
                    
                    self.Snube_draaien = QLabel()
                    q25Edit = QLineEdit('{:12.2f}'.format(rpsel[25]))
                    q25Edit.setFixedWidth(150)
                    q25Edit.setAlignment(Qt.AlignRight)
                    q25Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q25Edit.setDisabled(True)
                    
                    self.Nube_draaien = QLabel()
                    q26Edit = QLineEdit('{:12.2f}'.format(rpsel[26]))
                    q26Edit.setFixedWidth(150)
                    q26Edit.setAlignment(Qt.AlignRight)
                    q26Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q26Edit.setDisabled(True)
                    
                    self.Snube_bewerken = QLabel()
                    q27Edit = QLineEdit('{:12.2f}'.format(rpsel[27]))
                    q27Edit.setFixedWidth(150)
                    q27Edit.setAlignment(Qt.AlignRight)
                    q27Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q27Edit.setDisabled(True)

                    self.Nube_bewerken = QLabel()
                    q28Edit = QLineEdit('{:12.2f}'.format(rpsel[28]))
                    q28Edit.setFixedWidth(150)
                    q28Edit.setAlignment(Qt.AlignRight)
                    q28Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q28Edit.setDisabled(True)
                    
                    self.Sknippen = QLabel()
                    q29Edit = QLineEdit('{:12.2f}'.format(rpsel[29]))
                    q29Edit.setFixedWidth(150)
                    q29Edit.setAlignment(Qt.AlignRight)
                    q29Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q29Edit.setDisabled(True)
                       
                    self.Knippen = QLabel()
                    q30Edit = QLineEdit('{:12.2f}'.format(rpsel[30]))
                    q30Edit.setFixedWidth(150)
                    q30Edit.setAlignment(Qt.AlignRight)
                    q30Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q30Edit.setDisabled(True)
                    
                    self.Skanten = QLabel()
                    q31Edit = QLineEdit('{:12.2f}'.format(rpsel[31]))
                    q31Edit.setFixedWidth(150)
                    q31Edit.setAlignment(Qt.AlignRight)
                    q31Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q31Edit.setDisabled(True)
                            
                    self.Kanten = QLabel()
                    q32Edit = QLineEdit('{:12.2f}'.format(rpsel[32]))
                    q32Edit.setFixedWidth(150)
                    q32Edit.setAlignment(Qt.AlignRight)
                    q32Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q32Edit.setDisabled(True)

                    self.Sstansen = QLabel()
                    q33Edit = QLineEdit('{:12.2f}'.format(rpsel[33]))
                    q33Edit.setFixedWidth(150)
                    q33Edit.setAlignment(Qt.AlignRight)
                    q33Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q33Edit.setDisabled(True)
                    
                    self.Stansen = QLabel()
                    q34Edit = QLineEdit('{:12.2f}'.format(rpsel[34]))
                    q34Edit.setFixedWidth(150)
                    q34Edit.setAlignment(Qt.AlignRight)
                    q34Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q34Edit.setDisabled(True)
                    
                    self.Slassen_CO2 = QLabel()
                    q35Edit = QLineEdit('{:12.2f}'.format(rpsel[35]))
                    q35Edit.setFixedWidth(150)
                    q35Edit.setAlignment(Qt.AlignRight)
                    q35Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q35Edit.setDisabled(True)
                    
                    self.Lassen_CO2 = QLabel()
                    q36Edit = QLineEdit('{:12.2f}'.format(rpsel[36]))
                    q36Edit.setFixedWidth(150)
                    q36Edit.setAlignment(Qt.AlignRight)
                    q36Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q36Edit.setDisabled(True)

                    self.Slassen_hand = QLabel()
                    q37Edit = QLineEdit('{:12.2f}'.format(rpsel[37]))
                    q37Edit.setFixedWidth(150)
                    q37Edit.setAlignment(Qt.AlignRight)
                    q37Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q37Edit.setDisabled(True)
                    
                    self.Lassen_hand = QLabel()
                    q38Edit = QLineEdit('{:12.2f}'.format(rpsel[38]))
                    q38Edit.setFixedWidth(150)
                    q38Edit.setAlignment(Qt.AlignRight)
                    q38Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q38Edit.setDisabled(True)
                    
                    self.Sverpakken = QLabel()
                    q39Edit = QLineEdit('{:12.2f}'.format(rpsel[39]))
                    q39Edit.setFixedWidth(150)
                    q39Edit.setAlignment(Qt.AlignRight)
                    q39Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q39Edit.setDisabled(True)                    
                     
                    self.Verpakken = QLabel()
                    q40Edit = QLineEdit('{:12.2f}'.format(rpsel[40]))
                    q40Edit.setFixedWidth(150)
                    q40Edit.setAlignment(Qt.AlignRight)
                    q40Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q40Edit.setDisabled(True)
                                        
                    self.Sverzinken = QLabel()
                    q41Edit = QLineEdit('{:12.2f}'.format(rpsel[41]))
                    q41Edit.setFixedWidth(150)
                    q41Edit.setAlignment(Qt.AlignRight)
                    q41Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q41Edit.setDisabled(True)
                                        
                    self.Verzinken = QLabel()
                    q42Edit = QLineEdit('{:12.2f}'.format(rpsel[42]))
                    q42Edit.setFixedWidth(150)
                    q42Edit.setAlignment(Qt.AlignRight)
                    q42Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q42Edit.setDisabled(True)

                    self.Smoffelen = QLabel()
                    q43Edit = QLineEdit('{:12.2f}'.format(rpsel[43]))
                    q43Edit.setFixedWidth(150)
                    q43Edit.setAlignment(Qt.AlignRight)
                    q43Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q43Edit.setDisabled(True)
                   
                    self.Moffelen = QLabel()
                    q44Edit = QLineEdit('{:12.2f}'.format(rpsel[44]))
                    q44Edit.setFixedWidth(150)
                    q44Edit.setAlignment(Qt.AlignRight)
                    q44Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q44Edit.setDisabled(True)
                    
                    self.Sschilderen = QLabel()
                    q45Edit = QLineEdit('{:12.2f}'.format(rpsel[45]))
                    q45Edit.setFixedWidth(150)
                    q45Edit.setAlignment(Qt.AlignRight)
                    q45Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q45Edit.setDisabled(True)
                    
                    self.Schilderen = QLabel()
                    q46Edit = QLineEdit('{:12.2f}'.format(rpsel[46]))
                    q46Edit.setFixedWidth(150)
                    q46Edit.setAlignment(Qt.AlignRight)
                    q46Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q46Edit.setDisabled(True)
                    
                    self.Sspuiten = QLabel()
                    q47Edit = QLineEdit('{:12.2f}'.format(rpsel[47]))
                    q47Edit.setFixedWidth(150)
                    q47Edit.setAlignment(Qt.AlignRight)
                    q47Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q47Edit.setDisabled(True)
                    
                    self.Spuiten = QLabel()
                    q48Edit = QLineEdit('{:12.2f}'.format(rpsel[48]))
                    q48Edit.setFixedWidth(150)
                    q48Edit.setAlignment(Qt.AlignRight)
                    q48Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q48Edit.setDisabled(True)
                    
                    self.Sponsen = QLabel()
                    q49Edit = QLineEdit('{:12.2f}'.format(rpsel[49]))
                    q49Edit.setFixedWidth(150)
                    q49Edit.setAlignment(Qt.AlignRight)
                    q49Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q49Edit.setDisabled(True)
                    
                    self.Ponsen = QLabel()
                    q50Edit = QLineEdit('{:12.2f}'.format(rpsel[50]))
                    q50Edit.setFixedWidth(150)
                    q50Edit.setAlignment(Qt.AlignRight)
                    q50Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q50Edit.setDisabled(True)
                    
                    self.Spersen = QLabel()
                    q51Edit = QLineEdit('{:12.2f}'.format(rpsel[51]))
                    q51Edit.setFixedWidth(150)
                    q51Edit.setAlignment(Qt.AlignRight)
                    q51Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q51Edit.setDisabled(True)                    
                    
                    self.Persen = QLabel()
                    q52Edit = QLineEdit('{:12.2f}'.format(rpsel[52]))
                    q52Edit.setFixedWidth(150)
                    q52Edit.setAlignment(Qt.AlignRight)
                    q52Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q52Edit.setDisabled(True) 

                    self.Sgritstralen = QLabel()
                    q53Edit = QLineEdit('{:12.2f}'.format(rpsel[53]))
                    q53Edit.setFixedWidth(150)
                    q53Edit.setAlignment(Qt.AlignRight)
                    q53Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q53Edit.setDisabled(True) 
                    
                    self.Gritstralen = QLabel()
                    q54Edit = QLineEdit('{:12.2f}'.format(rpsel[54]))
                    q54Edit.setAlignment(Qt.AlignRight)
                    q54Edit.setFixedWidth(150)
                    q54Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q54Edit.setDisabled(True) 
                    
                    self.Smontage = QLabel()
                    q55Edit = QLineEdit('{:12.2f}'.format(rpsel[55]))
                    q55Edit.setFixedWidth(150)
                    q55Edit.setAlignment(Qt.AlignRight)
                    q55Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q55Edit.setDisabled(True) 
                                     
                    self.Montage = QLabel()
                    q56Edit = QLineEdit('{:12.2f}'.format(rpsel[56]))
                    q56Edit.setFixedWidth(150)
                    q56Edit.setAlignment(Qt.AlignRight)
                    q56Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q56Edit.setDisabled(True)  
                                                                          
                    grid = QGridLayout()
                    grid.setSpacing(20)
                    
                    lbl1 = QLabel('Cluster number')
                    lbl1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl1, 1, 0)
                    
                    lbl2 = QLabel(clusternr)
                    grid.addWidget(lbl2, 1, 1)
                           
                    lbl3 = QLabel('Description')
                    lbl3.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl3, 1, 2)
                    grid.addWidget(q1Edit, 1, 3, 1, 3) # RowSpan 1 ,ColumnSpan 3
                                                         
                    lbl4 = QLabel('Price')
                    lbl4.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl4, 2, 0)
                    grid.addWidget(q2Edit, 2, 1)
                    
                    lbl5 = QLabel('Unit')
                    lbl5.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl5, 2, 2)
                    grid.addWidget(q3Edit, 2, 3)
                    
                    lbl6 = QLabel('Materials')
                    lbl6.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl6, 2, 4)
                    grid.addWidget(q4Edit, 2, 5)
                    
                    lbl7 = QLabel('Wages')
                    lbl7.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl7, 2, 6)
                    grid.addWidget(q5Edit, 2, 7)
                    
                    lbl8 = QLabel('Services')
                    lbl8.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl8, 3, 0)
                    grid.addWidget(q6Edit, 3, 1)
                    
                    lbl9 = QLabel('Equipment')
                    lbl9.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl9, 3, 2)
                    grid.addWidget(q7Edit, 3, 3)
                    
                    lbl10 = QLabel('Hiring')
                    lbl10.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl10, 3, 4)
                    grid.addWidget(q8Edit, 3, 5)
                    
                    lbl11 = QLabel('Set costs\nsawing')
                    lbl11.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl11, 4, 0)
                    grid.addWidget(q9Edit, 4, 1)
                    
                    lbl12 = QLabel('Sawing')
                    lbl12.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl12, 4, 2)
                    grid.addWidget(q10Edit, 4, 3)
                    
                    lbl13 = QLabel('Set costs\nplaning')
                    lbl13.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl13, 4, 4)
                    grid.addWidget(q11Edit, 4, 5)
                      
                    lbl14 = QLabel('Planing')
                    lbl14.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl14, 4, 6)
                    grid.addWidget(q12Edit, 4, 7)
                    
                    lbl15 = QLabel('Set costs\nstabbing')
                    lbl15.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl15, 5, 0)
                    grid.addWidget(q13Edit, 5, 1)
                    
                    lbl16 = QLabel('Stabbing')
                    lbl16.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl16, 5, 2)
                    grid.addWidget(q14Edit, 5, 3)
                    
                    lbl17 = QLabel('Set costs\ndrilling')
                    lbl17.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl17, 5, 4)
                    grid.addWidget(q15Edit, 5, 5)
                    
                    lbl18 = QLabel('Drilling')
                    lbl18.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl18, 5, 6)
                    grid.addWidget(q16Edit, 5, 7)
                    
                    lbl19 = QLabel('Set costs\nmilling')
                    lbl19.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl19, 6, 0)
                    grid.addWidget(q17Edit, 6, 1)
                    
                    lbl20 = QLabel('Milling')
                    lbl20.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl20, 6, 2)
                    grid.addWidget(q18Edit, 6, 3)
                    
                    lbl21 = QLabel('Set costs\nturning small')
                    lbl21.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl21, 6, 4)
                    grid.addWidget(q19Edit, 6, 5)
                    
                    lbl22 = QLabel('Turning small')
                    lbl22.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl22, 6, 6)
                    grid.addWidget(q20Edit, 6, 7)
                    
                    lbl23 = QLabel('Set costs\nturning big')
                    lbl23.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl23, 7, 0)
                    grid.addWidget(q21Edit, 7, 1)
                    
                    lbl26 = QLabel('Turning big')
                    lbl26.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl26, 7, 2)
                    grid.addWidget(q22Edit, 7, 3)
                    
                    lbl27 = QLabel('Set costs\nthreading')
                    lbl27.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl27, 7, 4)
                    grid.addWidget(q23Edit, 7, 5)
                    
                    lbl28 = QLabel('Threading')
                    lbl28.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl28, 7, 6)
                    grid.addWidget(q24Edit, 7, 7)
                    
                    lbl27 = QLabel('Set costs\nCNC turning')
                    lbl27.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl27, 8, 0)
                    grid.addWidget(q25Edit, 8, 1)
                    
                    lbl28 = QLabel('CNC turning')
                    lbl28.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl28, 8, 2)
                    grid.addWidget(q26Edit, 8, 3)
                    
                    lbl29 = QLabel('Set costs\nCNC milling')
                    lbl29.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl29, 8, 4)
                    grid.addWidget(q27Edit, 8, 5)
                    
                    lbl30 = QLabel('CNC milling')
                    lbl30.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl30, 8, 6)
                    grid.addWidget(q28Edit, 8, 7)
                    
                    lbl31 = QLabel('Set costs\ncutting')
                    lbl31.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl31, 9, 0)
                    grid.addWidget(q29Edit, 9, 1)
                    
                    lbl32 = QLabel('Cutting')
                    lbl32.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl32, 9, 2)
                    grid.addWidget(q30Edit, 9, 3)
                    
                    lbl33 = QLabel('Set costs\nfolding')
                    lbl33.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl33, 9, 4)
                    grid.addWidget(q31Edit, 9, 5)
                    
                    lbl34 = QLabel('Folding')
                    lbl34.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl34, 9, 6)
                    grid.addWidget(q32Edit, 9, 7)
                    
                    lbl35 = QLabel('Set costs\nstamping')
                    lbl35.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl35, 10, 0)
                    grid.addWidget(q33Edit, 10, 1)
                    
                    lbl36 = QLabel('Stamping')
                    lbl36.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl36, 10, 2)
                    grid.addWidget(q34Edit, 10, 3)
                    
                    lbl37 = QLabel('Set costs\nwelding co2')
                    lbl37.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl37, 10, 4)
                    grid.addWidget(q35Edit, 10, 5)
                    
                    lbl38 = QLabel('Welding co2')
                    lbl38.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl38, 10, 6)
                    grid.addWidget(q36Edit, 10, 7)
                    
                    lbl39 = QLabel('Set costs\nwelding hand')
                    lbl39.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl39, 11, 0)
                    grid.addWidget(q37Edit, 11, 1)
                    
                    lbl40 = QLabel('Welding hand')
                    lbl40.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl40, 11, 2)
                    grid.addWidget(q38Edit, 11, 3)
                    
                    lbl41 = QLabel('Set costs\npacking')
                    lbl41.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl41, 11, 4)
                    grid.addWidget(q39Edit, 11, 5)
                        
                    lbl42 = QLabel('Packing')
                    lbl42.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl42, 11, 6)
                    grid.addWidget(q40Edit, 11, 7)
                    
                    lbl43 = QLabel('Set costs\ngalvanise')
                    lbl43.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl43, 12, 0)
                    grid.addWidget(q41Edit, 12, 1)
                    
                    lbl44 = QLabel('Galvanise')
                    lbl44.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl44, 12, 2)
                    grid.addWidget(q42Edit, 12, 3)
                    
                    lbl45 = QLabel('Set costs\nmuffling')
                    lbl45.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl45, 12, 4)
                    grid.addWidget(q43Edit, 12, 5)
                    
                    lbl46 = QLabel('muffling')
                    lbl46.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl46, 12, 6)
                    grid.addWidget(q44Edit, 12, 7)
                    
                    lbl47 = QLabel('Set costs\npainting')
                    lbl47.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl47, 13, 0)
                    grid.addWidget(q45Edit, 13, 1)
                    
                    lbl48 = QLabel('Painting')
                    lbl48.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl48, 13, 2)
                    grid.addWidget(q46Edit, 13, 3)
                    
                    lbl49 = QLabel('Set costs\nspraying')
                    lbl49.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl49, 13, 4)
                    grid.addWidget(q47Edit, 13, 5)
                                                              
                    lbl50 = QLabel('Spraying')
                    lbl50.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl50, 13, 6)
                    grid.addWidget(q48Edit, 13, 7)
                    
                    lbl51 = QLabel('Set costs\npunching')
                    lbl51.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl51, 14, 0)
                    grid.addWidget(q49Edit, 14, 1)
                 
                    lbl52 = QLabel('Punching')
                    lbl52.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl52, 14, 2)
                    grid.addWidget(q50Edit, 14, 3)
                    
                    lbl53 = QLabel('Set costs\npressing')
                    lbl53.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl53, 14, 4)
                    grid.addWidget(q51Edit, 14, 5)
                    
                    lbl54 = QLabel('Pressing')
                    lbl54.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl54, 14, 6)
                    grid.addWidget(q52Edit, 14, 7)
                    
                    lbl55 = QLabel('Set costs\ngrit blasting')
                    lbl55.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl55, 15, 0)
                    grid.addWidget(q53Edit, 15, 1)
                    
                    lbl56 = QLabel('Grit blasting')
                    lbl56.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl56, 15, 2)
                    grid.addWidget(q54Edit, 15, 3)
                    
                    lbl57 = QLabel('Set costs\nmounting')
                    lbl57.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl57, 15, 4)
                    grid.addWidget(q55Edit, 15, 5)
                    
                    lbl58 = QLabel('Mounting')
                    lbl58.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl58, 15, 6)
                    grid.addWidget(q56Edit, 15, 7)
                          
                    lbl = QLabel()
                    pixmap = QPixmap('./images/logos/verbinding.jpg')
                    lbl.setPixmap(pixmap)
                    grid.addWidget(lbl, 0, 0, 1, 1, Qt.AlignRight)
                                     
                    logo = QLabel()
                    pixmap = QPixmap('./images/logos/logo.jpg')
                    logo.setPixmap(pixmap)
                    grid.addWidget(logo , 0, 7, 1 , 1, Qt.AlignRight)
                    
                    grid.addWidget(QLabel('Request internal clusters'), 0, 1, 1, 8, Qt.AlignCenter)
                                                    
                    grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 18, 0, 1, 8, Qt.AlignCenter)
                    self.setLayout(grid)
                    self.setGeometry(300, 100, 150, 150)
            
                    sluitBtn = QPushButton('Close')
                    sluitBtn.clicked.connect(self.close)
            
                    grid.addWidget(sluitBtn, 17, 7, 1, 1, Qt.AlignRight)
                    sluitBtn.setFont(QFont("Arial",10))
                    sluitBtn.setFixedWidth(100)
                    sluitBtn.setStyleSheet("color: black;  background-color: gainsboro")
                                                                                              
            mainWin = MainWindow()
            mainWin.exec_()

    win = MyWindow(data_list, header)
    win.exec_()
    zoeken(m_email)