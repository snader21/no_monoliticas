from httpx import AsyncClient
from queries.base_command import BaseCommannd
from utils import config
class  get_propiedad(BaseCommannd):
	def  __init__(self, id_propiedad):
		self.id_propiedad = id_propiedad
            
	async def execute(self):
		async with AsyncClient(base_url=f'{config.propiedades_path}') as client:
			propiedad_request = await client.get(f'/propiedades/{self.id_propiedad}')
		if propiedad_request.status_code == 200:
			propiedad = propiedad_request.json()
			async with AsyncClient(base_url=f'{config.compania_path}') as client:
				compania_origen_request = await client.get(f'/companias/{propiedad.get("compania_duena")}')
			if compania_origen_request.status_code == 200:
				propiedad["compania_duena"] = compania_origen_request.json()
			async with AsyncClient(base_url=f'{config.compania_path}') as client:
				compania_destino_request = await client.get(f'/companias/{propiedad.get("compania_arrendataria")}')
			if compania_destino_request.status_code == 200:
				propiedad["compania_arrendataria"] = compania_destino_request.json()
				print(compania_destino_request.json())
		return {"data": propiedad}