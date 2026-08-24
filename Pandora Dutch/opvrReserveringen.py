from login import hoofdMenu
from validZt import zt
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QDialog, QLabel, QGridLayout, QTableView, QVBoxLayout,\
                             QPushButton, QMessageBox, QLineEdit, QComboBox
from sqlalchemy import (Table, Column, Integer, String, Float,\
                        MetaData, create_engine, ForeignKey)
from sqlalchemy.sql import select, and_
import logging
logger = logging.getLogger(__name__)

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
    msg.setText('Foutieve invoer\nzoekterm opnieuw invoeren s.v.p.!')
    msg.setWindowTitle('Reserveringen opvragen')               
    logger.debug("<<< Exiting ongInvoer()")
    msg.exec_()
    
def foutBestel():
    logger.debug(">>> Entering foutBestel()")
    msg = QMessageBox()
    logger.debug("foutBestel(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Bestelling is al eerder uitgevoerd!')
    msg.setWindowTitle('Reserveringen opvragen')               
    logger.debug("<<< Exiting foutBestel()")
    msg.exec_()
    
def foutOrder():
    logger.debug(">>> Entering foutOrder()")
    msg = QMessageBox()
    logger.debug("foutOrder(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Ongeldig inkoopordernummer!')
    msg.setWindowTitle('Reserveringen opvragen')               
    logger.debug("<<< Exiting foutOrder()")
    msg.exec_()
   
def geenRecord():
    logger.debug(">>> Entering geenRecord()")
    msg = QMessageBox()
    logger.debug("geenRecord(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Geen record gevonden\nmaak een andere selektie s.v.p.!')
    msg.setWindowTitle('Reserveringen opvragen')               
    logger.debug("<<< Exiting geenRecord()")
    msg.exec_() 
    
def updateOk():
    logger.debug(">>> Entering updateOk()")
    msg = QMessageBox()
    logger.debug("updateOk(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Information)
    msg.setText('Wijzigen zijn uitgevoerd')
    msg.setWindowTitle('Reserveringen opvragen')
    logger.debug("<<< Exiting updateOk()")
    msg.exec_()

def resKeuze(m_email):
    logger.debug(">>> Entering resKeuze(m_email=%s)", m_email)
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle("Opvragen reserveringen")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    
            self.setFont(QFont('Arial', 10))
    
            self.Keuze = QLabel()
            k0Edit = QComboBox()
            k0Edit.setFixedWidth(350)
            k0Edit.setFont(QFont("Arial",10))
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.addItem('                   Sorteersleutel zoeken')
            k0Edit.addItem('1. Alle reserveringen')
            k0Edit.addItem('2. Gesorteerd op reserveringsdatum')
            k0Edit.addItem('3. Gesorteerd op start levering')
            k0Edit.addItem('4. Gefilterd op artikelnummer')
            k0Edit.addItem('5. Gefilterd op werknummer / werkorder')
            k0Edit.addItem('6. Gefilterd op bestelde artikelen')
            k0Edit.addItem('7. Gefilterd op te bestellen artikelen')
            k0Edit.addItem('8. Gefilterd op categorienummer')
            k0Edit.activated[str].connect(self.k0Changed)
            
            self.Zoekterm = QLabel()
            zktermEdit = QLineEdit()
            zktermEdit.setFixedWidth(210)
            zktermEdit.setFont(QFont("Arial",10))
            zktermEdit.textChanged.connect(self.zktermChanged)
     
            grid = QGridLayout()
            grid.setSpacing(20)
                          
            lbl = QLabel()
            pixmap = QPixmap('./images/logos/verbinding.jpg')
            lbl.setPixmap(pixmap)
            grid.addWidget(lbl , 0, 0, 1, 2)
                                  
            grid.addWidget(k0Edit, 1, 0 ,1, 2, Qt.AlignRight)
            lbl1 = QLabel('Zoekterm')  
            lbl1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl1, 2, 0)
            grid.addWidget(zktermEdit, 2, 1)
            
            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)
            
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 4, 0, 1 , 2, Qt.AlignCenter)
            
            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo , 0, 1, 1 ,1, Qt.AlignRight)
    
            applyBtn = QPushButton('Zoeken')
            applyBtn.clicked.connect(self.accept)
    
            grid.addWidget(applyBtn, 3, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial",10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")
              
            cancelBtn = QPushButton('Sluiten')
            cancelBtn.clicked.connect(lambda: windowSluit(self,m_email))
    
            grid.addWidget(cancelBtn, 3, 1)
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
            
        def zktermChanged(self, text):
            logger.debug(">>> Entering zktermChanged(text=%s)", text)
            logger.debug("zktermChanged(self=%s,text=%s): Zoekterm → %s", self, text, Zoekterm)
            self.Zoekterm.setText(text)
            logger.debug("<<< Exiting zktermChanged(text=%s)", text)
 
        def returnk0(self):
            logger.debug(">>> Entering returnk0()")
            logger.debug("<<< Exiting returnk0()")
            return self.Keuze.text()
        
        def returnzkterm(self):
            logger.debug(">>> Entering returnzkterm()")
            logger.debug("<<< Exiting returnzkterm()")
            return self.Zoekterm.text()
        
        @staticmethod
        def getData(parent=None):
            logger.debug(">>> Entering getData(parent=%s)", parent)
            dialog = Widget(parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog)
            dialog.exec_()
            logger.debug("<<< Exiting getData(parent=%s)", parent)
            return [dialog.returnk0(), dialog.returnzkterm()] 

    window = Widget()
    data = window.getData()
    if not data[0] or data[0][0] == ' ':
        keuze = 0
    elif data[0]:
        keuze = int(data[0][0])
    else:
        keuze = 0
    if data[1]:
        zoekterm = data[1]
    else:
        zoekterm = ''
    toonReserveringen(keuze,zoekterm, m_email)

def toonReserveringen(keuze, zoekterm, m_email):
    logger.debug(">>> Entering toonReserveringen(keuze=%s,zoekterm=%s,m_email=%s)", keuze, zoekterm, m_email)
    metadata = MetaData()
    logger.debug("toonReserveringen(keuze=%s,zoekterm=%s,m_email=%s): metadata → %s", keuze, zoekterm, m_email, metadata)
    materiaallijsten = Table('materiaallijsten', metadata,
        Column('matlijstID', Integer, primary_key=True),
        Column('artikelID', None, ForeignKey('artikelen.artikelID')),
        Column('werknummerID', Integer),
        Column('calculatie', Integer),
        Column('icalculatie', Integer),
        Column('orderinkoopID', Integer),
        Column('hoeveelheid', Float),
        Column('reserverings_datum', String),
        Column('levertijd_begin', String),
        Column('levertijd_end', String),
        Column('categorie', Integer))
    artikelen = Table('artikelen', metadata,
        Column('artikelID', Integer(), primary_key=True),
        Column('artikelomschrijving', String),
        Column('artikelprijs', Float),
        Column('art_voorraad', Float),
        Column('categorie', String(10)),
        Column('bestelsaldo', Float),
        Column('reserveringsaldo', Float))
        
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("toonReserveringen(keuze=%s,zoekterm=%s,m_email=%s): engine → %s", keuze, zoekterm, m_email, engine)
    con = engine.connect()
    
    logger.debug("toonReserveringen(keuze=%s,zoekterm=%s,m_email=%s): con → %s", keuze, zoekterm, m_email, con)
    if keuze == 1:
        sel = select([materiaallijsten, artikelen]).where(materiaallijsten.c.artikelID == \
          artikelen.c.artikelID).order_by(materiaallijsten.c.artikelID)
        logger.debug("toonReserveringen(keuze=%s,zoekterm=%s,m_email=%s): sel → %s", keuze, zoekterm, m_email, sel)
    elif keuze == 2:
        sel = select([materiaallijsten, artikelen]).where(materiaallijsten.c.artikelID ==\
          artikelen.c.artikelID).order_by(materiaallijsten.c.reserverings_datum)
    elif keuze == 3:
        sel = select([materiaallijsten, artikelen]).where(materiaallijsten.c.artikelID ==\
          artikelen.c.artikelID).order_by(materiaallijsten.c.levertijd_begin)
    elif keuze == 4 and zt(zoekterm, 2):
        sel = select([materiaallijsten, artikelen]).where(and_(materiaallijsten.c.artikelID ==\
          artikelen.c.artikelID, materiaallijsten.c.artikelID ==  int(zoekterm)))
    elif keuze == 5 and zt(zoekterm, 21):
        sel = select([materiaallijsten, artikelen]).where(and_(materiaallijsten.c.artikelID ==\
          artikelen.c.artikelID, materiaallijsten.c.werknummerID == int(zoekterm)))
    elif keuze == 6:
        sel = select([materiaallijsten, artikelen]).where(and_(materiaallijsten.c.artikelID ==\
          artikelen.c.artikelID,materiaallijsten.c.orderinkoopID > 0)).order_by(materiaallijsten.c.artikelID)
    elif keuze == 7:
         sel = select([materiaallijsten, artikelen]).where(and_(materiaallijsten.c.artikelID ==\
           artikelen.c.artikelID,materiaallijsten.c.orderinkoopID == 0)).order_by(materiaallijsten.c.artikelID)
    elif keuze == 8 and str(zoekterm).isnumeric() and len(str(zoekterm)) == 1:
        sel = select([materiaallijsten,artikelen]).where(and_(materiaallijsten.c.artikelID ==\
          artikelen.c.artikelID, materiaallijsten.c.categorie == zoekterm)).order_by(artikelen.c.artikelID)
    else:
        ongInvoer()
        resKeuze(m_email)
    
    if con.execute(sel).fetchone():    
        rpres = con.execute(sel)
        logger.debug("toonReserveringen(keuze=%s,zoekterm=%s,m_email=%s): rpres → %s", keuze, zoekterm, m_email, rpres)
    else:
        geenRecord()
        resKeuze(m_email)
    
    class MyWindow(QDialog):
        logger.debug("<<< Exiting toonReserveringen(keuze=%s,zoekterm=%s,m_email=%s)", keuze, zoekterm, m_email)
        def __init__(self, data_list, header, *args):
            QDialog.__init__(self, *args,)
            self.setGeometry(100, 50, 1600, 900)
            self.setWindowTitle('Reserveringen opvragen')
            self.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
            self.setWindowFlags(self.windowFlags()| Qt.WindowSystemMenuHint |
                              Qt.WindowMinMaxButtonsHint)
            table_model = MyTableModel(self, data_list, header)
            table_view = QTableView()
            table_view.setModel(table_model)
            font = QFont("Arial", 10)
            table_view.setFont(font)
            table_view.resizeColumnsToContents()
            table_view.horizontalHeader().setSectionsMovable(True)
            table_view.setColumnHidden(11,True)
            table_view.setColumnHidden(15,True)
            table_view.setSelectionBehavior(QTableView.SelectRows)
            table_view.clicked.connect(showReservering)
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
            logger.debug(">>> Entering __init__(parent=%s)", parent)
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap)
            logger.debug("__init__(parent=%s): q1Edit → %s", parent, q1Edit)
            logger.debug("__init__(parent=%s): self.ResID → %s", parent, self.ResID)
            logger.debug("__init__(self=%s,parent=%s): q1Edit → %s", self, parent, q1Edit)
            logger.debug("__init__(parent=%s): q2Edit → %s", parent, q2Edit)
            logger.debug("__init__(parent=%s): self.Artikelnummer → %s", parent, self.Artikelnummer)
            logger.debug("__init__(self=%s,parent=%s): q2Edit → %s", self, parent, q2Edit)
            logger.debug("__init__(parent=%s): q3Edit → %s", parent, q3Edit)
            logger.debug("__init__(parent=%s): self.Artikelomschrijving → %s", parent, self.Artikelomschrijving)
            logger.debug("__init__(self=%s,parent=%s): q3Edit → %s", self, parent, q3Edit)
            logger.debug("__init__(parent=%s): q18Edit → %s", parent, q18Edit)
            logger.debug("__init__(parent=%s): self.Artikelvoorraad → %s", parent, self.Artikelvoorraad)
            logger.debug("__init__(self=%s,parent=%s): q18Edit → %s", self, parent, q18Edit)
            logger.debug("__init__(parent=%s): q4Edit → %s", parent, q4Edit)
            logger.debug("__init__(parent=%s): self.Werknummer → %s", parent, self.Werknummer)
            logger.debug("__init__(self=%s,parent=%s): q4Edit → %s", self, parent, q4Edit)
            logger.debug("__init__(parent=%s): q5Edit → %s", parent, q5Edit)
            logger.debug("__init__(parent=%s): self.Calculatie → %s", parent, self.Calculatie)
            logger.debug("__init__(self=%s,parent=%s): q5Edit → %s", self, parent, q5Edit)
            logger.debug("__init__(parent=%s): q10Edit → %s", parent, q10Edit)
            logger.debug("__init__(parent=%s): self.Icalculatie → %s", parent, self.Icalculatie)
            logger.debug("__init__(self=%s,parent=%s): q10Edit → %s", self, parent, q10Edit)
            logger.debug("__init__(parent=%s): q6Edit → %s", parent, q6Edit)
            logger.debug("__init__(parent=%s): self.Inkooporder → %s", parent, self.Inkooporder)
            logger.debug("__init__(self=%s,parent=%s): q6Edit → %s", self, parent, q6Edit)
            logger.debug("__init__(parent=%s): q17Edit → %s", parent, q17Edit)
            logger.debug("__init__(parent=%s): self.Hoeveelheid → %s", parent, self.Hoeveelheid)
            logger.debug("__init__(self=%s,parent=%s): q17Edit → %s", self, parent, q17Edit)
            logger.debug("__init__(parent=%s): q7Edit → %s", parent, q7Edit)
            logger.debug("__init__(parent=%s): self.Reserveringsaldo → %s", parent, self.Reserveringsaldo)
            logger.debug("__init__(self=%s,parent=%s): q7Edit → %s", self, parent, q7Edit)
            logger.debug("__init__(parent=%s): q8Edit → %s", parent, q8Edit)
            logger.debug("__init__(parent=%s): self.Reserveringdatum → %s", parent, self.Reserveringdatum)
            logger.debug("__init__(self=%s,parent=%s): q8Edit → %s", self, parent, q8Edit)
            logger.debug("__init__(parent=%s): q9Edit → %s", parent, q9Edit)
            logger.debug("__init__(parent=%s): self.Levering_start → %s", parent, self.Levering_start)
            logger.debug("__init__(self=%s,parent=%s): q9Edit → %s", self, parent, q9Edit)
            logger.debug("__init__(parent=%s): q11Edit → %s", parent, q11Edit)
            logger.debug("__init__(parent=%s): self.Levering_eind → %s", parent, self.Levering_eind)
            logger.debug("__init__(self=%s,parent=%s): q11Edit → %s", self, parent, q11Edit)
            logger.debug("__init__(parent=%s): q13Edit → %s", parent, q13Edit)
            logger.debug("__init__(parent=%s): self.Categorie → %s", parent, self.Categorie)
            logger.debug("__init__(self=%s,parent=%s): q13Edit → %s", self, parent, q13Edit)
            logger.debug("__init__(parent=%s): q14Edit → %s", parent, q14Edit)
            logger.debug("__init__(parent=%s): self.Artikelprijs → %s", parent, self.Artikelprijs)
            logger.debug("__init__(self=%s,parent=%s): q14Edit → %s", self, parent, q14Edit)
            logger.debug("__init__(parent=%s): q16Edit → %s", parent, q16Edit)
            logger.debug("__init__(parent=%s): self.Bestelsaldo → %s", parent, self.Bestelsaldo)
            logger.debug("__init__(self=%s,parent=%s): q16Edit → %s", self, parent, q16Edit)
            logger.debug("__init__(parent=%s): grid → %s", parent, grid)
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid)
            logger.debug("__init__(parent=%s): lbl → %s", parent, lbl)
            logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl)
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap)
            logger.debug("__init__(parent=%s): logo → %s", parent, logo)
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo)
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn)
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn)
            logger.debug("<<< Exiting __init__(parent=%s)", parent)
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
       
    header = ['MatlijstID','Artikelnummer','Werknummer','Calculatie','Icalculatie',\
              'Inkoopordernummer','Hoeveelheid','Reserveringdatum','Levertijd begin',\
              'Levertijd einde','Categorie', 'Artikelnummer','Artikelomschrijving',\
              'Artikelprijs','Artikelvoorraad','Categorie','Bestelsaldo','Reserveringsaldo']  
        
    data_list=[]
    for row in rpres:
        data_list += [(row)]
        
    def showReservering(idx):
        logger.debug(">>> Entering showReservering(idx=%s)", idx)
        mresnr = idx.data()
        logger.debug("showReservering(idx=%s): mresnr → %s", idx, mresnr)
        if idx.column() == 0:
            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            logger.debug("showReservering(idx=%s): engine → %s", idx, engine)
            con = engine.connect()
            sel = select([materiaallijsten, artikelen]).where(and_(materiaallijsten.c.artikelID ==\
                artikelen.c.artikelID, materiaallijsten.c.matlijstID == mresnr))
            logger.debug("showReservering(idx=%s): con → %s", idx, con)
            rpres = con.execute(sel).first()
            class Widget(QDialog):
                logger.debug("showReservering(idx=%s): sel → %s", idx, sel)
                def __init__(self, parent=None):
                    super(Widget, self).__init__(parent)
                    logger.debug("<<< Exiting showReservering(idx=%s)", idx)
                
                    self.setWindowTitle("Reserveringen opvragen")
                    self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
                                
                    self.setFont(QFont('Arial', 10))
                               
                    self.ResID = QLabel()
                    q1Edit = QLineEdit(str(rpres[0]))
                    q1Edit.setAlignment(Qt.AlignRight)
                    q1Edit.setFixedWidth(100)
                    q1Edit.setDisabled(True)
                    q1Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                
                    self.Artikelnummer = QLabel()
                    q2Edit = QLineEdit(str(rpres[1]))
                    q2Edit.setFixedWidth(100)
                    q2Edit.setAlignment(Qt.AlignRight)
                    q2Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q2Edit.setDisabled(True)
                    
                    self.Artikelomschrijving = QLabel()
                    q3Edit = QLineEdit(str(rpres[12]))
                    q3Edit.setFixedWidth(400)
                    q3Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q3Edit.setDisabled(True)
                    
                    self.Artikelvoorraad = QLabel()
                    q18Edit = QLineEdit('{:12.2f}'.format(rpres[14]))
                    q18Edit.setFixedWidth(100)
                    q18Edit.setAlignment(Qt.AlignRight)
                    q18Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q18Edit.setDisabled(True) 
                                    
                    self.Werknummer = QLabel()
                    q4Edit = QLineEdit(str(rpres[2]))
                    q4Edit.setFixedWidth(100)
                    q4Edit.setAlignment(Qt.AlignRight)
                    q4Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q4Edit.setDisabled(True)
                    
                    self.Calculatie = QLabel()
                    q5Edit = QLineEdit(str(rpres[3]))
                    q5Edit.setFixedWidth(100)
                    q5Edit.setAlignment(Qt.AlignRight)
                    q5Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q5Edit.setDisabled(True)
                    
                    self.Icalculatie = QLabel()
                    q10Edit = QLineEdit(str(rpres[4]))
                    q10Edit.setAlignment(Qt.AlignRight)
                    q10Edit.setFixedWidth(100)
                    q10Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q10Edit.setDisabled(True)
                                 
                    self.Inkooporder = QLabel()
                    q6Edit = QLineEdit(str(rpres[5]))
                    q6Edit.setFixedWidth(100)
                    q6Edit.setAlignment(Qt.AlignRight)
                    q6Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q6Edit.setDisabled(True)
                  
                    self.Hoeveelheid = QLabel()
                    q17Edit = QLineEdit('{:12.2f}'.format(rpres[6]))
                    q17Edit.setFixedWidth(100)
                    q17Edit.setAlignment(Qt.AlignRight)
                    q17Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q17Edit.setDisabled(True)
                                     
                    self.Reserveringsaldo = QLabel()
                    q7Edit = QLineEdit('{:12.2f}'.format(rpres[17]))
                    q7Edit.setFixedWidth(100)
                    q7Edit.setAlignment(Qt.AlignRight)
                    q7Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q7Edit.setDisabled(True)
                                   
                    self.Reserveringdatum = QLabel()
                    q8Edit = QLineEdit(str(rpres[7]))
                    q8Edit.setFixedWidth(100)
                    q8Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q8Edit.setDisabled(True)
                    
                    self.Levering_start= QLabel()
                    q9Edit = QLineEdit(str(rpres[8]))
                    q9Edit.setFixedWidth(100)
                    q9Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q9Edit.setDisabled(True)
  
                    self.Levering_eind = QLabel()
                    q11Edit = QLineEdit(str(rpres[9]))
                    q11Edit.setFixedWidth(100)
                    q11Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q11Edit.setDisabled(True)
                           
                    self.Categorie = QLabel()
                    q13Edit = QLineEdit(str(rpres[10]))
                    q13Edit.setFixedWidth(100)
                    q13Edit.setAlignment(Qt.AlignRight)
                    q13Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q13Edit.setDisabled(True)
                    
                    self.Artikelprijs = QLabel()
                    q14Edit = QLineEdit('{:12.2f}'.format(rpres[13]))
                    q14Edit.setFixedWidth(100)
                    q14Edit.setAlignment(Qt.AlignRight)
                    q14Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q14Edit.setDisabled(True)
                    
                    self.Bestelsaldo = QLabel()
                    q16Edit = QLineEdit('{:12.2f}'.format(rpres[16]))
                    q16Edit.setFixedWidth(100)
                    q16Edit.setAlignment(Qt.AlignRight)
                    q16Edit.setStyleSheet("QLineEdit { font-size: 10pt; font-family: Arial; color: black }")
                    q16Edit.setDisabled(True)
                                         
                    grid = QGridLayout()
                    grid.setSpacing(20)
                
                    lbl = QLabel()
                    pixmap = QPixmap('./images/logos/verbinding.jpg')
                    lbl.setPixmap(pixmap)
                    grid.addWidget(lbl , 0, 0)
                
                    logo = QLabel()
                    pixmap = QPixmap('./images/logos/logo.jpg')
                    logo.setPixmap(pixmap)
                    grid.addWidget(logo , 0, 3, 1, 1, Qt.AlignRight) 
                  
                    grid.addWidget(QLabel('MatlijstID'), 1, 0)
                    grid.addWidget(q1Edit, 1, 1)
                
                    grid.addWidget(QLabel('Artikelnummer'), 2, 0)
                    grid.addWidget(q2Edit, 2, 1)
                    
                    grid.addWidget(QLabel('Werknummer'), 2, 2)
                    grid.addWidget(q4Edit, 2, 3)
                    
                    grid.addWidget(QLabel('Calculatie'), 3, 0)
                    grid.addWidget(q5Edit, 3, 1)
                    
                    grid.addWidget(QLabel('Icalculatie'), 3, 2)
                    grid.addWidget(q10Edit, 3, 3)
                
                    grid.addWidget(QLabel('Artikelomschrijving'), 4, 0)
                    grid.addWidget(q3Edit, 4 ,1, 1, 3) 
                                             
                    grid.addWidget(QLabel('Inkoopordernummer'), 5, 0)
                    grid.addWidget(q6Edit, 5, 1)
                                                      
                    grid.addWidget(QLabel('Hoeveelheid'), 5, 2)
                    grid.addWidget(q17Edit, 5, 3)
                    
                    grid.addWidget(QLabel('Artikelvoorraad'), 6, 0)
                    grid.addWidget(q18Edit, 6, 1)
                
                    grid.addWidget(QLabel('Reserveringsaldo'), 6, 2)
                    grid.addWidget(q7Edit, 6, 3)
                
                    grid.addWidget(QLabel('Reserveringsdatum'), 7, 0)
                    grid.addWidget(q8Edit, 7, 1)
                    
                    grid.addWidget(QLabel('Bestelsaldo'), 7, 2)
                    grid.addWidget(q16Edit, 7, 3)
                
                    grid.addWidget(QLabel('Levering start'), 8, 0)
                    grid.addWidget(q9Edit, 8, 1) 
                                                          
                    grid.addWidget(QLabel('Levering eind'), 8, 2)
                    grid.addWidget(q11Edit, 8, 3)
                    
                    grid.addWidget(QLabel('Categorie'), 9,0)
                    grid.addWidget(q13Edit, 9, 1)
                    
                    grid.addWidget(QLabel('Artikelprijs'), 9, 2)
                    grid.addWidget(q14Edit, 9, 3)
                                     
                    grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 11, 0, 1, 4, Qt.AlignCenter)
                       
                    cancelBtn = QPushButton('Sluiten')
                    cancelBtn.clicked.connect(self.close)
                
                    grid.addWidget(cancelBtn, 10, 3, 1, 1, Qt.AlignRight)
                    cancelBtn.setFont(QFont("Arial", 10))
                    cancelBtn.setFixedWidth(100)
                    cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")
                                                  
                    self.setLayout(grid)
                    self.setGeometry(500, 100, 350, 300)
                    logger.debug("<<< Exiting __init__(parent=%s)", parent)
                    
            window = Widget()
            window.exec_()
                                
    win = MyWindow(data_list, header)
    win.exec_()
    resKeuze(m_email)    