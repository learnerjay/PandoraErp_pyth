from login import hoofdMenu
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QWidget, QTableView, QVBoxLayout, QComboBox,\
      QDialog, QLabel, QGridLayout, QPushButton, QMessageBox, QLineEdit
    
from sqlalchemy import (Table, Column, String, Float, MetaData, create_engine)
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
    
def ongInvoer():
    logger.debug(">>> Entering ongInvoer()")
    msg = QMessageBox()
    logger.debug("ongInvoer(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Invalid entry')
    msg.setWindowTitle('Request clusters')
    logger.debug("<<< Exiting ongInvoer()")
    msg.exec_()

def windowSluit(self, m_email):
    logger.debug(">>> Entering windowSluit(m_email=%s)", m_email)
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email)
                
def zoeken(m_email):
    logger.debug(">>> Entering zoeken(m_email=%s)", m_email)
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.debug(">>> Entering __init__(parent=%s)", parent)
            self.setWindowTitle("Cluster article lines")
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
            k0Edit.addItem('                       Cluster groups sort key')
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
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))
    
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
    if not data[0] or data[0][0] == ' ':
        ongInvoer()
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
            self.setGeometry(100, 50, 1700, 900)
            self.setWindowTitle('Request clusters')
            self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
            self.setWindowFlags(self.windowFlags()| Qt.WindowSystemMenuHint |
                              Qt.WindowMinMaxButtonsHint)
            table_model = MyTableModel(self, data_list, header)
            table_view = QTableView()
            table_view.setModel(table_model)
            font = QFont("Arial", 10)
            table_view.setFont(font)
            table_view.hideColumn(31)
            table_view.hideColumn(32)
            table_view.hideColumn(33)
            table_view.hideColumn(34)
            table_view.hideColumn(35)
            table_view.hideColumn(36)
            table_view.hideColumn(37)
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
            logger.debug("__init__(self=%s): q1Edit → %s", self, q1Edit)
            logger.debug("__init__(): q2Edit → %s", q2Edit)
            logger.debug("__init__(self=%s): q2Edit → %s", self, q2Edit)
            logger.debug("__init__(): q3Edit → %s", q3Edit)
            logger.debug("__init__(self=%s): q3Edit → %s", self, q3Edit)
            logger.debug("__init__(): q4Edit → %s", q4Edit)
            logger.debug("__init__(self=%s): q4Edit → %s", self, q4Edit)
            logger.debug("__init__(): q5Edit → %s", q5Edit)
            logger.debug("__init__(self=%s): q5Edit → %s", self, q5Edit)
            logger.debug("__init__(): q6Edit → %s", q6Edit)
            logger.debug("__init__(self=%s): q6Edit → %s", self, q6Edit)
            logger.debug("__init__(): q7Edit → %s", q7Edit)
            logger.debug("__init__(self=%s): q7Edit → %s", self, q7Edit)
            logger.debug("__init__(): q8Edit → %s", q8Edit)
            logger.debug("__init__(self=%s): q8Edit → %s", self, q8Edit)
            logger.debug("__init__(): q9Edit → %s", q9Edit)
            logger.debug("__init__(self=%s): q9Edit → %s", self, q9Edit)
            logger.debug("__init__(): q10Edit → %s", q10Edit)
            logger.debug("__init__(self=%s): q10Edit → %s", self, q10Edit)
            logger.debug("__init__(): q11Edit → %s", q11Edit)
            logger.debug("__init__(self=%s): q11Edit → %s", self, q11Edit)
            logger.debug("__init__(): q12Edit → %s", q12Edit)
            logger.debug("__init__(self=%s): q12Edit → %s", self, q12Edit)
            logger.debug("__init__(): q13Edit → %s", q13Edit)
            logger.debug("__init__(self=%s): q13Edit → %s", self, q13Edit)
            logger.debug("__init__(): q14Edit → %s", q14Edit)
            logger.debug("__init__(self=%s): q14Edit → %s", self, q14Edit)
            logger.debug("__init__(): q15Edit → %s", q15Edit)
            logger.debug("__init__(self=%s): q15Edit → %s", self, q15Edit)
            logger.debug("__init__(): q16Edit → %s", q16Edit)
            logger.debug("__init__(self=%s): q16Edit → %s", self, q16Edit)
            logger.debug("__init__(): q17Edit → %s", q17Edit)
            logger.debug("__init__(self=%s): q17Edit → %s", self, q17Edit)
            logger.debug("__init__(): q18Edit → %s", q18Edit)
            logger.debug("__init__(self=%s): q18Edit → %s", self, q18Edit)
            logger.debug("__init__(): q19Edit → %s", q19Edit)
            logger.debug("__init__(self=%s): q19Edit → %s", self, q19Edit)
            logger.debug("__init__(): q20Edit → %s", q20Edit)
            logger.debug("__init__(self=%s): q20Edit → %s", self, q20Edit)
            logger.debug("__init__(): q21Edit → %s", q21Edit)
            logger.debug("__init__(self=%s): q21Edit → %s", self, q21Edit)
            logger.debug("__init__(): q22Edit → %s", q22Edit)
            logger.debug("__init__(self=%s): q22Edit → %s", self, q22Edit)
            logger.debug("__init__(): q23Edit → %s", q23Edit)
            logger.debug("__init__(self=%s): q23Edit → %s", self, q23Edit)
            logger.debug("__init__(): q24Edit → %s", q24Edit)
            logger.debug("__init__(self=%s): q24Edit → %s", self, q24Edit)
            logger.debug("__init__(): q25Edit → %s", q25Edit)
            logger.debug("__init__(self=%s): q25Edit → %s", self, q25Edit)
            logger.debug("__init__(): q26Edit → %s", q26Edit)
            logger.debug("__init__(self=%s): q26Edit → %s", self, q26Edit)
            logger.debug("__init__(): q27Edit → %s", q27Edit)
            logger.debug("__init__(self=%s): q27Edit → %s", self, q27Edit)
            logger.debug("__init__(): q28Edit → %s", q28Edit)
            logger.debug("__init__(self=%s): q28Edit → %s", self, q28Edit)
            logger.debug("__init__(): q29Edit → %s", q29Edit)
            logger.debug("__init__(self=%s): q29Edit → %s", self, q29Edit)
            logger.debug("__init__(): q30Edit → %s", q30Edit)
            logger.debug("__init__(self=%s): q30Edit → %s", self, q30Edit)
            logger.debug("__init__(): q31Edit → %s", q31Edit)
            logger.debug("__init__(self=%s): q31Edit → %s", self, q31Edit)
            logger.debug("__init__(): q32Edit → %s", q32Edit)
            logger.debug("__init__(self=%s): q32Edit → %s", self, q32Edit)
            logger.debug("__init__(): q33Edit → %s", q33Edit)
            logger.debug("__init__(self=%s): q33Edit → %s", self, q33Edit)
            logger.debug("__init__(): q34Edit → %s", q34Edit)
            logger.debug("__init__(self=%s): q34Edit → %s", self, q34Edit)
            logger.debug("__init__(): q35Edit → %s", q35Edit)
            logger.debug("__init__(self=%s): q35Edit → %s", self, q35Edit)
            logger.debug("__init__(): q36Edit → %s", q36Edit)
            logger.debug("__init__(self=%s): q36Edit → %s", self, q36Edit)
            logger.debug("__init__(): q37Edit → %s", q37Edit)
            logger.debug("__init__(self=%s): q37Edit → %s", self, q37Edit)
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

    header = ['Cluster number', 'Description', 'Price', 'Unit', 'Materials', 'Wages', \
              'Services', 'Equipment', 'Hiring', 'hours\nconstruction', 'hours mounting', 'hours\nreturn welding', \
              'hours\nchief mechanic', 'hours\npower-supply', 'hours\nOCL', 'hours\ntrack laying','hours\ntrack welding', \
              'hours\nhiring', 'Trench machine', 'Press machine', 'Atlas crane', \
              'Crane big', 'Mainliner', 'Ballast scrape\nmachine', 'Wagon', 'Locomotor', \
              'Locomotive', 'Assembly\ntrolley', 'Stormobiel', 'hours\ntelecom', 'Robel train', \
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
    
    if keuze == '0':  
        sel = select([clusters]).where(clusters.c.clusterID < 'JL').order_by(clusters.c.clusterID.asc())
    else:
        sel = select([clusters]).where(clusters.c.clusterID.like(keuze+'%'))\
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
            logger.debug("showSelection(idx=%s): con → %s", idx, con)
            selcl = select([clusters]).where(clusters.c.clusterID == clusternr)
            rpsel = con.execute(selcl).first()
            logger.debug("showSelection(idx=%s): selcl → %s", idx, selcl)
            logger.debug("showSelection(idx=%s): rpsel → %s", idx, rpsel)
            
            class MainWindow(QDialog):
                logger.debug("<<< Exiting showSelection(idx=%s)", idx)
                def __init__(self):
                    QDialog.__init__(self)
                    
                    grid = QGridLayout()
                    grid.setSpacing(20)
                    self.setWindowTitle("Request clusters")
                    self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
                    
                    self.setFont(QFont('Arial', 10))   
                    
                    q1Edit = QLineEdit(rpsel[1])#description
                    q1Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q1Edit.setDisabled(True)
                                    
                    q2Edit = QLineEdit('{:12.2f}'.format(rpsel[2])) #price
                    q2Edit.setFixedWidth(150)
                    q2Edit.setAlignment(Qt.AlignRight)
                    q2Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q2Edit.setDisabled(True)
                     
                    q3Edit = QLineEdit(str(rpsel[3]))#unit
                    q3Edit.setFixedWidth(150)
                    q3Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q3Edit.setDisabled(True)
                    
                    q4Edit = QLineEdit('{:12.2f}'.format(rpsel[4]))#materials
                    q4Edit.setFixedWidth(150)
                    q4Edit.setAlignment(Qt.AlignRight)
                    q4Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q4Edit.setDisabled(True)
                    
                    q5Edit = QLineEdit('{:12.2f}'.format(rpsel[5])) #wages
                    q5Edit.setFixedWidth(150)
                    q5Edit.setAlignment(Qt.AlignRight)
                    q5Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q5Edit.setDisabled(True)
                    
                    q6Edit = QLineEdit('{:12.2f}'.format(rpsel[6])) #services
                    q6Edit.setFixedWidth(150)
                    q6Edit.setAlignment(Qt.AlignRight)
                    q6Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q6Edit.setDisabled(True)
                    
                    q7Edit = QLineEdit('{:12.2f}'.format(rpsel[7]))#equipment
                    q7Edit.setFixedWidth(150)
                    q7Edit.setAlignment(Qt.AlignRight)
                    q7Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q7Edit.setDisabled(True)
                    
                    q8Edit = QLineEdit('{:12.2f}'.format(rpsel[8]))#hiring
                    q8Edit.setFixedWidth(150)
                    q8Edit.setAlignment(Qt.AlignRight)
                    q8Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q8Edit.setDisabled(True)
                    
                    q9Edit = QLineEdit('{:12.2f}'.format(rpsel[9]))#hours construction
                    q9Edit.setFixedWidth(150)
                    q9Edit.setAlignment(Qt.AlignRight)
                    q9Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q9Edit.setDisabled(True)
                    
                    q10Edit = QLineEdit('{:12.2f}'.format(rpsel[10]))#hours mounting
                    q10Edit.setFixedWidth(150)
                    q10Edit.setAlignment(Qt.AlignRight)
                    q10Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q10Edit.setDisabled(True)
                    
                    q11Edit = QLineEdit('{:12.2f}'.format(rpsel[11]))#hours return welding
                    q11Edit.setFixedWidth(150)
                    q11Edit.setAlignment(Qt.AlignRight)
                    q11Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q11Edit.setDisabled(True)
                    
                    q12Edit = QLineEdit('{:12.2f}'.format(rpsel[12]))#hours chief mechanic
                    q12Edit.setFixedWidth(150)
                    q12Edit.setAlignment(Qt.AlignRight)
                    q12Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q12Edit.setDisabled(True)

                    q13Edit = QLineEdit('{:12.2f}'.format(rpsel[13]))#hours power-supply
                    q13Edit.setFixedWidth(150)
                    q13Edit.setAlignment(Qt.AlignRight)
                    q13Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q13Edit.setDisabled(True)
                    
                    q14Edit = QLineEdit('{:12.2f}'.format(rpsel[14]))#hours OCL
                    q14Edit.setFixedWidth(150)
                    q14Edit.setAlignment(Qt.AlignRight)
                    q14Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q14Edit.setDisabled(True)
                       
                    q15Edit = QLineEdit('{:12.2f}'.format(rpsel[15]))#hours track laying
                    q15Edit.setFixedWidth(150)
                    q15Edit.setAlignment(Qt.AlignRight)
                    q15Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q15Edit.setDisabled(True)
                    
                    q16Edit = QLineEdit('{:12.2f}'.format(rpsel[16]))#hours track welding
                    q16Edit.setFixedWidth(150)
                    q16Edit.setAlignment(Qt.AlignRight)
                    q16Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q16Edit.setDisabled(True)
                    
                    q17Edit = QLineEdit('{:12.2f}'.format(rpsel[17])) #hours hiring
                    q17Edit.setFixedWidth(150)
                    q17Edit.setAlignment(Qt.AlignRight)
                    q17Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q17Edit.setDisabled(True)
                       
                    q18Edit = QLineEdit('{:12.2f}'.format(rpsel[18])) #hours trench machine
                    q18Edit.setFixedWidth(150)
                    q18Edit.setAlignment(Qt.AlignRight)
                    q18Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q18Edit.setDisabled(True)
                            
                    q19Edit = QLineEdit('{:12.2f}'.format(rpsel[19])) #hours pressing machine
                    q19Edit.setFixedWidth(150)
                    q19Edit.setAlignment(Qt.AlignRight)
                    q19Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q19Edit.setDisabled(True)
                    
                    q20Edit = QLineEdit('{:12.2f}'.format(rpsel[20])) # atlas crane
                    q20Edit.setFixedWidth(150)
                    q20Edit.setAlignment(Qt.AlignRight)
                    q20Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q20Edit.setDisabled(True)
                    
                    q21Edit = QLineEdit('{:12.2f}'.format(rpsel[21])) #crane big
                    q21Edit.setFixedWidth(150)
                    q21Edit.setAlignment(Qt.AlignRight)
                    q21Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q21Edit.setDisabled(True)

                    q22Edit = QLineEdit('{:12.2f}'.format(rpsel[22]))#mainliner
                    q22Edit.setFixedWidth(150)
                    q22Edit.setAlignment(Qt.AlignRight)
                    q22Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q22Edit.setDisabled(True)

                    q23Edit = QLineEdit('{:12.2f}'.format(rpsel[23])) #ballast clearing machine
                    q23Edit.setFixedWidth(150)
                    q23Edit.setAlignment(Qt.AlignRight)
                    q23Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q23Edit.setDisabled(True)

                    q24Edit = QLineEdit('{:12.2f}'.format(rpsel[24])) #wagon
                    q24Edit.setFixedWidth(150)
                    q24Edit.setAlignment(Qt.AlignRight)
                    q24Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q24Edit.setDisabled(True)
  
                    q25Edit = QLineEdit('{:12.2f}'.format(rpsel[25])) #locomotor
                    q25Edit.setFixedWidth(150)
                    q25Edit.setAlignment(Qt.AlignRight)
                    q25Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q25Edit.setDisabled(True)

                    q26Edit = QLineEdit('{:12.2f}'.format(rpsel[26])) #locomotive
                    q26Edit.setFixedWidth(150)
                    q26Edit.setAlignment(Qt.AlignRight)
                    q26Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q26Edit.setDisabled(True)

                    q27Edit = QLineEdit('{:12.2f}'.format(rpsel[27])) #assembly trolley
                    q27Edit.setFixedWidth(150)
                    q27Edit.setAlignment(Qt.AlignRight)
                    q27Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q27Edit.setDisabled(True)
 
                    q28Edit = QLineEdit('{:12.2f}'.format(rpsel[28])) #stormobiel
                    q28Edit.setFixedWidth(150)
                    q28Edit.setAlignment(Qt.AlignRight)
                    q28Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q28Edit.setDisabled(True)
                                 
                    q29Edit = QLineEdit('{:12.2f}'.format(rpsel[29])) #hours telecom
                    q29Edit.setFixedWidth(150)
                    q29Edit.setAlignment(Qt.AlignRight)
                    q29Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q29Edit.setDisabled(True)
                                          
                    q30Edit = QLineEdit('{:12.2f}'.format(rpsel[30])) #robel train
                    q30Edit.setFixedWidth(150)
                    q30Edit.setAlignment(Qt.AlignRight)
                    q30Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q30Edit.setDisabled(True)
                    
                    q31Edit = QLineEdit('{:12.2f}'.format(rpsel[31])) #direction
                    q31Edit.setFixedWidth(150)
                    q31Edit.setAlignment(Qt.AlignRight)
                    q31Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q31Edit.setDisabled(True)
                                    
                    q32Edit = QLineEdit('{:12.2f}'.format(rpsel[32])) # housing
                    q32Edit.setFixedWidth(150)
                    q32Edit.setAlignment(Qt.AlignRight)
                    q32Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q32Edit.setDisabled(True)
                    
                    q33Edit = QLineEdit('{:12.2f}'.format(rpsel[33])) #cable work
                    q33Edit.setFixedWidth(150)
                    q33Edit.setAlignment(Qt.AlignRight)
                    q33Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q33Edit.setDisabled(True)
                    
                    q34Edit = QLineEdit('{:12.2f}'.format(rpsel[34])) #earth moving
                    q34Edit.setAlignment(Qt.AlignRight)
                    q34Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q34Edit.setDisabled(True)
                    
                    q35Edit = QLineEdit('{:12.2f}'.format(rpsel[35])) #concrete work
                    q35Edit.setFixedWidth(150)
                    q35Edit.setAlignment(Qt.AlignRight)
                    q35Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q35Edit.setDisabled(True)
                    
                    q36Edit = QLineEdit('{:12.2f}'.format(rpsel[36])) #Transport
                    q36Edit.setFixedWidth(150)
                    q36Edit.setAlignment(Qt.AlignRight)
                    q36Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q36Edit.setDisabled(True)
                    
                    q37Edit = QLineEdit('{:12.2f}'.format(rpsel[36])) #Remaining
                    q37Edit.setFixedWidth(150)
                    q37Edit.setAlignment(Qt.AlignRight)
                    q37Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q37Edit.setDisabled(True)
                    
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
                    
                    lbl20 = QLabel('Trench machine hours')
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
                                                          
                    lbl29 = QLabel('Mounting hours')
                    lbl29.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl29, 5, 2)
                    grid.addWidget(q27Edit, 5, 3)
                    
                    lbl30 = QLabel('Stormobiel hours')
                    lbl30.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl30, 6, 2)
                    grid.addWidget(q28Edit, 6, 3)
                    
                    lbl31 = QLabel('Telecom hours')
                    lbl31.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl31, 17, 2)
                    grid.addWidget(q29Edit, 17, 3) 
                                        
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
                                                                                                  
                    lbl15 = QLabel('Power-supply hours')
                    lbl15.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl15, 13, 2)
                    grid.addWidget(q13Edit, 13, 3)
                 
                    lbl16 = QLabel('OCL hours')
                    lbl16.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl16, 14, 2)
                    grid.addWidget(q14Edit, 14, 3)
                    
                    lbl17 = QLabel('Track laying hours')
                    lbl17.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl17, 15, 2)
                    grid.addWidget(q15Edit, 15, 3)
                    
                    lbl18 = QLabel('Track welding hours')
                    lbl18.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl18, 16, 2)
                    grid.addWidget(q16Edit, 16, 3)
                    
                    lbl31 = QLabel('Robel train hours')
                    lbl31.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl31, 7, 2)
                    grid.addWidget(q30Edit, 7, 3)

                    lbl = QLabel()
                    pixmap = QPixmap('./images/logos/verbinding.jpg')
                    lbl.setPixmap(pixmap)
                    grid.addWidget(lbl, 0, 0)
                    
                    logo = QLabel()
                    pixmap = QPixmap('./images/logos/logo.jpg')
                    logo.setPixmap(pixmap)
                    grid.addWidget(logo , 0, 3, 1 , 1, Qt.AlignRight)
                                                                   
                    grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 22, 0, 1, 4, Qt.AlignCenter)
                      
                    self.setLayout(grid)
                    self.setGeometry(400, 50, 150, 150)
            
                    applyBtn = QPushButton('Close')
                    applyBtn.clicked.connect(self.close)
            
                    grid.addWidget(applyBtn, 21, 3, 1, 1, Qt.AlignRight| Qt.AlignBottom)
                    applyBtn.setFont(QFont("Arial",10))
                    applyBtn.setFixedWidth(100)
                    applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
                                                                                              
            mainWin = MainWindow()
            mainWin.exec_()

    win = MyWindow(data_list, header)
    win.exec_()
    zoeken(m_email)