from fastapi import APIRouter, Body, status, Path
from typing import List

from src.services.user import LaboratoryService
from src.config.constants import LABORATORY_ROUTE
from src.entities.schemas.laboratory import LaboratorySchema

laboratory_router = APIRouter(prefix=LABORATORY_ROUTE)

@laboratory_router.get(
    path='', 
    response_model=List[LaboratorySchema],
    status_code=status.HTTP_200_OK
)
def get_laboratories():
    return LaboratoryService().get_all()

@laboratory_router.post(
    path="",
    response_model=dict,
    status_code=status.HTTP_201_CREATED
)
def create_laboratory(laboratory: LaboratorySchema = Body(...)):
    return LaboratoryService().add_one(laboratory.model_dump())

@laboratory_router.put(
    path="/{id}", 
    response_model=dict,
    status_code=status.HTTP_200_OK
)
def update_laboratory(id: int = Path(...), laboratory: LaboratorySchema = Body(...)):
    return LaboratoryService().update_one(id, laboratory.model_dump())

@laboratory_router.delete(
    path="/{id}",
    response_model=dict, 
    status_code=status.HTTP_200_OK
)
def delete_laboratory(id: int = Path(...)):
    return LaboratoryService().delete_one(id)