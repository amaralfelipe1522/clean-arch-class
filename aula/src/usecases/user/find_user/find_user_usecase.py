from domain.user.user_repository_interface import UserRepositoryInterface
from domain.__seedwork.use_case_interface import UseCaseInterface
from usecases.user.find_user.find_user_dto import FindUserInputDto, FindUserOutputDto

class FindUserUseCase(UseCaseInterface):
    user_repository: UserRepositoryInterface

    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def execute(self, input: FindUserInputDto) -> FindUserOutputDto:
        user = self.user_repository.find_user(user_id=input.id)
        print('Usuário encontrado: ', user)

        return FindUserOutputDto(id = user.id, name = user.name)
