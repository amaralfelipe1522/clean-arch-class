from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from infrastructure.api.database import get_session
from infrastructure.user.sqlalchemy.user_repository import UserRepository
from usecases.user.add_user.add_user_dto import AddUserInputDto
from usecases.user.add_user.add_user_usecase import AddUserUseCase
from usecases.user.find_user.find_user_dto import FindUserInputDto
from usecases.user.find_user.find_user_usecase import FindUserUseCase
from usecases.user.list_users.list_users_dto import ListUsersInputDto, ListUsersOutputDto
from usecases.user.list_users.list_users_usecase import ListUserUseCase
from usecases.user.update_user.update_user_dto import UpdateUserInputDto, UpdateUserOutputDto
from usecases.user.update_user.update_user_usecase import UpdateUserUseCase

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
    
# http://localhost:8000/users/
@router.get("/")
def list_users(session: Session = Depends(get_session)):
    try:
        user_repository = UserRepository(session=session)
        usecase = ListUserUseCase(user_repository=user_repository)
        output = usecase.execute(input=ListUsersInputDto())

        return output

    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
# http://localhost:8000/users/{id}
@router.post("/{user_id}")
def update_user(request: UpdateUserInputDto, session: Session = Depends(get_session)):
    try:
        user_repository = UserRepository(session=session)
        usecase = UpdateUserUseCase(user_repository=user_repository)
        output = usecase.execute(input=UpdateUserInputDto(id=request.id, name=request.name))

        return output

    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))