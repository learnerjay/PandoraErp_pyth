from login import hoofdMenu
import datetime, os
from PyQt5.QtWidgets import (QLabel, QLineEdit, QGridLayout, QPushButton,
                QDialog, QMessageBox ,QComboBox, QTableView, QWidget)
from PyQt5.QtGui import (QRegExpValidator, QFont, QPixmap, QIcon, QColor, QMovie)
from PyQt5.QtCore import (Qt, QRegExp, QAbstractTableModel, QSize)
from sqlalchemy import (Table, Column, Integer, String, Float, ForeignKey,
                        MetaData, create_engine, select, update, insert, and_, func)
import logging
logger = logging.getLogger(__name__)

metadata = MetaData()
orders_inkoop = Table('orders_inkoop', metadata,
    Column('orderinkoopID', Integer, primary_key=True),
    Column('besteldatum', String),
    Column('goedgekeurd', String),
    Column('afgemeld', String),
    Column('betaald', String),
    Column('leverancierID', None, ForeignKey('leveranciers.leverancierID')),
    Column('status', Integer),
    Column('betaald_bedrag', Float))
orders_inkoop_materieel = Table('orders_inkoop_materieel', metadata,
    Column('order_inkoop_materieelID', Integer, primary_key=True),
    Column('orderinkoopID', None, ForeignKey('orders_inkoop.orderinkoopID')),
    Column('werknummerID', None, ForeignKey('werken.werknummerID')),
    Column('werk_omschr', String),
    Column('uren_opdracht', Float),
    Column('uurtarief', Float),
    Column('bedrag_opdracht', Float),
    Column('plan_start', String),
    Column('werk_start', String),
    Column('plan_gereed', String),
    Column('werk_gereed', String),
    Column('status', Integer),
    Column('servicesID', None, ForeignKey('params_services.serviceID')),
    Column('services_omschr', String),
    Column('leverancierID', None, ForeignKey('leveranciers.leverancierID')),
    Column('datum_opdracht', String))
calculaties = Table('calculaties', metadata,
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
    Column('robeltrein', Float),
    Column('calcID', Integer(), primary_key=True),
    Column('koppelnummer', Integer),
    Column('verwerkt', Integer),
    Column('omschrijving', String),
    Column('werkomschrijving', String),
    Column('hoeveelheid', Float),
    Column('clusterID', Integer),
    Column('eenheid', String))
params_services = Table('params_services', metadata,
    Column('servicesID', Integer, primary_key=True),
    Column('hourly_tariff', Float),
    Column('item', String))
werken = Table('werken', metadata,
    Column('werknummerID', Integer(), primary_key=True),
    Column('werkomschrijving', String(50)),
    Column('voortgangstatus', String(1)),
    Column('statusweek', String(6)),
    Column('aanneemsom', Float),
    Column('begr_materialen', Float),
    Column('begr_materieel', Float),
    Column('kosten_materieel', Float),
    Column('startweek', String),
    Column('betaald_bedrag', Float),
    Column('meerminderwerk', Float),
    Column('opdracht_datum', String),
    Column('werk_sleuvengraver_uren', Float),
    Column('werk_persapparaat_uren', Float),
    Column('werk_atlaskraan_uren', Float),
    Column('werk_kraan_groot_uren', Float),
    Column('werk_mainliner_uren', Float),
    Column('werk_hormachine_uren', Float),
    Column('werk_wagon_uren', Float),
    Column('werk_locomotor_uren', Float),
    Column('werk_locomotief_uren', Float),
    Column('werk_montagewagen_uren', Float),
    Column('werk_stormobiel_uren',Float),
    Column('werk_robeltrein_uren', Float))
leveranciers = Table('leveranciers', metadata,
    Column('leverancierID', Integer(), primary_key=True),
    Column('bedrijfsnaam', String),
    Column('rechtsvorm', String),
    Column('btwnummer', String),
    Column('kvknummer', String),
    Column('telnr', String),
    Column('postcode', String),
    Column('huisnummer', String),
    Column('toevoeging', String))

def _11check(mwerknr):
    logger.warning(">>> Entering _11check(mwerknr=%s)", mwerknr, extra={"event.action": "_11check", "logrite.mwerknr": mwerknr})
    number = str(mwerknr)
    logger.debug("_11check(mwerknr=%s): number → %s", mwerknr, number, extra={"event.action": "_11check", "logrite.mwerknr": mwerknr})
    total = 0
    fullnumber = number
    logger.debug("_11check(mwerknr=%s): total → %s", mwerknr, total, extra={"event.action": "_11check", "logrite.mwerknr": mwerknr})
    for i in range(8):
        total += int(fullnumber[i])*(9-i)
        logger.debug("_11check(mwerknr=%s): fullnumber → %s", mwerknr, fullnumber, extra={"event.action": "_11check", "logrite.mwerknr": mwerknr})
        checkdigit = total % 11 % 10
    if checkdigit == int(fullnumber[8]):
        return True
    else:
        logger.debug("<<< Exiting _11check(mwerknr=%s)", mwerknr, extra={"event.action": "_11check", "logrite.mwerknr": mwerknr})
        return False

def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})

def noRecords():
    logger.warning(">>> Entering noRecords()", extra={"event.action": "noRecords"})
    msg = QMessageBox()
    logger.debug("noRecords(): msg → %s", msg, extra={"event.action": "noRecords"})
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('No items found for the given selection!')
    msg.setWindowTitle('Purchase orders equipment')
    logger.debug("<<< Exiting noRecords()", extra={"event.action": "noRecords"})
    msg.exec_()

def foutInvoer():
    logger.warning(">>> Entering foutInvoer()", extra={"event.action": "foutInvoer"})
    msg = QMessageBox()
    logger.debug("foutInvoer(): msg → %s", msg, extra={"event.action": "foutInvoer"})
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('No required input. Re-enter data!')
    msg.setWindowTitle('Purchase orders equipment')
    logger.debug("<<< Exiting foutInvoer()", extra={"event.action": "foutInvoer"})
    msg.exec_()

def foutWerknr():
    logger.warning(">>> Entering foutWerknr()", extra={"event.action": "foutWerknr"})
    msg = QMessageBox()
    logger.debug("foutWerknr(): msg → %s", msg, extra={"event.action": "foutWerknr"})
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Incorrect worknumber!')
    msg.setWindowTitle('Purchase orders equipment')
    logger.debug("<<< Exiting foutWerknr()", extra={"event.action": "foutWerknr"})
    msg.exec_()

def  reservDone(message):
    logger.warning(">>> Entering reservDone(message=%s)", message, extra={"event.action": "reservDone", "logrite.message": message})
    msg = QMessageBox()
    logger.debug("reservDone(message=%s): msg → %s", message, msg, extra={"event.action": "reservDone", "logrite.message": message})
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Information)
    msg.setText(message)
    msg.setWindowTitle('Order-reservations for equipment')
    logger.debug("<<< Exiting reservDone(message=%s)", message, extra={"event.action": "reservDone", "logrite.message": message})
    msg.exec_()

def wijzigOK(ordernr):
    logger.warning(">>> Entering wijzigOK(ordernr=%s)", ordernr, extra={"event.action": "wijzigOK", "logrite.ordernr": ordernr})
    msg = QMessageBox()
    logger.debug("wijzigOK(ordernr=%s): msg → %s", ordernr, msg, extra={"event.action": "wijzigOK", "logrite.ordernr": ordernr})
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Information)
    msg.setText('Changing order '+str(ordernr)+' was successful!')
    msg.setWindowTitle('Order-reservations for equipment')
    logger.debug("<<< Exiting wijzigOK(ordernr=%s)", ordernr, extra={"event.action": "wijzigOK", "logrite.ordernr": ordernr})
    msg.exec_()

def orderingOK(message):
    logger.warning(">>> Entering orderingOK(message=%s)", message, extra={"event.action": "orderingOK", "logrite.message": message})
    msg = QMessageBox()
    logger.debug("orderingOK(message=%s): msg → %s", message, msg, extra={"event.action": "orderingOK", "logrite.message": message})
    msg.setFont(QFont("Arial", 10))
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Information)
    msg.setText(message)
    msg.setWindowTitle('Ordering equipment')
    logger.debug("<<< Exiting orderingOK(message=%s)", message, extra={"event.action": "orderingOK", "logrite.message": message})
    msg.exec_()

def printing():
    logger.warning(">>> Entering printing()", extra={"event.action": "printing"})
    msg = QMessageBox()
    logger.debug("printing(): msg → %s", msg, extra={"event.action": "printing"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Information)
    msg.setText('Wait printing starts')
    msg.setWindowTitle('Print Equipment orders')
    logger.debug("<<< Exiting printing()", extra={"event.action": "printing"})
    msg.exec_()

def printOrder(ordernr):
    logger.warning(">>> Entering printOrder(ordernr=%s)", ordernr, extra={"event.action": "printOrder", "logrite.ordernr": ordernr})
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("printOrder(ordernr=%s): engine → %s", ordernr, engine, extra={"event.action": "printOrder", "logrite.ordernr": ordernr})
    con = engine.connect()
    selprint = select([orders_inkoop_materieel, leveranciers]).where(orders_inkoop_materieel.c.orderinkoopID == ordernr, \
                                    leveranciers.c.leverancierID == orders_inkoop_materieel.c.leverancierID)
    logger.debug("printOrder(ordernr=%s): con → %s", ordernr, con, extra={"event.action": "printOrder", "logrite.ordernr": ordernr})
    rpprint = con.execute(selprint).first()
    from postcode import checkpostcode
    logger.debug("printOrder(ordernr=%s): selprint → %s", ordernr, selprint, extra={"event.action": "printOrder", "logrite.ordernr": ordernr})
    logger.debug("printOrder(ordernr=%s): rpprint → %s", ordernr, rpprint, extra={"event.action": "printOrder", "logrite.ordernr": ordernr})
    street, residence = checkpostcode(rpprint[22], int(rpprint[23]))
    rgl = 0
    kop=\
     ('Order number: '+ str(rpprint[1])+'          Order date: '+str(rpprint[15])+'\n'+
     '==============================================================================================\n'+
     'Ordernumber Equipment      Worknr.   Description work        Hours  Rate Start      Finish    \n'+
     '==============================================================================================\n')
    logger.debug("printOrder(ordernr=%s): kop → %s", ordernr, kop, extra={"event.action": "printOrder", "logrite.ordernr": ordernr})
    from sys import platform
    if platform == 'win32':
        filename = '.\\forms\\Equipment_Orders\\EquipmentOrder_' + str(rpprint[1]) + '.txt'
    else:
        filename = './forms/Equipment_Orders/EquipmentOrder_' + str(rpprint[1]) + '.txt'
        logger.debug("printOrder(ordernr=%s): filename → %s", ordernr, filename, extra={"event.action": "printOrder", "logrite.ordernr": ordernr})
    adreskop = \
        ('\n\n\n\n\n\n\nOrder\n\n' + rpprint[17] + ' ' + rpprint[18] + ',\n' + \
         street + ' ' + rpprint[23] + rpprint[24] + ',\n' + \
         rpprint[22] + ' ' + residence + '.\n\n\n\n\n')
    logger.debug("printOrder(ordernr=%s): adreskop → %s", ordernr, adreskop, extra={"event.action": "printOrder", "logrite.ordernr": ordernr})
    open(filename, 'w').write(adreskop)
    mtotaal = 0
    logger.debug("printOrder(ordernr=%s): mtotaal → %s", ordernr, mtotaal, extra={"event.action": "printOrder", "logrite.ordernr": ordernr})
    if rgl == 0:
        rgl = 16
    open(filename, 'a').write(kop)

    msub = rpprint[4] * rpprint[5]
    logger.debug("printOrder(ordernr=%s): msub → %s", ordernr, msub, extra={"event.action": "printOrder", "logrite.ordernr": ordernr})
    open(filename, 'a').write('{:<12d}'.format(rpprint[1]) + '{:<2d}'.format(rpprint[12]) + '{:<12s}'.format(rpprint[13]) + ' ' +  '{:<10d}'.format(rpprint[2]) + '{:<20s}'.format(rpprint[3]) + \
    ' ' + '{:>8.2f}'.format(rpprint[4]) + ' ' + '{:>3.2f}'.format(rpprint[5]) + ' ' + '{:<6s}'.format(rpprint[7])+' '+'{:>6s}'.format(rpprint[9]) + '\n')
    mtotaal = mtotaal + msub
    rgl += 1

    tail = ( \
       '----------------------------------------------------------------------------------------------\n' +
       'Total  order assignment excluding VAT :' + '{:10.2f}'.format(mtotaal) + ' \n' +
       '==============================================================================================\n')
    open(filename, 'a').write(tail)

    from sys import platform
    if platform == 'win32':
        os.startfile(filename, "print")
    else:
        os.system("lpr " + filename)
    printing()
    logger.debug("<<< Exiting printOrder(ordernr=%s)", ordernr, extra={"event.action": "printOrder", "logrite.ordernr": ordernr})

def maak11proef(basisnr):
   logger.warning(">>> Entering maak11proef(basisnr=%s)", basisnr, extra={"event.action": "maak11proef", "logrite.basisnr": basisnr})
   basisnr = str(basisnr)
   basisnr = str((int(basisnr[0:8]))+int(1))
   logger.debug("maak11proef(basisnr=%s): basisnr → %s", basisnr, basisnr, extra={"event.action": "maak11proef", "logrite.basisnr": basisnr})
   total = 0
   logger.debug("maak11proef(basisnr=%s): total → %s", basisnr, total, extra={"event.action": "maak11proef", "logrite.basisnr": basisnr})
   for i in range(int(8)):
       total += int(basisnr[i])*(int(9)-i)
   checkdigit = total % 11 % 10
   logger.debug("maak11proef(basisnr=%s): checkdigit → %s", basisnr, checkdigit, extra={"event.action": "maak11proef", "logrite.basisnr": basisnr})
   basisuitnr = basisnr+str(checkdigit)
   logger.debug("maak11proef(basisnr=%s): basisuitnr → %s", basisnr, basisuitnr, extra={"event.action": "maak11proef", "logrite.basisnr": basisnr})
   logger.debug("<<< Exiting maak11proef(basisnr=%s)", basisnr, extra={"event.action": "maak11proef", "logrite.basisnr": basisnr})
   return basisuitnr

def calKeuze(m_email, auth1, auth2, auth3):
    logger.warning(">>> Entering calKeuze(m_email=%s,auth1=%s,auth2=%s,auth3=%s)", m_email, auth1, auth2, auth3, extra={"event.action": "calKeuze", "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            self.setWindowTitle("Inkoop orders materieel")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))

            self.setFont(QFont('Arial', 10))

            grid = QGridLayout()
            grid.setSpacing(20)

            # Choice
            self.k0Edit = QComboBox()
            self.k0Edit.setFixedWidth(380)
            self.k0Edit.setFont(QFont("Arial", 10))
            self.k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            self.k0Edit.setCurrentIndex(0)
            self.k0Edit.addItem('    Kies   ')
            self.k0Edit.setEditable(True)
            self.k0Edit.lineEdit().setFont(QFont("Arial", 10))
            self.k0Edit.lineEdit().setReadOnly(True)
            self.k0Edit.lineEdit().setAlignment(Qt.AlignCenter)
            self.k0Edit.setItemData(0, Qt.AlignCenter, Qt.TextAlignmentRole)
            self.k0Edit.addItem('1. Reserveren orders')
            self.k0Edit.addItem('2. Bestellen / Wijzig orders')
            self.k0Edit.addItem('3. Opvragen gereserveerde orders op werknummer')
            self.k0Edit.addItem('4. Opvragen bestelde orders op werknummer')
            self.k0Edit.addItem('5. Opvragen gereed orders op werknummer')
            self.k0Edit.addItem('6. Opvragen betaalde orders op werknummer')
            self.k0Edit.addItem('7. Opvragen afgesloten order op werknummer')
            self.k0Edit.addItem('8. Opvragen alle orders op werknummer')

            if auth1:
                self.k0Edit.model().item(1).setEnabled(True)
                self.k0Edit.model().item(2).setEnabled(True)
                self.k0Edit.model().item(3).setEnabled(True)
                self.k0Edit.model().item(4).setEnabled(True)
                self.k0Edit.model().item(5).setEnabled(True)
                self.k0Edit.model().item(6).setEnabled(True)
                self.k0Edit.model().item(7).setEnabled(True)
                self.k0Edit.model().item(8).setEnabled(True)
            elif auth2:
                self.k0Edit.model().item(1).setEnabled(False)
                self.k0Edit.model().item(1).setForeground(QColor('darkgrey'))
                self.k0Edit.model().item(1).setBackground(QColor('gainsboro'))
                self.k0Edit.model().item(2).setEnabled(True)
                self.k0Edit.model().item(3).setEnabled(True)
                self.k0Edit.model().item(4).setEnabled(True)
                self.k0Edit.model().item(5).setEnabled(True)
                self.k0Edit.model().item(6).setEnabled(True)
                self.k0Edit.model().item(7).setEnabled(True)
                self.k0Edit.model().item(8).setEnabled(True)
            elif auth3:
                self.k0Edit.model().item(1).setEnabled(False)
                self.k0Edit.model().item(1).setForeground(QColor('darkgrey'))
                self.k0Edit.model().item(1).setBackground(QColor('gainsboro'))
                self.k0Edit.model().item(2).setEnabled(False)
                self.k0Edit.model().item(2).setForeground(QColor('darkgrey'))
                self.k0Edit.model().item(2).setBackground(QColor('gainsboro'))
                self.k0Edit.model().item(3).setEnabled(True)
                self.k0Edit.model().item(4).setEnabled(True)
                self.k0Edit.model().item(5).setEnabled(True)
                self.k0Edit.model().item(6).setEnabled(True)
                self.k0Edit.model().item(7).setEnabled(True)
                self.k0Edit.model().item(8).setEnabled(True)
            else:
                self.k0Edit.model().item(1).setEnabled(False)
                self.k0Edit.model().item(1).setForeground(QColor('darkgrey'))
                self.k0Edit.model().item(1).setBackground(QColor('gainsboro'))
                self.k0Edit.model().item(2).setEnabled(False)
                self.k0Edit.model().item(2).setForeground(QColor('darkgrey'))
                self.k0Edit.model().item(2).setBackground(QColor('gainsboro'))
                self.k0Edit.model().item(3).setEnabled(False)
                self.k0Edit.model().item(3).setForeground(QColor('darkgrey'))
                self.k0Edit.model().item(3).setBackground(QColor('gainsboro'))
                self.k0Edit.model().item(4).setEnabled(False)
                self.k0Edit.model().item(4).setForeground(QColor('darkgrey'))
                self.k0Edit.model().item(4).setBackground(QColor('gainsboro'))
                self.k0Edit.model().item(5).setEnabled(False)
                self.k0Edit.model().item(5).setForeground(QColor('darkgrey'))
                self.k0Edit.model().item(5).setBackground(QColor('gainsboro'))
                self.k0Edit.model().item(6).setEnabled(False)
                self.k0Edit.model().item(6).setForeground(QColor('darkgrey'))
                self.k0Edit.model().item(6).setBackground(QColor('gainsboro'))
                self.k0Edit.model().item(7).setEnabled(False)
                self.k0Edit.model().item(7).setForeground(QColor('darkgrey'))
                self.k0Edit.model().item(7).setBackground(QColor('gainsboro'))
                self.k0Edit.model().item(8).setEnabled(False)
                self.k0Edit.model().item(8).setForeground(QColor('darkgrey'))
                self.k0Edit.model().item(8).setBackground(QColor('gainsboro'))

            # Worknumber
            self.werknrEdit = QLineEdit('8')
            self.werknrEdit.setFixedWidth(100)
            self.werknrEdit.setFont(QFont("Arial", 10))
            self.werknrEdit.setStyleSheet('color: black; background-color: #F8F7EE')
            reg_ex = QRegExp("^[8]{1}[0-9]{8}$")
            input_validator = QRegExpValidator(reg_ex, self.werknrEdit)
            self.werknrEdit.setValidator(input_validator)

            pyqt = QLabel()
            movie = QMovie('./images/logos/pyqt.gif')
            pyqt.setMovie(movie)
            movie.setScaledSize(QSize(180, 60))
            movie.start()
            grid.addWidget(pyqt, 1, 0, 1, 2)

            def k0Changed():
                logger.warning(">>> Entering k0Changed()", extra={"event.action": "k0Changed"})
                logger.debug("k0Changed(): k0Edit → %s", k0Edit, extra={"event.action": "k0Changed"})
                logger.debug("<<< Exiting k0Changed()", extra={"event.action": "k0Changed"})
                self.k0Edit.setCurrentIndex(self.k0Edit.currentIndex())
            self.k0Edit.currentIndexChanged.connect(k0Changed)

            def werknrChanged():
                logger.warning(">>> Entering werknrChanged()", extra={"event.action": "werknrChanged"})
                logger.debug("werknrChanged(): werknrEdit → %s", werknrEdit, extra={"event.action": "werknrChanged"})
                self.werknrEdit.setText(self.werknrEdit.text())
            self.werknrEdit.textChanged.connect(werknrChanged)

            grid.addWidget(self.k0Edit, 2, 1)
            lbl1 = QLabel('Werknummer')
            lbl1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl1, 3, 0)
            grid.addWidget(self.werknrEdit, 3, 1)

            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 7, 0, 1, 2, Qt.AlignCenter)

            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo, 1, 1, 1, 1, Qt.AlignRight)

            applyBtn = QPushButton('Zoeken')
            applyBtn.clicked.connect(lambda: bepaalMatch(m_email, self.k0Edit.currentIndex(), self.werknrEdit.text(), auth1, auth2, auth3))

            grid.addWidget(applyBtn, 6, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial", 10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")

            cancelBtn = QPushButton('Sluiten')
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))

            grid.addWidget(cancelBtn, 6, 1, 1, 1, Qt.AlignCenter)
            cancelBtn.setFont(QFont("Arial", 10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")

            self.setLayout(grid)
            self.setGeometry(600, 300, 150, 150)
            logger.debug("<<< Exiting __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})

    window = Widget()
    window.exec_()

def bepaalMatch(m_email, mchoice, mwerknr, auth1, auth2, auth3):
    logger.warning(">>> Entering bepaalMatch(m_email=%s,mchoice=%s,mwerknr=%s,auth1=%s,auth2=%s,auth3=%s)", m_email, mchoice, mwerknr, auth1, auth2, auth3, extra={"event.action": "bepaalMatch", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
    if (len(str(mwerknr)) < 9 or  _11check(mwerknr) == False) :
        foutWerknr()
        return
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("bepaalMatch(m_email=%s,mchoice=%s,mwerknr=%s,auth1=%s,auth2=%s,auth3=%s): engine → %s", m_email, mchoice, mwerknr, auth1, auth2, auth3, engine, extra={"event.action": "bepaalMatch", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
    conn = engine.connect()
    logger.debug("bepaalMatch(m_email=%s,mchoice=%s,mwerknr=%s,auth1=%s,auth2=%s,auth3=%s): conn → %s", m_email, mchoice, mwerknr, auth1, auth2, auth3, conn, extra={"event.action": "bepaalMatch", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
    selpar = select([params_services]).order_by(params_services.c.servicesID)
    logger.debug("bepaalMatch(m_email=%s,mchoice=%s,mwerknr=%s,auth1=%s,auth2=%s,auth3=%s): selpar → %s", m_email, mchoice, mwerknr, auth1, auth2, auth3, selpar, extra={"event.action": "bepaalMatch", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
    rppar = conn.execute(selpar).fetchall()
    logger.debug("bepaalMatch(m_email=%s,mchoice=%s,mwerknr=%s,auth1=%s,auth2=%s,auth3=%s): rppar → %s", m_email, mchoice, mwerknr, auth1, auth2, auth3, rppar, extra={"event.action": "bepaalMatch", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})

    selcal1 = select([calculaties.c.verwerkt]).where(calculaties.c.koppelnummer==mwerknr)
    rpcal1 = conn.execute(selcal1).first()
    logger.debug("bepaalMatch(m_email=%s,mchoice=%s,mwerknr=%s,auth1=%s,auth2=%s,auth3=%s): rpcal1 → %s", m_email, mchoice, mwerknr, auth1, auth2, auth3, rpcal1, extra={"event.action": "bepaalMatch", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
    mstat = rpcal1[0]
    logger.debug("bepaalMatch(m_email=%s,mchoice=%s,mwerknr=%s,auth1=%s,auth2=%s,auth3=%s): mstat → %s", m_email, mchoice, mwerknr, auth1, auth2, auth3, mstat, extra={"event.action": "bepaalMatch", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})

    if mchoice == 1:
        selcal = select([calculaties]).where(and_(calculaties.c.koppelnummer == mwerknr, calculaties.c.verwerkt == 1))
        rpcal = conn.execute(selcal)
    elif mchoice == 2:
        selcal = select([calculaties]).where(and_(calculaties.c.koppelnummer == mwerknr, calculaties.c.verwerkt == 2))
        rpcal = conn.execute(selcal)
        logger.debug("bepaalMatch(m_email=%s,mchoice=%s,mwerknr=%s,auth1=%s,auth2=%s,auth3=%s): rpcal → %s", m_email, mchoice, mwerknr, auth1, auth2, auth3, rpcal, extra={"event.action": "bepaalMatch", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
    elif mchoice == 3:
        selcal = select([calculaties]).where(and_(calculaties.c.koppelnummer == mwerknr, calculaties.c.verwerkt == 3))
        rpcal = conn.execute(selcal)
    elif mchoice == 4:
        selcal = select([calculaties]).where(and_(calculaties.c.koppelnummer == mwerknr, calculaties.c.verwerkt == 4))
        rpcal = conn.execute(selcal)
    elif mchoice == 5:
        selcal = select([calculaties]).where(and_(calculaties.c.koppelnummer == mwerknr, calculaties.c.verwerkt == 5))
        rpcal = conn.execute(selcal)
    elif mchoice == 6:
        selcal = select([calculaties]).where(and_(calculaties.c.koppelnummer == mwerknr, calculaties.c.verwerkt == 6))
        rpcal = conn.execute(selcal)
    elif mchoice == 7:
        selcal = select([calculaties]).where(and_(calculaties.c.koppelnummer == mwerknr, calculaties.c.verwerkt == 7))
        rpcal = conn.execute(selcal)
    elif mchoice == 8:
        selcal = select([calculaties]).where(and_(calculaties.c.koppelnummer == mwerknr, calculaties.c.verwerkt > 0))
        rpcal = conn.execute(selcal)
    else:
        foutInvoer()
        logger.debug("<<< Exiting bepaalMatch(m_email=%s,mchoice=%s,mwerknr=%s,auth1=%s,auth2=%s,auth3=%s)", m_email, mchoice, mwerknr, auth1, auth2, auth3, extra={"event.action": "bepaalMatch", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
        return

    class Widget(QDialog):
        logger.error("Exception in bepaalMatch(m_email=%s,mchoice=%s,mwerknr=%s,auth1=%s,auth2=%s,auth3=%s)", m_email, mchoice, mwerknr, auth1, auth2, auth3, exc_info=True, extra={"event.action": "bepaalMatch", "event.category": "process", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
        def __init__(self, data_list, header, *args):
            logger.warning(">>> Entering __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})
            QWidget.__init__(self, *args, )
            self.setWindowTitle('Reserveren / Bestellen / Opvragen Materieel')
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            self.setWindowFlags(self.windowFlags() | Qt.WindowSystemMenuHint |
                                Qt.WindowMinMaxButtonsHint)

            self.setFont(QFont('Arial', 10))

            grid = QGridLayout()
            logger.debug("__init__(data_list=%s,header=%s): grid → %s", data_list, header, grid, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): grid → %s", self, data_list, header, grid, extra={"event.action": "__init__", "logrite.data_list": data_list})
            grid.setSpacing(20)

            pyqt = QLabel()
            logger.debug("__init__(data_list=%s,header=%s): pyqt → %s", data_list, header, pyqt, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): pyqt → %s", self, data_list, header, pyqt, extra={"event.action": "__init__", "logrite.data_list": data_list})
            movie = QMovie('./images/logos/pyqt.gif')
            logger.debug("__init__(self=%s,data_list=%s,header=%s): movie → %s", self, data_list, header, movie, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(data_list=%s,header=%s): movie → %s", data_list, header, movie, extra={"event.action": "__init__", "logrite.data_list": data_list})
            pyqt.setMovie(movie)
            movie.setScaledSize(QSize(240, 80))
            movie.start()
            grid.addWidget(pyqt, 1, 0, 1, 2)

            logo = QLabel()
            logger.debug("__init__(data_list=%s,header=%s): logo → %s", data_list, header, logo, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): logo → %s", self, data_list, header, logo, extra={"event.action": "__init__", "logrite.data_list": data_list})
            pixmap = QPixmap('./images/logos/logo.jpg')
            logger.debug("__init__(self=%s,data_list=%s,header=%s): pixmap → %s", self, data_list, header, pixmap, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(data_list=%s,header=%s): pixmap → %s", data_list, header, pixmap, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logo.setPixmap(pixmap)
            grid.addWidget(logo, 1, 9, 1, 1, Qt.AlignRight)

            if mchoice == 1:
                orderBtn = QPushButton('Reserveren orders')
                logger.debug("__init__(data_list=%s,header=%s): orderBtn → %s", data_list, header, orderBtn, extra={"event.action": "__init__", "logrite.data_list": data_list})
                logger.debug("__init__(self=%s,data_list=%s,header=%s): orderBtn → %s", self, data_list, header, orderBtn, extra={"event.action": "__init__", "logrite.data_list": data_list})
                orderBtn.clicked.connect(lambda: insertOrders(m_email, mchoice, mwerknr, nlist, auth1, auth2, auth3, self))
            elif mchoice == 2:
                orderBtn = QPushButton('Bestellen / Wijzigen Orders')
                orderBtn.setDisabled(True)
                modifyOrders(m_email, mchoice, mwerknr, nlist, auth1, auth2, auth3, self)
                self.close()
                calKeuze(m_email, auth1, auth2, auth3)
            else:
                if mstat == 1:
                    orderBtn = QPushButton('Reserveren orders')
                    orderBtn.setDisabled(True)
                elif mstat > 1:
                    orderBtn = QPushButton('Bestellen / Wijzigen Orders')
                    orderBtn.setDisabled(True)
                    modifyOrders(m_email, mchoice, mwerknr, nlist, auth1, auth2, auth3, self)
                    self.close()
                    calKeuze(m_email, auth1, auth2, auth3)

            orderBtn.setFont(QFont("Arial", 10))
            orderBtn.setFixedWidth(220)

            grid.addWidget(orderBtn, 1, 7, 1, 3,  Qt.AlignBottom)

            closeBtn = QPushButton('Sluiten')
            logger.debug("__init__(data_list=%s,header=%s): closeBtn → %s", data_list, header, closeBtn, extra={"event.action": "__init__", "logrite.data_list": data_list})
            logger.debug("__init__(self=%s,data_list=%s,header=%s): closeBtn → %s", self, data_list, header, closeBtn, extra={"event.action": "__init__", "logrite.data_list": data_list})
            closeBtn.clicked.connect(self.close)

            closeBtn.setFont(QFont("Arial", 10))
            closeBtn.setFixedWidth(100)

            grid.addWidget(closeBtn, 1, 6, 1, 1, Qt.AlignRight | Qt.AlignBottom)
            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 1, 5, 1, 1, Qt.AlignCenter | Qt.AlignBottom)

            self.setLayout(grid)
            self.setGeometry(50, 50, 1600, 900)

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
            grid.addWidget(table_view, 0, 0, 1, 10)

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
            logger.debug("<<< Exiting rowCount(parent=%s)", parent, extra={"event.action": "rowCount"})
            return len(self.mylist)

        def columnCount(self, parent):
            logger.warning(">>> Entering columnCount(parent=%s)", parent, extra={"event.action": "columnCount"})
            try:
                return len(self.mylist[0])
            except:
                logger.error("Exception in columnCount(parent=%s)", parent, exc_info=True, extra={"event.action": "columnCount", "event.category": "process"})
                logger.debug("<<< Exiting columnCount(parent=%s)", parent, extra={"event.action": "columnCount"})
                return 0

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

    header = ['Werknummer','Werkomschrijving', 'ClusterID', 'Cluster omschrijving', 'Eenheid', 'Aantal', 'Materieelnummer',
          'Materieel omschrijving', 'Aantal te bestellen uren', 'Uurtarief', 'Bedrag', 'Order Status']

    data_list = []
    nlist = []
    for row in rpcal:
        mkopnr = row[13]
        mstatus = row[14]
        omschr = row[15]
        werk = row[16]
        hoev = row[17]
        clusternr = row[18]
        eenheid = row[19]
        for rowidx in range(0, 12):
            if int(row[rowidx]) > 0 :
                servicenr = rppar[rowidx][0]
                serviceDescr = rppar[rowidx][2]
                amount_hours = round(row[rowidx],2)
                hour_tariff = round(rppar[rowidx][1],2)
                amount = round(row[rowidx] * rppar[rowidx][1],2)
                data_list += [(mkopnr, werk, clusternr, omschr, eenheid, hoev, servicenr, serviceDescr,
                             amount_hours, hour_tariff, amount, mstatus)]
                nlist += [[servicenr, serviceDescr, mkopnr, werk, amount_hours, hour_tariff, amount, mstatus]]

    win = Widget(data_list, header)
    win.exec_()

def insertOrders(m_email, mchoice, mwerknr, nlist, auth1, auth2, auth3, self):
    logger.warning(">>> Entering insertOrders(m_email=%s,mchoice=%s,mwerknr=%s,nlist=%s,auth1=%s,auth2=%s,auth3=%s)", m_email, mchoice, mwerknr, nlist, auth1, auth2, auth3, extra={"event.action": "insertOrders", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.nlist": nlist, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
    nlist = sorted(nlist)
    logger.debug("insertOrders(m_email=%s,mchoice=%s,mwerknr=%s,nlist=%s,auth1=%s,auth2=%s,auth3=%s): nlist → %s", m_email, mchoice, mwerknr, nlist, auth1, auth2, auth3, nlist, extra={"event.action": "insertOrders", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.nlist": nlist, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
    size = len(nlist)
    logger.debug("insertOrders(m_email=%s,mchoice=%s,mwerknr=%s,nlist=%s,auth1=%s,auth2=%s,auth3=%s): size → %s", m_email, mchoice, mwerknr, nlist, auth1, auth2, auth3, size, extra={"event.action": "insertOrders", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.nlist": nlist, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
    logger.debug("insertOrders(m_email=%s,mchoice=%s,mwerknr=%s,nlist=%s,auth1=%s,auth2=%s,auth3=%s,self=%s): size → %s", m_email, mchoice, mwerknr, nlist, auth1, auth2, auth3, self, size, extra={"event.action": "insertOrders", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.nlist": nlist, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
    for size in range(-len(nlist), -1):
        if nlist[size][0] == nlist[size + 1][0]:
            nlist[size + 1][4] = round(nlist[size][4] + nlist[size + 1][4], 2)
            nlist[size + 1][6] = round(nlist[size + 1][6] + nlist[size][6], 2)
            del nlist[size]
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("insertOrders(m_email=%s,mchoice=%s,mwerknr=%s,nlist=%s,auth1=%s,auth2=%s,auth3=%s): engine → %s", m_email, mchoice, mwerknr, nlist, auth1, auth2, auth3, engine, extra={"event.action": "insertOrders", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.nlist": nlist, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
    logger.debug("insertOrders(m_email=%s,mchoice=%s,mwerknr=%s,nlist=%s,auth1=%s,auth2=%s,auth3=%s,self=%s): engine → %s", m_email, mchoice, mwerknr, nlist, auth1, auth2, auth3, self, engine, extra={"event.action": "insertOrders", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.nlist": nlist, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
    logger.debug("insertOrders(m_email=%s,mchoice=%s,mwerknr=%s,nlist=%s,auth1=%s,auth2=%s,auth3=%s): matname → %s", m_email, mchoice, mwerknr, nlist, auth1, auth2, auth3, matname, extra={"event.action": "insertOrders", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.nlist": nlist, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
    logger.debug("insertOrders(m_email=%s,mchoice=%s,mwerknr=%s,nlist=%s,auth1=%s,auth2=%s,auth3=%s,self=%s): matname → %s", m_email, mchoice, mwerknr, nlist, auth1, auth2, auth3, self, matname, extra={"event.action": "insertOrders", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.nlist": nlist, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
    con = engine.connect()
    logger.debug("insertOrders(m_email=%s,mchoice=%s,mwerknr=%s,nlist=%s,auth1=%s,auth2=%s,auth3=%s,self=%s): con → %s", m_email, mchoice, mwerknr, nlist, auth1, auth2, auth3, self, con, extra={"event.action": "insertOrders", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.nlist": nlist, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
    logger.debug("insertOrders(m_email=%s,mchoice=%s,mwerknr=%s,nlist=%s,auth1=%s,auth2=%s,auth3=%s): con → %s", m_email, mchoice, mwerknr, nlist, auth1, auth2, auth3, con, extra={"event.action": "insertOrders", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.nlist": nlist, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
    # next loop of compressed nlist
    # produce an order for each row
    matname = ''
    for item in nlist:
        if item[7] == 1:
            try:
                matnr = (con.execute(select([func.max(orders_inkoop_materieel.c.order_inkoop_materieelID, type_=Integer)])).scalar())
                logger.debug("insertOrders(m_email=%s,mchoice=%s,mwerknr=%s,nlist=%s,auth1=%s,auth2=%s,auth3=%s,self=%s): matnr → %s", m_email, mchoice, mwerknr, nlist, auth1, auth2, auth3, self, matnr, extra={"event.action": "insertOrders", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.nlist": nlist, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
                matnr += 1
            except:
                logger.error("Exception in insertOrders(m_email=%s,mchoice=%s,mwerknr=%s,nlist=%s,auth1=%s,auth2=%s,auth3=%s)", m_email, mchoice, mwerknr, nlist, auth1, auth2, auth3, exc_info=True, extra={"event.action": "insertOrders", "event.category": "process", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.nlist": nlist, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
                matnr = 1
            try:
                ordnr = (con.execute(select([func.max(orders_inkoop.c.orderinkoopID, type_=Integer)])).scalar())
                ordnr = int(maak11proef(ordnr))
                logger.debug("insertOrders(m_email=%s,mchoice=%s,mwerknr=%s,nlist=%s,auth1=%s,auth2=%s,auth3=%s,self=%s): ordnr → %s", m_email, mchoice, mwerknr, nlist, auth1, auth2, auth3, self, ordnr, extra={"event.action": "insertOrders", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.nlist": nlist, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
            except:
                ordnr = 400000003
            try:
                upd = update(calculaties).where(calculaties.c.koppelnummer == mwerknr).values(verwerkt = 2)
                logger.debug("insertOrders(m_email=%s,mchoice=%s,mwerknr=%s,nlist=%s,auth1=%s,auth2=%s,auth3=%s): upd → %s", m_email, mchoice, mwerknr, nlist, auth1, auth2, auth3, upd, extra={"event.action": "insertOrders", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.nlist": nlist, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
                con.execute(upd)
                ins_inkoop = insert(orders_inkoop).values(orderinkoopID = ordnr, status = 2)
                logger.debug("insertOrders(m_email=%s,mchoice=%s,mwerknr=%s,nlist=%s,auth1=%s,auth2=%s,auth3=%s): ins_inkoop → %s", m_email, mchoice, mwerknr, nlist, auth1, auth2, auth3, ins_inkoop, extra={"event.action": "insertOrders", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.nlist": nlist, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
                logger.debug("insertOrders(m_email=%s,mchoice=%s,mwerknr=%s,nlist=%s,auth1=%s,auth2=%s,auth3=%s,self=%s): ins_inkoop → %s", m_email, mchoice, mwerknr, nlist, auth1, auth2, auth3, self, ins_inkoop, extra={"event.action": "insertOrders", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.nlist": nlist, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
                logger.debug("insertOrders(m_email=%s,mchoice=%s,mwerknr=%s,nlist=%s,auth1=%s,auth2=%s,auth3=%s): insertres → %s", m_email, mchoice, mwerknr, nlist, auth1, auth2, auth3, insertres, extra={"event.action": "insertOrders", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.nlist": nlist, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
                con.execute(ins_inkoop)
                insertres = insert(orders_inkoop_materieel).values(order_inkoop_materieelID = matnr, orderinkoopID = ordnr,
                    servicesID = item[0], services_omschr = item[1], werknummerID = item[2], werk_omschr = item[3],
                    uren_opdracht = item[4], uurtarief = item[5], bedrag_opdracht = item[6], status = 2)
                con.execute(insertres)
                matname = matname+'Order: '+str(ordnr)+', Equipment: '+str(matnr)+' , '+str(item[0])+' , '+str(item[1])+('\n')
            except Exception as e:
                logger.error("Exception in insertOrders(m_email=%s,mchoice=%s,mwerknr=%s,nlist=%s,auth1=%s,auth2=%s,auth3=%s): %s", m_email, mchoice, mwerknr, nlist, auth1, auth2, auth3, str(e), exc_info=True, extra={"event.action": "insertOrders", "event.category": "process", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.nlist": nlist, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
                noRecords()
                logger.debug("<<< Exiting insertOrders(m_email=%s,mchoice=%s,mwerknr=%s,nlist=%s,auth1=%s,auth2=%s,auth3=%s)", m_email, mchoice, mwerknr, nlist, auth1, auth2, auth3, extra={"event.action": "insertOrders", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.nlist": nlist, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
                return

    message = 'Reserveringen zijn gedaan voor: \n'+matname
    logger.debug("insertOrders(m_email=%s,mchoice=%s,mwerknr=%s,nlist=%s,auth1=%s,auth2=%s,auth3=%s,self=%s): message → %s", m_email, mchoice, mwerknr, nlist, auth1, auth2, auth3, self, message, extra={"event.action": "insertOrders", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.nlist": nlist, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
    reservDone(message)
    self.close()
    calKeuze(m_email, auth1,auth2,auth3)

def modifyOrders(m_email, mchoice, mwerknr, nlist, auth1, auth2, auth3, self):
    logger.warning(">>> Entering modifyOrders(m_email=%s,mchoice=%s,mwerknr=%s,nlist=%s,auth1=%s,auth2=%s,auth3=%s)", m_email, mchoice, mwerknr, nlist, auth1, auth2, auth3, extra={"event.action": "modifyOrders", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.nlist": nlist, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("modifyOrders(m_email=%s,mchoice=%s,mwerknr=%s,nlist=%s,auth1=%s,auth2=%s,auth3=%s): engine → %s", m_email, mchoice, mwerknr, nlist, auth1, auth2, auth3, engine, extra={"event.action": "modifyOrders", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.nlist": nlist, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
    logger.debug("modifyOrders(m_email=%s,mchoice=%s,mwerknr=%s,nlist=%s,auth1=%s,auth2=%s,auth3=%s,self=%s): engine → %s", m_email, mchoice, mwerknr, nlist, auth1, auth2, auth3, self, engine, extra={"event.action": "modifyOrders", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.nlist": nlist, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
    con = engine.connect()
    logger.debug("modifyOrders(m_email=%s,mchoice=%s,mwerknr=%s,nlist=%s,auth1=%s,auth2=%s,auth3=%s): con → %s", m_email, mchoice, mwerknr, nlist, auth1, auth2, auth3, con, extra={"event.action": "modifyOrders", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.nlist": nlist, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
    logger.debug("modifyOrders(m_email=%s,mchoice=%s,mwerknr=%s,nlist=%s,auth1=%s,auth2=%s,auth3=%s,self=%s): con → %s", m_email, mchoice, mwerknr, nlist, auth1, auth2, auth3, self, con, extra={"event.action": "modifyOrders", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.nlist": nlist, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})

    try:
        if mchoice < 3 or mchoice == 8:
            selord = (select([orders_inkoop_materieel.c.orderinkoopID,orders_inkoop_materieel.c.servicesID,
              orders_inkoop_materieel.c.services_omschr, orders_inkoop_materieel.c.werknummerID,orders_inkoop_materieel.c.werk_omschr,
              orders_inkoop_materieel.c.uren_opdracht,orders_inkoop_materieel.c.uurtarief, orders_inkoop_materieel.c.bedrag_opdracht,
              orders_inkoop_materieel.c.status]).where(orders_inkoop_materieel.c.werknummerID == mwerknr)
              .order_by(orders_inkoop_materieel.c.servicesID))
        elif mchoice == 3:
            selord = (select([orders_inkoop_materieel.c.orderinkoopID, orders_inkoop_materieel.c.servicesID,
              orders_inkoop_materieel.c.services_omschr, orders_inkoop_materieel.c.werknummerID,
              orders_inkoop_materieel.c.werk_omschr, orders_inkoop_materieel.c.uren_opdracht,
              orders_inkoop_materieel.c.uurtarief,orders_inkoop_materieel.c.bedrag_opdracht, orders_inkoop_materieel.c.status]).
              where(and_(orders_inkoop_materieel.c.werknummerID == mwerknr, orders_inkoop_materieel.c.status == 2))
              .order_by(orders_inkoop_materieel.c.servicesID))
        elif mchoice == 4:
            selord = (select([orders_inkoop_materieel.c.orderinkoopID, orders_inkoop_materieel.c.servicesID,
                  orders_inkoop_materieel.c.services_omschr, orders_inkoop_materieel.c.werknummerID,
                  orders_inkoop_materieel.c.werk_omschr, orders_inkoop_materieel.c.uren_opdracht,
                  orders_inkoop_materieel.c.uurtarief, orders_inkoop_materieel.c.bedrag_opdracht,
                  orders_inkoop_materieel.c.status]).where(and_(orders_inkoop_materieel.c.werknummerID == mwerknr,
                  orders_inkoop_materieel.c.status == 3)).order_by(orders_inkoop_materieel.c.servicesID))
        elif mchoice == 5:
            selord = (select([orders_inkoop_materieel.c.orderinkoopID, orders_inkoop_materieel.c.servicesID,
               orders_inkoop_materieel.c.services_omschr, orders_inkoop_materieel.c.werknummerID,
               orders_inkoop_materieel.c.werk_omschr, orders_inkoop_materieel.c.uren_opdracht, orders_inkoop_materieel.c.uurtarief,
               orders_inkoop_materieel.c.bedrag_opdracht,orders_inkoop_materieel.c.status]).
               where(and_(orders_inkoop_materieel.c.werknummerID == mwerknr, orders_inkoop_materieel.c.status == 4))
              .order_by(orders_inkoop_materieel.c.servicesID))
        elif mchoice == 6:
            selord = (select([orders_inkoop_materieel.c.orderinkoopID, orders_inkoop_materieel.c.servicesID,
              orders_inkoop_materieel.c.services_omschr, orders_inkoop_materieel.c.werknummerID,
              orders_inkoop_materieel.c.werk_omschr, orders_inkoop_materieel.c.uren_opdracht,orders_inkoop_materieel.c.uurtarief,
              orders_inkoop_materieel.c.bedrag_opdracht, orders_inkoop_materieel.c.status]).
              where(and_(orders_inkoop_materieel.c.werknummerID == mwerknr, orders_inkoop_materieel.c.status == 5))
              .order_by(orders_inkoop_materieel.c.servicesID))
        elif mchoice == 7:
            selord = (select([orders_inkoop_materieel.c.orderinkoopID, orders_inkoop_materieel.c.servicesID,
              orders_inkoop_materieel.c.services_omschr, orders_inkoop_materieel.c.werknummerID,
              orders_inkoop_materieel.c.werk_omschr, orders_inkoop_materieel.c.uren_opdracht,
              orders_inkoop_materieel.c.uurtarief, orders_inkoop_materieel.c.bedrag_opdracht, orders_inkoop_materieel.c.status]).
              where(and_(orders_inkoop_materieel.c.werknummerID == mwerknr, orders_inkoop_materieel.c.status == 6)).
              order_by(orders_inkoop_materieel.c.servicesID))
        rpord = con.execute(selord)
    except Exception as e:
        logger.debug("modifyOrders(m_email=%s,mchoice=%s,mwerknr=%s,nlist=%s,auth1=%s,auth2=%s,auth3=%s): rpord → %s", m_email, mchoice, mwerknr, nlist, auth1, auth2, auth3, rpord, extra={"event.action": "modifyOrders", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.nlist": nlist, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
        logger.debug("modifyOrders(m_email=%s,mchoice=%s,mwerknr=%s,nlist=%s,auth1=%s,auth2=%s,auth3=%s,self=%s): rpord → %s", m_email, mchoice, mwerknr, nlist, auth1, auth2, auth3, self, rpord, extra={"event.action": "modifyOrders", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.nlist": nlist, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
        print(str(e))
    class Widget(QDialog):
        logger.error("Exception in modifyOrders(m_email=%s,mchoice=%s,mwerknr=%s,nlist=%s,auth1=%s,auth2=%s,auth3=%s): %s", m_email, mchoice, mwerknr, nlist, auth1, auth2, auth3, str(e), exc_info=True, extra={"event.action": "modifyOrders", "event.category": "process", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.nlist": nlist, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
        def __init__(self, data_list, header, *args):
            logger.debug("<<< Exiting modifyOrders(m_email=%s,mchoice=%s,mwerknr=%s,nlist=%s,auth1=%s,auth2=%s,auth3=%s)", m_email, mchoice, mwerknr, nlist, auth1, auth2, auth3, extra={"event.action": "modifyOrders", "logrite.mchoice": mchoice, "logrite.mwerknr": mwerknr, "logrite.nlist": nlist, "logrite.auth1": auth1, "logrite.auth2": auth2, "logrite.auth3": auth3})
            QWidget.__init__(self, *args, )
            self.setWindowTitle('Bestellen / Wijzigen orders')
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            self.setWindowFlags(self.windowFlags() | Qt.WindowSystemMenuHint |
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
            table_view.clicked.connect(chooseInkooporder)
            grid.addWidget(table_view, 0, 0, 1, 10)

            pyqt = QLabel()
            movie = QMovie('./images/logos/pyqt.gif')
            pyqt.setMovie(movie)
            movie.setScaledSize(QSize(240, 80))
            movie.start()
            grid.addWidget(pyqt, 1, 0, 1, 2)

            logo = QLabel()
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo, 1, 9, 1, 1, Qt.AlignRight)

            closeBtn = QPushButton('Sluiten')
            closeBtn.clicked.connect(self.close)

            closeBtn.setFont(QFont("Arial", 10))
            closeBtn.setFixedWidth(100)

            grid.addWidget(closeBtn, 1, 8, 1, 1)

            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 1, 5, 1, 1,
                           Qt.AlignCenter | Qt.AlignBottom)

            self.setLayout(grid)
            self.setGeometry(50, 50, 1200, 900)

    class MyTableModel(QAbstractTableModel):
        def __init__(self, parent, mylist, header, *args):
            QAbstractTableModel.__init__(self, parent, *args)
            self.mylist = mylist
            self.header = header
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): inkorderEdit → %s", parent, inkorderEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): inkorderEdit → %s", self, parent, inkorderEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): werknrEdit → %s", parent, werknrEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): werknrEdit → %s", self, parent, werknrEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.q3Edit → %s", parent, self.q3Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q3Edit → %s", self, parent, q3Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): reg_ex → %s", parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): reg_ex → %s", self, parent, reg_ex, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): input_validator → %s", parent, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): input_validator → %s", self, parent, input_validator, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.q4Edit → %s", parent, self.q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): q4Edit → %s", self, parent, q4Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): self.k0Edit → %s", parent, self.k0Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): k0Edit → %s", self, parent, k0Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): slist → %s", self, parent, slist, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): grid → %s", parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): grid → %s", self, parent, grid, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lblord → %s", parent, lblord, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lblord → %s", self, parent, lblord, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl → %s", parent, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl → %s", self, parent, lbl, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): pixmap → %s", parent, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): pixmap → %s", self, parent, pixmap, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl1 → %s", parent, lbl1, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl1 → %s", self, parent, lbl1, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): strstatus → %s", parent, strstatus, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): strstatus → %s", self, parent, strstatus, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): sellev1 → %s", parent, sellev1, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): rplev1 → %s", parent, rplev1, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): rplev1 → %s", self, parent, rplev1, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl3 → %s", parent, lbl3, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl3 → %s", self, parent, lbl3, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl4 → %s", parent, lbl4, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl4 → %s", self, parent, lbl4, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl6 → %s", parent, lbl6, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl6 → %s", self, parent, lbl6, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl7 → %s", parent, lbl7, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl7 → %s", self, parent, lbl7, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): lbl5 → %s", parent, lbl5, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl5 → %s", self, parent, lbl5, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): orderBtn → %s", parent, orderBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): orderBtn → %s", self, parent, orderBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): printBtn → %s", parent, printBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): printBtn → %s", self, parent, printBtn, extra={"event.action": "__init__"})
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})

        def rowCount(self, parent):
            return len(self.mylist)

        def columnCount(self, parent):
            try:
                return len(self.mylist[0])
            except:
                return 0

        def data(self, index, role):
            veld = self.mylist[index.row()][index.column()]
            if not index.isValid():
                return None
            elif role == Qt.TextAlignmentRole and (type(veld) == float or type(veld) == int):
                return Qt.AlignRight | Qt.AlignVCenter
            elif role != Qt.DisplayRole:
                return None
            if type(veld) == float:
                return '{:12.2f}'.format(veld)
            else:
                return veld

        def headerData(self, col, orientation, role):
            if orientation == Qt.Horizontal and role == Qt.DisplayRole:
                return self.header[col]
            return None

    header = ['Ordernummer', 'MaterieelID', 'Materieel omschrijving', 'Werknummer', 'Werkomschrijving', 'Begrote uren', 'Uurtarief',
              'Bedrag subtotaal', 'Order Status', 'OrderInkoopID']

    data_list = []
    for row in rpord:
        data_list += [(row)]

    def chooseInkooporder(idx):
        logger.warning(">>> Entering chooseInkooporder(idx=%s)", idx, extra={"event.action": "chooseInkooporder", "logrite.idx": idx})
        ordernr = idx.data()
        logger.debug("chooseInkooporder(idx=%s): ordernr → %s", idx, ordernr, extra={"event.action": "chooseInkooporder", "logrite.idx": idx})
        if idx.column() == 0:
            try:
                selorder = select([orders_inkoop_materieel, orders_inkoop]).where(and_(orders_inkoop.c.orderinkoopID ==
                             ordernr, orders_inkoop_materieel.c.orderinkoopID == orders_inkoop.c.orderinkoopID))
                rporder = con.execute(selorder).first()
            except Exception as e:
                logger.debug("chooseInkooporder(idx=%s): rporder → %s", idx, rporder, extra={"event.action": "chooseInkooporder", "logrite.idx": idx})
                print(str(e))
                noRecords()
                return
            try:
                sellev = select([leveranciers.c.leverancierID, leveranciers.c.bedrijfsnaam, leveranciers.c.rechtsvorm,
                            leveranciers.c.postcode, leveranciers.c.huisnummer]).order_by(leveranciers.c.bedrijfsnaam)
                rplev = con.execute(sellev)
            except:
                logger.debug("chooseInkooporder(idx=%s): rplev → %s", idx, rplev, extra={"event.action": "chooseInkooporder", "logrite.idx": idx})
                noRecords()
                logger.error("Exception in chooseInkooporder(idx=%s)", idx, exc_info=True, extra={"event.action": "chooseInkooporder", "event.category": "process", "logrite.idx": idx})
                logger.debug("<<< Exiting chooseInkooporder(idx=%s)", idx, extra={"event.action": "chooseInkooporder", "logrite.idx": idx})
                return

            class Widget(QDialog):
                def __init__(self, parent=None):
                    super(Widget, self).__init__(parent)
                    logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
                    self.setWindowTitle("Ordering Modify Equipment for "+mwerknr)
                    self.setWindowIcon(QIcon('./images/logos/logo.jpg'))

                    self.setFont(QFont('Arial', 10))

                    #Purchase order
                    inkorderEdit = QLineEdit(str(ordernr))
                    inkorderEdit.setDisabled(True)
                    inkorderEdit.setAlignment(Qt.AlignRight)
                    inkorderEdit.setFixedWidth(100)
                    inkorderEdit.setFont(QFont("Arial", 10))

                    # Work number
                    werknrEdit = QLineEdit(str(mwerknr))
                    werknrEdit.setFixedWidth(100)
                    werknrEdit.setAlignment(Qt.AlignRight)
                    werknrEdit.setDisabled(True)
                    werknrEdit.setFont(QFont("Arial", 10))

                    # Start planned
                    self.q3Edit = QLineEdit(rporder[7])
                    self.q3Edit.setCursorPosition(0)
                    self.q3Edit.setFixedWidth(130)
                    self.q3Edit.setFont(QFont("Arial", 10))
                    reg_ex = QRegExp('^[2]{1}[0]{1}[0-9]{2}[-]{1}[0-1]{1}[0-9]{1}[-]{1}[0-3]{1}[0-9]{1}$')
                    input_validator = QRegExpValidator(reg_ex, self.q3Edit)
                    self.q3Edit.setValidator(input_validator)

                    # Finish planned
                    self.q4Edit = QLineEdit(rporder[9])
                    self.q4Edit.setCursorPosition(0)
                    self.q4Edit.setFixedWidth(130)
                    self.q4Edit.setFont(QFont("Arial", 10))
                    reg_ex = QRegExp('^[2]{1}[0]{1}[0-9]{2}[-]{1}[0-1]{1}[0-9]{1}[-]{1}[0-3]{1}[0-9]{1}$')
                    input_validator = QRegExpValidator(reg_ex,self.q4Edit)
                    self.q4Edit.setValidator(input_validator)

                    # Supplier
                    self.k0Edit = QComboBox()
                    self.k0Edit.setFixedWidth(400)
                    self.k0Edit.setFont(QFont("Arial", 10))
                    self.k0Edit.setStyleSheet('color: black; background-color: #F8F7EE')
                    self.k0Edit.setMaxVisibleItems(15)
                    self.k0Edit.addItem('                      Choose Supplier')
                    k = 0
                    slist = []
                    for row in rplev:
                        slist += [(row)]
                        self.k0Edit.addItem(str(slist[k][0])+' '+slist[k][1]+' '+slist[k][2])
                        k += 1

                    grid = QGridLayout()
                    grid.setSpacing(20)

                    lblord = QLabel('              Ordering / View Equipment    ')
                    lblord.setStyleSheet("font: 18pt Comic Sans MS; color: black ; background-color: #D9E1DF")
                    grid.addWidget(lblord, 1, 0, 1, 4, Qt.AlignCenter)

                    lbl = QLabel()
                    pixmap = QPixmap('./images/logos/verbinding.jpg')
                    lbl.setPixmap(pixmap)
                    grid.addWidget(lbl, 1, 0)

                    self.setFont(QFont('Arial', 10))

                    lbl1 = QLabel('Order number')
                    lbl1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    grid.addWidget(lbl1, 5, 0)
                    grid.addWidget(inkorderEdit, 5, 1)

                    grid.addWidget(QLabel('Work number'), 6, 0, 1, 1, Qt.AlignRight)
                    grid.addWidget(werknrEdit, 6, 1)

                    grid.addWidget(self.k0Edit, 7, 1, 1, 3)
                    grid.addWidget(QLabel('*'), 7, 0, Qt.AlignRight)

                    mstatus = rporder[11]
                    if mstatus == 0:
                        strstatus = 'calculatie'
                    elif mstatus == 1:
                        strstatus = 'werk gekoppeld'
                    elif mstatus == 2:
                        strstatus = 'gereserveerd'
                    elif mstatus == 3:
                        strstatus = 'besteld'
                    elif mstatus == 4:
                        strstatus = 'gereed'
                    elif mstatus == 5:
                        strstatus = 'betalld'
                    else:
                        strstatus = 'afgesloten'

                    orderdate = ''
                    if mstatus > 2:
                        sellev1 = select([leveranciers]).where(and_(leveranciers.c.leverancierID == orders_inkoop.c.leverancierID,
                                orders_inkoop.c.orderinkoopID == ordernr))
                        rplev1 = con.execute(sellev1).first()
                        orderdate = rporder[15]
                        lbl3 = QLabel('Materieel: ' + str(rporder[12]) + '  ' + rporder[13])
                        grid.addWidget(lbl3, 6, 2, 1, 2)
                        lbl4 = QLabel('Leverancier: ' + str(rplev1[0])+'\n'+rplev1[1]+' '+rplev1[2])
                        grid.addWidget(lbl4, 9, 2, 1, 2)
                        lbl6 = QLabel('Begrote uren   : ' + str(round(rporder[4], 2)) + '\nUurtarief           :   ' + str(round(rporder[5], 2)))
                        grid.addWidget(lbl6, 8, 2, 1, 2)
                        lbl7 = QLabel('Totaal     : ')
                        grid.addWidget(lbl7, 11, 0)
                        grid.addWidget(QLabel(str(round(rporder[6], 2))), 11, 1)

                    lbl5 = QLabel('Order status: '+strstatus+'\n'+'Order datum : '+orderdate)
                    if orderdate == '':
                        lbl5 = QLabel('Order status: '+strstatus)
                    grid.addWidget(lbl5, 5, 2, 1, 2)

                    lbl6 = QLabel('Geplande start            *')
                    grid.addWidget(lbl6, 8, 0)
                    grid.addWidget(self.q3Edit, 8, 1)

                    lbl7 = QLabel('Gepland gereed          *')
                    grid.addWidget(lbl7, 9, 0)
                    grid.addWidget(self.q4Edit, 9, 1)
                    grid.addWidget(QLabel('*Verplicht'), 7, 0)

                    logo = QLabel()
                    pixmap = QPixmap('./images/logos/logo.jpg')
                    logo.setPixmap(pixmap)
                    grid.addWidget(logo, 1, 3, 1, 1, Qt.AlignRight)

                    self.setLayout(grid)
                    self.setGeometry(600, 150, 150, 150)

                    orderBtn = QPushButton('Bestel')
                    orderBtn.clicked.connect(lambda: showResults(self))

                    grid.addWidget(orderBtn, 12, 3, 1, 1, Qt.AlignRight)
                    orderBtn.setFont(QFont("Arial", 10))
                    orderBtn.setFixedWidth(100)
                    orderBtn.setStyleSheet("color: black;  background-color: gainsboro")

                    printBtn = QPushButton('Print order')
                    printBtn.clicked.connect(lambda: printOrder(ordernr))

                    grid.addWidget(printBtn, 12, 2, 1, 1, Qt.AlignRight)
                    printBtn.setFont(QFont("Arial", 10))
                    printBtn.setFixedWidth(100)
                    printBtn.setStyleSheet("color: black;  background-color: gainsboro")
                
                    if auth1 and mchoice == 2 and mstatus == 2:      # insert   reservation/insert   reserved
                        orderBtn.setEnabled(True)
                        printBtn.setEnabled(False)
                        self.q3Edit.setEnabled(True)
                        self.q4Edit.setEnabled(True)
                        self.k0Edit.setEnabled(True)
                    elif auth1 and mchoice == 2 and mstatus > 2:     # insert  reservation/insert  ordered
                        orderBtn.setEnabled(False)
                        printBtn.setEnabled(True)
                        self.q3Edit.setEnabled(False)
                        self.q4Edit.setEnabled(False)
                        self.k0Edit.setEnabled(False)
                    elif auth1 and mchoice == 3:                     # insert ordered
                        printBtn.setEnabled(False)
                        orderBtn.setEnabled(False)
                        self.q3Edit.setEnabled(False)
                        self.q4Edit.setEnabled(False)
                        self.k0Edit.setEnabled(False)
                    elif auth2:                                      #modify
                        orderBtn.setEnabled(False)
                        printBtn.setEnabled(False)
                        self.q3Edit.setEnabled(False)
                        self.q4Edit.setEnabled(False)
                        self.k0Edit.setEnabled(False)
                    else:                                            # query
                        logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
                        orderBtn.setEnabled(False)
                        printBtn.setEnabled(False)
                        self.q3Edit.setEnabled(False)
                        self.q4Edit.setEnabled(False)
                        self.k0Edit.setEnabled(False)

                    def q3Changed():
                        logger.warning(">>> Entering q3Changed()", extra={"event.action": "q3Changed"})
                        logger.debug("q3Changed(): q3Edit → %s", q3Edit, extra={"event.action": "q3Changed"})
                        self.q3Edit.setText(self.q3Edit.text())
                    self.q3Edit.textChanged.connect(q3Changed)

                    def q4Changed():
                        logger.warning(">>> Entering q4Changed()", extra={"event.action": "q4Changed"})
                        logger.debug("q4Changed(): q4Edit → %s", q4Edit, extra={"event.action": "q4Changed"})
                        self.q4Edit.setText(self.q4Edit.text())
                    self.q4Edit.textChanged.connect(q4Changed)

                    def k0Changed():
                        logger.warning(">>> Entering k0Changed()", extra={"event.action": "k0Changed"})
                        self.k0Edit.setCurrentText(self.k0Edit.currentText())
                        logger.debug("<<< Exiting k0Changed()", extra={"event.action": "k0Changed"})
                        self.k0Edit.setCurrentIndex(self.k0Edit.currentIndex())
                    self.k0Edit.activated.connect(k0Changed)

                    def showResults(self):
                        logger.warning(">>> Entering showResults()", extra={"event.action": "showResults"})
                        leverancier = self.k0Edit.currentText()
                        logger.debug("showResults(): leverancier → %s", leverancier, extra={"event.action": "showResults"})
                        logger.debug("showResults(self=%s): leverancier → %s", self, leverancier, extra={"event.action": "showResults"})
                        leverancier_index = self.k0Edit.currentIndex()-1
                        logger.debug("showResults(): leverancier_index → %s", leverancier_index, extra={"event.action": "showResults"})
                        logger.debug("showResults(self=%s): leverancier_index → %s", self, leverancier_index, extra={"event.action": "showResults"})
                        startdate = self.q3Edit.text()
                        logger.debug("showResults(): startdate → %s", startdate, extra={"event.action": "showResults"})
                        logger.debug("showResults(self=%s): startdate → %s", self, startdate, extra={"event.action": "showResults"})
                        finishdate = self.q4Edit.text()
                        logger.debug("showResults(): finishdate → %s", finishdate, extra={"event.action": "showResults"})
                        logger.debug("showResults(self=%s): finishdate → %s", self, finishdate, extra={"event.action": "showResults"})
                        if len(startdate) < 10 or len(finishdate) < 10 or self.k0Edit.currentIndex() == 0:
                            foutInvoer()
                            return
                        leverancierlist = slist[leverancier_index]
                        dt = str(datetime.datetime.now())[0:10]
                        logger.debug("<<< Exiting showResults()", extra={"event.action": "showResults"})
                        updord = update(orders_inkoop).where(orders_inkoop.c.orderinkoopID == ordernr)\
                            .values(besteldatum = dt, leverancierID = leverancierlist[0], status = 3)
                        logger.debug("showResults(self=%s): leverancierlist → %s", self, leverancierlist, extra={"event.action": "showResults"})
                        con.execute(updord)
                        updmatord = update(orders_inkoop_materieel).where(orders_inkoop_materieel.c.orderinkoopID == ordernr)\
                           .values(leverancierID = leverancierlist[0], datum_opdracht = dt, plan_start = startdate,\
                            plan_gereed = finishdate, status = 3)
                        con.execute(updmatord)
                        orderingOK('Ordering of '+str(ordernr)+' is successful' + '\nYou can now print the order!')
                        orderBtn.setDisabled(True)
                        logger.debug("showResults(self=%s): orderBtn → %s", self, orderBtn, extra={"event.action": "showResults"})
                        logger.debug("showResults(self=%s): printBtn → %s", self, printBtn, extra={"event.action": "showResults"})
                        printBtn.setEnabled(True)
                        # self.close()

                    selwerk = select([werken]).where(and_(werken.c.werknummerID == mwerknr, orders_inkoop_materieel.c.werknummerID == werken.c.werknummerID))
                    rpwerk = con.execute(selwerk).first()

                    real_equipment_hours = rpwerk[rporder[12]+11]

                    lblmod = QLabel('               Wijzig / Opvragen Materieel             ')
                    lblmod.setStyleSheet("font: 18pt Comic Sans MS; color: black ; background-color: #D9E1DF")
                    grid.addWidget(lblmod, 13, 0 , 1, 4, Qt.AlignCenter)

                    # Actual start
                    self.q1Edit = QLineEdit(rporder[8])
                    self.q1Edit.setCursorPosition(0)
                    self.q1Edit.setFixedWidth(130)
                    self.q1Edit.setFont(QFont("Arial", 10))
                    reg_ex = QRegExp('^[2]{1}[0]{1}[0-9]{2}[-]{1}[0-1]{1}[0-9]{1}[-]{1}[0-3]{1}[0-9]{1}$')
                    input_validator = QRegExpValidator(reg_ex, self.q1Edit)
                    self.q1Edit.setValidator(input_validator)

                    # Actual finish
                    self.q6Edit = QLineEdit(rporder[10])
                    self.q6Edit.setCursorPosition(0)
                    self.q6Edit.setFixedWidth(130)
                    self.q6Edit.setFont(QFont("Arial", 10))
                    reg_ex = QRegExp('^[2]{1}[0]{1}[0-9]{2}[-]{1}[0-1]{1}[0-9]{1}[-]{1}[0-3]{1}[0-9]{1}$')
                    input_validator = QRegExpValidator(reg_ex, self.q6Edit)
                    self.q6Edit.setValidator(input_validator)

                    # Actual hours by work number and equipment
                    self.q9Edit = QLineEdit(str(round(real_equipment_hours, 2)))
                    self.q9Edit.setCursorPosition(0)
                    self.q9Edit.setFixedWidth(130)
                    self.q9Edit.setDisabled(True)
                    self.q9Edit.setFont(QFont("Arial", 10))

                    # Order approved date
                    self.q8Edit = QLineEdit(rporder[18])
                    self.q8Edit.setCursorPosition(0)
                    self.q8Edit.setFixedWidth(130)
                    self.q8Edit.setFont(QFont("Arial", 10))
                    reg_ex = QRegExp('^[2]{1}[0]{1}[0-9]{2}[-]{1}[0-1]{1}[0-9]{1}[-]{1}[0-3]{1}[0-9]{1}$')
                    input_validator = QRegExpValidator(reg_ex, self.q8Edit)
                    self.q8Edit.setValidator(input_validator)

                    # Order paid date
                    self.q7Edit = QLineEdit(rporder[20])
                    self.q7Edit.setCursorPosition(0)
                    self.q7Edit.setFixedWidth(130)
                    self.q7Edit.setFont(QFont("Arial", 10))
                    reg_ex = QRegExp('^[2]{1}[0]{1}[0-9]{2}[-]{1}[0-1]{1}[0-9]{1}[-]{1}[0-3]{1}[0-9]{1}$')
                    input_validator = QRegExpValidator(reg_ex, self.q7Edit)
                    self.q7Edit.setValidator(input_validator)

                    # order closed
                    self.q2Edit = QLineEdit(rporder[19])
                    self.q2Edit.setCursorPosition(0)
                    self.q2Edit.setFixedWidth(130)
                    self.q2Edit.setFont(QFont("Arial", 10))
                    reg_ex = QRegExp('^[2]{1}[0]{1}[0-9]{2}[-]{1}[0-1]{1}[0-9]{1}[-]{1}[0-3]{1}[0-9]{1}$')
                    input_validator = QRegExpValidator(reg_ex, self.q2Edit)
                    self.q2Edit.setValidator(input_validator)

                    # Invoice
                    self.q5Edit = QLineEdit('0')
                    self.q5Edit.setCursorPosition(0)
                    self.q5Edit.setFixedWidth(130)
                    self.q5Edit.setFont(QFont("Arial", 10))
                    reg_ex = QRegExp("^[-+]?[0-9]*\\.?[0-9]+$")
                    input_validator = QRegExpValidator(reg_ex, self.q5Edit)
                    self.q5Edit.setValidator(input_validator)

                    # Amount paid
                    self.q10Edit = QLineEdit(str(float(round(rporder[23], 2))))
                    self.q10Edit.setCursorPosition(0)
                    self.q10Edit.setDisabled(True)
                    self.q10Edit.setFixedWidth(130)
                    self.q10Edit.setFont(QFont("Arial", 10))

                    lbl10 = QLabel('Start werk datum')
                    grid.addWidget(lbl10, 14, 0)
                    grid.addWidget(self.q1Edit, 14, 1)

                    lbl11 = QLabel('Einde werk datum')
                    grid.addWidget(lbl11, 14, 2)
                    grid.addWidget(self.q6Edit, 14, 3)

                    lbl12 = QLabel('Werkelijke uren')
                    grid.addWidget(lbl12, 15, 0)
                    grid.addWidget(self.q9Edit, 15, 1)

                    lbl14 = QLabel('Goedgekeurd werk datum')
                    grid.addWidget(lbl14, 15, 2)
                    grid.addWidget(self.q8Edit, 15, 3)

                    lbl15 = QLabel('Totaal betaald datum')
                    grid.addWidget(lbl15, 16, 0)
                    grid.addWidget(self.q7Edit, 16, 1)

                    lbl16 = QLabel('Gesloten order datum')
                    grid.addWidget(lbl16, 16, 2)
                    grid.addWidget(self.q2Edit, 16, 3)

                    lbl17 = QLabel('Rekening bedrag te betalen')
                    grid.addWidget(lbl17, 17, 0)
                    grid.addWidget(self.q5Edit, 17,1)

                    lbl18 = QLabel('Totaal bedrag betaald')
                    grid.addWidget(lbl18, 17, 2)
                    grid.addWidget(self.q10Edit, 17, 3)

                    modifyBtn = QPushButton('Wijzig')
                    modifyBtn.clicked.connect(lambda: saveModified(self, mstatus))

                    grid.addWidget(modifyBtn, 18, 3, Qt.AlignRight)
                    modifyBtn.setFont(QFont("Arial", 10))
                    modifyBtn.setFixedWidth(100)
                    modifyBtn.setStyleSheet("color: black;  background-color: gainsboro")

                    if ((mchoice == 1 or mchoice == 2) and (mstatus < 3)) or mchoice > 2 or mstatus == 6:
                        self.q1Edit.setDisabled(True)
                        self.q2Edit.setDisabled(True)
                        self.q5Edit.setDisabled(True)
                        self.q6Edit.setDisabled(True)
                        self.q7Edit.setDisabled(True)
                        self.q8Edit.setDisabled(True)
                        modifyBtn.setDisabled(True)

                    closeBtn = QPushButton('Sluiten')
                    closeBtn.clicked.connect(self.close)

                    grid.addWidget(closeBtn, 18, 2, Qt.AlignRight)
                    closeBtn.setFont(QFont("Arial", 10))
                    closeBtn.setFixedWidth(100)
                    closeBtn.setStyleSheet("color: black;  background-color: gainsboro")

                    grid.addWidget(QLabel('\u00A9 2017 all rights reserved - dj.jansen@casema.nl'), 19, 0, 1, 4,
                                   Qt.AlignCenter)

                    def q1Changed():
                        logger.warning(">>> Entering q1Changed()", extra={"event.action": "q1Changed"})
                        logger.debug("q1Changed(): q1Edit → %s", q1Edit, extra={"event.action": "q1Changed"})
                        self.q1Edit.setText(self.q1Edit.text())
                    self.q3Edit.textChanged.connect(q1Changed)

                    def q6Changed():
                        logger.warning(">>> Entering q6Changed()", extra={"event.action": "q6Changed"})
                        logger.debug("q6Changed(): q6Edit → %s", q6Edit, extra={"event.action": "q6Changed"})
                        self.q6Edit.setText(self.q6Edit.text())
                    self.q6Edit.textChanged.connect(q6Changed)

                    def q8Changed():
                        logger.warning(">>> Entering q8Changed()", extra={"event.action": "q8Changed"})
                        logger.debug("q8Changed(): q8Edit → %s", q8Edit, extra={"event.action": "q8Changed"})
                        self.q8Edit.setText(self.q8Edit.text())
                    self.q8Edit.textChanged.connect(q8Changed)

                    def q7Changed():
                        logger.warning(">>> Entering q7Changed()", extra={"event.action": "q7Changed"})
                        logger.debug("q7Changed(): q7Edit → %s", q7Edit, extra={"event.action": "q7Changed"})
                        self.q7Edit.setText(self.q7Edit.text())
                    self.q7Edit.textChanged.connect(q7Changed)

                    def q2Changed():
                        logger.warning(">>> Entering q2Changed()", extra={"event.action": "q2Changed"})
                        logger.debug("q2Changed(): q2Edit → %s", q2Edit, extra={"event.action": "q2Changed"})
                        self.q2Edit.setText(self.q2Edit.text())
                    self.q3Edit.textChanged.connect(q2Changed)

                    def saveModified(self,mstatus):
                        logger.warning(">>> Entering saveModified(mstatus=%s)", mstatus, extra={"event.action": "saveModified", "logrite.mstatus": mstatus})
                        start = self.q1Edit.text()       # date
                        finish = self.q6Edit.text()      # date
                        logger.debug("saveModified(mstatus=%s): finish → %s", mstatus, finish, extra={"event.action": "saveModified", "logrite.mstatus": mstatus})
                        logger.debug("saveModified(self=%s,mstatus=%s): finish → %s", self, mstatus, finish, extra={"event.action": "saveModified", "logrite.mstatus": mstatus})
                        if len(finish) == 10:
                            mstatus = 4
                        approved = self.q8Edit.text()    # date
                        logger.debug("saveModified(mstatus=%s): approved → %s", mstatus, approved, extra={"event.action": "saveModified", "logrite.mstatus": mstatus})
                        logger.debug("saveModified(self=%s,mstatus=%s): approved → %s", self, mstatus, approved, extra={"event.action": "saveModified", "logrite.mstatus": mstatus})
                        logger.debug("saveModified(mstatus=%s): closed → %s", mstatus, closed, extra={"event.action": "saveModified", "logrite.mstatus": mstatus})
                        logger.debug("saveModified(self=%s,mstatus=%s): closed → %s", self, mstatus, closed, extra={"event.action": "saveModified", "logrite.mstatus": mstatus})
                        paid = self.q7Edit.text()        # date
                        logger.debug("saveModified(self=%s,mstatus=%s): paid → %s", self, mstatus, paid, extra={"event.action": "saveModified", "logrite.mstatus": mstatus})
                        logger.debug("saveModified(mstatus=%s): paid → %s", mstatus, paid, extra={"event.action": "saveModified", "logrite.mstatus": mstatus})
                        if len(paid) == 10:
                            mstatus = 5
                        closed = self.q2Edit.text()      # date
                        if len(closed) == 10:
                            mstatus = 6
                        invoice = round(float(self.q5Edit.text()), 2)
                        logger.debug("saveModified(mstatus=%s): invoice → %s", mstatus, invoice, extra={"event.action": "saveModified", "logrite.mstatus": mstatus})
                        logger.debug("saveModified(self=%s,mstatus=%s): invoice → %s", self, mstatus, invoice, extra={"event.action": "saveModified", "logrite.mstatus": mstatus})

                        if not((len(start) == 0 or len(start) == 10) and (len(finish) == 0 or len(finish) == 10) and (len(approved) == 0\
                              or len(approved) == 10) and  (len(paid) == 0 or len(approved) == 10) and (len(closed) == 0 or len(closed) == 10)):
                            foutInvoer()
                            return
                        else:
                            logger.debug("<<< Exiting saveModified(mstatus=%s)", mstatus, extra={"event.action": "saveModified", "logrite.mstatus": mstatus})
                            logger.debug("saveModified(self=%s,mstatus=%s): q5Edit → %s", self, mstatus, q5Edit, extra={"event.action": "saveModified", "logrite.mstatus": mstatus})
                            self.q5Edit.setText('0')
                            selval = select([orders_inkoop]).where(orders_inkoop.c.orderinkoopID == ordernr)
                            rpval = con.execute(selval).first()
                            logger.debug("saveModified(self=%s,mstatus=%s): rpval → %s", self, mstatus, rpval, extra={"event.action": "saveModified", "logrite.mstatus": mstatus})
                            logger.debug("saveModified(self=%s,mstatus=%s): q10Edit → %s", self, mstatus, q10Edit, extra={"event.action": "saveModified", "logrite.mstatus": mstatus})
                            self.q10Edit.setText(str(float(round(rpval[7]+invoice, 2))))
                            grid.addWidget(self.q10Edit, 17, 3)
                            wijzigOK(ordernr)

                        updmatord = update(orders_inkoop_materieel).where(orders_inkoop_materieel.c.orderinkoopID == ordernr)\
                        .values(werk_start = start, werk_gereed = finish, status = mstatus)
                        con.execute(updmatord)
                        updord = update(orders_inkoop).where(orders_inkoop.c.orderinkoopID == ordernr)\
                            .values(goedgekeurd = approved, betaald = paid, afgemeld = closed,\
                            betaald_bedrag = orders_inkoop.c.betaald_bedrag + invoice, status = mstatus)
                        con.execute(updord)
                        updcal = update(calculaties).where(calculaties.c.koppelnummer == mwerknr).values(verwerkt = mstatus)
                        con.execute(updcal)

            window = Widget()
            window.exec_()

    win = Widget(data_list, header)
    win.exec_()