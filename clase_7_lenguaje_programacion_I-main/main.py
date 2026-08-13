from repositories.user_repository import UserRepository
from services.user_service import UserService
from ui.app_window import AppWindow

def main():
    repository = UserRepository()
    service = UserService(repository)

    app_window = AppWindow(service)

    app_window.mainloop()


if __name__ == "__main__":
    main()
