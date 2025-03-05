from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/github-webhook', methods=['POST'])
def webhook():
    try:
        print("🚀 Webhook recibido, actualizando código...")
        
        # Ejecutar git pull para actualizar el código
        subprocess.run(['git', 'pull', 'origin', 'main'], cwd='/home/ubuntu/test1', check=True)

        # Ejecutar script de despliegue
        subprocess.run(['./deploy.sh'], check=True)

        return "✅ Código actualizado y microservicios reiniciados", 200
    except subprocess.CalledProcessError as e:
        return f"❌ Error en el despliegue: {e}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)

