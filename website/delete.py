from flask import Blueprint, render_template, request, flash, jsonify
from .config import DB_HOST, DB_NAME, DB_USER, DB_PASS
import psycopg2

conn = psycopg2.connect(dbname = DB_NAME, user = DB_USER,
                        password = DB_PASS, host = DB_HOST)

delete = Blueprint('delete', __name__)

@delete.route('/employee', methods = ['GET', 'DELETE'])
def dEmployee():

    if request.method == 'DELETE':
        pesel = request.json['pesel']
        
        cur = conn.cursor()
        try:
            insertQuery = "delete from person where pesel = %s;"
            cur.execute(insertQuery, (pesel,))
            conn.commit()

            print("Employee deleted")
            flash("Employee deleted", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()
    return render_template('delete/dEmployee.html')

@delete.route('/client', methods = ['GET', 'DELETE'])
def dClient():
    if request.method == 'DELETE':
        pesel = request.json['pesel']
        
        cur = conn.cursor()
        try:
            insertQuery = "delete from client where pesel = %s;"
            cur.execute(insertQuery, (pesel,))
            conn.commit()

            print("Client deleted")
            flash("Client deleted", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()

    return render_template('delete/dClient.html')

@delete.route('/equipment', methods = ['GET', 'DELETE'])
def dEquipment():

    if request.method == 'DELETE':
        id = request.json['id']
        
        cur = conn.cursor()
        try:
            insertQuery = "delete from equipment where id = %s;"
            cur.execute(insertQuery, (id,))
            conn.commit()

            print("Equipment deleted")
            flash("Equipment deleted", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()
    return render_template('delete/dEquipment.html')

@delete.route('/farmland', methods = ['GET', 'DELETE'])
def dFarmland():

    if request.method == 'DELETE':
        address = request.json['address']
        
        cur = conn.cursor()
        try:
            insertQuery = "delete from farmland where address = %s;"
            cur.execute(insertQuery, (address,))
            conn.commit()

            print("Farmland deleted")
            flash("Farmland deleted", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()
    return render_template('delete/dFarmland.html')

@delete.route('/lodging', methods = ['GET', 'DELETE'])
def dLodging():

    if request.method == 'DELETE':
        address = request.json['address']
        
        cur = conn.cursor()
        try:
            insertQuery = "delete from lodging where address = %s;"
            cur.execute(insertQuery, (address,))
            conn.commit()

            print("Lodging deleted")
            flash("Lodging deleted", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()
    return render_template('delete/dLodging.html')

@delete.route('/warehouse', methods = ['GET', 'DELETE'])
def dWarehouse():

    if request.method == 'DELETE':
        address = request.json['address']
        
        cur = conn.cursor()
        try:
            insertQuery = "delete from warehouse where address = %s;"
            cur.execute(insertQuery, (address,))
            conn.commit()

            print("Warehouse deleted")
            flash("Warehouse deleted", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()
            
    return render_template('delete/dWarehouse.html')

@delete.route('/transaction', methods = ['GET', 'DELETE'])
def dTransaction():

    if request.method == 'DELETE':
        id = request.json['id']

        cur = conn.cursor()
        try:
            insertQuery = "delete from transaction where id = %s;"
            cur.execute(insertQuery, (id,))
            conn.commit()

            print("Transaction deleted")
            flash("Transaction deleted", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()
            
    return render_template('delete/dTransaction.html')