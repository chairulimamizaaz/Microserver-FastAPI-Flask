from flask import Flask, request, jsonify
import psycopg2
import psycopg2.extras

app = Flask(__name__)

def get_db():
    return psycopg2.connect(
        dbname="mydatabase",
        user="user",
        password="password",
        host="postgres"
    )

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db()
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute("SELECT id, email, name FROM users;")
            users = cur.fetchall()
            users_list = [dict(user) for user in users]
        return jsonify(users_list)
    finally:
        conn.close()

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    conn = get_db()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE users SET email=%s, name=%s, password=%s WHERE id=%s RETURNING id;",
                (data['email'], data['name'], data['password'], user_id)
            )
            if cur.fetchone():
                conn.commit()
                return jsonify({"success": True}), 200
            else:
                return jsonify({"error": "User not found"}), 404
    except psycopg2.DatabaseError as e:
        conn.rollback()
        return jsonify({"error": "Database error", "errorMsg": str(e)}), 500
    finally:
        conn.close()

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    conn = get_db()
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM users WHERE id=%s RETURNING id;", (user_id,))
            if cur.fetchone():
                conn.commit()
                return jsonify({"success": True}), 200
            else:
                return jsonify({"error": "User not found"}), 404
    except psycopg2.DatabaseError as e:
        conn.rollback()
        return jsonify({"error": "Database error", "errorMsg": str(e)}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
