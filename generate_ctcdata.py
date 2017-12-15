from collections import Counter
fc = Counter()
f = [line.strip() for line in open('1March06-train.font')]
u = [line.strip() for line in open('1March06-train.uni')]


with open('train.txt','w') as src:
  for i,l in enumerate(f):
      src.write(f[i]+'\t'+u[i]+'\n')
