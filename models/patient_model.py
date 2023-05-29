class Patient(BaseModel):
    __tablename__ = 'patients'

    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    medical_history = Column(String(255), nullable=True)

    user = relationship("User", backref="patient", uselist=False)

    def __init__(self, user_id, medical_history=None):
        self.user_id = user_id
        self.medical_history = medical_history
