from login import hoofdMenu
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtWidgets import QDialog, QWidget, QTableView, QVBoxLayout, QLabel,\
      QLineEdit, QGridLayout, QPushButton
from sqlalchemy import (Table, Column, Integer, String, Float, MetaData,\
                        create_engine, select)
import logging
logger = logging.getLogger(__name__)

def toonResult(m_email):
    logger.debug(">>> Entering toonResult(m_email=%s)", m_email)
    metadata = MetaData()
    logger.debug("toonResult(m_email=%s): metadata → %s", m_email, metadata)
    resultaten = Table('resultaten', metadata,
        Column('resID', Integer(), primary_key=True),
        Column('boekweek', String),
        Column('statusweek', String),
        Column('btotaal', Float),
        Column('wtotaal', Float),
        Column('betaald_bedrag', Float),
        Column('meerminderwerk', Float),
        Column('onderhandenwerk', Float),
        Column('aanneemsom', Float),
        Column('blonen', Float),
        Column('wlonen', Float),
        Column('bmaterialen', Float),
        Column('wmaterialen', Float),
        Column('bmaterieel', Float),
        Column('wmaterieel', Float),
        Column('bprojectkosten', Float),
        Column('wprojectkosten', Float),
        Column('binhuur', Float),
        Column('winhuur', Float),
        Column('bdiensten', Float),
        Column('wdiensten', Float),
        Column('bruto_winst', Float))
    
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
    logger.debug("toonResult(m_email=%s): engine → %s", m_email, engine)
    selres = select([resultaten]).order_by(resultaten.c.boekweek, resultaten.c.statusweek)
    rpres = con.execute(selres)
    logger.debug("toonResult(m_email=%s): con → %s", m_email, con)
    
    class window(QDialog):
        logger.debug("toonResult(m_email=%s): selres → %s", m_email, selres)
        def __init__(self, data_list, header, *args):
            logger.debug("<<< Exiting toonResult(m_email=%s)", m_email)
            QWidget.__init__(self, *args,)
            logger.debug(">>> Entering __init__(data_list=%s,header=%s)", data_list, header)
            self.setGeometry(100, 50, 1700, 900)
            self.setWindowTitle('Request results per book week')
            logger.debug("__init__(data_list=%s,header=%s): font → %s", data_list, header, font)
            logger.debug("__init__(data_list=%s,header=%s): table_view → %s", data_list, header, table_view)
            self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
            self.setWindowFlags(self.windowFlags()| Qt.WindowSystemMenuHint |
                              Qt.WindowMinMaxButtonsHint)
            table_model = MyTableModel(self, data_list, header)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): table_model → %s", self, data_list, header, table_model)
            logger.debug("__init__(data_list=%s,header=%s): table_model → %s", data_list, header, table_model)
            table_view = QTableView()
            logger.debug("__init__(self=%s,data_list=%s,header=%s): table_view → %s", self, data_list, header, table_view)
            table_view.setModel(table_model)
            font = QFont("Arial", 10)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): font → %s", self, data_list, header, font)
            table_view.setFont(font)
            table_view.resizeColumnsToContents()
            table_view.setSelectionBehavior(QTableView.SelectRows)
            table_view.clicked.connect(Resultaten)
            layout = QVBoxLayout(self)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): layout → %s", self, data_list, header, layout)
            logger.debug("__init__(data_list=%s,header=%s): layout → %s", data_list, header, layout)
            layout.addWidget(table_view)
            self.setLayout(layout)
            logger.debug("<<< Exiting __init__(data_list=%s,header=%s)", data_list, header)
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
            logger.debug("__init__(): self.lbl → %s", self.lbl)
            logger.debug("__init__(): self.pixmap → %s", self.pixmap)
            logger.debug("__init__(self=%s): lbl → %s", self, lbl)
            logger.debug("__init__(): self.logo → %s", self.logo)
            logger.debug("__init__(self=%s): logo → %s", self, logo)
            logger.debug("__init__(self=%s): index → %s", self, index)
            logger.debug("__init__(self=%s): horpos → %s", self, horpos)
            logger.debug("__init__(self=%s): verpos → %s", self, verpos)
            logger.debug("__init__(): self.Gegevens → %s", self.Gegevens)
            logger.debug("__init__(): q1Edit → %s", q1Edit)
            logger.debug("__init__(self=%s): q1Edit → %s", self, q1Edit)
            logger.debug("__init__(): terugBtn → %s", terugBtn)
            logger.debug("__init__(self=%s): terugBtn → %s", self, terugBtn)
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
                                       
    header = ['ID','Book week','Status week','Total budgeted','Total realised','Payed amount',\
          'More/less work','Work in progress','Contract price','Wages budgeted','Wages realised',\
          'Materials budgeted','Materials realised','Equipment budgeted','Equipment realised',\
          'Project costs budgeted','Project costs realised','Hiring budgeted','Hiring realised',\
          'Services budgeted','Services realised','Gross profit']

    data_list=[]
    for row in rpres:
        data_list += [(row)]
        
    def Resultaten(idx):
        logger.debug(">>> Entering Resultaten(idx=%s)", idx)
        idxnr = idx.data()
        logger.debug("Resultaten(idx=%s): idxnr → %s", idx, idxnr)
        if  idx.column() == 0:
            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            logger.debug("Resultaten(idx=%s): engine → %s", idx, engine)
            con = engine.connect()
            selres = select([resultaten]).where(resultaten.c.resID == idxnr)
            logger.debug("Resultaten(idx=%s): con → %s", idx, con)
            rpres = con.execute(selres).first()
   
            logger.debug("Resultaten(idx=%s): selres → %s", idx, selres)
            logger.debug("Resultaten(idx=%s): rpres → %s", idx, rpres)
            class Window(QDialog):
                def __init__(self):
                    logger.debug("<<< Exiting Resultaten(idx=%s)", idx)
                    QDialog.__init__(self)
                    
                    grid = QGridLayout()
                    grid.setSpacing(20)
                    
                    self.setWindowTitle("Request results per book week")
                    self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
                    
                    self.setFont(QFont('Arial', 10))   
                                                      
                    self.lbl = QLabel()
                    self.pixmap = QPixmap('./images/logos/verbinding.jpg')
                    self.lbl.setPixmap(self.pixmap)
                    grid.addWidget(self.lbl , 0, 0)
                    
                    grid.addWidget(QLabel('Request results works external per booking week'),0, 2, 1, 3)
            
                    self.logo = QLabel()
                    self.pixmap = QPixmap('./images/logos/logo.jpg')
                    self.logo.setPixmap(self.pixmap)
                    grid.addWidget(self.logo , 0, 5, 1, 1, Qt.AlignRight)                
                    index = 3
                    for item in header:
                        horpos = index%3
                        verpos = index
                        if index%3 == 1:
                            verpos = index - 1
                        elif index%3 == 2:
                            verpos = index -2
                        self.lbl = QLabel('{:15}'.format(header[index-3]))
                        
                        self.Gegevens = QLabel()
                        if index-3 > 2:
                            q1Edit = QLineEdit('{:12.2f}'.format(rpres[index-3]))
                        else:
                            q1Edit = QLineEdit(str(rpres[index-3]))
                        q1Edit.setAlignment(Qt.AlignRight)
                        q1Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                        q1Edit.setFixedWidth(150)
                        q1Edit.setDisabled(True)
                        grid.addWidget(self.lbl, verpos, horpos+horpos%3)
                        grid.addWidget(q1Edit, verpos, horpos+horpos%3+1)
                        
                        index +=1
                        
                    terugBtn = QPushButton('Close')
                    terugBtn.clicked.connect(self.accept)
            
                    grid.addWidget(terugBtn, verpos+1, 5, 1 , 1, Qt.AlignRight)
                    terugBtn.setFont(QFont("Arial",10))
                    terugBtn.setFixedWidth(100)  
                    terugBtn.setStyleSheet("color: black;  background-color: gainsboro") 
                    
                    grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), verpos+2, 2, 1, 2)
                                                                            
                    self.setLayout(grid)
                    self.setGeometry(200, 300, 150, 150)
                            
            mainWin = Window()
            mainWin.exec_()
                        
    win = window(data_list, header)
    win.exec_()
    hoofdMenu(m_email)