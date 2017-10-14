# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 17:39:23 2017

@author: Dorien Xia
"""
import os
from collections import OrderedDict

def driver_parse(driver_string):
    name=driver_string.split(' ')[1].split('\n')[0]
    return name

assert driver_parse("Driver Dan")=="Dan"
assert driver_parse("Driver Alex")=="Alex"

def hours_calculator(time_string):
    time_list=time_string.split(':')
    hours=int(time_list[0])+int(time_list[1])/60
    return hours
	
assert hours_calculator("7:45")==7.75
assert hours_calculator("23:30")==23.5

def trip_parse(trip_string, output_dict):
    trip_list=trip_string.split(' ')
    trip_name=trip_list[1].split('\n')[0]
    trip_start=hours_calculator(trip_list[2])
    trip_end=hours_calculator(trip_list[3])
    trip_distance=float(trip_list[4].split('\n')[0])
    trip_time_test=(trip_end-trip_start)
    if trip_time_test<0:
        trip_time=round(24-trip_start+trip_end,2)
    else:
        trip_time=trip_time_test
    #Miles_Per_Hour=float(trip_distance)/trip_time
    output_dict[trip_name]['Distance'].append(trip_distance)
    output_dict[trip_name]['Trip Time'].append(trip_time)
    return output_dict

"""
Script Functionality Starts Here
"""

test_output_dict={'Dan': {'Distance': [], 'Trip Time': []}, 'Alex': {'Distance': [], 'Trip Time': []}, 'Bob': {'Distance': [], 'Trip Time': []}, 'Clara': {'Distance': [], 'Trip Time': []}}
#print(trip_parse("Trip Dan 07:15 07:45 17.3",test_output_dict)["Dan"]["Trip Time"][0])
#print(trip_parse("Trip Clara 23:01 1:16 42.0",test_output_dict)["Clara"]["Trip Time"][0])
assert trip_parse("Trip Dan 07:15 07:45 17.3",test_output_dict)["Dan"]["Trip Time"][0]==0.5
assert trip_parse("Trip Alex 12:01 13:16 42.0",test_output_dict)["Alex"]["Trip Time"][0]==1.25
assert trip_parse("Trip Clara 23:00 1:15 42.0",test_output_dict)["Clara"]["Trip Time"][0]==2.25
    

input_list=[]
with open("input.txt") as f:
    input_list=f.readlines()
    #print(input_list)
	
assert len(input_list)>0

int_output_dict={}
for i in input_list:
    if i.split(' ')[0]=='Driver':
        name=driver_parse(i)
        int_output_dict[name]={}
        int_output_dict[name]['Distance']=[]
        int_output_dict[name]['Trip Time']=[]
for i in input_list:
    if i.split(' ')[0]=='Trip':
        #print(i)
        trip_parse(i,int_output_dict)
    
assert len(int_output_dict)>0

final_output_dict={}        
for k in int_output_dict:
    final_output_dict[k]={}
    final_output_dict[k]['Distance']=[]
    final_output_dict[k]['MPH']=[]
    if len(int_output_dict[k]['Distance'])!=0:
        final_output_dict[k]['Distance']=int(round(sum(int_output_dict[k]['Distance'])))
        #final_output_dict[k]['Distance']=sum(int_output_dict[k]['Distance'])
    else:
        final_output_dict[k]['Distance']=0
    if sum(int_output_dict[k]['Trip Time'])!=0:
        final_output_dict[k]['MPH']=int(round(sum(int_output_dict[k]['Distance'])/sum(int_output_dict[k]['Trip Time'])))
        #final_output_dict[k]['MPH']=sum(int_output_dict[k]['Distance'])/sum(int_output_dict[k]['Trip Time'])
    else:
        final_output_dict[k]['MPH']=0
        
assert len(final_output_dict)>0

#final_output_list=[]
#for k in final_output_dict:
#    string_to_append=k+(final_output_dict[k])
#    final_output_list.append(string_to_append)
#print(final_output_list)

list_distance_compare=[]
for k in final_output_dict:
    list_distance_compare.append(final_output_dict[k]['Distance'])
    
print(list_distance_compare)

output_list=[]

try:
    os.remove("output.txt")
except OSError:
    pass
fout = open("output.txt", 'w')
#with open("output.txt") as f:
#    output_list=f.readlines()

output_list=[]
len_output_list=len(output_list)
print("final output dict is:" + str(final_output_dict))
#while len(final_output_dict)>len_output_list:
print("length final output dict is: " +str(len(final_output_dict)))
for i in range(len(list_distance_compare)):
    for k in final_output_dict:
        if final_output_dict[k]['Distance']==0:
            output_string=str(k)+': '+str(final_output_dict[k]['Distance'])+' miles \n'
        else:
            output_string=str(k)+': '+str(final_output_dict[k]['Distance'])+' miles @ '+str(final_output_dict[k]['MPH'])+' mph\n'
            #print(output_string)
        #print(len(list_distance_compare))
        if final_output_dict[k]['Distance']==max(list_distance_compare):
            #print(final_output_dict[k]['Distance'])
            fout.write(output_string)
            list_distance_compare.remove(max(list_distance_compare))
            #with open("output.txt") as f:
                #output_list=f.readlines()
                #len_output_list=len(output_list)
            break
            #print(list_distance_compare)
        elif final_output_dict[k]['Distance']==0 and len(list_distance_compare)==1:
            fout.write(output_string)
            break

fout.close()
    
        
print(int_output_dict)
print('\n')
print('\n')
print('\n')
print(final_output_dict)


assert final_output_dict['Dan']['Distance']==39
assert final_output_dict['Dan']['MPH']==47
assert final_output_dict['Alex']['Distance']==42
assert final_output_dict['Alex']['MPH']==34
assert final_output_dict['Bob']['Distance']==0
assert final_output_dict['Bob']['MPH']==0

os.startfile("output.txt")

with open("output.txt") as fout1:
    output_list1=fout1.readlines()
print(output_list1)

print("len final output dict is:"+str(len(final_output_dict)))
print("len final output list is:"+str(len(output_list1)))
assert len(final_output_dict)==len(output_list1)