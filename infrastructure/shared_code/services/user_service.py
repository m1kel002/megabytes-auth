from infrastructure.shared_code.entities.user import User


class UserService():

    @classmethod
    def create(params: dict):
        user = User(**params)
        user.update_fields()
        user.save()

    @classmethod
    def get(id: str):
        return User.get(id, 'user')

    @classmethod
    def get_user_by_username(cls, username: str):
        print(f'Querying user by username: {username}')
        users = list(User.usernameIndex.query(username))
        return users[0]

    @classmethod
    def to_simple_response(cls, entity: User):
        return dict(username=entity.username,
                    name=f'{entity.firstName} {entity.lastName}',
                    gender=entity.gender,
                    birthdate=entity.birthdate,
                    email=entity.email)
