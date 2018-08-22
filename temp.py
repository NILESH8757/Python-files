#someone published a blog on codeforces with this script linked.
#I couldn't retrive the original blog. All copyrights reserved to original author.
import sys
import json
import subprocess 
gp30 = [100, 75, 60, 50, 45, 40, 36, 32, 29, 26, 24, 22, 20, 18, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def main(argv):
	subprocess.call(['sh', '-c', 'curl \'https://codeforces.com/api/contest.standings?contestId=1023&from=1&count=30&showUnofficial=false\' >contest1.txt '])
	subprocess.call(['sh', '-c', 'curl \'https://codeforces.com/api/contest.standings?contestId=1025&from=1&count=30&showUnofficial=false\' >contest2.txt '])
	scores = list(map((lambda x: json.loads(open('contest' + str(x) + '.txt').read())), [1, 2]))
	part = {}
	for score in scores:
		for i in range(30):
			row = score['result']['rows'][i]
			handle = row['party']['members'][0]['handle']
			part.setdefault(handle, 0)
			part[handle] += gp30[i]
	participants = list(part.items())
	participants.sort(key=(lambda x: -x[1]))
	print('Winners:')
	for i in range(10):
		print('#{}: [user: {}] (score = {})'.format(i+1, participants[i][0], participants[i][1]))
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
