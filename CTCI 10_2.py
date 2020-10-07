# Group Anagrams: write a method to sort an array of strings so that all the anagrams are next to each other.

# Anagrams are words that have the same characters but in different orders

def groupAnagrams (arr):

	result = {}

	for i in arr:
		x = "".join(sorted(i))

		if x in result:
			result[x].append(i)
		else:
			result[x] = [i]
			
	return list(result.values())

if __name__ == '__main__':
	print ("This is the implementation of Group Anagrams")

	arr = ["eat","tea","tan","ate","nat","bat", "cat", "dog", "tac", "god", "act"]

	print (groupAnagrams(arr))