import requests

try:
	r=requests.get('http://172.31.112.199/laboratorio/alta.php',timeout=1)
	print(r.ok)
	print(r.status_code)
#	print(r.raise_for_status())
except:
	print('error de coneccion')
"""except requests.exceptions.ConnectTimeout:
	print('no se conecta jajaja')
except requests.exceptions.HTTPError:
	print('Url no esta')
"""

try:
	u=requests.post('http://172.31.112.199/laboratorio/alta.php',data={'var1' :"SIE"},timeout=1)
	print(u.ok)
	print(u.status_code)
except:
	print('error de conexin 2')





print('End of file')
