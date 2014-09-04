import thinkstats
import math
import first
import survey
import Pmf
import operator
from collections import defaultdict

#Exercise 2.1

def pumpkin(pumplist):
    mean , var = thinkstats.MeanVar(pumplist)
    stdev = math.sqrt(var)
    print 'mean: %.2f' % mean +' variance: %.2f' % var + ' standard deviation: %.2f' % stdev + "\n"
    
test_batch = [1,1,1,3,3,591] 
print '\nExercise 2.1:'
pumpkin(test_batch)

#Exercise 2.2

tables, firsts, others = first.MakeTables()
first.ProcessTables(firsts, others)
meanfirsts, varfirsts = thinkstats.MeanVar(firsts.lengths)
meanothers, varothers = thinkstats.MeanVar(others.lengths)
stdevfirsts = math.sqrt(varfirsts)
stdevothers = math.sqrt(varothers)

print 'Exercise 2.2:'
print 'Standard Deviation for first pregnancies: %.2f' % stdevfirsts
print 'Standard Deviation for other pregnancies: %.2f' % stdevothers + "\n"

#Exercise 2.3

def mode(h):
    max = 0
    hmode = ''
    list = h.Values()
    while len(list)>0:
        x = list[0]
        if h.Freq(x) > max:
            hmode = x
            max = h.Freq(x)
        list = list[1:]
    return hmode

def allmodes(h):
    d = defaultdict()
    list = h.Values()
    for l in list:
        d[l] = h.Freq(l)
    #sorted(d,key=lambda x: x[1])
    sorted_d = sorted(d.iteritems(), key=operator.itemgetter(1))
    return sorted_d

hist = Pmf.MakeHistFromList([1,2,2,3,3,3,5])


print 'Exercise 2.3:'
print 'Mode: ' + str(mode(hist))
print 'AllModes: ' + str(allmodes(hist)) + '\n' s


#Exercise 2.5

def PmfMean(p):
    list = p.Values()
    m = 0
    for l in list:
        m = m + p.Prob(l)*l 
    return m
    
def PmfVar(p):
    list = p.Values()
    m = PmfMean(p)
    v = 0
    for l in list:
        v = v + p.Prob(l)*((l - m)**2)
    return v
    
print 'Exercise 2.5:'
pmf = Pmf.MakePmfFromList([1,2,2,3,5])
print PmfMean(pmf)
print PmfVar(pmf)
    
