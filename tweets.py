from collections import defaultdict
from collections import Counter

FileA = "./MaxTweets.txt"
FileB = "./MaxweetsEveryHour.txt"
FileC = "./MaxFollowers.txt"
FileD = "./MaxRetweets.txt"

ResultFile_PATH = "./USA.txt"

COUNT = Counter()
USERNAMES = defaultdict(int)

N = int(input("Enter value of N: "))

F = open(ResultFile_PATH, 'r', encoding = "utf-8")


for line in F:
    USERNAMES[line.split("\t|\t")[0]] += 1
COUNT = Counter(USERNAMES)
print(COUNT.most_common(N))
TEXT_FILE = open(FileA, "w")
TEXT_FILE.write('\n'.join(str(d) for d in COUNT.most_common(N)))
TEXT_FILE.close()
F.close()


F = open(ResultFile_PATH, 'r', encoding = "utf-8")
USERNAMES = defaultdict(int)
COUNT = Counter()
for line in F:
    if len(line.split("\t|\t")) == 5:
        USERNAMES[line.split("\t|\t")[0]] += int(line.split("\t|\t")[3])
COUNT = Counter(USERNAMES)
print(COUNT.most_common(N))
TEXT_FILE = open(FileC, "w")
TEXT_FILE.write('\n'.join(str(d) for d in COUNT.most_common(N)))
TEXT_FILE.close()
F.close()


F = open(ResultFile_PATH, 'r', encoding = "utf-8")
USERNAMES = defaultdict(int)
COUNT = Counter()
for line in F:
    if len(line.split("\t|\t")) == 5:
        USERNAMES[line.split("\t|\t")[0]] += int(line.split("\t|\t")[4])
COUNT = Counter(USERNAMES)
print(COUNT.most_common(N))
TEXT_FILE = open(FileD, "w")
TEXT_FILE.write('\n'.join(str(d) for d in COUNT.most_common(N)))
TEXT_FILE.close()
F.close()