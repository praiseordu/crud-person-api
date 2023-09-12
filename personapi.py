from flask import Flask, request, jsonify
import mysql.connector
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

# MySQL configuration
db_config = {
    'host': 'praiseordu.mysql.pythonanywhere-services.com',
    'user': 'praiseordu',
    'password': 'qwerty@123',
    'database': 'praiseordu$persons',
}

# Dummy user credentials for illustration (replace with your authentication system)
users = {
    'praiseordu': 'password123',
}

@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username

# CREATE: Adding a new person
@app.route('/api', methods=['POST'])
@auth.login_required
def create_person():
    data = request.get_json()
    if 'name' in data and isinstance(data['name'], str) and len(data['name']) > 0:
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor(prepared=True)
            sql = "INSERT INTO persons (name) VALUES (%s)"
            val = (data['name'],)
            cursor.execute(sql, val)
            conn.commit()
            return jsonify({'message': 'Person created successfully'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        finally:
            cursor.close()
            conn.close()
    else:
        return jsonify({'error': 'Invalid or missing "name" field in the request'}), 400

# READ: Fetching details of a person
@app.route('/api/<string:name>', methods=['GET'])
@auth.login_required
def get_person(name):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(prepared=True)
        sql = "SELECT * FROM persons WHERE name = %s"
        val = (name,)
        cursor.execute(sql, val)
        person = cursor.fetchone()
        if person:
            return jsonify(person), 200
        else:
            return jsonify({'error': 'Person not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# UPDATE: Modifying details of an existing person
@app.route('/api/<string:name>', methods=['PUT'])
@auth.login_required
def update_person(name):
    data = request.get_json()
    if 'name' in data and isinstance(data['name'], str) and len(data['name']) > 0:
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor(prepared=True)
            sql = "UPDATE persons SET name = %s WHERE name = %s"
            val = (data['name'], name)
            cursor.execute(sql, val)
            conn.commit()
            return jsonify({'message': 'Person updated successfully'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        finally:
            cursor.close()
            conn.close()
    else:
        return jsonify({'error': 'Invalid or missing "name" field in the request'}), 400

# DELETE: Removing a person
@app.route('/api/<string:name>', methods=['DELETE'])
@auth.login_required
def delete_person(name):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(prepared=True)
        sql = "DELETE FROM persons WHERE name = %s"
        val = (name,)
        cursor.execute(sql, val)
        conn.commit()
        return jsonify({'message': 'Person deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
