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

@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    conn = get_db()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO users (email, name, password) VALUES (%s, %s, %s) RETURNING id;",
                (data['email'], data['name'], data['password'])
            )
            user_id = cur.fetchone()[0]
            conn.commit()
            return jsonify({"success": True, "user_id": user_id}), 201
    except psycopg2.DatabaseError as e:
        conn.rollback()
        app.logger.error(f"Database error: {e}")
        return jsonify({"error": "Database error", "errorMsg": str(e)}), 500
    except Exception as e:
        app.logger.error(f"Unexpected error: {e}")
        return jsonify({"error": "Unexpected error", "errorMsg": str(e)}), 500
    finally:
        conn.close()

@app.route('/login', methods=['POST'])
def login_user():
    data = request.json
    email = data.get('email')
    provided_password = data.get('password')

    if not email or not provided_password:
        return jsonify({"error": "Email and password are required"}), 400

    conn = get_db()
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute("SELECT password FROM users WHERE email = %s", (email,))
            result = cur.fetchone()
            if result:
                stored_password = result['password']
                if provided_password == stored_password:
                    return jsonify({"success": True}), 200
                else:
                    return jsonify({"error": "Invalid credentials"}), 401
            else:
                return jsonify({"error": "User not found"}), 404
    except Exception as e:
        app.logger.error(f"Internal Server Error: {e}")
        return jsonify({"error": "Internal Server Error", "errorMsg": str(e)}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
