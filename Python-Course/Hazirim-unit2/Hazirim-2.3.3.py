#===============INPUT=======================
Number_LEVENIM = input('Number of LEVNIM: ')
print(Number_LEVENIM)
Number_LEVENIM = int(Number_LEVENIM)

#=================Numbers per PIG=====================
First_PIG = (Number_LEVENIM // 100) # First Pig

Second_PIG = int(Number_LEVENIM%100//10) # Second Pig

Threed_PIG = int(Number_LEVENIM%10) # Threed Pig

Total_Collect = Threed_PIG+Second_PIG+First_PIG

print(Total_Collect)
#================Split=======================

Split_Equal = int(Total_Collect / 3)
print(Split_Equal)

#=================%======================

print(Total_Collect % 3)

#================TRUE\FALSE=======================
print(Split_Equal % 3 == 0)