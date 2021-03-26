from myfile import b

print(b.name)

import importlib
res = 'myfile.b'
ret = importlib.import_module(res)
print(ret.name)