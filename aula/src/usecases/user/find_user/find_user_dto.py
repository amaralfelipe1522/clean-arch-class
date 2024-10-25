from pydantic import BaseModel # type: ignore
from uuid import UUID

class FindUserInputDto(BaseModel):
    id: UUID

class FindUserOutputDto(BaseModel):
    id: UUID
    name: str