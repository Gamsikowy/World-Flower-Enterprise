from flask import Blueprint, render_template, request, flash, redirect
from .config import DB_HOST, DB_NAME, DB_USER, DB_PASS
import psycopg2

conn = psycopg2.connect(dbname = DB_NAME, user = DB_USER,
                        password = DB_PASS, host = DB_HOST)

update = Blueprint('update', __name__)

@update.route('/employee', methods = ['GET', 'PUT'])
def uEmployee():
    if request.method == 'PUT':

        pesel = request.json['pesel']
        name = request.json['name']
        surname = request.json['surname']
        phone = request.json['phone']
        birth = request.json['birth']
        salary = request.json['salary']
        role = request.json['role']
        lodgingAddress = request.json['lodgingAddress']
        
        cur = conn.cursor()
        try:
            record = (name, surname, phone, birth, salary, role, lodgingAddress, pesel)
           
            indices = [i for i, x in enumerate(record) if x == '' or x == None]
           
            if indices:
                insertQuery = "select name, surname, phone_number, birth_date, salary, role, lodging_address from person where pesel = %s;"
                cur.execute(insertQuery, (pesel,))
                result = cur.fetchone()
                
                record = list(record)
                
                for i in indices:
                    record[i] = result[i]

                record = tuple(record)
                
                insertQuery = "update person set (name, surname, phone_number, birth_date, salary, role, lodging_address) = (%s, %s, %s, %s, %s, %s, %s) where pesel = %s;"
                cur.execute(insertQuery, record)
                conn.commit()
            else:
                insertQuery = "update person set (name, surname, phone_number, birth_date, salary, role, lodging_address) = (%s, %s, %s, %s, %s, %s, %s) where id = %s;"
                record = (name, surname, phone, birth, salary, role, lodgingAddress, pesel)
                cur.execute(insertQuery, record)
                conn.commit()

            print("Employee modified")
            flash("Employee modified", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()
    return render_template('update/uEmployee.html')

@update.route('/warehouse', methods = ['GET', 'PUT'])
def uWarehouse():
    if request.method == 'PUT':
        address = request.json['address']
        flower_quantity = request.json['flowerQuantity']
        seed_quantity = request.json['seedQuantity']
        flower_price = request.json['flowerPrice']
        seed_price = request.json['seedPrice']
            
        cur = conn.cursor()
        try:
            insertQuery = "update warehouse set (flower_quantity, seed_quantity, flower_price, seed_price) = (%s, %s, %s, %s) where address = %s;"
            record = (flower_quantity, seed_quantity, flower_price, seed_price, address)
            cur.execute(insertQuery, record)
            conn.commit()
            print("Warehouse updated")
            flash("Warehouse updated", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()

    return render_template('update/uWarehouse.html')

@update.route('/lodging', methods = ['GET', 'PUT'])
def uLodging():
    if request.method == 'PUT':
        address = request.json['address']
        apartments = request.json['apartments']
            
        cur = conn.cursor()
        try:
            insertQuery = "update lodging set apartments = %s where address = %s;"
            record = (apartments, address)
            cur.execute(insertQuery, record)
            conn.commit()
            print("Lodging updated")
            flash("Lodging updated", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()
    
    return render_template('update/uLodging.html')

@update.route('/farmland', methods = ['GET', 'PUT'])
def uFarmland():
    if request.method == 'PUT':
        address = request.json['address']
        area = request.json['area']
            
        cur = conn.cursor()
        try:
            insertQuery = "update farmland set area = (%s) where address = %s;"
            record = (area, address)
            cur.execute(insertQuery, record)
            conn.commit()
            print("Farmland updated")
            flash("Farmland updated", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()

    return render_template('update/uLodging.html')

@update.route('/client', methods = ['GET', 'PUT'])
def uClient():
    if request.method == 'PUT':

        pesel = request.json['pesel']
        name = request.json['name']
        surname = request.json['surname']
        company = request.json['company']
        
        try:
            cur = conn.cursor()
            record = (name, surname, company, pesel)
            
            indices = [i for i, x in enumerate(record) if x == '']

            if indices:
                insertQuery = "select name, surname, company from client where pesel = %s;"
                cur.execute(insertQuery, (pesel,))
                result = cur.fetchone()
                
                record = list(record)
                print(record)
                
                for i in indices:
                    record[i] = result[i]

                record = tuple(record)

                insertQuery = "update client set (name, surname, company) = (%s, %s, %s) where pesel = %s;"
                cur.execute(insertQuery, record)
                conn.commit()
            else:
                insertQuery = "update client set (name, surname, company) = (%s, %s, %s) where pesel = %s;"
                record = (name, surname, company, pesel)
                cur.execute(insertQuery, record)
                conn.commit()

            print("Client modified")
            flash("Client modified", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()

    return render_template('update/uClient.html')

@update.route('/equipment', methods = ['GET', 'PUT'])
def uEquipment():
    if request.method == 'PUT':

        id = request.json['id']
        name = request.json['name']
        model = request.json['model']
        warrantyValidity = request.json['warranty_validity']
        
        cur = conn.cursor()
        try:
            record = (name, model, warrantyValidity, id)
            
            indices = [i for i, x in enumerate(record) if x == '']
            
            if indices:
                insertQuery = "select name, model, warranty_validity from equipment where id = %s;"
                cur.execute(insertQuery, (id,))
                result = cur.fetchone()
                
                record = list(record)
                
                for i in indices:
                    record[i] = result[i]

                record = tuple(record)

                insertQuery = "update equipment set (name, model, warranty_validity) = (%s, %s, %s) where id = %s;"
                cur.execute(insertQuery, record)
                conn.commit()
            else:
                insertQuery = "update equipment set (name, model, warranty_validity) = (%s, %s, %s) where id = %s;"
                record = (name, model, warrantyValidity, id)
                cur.execute(insertQuery, record)
                conn.commit()

            print("Equipment modified")
            flash("Equipment modified", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()

    return render_template('update/uEquipment.html')

@update.route('/transaction', methods = ['GET', 'PUT'])
def uTransaction():
    if request.method == 'PUT':
        id = request.json['id']
        flower_quantity = request.json['flower_quantity']
        seed_quantity = request.json['seed_quantity']
        payment = request.json['payment']
        date_of_transaction = request.json['date_of_transaction']
        client_pesel = request.json['client_pesel']
        warehouse_address = request.json['warehouse_address']
        person_pesel = request.json['person_pesel']
            
        cur = conn.cursor()
        try:
            record = (flower_quantity, seed_quantity, payment, date_of_transaction, client_pesel, warehouse_address, person_pesel, id)
            
            indices = [i for i, x in enumerate(record) if x == '']
            print(indices)
            
            if indices:
                insertQuery = "select flower_quantity, seed_quantity, payment, date_of_transaction, client_pesel, warehouse_address, person_pesel from transaction where id = %s;"
                cur.execute(insertQuery, (id,))
                result = cur.fetchone()
                
                record = list(record)
                
                for i in indices:
                    print(result)
                    record[i] = result[i]

                record = tuple(record)

                insertQuery = "update transaction set (flower_quantity, seed_quantity, payment, date_of_transaction, client_pesel, warehouse_address, person_pesel) = (%s, %s, %s, %s, %s, %s, %s) where id = %s;"
                cur.execute(insertQuery, record)
                conn.commit()
            else:
                insertQuery = "update transaction set (flower_quantity, seed_quantity, payment, date_of_transaction, client_pesel, warehouse_address, person_pesel) = (%s, %s, %s, %s, %s, %s, %s) where id = %s;"
                record = (flower_quantity, seed_quantity, payment, date_of_transaction, client_pesel, warehouse_address, person_pesel, id)
                cur.execute(insertQuery, record)
                conn.commit()
            
            print("Transaction updated")
            flash("Transaction updated", category = 'success')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            flash("The operation could not be performed successfully", category = 'error')
        finally:
            cur.close()

    return render_template('update/uTransaction.html')