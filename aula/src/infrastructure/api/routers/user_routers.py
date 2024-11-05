from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from infrastructure.api.database import get_session
from usecases.user.add_user.add_user_dto import AddUserInputDto
from usecases.user.add_user.add_user_usecase import AddUserUseCase
from infrastructure.user.sqlalchemy.user_repository import UserRepository

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def add_user(request: AddUserInputDto, session: Session = Depends(get_session)):
    try:
        user_repository = UserRepository(session=session)
        usecase = AddUserUseCase(user_repository=user_repository)
        output = usecase.execute(input=request)

        return output
    
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))