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
    logger.debug(">>> Entering refresh(keuze=%s,m_email=%s)", keuze, m_email)
    self.close()
    loonTabellen(keuze, m_email)
    logger.debug("<<< Exiting refresh(keuze=%s,m_email=%s)", keuze, m_email)

def windowSluit(self, m_email):
    logger.debug(">>> Entering windowSluit(m_email=%s)", m_email)
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email)

def ongInvoer():
    logger.debug(">>> Entering ongInvoer()")
    msg = QMessageBox()
    logger.debug("ongInvoer(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Please re-enter incorrect input\nsearch term!')
    msg.setWindowTitle('Change pay table')
    logger.debug("<<< Exiting ongInvoer()")
    msg.exec_()
    
def geenRecord():
    logger.debug(">>> Entering geenRecord()")
    msg = QMessageBox()
    logger.debug("geenRecord(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('No record found\ncreate another selection please!')
    msg.setWindowTitle('Change pay table')
    logger.debug("<<< Exiting geenRecord()")
    msg.exec_() 
   
def invoerOK():
    logger.debug(">>> Entering invoerOK()")
    msg = QMessageBox()
    logger.debug("invoerOK(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setIcon(QMessageBox.Information)
    msg.setText('Insert successful!')
    msg.setWindowTitle('Change pay table')
    logger.debug("<<< Exiting invoerOK()")
    msg.exec_()
    
def zoeken(m_email):
    logger.debug(">>> Entering zoeken(m_email=%s)", m_email)
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.debug(">>> Entering __init__(parent=%s)", parent)
            self.setWindowTitle("Modify wages table")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
    
            self.Keuze = QLabel()
            logger.debug("__init__(parent=%s): self.Keuze → %s", parent, self.Keuze)
            k0Edit = QComboBox()
            logger.debug("__init__(self=%s,parent=%s): k0Edit → %s", self, parent, k0Edit)
            logger.debug("__init__(parent=%s): k0Edit → %s", parent, k0Edit)
            k0Edit.setFixedWidth(210)
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.setFont(QFont("Arial",10))
            k0Edit.addItem('    Search sort key')
            k0Edit.addItem('1. Salary table internally')
            k0Edit.addItem('2. Salary table externally')
            k0Edit.addItem('3. Wages table indirect')
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
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 4, 0, 1 , 2, Qt.AlignCenter)
            
            logo = QLabel()
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo)
            logger.debug("__init__(parent=%s): logo → %s", parent, logo)
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 1, 1 ,1, Qt.AlignRight)
    
            applyBtn = QPushButton('Search')
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn)
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn)
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 3, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
              
            cancelBtn = QPushButton('Close')
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn)
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn)
            cancelBtn.clicked.connect(lambda: windowSluit(self,m_email))
    
            grid.addWidget(cancelBtn, 3, 1)
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
    if not data[0] or data[0][0] == ' ':
        keuze = 0
    elif data[0]:
        keuze = int(data[0][0])
    else:
        keuze = 0
    loonTabellen(keuze, m_email)

def loonTabellen(keuze, m_email):
    logger.debug(">>> Entering loonTabellen(keuze=%s,m_email=%s)", keuze, m_email)
    class MyWindow(QDialog):
        def __init__(self, data_list, header, *args):
            QWidget.__init__(self, *args,)
            self.setWindowTitle('Request wage payments')
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
            table_view.setSelectionBehavior(QTableView.SelectRows)
            table_view.resizeColumnsToContents()
            #table_view.clicked.connect(selectRow)
            table_view.clicked.connect(wijzLoonschaal)
            grid.addWidget(table_view, 0, 0, 1, 7)
             
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl, 1, 0, 1, 2)
       
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 1, 6, 1, 1, Qt.AlignRight)
            
            freshBtn = QPushButton('Refresh')
            freshBtn.clicked.connect(lambda: refresh(keuze, m_email, self))

            freshBtn.setFont(QFont("Arial",10))
            freshBtn.setFixedWidth(100) 
            freshBtn.setStyleSheet("color: black;  background-color: gainsboro")
   
            grid.addWidget(freshBtn, 1, 5, 1, 1, Qt.AlignRight |Qt.AlignTop)
        
            sluitBtn = QPushButton('Close')
            sluitBtn.clicked.connect(self.close)

            sluitBtn.setFont(QFont("Arial",10))
            sluitBtn.setFixedWidth(100) 
            sluitBtn.setStyleSheet("color: black;  background-color: gainsboro") 
            
            grid.addWidget(sluitBtn, 1, 4, 1, 1, Qt.AlignTop)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 1, 0, 1, 7, Qt.AlignCenter | Qt.AlignBottom)
            
            self.setLayout(grid)
            self.setGeometry(500, 100, 950, 800)
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
            logger.debug("__init__(): grid → %s", grid)
            logger.debug("__init__(self=%s): grid → %s", self, grid)
            logger.debug("__init__(): self.lbl → %s", self.lbl)
            logger.debug("__init__(): self.pixmap → %s", self.pixmap)
            logger.debug("__init__(self=%s): lbl → %s", self, lbl)
            logger.debug("__init__(): self.logo → %s", self.logo)
            logger.debug("__init__(self=%s): logo → %s", self, logo)
            logger.debug("__init__(): input_validator → %s", input_validator)
            logger.debug("__init__(): q1Edit → %s", q1Edit)
            logger.debug("__init__(): self.Loontabelnummer → %s", self.Loontabelnummer)
            logger.debug("__init__(self=%s): q1Edit → %s", self, q1Edit)
            logger.debug("__init__(): q2Edit → %s", q2Edit)
            logger.debug("__init__(): self.Omschrijving → %s", self.Omschrijving)
            logger.debug("__init__(self=%s): q2Edit → %s", self, q2Edit)
            logger.debug("__init__(): q3Edit → %s", q3Edit)
            logger.debug("__init__(): self.Maandloon → %s", self.Maandloon)
            logger.debug("__init__(self=%s): q3Edit → %s", self, q3Edit)
            logger.debug("__init__(): reg_ex → %s", reg_ex)
            logger.debug("__init__(self=%s): reg_ex → %s", self, reg_ex)
            logger.debug("__init__(self=%s): input_validator → %s", self, input_validator)
            logger.debug("__init__(): q4Edit → %s", q4Edit)
            logger.debug("__init__(): self.Tabelloon → %s", self.Tabelloon)
            logger.debug("__init__(self=%s): q4Edit → %s", self, q4Edit)
            logger.debug("__init__(): q5Edit → %s", q5Edit)
            logger.debug("__init__(): self.Werkuurloon → %s", self.Werkuurloon)
            logger.debug("__init__(self=%s): q5Edit → %s", self, q5Edit)
            logger.debug("__init__(): q6Edit → %s", q6Edit)
            logger.debug("__init__(): self.Reisuurloon → %s", self.Reisuurloon)
            logger.debug("__init__(self=%s): q6Edit → %s", self, q6Edit)
            logger.debug("__init__(): lbl1 → %s", lbl1)
            logger.debug("__init__(self=%s): lbl1 → %s", self, lbl1)
            logger.debug("__init__(): lbl2 → %s", lbl2)
            logger.debug("__init__(self=%s): lbl2 → %s", self, lbl2)
            logger.debug("__init__(): lbl3 → %s", lbl3)
            logger.debug("__init__(self=%s): lbl3 → %s", self, lbl3)
            logger.debug("__init__(): lbl5 → %s", lbl5)
            logger.debug("__init__(self=%s): lbl5 → %s", self, lbl5)
            logger.debug("__init__(): lbl6 → %s", lbl6)
            logger.debug("__init__(self=%s): lbl6 → %s", self, lbl6)
            logger.debug("__init__(): lbl7 → %s", lbl7)
            logger.debug("__init__(self=%s): lbl7 → %s", self, lbl7)
            logger.debug("__init__(): lbl9 → %s", lbl9)
            logger.debug("__init__(): lbl8 → %s", lbl8)
            logger.debug("__init__(self=%s): lbl8 → %s", self, lbl8)
            logger.debug("__init__(self=%s): lbl9 → %s", self, lbl9)
            logger.debug("__init__(): wijzig → %s", wijzig)
            logger.debug("__init__(self=%s): wijzig → %s", self, wijzig)
            logger.debug("__init__(): sluit → %s", sluit)
            logger.debug("__init__(self=%s): sluit → %s", self, sluit)
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
        logger.debug(">>> Entering wijzLoonschaal(idx=%s)", idx)
        mloonnr = idx.data()
        logger.debug("wijzLoonschaal(idx=%s): mloonnr → %s", idx, mloonnr)
        if  idx.column() == 0:
            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            logger.debug("wijzLoonschaal(idx=%s): engine → %s", idx, engine)
            con = engine.connect()
            sellon = select([lonen]).where(lonen.c.loonID == mloonnr)
            logger.debug("wijzLoonschaal(idx=%s): con → %s", idx, con)
            rplon = con.execute(sellon).first()
    
            logger.debug("wijzLoonschaal(idx=%s): sellon → %s", idx, sellon)
            logger.debug("wijzLoonschaal(idx=%s): rplon → %s", idx, rplon)
            class Widget(QDialog):
                def __init__(self):
                    logger.debug("<<< Exiting wijzLoonschaal(idx=%s)", idx)
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
                    logger.debug(">>> Entering q2Changed(text=%s)", text)
                    logger.debug("q2Changed(self=%s,text=%s): Omschrijving → %s", self, text, Omschrijving)
                    self.Omschrijving.setText(text)
                    logger.debug("<<< Exiting q2Changed(text=%s)", text)
            
                def q3Changed(self,text):
                    logger.debug(">>> Entering q3Changed(text=%s)", text)
                    logger.debug("q3Changed(self=%s,text=%s): Maandloon → %s", self, text, Maandloon)
                    self.Maandloon.setText(text)
                    logger.debug("<<< Exiting q3Changed(text=%s)", text)
            
                def q4Changed(self,text):
                    logger.debug(">>> Entering q4Changed(text=%s)", text)
                    logger.debug("q4Changed(self=%s,text=%s): Tabelloon → %s", self, text, Tabelloon)
                    self.Tabelloon.setText(text)
                    logger.debug("<<< Exiting q4Changed(text=%s)", text)
                                    
                def q6Changed(self,text):
                    logger.debug(">>> Entering q6Changed(text=%s)", text)
                    logger.debug("q6Changed(self=%s,text=%s): Reisuurloon → %s", self, text, Reisuurloon)
                    self.Reisuurloon.setText(text)
                    logger.debug("<<< Exiting q6Changed(text=%s)", text)
                          
                def returnq2(self):
                    logger.debug(">>> Entering returnq2()")
                    logger.debug("<<< Exiting returnq2()")
                    return self.Omschrijving.text()
                
                def returnq3(self):
                    logger.debug(">>> Entering returnq3()")
                    logger.debug("<<< Exiting returnq3()")
                    return self.Maandloon.text()
                
                def returnq4(self):
                    logger.debug(">>> Entering returnq4()")
                    logger.debug("<<< Exiting returnq4()")
                    return self.Tabelloon.text()
                
                def returnq6(self):
                    logger.debug(">>> Entering returnq6()")
                    logger.debug("<<< Exiting returnq6()")
                    return self.Reisuurloon.text()
                        
                @staticmethod
                def getData(parent=None):
                    logger.debug(">>> Entering getData(parent=%s)", parent)
                    dialog = Widget()
                    dialog.exec_()
                    logger.debug("<<< Exiting getData(parent=%s)", parent)
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