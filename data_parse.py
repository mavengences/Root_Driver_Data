# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 17:39:23 2017

@author: Dorien Xia
"""

def driver_parse(driver_string):
    name=driver_string.split(' ')[1].split('\n')[0]
    return name

def hours_calculator(time_string):
    time_list=time_string.split(':')
    hours=int(time_list[0])+int(time_list[1])/60
    return hours

def trip_parse(trip_string, output_dict):
    trip_list=trip_string.split(' ')
    trip_name=trip_list[1].split('\n')[0]
    trip_start=hours_calculator(trip_list[2])
    trip_end=hours_calculator(trip_list[3])
    trip_distance=float(trip_list[4].split('\n')[0])
    trip_time_test=(trip_end-trip_start)
    if trip_time_test<0:
        trip_time=24-trip_end+trip_start
    else:
        trip_time=trip_time_test
    #Miles_Per_Hour=float(trip_distance)/trip_time
    output_dict[trip_name]['Distance'].append(trip_distance)
    output_dict[trip_name]['Trip Time'].append(trip_time)


    
"""
Script Functionality Starts Here
"""


input_list=[]
with open("input.txt") as f:
    input_list=f.readlines()
    #print(input_list)

int_output_dict={}
for i in input_list:
    if i.split(' ')[0]=='Driver':
        name=driver_parse(i)
        int_output_dict[name]={}
        int_output_dict[name]['Distance']=[]
        int_output_dict[name]['Trip Time']=[]
for i in input_list:
    if i.split(' ')[0]=='Trip':
        print(i)
        trip_parse(i,int_output_dict)

final_output_dict={}        
for k in int_output_dict:
    final_output_dict[k]={}
    final_output_dict[k]['Distance']=[]
    final_output_dict[k]['MPH']=[]
    if len(int_output_dict[k]['Distance'])!=0:
        final_output_dict[k]['Distance']=int(round(sum(int_output_dict[k]['Distance'])))
        #final_output_dict[k]['Distance']=sum(int_output_dict[k]['Distance'])
    else:
        final_output_dict[k]['Distance']=[]
    if sum(int_output_dict[k]['Trip Time'])!=0:
        final_output_dict[k]['MPH']=int(round(sum(int_output_dict[k]['Distance'])/sum(int_output_dict[k]['Trip Time'])))
        #final_output_dict[k]['MPH']=sum(int_output_dict[k]['Distance'])/sum(int_output_dict[k]['Trip Time'])
    else:
        final_output_dict[k]['MPH']=[]
        
print(int_output_dict)
print('\n')
print('\n')
print('\n')
print(final_output_dict)

assert final_output_dict['Dan']['Distance']==39
assert final_output_dict['Dan']['MPH']==47
assert final_output_dict['Alex']['Distance']==42
assert final_output_dict['Alex']['MPH']==34
assert final_output_dict['Bob']['Distance']==[]
assert final_output_dict['Bob']['MPH']==[]