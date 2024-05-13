from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    dbname="mydatabase",
    user="user",
    password="password",
    host="postgres"
)

# @app.route('/receive', methods=['POST'])
@app.route('/receive', methods=['POST'])
def receive_data():
    try:
        data = request.json
        with conn.cursor() as cur:
            cur.execute("INSERT INTO data_table (data_column) VALUES (%s)", [str(data)])
            conn.commit()
        return jsonify({"success": True}), 200
    except psycopg2.DatabaseError as e:
        conn.rollback()  # Rollback to clear any failed transaction blocks
        app.logger.error(f"Database error: {e}")
        return jsonify({"error": "Database error", "errorMsg": str(e)}), 500
    except Exception as e:
        app.logger.error(f"Unexpected error: {e}")
        return jsonify({"error": "Unexpected error", "errorMsg": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001) 
# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route('/receive', methods=['POST'])
# def receive_data():
#     data = request.json
#     print("Data received:", data)
#     return jsonify({"status": "Data received", "yourData": data})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5001) 
