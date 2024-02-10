from infrastructure.shared_code.entities.user import User


class UserService():

    def create(params: dict):
        user = User(**params)
        user.update_fields()
        user.save()

    # get user info
    def get():
        print("test user")
