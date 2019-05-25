
import subprocess
import os
import pandas as pd
import re
from mpl_toolkits.basemap import Basemap, cm
import matplotlib.pyplot as plt

def grib_to_dataframe(grib_file_name):
    output_txt=subprocess.check_output(['grib_get_data',grib_file_name])
    #clean_output_txt=' '.join(output_txt.split())
    clean_output_txt=re.sub('\s+', ' ', str(output_txt)).strip()
    output_grib_list=str(clean_output_txt).split('\\n')
    output_grib_data=output_grib_list[1:]
    try:
        titles_dirt=output_grib_list[0].split("'")[1].split(',')
    except:
        titles_dirt=output_grib_list[0].split(',')
    titles = [item.strip() for item in titles_dirt]
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
grib_df_10=grib_df.head(2000)

for i in grib_df.keys():
    grib_df[i] = grib_df[i].astype(float)

m=Basemap(projection='robin',lon_0=0.0)
m.drawcoastlines()
m.drawcountries()

#x_coor=grib_df['Latitude'].tolist()
x_coor=grib_df['Longitude'].tolist()
y_coor=grib_df['Latitude'].tolist()
pressure=grib_df['Value'].tolist()
normalized_pressure=[(item-4500)/2000 for item in pressure]
x,y=m(x_coor,y_coor)
m.plot(x,y,'go',markersize=1,alpha=0.5)
#clevs = [0,0.25,0.5,0.75,1]
#cs = m.contourf(x,y,normalized_pressure,clevs,cmap=cm.s3pcpn)
# add colorbar.
#cbar = m.colorbar(cs,location='bottom',pad="5%")
#cbar.set_label('mm')
plt.title('Basemap Tutorial')
plt.show()