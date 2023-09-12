from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db_config = {
    'host': 'praiseordu.mysql.pythonanywhere-services.com',
    'user': 'praiseordu',
    'password': 'Jakehicks123',
    'database': 'praiseordu$persons',
}

# CREATE: Adding a new person
@app.route('/api', methods=['POST'])
def create_person():
    data = request.get_json()
    conn = mysql.connector.connect(**db_config)
    try:
        if 'name' in data:
            cursor = conn.cursor(prepared=True)
            sql = "INSERT INTO persons (name) VALUES (%s)"
            val = (data['name'],)
            cursor.execute(sql, val)
            conn.commit()
            return jsonify({'message': 'Person created successfully'}), 201
        else:
            return jsonify({'error': 'Name is required'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# READ: Fetching details of a person
@app.route('/api/<int:user_id>', methods=['GET'])
def get_person(user_id):
    conn = mysql.connector.connect(**db_config)
    try:
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM persons WHERE id = %s"
        val = (user_id,)
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
@app.route('/api/<int:user_id>', methods=['PUT'])
def update_person(user_id):
    data = request.get_json()
    conn = mysql.connector.connect(**db_config)
    try:
        if 'name' in data:
            cursor = conn.cursor(prepared=True)
            sql = "UPDATE persons SET name = %s WHERE id = %s"
            val = (data['name'], user_id)
            cursor.execute(sql, val)
            conn.commit()
            return jsonify({'message': 'Person updated successfully'}), 200
        else:
            return jsonify({'error': 'Name is required'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# DELETE: Removing a person
@app.route('/api/<int:user_id>', methods=['DELETE'])
def delete_person(user_id):
    conn = mysql.connector.connect(**db_config)
    try:
        cursor = conn.cursor(prepared=True)
        sql = "DELETE FROM persons WHERE id = %s"
        val = (user_id,)
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
