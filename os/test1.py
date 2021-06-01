import psutil
procs = {p.pid: p.info for p in psutil.process_iter(attrs=['name', 'username'])}
# [p.info for p in psutil.process_iter(attrs=['pid', 'name']) if 'python' in p.info['name']]

print(procs)
for _ in procs:
    print(procs.name)

# print(p.info)