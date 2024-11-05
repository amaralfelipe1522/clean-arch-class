from pydantic import BaseModel # type: ignore
from uuid import UUID

class UpdateUserInputDto(BaseModel):
    id: UUID
    name: str

class UpdateUserOutputDto(BaseModel):
    id: UUID
    name: str