from pydantic import BaseModel # type: ignore
from uuid import UUID

class AddUserInputDto(BaseModel): # BaseModel valida a tipagem do input
    name: str

class AddUserOutputDto(BaseModel):
    id: UUID
    name: str