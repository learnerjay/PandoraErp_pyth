from login import hoofdMenu
import  datetime
from PyQt5.QtWidgets import QLabel, QLineEdit, QGridLayout, QPushButton, QComboBox,\
      QDialog, QMessageBox, QWidget, QTableView
from PyQt5.QtGui import QFont, QIcon, QRegExpValidator, QPixmap
from PyQt5.QtCore import Qt,  QRegExp, QAbstractTableModel
from sqlalchemy import (Table, Column, Integer, String, Float, Boolean,\
                        MetaData, create_engine)
from sqlalchemy.sql import select, update
import logging
logger = logging.getLogger(__name__)

def refresh(keuze, m_email, self):
    logger.warning(">>> Entering refresh(keuze=%s,m_email=%s)", keuze, m_email, extra={"event.action": "refresh", "logrite.keuze": keuze})
    self.close()
    loonTabellen(keuze, m_email)
    logger.debug("<<< Exiting refresh(keuze=%s,m_email=%s)", keuze, m_email, extra={"event.action": "refresh", "logrite.keuze": keuze})

def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})

def ongInvoer():
    logger.warning(">>> Entering ongInvoer()", extra={"event.action": "ongInvoer"})
    msg = QMessageBox()
    logger.debug("ongInvoer(): msg → %s", msg, extra={"event.action": "ongInvoer"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Please re-enter incorrect input\nsearch term!')
    msg.setWindowTitle('Change pay table')
    logger.debug("<<< Exiting ongInvoer()", extra={"event.action": "ongInvoer"})
    msg.exec_()
    
def geenRecord():
    logger.warning(">>> Entering geenRecord()", extra={"event.action": "geenRecord"})
    msg = QMessageBox()
    logger.debug("geenRecord(): msg → %s", msg, extra={"event.action": "geenRecord"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('No record found\ncreate another selection please!')
    msg.setWindowTitle('Change pay table')
    logger.debug("<<< Exiting geenRecord()", extra={"event.action": "geenRecord"})
    msg.exec_() 
   
def invoerOK():
    logger.warning(">>> Entering invoerOK()", extra={"event.action": "invoerOK"})
    msg = QMessageBox()
    logger.debug("invoerOK(): msg → %s", msg, extra={"event.action": "invoerOK"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Information)
    msg.setText('Insert successful!')
    msg.setWindowTitle('Change pay table')
    logger.debug("<<< Exiting invoerOK()", extra={"event.action": "invoerOK"})
    msg.exec_()
    
def zoeken(m_email):
    logger.warning(">>> Entering zoeken(m_email=%s)", m_email, extra={"event.action": "zoeken"})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            self.setWindowTitle("Modify wages table")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
    
            self.Keuze = QLabel()
            logger.debug("__init__(parent=%s): self.Keuze → %s", parent, self.Keuze, extra={"event.action": "__init__"})
            k0Edit = QComboBox()
            logger.debug("__init__(self=%s,parent=%s): k0Edit → %s", self, parent, k0Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): k0Edit → %s", parent, k0Edit, extra={"event.action": "__init__"})
            k0Edit.setFixedWidth(210)
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.setFont(QFont("Arial",10))
            k0Edit.addItem('    Search sort key')
            k0Edit.addItem('1. Salary table internally')
            k0Edit.addItem('2. Salary table externally')
            k0Edit.addItem('3. Wages table indirect')
            k0Edit.activated[str].connect(self.k0Changed)
                 
            grid = QGridLayout()
            logger.debug("__init__(parent=%s): grid → %s", parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid, extra={"event.action": "__init__"})
            grid.setSpacing(20)
                          
            lbl = QLabel()
            logger.debug("__init__(parent=%s): lbl → %s", parent, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl, extra={"event.action": "__init__"})
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap, extra={"event.action": "__init__"})
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 0, 0, 1, 2)
                                  
            grid.addWidget(k0Edit, 1, 1)
            
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 4, 0, 1 , 2, Qt.AlignCenter)
            
            logo = QLabel()
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 1, 1 ,1, Qt.AlignRight)
    
            applyBtn = QPushButton('Search')
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn, extra={"event.action": "__init__"})
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 3, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
              
            cancelBtn = QPushButton('Close')
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn, extra={"event.action": "__init__"})
            cancelBtn.clicked.connect(lambda: windowSluit(self,m_email))
    
            grid.addWidget(cancelBtn, 3, 1)
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            cancelBtn.setFont(QFont("Arial",10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
        
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
            dialog = Widget(parent)
            dialog.exec_()
            return [dialog.returnk0()] 
        
    window = Widget()
    data = window.getData()
    if not data[0] or data[0][0] == ' ':
        keuze = 0
    elif data[0]:
        keuze = int(data[0][0])
    else:
        keuze = 0
    loonTabellen(keuze, m_email)

def loonTabellen(keuze, m_email):
    logger.warning(">>> Entering loonTabellen(keuze=%s,m_email=%s)", keuze, m_email, extra={"event.action": "loonTabellen", "logrite.keuze": keuze})
    class MyWindow(QDialog):
        def __init__(self, data_list, header, *args):
            logger.warning(">>> Entering __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})
            QWidget.__init__(self, *args,)
            self.setWindowTitle('Request wage payments')
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            self.setWindowFlags(self.windowFlags()| Qt.WindowSystemMenuHint |
                    Qt.WindowMinMaxButtonsHint)
            self.setFont(QFont('Arial', 10))
            
            grid = QGridLayout()
            logger.debug("__init__(data_list=%s,header=%s): grid → %s", data_list, header, grid, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): grid → %s", self, data_list, header, grid, extra={"event.action": "__init__", "logrite.data_list": data_list})
            grid.setSpacing(20)
            
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
            table_view.setSelectionBehavior(QTableView.SelectRows)
            table_view.resizeColumnsToContents()
            #table_view.clicked.connect(selectRow)
            table_view.clicked.connect(wijzLoonschaal)
            grid.addWidget(table_view, 0, 0, 1, 7)
             
            lbl = QLabel()
            logger.debug("__init__(data_list=%s,header=%s): lbl → %s", data_list, header, lbl, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): lbl → %s", self, data_list, header, lbl, extra={"event.action": "__init__", "logrite.data_list": data_list})
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            logger.debug("__init__(self=%s,data_list=%s,header=%s): pixmap → %s", self, data_list, header, pixmap, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(data_list=%s,header=%s): pixmap → %s", data_list, header, pixmap, extra={"event.action": "__init__", "logrite.data_list": data_list})
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl, 1, 0, 1, 2)
       
            logo = QLabel()
            logger.debug("__init__(data_list=%s,header=%s): logo → %s", data_list, header, logo, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): logo → %s", self, data_list, header, logo, extra={"event.action": "__init__", "logrite.data_list": data_list})
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 1, 6, 1, 1, Qt.AlignRight)
            
            freshBtn = QPushButton('Refresh')
            logger.debug("__init__(data_list=%s,header=%s): freshBtn → %s", data_list, header, freshBtn, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): freshBtn → %s", self, data_list, header, freshBtn, extra={"event.action": "__init__", "logrite.data_list": data_list})
            freshBtn.clicked.connect(lambda: refresh(keuze, m_email, self))

            freshBtn.setFont(QFont("Arial",10))
            freshBtn.setFixedWidth(100) 
            freshBtn.setStyleSheet("color: black;  background-color: gainsboro")
   
            grid.addWidget(freshBtn, 1, 5, 1, 1, Qt.AlignRight |Qt.AlignTop)
        
            sluitBtn = QPushButton('Close')
            logger.debug("__init__(data_list=%s,header=%s): sluitBtn → %s", data_list, header, sluitBtn, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): sluitBtn → %s", self, data_list, header, sluitBtn, extra={"event.action": "__init__", "logrite.data_list": data_list})
            sluitBtn.clicked.connect(self.close)

            sluitBtn.setFont(QFont("Arial",10))
            sluitBtn.setFixedWidth(100) 
            sluitBtn.setStyleSheet("color: black;  background-color: gainsboro") 
            
            grid.addWidget(sluitBtn, 1, 4, 1, 1, Qt.AlignTop)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 1, 0, 1, 7, Qt.AlignCenter | Qt.AlignBottom)
            
            self.setLayout(grid)
            self.setGeometry(500, 100, 950, 800)
            self.setLayout(grid)
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
            logger.debug("__init__(): self.Loontabelnummer → %s", self.Loontabelnummer, extra={"event.action": "__init__"})
            logger.debug("__init__(): q1Edit → %s", q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q1Edit → %s", self, q1Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Omschrijving → %s", self.Omschrijving, extra={"event.action": "__init__"})
            logger.debug("__init__(): q2Edit → %s", q2Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q2Edit → %s", self, q2Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Maandloon → %s", self.Maandloon, extra={"event.action": "__init__"})
            logger.debug("__init__(): q3Edit → %s", q3Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q3Edit → %s", self, q3Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): reg_ex → %s", reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): reg_ex → %s", self, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(): input_validator → %s", input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): input_validator → %s", self, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Tabelloon → %s", self.Tabelloon, extra={"event.action": "__init__"})
            logger.debug("__init__(): q4Edit → %s", q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q4Edit → %s", self, q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Werkuurloon → %s", self.Werkuurloon, extra={"event.action": "__init__"})
            logger.debug("__init__(): q5Edit → %s", q5Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q5Edit → %s", self, q5Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): self.Reisuurloon → %s", self.Reisuurloon, extra={"event.action": "__init__"})
            logger.debug("__init__(): q6Edit → %s", q6Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): q6Edit → %s", self, q6Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl1 → %s", lbl1, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl1 → %s", self, lbl1, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl2 → %s", lbl2, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl2 → %s", self, lbl2, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl3 → %s", lbl3, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl3 → %s", self, lbl3, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl5 → %s", lbl5, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl5 → %s", self, lbl5, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl6 → %s", lbl6, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl6 → %s", self, lbl6, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl7 → %s", lbl7, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl7 → %s", self, lbl7, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl8 → %s", lbl8, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl8 → %s", self, lbl8, extra={"event.action": "__init__"})
            logger.debug("__init__(): lbl9 → %s", lbl9, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): lbl9 → %s", self, lbl9, extra={"event.action": "__init__"})
            logger.debug("__init__(): wijzig → %s", wijzig, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): wijzig → %s", self, wijzig, extra={"event.action": "__init__"})
            logger.debug("__init__(): sluit → %s", sluit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s): sluit → %s", self, sluit, extra={"event.action": "__init__"})
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
              
    header = ['WageID', 'Tabular wages', 'Working hourly wage', 'Travel hourly wage', 'Direct',\
      'Monthly payment','Job description', 'Modification date']
      
    metadata = MetaData()   
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
    con = engine.connect()
    if keuze == 1:
        sellon = select([lonen]).where(lonen.c.loonID > 52).order_by(lonen.c.loonID)
    elif keuze == 2:
        sellon = select([lonen]).where(lonen.c.loonID < 37).order_by(lonen.c.loonID)
    elif keuze == 3:
        sellon = select([lonen]).where(lonen.c.loonID.between(37,52)).order_by(lonen.c.loonID)
    else:
        ongInvoer()
        zoeken(m_email)
     
    if con.execute(sellon).fetchone():
        rplon = con.execute(sellon)
    else:
        geenRecord()
        zoeken(m_email)
        
    data_list=[]
    for row in rplon:
        data_list += [(row)]

    def wijzLoonschaal(idx):
        logger.warning(">>> Entering wijzLoonschaal(idx=%s)", idx, extra={"event.action": "wijzLoonschaal", "logrite.idx": idx})
        mloonnr = idx.data()
        logger.debug("wijzLoonschaal(idx=%s): mloonnr → %s", idx, mloonnr, extra={"event.action": "wijzLoonschaal", "logrite.idx": idx})
        if  idx.column() == 0:
            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            logger.debug("wijzLoonschaal(idx=%s): engine → %s", idx, engine, extra={"event.action": "wijzLoonschaal", "logrite.idx": idx})
            con = engine.connect()
            sellon = select([lonen]).where(lonen.c.loonID == mloonnr)
            logger.debug("wijzLoonschaal(idx=%s): con → %s", idx, con, extra={"event.action": "wijzLoonschaal", "logrite.idx": idx})
            rplon = con.execute(sellon).first()
    
            logger.debug("wijzLoonschaal(idx=%s): sellon → %s", idx, sellon, extra={"event.action": "wijzLoonschaal", "logrite.idx": idx})
            logger.debug("wijzLoonschaal(idx=%s): rplon → %s", idx, rplon, extra={"event.action": "wijzLoonschaal", "logrite.idx": idx})
            class Widget(QDialog):
                def __init__(self):
                    logger.debug("<<< Exiting wijzLoonschaal(idx=%s)", idx, extra={"event.action": "wijzLoonschaal", "logrite.idx": idx})
                    QDialog.__init__(self)
                    
                    grid = QGridLayout()
                    grid.setSpacing(12)
                    
                    self.setWindowTitle("Request / change pay tables")
                    self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
                    
                    self.setFont(QFont('Arial', 10))   
                                                      
                    self.lbl = QLabel()
                    self.pixmap = QPixmap('./images/logos/verbinding.jpg')
                    self.lbl.setPixmap(self.pixmap)
                    grid.addWidget(self.lbl , 0, 0)
                    
                    self.logo = QLabel()
                    self.pixmap = QPixmap('./images/logos/logo.jpg')
                    self.logo.setPixmap(self.pixmap)
                    grid.addWidget(self.logo , 0, 1, 1, 2, Qt.AlignRight) 
                    
                    grid.addWidget(QLabel('Request / change pay tables'), 0, 1)
                        
                    self.Loontabelnummer = QLabel()
                    q1Edit = QLineEdit(str(rplon[0]))
                    q1Edit.setFixedWidth(100)
                    q1Edit.setAlignment(Qt.AlignRight)
                    q1Edit.setDisabled(True)
                    q1Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                 
                    self.Omschrijving = QLabel()
                    q2Edit = QLineEdit(rplon[6])
                    q2Edit.setFixedWidth(320)
                    q2Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q2Edit.textChanged.connect(self.q2Changed)
                    q2Edit.setDisabled(True)
                    
                    self.Maandloon = QLabel()
                    q3Edit = QLineEdit(str(round(float(rplon[5]),2)))
                    q3Edit.setFixedWidth(100)
                    q3Edit.setAlignment(Qt.AlignRight)
                    q3Edit.setFont(QFont("Arial",10))
                    q3Edit.textChanged.connect(self.q3Changed)
                    reg_ex = QRegExp("^[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q3Edit)
                    q3Edit.setValidator(input_validator)
                                               
                    self.Tabelloon = QLabel()
                    q4Edit = QLineEdit(str(round(float(rplon[1]),2)))
                    q4Edit.setFixedWidth(100) 
                    q4Edit.setAlignment(Qt.AlignRight)
                    q4Edit.setFont(QFont("Arial",10))
                    q4Edit.textChanged.connect(self.q4Changed)
                    reg_ex = QRegExp("^[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q4Edit)
                    q4Edit.setValidator(input_validator)
                                            
                    self.Werkuurloon = QLabel()
                    q5Edit = QLineEdit('{:12.2f}'.format(rplon[2]))
                    q5Edit.setAlignment(Qt.AlignRight)
                    q5Edit.setFixedWidth(100)
                    q5Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q5Edit.setDisabled(True)
                  
                    self.Reisuurloon = QLabel()
                    q6Edit = QLineEdit(str(round(float(rplon[3]),2)))
                    q6Edit.setFixedWidth(100)
                    q6Edit.setAlignment(Qt.AlignRight)
                    q6Edit.setFont(QFont("Arial",10))
                    q6Edit.textChanged.connect(self.q6Changed)
                    reg_ex = QRegExp("^[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, q6Edit)
                    q6Edit.setValidator(input_validator)
                    
                    lbl1 = QLabel('Wage table number')
                    grid.addWidget(lbl1, 1, 0)
                    grid.addWidget(q1Edit, 1, 1)
                    
                    lbl2 = QLabel('Job description')
                    grid.addWidget(lbl2, 2, 0)
                    grid.addWidget(q2Edit, 2, 1, 1, 2)
                    
                    lbl3 = QLabel('Monthly payment')
                    grid.addWidget(lbl3, 3, 0)
                    grid.addWidget(q3Edit, 3, 1)
                              
                    lbl5 = QLabel('Tabular wages')
                    grid.addWidget(lbl5, 4, 0)
                    grid.addWidget(q4Edit, 4, 1)
                    
                    lbl6 = QLabel('Working hourly wage budgeted')
                    grid.addWidget(lbl6, 5, 0)
                    grid.addWidget(q5Edit, 5, 1)
                    
                    lbl7 = QLabel('Travel hourly wage budgeted')
                    grid.addWidget(lbl7, 6, 0)
                    grid.addWidget(q6Edit, 6, 1)
                    
                    lbl8 = QLabel('Modification date')
                    lbl9 = QLabel(str(rplon[7]))
                    grid.addWidget(lbl8, 7 ,0)
                    grid.addWidget(lbl9, 7, 1)
                           
                    wijzig = QPushButton('Modify')
                    wijzig.clicked.connect(self.accept)
            
                    grid.addWidget(wijzig, 8, 1, 1 , 2, Qt.AlignRight)
                    wijzig.setFont(QFont("Arial",10))
                    wijzig.setFixedWidth(100) 
                     
                    sluit = QPushButton('Close')
                    sluit.clicked.connect(self.close)
            
                    grid.addWidget(sluit, 8, 1, 1, 2, Qt.AlignCenter)
                    sluit.setFont(QFont("Arial",10))
                    sluit.setFixedWidth(100)  
                    
                    grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 9, 0, 1, 3, Qt.AlignCenter)
                                                                            
                    self.setLayout(grid)
                    self.setGeometry(600, 250, 150, 150)
                    
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
            if data[0] == '' and data[1]== ''   and data[2] == '' and data[3] =='':
                return()
            if data[0]:
                momschr = data[0]
            else:
                momschr = rplon[6]
            if data[1]:
                mmndloon = float(data[1])
            else:
                mmndloon = rplon[5]
            if data[2]:
                mtabelloon = float(data[2])
            else:
                mtabelloon = rplon[1]
            if data[3]:
                mreisuurloon = float(data[3])
            else:
                mreisuurloon = rplon[3]
                
            mboekd = str(datetime.datetime.now())[0:10] 
            
            updlon = update(lonen).where(lonen.c.loonID==mloonnr)\
                .values(functieomschr=momschr, maandloon = mmndloon, tabelloon = mtabelloon,\
                 reisuur = mreisuurloon, boekdatum = mboekd)
            con.execute(updlon)
            invoerOK()
    
    win = MyWindow(data_list, header)
    win.exec_()
    zoeken(m_email)     