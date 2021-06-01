import psutil, os, signal
#procs = {p.pid: p.info for p in psutil.process_iter(attrs=['name', 'username'])}
res=[p.info for p in psutil.process_iter(attrs=['pid', 'name']) if 'notepad' in p.info['name']]
print([p.info for p in psutil.process_iter(attrs=['pid', 'name']) if 'notepad' in p.info['name']])
print(res)
print(type(res))
print(res['pid'])

