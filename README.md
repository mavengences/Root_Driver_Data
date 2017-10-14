
Root Insurance Coding Challenge

Python 3.6 

Dorien Xia

To run this code, clone the github repo/ extract the tarball, cd to the directory where the code is located and type "python data_parse.py"

Code documentation/ thought process can be seen below:

The first step to solving this coding challenge is to read the input text file in as a python object. In this case, I chose to 
read the object in as a python list line by line because lists are easily iterable and easy to sort. 
```

input_list=[]
with open("input.txt") as f:
    input_list=f.readlines()
    #print(input_list)

```	

Once the input file is loaded line by line into a python list, we will iterate over that list to determine whether or not a certain
record is a "Driver" record or a "Trip". In order to do this, we will parse each line within the input list to determine
whether or not the first record within each line is "Driver" or "Trip". To do the parsing, I used the python split function which turns an input string into a list delimieted by (' '). Then I call the first object in the list to check for Driver or Trip. The "Assert" statement below checks to ensure
that the input list is not empty. This test case is a good safety precaution that will cause the script to fail if the input is empty. 

```
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

```

After scanning the file to determine drivers vs trips, I parse each line accordingly where "trip" values are parsed differntly
compared to "driver" values. I will also create a hash-map (python dictionary-list) where each driver name is the primary key. Under each primary key,
There will be python lists corresponding to the number of trips they have taken, distance and travel time. The Driver parse function parses the
driver row and returns name while the trip parse function will parse the trip rows and append data to the hash map called "int_output_dict".
Assert statements with corresponding test cases are used after every function to ensure that the code is running as expected. I chose to use a python dictionary for the overall data structure because dictionaries are called via name such as "Bob" instead of number ex [0]. That way, If I want to see Bob's trip data, I can call ["bob"]["trip data"] instead of creating a for loop and searching over the entire list [0-3] for the name "bob". That being said, both lists and dictionaries have their advantages/disadvantages. The disadvantage for using dictionaries was that final sorting procedures would have to be written manually since python does not contain any native dictionary sorting functions.  

```
def driver_parse(driver_string):
    name=driver_string.split(' ')[1].split('\n')[0]
    return name

assert driver_parse("Driver Dan")=="Dan"
assert driver_parse("Driver Alex")=="Alex"
```

This hours calculator function below is used to turn time in the standard form to numerical form ex: 7:30 -> 7.5. 8:15 -> 8.25
We will also use the .split('\n')[0] function to remove unwanted characters (ex '\n') from the parsing above.
```
def hours_calculator(time_string):
    time_list=time_string.split(':')
    hours=int(time_list[0])+int(time_list[1])/60
    return hours
	
assert hours_calculator("7:45")==7.75
assert hours_calculator("23:30")==23.5

```
The trip parse function below will parse the trip data and append to the corresponding JSON hash maps created above. It will also call the "hours Calculator" function to help with time/trip length calculations. 
```

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
    output_dict[trip_name]['Distance'].append(trip_distance)
    output_dict[trip_name]['Trip Time'].append(trip_time)
    return output_dict
	
test_output_dict={'Dan': {'Distance': [], 'Trip Time': []}, 'Alex': {'Distance': [], 'Trip Time': []}, 'Bob': {'Distance': [], 'Trip Time': []}, 'Clara': {'Distance': [], 'Trip Time': []}}
#print(trip_parse("Trip Dan 07:15 07:45 17.3",test_output_dict)["Dan"]["Trip Time"][0])
#print(trip_parse("Trip Clara 23:01 1:16 42.0",test_output_dict)["Clara"]["Trip Time"][0])
assert trip_parse("Trip Dan 07:15 07:45 17.3",test_output_dict)["Dan"]["Trip Time"][0]==0.5
assert trip_parse("Trip Alex 12:01 13:16 42.0",test_output_dict)["Alex"]["Trip Time"][0]==1.25
assert trip_parse("Trip Clara 23:00 1:15 42.0",test_output_dict)["Clara"]["Trip Time"][0]==2.25

test_string_gen_dict={'Dan': {'Distance': 39, 'MPH': 47}, 'Alex': {'Distance': 42, 'MPH': 34}, 'Bob': {'Distance': 0, 'MPH': 0}}
```

The code below will iterate over the hash map generated in the above statement and aggregate the trip data to determine MPH and total distance traveled.
It utilizes a lot of python existing list summation operations as well as basic division and json list search criteria. It generates a final JSON output 
hash-map where each user (Dan, Bob and Alex) has his MPH and distance aggregated into single numbers. 

ex output: 
{'Dan': {'Distance': 39, 'MPH': 47}, 'Alex': {'Distance': 42, 'MPH': 34}, 'Bob': {'Distance': 0, 'MPH': 0}}

    
```

final_output_dict={}        
for k in int_output_dict:
    final_output_dict[k]={}
    final_output_dict[k]['Distance']=[]
    final_output_dict[k]['MPH']=[]
    if len(int_output_dict[k]['Distance'])!=0:
        final_output_dict[k]['Distance']=int(round(sum(int_output_dict[k]['Distance'])))
    else:
        final_output_dict[k]['Distance']=0
    if sum(int_output_dict[k]['Trip Time'])!=0:
        final_output_dict[k]['MPH']=int(round(sum(int_output_dict[k]['Distance'])/sum(int_output_dict[k]['Trip Time'])))
    else:
        final_output_dict[k]['MPH']=0
```

The assertions below will ensure that  the final output above matches the required output in the problem statement

```
        
assert len(final_output_dict)>0
assert final_output_dict['Dan']['Distance']==39
assert final_output_dict['Dan']['MPH']==47
assert final_output_dict['Alex']['Distance']==42
assert final_output_dict['Alex']['MPH']==34
assert final_output_dict['Bob']['Distance']==0
assert final_output_dict['Bob']['MPH']==0

```

The code below will create a new list used for sorting the final output dicitonary based on distance. The new list will contain all 
distance values generated in the final output hash map above. 

```

list_distance_compare=[]
for k in final_output_dict:
    list_distance_compare.append(final_output_dict[k]['Distance'])
    
print(list_distance_compare)


```

This code below will create the report file by generating a "output.txt" document and writing values from the final hash-map above to 
said file. It will also iterate over the length of the the file and sort the output by Distance with Higher distances at the top. In 
order to accomplish the sorting, it will generate the output string, check to see if the distance for the output string is equal 
to the maximum distance generated from the list above and then write it to the file. It will iterate over the length of the hash map
so that the number of lines in the final output is the same as the number of users in the output JSON hash map. 

```
output_list=[]

try:
    os.remove("output.txt")
except OSError:
    pass
fout = open("output.txt", 'w')

output_list=[]
len_output_list=len(output_list)
print("final output dict is:" + str(final_output_dict))
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
            break
            #print(list_distance_compare)
        elif final_output_dict[k]['Distance']==0 and len(list_distance_compare)==1:
            fout.write(output_string)
            break

fout.close()
 
```

The below code will open the final output report and print some important hash maps used in the creation process just for reference


``` 
print(int_output_dict)
print('\n')
print('\n')
print('\n')
print(final_output_dict)


os.startfile("output.txt")

```

The below code contains test assertions to ensure that the number of rows in the final output report is the same as the number
or rows in the final hash map above

``` 

with open("output.txt") as fout1:
    output_list1=fout1.readlines()
print(output_list1)
print("len final output dict is:"+str(len(final_output_dict)))
print("len final output list is:"+str(len(output_list1)))
assert len(final_output_dict)==len(output_list1)
```

FIN
```
