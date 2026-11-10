from login import hoofdMenu
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QGridLayout, QVBoxLayout, \
    QComboBox, QDialog, QLineEdit, QMessageBox, QTableView
from sqlalchemy import (Table, Column, Integer, Boolean,  Float, String, MetaData, ForeignKey, \
                        create_engine, select, and_)
import logging
logger = logging.getLogger(__name__)

metadata = MetaData()
materieelmutaties = Table('materieelmutaties', metadata,
    Column('mutatieID', Integer(), primary_key=True),
    Column('werknummerID', None, ForeignKey('werken.werknummerID')),
    Column('servicesID', None, ForeignKey('params_services.servicesID')),
    Column('leverancierID', None, ForeignKey('leveranciers.leverancierID')),
    Column('orderinkoopID', None, ForeignKey('orders_inkoop_materieel.orderinkoopID')),
    Column('order_inkoop_materieelID', None, ForeignKey('orders_inkoop_materieel.order_inkoop_materieelID')),
    Column('uren_geboekt', Float),
    Column('boekbedrag', Float),
    Column('boekdatum', String),
    Column('meerwerkstatus', Boolean))
orders_inkoop_materieel = Table('orders_inkoop_materieel', metadata,
    Column('order_inkoop_materieelID', Integer, primary_key=True),
    Column('werknummerID', None, ForeignKey('werken.werknummerID')),
    Column('servicesID', None, ForeignKey('params_services.servicesID')),
    Column('leverancierID', None, ForeignKey('leveranciers.leverancierID')),
    Column('orderinkoopID', None, ForeignKey('orders_inkoop.orderinkoopID')),
    Column('uren_opdracht', Float))
werken = Table('werken', metadata,
    Column('werknummerID', Integer(), primary_key=True),
    Column('werkomschrijving', String(50)))
orders_inkoop = Table('orders_inkoop', metadata,
   Column('orderinkoopID', Integer, primary_key=True),
   Column('leverancierID', None, ForeignKey('leveranciers.leverancierID')))
leveranciers = Table('leveranciers', metadata,
  Column('leverancierID', Integer, primary_key=True),
  Column('bedrijfsnaam', String),
  Column('rechtsvorm', String))
params_services = Table('params_services', metadata,
    Column('servicesID', Integer(), primary_key=True),
    Column('hourly_tariff', Float),
    Column('overhead_factor', Float),
    Column('item', String))

engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
conn = engine.connect()

def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})

def geenRecord():
    logger.warning(">>> Entering geenRecord()", extra={"event.action": "geenRecord"})
    msg = QMessageBox()
    logger.debug("geenRecord(): msg → %s", msg, extra={"event.action": "geenRecord"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Geen gegevens gevonden\nmaak een andere selektie!')
    msg.setWindowTitle('Opvragen services / Materieel')
    logger.debug("<<< Exiting geenRecord()", extra={"event.action": "geenRecord"})
    msg.exec_()

def ongInvoer():
    logger.warning(">>> Entering ongInvoer()", extra={"event.action": "ongInvoer"})
    msg = QMessageBox()
    logger.debug("ongInvoer(): msg → %s", msg, extra={"event.action": "ongInvoer"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Onjuiste gegevens opgegeven\nzoek term!')
    msg.setWindowTitle('Opvragen services / Materieel')
    logger.debug("<<< Exiting ongInvoer()", extra={"event.action": "ongInvoer"})
    msg.exec_()


def mutatieKeuze(m_email):
    logger.warning(">>> Entering mutatieKeuze(m_email=%s)", m_email, extra={"event.action": "mutatieKeuze"})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            self.setWindowTitle("Menu keuze opvragen gevgevens materieel uren verbruik")
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))

            self.setFont(QFont('Arial', 10))

            self.Keuze = QLabel()
            logger.debug("__init__(parent=%s): self.Keuze → %s", parent, self.Keuze, extra={"event.action": "__init__"})
            k0Edit = QComboBox()
            logger.debug("__init__(self=%s,parent=%s): k0Edit → %s", self, parent, k0Edit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): k0Edit → %s", parent, k0Edit, extra={"event.action": "__init__"})
            k0Edit.setFixedWidth(230)
            k0Edit.setFont(QFont("Arial", 10))
            k0Edit.setStyleSheet("color: black;  background-color: #F8F7EE")
            k0Edit.addItem('      Search sort key')
            k0Edit.addItem('1. Alle wijzigingen')
            k0Edit.addItem('2. Op werknummer')
            k0Edit.addItem('3. Op werk omschrijving')
            k0Edit.addItem('4. Op leverancier nummer')
            k0Edit.addItem('5. Op levernacier naam')
            k0Edit.addItem('6. Op inkooporder nummer')
            k0Edit.addItem('7. Op materieel type (1-12)')
            k0Edit.addItem('8. Op boekdatum jjjj(-mm(-dd))')
            k0Edit.activated[str].connect(self.k0Changed)

            self.Zoekterm = QLabel()
            logger.debug("__init__(parent=%s): self.Zoekterm → %s", parent, self.Zoekterm, extra={"event.action": "__init__"})
            zktermEdit = QLineEdit()
            logger.debug("__init__(self=%s,parent=%s): zktermEdit → %s", self, parent, zktermEdit, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): zktermEdit → %s", parent, zktermEdit, extra={"event.action": "__init__"})
            zktermEdit.setFixedWidth(230)
            zktermEdit.setFont(QFont("Arial", 10))
            zktermEdit.textChanged.connect(self.zktermChanged)

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
            grid.addWidget(lbl, 0, 0, 1, 2)

            logo = QLabel()
            logger.debug("__init__(parent=%s): logo → %s", parent, logo, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): logo → %s", self, parent, logo, extra={"event.action": "__init__"})
            pixmap = QPixmap('./images/logos/logo.jpg')
            logo.setPixmap(pixmap)
            grid.addWidget(logo, 0, 1, 1, 1, Qt.AlignRight)

            grid.addWidget(k0Edit, 1, 1)
            lbl1 = QLabel('Zoek term')
            logger.debug("__init__(parent=%s): lbl1 → %s", parent, lbl1, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): lbl1 → %s", self, parent, lbl1, extra={"event.action": "__init__"})
            lbl1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            grid.addWidget(lbl1, 2, 0)
            grid.addWidget(zktermEdit, 2, 1)

            self.setLayout(grid)
            self.setGeometry(500, 300, 150, 150)

            grid.addWidget(QLabel('\u00A9 2017 all rights reserved dj.jansen@casema.nl'), 4, 0, 1, 3, Qt.AlignCenter)

            applyBtn = QPushButton('Zoeken')
            logger.debug("__init__(parent=%s): applyBtn → %s", parent, applyBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): applyBtn → %s", self, parent, applyBtn, extra={"event.action": "__init__"})
            applyBtn.clicked.connect(self.accept)

            grid.addWidget(applyBtn, 3, 1, 1, 1, Qt.AlignRight)
            applyBtn.setFont(QFont("Arial", 10))
            applyBtn.setFixedWidth(100)
            applyBtn.setStyleSheet("color: black;  background-color: gainsboro")

            cancelBtn = QPushButton('Sluiten')
            logger.debug("__init__(parent=%s): cancelBtn → %s", parent, cancelBtn, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): cancelBtn → %s", self, parent, cancelBtn, extra={"event.action": "__init__"})
            cancelBtn.clicked.connect(lambda: windowSluit(self, m_email))

            grid.addWidget(cancelBtn, 3, 1)
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            cancelBtn.setFont(QFont("Arial", 10))
            cancelBtn.setFixedWidth(100)
            cancelBtn.setStyleSheet("color: black;  background-color: gainsboro")

        def k0Changed(self, text):
            logger.warning(">>> Entering k0Changed(text=%s)", text, extra={"event.action": "k0Changed", "logrite.text": text})
            self.Keuze.setText(text)
            logger.debug("<<< Exiting k0Changed(text=%s)", text, extra={"event.action": "k0Changed", "logrite.text": text})

        def zktermChanged(self, text):
            logger.warning(">>> Entering zktermChanged(text=%s)", text, extra={"event.action": "zktermChanged", "logrite.text": text})
            self.Zoekterm.setText(text)
            logger.debug("<<< Exiting zktermChanged(text=%s)", text, extra={"event.action": "zktermChanged", "logrite.text": text})

        def returnk0(self):
            logger.warning(">>> Entering returnk0()", extra={"event.action": "returnk0"})
            logger.debug("<<< Exiting returnk0()", extra={"event.action": "returnk0"})
            return self.Keuze.text()

        def returnzkterm(self):
            logger.warning(">>> Entering returnzkterm()", extra={"event.action": "returnzkterm"})
            logger.debug("<<< Exiting returnzkterm()", extra={"event.action": "returnzkterm"})
            return self.Zoekterm.text()

        @staticmethod
        def getData(parent=None):
            logger.warning(">>> Entering getData(parent=%s)", parent, extra={"event.action": "getData"})
            dialog = Widget(parent)
            logger.debug("getData(parent=%s): dialog → %s", parent, dialog, extra={"event.action": "getData"})
            dialog.exec_()
            logger.debug("<<< Exiting getData(parent=%s)", parent, extra={"event.action": "getData"})
            return [dialog.returnk0(), dialog.returnzkterm()]

    window = Widget()
    data = window.getData()
    if data[0]:
        keuze = int(data[0][0])
    else:
        ongInvoer()
        mutatieKeuze(m_email)
    if data[1]:
        zoekterm = data[1]
    else:
        zoekterm = ''
    toonMutaties(keuze, zoekterm, m_email)

def toonMutaties(keuze, zoekterm, m_email):
    logger.warning(">>> Entering toonMutaties(keuze=%s,zoekterm=%s,m_email=%s)", keuze, zoekterm, m_email, extra={"event.action": "toonMutaties", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
    import validZt
    if keuze == 1:
        sel = select([materieelmutaties, orders_inkoop_materieel, werken, leveranciers]) \
            .where(and_(werken.c.werknummerID == materieelmutaties.c.werknummerID, \
                        leveranciers.c.leverancierID == materieelmutaties.c.leverancierID, \
                        orders_inkoop_materieel.c.orderinkoopID == materieelmutaties.c.orderinkoopID)) \
            .order_by(werken.c.werknummerID)
    elif keuze == 2 and validZt.zt(zoekterm, 8):
        sel = select([materieelmutaties, orders_inkoop_materieel, werken, leveranciers]) \
            .where(and_(werken.c.werknummerID == materieelmutaties.c.werknummerID, \
                        leveranciers.c.leverancierID == materieelmutaties.c.leverancierID, \
                        orders_inkoop_materieel.c.orderinkoopID == materieelmutaties.c.orderinkoopID, \
                        werken.c.werknummerID == int(zoekterm)))
    elif keuze == 3:
        sel = select([materieelmutaties, orders_inkoop_materieel, werken, leveranciers]) \
            .where(and_(werken.c.werknummerID == materieelmutaties.c.werknummerID, \
                        leveranciers.c.leverancierID == materieelmutaties.c.leverancierID, \
                        orders_inkoop_materieel.c.orderinkoopID == materieelmutaties.c.orderinkoopID, \
                        werken.c.werkomschrijving.ilike('%' + zoekterm + '%'))) \
            .order_by(werken.c.werknummerID)
    elif keuze == 4 and validZt.zt(zoekterm, 3):
        sel = select([materieelmutaties, orders_inkoop_materieel, werken, leveranciers]) \
            .where(and_(werken.c.werknummerID == materieelmutaties.c.werknummerID, \
                        leveranciers.c.leverancierID == materieelmutaties.c.leverancierID, \
                        orders_inkoop_materieel.c.orderinkoopID == materieelmutaties.c.orderinkoopID, \
                        leveranciers.c.leverancierID == int(zoekterm)))
    elif keuze == 5:
        sel = select([materieelmutaties, orders_inkoop_materieel, werken, leveranciers]) \
            .where(and_(werken.c.werknummerID == materieelmutaties.c.werknummerID, \
                        leveranciers.c.leverancierID == materieelmutaties.c.leverancierID, \
                        orders_inkoop_materieel.c.orderinkoopID == materieelmutaties.c.orderinkoopID, \
                        leveranciers.c.bedrijfsnaam.ilike('%' + zoekterm + '%')))
    elif keuze == 6 and validZt.zt(zoekterm, 5):
        sel = select([materieelmutaties, orders_inkoop_materieel, werken, leveranciers]) \
            .where(and_(werken.c.werknummerID == materieelmutaties.c.werknummerID, \
                        leveranciers.c.leverancierID == materieelmutaties.c.leverancierID, \
                        orders_inkoop_materieel.c.orderinkoopID == materieelmutaties.c.orderinkoopID, \
                        orders_inkoop.c.orderinkoopID == int(zoekterm)))
    elif keuze == 7 and validZt.zt(zoekterm, 16):
        sel = select([materieelmutaties, orders_inkoop_materieel, werken, leveranciers]) \
            .where(and_(werken.c.werknummerID == materieelmutaties.c.werknummerID, \
                        leveranciers.c.leverancierID == materieelmutaties.c.leverancierID, \
                        orders_inkoop_materieel.c.orderinkoopID == materieelmutaties.c.orderinkoopID, \
                        materieelmutaties.c.servicesID == int(zoekterm))).order_by(materieelmutaties.c.servicesID)
    elif keuze == 8 and validZt.zt(zoekterm, 10):
        sel = select([materieelmutaties, orders_inkoop_materieel, werken, leveranciers]) \
            .where(and_(werken.c.werknummerID == materieelmutaties.c.werknummerID, \
                        leveranciers.c.leverancierID == materieelmutaties.c.leverancierID, \
                        orders_inkoop_materieel.c.orderinkoopID == materieelmutaties.c.orderinkoopID, \
                        materieelmutaties.c.boekdatum.ilike(zoekterm + '%'))).order_by(materieelmutaties.c.boekdatum)
    else:
        ongInvoer()
        mutatieKeuze(m_email)

    try:
        rp = conn.execute(sel)
    except Exception as e:
        logger.debug("toonMutaties(keuze=%s,zoekterm=%s,m_email=%s): rp → %s", keuze, zoekterm, m_email, rp, extra={"event.action": "toonMutaties", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
        geenRecord()
        logger.error("Exception in toonMutaties(keuze=%s,zoekterm=%s,m_email=%s): %s", keuze, zoekterm, m_email, str(e), exc_info=True, extra={"event.action": "toonMutaties", "event.category": "process", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
        mutatieKeuze(m_email)

    class MyWindow(QDialog):
        logger.debug("<<< Exiting toonMutaties(keuze=%s,zoekterm=%s,m_email=%s)", keuze, zoekterm, m_email, extra={"event.action": "toonMutaties", "logrite.keuze": keuze, "logrite.zoekterm": zoekterm})
        def __init__(self, data_list, header, *args):
            logger.warning(">>> Entering __init__(data_list=%s,header=%s)", data_list, header, extra={"event.action": "__init__", "logrite.data_list": data_list})
            QWidget.__init__(self, *args, )
            self.setGeometry(10, 50, 1900, 900)
            self.setWindowTitle('Opvragen materieel mutaties')
            self.setWindowIcon(QIcon('./images/logos/logo.jpg'))
            self.setWindowFlags(self.windowFlags() | Qt.WindowSystemMenuHint |
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
            table_view.setColumnHidden(1, True)
            table_view.setColumnHidden(5, True)
            table_view.setColumnHidden(10, True)
            table_view.setColumnHidden(11, True)
            table_view.setColumnHidden(12, True)
            table_view.setColumnHidden(13, True)
            table_view.setColumnHidden(14, True)
            #table_view.clicked.connect(showAccount)
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

    eqlist = ['','Sleuvengraver','Persmachine','Atlas kraan','Kraan groot','Mainliner','Hormachine',\
             'Wagon','Locomotor','Locomotief','Montagewagen','Stormobiel','Robeltrein']

    header = ['MutatieID', '', 'MaterieelID', 'Materieelnaam', 'InkooporderID', '','Geboekte uren',\
              'Bedrag geboekt', 'Boekdatum', 'Meer/minder werk','', '','', '', '', 'Uren opdracht',\
              'Werk nummer', 'Werkomschrijving', 'LeverancierID', 'Bedrijfsnaam', 'Rechtsvorm']

    data_list = []
    for row in rp:
        data_list += [(row[0],row[1],row[2],eqlist[row[2]],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],\
                       row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20])]

    win = MyWindow(data_list, header)
    win.exec_()

    mutatieKeuze(m_email)
