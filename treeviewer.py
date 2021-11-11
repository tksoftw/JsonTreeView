# DEPTHSTRING = "V V V V V"

def treeViewDict(d: dict, prefix = '') -> None:
  for k in d.keys():
    if isinstance(d[k], dict):
      print(f"{len(prefix)*' ' + prefix}[\"{str(k)}\"]:")
      prefix += '-'
      treeViewDict(d[k], prefix)
      prefix = prefix[:-1]
    elif isinstance(d[k], list):
      print(f"{len(prefix)*' ' + prefix}[\"{str(k)}\"]:")
      prefix += '-'
      treeViewList(d[k], prefix)
      prefix = prefix[:-1]
    else:
      print(f"{len(prefix)*' ' + prefix}[\"{str(k)}\"]:", str(type(d[k]))[8:-2])

def treeViewList(l: list, prefix = '') -> None:
  for i in range(len(l)):
    if isinstance(l[i], list):
      print(f"{len(prefix)*' ' + prefix}[{i}]:")
      prefix += '>'
      treeViewList(l[i], prefix)
      prefix = prefix[:-1]
    elif isinstance(l[i], dict):
      print(f"{len(prefix)*' ' + prefix}[{i}]:")
      prefix += '>'
      treeViewDict(l[i], prefix)
      prefix = prefix[:-1]
    else:
      print(f"{len(prefix)*' ' + prefix}[{i}]:", str(type(l[i]))[8:-2])

def viewTree(o: any) -> None:
  if isinstance(o, dict):
    treeViewDict(o)
  elif isinstance(o, list):
    treeViewList(o)
  else:
    print('Unsupported type')