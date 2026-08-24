from login import hoofdMenu
import datetime, os
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from sqlalchemy import (Table, Column, Integer, String, MetaData,\
                        create_engine, Float, select)
import logging
logger = logging.getLogger(__name__)

def jaarweek():
    logger.debug(">>> Entering jaarweek()")
    dt = datetime.datetime.now()
    logger.debug("jaarweek(): dt → %s", dt)
    week = ('0'+str(dt.isocalendar()[1]))[-2:]
    logger.debug("jaarweek(): week → %s", week)
    jaar = str(dt.isocalendar()[0])
    jrwk = jaar+week
    logger.debug("jaarweek(): jrwk → %s", jrwk)
    logger.debug("jaarweek(): jaar → %s", jaar)
    logger.debug("<<< Exiting jaarweek()")
    return(jrwk)
    
def printing():
    logger.debug(">>> Entering printing()")
    msg = QMessageBox()
    logger.debug("printing(): msg → %s", msg)
    msg.setStyleSheet("color: black;  background-color: gainsboro")
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    msg.setIcon(QMessageBox.Information)
    msg.setText('Just a moment printing is started!')
    msg.setWindowTitle('Printing invoices')
    msg.setWindowIcon(QIcon('./images/logos/logo.jpg'))
    logger.debug("<<< Exiting printing()")
    msg.exec_()

def printGeg(m_email, filename):
    logger.debug(">>> Entering printGeg(m_email=%s,filename=%s)", m_email, filename)
    from sys import platform
    msgBox=QMessageBox()
    logger.debug("printGeg(m_email=%s,filename=%s): msgBox → %s", m_email, filename, msgBox)
    msgBox.setStyleSheet("color: black;  background-color: gainsboro")
    msgBox.setWindowIcon(QIcon('./images/logos/logo.jpg')) 
    msgBox.setWindowTitle("Print list to invoice works")
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Would you like to print out the list of external works to be invoiced?");
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
        hoofdMenu(m_email)
    else:
        hoofdMenu(m_email)
        logger.debug("<<< Exiting printGeg(m_email=%s,filename=%s)", m_email, filename)

def maakLijst(m_email):
    logger.debug(">>> Entering maakLijst(m_email=%s)", m_email)
    from sys import platform
    metadata = MetaData()
    logger.debug("maakLijst(m_email=%s): metadata → %s", m_email, metadata)
    werken = Table('werken', metadata,
        Column('werknummerID', Integer(), primary_key=True),
        Column('werkomschrijving', String),
        Column('aanneemsom', Float),
        Column('kosten_materialen', Float),
        Column('kosten_lonen', Float),
        Column('kosten_materieel', Float),
        Column('kosten_leiding', Float),
        Column('kosten_huisv', Float),
        Column('kosten_overig', Float),
        Column('kosten_vervoer', Float),
        Column('meerminderwerk', Float),
        Column('voortgangstatus', String),
        Column('statusweek',  String),
        Column('betaald_bedrag', Float),
        Column('begr_huisv', Float),
        Column('begr_leiding', Float),
        Column('begr_overig', Float),
        Column('kosten_inhuur', Float),
        Column('beton_bvl', Float),
        Column('kabelwerk', Float),
        Column('grondverzet', Float),
        Column('begr_inhuur', Float),
        Column('begr_vervoer', Float),
        Column('begr_beton_bvl', Float),
        Column('begr_kabelwerk', Float),
        Column('begr_grondverzet', Float),
        Column('begr_materieel',Float),
        Column('begr_materialen', Float),
        Column('begr_lonen', Float),
        Column('startweek', String))
        
    engine = create_engine('postgresql+psycopg2://postgres@localhost/bisystem')
    logger.debug("maakLijst(m_email=%s): engine → %s", m_email, engine)
    con = engine.connect()
    logger.debug("maakLijst(m_email=%s): con → %s", m_email, con)
    
    sel = select([werken]).order_by(werken.c.werknummerID)
    logger.debug("maakLijst(m_email=%s): sel → %s", m_email, sel)
    rpwerken = con.execute(sel)
    rgl = 0
    logger.debug("maakLijst(m_email=%s): rpwerken → %s", m_email, rpwerken)
    mblad = 0
    for row in rpwerken:
        logger.debug("maakLijst(m_email=%s): mblad → %s", m_email, mblad)
        msom = row[2]
        logger.debug("maakLijst(m_email=%s): msom → %s", m_email, msom)
        mktotal=row[3]+row[4]+row[5]+row[6]+row[7]+row[8]+row[9]+row[17]\
         +row[18]+row[19]+row[20]
        logger.debug("maakLijst(m_email=%s): mktotal → %s", m_email, mktotal)
        mbetaald = row[13]
        logger.debug("maakLijst(m_email=%s): mbetaald → %s", m_email, mbetaald)
        mvgangst = row[11]
        logger.debug("maakLijst(m_email=%s): mvgangst → %s", m_email, mvgangst)
        mstatwk = row[12]
        logger.debug("maakLijst(m_email=%s): mstatwk → %s", m_email, mstatwk)
        mfact = 0
        logger.debug("maakLijst(m_email=%s): mfact → %s", m_email, mfact)
        mwerknr = row[0]
        logger.debug("maakLijst(m_email=%s): mwerknr → %s", m_email, mwerknr)
        mmeerwerk = float(row[10])
        logger.debug("maakLijst(m_email=%s): mmeerwerk → %s", m_email, mmeerwerk)
        if mvgangst == 'A':
            if mktotal > 0:
                mvgangst = 'B'
                mstatwk = jaarweek()
        elif mvgangst == 'B':      
            if mktotal > msom/3:
                mvgangst = 'C'
                mstatwk = jaarweek()
        elif mvgangst == 'C':
            if mktotal > msom/2:
                mvgangst = 'D'
                mstatwk = jaarweek()
            mfact = msom/3-mbetaald
        elif mvgangst == 'D':
            if mktotal > msom/1.5:
                mvgangst = 'E'
                mstatwk = jaarweek()
        elif mvgangst == 'E':
            if mktotal >= msom:
                mvgangst = 'F'
                mstatwk = jaarweek()
            mfact = msom/1.5-mbetaald
        elif mvgangst == 'F':
            mfact = msom-mbetaald*0.9
        elif mvgangst == 'G':
            mfact = msom+mmeerwerk-mbetaald 
        if mfact > 1:
            if rgl == 0 or rgl%57 == 0:
                mblad += 1
                if platform == 'win32':
                    filename = '.\\forms\\Facturen_Werken\\Billing_works_'+str(datetime.datetime.now())[0:10]+'.txt'
                else:
                    filename = './forms/Facturen_Werken/Billing_works_'+str(datetime.datetime.now())[0:10]+'.txt'
                    logger.debug("maakLijst(m_email=%s): filename → %s", m_email, filename)
                kop =\
            ('Invoices external works Date: '+str(datetime.datetime.now())[0:10]+' Page '+str(mblad)+'\n'+
            "==============================================================================================\n"+
            "Work number     Description     Status   Contr.price still invoicing already payed   More work\n"+
            "==============================================================================================\n")
                if rgl == 0:
                    open(filename, 'w').write(kop)
                elif rgl%57 == 0:
                    open(filename, 'a').write(kop)
                
            gegevens = str(mwerknr)+' '+"{:18s}".format(str(row[1])[0:18])+'  '\
                 +str(mvgangst)+' '+str(mstatwk)+' '+"{:>12.2f}"\
                 .format(msom)+'   '+"{:>12.2f}".format(mfact)+'   '+"{:>12.2f}".format(mbetaald)\
                 +' '+"{:>12.2f}".format(mmeerwerk)
            logger.debug("maakLijst(m_email=%s): gegevens → %s", m_email, gegevens)
            open(filename,'a').write (gegevens+'\n') 
            rgl += 1
    printGeg(m_email, filename)    
    logger.debug("<<< Exiting maakLijst(m_email=%s)", m_email)
        