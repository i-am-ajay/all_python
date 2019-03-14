from salary import global_vars
from salary.create_workbook import create_workbook, create_sheet_with_headers, create_sheets_as_heads
from salary.get_sheet import get_sheet
from salary.global_vars import COMMON_HEAD_FOX_HEAD_MAP


def head_mapping(file_name, sheet_name):
    sheet = get_sheet(file_name, sheet_name)
    last_cell = sheet.max_row
    for row in range(1, last_cell):
        cell1 = sheet.cell(row=row, column=1)
        cell2 = sheet.cell(row=row, column=2)
        if cell2.value:
            global_vars.FOX_PROD_SALHEADS[cell1.value] = cell2.value


def sequence_mapping(file_name, sheet_name):
    sheet = get_sheet(file_name, sheet_name)
    count = 0
    for row in sheet:
        for col in row:
            prod_head = global_vars.FOX_PROD_SALHEADS.get(col.value,'None')
            if prod_head != ' ':
                global_vars.HEAD_SEQUENCE[col.value] = count
                global_vars.SEQUENCE_HEAD_MAP[count] = col.value
            elif col.value == 'PR_ADEPF':
                global_vars.HEAD_SEQUENCE[col.value] = count
                global_vars.SEQUENCE_HEAD_MAP[count] = col.value
            elif col.value == 'PR_ADPF':
                global_vars.HEAD_SEQUENCE[col.value] = count
                global_vars.SEQUENCE_HEAD_MAP[count] = col.value
            count += 1


        break


def common_head_fox_mapping():
    COMMON_HEAD_FOX_HEAD_MAP['Arrear'] = 'PR_AIDA'
    COMMON_HEAD_FOX_HEAD_MAP['Basic'] = 'PR_IBASIC'
    COMMON_HEAD_FOX_HEAD_MAP['Bonus'] = 'PR_IBONUS'
    COMMON_HEAD_FOX_HEAD_MAP['Car'] = 'PR_CAR_ADV'
    #COMMON_HEAD_FOX_HEAD_MAP['Car'] = 'PR_CAR_INT'
    COMMON_HEAD_FOX_HEAD_MAP['ChildBirth'] = 'PR_ADV_CBI'
    COMMON_HEAD_FOX_HEAD_MAP['ConAll'] = 'PR_ITS'
    COMMON_HEAD_FOX_HEAD_MAP['Cycle'] = 'PR_ADV_CYL'
    COMMON_HEAD_FOX_HEAD_MAP['DA'] = 'PR_IDA'
    COMMON_HEAD_FOX_HEAD_MAP['Day Amount'] = 'DAY_AMT'
    COMMON_HEAD_FOX_HEAD_MAP['Day Off'] = 'DAY_OFF'
    COMMON_HEAD_FOX_HEAD_MAP['Dirty'] = 'PR_IDIRTY'
    COMMON_HEAD_FOX_HEAD_MAP['DP'] = 'PR_IDP'
    COMMON_HEAD_FOX_HEAD_MAP['Educ'] = 'PR_ADV_EDU'
    COMMON_HEAD_FOX_HEAD_MAP['EL Amount'] = 'EL_AMT'
    COMMON_HEAD_FOX_HEAD_MAP['EL Days'] = 'PR_EL'
    COMMON_HEAD_FOX_HEAD_MAP['Elec'] = 'PR_DELEC'
    COMMON_HEAD_FOX_HEAD_MAP['FPF'] = 'PR_DEPF'
    COMMON_HEAD_FOX_HEAD_MAP['AFPF'] = 'PR_ADEPF'
    COMMON_HEAD_FOX_HEAD_MAP['Festival'] = 'PR_ADV_FES'
    COMMON_HEAD_FOX_HEAD_MAP['Funeral'] = 'PR_ADV_OTH'
    COMMON_HEAD_FOX_HEAD_MAP['HouseBuilding'] = 'PR_ADV_O2'
    #COMMON_HEAD_FOX_HEAD_MAP['HouseBuilding'] = 'PR_O2_INT'
    COMMON_HEAD_FOX_HEAD_MAP['HRA'] = 'PR_IHRA'
    COMMON_HEAD_FOX_HEAD_MAP['OT Amount'] = 'HRS_AMT'
    COMMON_HEAD_FOX_HEAD_MAP['OT Hours'] = 'HRS'
    COMMON_HEAD_FOX_HEAD_MAP['IT'] = 'PR_DIT'
    COMMON_HEAD_FOX_HEAD_MAP['LWP Amount'] = 'PR_DLWPVAL'
    COMMON_HEAD_FOX_HEAD_MAP['LWP Hrs'] = 'PR_LWB'
    COMMON_HEAD_FOX_HEAD_MAP['MarAdv'] = 'PR_ADV_MAR'
    COMMON_HEAD_FOX_HEAD_MAP['Mess'] = 'PR_DMESSAL'
    COMMON_HEAD_FOX_HEAD_MAP['NCA'] = 'N_CARE'
    COMMON_HEAD_FOX_HEAD_MAP['Other Deduction'] = 'PR_DOTH_1'
    COMMON_HEAD_FOX_HEAD_MAP['OT Hours'] = 'HRS'
    COMMON_HEAD_FOX_HEAD_MAP['Other Earning'] = 'PR_IOTALW'
    COMMON_HEAD_FOX_HEAD_MAP['PCA'] = 'P_CARE'
    COMMON_HEAD_FOX_HEAD_MAP['Level'] = 'PR_PAYSCAL'
    COMMON_HEAD_FOX_HEAD_MAP['PF'] = 'PR_DPF'
    COMMON_HEAD_FOX_HEAD_MAP['PF'] = 'PR_ADPF'
    COMMON_HEAD_FOX_HEAD_MAP['Sal Adv'] = 'PR_ADV_SA'
    COMMON_HEAD_FOX_HEAD_MAP['Scooter'] = 'PR_ADV_SCO'
    COMMON_HEAD_FOX_HEAD_MAP['Security'] = 'PR_DSECUR'
    COMMON_HEAD_FOX_HEAD_MAP['SisMarr'] = 'S_M_ADV'
    COMMON_HEAD_FOX_HEAD_MAP['SP'] = 'PR_ISP'
    COMMON_HEAD_FOX_HEAD_MAP['SWF'] = 'PR_DOTHER'
    COMMON_HEAD_FOX_HEAD_MAP['LIC'] = 'PR_LICAMT'
    COMMON_HEAD_FOX_HEAD_MAP['Uniform'] = 'PR_IUNIFOR'
    COMMON_HEAD_FOX_HEAD_MAP['VPF'] = 'PR_DVOLPF'
    COMMON_HEAD_FOX_HEAD_MAP['Washing'] = 'PR_IWASHIN'
    COMMON_HEAD_FOX_HEAD_MAP['Cycle'] = 'PR_ADV_CYL'


if __name__ == '__main__':
    head_mapping('D:\Software\Software\HR Module\Salary\Salary Sept 2017.xlsx','Map')
    sequence_mapping('D:\Software\Software\HR Module\Salary\Salary Sept 2017.xlsx','Sept 2017')
    print(global_vars.FOX_PROD_SALHEADS)
    print(global_vars.HEAD_SEQUENCE)
    print(global_vars.SEQUENCE_HEAD_MAP)

    workbook = create_workbook()
    sheet = create_sheets_as_heads(workbook, global_vars.FOX_PROD_SALHEADS.keys(), 'D://text1.xlsx')
    print(sheet.cell(row=1, column=1).value)
    print(map)
