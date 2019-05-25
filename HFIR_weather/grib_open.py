
import subprocess
import os
import pandas as pd
import re

def grib_to_dataframe(grib_file_name):
    output_txt=subprocess.check_output(['grib_get_data',grib_file_name])
    #clean_output_txt=' '.join(output_txt.split())
    clean_output_txt=re.sub('\s+', ' ', str(output_txt)).strip()
    output_grib_list=str(clean_output_txt).split('\\n')
    output_grib_data=output_grib_list[1:]
    try:
        titles=output_grib_list[0].split("'")[1].split(',')
    except:
        titles=output_grib_list[0].split(',')
    list_pre_dataframe=[]
    for row in output_grib_data:
        dict_to_append={}
        list_to_append=[]
        list_to_append=row.strip().split(' ')
        if len(list_to_append)<len(titles):
            continue
        for i in range(0,len(titles)):
            dict_to_append[titles[i]]=list_to_append[i]
        list_pre_dataframe.append(dict_to_append)  
    grib_dataframe=pd.DataFrame(list_pre_dataframe)
    return grib_dataframe

grib_df=grib_to_dataframe('A_HHXK50ECMF121200_C_ECMF_20190412120000_72h_gh_500hPa_global_0p5deg_grib2.bin')
grib_df.head()