import time

# get the start time
st = time.time()
stp = time.process_time()

all = {}
for i in range(10000000):
  o = {}
  o['i'] = i
  s = str(i)
  l = len(s)
  o['l'] = [l]
  all[i] = o







# wait for 3 seconds
print('wait')
time.sleep(1)
print('Done')

# get the end time
et = time.time()
etp = time.process_time()

# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
# print(all[99999])

# get execution time
res = etp - stp
print('CPU Execution time:', res, 'seconds')
