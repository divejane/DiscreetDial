open_hosts =  [['DO NOT DELETE'], ['70.115.119.225', 53416, 'room1', 'b'], ['70.115.119.225', 53417, 'room2', 'b'], ['70.115.119.225', 53418, 'room3', 'b']] 

temp_hosts = [[open_hosts[x][2], open_hosts[x][3]] for x in range(len(open_hosts))[1:]]
print(temp_hosts)