from salary import global_vars


def generate_fox_sal_map(row):
    fox_sal_map = {}
    fox_sal_map['Car'] = 0.0
    fox_sal_map['HouseBuilding'] = 0.0
    fox_sal_map['Scooter'] = 0.0
    fox_sal_map['MarAdv'] = 0.0
    fox_sal_map['SisMarr'] = 0.0
    fox_sal_map['PF'] = 0.0
    fox_sal_map['FPF'] = 0.0

    for x in global_vars.FOX_PROD_SALHEADS:
        index = global_vars.HEAD_SEQUENCE[x]
        fox_value = row[index].value if row[index].value else 0.0
        try:
            fox_value = float(fox_value)
        except TypeError as excep:
            pass
        except ValueError as excep:
            pass
        if x == 'PR_AIDA':
            fox_sal_map['Arrear'] = fox_value
        elif x == 'PR_IBASIC':
            fox_sal_map['Basic'] = fox_value
        elif x == 'PR_IBONUS':
            fox_sal_map['Bonus'] = fox_value
        elif x == 'PR_CAR_ADV':
            val = fox_sal_map['Car'] + fox_value
            fox_sal_map['Car'] = val
        elif x == 'PR_CAR_INT':
            val = fox_sal_map['Car'] + fox_value
            fox_sal_map['Car'] = val
        elif x == 'PR_ADV_CBI':
            fox_sal_map['ChildBirth'] = fox_value
        elif x == 'PR_ITS':
            fox_sal_map['ConAll'] = fox_value
        elif x == 'PR_ADV_CYL':
            fox_sal_map['Cycle'] = fox_value
        elif x == 'PR_IDA':
            fox_sal_map['DA'] = fox_value
        elif x == 'DAY_AMT':
            fox_sal_map['Day Amount'] = fox_value
        elif x == 'DAY_OFF':
            fox_sal_map['Day Off'] = fox_value
        elif x == 'PR_IDIRTY':
            fox_sal_map['Dirty'] = fox_value
        elif x == 'PR_IDP':
            fox_sal_map['DP'] = fox_value
        elif x == 'PR_ADV_EDU':
            fox_sal_map['Educ'] = fox_value
        elif x == 'EL_AMT':
            fox_sal_map['EL Amount'] = fox_value
        elif x == 'PR_EL':
            fox_sal_map['EL Days'] = fox_value
        elif x == 'PR_DELEC':
            fox_sal_map['Elec'] = fox_value
        elif x == 'PR_DEPF':
            fox_sal_map['FPF'] += fox_value
        elif x == 'PR_ADEPF':
            fox_sal_map['FPF'] += fox_value
        elif x == 'PR_ADV_FES':
            fox_sal_map['Festival'] = fox_value
        elif x == 'PR_ADV_OTH':
            fox_sal_map['Funeral'] = fox_value
        elif x == 'PR_ADV_O2':
            val = fox_sal_map['HouseBuilding'] + fox_value
            fox_sal_map['HouseBuilding'] = val
        elif x == 'PR_O2_INT':
            val = fox_sal_map['HouseBuilding'] + fox_value
            fox_sal_map['HouseBuilding'] = val
        elif x == 'PR_IHRA':
            fox_sal_map['HRA'] = fox_value
        elif x == 'HRS_AMT':
            fox_sal_map['OT Amount'] = fox_value
        elif x == 'HRS':
            fox_sal_map['OT Hours'] = fox_value
        elif x == 'PR_DIT':
            fox_sal_map['IT'] = fox_value
        elif x == 'PR_DLWPVAL':
            fox_sal_map['LWP Amount'] = fox_value
        elif x == 'PR_LWB':
            fox_sal_map['LWP Hrs'] = fox_value
        elif x == 'PR_ADV_MAR':
            val = fox_sal_map['MarAdv'] + fox_value
            fox_sal_map['MarAdv'] = val
        elif x == 'PR_DMESSAL':
            fox_sal_map['Mess'] = fox_value
        elif x == 'N_CARE':
            fox_sal_map['NCA'] = fox_value
        elif x == 'PR_DOTH_1':
            fox_sal_map['Other Deduction'] = fox_value
        elif x == 'HRS':
            fox_sal_map['OT Hours'] = fox_value
        elif x == 'PR_IOTALW':
            fox_sal_map['Other Earning'] = fox_value
        elif x == 'P_CARE':
            fox_sal_map['PCA'] = fox_value
        elif x == 'PR_PAYSCAL':
            fox_sal_map['Level'] = fox_value
        elif x == 'PR_DPF':
            fox_sal_map['PF'] += fox_value
        elif x == 'PR_ADPF':
            fox_sal_map['PF'] += fox_value
        elif x == 'PR_ADV_SA':
            fox_sal_map['Sal Adv'] = fox_value
        elif x == 'PR_ADV_SCO':
            val = fox_sal_map['Scooter'] + fox_value
            fox_sal_map['Scooter'] = val
        elif x == 'PR_SCO_INT':
            val = fox_sal_map['Scooter'] + fox_value
            fox_sal_map['Scooter'] = val
        elif x == 'PR_DSECUR':
            fox_sal_map['Security'] = fox_value
        elif x == 'S_M_ADV':
            val = fox_sal_map['SisMarr'] + fox_value
            fox_sal_map['SisMarr'] = val
        elif x == 'PR_SIS_INT':
            val = fox_sal_map['SisMarr'] + fox_value
            fox_sal_map['SisMarr'] = val
        elif x == 'PR_ISP':
            fox_sal_map['SP'] = fox_value
        elif x == 'PR_DOTHER':
            fox_sal_map['SWF'] = fox_value
        elif x == 'PR_LICAMT':
            fox_sal_map['LIC'] = fox_value
        elif x == 'PR_IUNIFOR':
            fox_sal_map['Uniform'] = fox_value
        elif x == 'PR_DVOLPF':
            fox_sal_map['VPF'] = fox_value
        elif x == 'PR_IWASHIN':
            fox_sal_map['Washing'] = fox_value
        elif x == 'PR_ADV_CYL':
            fox_sal_map['Cycle'] = fox_value
    return fox_sal_map

