import string
import sys
from dedupFuncs import *

duplicates = []
if len(sys.argv) == 1:
    print "Please enter a filename to deduplicate"
    sys.exit()

fileName = sys.argv[1]
print fileName[:-4]

print 'Reading records...'
all_records = read_records(fileName[:-4])

print str(len(all_records)) + ' records found'

#print 'Excluding duplicate titles...'
#edited_records = uniqify(all_records, lambda x: x[len(x)-1:][0])

#print 'Flagging likely duplicates...'
#likely_dups = likely(edited_records.edit)

print 'Running...'
results = uniquify(all_records)

total_dups = 0
remaining = 0

for i in range(1, len(results)):
    output_records(fileName[:-4], 'Iteration' + str(i), results[i].edit)
    print 'it {0} - duplicates: {1}\tremaining: {2}'.format(i, len(results[i].duplicates), len(results[i].edit))
    total_dups += len(results[i].duplicates)
    

print 'deduplication complete.'
print 'duplicates: {0}'.format(total_dups)


#print 'duplicates removed: ', len(edited_records.duplicates)
#print 'Possible duplicates: ', len(likely_dups)
