from typing import List

from fastapi import APIRouter
from newsletter.schemas.inscrito import InscritoIN, InscritoOUT
from newsletter.db.db_services import atualizar_inscrito_db, gravar_inscrito_db, get_inscritos_db, get_inscrito_db, delete_inscrito_db


router = APIRouter()

@router.get("/")
def root_path():
  return 'Hello'


@router.get("/inscritos", response_model=List[InscritoOUT], tags=["inscritos"])
def get_inscritos():
  '''pegar todos os inscritos.'''
  return get_inscritos_db()


@router.get('/inscritos/{id}', response_model=InscritoOUT, tags=["inscritos"])
def get_inscrito(id: int):
  '''pegar inscrito pelo id.'''
  user = get_inscrito_db(id)
  return user


@router.post("/inscritos", response_model=InscritoOUT, tags=["inscritos"])
def registrar_inscrito(body: InscritoIN):
  '''registrar um novo inscrito.'''
  id_db = gravar_inscrito_db(body.nome, body.email)
  return InscritoOUT(id=id_db, nome=body.nome, email=body.email)


@router.put("/inscritos/{id}", response_model=InscritoOUT, tags=["inscritos"])
def atualizar_inscrito(id: int, update:InscritoIN):
  updated_user = atualizar_inscrito_db(id, update.nome, update.email)
  return updated_user


@router.delete("/inscritos/{id}", tags=["inscritos"])
def delete_inscrito(id: int):
  return delete_inscrito_db(id)