'''
# it should use the double quotation marks to include the two arguments
# python create_file_by_name.py "QUESTION" "LEVEL"
# >>> python create_file_by_name.py "2134. Minimum Swaps to Group All 1's Together II" "medium"
'''

import os
import sys

fname = sys.argv[1]
level = sys.argv[2]

letters = fname.split(' ')

new_name_0 = letters[0].split('.')[0] + '--' + level + '--'
new_name_1 = ('-'.join(letters[1:])).replace('\'', '')

new_name = new_name_0 + new_name_1 + '.md'

print(new_name)

os.system("cp draft/a.md " + new_name)
