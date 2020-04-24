import os

print(os.stat('conf.yaml'))

cur=os.getcwd()
print(os.path.split(cur))
print(os.path.dirname(cur))
print(os.path.basename(cur))