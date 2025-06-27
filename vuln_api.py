# API avec Vulnérabilités Intentionnelles pour Test de Détection
# ⚠️ ATTENTION: Ce fichier contient des vulnérabilités de sécurité pour des fins de test uniquement

from flask import Flask, request, jsonify, session
from flask_cors import CORS
import sqlite3
import json
import hashlib
import base64
import os
import subprocess
import pickle
import yaml
import xml.etree.ElementTree as ET
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "very_secret_key_123"  # Vulnérabilité 1: Clé secrète en dur
CORS(app)  # Vulnérabilité 2: CORS activé pour tous les domaines

# Vulnérabilité 3: Base de données avec injection SQL possible
def init_db():
    conn = sqlite3.connect('vulnerable.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT,
            email TEXT,
            role TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY,
            title TEXT,
            content TEXT,
            author_id INTEGER,
            is_public BOOLEAN
        )
    ''')
    conn.commit()
    conn.close()

# Vulnérabilité 4: Injection SQL - Pas de paramètres préparés
@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    conn = sqlite3.connect('vulnerable.db')
    cursor = conn.cursor()
    # Vulnérabilité: Injection SQL directe
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    user = cursor.fetchone()
    conn.close()
    return jsonify(user)

# Vulnérabilité 5: Injection SQL dans authentification
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    conn = sqlite3.connect('vulnerable.db')
    cursor = conn.cursor()
    # Vulnérabilité: Injection SQL dans la requête
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")
    user = cursor.fetchone()
    conn.close()
    
    if user:
        session['user_id'] = user[0]
        session['role'] = user[4]
        return jsonify({"message": "Login successful"})
    return jsonify({"error": "Invalid credentials"}), 401

# Vulnérabilité 6: Pas de validation d'entrée
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    # Vulnérabilité: Pas de validation des données d'entrée
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    
    conn = sqlite3.connect('vulnerable.db')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO users (username, password, email, role) VALUES ('{username}', '{password}', '{email}', 'user')")
    conn.commit()
    conn.close()
    return jsonify({"message": "User registered"})

# Vulnérabilité 7: Exposition d'informations sensibles
@app.route('/admin/users', methods=['GET'])
def get_all_users():
    # Vulnérabilité: Pas de vérification d'autorisation
    conn = sqlite3.connect('vulnerable.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, password, email, role FROM users")
    users = cursor.fetchall()
    conn.close()
    # Vulnérabilité: Exposition des mots de passe en clair
    return jsonify([{"id": u[0], "username": u[1], "password": u[2], "email": u[3], "role": u[4]} for u in users])

# Vulnérabilité 8: IDOR (Insecure Direct Object Reference)
@app.route('/users/<int:user_id>/profile', methods=['GET'])
def get_user_profile(user_id):
    # Vulnérabilité: Pas de vérification si l'utilisateur peut accéder à ce profil
    conn = sqlite3.connect('vulnerable.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
    user = cursor.fetchone()
    conn.close()
    return jsonify({"id": user[0], "username": user[1], "email": user[3], "role": user[4]})

# Vulnérabilité 9: Command Injection
@app.route('/ping', methods=['POST'])
def ping_host():
    data = request.get_json()
    host = data.get('host')
    # Vulnérabilité: Injection de commande
    result = subprocess.check_output(f"ping -c 1 {host}", shell=True)
    return jsonify({"result": result.decode()})

# Vulnérabilité 10: Path Traversal
@app.route('/file/<filename>', methods=['GET'])
def read_file(filename):
    # Vulnérabilité: Path traversal possible
    file_path = f"/var/www/files/{filename}"
    with open(file_path, 'r') as f:
        content = f.read()
    return jsonify({"content": content})

# Vulnérabilité 11: XXE (XML External Entity)
@app.route('/parse-xml', methods=['POST'])
def parse_xml():
    xml_data = request.data
    # Vulnérabilité: XXE possible
    root = ET.fromstring(xml_data)
    return jsonify({"parsed": root.text})

# Vulnérabilité 12: Deserialization dangereuse
@app.route('/deserialize', methods=['POST'])
def deserialize_data():
    data = request.data
    # Vulnérabilité: Deserialization pickle dangereuse
    obj = pickle.loads(data)
    return jsonify({"deserialized": str(obj)})

# Vulnérabilité 13: YAML unsafe load
@app.route('/parse-yaml', methods=['POST'])
def parse_yaml():
    yaml_data = request.data
    # Vulnérabilité: YAML unsafe load
    data = yaml.load(yaml_data, Loader=yaml.Loader)
    return jsonify({"parsed": data})

# Vulnérabilité 14: JWT sans vérification
@app.route('/verify-token', methods=['POST'])
def verify_token():
    token = request.json.get('token')
    # Vulnérabilité: Pas de vérification de signature JWT
    try:
        payload = base64.b64decode(token.split('.')[1])
        return jsonify({"valid": True, "payload": json.loads(payload)})
    except:
        return jsonify({"valid": False})

# Vulnérabilité 15: Rate Limiting absent
@app.route('/api/endpoint', methods=['GET'])
def api_endpoint():
    # Vulnérabilité: Pas de rate limiting
    return jsonify({"data": "sensitive_data"})

# Vulnérabilité 16: Logging d'informations sensibles
@app.route('/payment', methods=['POST'])
def process_payment():
    data = request.get_json()
    # Vulnérabilité: Logging de données sensibles
    print(f"Processing payment for card: {data.get('card_number')}")
    print(f"CVV: {data.get('cvv')}")
    return jsonify({"status": "success"})

# Vulnérabilité 17: Headers de sécurité manquants
@app.route('/secure', methods=['GET'])
def secure_endpoint():
    response = jsonify({"message": "secure"})
    # Vulnérabilité: Headers de sécurité manquants
    # response.headers['X-Content-Type-Options'] = 'nosniff'
    # response.headers['X-Frame-Options'] = 'DENY'
    # response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

# Vulnérabilité 18: Validation de type absente
@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    # Vulnérabilité: Pas de validation de type
    a = data.get('a')
    b = data.get('b')
    result = a + b  # Peut causer des erreurs si a ou b ne sont pas des nombres
    return jsonify({"result": result})

# Vulnérabilité 19: Gestion d'erreurs qui expose des informations
@app.route('/debug/<int:user_id>', methods=['GET'])
def debug_user(user_id):
    try:
        conn = sqlite3.connect('vulnerable.db')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
        user = cursor.fetchone()
        conn.close()
        if not user:
            # Vulnérabilité: Exposition d'informations sensibles dans les erreurs
            raise Exception(f"User with ID {user_id} not found in database vulnerable.db")
        return jsonify({"user": user})
    except Exception as e:
        # Vulnérabilité: Exposition de stack trace
        return jsonify({"error": str(e)}), 500

# Vulnérabilité 20: Session fixation
@app.route('/set-session', methods=['POST'])
def set_session():
    data = request.get_json()
    # Vulnérabilité: Session fixation possible
    session['user_id'] = data.get('user_id')
    session['role'] = data.get('role')
    return jsonify({"message": "Session set"})

# Vulnérabilité 21: CSRF protection absente
@app.route('/transfer', methods=['POST'])
def transfer_money():
    data = request.get_json()
    # Vulnérabilité: Pas de protection CSRF
    amount = data.get('amount')
    to_account = data.get('to_account')
    return jsonify({"message": f"Transferred {amount} to {to_account}"})

# Vulnérabilité 22: Authentification par défaut faible
@app.route('/admin', methods=['GET'])
def admin_panel():
    # Vulnérabilité: Authentification par défaut
    if session.get('role') == 'admin':
        return jsonify({"admin_data": "sensitive_admin_data"})
    return jsonify({"error": "Unauthorized"}), 401

# Vulnérabilité 23: Hachage de mot de passe faible
@app.route('/weak-hash', methods=['POST'])
def weak_hash_password():
    data = request.get_json()
    password = data.get('password')
    # Vulnérabilité: Hachage MD5 faible
    hashed = hashlib.md5(password.encode()).hexdigest()
    return jsonify({"hashed": hashed})

# Vulnérabilité 24: Exposition de version
@app.route('/version', methods=['GET'])
def get_version():
    # Vulnérabilité: Exposition de version
    return jsonify({
        "version": "1.0.0",
        "framework": "Flask 2.0.1",
        "python": "3.9.0",
        "database": "SQLite 3.35.0"
    })

# Vulnérabilité 25: Pas de validation de taille de fichier
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file"}), 400
    
    file = request.files['file']
    # Vulnérabilité: Pas de validation de taille
    filename = file.filename
    file.save(f"/uploads/{filename}")
    return jsonify({"message": "File uploaded"})

# Vulnérabilité 26: Pas de validation de type de fichier
@app.route('/upload-image', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image"}), 400
    
    image = request.files['image']
    # Vulnérabilité: Pas de validation de type MIME
    filename = image.filename
    image.save(f"/uploads/images/{filename}")
    return jsonify({"message": "Image uploaded"})

# Vulnérabilité 27: Exposition de chemins de fichiers
@app.route('/files', methods=['GET'])
def list_files():
    # Vulnérabilité: Exposition de chemins de fichiers
    files = os.listdir('/var/www/files')
    return jsonify({"files": files})

# Vulnérabilité 28: Pas de validation de longueur
@app.route('/comment', methods=['POST'])
def add_comment():
    data = request.get_json()
    comment = data.get('comment')
    # Vulnérabilité: Pas de validation de longueur
    conn = sqlite3.connect('vulnerable.db')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO posts (title, content) VALUES ('Comment', '{comment}')")
    conn.commit()
    conn.close()
    return jsonify({"message": "Comment added"})

# Vulnérabilité 29: Pas de validation de format d'email
@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.get_json()
    email = data.get('email')
    # Vulnérabilité: Pas de validation d'email
    conn = sqlite3.connect('vulnerable.db')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO users (email) VALUES ('{email}')")
    conn.commit()
    conn.close()
    return jsonify({"message": "Subscribed"})

# Vulnérabilité 30: Pas de validation de paramètres d'URL
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    # Vulnérabilité: Pas de validation des paramètres d'URL
    conn = sqlite3.connect('vulnerable.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM posts WHERE title LIKE '%{query}%'")
    results = cursor.fetchall()
    conn.close()
    return jsonify({"results": results})

# Vulnérabilité 31: Pas de validation de JSON
@app.route('/process-json', methods=['POST'])
def process_json():
    data = request.get_json()
    # Vulnérabilité: Pas de validation de structure JSON
    return jsonify({"processed": data})

# Vulnérabilité 32: Pas de validation de contenu-type
@app.route('/process-data', methods=['POST'])
def process_data():
    # Vulnérabilité: Pas de validation de content-type
    data = request.data
    return jsonify({"received": data.decode()})

# Vulnérabilité 33: Pas de validation de méthode HTTP
@app.route('/resource', methods=['GET', 'POST', 'PUT', 'DELETE'])
def resource():
    # Vulnérabilité: Pas de validation de méthode HTTP
    return jsonify({"method": request.method})

# Vulnérabilité 34: Pas de validation d'en-têtes
@app.route('/api/data', methods=['GET'])
def get_data():
    # Vulnérabilité: Pas de validation d'en-têtes
    user_agent = request.headers.get('User-Agent')
    return jsonify({"user_agent": user_agent})

# Vulnérabilité 35: Pas de validation de cookies
@app.route('/set-cookie', methods=['POST'])
def set_cookie():
    data = request.get_json()
    # Vulnérabilité: Pas de validation de cookies
    response = jsonify({"message": "Cookie set"})
    response.set_cookie('user_data', data.get('data'))
    return response

# Vulnérabilité 36: Pas de validation de session
@app.route('/session-data', methods=['GET'])
def get_session_data():
    # Vulnérabilité: Pas de validation de session
    return jsonify({"session": dict(session)})

# Vulnérabilité 37: Pas de validation de token
@app.route('/validate-token', methods=['POST'])
def validate_token():
    token = request.json.get('token')
    # Vulnérabilité: Pas de validation de token
    return jsonify({"valid": True, "token": token})

# Vulnérabilité 38: Pas de validation de signature
@app.route('/verify-signature', methods=['POST'])
def verify_signature():
    data = request.get_json()
    signature = data.get('signature')
    # Vulnérabilité: Pas de validation de signature
    return jsonify({"verified": True})

# Vulnérabilité 39: Pas de validation de certificat
@app.route('/ssl-info', methods=['GET'])
def get_ssl_info():
    # Vulnérabilité: Pas de validation de certificat SSL
    return jsonify({"ssl_enabled": True})

# Vulnérabilité 40: Pas de validation de proxy
@app.route('/proxy-info', methods=['GET'])
def get_proxy_info():
    # Vulnérabilité: Pas de validation de proxy
    return jsonify({"proxy": request.headers.get('X-Forwarded-For')})

# Vulnérabilité 41: Pas de validation de cache
@app.route('/cached-data', methods=['GET'])
def get_cached_data():
    # Vulnérabilité: Pas de validation de cache
    response = jsonify({"data": "cached_data"})
    response.headers['Cache-Control'] = 'public, max-age=31536000'
    return response

# Vulnérabilité 42: Pas de validation de compression
@app.route('/compressed-data', methods=['GET'])
def get_compressed_data():
    # Vulnérabilité: Pas de validation de compression
    return jsonify({"data": "compressed_data"})

# Vulnérabilité 43: Pas de validation de redirection
@app.route('/redirect', methods=['GET'])
def redirect():
    url = request.args.get('url')
    # Vulnérabilité: Pas de validation de redirection
    return jsonify({"redirect": url})

# Vulnérabilité 44: Pas de validation de callback
@app.route('/callback', methods=['GET'])
def callback():
    callback_url = request.args.get('callback')
    # Vulnérabilité: Pas de validation de callback
    return jsonify({"callback": callback_url})

# Vulnérabilité 45: Pas de validation de webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    webhook_url = request.json.get('webhook_url')
    # Vulnérabilité: Pas de validation de webhook
    return jsonify({"webhook": webhook_url})

# Vulnérabilité 46: Pas de validation de template
@app.route('/template', methods=['POST'])
def process_template():
    template = request.json.get('template')
    # Vulnérabilité: Pas de validation de template
    return jsonify({"template": template})

# Vulnérabilité 47: Pas de validation de regex
@app.route('/regex', methods=['POST'])
def process_regex():
    pattern = request.json.get('pattern')
    text = request.json.get('text')
    # Vulnérabilité: Pas de validation de regex
    import re
    matches = re.findall(pattern, text)
    return jsonify({"matches": matches})

# Vulnérabilité 48: Pas de validation de date
@app.route('/date', methods=['POST'])
def process_date():
    date_str = request.json.get('date')
    # Vulnérabilité: Pas de validation de date
    from datetime import datetime
    date = datetime.strptime(date_str, '%Y-%m-%d')
    return jsonify({"date": date.isoformat()})

# Vulnérabilité 49: Pas de validation de timezone
@app.route('/timezone', methods=['POST'])
def process_timezone():
    timezone = request.json.get('timezone')
    # Vulnérabilité: Pas de validation de timezone
    return jsonify({"timezone": timezone})

# Vulnérabilité 50: Pas de validation de locale
@app.route('/locale', methods=['POST'])
def process_locale():
    locale = request.json.get('locale')
    # Vulnérabilité: Pas de validation de locale
    return jsonify({"locale": locale})

if __name__ == '__main__':
    init_db()
    # Vulnérabilité: Mode debug activé en production
    app.run(debug=True, host='0.0.0.0', port=5000)

# Vulnérabilités d'API incluses dans ce fichier:
# 1. Clé secrète en dur
# 2. CORS activé pour tous les domaines
# 3. Injection SQL sans paramètres préparés
# 4. Pas de validation d'entrée
# 5. Exposition d'informations sensibles
# 6. IDOR (Insecure Direct Object Reference)
# 7. Command Injection
# 8. Path Traversal
# 9. XXE (XML External Entity)
# 10. Deserialization dangereuse (pickle)
# 11. YAML unsafe load
# 12. JWT sans vérification
# 13. Rate Limiting absent
# 14. Logging d'informations sensibles
# 15. Headers de sécurité manquants
# 16. Validation de type absente
# 17. Gestion d'erreurs exposant des informations
# 18. Session fixation
# 19. CSRF protection absente
# 20. Authentification par défaut faible
# 21. Hachage de mot de passe faible (MD5)
# 22. Exposition de version
# 23. Pas de validation de taille de fichier
# 24. Pas de validation de type de fichier
# 25. Exposition de chemins de fichiers
# 26. Pas de validation de longueur
# 27. Pas de validation de format d'email
# 28. Pas de validation de paramètres d'URL
# 29. Pas de validation de JSON
# 30. Pas de validation de contenu-type
# 31. Pas de validation de méthode HTTP
# 32. Pas de validation d'en-têtes
# 33. Pas de validation de cookies
# 34. Pas de validation de session
# 35. Pas de validation de token
# 36. Pas de validation de signature
# 37. Pas de validation de certificat
# 38. Pas de validation de proxy
# 39. Pas de validation de cache
# 40. Pas de validation de compression
# 41. Pas de validation de redirection
# 42. Pas de validation de callback
# 43. Pas de validation de webhook
# 44. Pas de validation de template
# 45. Pas de validation de regex
# 46. Pas de validation de date
# 47. Pas de validation de timezone
# 48. Pas de validation de locale
# 49. Mode debug activé en production
# 50. Exposition de stack trace 
