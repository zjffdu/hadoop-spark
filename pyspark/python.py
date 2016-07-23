

def both_ends(s):
	if len(s) <= 2:
		return s
	return s[:2] + s[-2:]


def remove_adjacent(nums):
	result = []
	last = None
	for x in nums:
		if x != last:
			result.append(x)
			last=x
	return result


def verbing(s):
	if len(s) < 3:
		return s
	elif s.endswith('ing'):
		return s+'ly'
	else:
		return s+'ing'

