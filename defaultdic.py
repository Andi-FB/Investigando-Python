from collections import defaultdict


def sorting_func(string):
    return int(string)


d = defaultdict(list)
d['python'].append('10')
d['python'].append('2')
d['python'].append('5')

print("d['python'].__contains__('10'): {}".format(d['python'].__contains__('10')))
print(str(d['python']))
d['python'].sort(key=sorting_func)
print('d["python"]: ' + str(d['python']))
print('d["python"][0]: ' + d['python'][0])
print('d["python"][2]: ' + d['python'][2])
print(str(len(d['python'])))