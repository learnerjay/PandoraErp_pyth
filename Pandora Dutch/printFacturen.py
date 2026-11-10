from login import hoofdMenu
from postcode import checkpostcode
import os, datetime
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import  QDialog, QWidget, QMessageBox, QTableView, QVBoxLayout
from sqlalchemy import (Table, Column, Integer, String, MetaData, create_engine,\
                        Float, ForeignKey, select, and_)
import logging
logger = logging.getLogger(__name__)

def geenBest(m_email):
    logger.warning(">>> Entering geenBest(m_email=%s)", m_email, extra={"event.action": "geenBest"})
    msg = QMessageBox()
    logger.debug("geenBest(m_email=%s): msg → %s", m_email, msg, extra={"event.action": "geenBest"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Information)
    msg.setText('Nog geen facturen aanwezig voor deze klant!')
    msg.setWindowTitle('Facturen printen')
    msg.exec_()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting geenBest(m_email=%s)", m_email, extra={"event.action": "geenBest"})

def printing():
    logger.warning(">>> Entering printing()", extra={"event.action": "printing"})
    msg = QMessageBox()
    logger.debug("printing(): msg → %s", msg, extra={"event.action": "printing"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msg.setIcon(QMessageBox.Information)
    msg.setText('Ogenblik afdrukken wordt gestart!')
    msg.setWindowTitle('Webverkooporders printen')
    logger.debug("<<< Exiting printing()", extra={"event.action": "printing"})
    msg.exec_()
    
def printGeg(filename, movbestnr):
    logger.warning(">>> Entering printGeg(filename=%s,movbestnr=%s)", filename, movbestnr, extra={"event.action": "printGeg", "logrite.filename": filename, "logrite.movbestnr": movbestnr})
    from sys import platform
    msgBox=QMessageBox()
    logger.debug("printGeg(filename=%s,movbestnr=%s): msgBox → %s", filename, movbestnr, msgBox, extra={"event.action": "printGeg", "logrite.filename": filename, "logrite.movbestnr": movbestnr})
    msgBox.setStyleSheet("color: black;  background-color: gainsboro")
    msgBox.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msgBox.setWindowTitle("Printen orderfactuur")
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Wilt U factuur van ordernummer "+str(movbestnr)+" uitprinten?");
    msgBox.setStandardButtons(QMessageBox.Yes)
    msgBox.addButton(QMessageBox.No)
    msgBox.setStyleSheet("color: black;  background-color: gainsboro")
    msgBox.setDefaultButton(QMessageBox.Yes)
    if(msgBox.exec_() == QMessageBox.Yes):
        if platform == 'win32':
            os.startfile(filename, "print")
        else:
            os.system("lpr "+filename)
        printing()
        logger.debug("<<< Exiting printGeg(filename=%s,movbestnr=%s)", filename, movbestnr, extra={"event.action": "printGeg", "logrite.filename": filename, "logrite.movbestnr": movbestnr})
    
def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    
def kiesOrder(m_email):
    logger.warning(">>> Entering kiesOrder(m_email=%s)", m_email, extra={"event.action": "kiesOrder"})
    metadata = MetaData()
    logger.debug("kiesOrder(m_email=%s): metadata → %s", m_email, metadata, extra={"event.action": "kiesOrder"})
    orders_verkoop = Table('orders_verkoop', metadata,
        Column('ovbestelID', Integer, primary_key=True),
        Column('klantID', None, ForeignKey('klanten.klantID')),
        Column('ovbesteldatum', String),
        Column('datum_betaald', String),
        Column('datum_geleverd', String),
        Column('bedrag', Float))
    klanten = Table('klanten', metadata,
        Column('klantID', Integer(), primary_key=True),
        Column('accountID', None, ForeignKey('accounts.accountID')),
        Column('rekening', String))
    accounts = Table('accounts', metadata,
        Column('accountID', Integer(), primary_key=True),
        Column('aanhef', String),
        Column('voornaam', String), 
        Column('tussenvoegsel', String),
        Column('achternaam', String),
        Column('postcode', String),       
        Column('huisnummer', String),
        Column('toevoeging', String),
        Column('email', String),
        Column('telnr', String)) 
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("kiesOrder(m_email=%s): engine → %s", m_email, engine, extra={"event.action": "kiesOrder"})
    con = engine.connect()
    logger.debug("kiesOrder(m_email=%s): con → %s", m_email, con, extra={"event.action": "kiesOrder"})
    selord = select([orders_verkoop, klanten, accounts]).where(and_(orders_verkoop.c.klantID == klanten.c.klantID,\
                klanten.c.accountID == accounts.c.accountID, accounts.c.email == m_email))
    logger.debug("kiesOrder(m_email=%s): selord → %s", m_email, selord, extra={"event.action": "kiesOrder"})
    rpc = con.execute(selord).fetchone()
    logger.debug("kiesOrder(m_email=%s): rpc → %s", m_email, rpc, extra={"event.action": "kiesOrder"})
    if rpc:
        rpord = con.execute(selord)
    else:
        logger.debug("kiesOrder(m_email=%s): rpord → %s", m_email, rpord, extra={"event.action": "kiesOrder"})
        geenBest(m_email)
    
    mpostcode = rpc[14]
    logger.debug("kiesOrder(m_email=%s): mpostcode → %s", m_email, mpostcode, extra={"event.action": "kiesOrder"})
    mhuisnr = int(rpc[15])
    logger.debug("kiesOrder(m_email=%s): mhuisnr → %s", m_email, mhuisnr, extra={"event.action": "kiesOrder"})
    madres = checkpostcode(mpostcode,mhuisnr)
    logger.debug("kiesOrder(m_email=%s): madres → %s", m_email, madres, extra={"event.action": "kiesOrder"})
    mstraat = madres[0]
    logger.debug("kiesOrder(m_email=%s): mstraat → %s", m_email, mstraat, extra={"event.action": "kiesOrder"})
    mplaats = madres[1]
    logger.debug("kiesOrder(m_email=%s): mplaats → %s", m_email, mplaats, extra={"event.action": "kiesOrder"})
    
    class MyWindow(QDialog):
        logger.debug("<<< Exiting kiesOrder(m_email=%s)", m_email, extra={"event.action": "kiesOrder"})
        def __init__(self, data_list, header, *args):
            logger.warning(">>> Entering __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})
            QWidget.__init__(self, *args,)
            self.setGeometry(50, 50, 900, 900)
            self.setWindowTitle('Printen orderfacturen')
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
            table_view.setColumnHidden(1,True)
            table_view.setColumnHidden(6,True)
            table_view.setColumnHidden(9,True)
            table_view.setColumnHidden(10,True)
            table_view.setColumnHidden(11,True)
            table_view.setColumnHidden(12,True)
            table_view.setColumnHidden(13,True)
            table_view.setColumnHidden(14,True)
            table_view.setColumnHidden(15,True)
            table_view.setColumnHidden(16,True)
            table_view.setColumnHidden(17,True)
            table_view.setColumnHidden(18,True)
            table_view.resizeColumnsToContents()
            table_view.setSelectionBehavior(QTableView.SelectRows)
            table_view.clicked.connect(printFactuur)
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
            self.header = header
        def rowCount(self, parent):
            logger.warning(">>> Entering rowCount(parent=%s)", parent, extra={"event.action": "rowCount"})
            return len(self.mylist)
        def columnCount(self, parent):
            logger.warning(">>> Entering columnCount(parent=%s)", parent, extra={"event.action": "columnCount"})
            return len(self.mylist[0])
        def data(self, index, role):
            logger.warning(">>> Entering data(index=%s,role=%s)", index, role, extra={"event.action": "data", "logrite.index": index, "logrite.role": role})
            if not index.isValid():
                return None
            elif role != Qt.DisplayRole:
               return None
            veld = self.mylist[index.row()][index.column()]
            logger.debug("data(self=%s,index=%s,role=%s): veld → %s", self, index, role, veld, extra={"event.action": "data", "logrite.index": index, "logrite.role": role})
            if type(veld) == float:
                return '{:>12.2f}'.format(round(veld,2))
            elif type(veld) == int:
                return '{:>9d}'.format(veld)
            else:
                logger.debug("<<< Exiting data(index=%s,role=%s)", index, role, extra={"event.action": "data", "logrite.index": index, "logrite.role": role})
                return str(veld)
        def headerData(self, col, orientation, role):
            logger.warning(">>> Entering headerData(col=%s,orientation=%s,role=%s)", col, orientation, role, extra={"event.action": "headerData", "logrite.col": col, "logrite.orientation": orientation, "logrite.role": role})
            if orientation == Qt.Horizontal and role == Qt.DisplayRole:
                return self.header[col]
            logger.debug("<<< Exiting headerData(col=%s,orientation=%s,role=%s)", col, orientation, role, extra={"event.action": "headerData", "logrite.col": col, "logrite.orientation": orientation, "logrite.role": role})
            return None
      
    header = ['Bestelnummer','','Besteldatum','Betaaldatum', 'Leverdatum','Totaalbedrag','', 'Accountnr',\
              'Rekeningnr','','','','','','','','','','']
    
    data_list=[]
    for row in rpord:
        data_list += [(row)]
        
    def Heading(movbestnr, mblad):
        logger.warning(">>> Entering Heading(movbestnr=%s,mblad=%s)", movbestnr, mblad, extra={"event.action": "Heading", "logrite.movbestnr": movbestnr, "logrite.mblad": mblad})
        kop=\
            ('Ordernummer: '+ str(movbestnr)+'          Datum: '+str(datetime.datetime.now())[0:10]+'      Besteldatum: '+str(rpc[2])+' Blad : '+str(mblad)+'\n'+
            '==============================================================================================\n'+
            'Artikelnr  Omschrijving                        Eenheid Aantal     Prijs   Subtotaal       BTW \n'+
            '==============================================================================================\n')
        logger.debug("<<< Exiting Heading(movbestnr=%s,mblad=%s)", movbestnr, mblad, extra={"event.action": "Heading", "logrite.movbestnr": movbestnr, "logrite.mblad": mblad})
        return(kop)
        
    def printFactuur(idx):
        logger.warning(">>> Entering printFactuur(idx=%s)", idx, extra={"event.action": "printFactuur", "logrite.idx": idx})
        from sys import platform
        movbestnr = idx.data()
        logger.debug("printFactuur(idx=%s): movbestnr → %s", idx, movbestnr, extra={"event.action": "printFactuur", "logrite.idx": idx})
        if idx.column() == 0:
            metadata = MetaData()
            logger.debug("printFactuur(idx=%s): metadata → %s", idx, metadata, extra={"event.action": "printFactuur", "logrite.idx": idx})
            orders_verkoop_artikelen = Table('orders_verkoop_artikelen', metadata,
                Column('ovaID', Integer, primary_key=True),
                Column('ovbestelID', None, ForeignKey('orders_verkoop.ovbestelID')),
                Column('artikelID', None, ForeignKey('artikelen.artikelID')),
                Column('ovaantal', Integer),
                Column('ovleverdatum', String),
                Column('verkoopprijs', Float),
                Column('regel', Integer),
                Column('retour', Float),
                Column('betaaldatum', String),
                Column('leveringsdatum', String))
            logger.debug("printFactuur(idx=%s): selova → %s", idx, selova, extra={"event.action": "printFactuur", "logrite.idx": idx})
            artikelen = Table('artikelen', metadata,
                Column('artikelID', Integer(), primary_key=True),
                Column('artikelomschrijving', String),
                Column('artikelprijs', Float),
                Column('art_voorraad', Float),
                Column('art_eenheid', String),
                Column('locatie_magazijn', String))
                
            engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
            logger.debug("printFactuur(idx=%s): engine → %s", idx, engine, extra={"event.action": "printFactuur", "logrite.idx": idx})
            con = engine.connect()
            logger.debug("printFactuur(idx=%s): con → %s", idx, con, extra={"event.action": "printFactuur", "logrite.idx": idx})
            selova = select([orders_verkoop_artikelen,artikelen]).where(and_(\
              orders_verkoop_artikelen.c.ovbestelID == movbestnr, orders_verkoop_artikelen\
              .c.artikelID == artikelen.c.artikelID)).order_by(orders_verkoop_artikelen.c.ovaID)
            rpova = con.execute(selova)
            logger.debug("printFactuur(idx=%s): rpova → %s", idx, rpova, extra={"event.action": "printFactuur", "logrite.idx": idx})
                
            mblad = 1
            logger.debug("printFactuur(idx=%s): mblad → %s", idx, mblad, extra={"event.action": "printFactuur", "logrite.idx": idx})
            rgl = 0
            if platform == 'win32':
                filename = '.\\forms\\Weborders_Facturen\\Weborder-factuur_'+str(rpc[0])+'.txt'
            else:
                filename = './forms/Weborders_Facturen/Weborder-factuur_'+str(rpc[0])+'.txt' 
                logger.debug("printFactuur(idx=%s): filename → %s", idx, filename, extra={"event.action": "printFactuur", "logrite.idx": idx})
            adreskop=\
            ('\n\n\n\n\n\n\nFACTUUR\n\n'+rpc[10]+' '+rpc[11]+' '+rpc[12]+' '+rpc[13]+',\n'+\
             mstraat+' '+rpc[15]+rpc[16]+',\n'+\
             rpc[14]+' '+mplaats+'.\n\n\n\n\n')
            logger.debug("printFactuur(idx=%s): adreskop → %s", idx, adreskop, extra={"event.action": "printFactuur", "logrite.idx": idx})
            open(filename,'w').write(adreskop)
            mtotaal = 0
            logger.debug("printFactuur(idx=%s): mtotaal → %s", idx, mtotaal, extra={"event.action": "printFactuur", "logrite.idx": idx})
            
            for row in rpova:
                if rgl == 0:
                    kop =  Heading(movbestnr, mblad)
                    logger.debug("printFactuur(idx=%s): kop → %s", idx, kop, extra={"event.action": "printFactuur", "logrite.idx": idx})
                    open(filename, 'a').write(kop)
                    rgl = 16
                elif rgl%57 == 0:
                    mblad += 1
                    kop =  Heading(movbestnr, mblad)
                    open(filename, 'a').write(kop)
                msub = row[3]*row[5]
                logger.debug("printFactuur(idx=%s): msub → %s", idx, msub, extra={"event.action": "printFactuur", "logrite.idx": idx})
                open(filename,'a').write('{:<11d}'.format(row[2])+'{:<37.35s}'.format(row[11])+\
                 '{:>6s}'.format(row[14])+' '+'{:>6.2f}'.format(row[3])+'{:>10.2f}'.format(row[5])+\
                 ' '+'{:>10.2f}'.format(msub)+' '+'{:>10.2f}'.format(msub*21/121)+'\n')
                mtotaal = mtotaal+msub
                rgl += 1
           
            tail =(\
                   
            '----------------------------------------------------------------------------------------------\n'+
            'Totaal factuurbedrag inclusief 21% BTW                                  '+'{:10.2f}'.format(mtotaal)+' \n'+
            '==============================================================================================\n')    
            open(filename,'a').write(tail)
        printGeg(filename, movbestnr)
        logger.debug("<<< Exiting printFactuur(idx=%s)", idx, extra={"event.action": "printFactuur", "logrite.idx": idx})
            
    win = MyWindow(data_list, header)
    win.exec_()
    hoofdMenu(m_email)