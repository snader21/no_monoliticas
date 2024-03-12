from httpx import AsyncClient
from queries.base_command import BaseCommannd
from utils import config
class  get_propiedades(BaseCommannd):
	def  __init__(self):
		pass
            
	async def execute(self):
		async with AsyncClient(base_url=f'{config.propiedades_path}') as client:
			propiedad_request = await client.get('/propiedades/')
			print('urlPeticion', propiedad_request.url)
		if propiedad_request.status_code == 200:
			propiedades = propiedad_request.json()
			return propiedades