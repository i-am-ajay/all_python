from salary import global_vars


def generate_prod_sal_map(prod_map):
    prod_sal_map = {}
    prod_sal_map['Funeral'] = 0.0
    prod_sal_map['HouseBuilding'] = 0.0
    prod_sal_map['Festival'] = 0.0
    prod_sal_map['MarAdv'] = 0.0
    prod_sal_map['Salary'] = 0.0
    prod_sal_map['Educ'] = 0.0
    prod_sal_map['ChildBirth'] = 0.0
    prod_sal_map['LIC'] = 0.0
    prod_sal_map['SWF'] = 0.0
    prod_sal_map['Car'] = 0.0
    prod_sal_map['SisMarr'] = 0.0
    prod_sal_map['Other Earning']= 0.0
    prod_sal_map['Other Deduction'] = 0.0
    prod_sal_map['Scooter'] = 0.0
    prod_sal_map['FPF'] = 0.0
    prod_sal_map['PF'] = 0.0

    for x in prod_map:
        amount = abs(float(prod_map.get(x, 0.0)))
        if x == '9||ARREAR':
            prod_sal_map['Arrear'] = amount
        elif x == '9||BASIC':
            prod_sal_map['Basic'] = amount
        elif x == '9||BONUS':
            prod_sal_map['Bonus'] = amount
        elif x == '9||Car':
            val = prod_sal_map['Car'] + amount
            prod_sal_map['Car'] = val
        elif x == '9||Car Int.':
            val = prod_sal_map['Car'] + amount
            prod_sal_map['Car'] = val
        elif x.lower().find('child') > -1:
            val = prod_sal_map['ChildBirth'] + amount
            prod_sal_map['ChildBirth'] = val
        elif x == '9||CONALL':
            prod_sal_map['ConAll'] = amount
        elif x == '9||Cycle':
            prod_sal_map['Cycle'] = amount
        elif x == '9||DA':
            prod_sal_map['DA'] = amount
        elif x == '9||COFFAMT':
            prod_sal_map['Day Amount'] = amount
        elif x == '9||COFF':
            prod_sal_map['Day Off'] = amount
        elif x == '9||DIRTYALLWN':
            prod_sal_map['Dirty'] = amount
        elif x == '9||DP':
            prod_sal_map['DP'] = amount
        elif x.lower().find('higheredu') > -1:
            val = prod_sal_map['Educ'] + amount
            prod_sal_map['Educ'] = val
        elif x == '9||ELAMT':
            prod_sal_map['EL Amount'] = amount
        elif x == '9||ELDAYS':
            prod_sal_map['EL Days'] = amount
        elif x == '9||ELECTRICITY':
            prod_sal_map['Elec'] = amount
        elif x == '9||FPF':
            prod_sal_map['FPF'] += amount
        elif x == '9||AFPF':
            prod_sal_map['FPF'] += amount
        elif x.lower().find('festival') > -1:
            val = prod_sal_map['Festival'] + amount
            prod_sal_map['Festival'] = val
        elif x.lower().find('funeral') > -1:
            val = prod_sal_map['Funeral'] + amount
            prod_sal_map['Funeral'] = val
        elif x.lower().find('housebuilding') > -1:
            val = prod_sal_map['HouseBuilding'] + amount
            prod_sal_map['HouseBuilding'] = val
        elif x == '9||HouseBuilding Int.':
            prod_sal_map += amount
        elif x == '9||HRA':
            prod_sal_map['HRA'] = amount
        elif x == '9||OTAMT':
            prod_sal_map['OT Amount'] = amount
        elif x == '9||OTHRS':
            prod_sal_map['OT Hours'] = amount
        elif x == '9||IT':
            prod_sal_map['IT'] = amount
        elif x == '9||LWPAMT':
            prod_sal_map['LWP Amount'] = amount
        elif x == '9||LWPDAYS':
            prod_sal_map['LWP Hrs'] = amount
        elif x.lower().find('marriagedep') > -1:
            val = prod_sal_map['MarAdv'] + amount
            prod_sal_map['MarAdv'] = val
        elif x.lower().find('marriageself') > -1:
            val = prod_sal_map['MarAdv'] + amount
            prod_sal_map['MarAdv'] = val
        elif x == '9||MESS':
            prod_sal_map['Mess'] = amount
        elif x == '9||NCA':
            prod_sal_map['NCA'] = amount
        elif x == '9||OTHERSD':
            prod_sal_map['Other Deduction'] += amount
        elif x == '9||MTELCHARGES':
            prod_sal_map['Other Deduction'] += amount
        elif x == '9||DNBFEE':
            prod_sal_map['Other Deduction'] += amount
        elif x == '9||HC':
            prod_sal_map['Other Deduction'] += amount
        elif x == '9||OTHERSE':
            prod_sal_map['Other Earning'] += amount
        elif x == '9||CASHALL':
            prod_sal_map['Other Earning'] += amount
        elif x == '9||OINC':
            prod_sal_map['Other Earning'] += amount
        elif x == '9||PCA':
            prod_sal_map['PCA'] = amount
        elif x == '9||LEVEL':
            prod_sal_map['Level'] = amount
        elif x == '9||PF':
            prod_sal_map['PF'] += amount
        elif x == '9||APF':
            prod_sal_map['PF'] += amount
        elif x == '9||Salary':
            prod_sal_map['Sal Adv'] = amount
        elif x == '9||Scooter':
            prod_sal_map['Scooter'] += amount
        elif x == '9||Scooter Int.':
            prod_sal_map['Scooter'] += amount
        elif x == '9||SECURITYC':
            prod_sal_map['Security'] = amount
        elif x.lower().find('marriagesis') > -1:
            val = prod_sal_map['SisMarr'] + amount
            prod_sal_map['SisMarr'] = val
        elif x == '9||CC':
            prod_sal_map['SP'] = amount
        elif x.lower().find('swf') > -1:
            val = prod_sal_map['SWF'] + amount
            prod_sal_map['SWF'] = val
        elif x.lower().find('lic') > -1:
            val = prod_sal_map['LIC'] + amount
            prod_sal_map['LIC'] = val
        elif x == '9||UALL':
            prod_sal_map['Uniform'] = amount
        elif x == '9||VPF':
            prod_sal_map['VPF'] = amount
        elif x == '9||WA':
            prod_sal_map['Washing'] = amount
        elif x == '9||CYCLE':
            prod_sal_map['Cycle'] = amount
    return prod_sal_map

