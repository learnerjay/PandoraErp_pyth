from login import hoofdMenu
import datetime
from PyQt5.QtGui import  QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtWidgets import QWidget, QTableView, QComboBox, QMessageBox,\
          QGridLayout, QDialog, QPushButton, QLabel, QLineEdit,QCheckBox
from sqlalchemy import (Table, Column, Integer, Float, String, MetaData,\
                                create_engine)
from sqlalchemy.sql import select, update
import logging
logger = logging.getLogger(__name__)

def refresh(m_email, keuze, self):
    logger.debug(">>> Entering refresh(m_email=%s,keuze=%s)", m_email, keuze)
    self.close()
    toonRetouren(m_email, keuze) 
    logger.debug("<<< Exiting refresh(m_email=%s,keuze=%s)", m_email, keuze)

def windowSluit(m_email, self):
    logger.debug(">>> Entering windowSluit(m_email=%s)", m_email)
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email)

def betalingGeboekt():
    logger.debug(">>> Entering betalingGeboekt()")
    msg = QMessageBox()
    logger.debug("betalingGeboekt(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Payment has been booked!')
    msg.setWindowTitle('Return payment')               
    logger.debug("<<< Exiting betalingGeboekt()")
    msg.exec_() 

def retKeuze(m_email):
    logger.debug(">>> Entering retKeuze(m_email=%s)", m_email)
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.debug(">>> Entering __init__(parent=%s)", parent)
            self.setWindowTitle("Requesting web returns")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
    
            self.Keuze = QLabel()
            logger.debug("__init__(parent=%s): self.Keuze → %s", parent, self.Keuze)
            k0Edit = QComboBox()
            logger.debug("__init__(self=%s,parent=%s): k0Edit → %s", self, parent, k0Edit)
            logger.debug("__init__(parent=%s): k0Edit → %s", parent, k0Edit)
            k0Edit.setFixedWidth(230)
            k0Edit.setFont(QFont("Arial",10))
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.addItem(' Search sort key')
            k0Edit.addItem('1. Sorted on e-mail address')
            k0Edit.addItem('2. Filtered not payed')
            k0Edit.addItem('3. Filtered payed')
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
            grid.addWidget(lbl , 1, 0, 1 ,2)
            
            logo = QLabel()
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo)
            logger.debug("__init__(parent=%s): logo → %s", parent, logo)
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 1, 1, 1, 2, Qt.AlignRight)
                                  
            grid.addWidget(k0Edit, 2, 1, 1, 2)
                       
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 6, 0, 1, 3)
        
            applyBtn = QPushButton('Search')
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn)
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn)
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 5, 2, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
            
            closeBtn = QPushButton('Close')
            logger.debug("__init__(self=%s,parent=%s): closeBtn → %s", self, parent, closeBtn)
            logger.debug("__init__(parent=%s): closeBtn → %s", parent, closeBtn)
            closeBtn.clicked.connect(lambda: windowSluit(m_email, self))
    
            grid.addWidget(closeBtn, 5, 1, 1, 1)
            logger.debug("<<< Exiting __init__(parent=%s)", parent)
            closeBtn.setFont(QFont("Arial",10))
            closeBtn.setFixedWidth(100)
            closeBtn.setStyleSheet("color: black;  background-color: gainsboro")
            logger.debug(">>> Entering __init__(data_list=%s,header=%s)", data_list, header)
            logger.debug("__init__(data_list=%s,header=%s): font → %s", data_list, header, font)
            logger.debug("__init__(data_list=%s,header=%s): table_view → %s", data_list, header, table_view)
            logger.debug("__init__(data_list=%s,header=%s): table_model → %s", data_list, header, table_model)
            logger.debug("__init__(data_list=%s,header=%s): grid → %s", data_list, header, grid)
            logger.debug("__init__(self=%s,data_list=%s,header=%s): grid → %s", self, data_list, header, grid)
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
        retKeuze(m_email)
    toonRetouren(m_email, keuze)
                    
def toonRetouren(m_email, keuze):
    logger.debug(">>> Entering toonRetouren(m_email=%s,keuze=%s)", m_email, keuze)
    class MyWindow(QDialog):
        def __init__(self, data_list, header, *args):
            QWidget.__init__(self, *args,)
            self.setWindowTitle('Web returns paying/ requesting')
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
            table_view.setSelectionBehavior(QTableView.SelectRows)
            #table_view.clicked.connect(selectRow)
            table_view.clicked.connect(showSelection)
            grid.addWidget(table_view, 0, 0, 1, 8)
            
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl, 1, 0, 1, 2)
       
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 1, 7, 1, 1, Qt.AlignRight)
            
            freshBtn = QPushButton('Refresh')
            freshBtn.clicked.connect(lambda: refresh(m_email, keuze, self))

            freshBtn.setFont(QFont("Arial",10))
            freshBtn.setFixedWidth(100) 
            freshBtn.setStyleSheet("color: black;  background-color: gainsboro")
   
            grid.addWidget(freshBtn, 1, 6, 1, 1, Qt.AlignRight)
            
            sluitBtn = QPushButton('Close')
            sluitBtn.clicked.connect(self.close)

            sluitBtn.setFont(QFont("Arial",10))
            sluitBtn.setFixedWidth(100) 
            sluitBtn.setStyleSheet("color: black;  background-color: gainsboro") 
            
            grid.addWidget(sluitBtn, 1, 5)
          
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 1, 1, 1, 5, Qt.AlignCenter)
            
            self.setLayout(grid)
            self.setGeometry(50, 50, 1050, 900)
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
            logger.debug("__init__(): q1Edit → %s", q1Edit)
            logger.debug("__init__(self=%s): q1Edit → %s", self, q1Edit)
            logger.debug("__init__(): cBox → %s", cBox)
            logger.debug("__init__(self=%s): cBox → %s", self, cBox)
            logger.debug("__init__(): retourBtn → %s", retourBtn)
            logger.debug("__init__(self=%s): retourBtn → %s", self, retourBtn)
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
  
    header = ['Return number','E-mail address', 'Amount','Account number', 'Article number',\
              'Number','Order','Payed', 'Booking']
    
    metadata = MetaData()              
    webretouren = Table('webretouren', metadata,
        Column('retourID', Integer(), primary_key=True),
        Column('e_mail', String),
        Column('bedrag', Float),
        Column('rekening', String),
        Column('artikelID', Integer),
        Column('aantal', Float),
        Column('ordernummer', Integer),
        Column('betaald', String),
        Column('boeking', String))
    
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    con = engine.connect()
    
    if keuze == 1:
        sel = select([webretouren]).order_by(webretouren.c.e_mail)
    elif keuze == 2:
        sel = select([webretouren]).where(webretouren.c.betaald == '')\
         .order_by(webretouren.c.e_mail.asc()) 
    elif keuze == 3:
        sel = select([webretouren]).where(webretouren.c.betaald != '').\
         order_by(webretouren.c.betaald)
    else:
        sel = select([webretouren]).order_by(webretouren.c.e_mail)
        
    rp = con.execute(sel)
     
    data_list=[]
    for row in rp:
        data_list += [(row)]
        
    def showSelection(idx):
        logger.debug(">>> Entering showSelection(idx=%s)", idx)
        mretnr = idx.data()
        logger.debug("showSelection(idx=%s): mretnr → %s", idx, mretnr)
        if idx.column() == 0:
            
            header = ['Return number','E-mail address', 'Amount','Account number', 'Article number',\
                  'Number','Order','Payed', 'Booking']
            
            metadata = MetaData()              
            logger.debug("showSelection(idx=%s): metadata → %s", idx, metadata)
            webretouren = Table('webretouren', metadata,
                Column('retourID', Integer(), primary_key=True),
                Column('e_mail', String),
                Column('bedrag', Float),
                Column('rekening', String),
                Column('artikelID', Integer),
                Column('aantal', Float),
                Column('ordernummer', Integer),
                Column('betaald', String),
                Column('boeking', String))
            
            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            logger.debug("showSelection(idx=%s): engine → %s", idx, engine)
            con = engine.connect()
            logger.debug("showSelection(idx=%s): con → %s", idx, con)
              
            sel = select([webretouren]).where(webretouren.c.retourID == mretnr)
            logger.debug("showSelection(idx=%s): sel → %s", idx, sel)
            rpret = con.execute(sel).first()
            logger.debug("showSelection(idx=%s): rpret → %s", idx, rpret)
            mbet = rpret[7]
               
            logger.debug("showSelection(idx=%s): mbet → %s", idx, mbet)
            class MainWindow(QDialog):
                logger.debug("<<< Exiting showSelection(idx=%s)", idx)
                def __init__(self):
                    QDialog.__init__(self)
                    
                    grid = QGridLayout()
                    grid.setSpacing(20)
                     
                    self.setWindowTitle("Returns Web articles")
                    self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
                    
                    self.setFont(QFont('Arial', 10))   
                                                      
                    self.lbl = QLabel()
                    self.pixmap = QPixmap('./images/logos/verbinding.jpg')
                    self.lbl.setPixmap(self.pixmap)
                    grid.addWidget(self.lbl , 0, 0)
                    
                    grid.addWidget(QLabel('Returns Web articles'),0, 1, 1, 2)
            
                    self.logo = QLabel()
                    self.pixmap = QPixmap('./images/logos/logo.jpg')
                    self.logo.setPixmap(self.pixmap)
                    grid.addWidget(self.logo , 0, 2, 1, 1, Qt.AlignRight)    
                    
                    index = 1
                    for item in header:
                        self.lbl = QLabel(header[index-1])
                        if type(rpret[index-1]) == float:
                            q1Edit = QLineEdit('{:12.2f}'.format(rpret[index-1]))
                            q1Edit.setAlignment(Qt.AlignRight)
                        elif type(rpret[index-1]) == int:
                            q1Edit = QLineEdit(str(rpret[index-1]))
                            q1Edit.setAlignment(Qt.AlignRight)
                        else:
                            q1Edit = QLineEdit(str(rpret[index-1]))
                        q1Edit.setFixedWidth(200)
                        q1Edit.setDisabled(True)
                        q1Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                        grid.addWidget(self.lbl, index, 0)
                        grid.addWidget(q1Edit, index, 1)
                        index +=1
                        
                    cBox = QCheckBox('Paying')
                    if mbet:
                        cBox.setDisabled(True)
                    cBox.stateChanged.connect(self.cBoxChanged)
                    grid.addWidget(cBox, index -1, 2)
                         
                    retourBtn = QPushButton('OK')
                    retourBtn.clicked.connect(self.accept)
                    
                    grid.addWidget(retourBtn, index+1, 2)
                    retourBtn.setFont(QFont("Arial",10))
                    retourBtn.setFixedWidth(100)  
                    retourBtn.setStyleSheet("color: black;  background-color: gainsboro")
                   
                    grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), index+2, 0, 1, 3, Qt.AlignCenter)
                    
                    self.setLayout(grid)
                    self.setGeometry(100, 150, 150, 150)
       
                state = False
                def cBoxChanged(self, state):
                    logger.debug(">>> Entering cBoxChanged(state=%s)", state)
                    logger.debug("cBoxChanged(state=%s): self.state → %s", state, self.state)
                    logger.debug("cBoxChanged(self=%s,state=%s): self.state → %s", self, state, self.state)
                    if state == Qt.Checked:
                        self.state = True                    
                        logger.debug("<<< Exiting cBoxChanged(state=%s)", state)
                    
                def returncBox(self):
                      logger.debug(">>> Entering returncBox()")
                      logger.debug("<<< Exiting returncBox()")
                      return self.state
                       
                @staticmethod
                def getData(parent=None):
                    logger.debug(">>> Entering getData(parent=%s)", parent)
                    dialog = MainWindow()
                    dialog.exec_()
                    return [dialog.returncBox()] 
                
            mainWin = MainWindow()
            data = mainWin.getData()
                 
            if data[0] and not mbet:
                upd = update(webretouren).where(webretouren.c.retourID == mretnr).\
                 values(betaald = str(datetime.datetime.now())[0:10])
                con.execute(upd) 
                betalingGeboekt()
           
    win = MyWindow(data_list, header)
    win.exec_()
    retKeuze(m_email)