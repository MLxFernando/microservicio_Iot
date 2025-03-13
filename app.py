import random
import time
import requests
from flask import Flask

app = Flask(__name__)

# Simulamos la lectura de glucosa
def get_glucose_level():
    return random.randint(50, 300)  # Generamos un nivel de glucosa entre 50 y 300 mg/dl

@app.route('/simulate-glucose', methods=['GET'])
def simulate_glucose():
    glucose_level = get_glucose_level()
    print(f"Glucosa simulada: {glucose_level} mg/dl")

    # Enviar los datos de glucosa al microservicio de Alertas
    alert_url = "http://alert-service:5002/alert"
    data = {'glucose_level': glucose_level}
    response = requests.post(alert_url, json=data)
    
    return f"Nivel de glucosa simulado: {glucose_level} mg/dl", 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
