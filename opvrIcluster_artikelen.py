from login import hoofdMenu
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QWidget, QTableView, QVBoxLayout, QComboBox,\
     QDialog, QLabel, QGridLayout, QPushButton, QMessageBox, QLineEdit
   
from sqlalchemy import (Table, Column, Integer, String, Float, ForeignKey,\
                        MetaData, create_engine)
from sqlalchemy.sql import select, and_
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
    msg.setWindowTitle('Request cluster articles')
    logger.debug("<<< Exiting geenRecord()")
    msg.exec_()
    
def geenRegels():
    logger.debug(">>> Entering geenRegels()")
    msg = QMessageBox()
    logger.debug("geenRegels(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('There are no article rules for this cluster yet!')
    msg.setWindowTitle('Request cluster articles')
    logger.debug("<<< Exiting geenRegels()")
    msg.exec_()
    
def ongInvoer():
    logger.debug(">>> Entering ongInvoer()")
    msg = QMessageBox()
    logger.debug("ongInvoer(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Please re-enter incorrect input\nsearch term!')
    msg.setWindowTitle('Request cluster articles')
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
            k0Edit.setFixedWidth(340)
            k0Edit.setFont(QFont("Arial",10))
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.addItem('            Cluster Groups Sort Key')
            k0Edit.addItem('0. Alle Clusters')
            k0Edit.addItem('LA-LK. Machined parts')
            k0Edit.addItem('MA-MK. Bolts and nuts')
            k0Edit.addItem('NA-NK. Casting machining')
            k0Edit.addItem('OA-OK. Welding composite')
            k0Edit.addItem('PA-PK. Sheet metal assembled')
            k0Edit.addItem('RA-RK. Plastic parts')
            k0Edit.addItem('SA-SK. Prefab mounting parts')
            k0Edit.addItem('TA-TK. Composite parts')
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
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 3, 0, 1, 3, Qt.AlignRight)
            
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
    zoekterm = ''
    if not data[0] or data[0][0] == ' ':
        ongInvoer()
        zoeken(m_email)
    elif data[0]:
        zoekterm = data[0][0]
    toonIclusterartikelen(zoekterm, m_email)
    
def  toonIclusterartikelen(zoekterm, m_email):
    logger.debug(">>> Entering toonIclusterartikelen(zoekterm=%s,m_email=%s)", zoekterm, m_email)
    import validZt                     
    class MyWindow(QDialog):
        logger.debug("<<< Exiting toonIclusterartikelen(zoekterm=%s,m_email=%s)", zoekterm, m_email)
        def __init__(self, data_list, header, *args):
            QWidget.__init__(self, *args,)
            self.setGeometry(50, 50, 1800, 900)
            self.setWindowTitle('Request articles per cluster')
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
            logger.debug("__init__(self=%s): q1Edit → %s", self, q1Edit)
            logger.debug("__init__(): q6Edit → %s", q6Edit)
            logger.debug("__init__(self=%s): q6Edit → %s", self, q6Edit)
            logger.debug("__init__(): q2Edit → %s", q2Edit)
            logger.debug("__init__(self=%s): q2Edit → %s", self, q2Edit)
            logger.debug("__init__(): q3Edit → %s", q3Edit)
            logger.debug("__init__(self=%s): q3Edit → %s", self, q3Edit)
            logger.debug("__init__(): q5Edit → %s", q5Edit)
            logger.debug("__init__(self=%s): q5Edit → %s", self, q5Edit)
            logger.debug("__init__(): lbl1 → %s", lbl1)
            logger.debug("__init__(self=%s): lbl1 → %s", self, lbl1)
            logger.debug("__init__(): lbl2 → %s", lbl2)
            logger.debug("__init__(self=%s): lbl2 → %s", self, lbl2)
            logger.debug("__init__(): lbl9 → %s", lbl9)
            logger.debug("__init__(self=%s): lbl9 → %s", self, lbl9)
            logger.debug("__init__(): lbl10 → %s", lbl10)
            logger.debug("__init__(self=%s): lbl10 → %s", self, lbl10)
            logger.debug("__init__(): lbl3 → %s", lbl3)
            logger.debug("__init__(self=%s): lbl3 → %s", self, lbl3)
            logger.debug("__init__(): lbl8 → %s", lbl8)
            logger.debug("__init__(self=%s): lbl8 → %s", self, lbl8)
            logger.debug("__init__(): lbl4 → %s", lbl4)
            logger.debug("__init__(self=%s): lbl4 → %s", self, lbl4)
            logger.debug("__init__(): lbl5 → %s", lbl5)
            logger.debug("__init__(self=%s): lbl5 → %s", self, lbl5)
            logger.debug("__init__(): lbl7 → %s", lbl7)
            logger.debug("__init__(self=%s): lbl7 → %s", self, lbl7)
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
              
    header = ['Cluster number', 'Description', 'Price', 'Unit', 'Materials', 'Wages',\
              'Services', 'Equipment', 'Hiring', 'Sawing', 'Planing','Stabbing',\
              'Drilling', 'Milling', 'Turning small', 'Turning big', 'Threading',\
              'CNC turning', 'CNC milling', 'Cutting', 'Folding',\
              'Die-cutting', 'Welding CO2', 'Welding hand', 'Packing', 'Galvanise',\
              'Muffling', 'Painting', 'Spraying', 'Punching','Pressing','Grit blasting']
    
    metadata = MetaData()
    iclusters = Table('iclusters', metadata,
        Column('iclusterID', Integer(), primary_key=True),
        Column('omschrijving', String),
        Column('prijs', Float),
        Column('eenheid', String),
        Column('materialen', Float),
        Column('lonen', Float),
        Column('diensten', Float),
        Column('materieel', Float),
        Column('inhuur', Float),
        Column('zagen', Float),
        Column('schaven', Float),
        Column('steken', Float),
        Column('boren', Float),
        Column('frezen', Float),
        Column('draaien_klein', Float),
        Column('draaien_groot', Float),
        Column('tappen', Float),
        Column('nube_draaien', Float),
        Column('nube_bewerken', Float),
        Column('knippen', Float),
        Column('kanten', Float),
        Column('stansen', Float),
        Column('lassen_co2', Float),
        Column('lassen_hand', Float),
        Column('verpakken', Float),
        Column('verzinken', Float),
        Column('moffelen', Float),
        Column('schilderen', Float),
        Column('spuiten', Float),
        Column('ponsen', Float),
        Column('persen', Float),
        Column('gritstralen', Float))
       
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
     
    if zoekterm == '0':
        sel = select([iclusters]).order_by(iclusters.c.iclusterID)
    elif validZt.zt(zoekterm, 25):
        sel = select([iclusters]).where(iclusters.c.iclusterID.ilike(zoekterm+'%'))\
                              .order_by(iclusters.c.iclusterID)
    else:
        ongInvoer()
        zoeken(m_email)
        
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
        clusternr = str(idx.data())
        logger.debug("showSelection(idx=%s): clusternr → %s", idx, clusternr)
        if idx.column() == 0:
            metadata = MetaData()
            logger.debug("showSelection(idx=%s): metadata → %s", idx, metadata)
            iclusters = Table('iclusters', metadata,
                Column('iclusterID', Integer, primary_key=True),
                Column('omschrijving', String))
            artikelen = Table('artikelen', metadata,
                Column('artikelID', Integer, primary_key=True),
                Column('artikelomschrijving', String),
                Column('artikelprijs', Float))
            icluster_artikelen = Table('icluster_artikelen', metadata,
                Column('icluster_artID', Integer, primary_key=True),
                Column('iclusterID', None, ForeignKey('iclusters.iclusterID')),
                Column('artikelID', None, ForeignKey('artikelen.artikelID')),
                Column('hoeveelheid', Float))
    
            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            logger.debug("showSelection(idx=%s): engine → %s", idx, engine)
            con = engine.connect()
            selcl = select([icluster_artikelen, iclusters, artikelen]).where(and_\
             (icluster_artikelen.c.iclusterID == clusternr, icluster_artikelen.c.iclusterID==\
              iclusters.c.iclusterID, icluster_artikelen.c.artikelID == artikelen.c.artikelID))
            logger.debug("showSelection(idx=%s): con → %s", idx, con)
            if con.execute(selcl).fetchone():
                rpsel = con.execute(selcl)
                logger.debug("showSelection(idx=%s): selcl → %s", idx, selcl)
            else:
                geenRegels()
                logger.debug("showSelection(idx=%s): rpsel → %s", idx, rpsel)
                return
            regel = 0
            logger.debug("<<< Exiting showSelection(idx=%s)", idx)
            logger.debug("showSelection(idx=%s): regel → %s", idx, regel)
            for row in rpsel:
                regel += 1
                class MainWindow(QDialog):
                    def __init__(self):
                        QDialog.__init__(self)
                        
                        grid = QGridLayout()
                        grid.setSpacing(20)
                        self.setWindowTitle("Request article lines per cluster")
                        self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
                        
                        self.setFont(QFont('Arial', 10))   
                        
                        q1Edit = QLineEdit(str(row[5]))
                        q1Edit.setFixedWidth(400)
                        q1Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                        q1Edit.setDisabled(True)
                        
                        q6Edit = QLineEdit(str(row[2]))
                        q6Edit.setFixedWidth(150)
                        q6Edit.setAlignment(Qt.AlignRight)
                        q6Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                        q6Edit.setDisabled(True)
                                       
                        q2Edit = QLineEdit('{:12.2f}'.format(row[8]))
                        q2Edit.setFixedWidth(150)
                        q2Edit.setAlignment(Qt.AlignRight)
                        q2Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                        q2Edit.setDisabled(True)
                         
                        q3Edit = QLineEdit('{:12.2f}'.format(row[3]))
                        q3Edit.setFixedWidth(150)
                        q3Edit.setAlignment(Qt.AlignRight)
                        q3Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                        q3Edit.setDisabled(True)
                        
                        q5Edit = QLineEdit(str(row[7]))
                        q5Edit.setFixedWidth(400)
                        q5Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                        q5Edit.setDisabled(True)
                                               
                        grid = QGridLayout()
                        grid.setSpacing(20)
                        
                        lbl1 = QLabel('Cluster number')
                        lbl1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                        grid.addWidget(lbl1, 1, 0)
                        
                        lbl2 = QLabel(clusternr)
                        grid.addWidget(lbl2, 1, 1)
                        
                        lbl9 = QLabel('Line number: ')
                        lbl9.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                        grid.addWidget(lbl9, 1, 2)
                        
                        lbl10 = QLabel(str(regel))
                        grid.addWidget(lbl10, 1, 3)
                               
                        lbl3 = QLabel('Cluster description')
                        lbl3.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                        grid.addWidget(lbl3, 2, 0)
                        grid.addWidget(q1Edit, 2, 1, 1, 3) 
                        
                        lbl8 = QLabel('Article number')
                        lbl8.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                        grid.addWidget(lbl8, 3, 0)
                        grid.addWidget(q6Edit, 3, 1)
                                                                
                        lbl4 = QLabel('Article price')
                        lbl4.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                        grid.addWidget(lbl4, 4, 0)
                        grid.addWidget(q2Edit, 4, 1)
                        
                        lbl5 = QLabel('Quantity\nArticles per cluster')
                        lbl5.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                        grid.addWidget(lbl5, 5, 0)
                        grid.addWidget(q3Edit, 5, 1)
                       
                        lbl7 = QLabel('Article description')
                        lbl7.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                        grid.addWidget(lbl7, 6, 0)
                        grid.addWidget(q5Edit, 6, 1, 1, 3)
                      
                        lbl = QLabel()
                        pixmap = QPixmap('./images/logos/verbinding.jpg')
                        lbl.setPixmap(pixmap)
                        grid.addWidget(lbl, 0, 0, 1, 2)
                        
                        logo = QLabel()
                        pixmap = QPixmap('./images/logos/logo.jpg')
                        logo.setPixmap(pixmap)
                        grid.addWidget(logo , 0, 3, 1 , 1, Qt.AlignRight)
                                                         
                        grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 8, 0, 1, 4, Qt.AlignCenter)
                          
                        self.setLayout(grid)
                        self.setGeometry(500, 300, 150, 150)
                
                        applyBtn = QPushButton('Lines')
                        applyBtn.clicked.connect(self.accept)
                
                        grid.addWidget(applyBtn, 7, 3, 1, 1, Qt.AlignRight)
                        applyBtn.setFont(QFont("Arial",10))
                        applyBtn.setFixedWidth(100)
                        applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
                                                                                                                          
                mainWin = MainWindow()
                mainWin.exec_()    
    
    win = MyWindow(data_list, header)
    win.exec_()
    zoeken(m_email)