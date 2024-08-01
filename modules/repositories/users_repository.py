from modules.models.users import User


class UserRepository:
    def __init__(self, session):
        self.session = session

    def create(self, name, telegram_id):
        user = User(
            name=name,
            telegram_id=telegram_id
        )
        self.session.add(user)
        self.session.commit()

    def get(self, telegram_id):
        return (self.session.query(User)
                .filter_by(telegram_id=telegram_id)
                .first())

    def delete(self, telegram_id):
        target_user = self.get(telegram_id)
        if target_user:
            self.session.delete(target_user)
            self.session.commit()
        else:
            raise ValueError("Couldn't find'")
