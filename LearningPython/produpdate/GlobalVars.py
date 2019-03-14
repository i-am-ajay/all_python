__author__ = 'gaa8664'

EMP_DES_MAPPING = {
    'Designation||96': 'Jr. Technical Officer',
    'Designation||539': 'Sr. Technical Assistant',
    'Designation||537': 'Sr. Staff Nurse',
    'Designation||199': 'Staff Nurse',
    'Designation||NO': 'Nursing Officer',
    'Designation||213': 'Ward Sister',
    'Designation||536': 'Sr. Ward Sister',
    'Designation||SNO': 'Senior Nursing Officer',
    'Designation||120': 'Nursing Aid',
    'Designation||542': 'Nursing Assistant'
}

# map old designation code to new designation, so that in to designation entry new designation could be added in prodigious redesignation module.
EMP_NEW_DES = {
    'Designation||537': 'Nursing Officer',
    'Designation||199': 'Nursing Officer',
    'Designation||213': 'Senior Nursing Officer',
    'Designation||536': 'Senior Nursing Officer',
    'Designation||539' : 'Jr. Technical Officer',
    'Designation||120' : 'Nursing Assistant'
}

#map old designation to new designation so that old designation could be replaced by new designation against employee.
EMP_NEW_DES_CODE = {
    'Designation||537': 'Designation||NO',
    'Designation||199': 'Designation||NO',
    'Designation||213': 'Designation||SNO',
    'Designation||536': 'Designation||SNO',
    'Designation||539': 'Designation||96',
    'Designation||120': 'Designation||542'
}