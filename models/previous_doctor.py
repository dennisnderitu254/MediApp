class PreviousDoctor(BaseModel):
    __tablename__ = 'previous_doctors'

    patient_id = Column(String(36), ForeignKey('patients.id'), nullable=False)
    doctor_id = Column(String(36), ForeignKey('doctors.id'), nullable=False)

    patient = relationship("Patient", backref="previous_doctors")
    doctor = relationship("Doctor", backref="previous_patients")

    def __init__(self, patient_id, doctor_id):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
