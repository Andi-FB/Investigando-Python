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


class SimSet:

    def __init__(self, data):
        self.data = data
        self.list_of_sims = []

    def register_sim(self, sim):
        self.list_of_sims.append(sim)

    def __str__(self):
        sims_to_str = []
        for x in self.list_of_sims:
            sims_to_str.append(str(x))
        return 'Sim Set info:\n\tData: {0}\n\tList Of Sims: {1}'.format(self.data, sims_to_str)


class Sim:

    def __init__(self, sim_set, other_data):
        self.sim_set = sim_set
        self.other_data = other_data
        sim_set.register_sim(self)

    def __str__(self):
        return 'Sim Info:\n\tsimset: {0}\n\tother data: {1}'.format(self.sim_set.data, self.other_data)


simset1 = SimSet('THIS IS THE SIM_SET!')
sim1 = Sim(simset1, 'THIS IS THE SIM!')
print(simset1)
print('#' * 30)
print(sim1)
print('#' * 30)
#Now you can access to the sim_set that the sim Belongs:
print(sim1.sim_set.data)