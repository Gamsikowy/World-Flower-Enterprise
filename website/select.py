from flask import Blueprint, render_template
from .config import DB_HOST, DB_NAME, DB_USER, DB_PASS
import psycopg2

conn = psycopg2.connect(dbname = DB_NAME, user = DB_USER,
                        password = DB_PASS, host = DB_HOST)

select = Blueprint('select', __name__)

@select.route('/employee')
def sEmployee():

    cur = conn.cursor()
    try:
        insertQuery = "select * from person;"
        cur.execute(insertQuery)
        rows = cur.fetchall()
    except psycopg2.DatabaseError as e:
        print(f'Error {e}')
    finally:
        cur.close()
    return render_template('select/sEmployee.html', rows = rows)

@select.route('/clients')
def sClient():

    cur = conn.cursor()
    try:
        insertQuery = "select * from client;"
        cur.execute(insertQuery)
        rows = cur.fetchall()
    except psycopg2.DatabaseError as e:
        print(f'Error {e}')
    finally:
        cur.close()
    return render_template('select/sClient.html', rows = rows)

@select.route('/equipment')
def sEquipment():

    cur = conn.cursor()
    try:
        insertQuery = "select * from equipment;"
        cur.execute(insertQuery)
        rows = cur.fetchall()
    except psycopg2.DatabaseError as e:
        print(f'Error {e}')
    finally:
        cur.close()
    return render_template('select/sEquipment.html', rows = rows)

@select.route('/sowing')
def sSowing():
    return render_template('select/sSowing.html')

@select.route('/harvest')
def sHarvest():

    cur = conn.cursor()
    try:
        insertQuery = "select * from harvest;"
        cur.execute(insertQuery)
        rows = cur.fetchall()
    except psycopg2.DatabaseError as e:
        print(f'Error {e}')
    finally:
        cur.close()
    return render_template('select/sHarvest.html', rows = rows)

@select.route('/weeding')
def sWeeding():
    return render_template('select/sWeeding.html')

@select.route('/transactions')
def sTransactions():
    return render_template('select/sTransactions.html')

@select.route('/lodging')
def sLodging():

    cur = conn.cursor()
    try:
        insertQuery = "select * from lodging;"
        cur.execute(insertQuery)
        rows = cur.fetchall()
    except psycopg2.DatabaseError as e:
        print(f'Error {e}')
    finally:
        cur.close()
    return render_template('select/sLodging.html', rows = rows)

@select.route('/farmland')
def sFarmland():
    
    cur = conn.cursor()
    try:
        insertQuery = "select * from farmland;"
        cur.execute(insertQuery)
        rows = cur.fetchall()
    except psycopg2.DatabaseError as e:
        print(f'Error {e}')
    finally:
        cur.close()
    
    return render_template('select/sFarmland.html', rows = rows)

@select.route('/warehouse')
def sWarehouse():
    return render_template('select/sWarehouse.html')