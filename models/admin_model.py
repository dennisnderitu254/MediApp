class Admin(BaseModel):
    __tablename__ = 'admins'

    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)

    user = relationship("User", backref="admin", uselist=False)

    def __init__(self, user_id):
        self.user_id = user_id
