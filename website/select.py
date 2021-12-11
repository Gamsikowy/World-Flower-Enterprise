from flask import Blueprint, render_template
from .config import DB_HOST, DB_NAME, DB_USER, DB_PASS
import psycopg2

conn = psycopg2.connect(dbname = DB_NAME, user = DB_USER,
                        password = DB_PASS, host = DB_HOST)

select = Blueprint('select', __name__)

@select.route('/employees')
def sEmployee():
    return render_template('select/sEmployee.html')

@select.route('/client')
def sClient():
    return render_template('select/sClient.html')

@select.route('/equipment')
def sEquipment():
    return render_template('select/sEquipment.html')

@select.route('/sowing')
def sSowing():
    return render_template('select/sSowing.html')

@select.route('/harvest')
def sHarvest():
    return render_template('select/sHarvest.html')

@select.route('/weeding')
def sWeeding():
    return render_template('select/sWeeding.html')

@select.route('/transactions')
def sTransactions():
    return render_template('select/sTransactions.html')

@select.route('/lodging')
def sLodging():
    return render_template('select/sLodging.html')

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
        conn.close()
    print(rows)
    return render_template('select/sFarmland.html', rows = rows)#headings = headings

@select.route('/warehouse')
def sWarehouse():
    return render_template('select/sWarehouse.html')