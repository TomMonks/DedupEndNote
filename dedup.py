import string
import sys
from dedupFuncs import *

duplicates = []
if len(sys.argv) == 1:
    print "Please enter a filename to deduplicate"
    sys.exit()

fileName = sys.argv[1]

print 'Reading records...'
all_records = read_records(fileName)

print 'Excluding duplicate titles...'
edited_records = uniqify(all_records, lambda x: x[len(x)-1:][0])

print 'Flagging likely duplicates...'
likely_dups = likely(edited_records.edit)

print 'Outputting results...'
output_records(fileName, 'edit', edited_records.edit)
output_records(fileName, 'dups', edited_records.duplicates)
output_records(fileName, 'likely_dups', likely_dups)

print 'deduplication complete'
print 'duplicates removed: ', len(edited_records.duplicates)
print 'Possible duplicates: ', len(likely_dups)
