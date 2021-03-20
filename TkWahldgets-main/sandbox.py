import pandas as pd

df = pd.ExcelFile('IEEE_Member_App_17-18.xlsx')
print(df.sheet_names)
df_sn = df.sheet_names
df_sn.insert(0,'xxxx')
print(df_sn)

def defop(array,var):
    if var == 'Y':
        array_var = array
        array_var.insert(0,'---Select year---')
    if var == 'E':
        array_var = array
        array_var.insert(0,'---Select event---')
    return array_var

print(defop(df.sheet_names,'E')[0])
