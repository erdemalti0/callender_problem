p1_time = [['09:00','10:30'],['10:30','12:00'],['14:00','15:00'],['16:00','17:30']]
Bounded1 = ['08:00','20:00']

p2_time = [['10:00','11:30'],['12:00','13:00'],['14:00','15:30'],['16:30','18:00']]
Bounded2 = ['08:00','19:00']

def free_time_finder(time_list):
    free_times = []
    
    for i in range(len(time_list) - 1):
        if time_list[i][1] != time_list[i+1][0]:

            free_time = [time_list[i][1],time_list[i+1][0]]
            free_times.append(free_time)

    return free_times
def time_to_integer(time):
    hour = int(time[0:2])
    minute = int(time[3:5])

    total = (hour * 60) + minute
    return total
def add_bound(free_time,bounded,p_time):
    if bounded[0] == p_time[0][0]:
        pass

    if bounded[-1] == p_time[-1][-1]:
        pass

    if time_to_integer(bounded[0]) < time_to_integer(p_time[0][0]):
        free_time.insert(0,[bounded[0],p_time[0][0]])

    if time_to_integer(bounded[-1]) > time_to_integer(p_time[-1][-1]):
        free_time.append([p_time[-1][-1],bounded[-1]]) 
def compare(time_1,time_2):
    available_meeting_times = []
    for i in range(len(time_1)):
        t1_1 = time_to_integer(time_1[i][0])
        t1_2 = time_to_integer(time_1[i][1])

        for j in range(len(time_2)):
            t2_1 = time_to_integer(time_2[j][0])
            t2_2 = time_to_integer(time_2[j][1])

            if t1_1 <= t2_1 and t1_2 >= t2_2:
                available_meeting_times.append([time_2[j][0],time_2[j][1]])

            elif t1_1 >= t2_1 and t1_2 <= t2_2:
                available_meeting_times.append([time_1[i][0],time_1[i][1]])

            elif t2_1 < t1_1 and t2_2 < t1_2 and t1_1  < t2_2:
                available_meeting_times.append([time_1[i][0],time_2[j][1]])

            elif t2_1 > t1_1 and t2_2 > t1_2 and t1_1 >  t1_2:
                available_meeting_times.append([time_2[j][0],time_1[i][1]])

    return available_meeting_times


free_time_1 = free_time_finder(p1_time)
free_time_2 = free_time_finder(p2_time)
add_bound(free_time_1,Bounded1,p1_time)
add_bound(free_time_2,Bounded2,p2_time)

print(compare(free_time_1,free_time_2))