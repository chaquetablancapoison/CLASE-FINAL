from models.user import User


class UserRepository:
    _users: list[User] = [
        User("Juan", "Santana", 22, "juan.santana@gmail.com"),
        User("Carlos", "Pérez", 18, "carlos.perez@gmail.com"),
        User("María", "Sosa", 32, "maria.sosa@hotmail.com"),
    ]

    def find_all(self) -> list[User]:
        return self._users

    def create_one(self, user: User):
        self._users.append(user)
