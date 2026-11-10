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
    logger.warning(">>> Entering toonResult(m_email=%s)", m_email, extra={"event.action": "toonResult"})
    metadata = MetaData()
    logger.debug("toonResult(m_email=%s): metadata → %s", m_email, metadata, extra={"event.action": "toonResult"})
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
    
    logger.debug("toonResult(m_email=%s): resultaten → %s", m_email, resultaten, extra={"event.action": "toonResult"})
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("toonResult(m_email=%s): engine → %s", m_email, engine, extra={"event.action": "toonResult"})
    con = engine.connect()
    selres = select([resultaten]).order_by(resultaten.c.boekweek, resultaten.c.statusweek)
    logger.debug("toonResult(m_email=%s): con → %s", m_email, con, extra={"event.action": "toonResult"})
    rpres = con.execute(selres)
    
    logger.debug("toonResult(m_email=%s): selres → %s", m_email, selres, extra={"event.action": "toonResult"})
    class window(QDialog):
        logger.debug("<<< Exiting toonResult(m_email=%s)", m_email, extra={"event.action": "toonResult"})
        def __init__(self, data_list, header, *args):
            logger.warning(">>> Entering __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})
            QWidget.__init__(self, *args,)
            self.setGeometry(100, 50, 1700, 900)
            self.setWindowTitle('Request results per book week')
            self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
            self.setWindowFlags(self.windowFlags()| Qt.WindowSystemMenuHint |
                              Qt.WindowMinMaxButtonsHint)
            table_model = MyTableModel(self, data_list, header)
            logger.debug("__init__(data_list=%s,header=%s): table_model → %s", data_list, header, table_model, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): table_model → %s", self, data_list, header, table_model, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(data_list=%s,header=%s): font → %s", data_list, header, font, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): font → %s", self, data_list, header, font, extra={"event.action": "__init__", "logrite.data_list": data_list})
            table_view = QTableView()
            logger.debug("__init__(self=%s,data_list=%s,header=%s): table_view → %s", self, data_list, header, table_view, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(data_list=%s,header=%s): table_view → %s", data_list, header, table_view, extra={"event.action": "__init__", "logrite.data_list": data_list})
            table_view.setModel(table_model)
            font = QFont("Arial", 10)
            table_view.setFont(font)
            table_view.resizeColumnsToContents()
            table_view.setSelectionBehavior(QTableView.SelectRows)
            table_view.clicked.connect(Resultaten)
            layout = QVBoxLayout(self)
            logger.debug("__init__(data_list=%s,header=%s): layout → %s", data_list, header, layout, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): layout → %s", self, data_list, header, layout, extra={"event.action": "__init__", "logrite.data_list": data_list})
            layout.addWidget(table_view)
            self.setLayout(layout)
            logger.debug("<<< Exiting __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})
    
    class MyTableModel(QAbstractTableModel):
        def __init__(self, parent, mylist, header, *args):
            logger.warning(">>> Entering __init__(parent=%s,mylist=%s,header=%s)", parent, mylist, header, extra={"event.action": "__init__", "logrite.mylist": mylist})
            logger.debug("__init__(self=%s,parent=%s,mylist=%s,header=%s): self.mylist → %s", self, parent, mylist, header, self.mylist, extra={"event.action": "__init__", "logrite.mylist": mylist})
            logger.debug("__init__(self=%s,parent=%s,mylist=%s,header=%s): self.header → %s", self, parent, mylist, header, self.header, extra={"event.action": "__init__", "logrite.mylist": mylist})
            QAbstractTableModel.__init__(self, parent, *args)
            logger.debug("<<< Exiting __init__(parent=%s,mylist=%s,header=%s)", parent, mylist, header, extra={"event.action": "__init__", "logrite.mylist": mylist})
            self.mylist = mylist
            logger.warning(">>> Entering __init__()", extra={"event.action": "__init__"})
            logger.debug("__init__(): grid → %s", grid, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): grid → %s", self, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.lbl → %s", self.lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.pixmap → %s", self.pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl → %s", self, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.logo → %s", self.logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): logo → %s", self, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): index → %s", self, index, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): horpos → %s", self, horpos, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): verpos → %s", self, verpos, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Gegevens → %s", self.Gegevens, extra={"event.action": "__init__"})
            logger.debug("__init__(): q1Edit → %s", q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q1Edit → %s", self, q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): terugBtn → %s", terugBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): terugBtn → %s", self, terugBtn, extra={"event.action": "__init__"})
            logger.debug("<<< Exiting __init__()", extra={"event.action": "__init__"})
            self.header = header
        def rowCount(self, parent):
            logger.warning(">>> Entering rowCount(parent=%s)", parent, extra={"event.action": "rowCount"})
            return len(self.mylist)
        def columnCount(self, parent):
            logger.warning(">>> Entering columnCount(parent=%s)", parent, extra={"event.action": "columnCount"})
            return len(self.mylist[0])
        def data(self, index, role):
            logger.warning(">>> Entering data(index=%s,role=%s)", index, role, extra={"event.action": "data", "logrite.index": index, "logrite.role": role})
            veld = self.mylist[index.row()][index.column()]
            logger.debug("data(index=%s,role=%s): veld → %s", index, role, veld, extra={"event.action": "data", "logrite.index": index, "logrite.role": role})
            logger.debug("data(self=%s,index=%s,role=%s): veld → %s", self, index, role, veld, extra={"event.action": "data", "logrite.index": index, "logrite.role": role})
            if not index.isValid():
                return None
            elif role == Qt.TextAlignmentRole and (type(veld) == float or type(veld) == int):
                return Qt.AlignRight | Qt.AlignVCenter
            elif role != Qt.DisplayRole:
                return None
            if type(veld) == float:
                return '{:12.2f}'.format(veld)
            else:
                logger.debug("<<< Exiting data(index=%s,role=%s)", index, role, extra={"event.action": "data", "logrite.index": index, "logrite.role": role})
                return veld
        def headerData(self, col, orientation, role):
            logger.warning(">>> Entering headerData(col=%s,orientation=%s,role=%s)", col, orientation, role, extra={"event.action": "headerData", "logrite.col": col, "logrite.orientation": orientation, "logrite.role": role})
            if orientation == Qt.Horizontal and role == Qt.DisplayRole:
                return self.header[col]
            logger.debug("<<< Exiting headerData(col=%s,orientation=%s,role=%s)", col, orientation, role, extra={"event.action": "headerData", "logrite.col": col, "logrite.orientation": orientation, "logrite.role": role})
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
        logger.warning(">>> Entering Resultaten(idx=%s)", idx, extra={"event.action": "Resultaten", "logrite.idx": idx})
        idxnr = idx.data()
        logger.debug("Resultaten(idx=%s): idxnr → %s", idx, idxnr, extra={"event.action": "Resultaten", "logrite.idx": idx})
        if  idx.column() == 0:
            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            logger.debug("Resultaten(idx=%s): engine → %s", idx, engine, extra={"event.action": "Resultaten", "logrite.idx": idx})
            con = engine.connect()
            selres = select([resultaten]).where(resultaten.c.resID == idxnr)
            logger.debug("Resultaten(idx=%s): con → %s", idx, con, extra={"event.action": "Resultaten", "logrite.idx": idx})
            rpres = con.execute(selres).first()
   
            logger.debug("Resultaten(idx=%s): selres → %s", idx, selres, extra={"event.action": "Resultaten", "logrite.idx": idx})
            logger.debug("Resultaten(idx=%s): rpres → %s", idx, rpres, extra={"event.action": "Resultaten", "logrite.idx": idx})
            class Window(QDialog):
                def __init__(self):
                    logger.debug("<<< Exiting Resultaten(idx=%s)", idx, extra={"event.action": "Resultaten", "logrite.idx": idx})
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