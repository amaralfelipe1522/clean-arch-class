from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from infrastructure.api.database import get_session
from infrastructure.user.sqlalchemy.user_repository import UserRepository
from usecases.user.add_user.add_user_dto import AddUserInputDto
from usecases.user.add_user.add_user_usecase import AddUserUseCase
from usecases.user.find_user.find_user_dto import FindUserInputDto, FindUserOutputDto
from usecases.user.find_user.find_user_usecase import FindUserUseCase

# Swagger -> http://localhost:8000/docs
router = APIRouter(prefix="/users", tags=["Users"])

# http://localhost:8000/users
@router.post("/")
def add_user(request: AddUserInputDto, session: Session = Depends(get_session)):
    try:
        user_repository = UserRepository(session=session)
        usecase = AddUserUseCase(user_repository=user_repository)
        output = usecase.execute(input=request)

        return output
    
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

# http://localhost:8000/users/{id}
@router.get("/{user_id}")
def find_user(user_id: UUID, session: Session = Depends(get_session)):
    try:
        user_repository = UserRepository(session=session)
        usecase = FindUserUseCase(user_repository=user_repository)
        output = usecase.execute(input=FindUserInputDto(id=user_id))

        return output

    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))