from pydantic import BaseModel, Field

class InscritoIN(BaseModel):
  nome:  str = Field(..., description= "nome do inscrito")
  email: str = Field(..., description= "email do inscrito")


class InscritoOUT(BaseModel):
  id:    int = Field(..., description= "id do inscrito")
  nome:  str = Field(..., description= "nome do inscrito")
  email: str = Field(..., description= "email do inscrito")