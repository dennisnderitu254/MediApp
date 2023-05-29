class Diagnosis(BaseModel):
    __tablename__ = 'diagnoses'

    appointment_id = Column(String(36), ForeignKey('appointments.id'), nullable=False)
    diagnosis_details = Column(String(255), nullable=False)

    appointment = relationship("Appointment", backref="diagnosis")

    def __init__(self, appointment_id, diagnosis_details):
        self.appointment_id = appointment_id
        self.diagnosis_details = diagnosis_details
