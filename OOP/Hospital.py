# Create a suedo hospital
import random

class Patient(object):
    def __init__(self,name,allergies):
        self.id = 0
        self.name = name
        self.allergies = allergies
        self.bed = 'none'

class Hospital(object):
    def __init__(self,name,capacity):
        self.name = name
        self.patients = []
        self.capacity = capacity
    
    def info(self):
        print self.name, ' Patients : ', len(self.patients)
        for patient in self.patients:
            # call.displayCall()
            print 'Patient ', '%-20s' % patient.name,' Bed: ', patient.bed

    def addPatient(self,patient): # Add patient record, use random/coin flip tp determine Addmitance
        random_num = random.random()*2
        if random_num <= 1:
            # hospital is full/unable to admit
            admission = patient.name," Admission Failure, Hospital is Full"
            return admission
        else: # Admit the Patient
            room = int(random_num *50)
            admission = patient.name," Admission Accepted, bed # ",room,' assigned.'            
            self.patients.append(patient)
            patient.bed = room
            return admission



    def discharge(self,patient):  # And Set patient bed to none!!!
        self.patients.remove(patient)
        patient.bed = 'none'
        print patient.name,' Has been discharged. patient bed: ',patient.bed
        return

## Do some hospital Business
##

# Enter Patient
# Admit to hospital according to capacity(Random determination)
#   add patient to patients array accordingly
# diaplay Hospital patients
# discharge a patient
#   set patient bed to none

jonesM = Patient('Marvin Jones','NO Allergies')
smithT = Patient('Thomas Smith','Penicillin')
lewisL = Patient('Lanny Lewis','peanut Butter')
franzS = Patient('Steve Franz','NO Allergies')
domingoA = Patient('Alberto Domingo','Ragweed')

#random_num = random.random()
#print int(random_num *100) # room#
print
StElseWhere = Hospital('St ElseWhere',200)
print StElseWhere.addPatient(jonesM)
print StElseWhere.addPatient(smithT)
print StElseWhere.addPatient(lewisL)
print StElseWhere.addPatient(domingoA)
print
StElseWhere.info()
print
StElseWhere.discharge(smithT)
print
StElseWhere.info()





