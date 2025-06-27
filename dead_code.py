# Fichier avec Vulnérabilités Dormantes/Latentes pour Test de Détection
# ⚠️ ATTENTION: Ce fichier contient des vulnérabilités non activées pour des fins de test uniquement

import os
import subprocess
import sqlite3
import pickle
import yaml
import json
import base64
import hashlib
import socket
import urllib.request
import xml.etree.ElementTree as ET
from flask import Flask, request
import requests
import paramiko
import ftplib
import telnetlib

# Vulnérabilité 1: Fonction d'injection SQL définie mais non appelée
def vulnerable_sql_injection(username):
    """Fonction avec injection SQL - non appelée"""
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Vulnérabilité: Injection SQL directe
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    user = cursor.fetchone()
    conn.close()
    return user

# Vulnérabilité 2: Fonction d'injection de commande définie mais non utilisée
def vulnerable_command_injection(command):
    """Fonction avec injection de commande - non appelée"""
    # Vulnérabilité: Injection de commande
    result = subprocess.check_output(command, shell=True)
    return result.decode()

# Vulnérabilité 3: Fonction de path traversal définie mais inactive
def vulnerable_path_traversal(filename):
    """Fonction avec path traversal - non appelée"""
    # Vulnérabilité: Path traversal possible
    file_path = f"/var/www/files/{filename}"
    with open(file_path, 'r') as f:
        content = f.read()
    return content

# Vulnérabilité 4: Fonction XXE définie mais non utilisée
def vulnerable_xxe(xml_data):
    """Fonction avec XXE - non appelée"""
    # Vulnérabilité: XXE possible
    root = ET.fromstring(xml_data)
    return root.text

# Vulnérabilité 5: Fonction de deserialization dangereuse définie mais inactive
def vulnerable_deserialization(data):
    """Fonction avec deserialization dangereuse - non appelée"""
    # Vulnérabilité: Deserialization pickle dangereuse
    obj = pickle.loads(data)
    return obj

# Vulnérabilité 6: Fonction YAML unsafe load définie mais non utilisée
def vulnerable_yaml_load(yaml_data):
    """Fonction avec YAML unsafe load - non appelée"""
    # Vulnérabilité: YAML unsafe load
    data = yaml.load(yaml_data, Loader=yaml.Loader)
    return data

# Vulnérabilité 7: Fonction de hachage faible définie mais inactive
def vulnerable_hash(password):
    """Fonction avec hachage MD5 faible - non appelée"""
    # Vulnérabilité: Hachage MD5 faible
    hashed = hashlib.md5(password.encode()).hexdigest()
    return hashed

# Vulnérabilité 8: Fonction de génération de clé faible définie mais non utilisée
def vulnerable_key_generation():
    """Fonction avec génération de clé faible - non appelée"""
    # Vulnérabilité: Clé faible
    import random
    key = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    return key

# Vulnérabilité 9: Fonction de validation d'email absente définie mais inactive
def vulnerable_email_validation(email):
    """Fonction sans validation d'email - non appelée"""
    # Vulnérabilité: Pas de validation d'email
    return email

# Vulnérabilité 10: Fonction de validation d'entrée absente définie mais non utilisée
def vulnerable_input_validation(user_input):
    """Fonction sans validation d'entrée - non appelée"""
    # Vulnérabilité: Pas de validation d'entrée
    return user_input

# Vulnérabilité 11: Fonction de gestion d'erreurs dangereuse définie mais inactive
def vulnerable_error_handling():
    """Fonction avec gestion d'erreurs dangereuse - non appelée"""
    try:
        # Code qui peut échouer
        result = 1 / 0
    except Exception as e:
        # Vulnérabilité: Exposition d'informations sensibles
        print(f"Error: {e}")
        print(f"Stack trace: {e.__traceback__}")
        return str(e)

# Vulnérabilité 12: Fonction de logging d'informations sensibles définie mais non utilisée
def vulnerable_logging(data):
    """Fonction avec logging d'informations sensibles - non appelée"""
    # Vulnérabilité: Logging de données sensibles
    print(f"Processing sensitive data: {data}")
    print(f"Password: {data.get('password')}")
    print(f"Credit card: {data.get('credit_card')}")
    return "logged"

# Vulnérabilité 13: Fonction de stockage de secrets en clair définie mais inactive
def vulnerable_secret_storage(secret):
    """Fonction avec stockage de secrets en clair - non appelée"""
    # Vulnérabilité: Stockage de secrets en clair
    with open('/tmp/secrets.txt', 'w') as f:
        f.write(f"SECRET={secret}")
    return "stored"

# Vulnérabilité 14: Fonction de transmission de données non chiffrées définie mais non utilisée
def vulnerable_data_transmission(data):
    """Fonction avec transmission non chiffrée - non appelée"""
    # Vulnérabilité: Transmission non chiffrée
    url = "http://example.com/api/data"
    response = requests.post(url, data=data)
    return response.text

# Vulnérabilité 15: Fonction de connexion SSH non sécurisée définie mais inactive
def vulnerable_ssh_connection(host, username, password):
    """Fonction avec connexion SSH non sécurisée - non appelée"""
    # Vulnérabilité: Connexion SSH avec mot de passe en clair
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=password)
    return ssh

# Vulnérabilité 16: Fonction de connexion FTP non sécurisée définie mais non utilisée
def vulnerable_ftp_connection(host, username, password):
    """Fonction avec connexion FTP non sécurisée - non appelée"""
    # Vulnérabilité: Connexion FTP non sécurisée
    ftp = ftplib.FTP(host)
    ftp.login(username, password)
    return ftp

# Vulnérabilité 17: Fonction de connexion Telnet définie mais inactive
def vulnerable_telnet_connection(host, username, password):
    """Fonction avec connexion Telnet - non appelée"""
    # Vulnérabilité: Connexion Telnet non sécurisée
    tn = telnetlib.Telnet(host)
    tn.read_until(b"login: ")
    tn.write(username.encode('ascii') + b"\n")
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
    return tn

# Vulnérabilité 18: Fonction de socket non sécurisé définie mais non utilisée
def vulnerable_socket_connection(host, port):
    """Fonction avec socket non sécurisé - non appelée"""
    # Vulnérabilité: Socket non sécurisé
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    return sock

# Vulnérabilité 19: Fonction de requête HTTP non sécurisée définie mais inactive
def vulnerable_http_request(url):
    """Fonction avec requête HTTP non sécurisée - non appelée"""
    # Vulnérabilité: Requête HTTP non sécurisée
    response = urllib.request.urlopen(url)
    return response.read()

# Vulnérabilité 20: Fonction de validation de certificat SSL désactivée définie mais non utilisée
def vulnerable_ssl_connection(url):
    """Fonction avec validation SSL désactivée - non appelée"""
    # Vulnérabilité: Validation SSL désactivée
    import ssl
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    response = urllib.request.urlopen(url, context=context)
    return response.read()

# Vulnérabilité 21: Fonction de génération de token faible définie mais inactive
def vulnerable_token_generation():
    """Fonction avec génération de token faible - non appelée"""
    # Vulnérabilité: Token faible
    import time
    import random
    token = f"{int(time.time())}{random.randint(1000, 9999)}"
    return token

# Vulnérabilité 22: Fonction de validation de session absente définie mais non utilisée
def vulnerable_session_validation(session_id):
    """Fonction sans validation de session - non appelée"""
    # Vulnérabilité: Pas de validation de session
    return session_id

# Vulnérabilité 23: Fonction de validation de token absente définie mais inactive
def vulnerable_token_validation(token):
    """Fonction sans validation de token - non appelée"""
    # Vulnérabilité: Pas de validation de token
    return token

# Vulnérabilité 24: Fonction de validation de signature absente définie mais non utilisée
def vulnerable_signature_validation(signature):
    """Fonction sans validation de signature - non appelée"""
    # Vulnérabilité: Pas de validation de signature
    return signature

# Vulnérabilité 25: Fonction de validation de certificat absente définie mais inactive
def vulnerable_certificate_validation(certificate):
    """Fonction sans validation de certificat - non appelée"""
    # Vulnérabilité: Pas de validation de certificat
    return certificate

# Vulnérabilité 26: Fonction de validation de proxy absente définie mais non utilisée
def vulnerable_proxy_validation(proxy):
    """Fonction sans validation de proxy - non appelée"""
    # Vulnérabilité: Pas de validation de proxy
    return proxy

# Vulnérabilité 27: Fonction de validation de cache absente définie mais inactive
def vulnerable_cache_validation(cache):
    """Fonction sans validation de cache - non appelée"""
    # Vulnérabilité: Pas de validation de cache
    return cache

# Vulnérabilité 28: Fonction de validation de compression absente définie mais non utilisée
def vulnerable_compression_validation(compression):
    """Fonction sans validation de compression - non appelée"""
    # Vulnérabilité: Pas de validation de compression
    return compression

# Vulnérabilité 29: Fonction de validation de redirection absente définie mais inactive
def vulnerable_redirect_validation(redirect_url):
    """Fonction sans validation de redirection - non appelée"""
    # Vulnérabilité: Pas de validation de redirection
    return redirect_url

# Vulnérabilité 30: Fonction de validation de callback absente définie mais non utilisée
def vulnerable_callback_validation(callback_url):
    """Fonction sans validation de callback - non appelée"""
    # Vulnérabilité: Pas de validation de callback
    return callback_url

# Vulnérabilité 31: Fonction de validation de webhook absente définie mais inactive
def vulnerable_webhook_validation(webhook_url):
    """Fonction sans validation de webhook - non appelée"""
    # Vulnérabilité: Pas de validation de webhook
    return webhook_url

# Vulnérabilité 32: Fonction de validation de template absente définie mais non utilisée
def vulnerable_template_validation(template):
    """Fonction sans validation de template - non appelée"""
    # Vulnérabilité: Pas de validation de template
    return template

# Vulnérabilité 33: Fonction de validation de regex dangereuse définie mais inactive
def vulnerable_regex_validation(pattern, text):
    """Fonction avec regex dangereuse - non appelée"""
    # Vulnérabilité: Regex dangereuse (ReDoS)
    import re
    matches = re.findall(pattern, text)
    return matches

# Vulnérabilité 34: Fonction de validation de date absente définie mais non utilisée
def vulnerable_date_validation(date_str):
    """Fonction sans validation de date - non appelée"""
    # Vulnérabilité: Pas de validation de date
    from datetime import datetime
    date = datetime.strptime(date_str, '%Y-%m-%d')
    return date

# Vulnérabilité 35: Fonction de validation de timezone absente définie mais inactive
def vulnerable_timezone_validation(timezone):
    """Fonction sans validation de timezone - non appelée"""
    # Vulnérabilité: Pas de validation de timezone
    return timezone

# Vulnérabilité 36: Fonction de validation de locale absente définie mais non utilisée
def vulnerable_locale_validation(locale):
    """Fonction sans validation de locale - non appelée"""
    # Vulnérabilité: Pas de validation de locale
    return locale

# Vulnérabilité 37: Fonction de validation de longueur absente définie mais inactive
def vulnerable_length_validation(text):
    """Fonction sans validation de longueur - non appelée"""
    # Vulnérabilité: Pas de validation de longueur
    return text

# Vulnérabilité 38: Fonction de validation de type absente définie mais non utilisée
def vulnerable_type_validation(data):
    """Fonction sans validation de type - non appelée"""
    # Vulnérabilité: Pas de validation de type
    return data

# Vulnérabilité 39: Fonction de validation de format absente définie mais inactive
def vulnerable_format_validation(data):
    """Fonction sans validation de format - non appelée"""
    # Vulnérabilité: Pas de validation de format
    return data

# Vulnérabilité 40: Fonction de validation de contenu absente définie mais non utilisée
def vulnerable_content_validation(content):
    """Fonction sans validation de contenu - non appelée"""
    # Vulnérabilité: Pas de validation de contenu
    return content

# Vulnérabilité 41: Fonction de validation de méthode HTTP absente définie mais inactive
def vulnerable_method_validation(method):
    """Fonction sans validation de méthode HTTP - non appelée"""
    # Vulnérabilité: Pas de validation de méthode HTTP
    return method

# Vulnérabilité 42: Fonction de validation d'en-têtes absente définie mais non utilisée
def vulnerable_headers_validation(headers):
    """Fonction sans validation d'en-têtes - non appelée"""
    # Vulnérabilité: Pas de validation d'en-têtes
    return headers

# Vulnérabilité 43: Fonction de validation de cookies absente définie mais inactive
def vulnerable_cookies_validation(cookies):
    """Fonction sans validation de cookies - non appelée"""
    # Vulnérabilité: Pas de validation de cookies
    return cookies

# Vulnérabilité 44: Fonction de validation de paramètres absente définie mais non utilisée
def vulnerable_parameters_validation(params):
    """Fonction sans validation de paramètres - non appelée"""
    # Vulnérabilité: Pas de validation de paramètres
    return params

# Vulnérabilité 45: Fonction de validation de corps de requête absente définie mais inactive
def vulnerable_body_validation(body):
    """Fonction sans validation de corps de requête - non appelée"""
    # Vulnérabilité: Pas de validation de corps de requête
    return body

# Vulnérabilité 46: Fonction de validation de réponse absente définie mais non utilisée
def vulnerable_response_validation(response):
    """Fonction sans validation de réponse - non appelée"""
    # Vulnérabilité: Pas de validation de réponse
    return response

# Vulnérabilité 47: Fonction de validation de statut absente définie mais inactive
def vulnerable_status_validation(status):
    """Fonction sans validation de statut - non appelée"""
    # Vulnérabilité: Pas de validation de statut
    return status

# Vulnérabilité 48: Fonction de validation de code d'erreur absente définie mais non utilisée
def vulnerable_error_code_validation(error_code):
    """Fonction sans validation de code d'erreur - non appelée"""
    # Vulnérabilité: Pas de validation de code d'erreur
    return error_code

# Vulnérabilité 49: Fonction de validation de message d'erreur absente définie mais inactive
def vulnerable_error_message_validation(error_message):
    """Fonction sans validation de message d'erreur - non appelée"""
    # Vulnérabilité: Pas de validation de message d'erreur
    return error_message

# Vulnérabilité 50: Fonction de validation de stack trace absente définie mais non utilisée
def vulnerable_stack_trace_validation(stack_trace):
    """Fonction sans validation de stack trace - non appelée"""
    # Vulnérabilité: Pas de validation de stack trace
    return stack_trace

# Variables avec vulnérabilités dormantes
vulnerable_secret = "admin123"  # Vulnérabilité: Secret en dur - non utilisé
vulnerable_api_key = "sk-1234567890abcdef"  # Vulnérabilité: API key en dur - non utilisée
vulnerable_password = "password123"  # Vulnérabilité: Mot de passe en dur - non utilisé
vulnerable_token = "very_secret_token_123"  # Vulnérabilité: Token en dur - non utilisé

# Classes avec vulnérabilités dormantes
class VulnerableClass:
    """Classe avec vulnérabilités dormantes - non instanciée"""
    
    def __init__(self):
        self.secret = "class_secret_123"  # Vulnérabilité: Secret en dur
    
    def vulnerable_method(self, data):
        """Méthode avec vulnérabilité - non appelée"""
        # Vulnérabilité: Pas de validation d'entrée
        return data
    
    def vulnerable_encryption(self, text):
        """Méthode avec chiffrement faible - non appelée"""
        # Vulnérabilité: Chiffrement faible
        return base64.b64encode(text.encode()).decode()

# Configuration avec vulnérabilités dormantes
vulnerable_config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "user": "admin",
        "password": "admin123"  # Vulnérabilité: Mot de passe en clair - non utilisé
    },
    "api": {
        "key": "sk-1234567890abcdef",  # Vulnérabilité: API key en clair - non utilisée
        "secret": "very_secret_token_123"  # Vulnérabilité: Secret en clair - non utilisé
    },
    "security": {
        "enabled": False,  # Vulnérabilité: Sécurité désactivée - non utilisée
        "auth_required": False  # Vulnérabilité: Auth désactivée - non utilisée
    }
}

# Fonction principale qui n'utilise aucune des vulnérabilités
def main():
    """Fonction principale sans vulnérabilités actives"""
    print("Application démarrée")
    print("Aucune vulnérabilité n'est activement utilisée")
    return "success"

# Point d'entrée
if __name__ == "__main__":
    main()

# Vulnérabilités dormantes incluses dans ce fichier:
# 1. Injection SQL définie mais non appelée
# 2. Injection de commande définie mais non utilisée
# 3. Path traversal défini mais non appelé
# 4. XXE défini mais non utilisé
# 5. Deserialization dangereuse définie mais inactive
# 6. YAML unsafe load défini mais non utilisé
# 7. Hachage MD5 faible défini mais non appelé
# 8. Génération de clé faible définie mais non utilisée
# 9. Validation d'email absente définie mais inactive
# 10. Validation d'entrée absente définie mais non utilisée
# 11. Gestion d'erreurs dangereuse définie mais inactive
# 12. Logging d'informations sensibles défini mais non utilisé
# 13. Stockage de secrets en clair défini mais non appelé
# 14. Transmission de données non chiffrées définie mais non utilisée
# 15. Connexion SSH non sécurisée définie mais inactive
# 16. Connexion FTP non sécurisée définie mais non utilisée
# 17. Connexion Telnet définie mais inactive
# 18. Socket non sécurisé défini mais non appelé
# 19. Requête HTTP non sécurisée définie mais non utilisée
# 20. Validation de certificat SSL désactivée définie mais inactive
# 21. Variables avec secrets en dur non utilisées
# 22. Classe avec vulnérabilités non instanciée
# 23. Configuration avec vulnérabilités non utilisée 
