"""Se encarga de gestionar el almacenamiento de los datos en memoria."""

from models.user import User

class UserRepository:
    # Simula mi base de datos
    _users: list[User] = [
        User("Juan", "Santana", 22, "juan.santana@gmail.com"),
        User("Carlos", "Pérez", 18, "carlos.perez@gmail.com"),
        User("María", "Sosa", 32, "maria.sosa@hotmail.com"),
    ]

    def __init__(self) -> None:
        pass

    def find_all(self) -> list[User]:
        """Retorna todos los usuarios registrados."""
        return self._users

    def create_one(self, user: User):
        self._users.append(user)
