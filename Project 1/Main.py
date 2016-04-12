from TrieNode import TrieNode 
from suffixtree import SuffixTree

file_object = open("Files/mississippi.txt")

print"Reading mississippi.txt:"
content = file_object.read()

print content


print "Testing TrieNode.py"
tn = TrieNode("Test", 23, 32)

print tn.indexes
print tn.child
print tn.sibling

tn.change_indexes([3, 2])
tn.change_child("Nope")
tn.change_sibling(None)

print tn.indexes
print tn.child
print tn.sibling