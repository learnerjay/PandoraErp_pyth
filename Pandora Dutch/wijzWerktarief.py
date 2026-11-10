from login import hoofdMenu
import  datetime
from PyQt5.QtWidgets import QMessageBox, QDialog
from PyQt5.QtGui import QIcon
from sqlalchemy import (Table, Column, Integer, String, Float, Boolean,\
                        MetaData, create_engine, ForeignKey, select, update)
import logging
logger = logging.getLogger(__name__)

def windowSluit(self, m_email):
    logger.warning(">>> Entering windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})
    self.close()
    hoofdMenu(m_email)
    logger.debug("<<< Exiting windowSluit(m_email=%s)", m_email, extra={"event.action": "windowSluit"})

def invoerOK():
    logger.warning(">>> Entering invoerOK()", extra={"event.action": "invoerOK"})
    msg = QMessageBox()
    logger.debug("invoerOK(): msg → %s", msg, extra={"event.action": "invoerOK"})
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Information)
    msg.setText('Wijzigen van verkoop_uurtarieven gelukt!')
    msg.setWindowTitle('UURTARIEVEN')
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    logger.debug("<<< Exiting invoerOK()", extra={"event.action": "invoerOK"})
    msg.exec_()
      
def winKeuze(m_email):
    logger.warning(">>> Entering winKeuze(m_email=%s)", m_email, extra={"event.action": "winKeuze"})
    class Widget(QDialog):
        def __init__(self, parent=None):
            super(Widget, self).__init__(parent)
            logger.warning(">>> Entering __init__(parent=%s)", parent, extra={"event.action": "__init__"})
            msg = QMessageBox.question(self, 'Verkoop-uurtarieven aanpassen',\
             "Verkoop-uurtarieven aanpassen?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if msg == QMessageBox.No:
                windowSluit(self, m_email)
                winKeuze(m_email)
            metadata = MetaData()
            logger.debug("__init__(parent=%s): metadata → %s", parent, metadata, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): metadata → %s", self, parent, metadata, extra={"event.action": "__init__"})
            params_hours = Table('params_hours', metadata,
                 Column('rateID', Integer(), primary_key=True),
                 Column('item', String),
                 Column('hourly_tariff', Float),
                 Column('wageID', None, ForeignKey('lonen.loonID')),
                 Column('travel_time', Float),
                 Column('overhead_factor', Float),
                 Column('date', String))
            logger.debug("__init__(parent=%s): selpar → %s", parent, selpar, extra={"event.action": "__init__"})
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
            logger.debug("__init__(parent=%s): engine → %s", parent, engine, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): engine → %s", self, parent, engine, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): rppar → %s", parent, rppar, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): rppar → %s", self, parent, rppar, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): mboekd → %s", parent, mboekd, extra={"event.action": "__init__"})
            logger.debug("__init__(self=%s,parent=%s): mboekd → %s", self, parent, mboekd, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): updpar → %s", parent, updpar, extra={"event.action": "__init__"})
            con = engine.connect()
            logger.debug("__init__(self=%s,parent=%s): con → %s", self, parent, con, extra={"event.action": "__init__"})
            logger.debug("__init__(parent=%s): con → %s", parent, con, extra={"event.action": "__init__"})
            selpar = select([params_hours, lonen]).where(params_hours.c.rateID == lonen.c.loonID).order_by(
                lonen.c.loonID)
            rppar = con.execute(selpar)
            mboekd = str(datetime.datetime.now())[0:10]
            for row in rppar:
                updpar = update(params_hours).where(params_hours.c.rateID == row[3]).values(
                    hourly_tariff=row[8] * row[5], date=mboekd, travel_time=row[8] / 3)
                con.execute(updpar)
                updlon = update(lonen).where(lonen.c.loonID == row[7]).values(werkuur=row[2])
                logger.debug("__init__(parent=%s): updlon → %s", parent, updlon, extra={"event.action": "__init__"})
                con.execute(updlon)
                updlon = update(lonen).where(lonen.c.loonID == row[7] - 1).values(werkuur=row[2])
                con.execute(updlon)
                updlon = update(lonen).where(lonen.c.loonID == row[7] - 2).values(werkuur=row[2])
                con.execute(updlon)
                if row[0] < 37:
                    updlon = update(lonen).where(lonen.c.loonID == row[7] - 3).values(werkuur=row[2])
                    con.execute(updlon)
            invoerOK()
            windowSluit(self, m_email)
            logger.debug("<<< Exiting __init__(parent=%s)", parent, extra={"event.action": "__init__"})

    window = Widget()
    window.show()
