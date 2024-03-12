from typing import Union
from fastapi import APIRouter, Request, Response, status
from fastapi.responses import JSONResponse
from queries.get_propiedad import get_propiedad
from queries.get_propiedades import get_propiedades

router = APIRouter()



@router.get("/propiedadesAlpes/v1/ping", status_code=200)
def service_alive():
    return JSONResponse(status_code=status.HTTP_200_OK, content="pong")

@router.get("/propiedadesAlpes/v1/get_propiedad/{id_propiedad}", status_code=200)
async def get_info_by_id(request: Request, id_propiedad: str):
    post = await get_propiedad(id_propiedad).execute()
    return post

@router.get("/propiedadesAlpes/v1/get_propiedades/", status_code=200)
async def get_info_by_id(request: Request):
    post = await get_propiedades().execute()
    return post