import psutil , re
results = []
for proc in psutil.process_iter(['pid', 'name', 'username',"cmdline"]):
    if (proc.info["cmdline"] != []) & (proc.info["name"] == "python") :
        bool_sum = np.sum([True for i in proc.info["cmdline"] if re.search("joblib" , i) is not None])
        if bool_sum > 0 :
            results.append(proc.info["pid"])
print(proc)
print(results)
# for pid in results :            
#     psutil.Process(pid).kill()