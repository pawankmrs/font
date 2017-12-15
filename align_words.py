from collections import Counter
fc = Counter()
f = [line.strip() for line in open('1March06-1-22.pdf.font.txt')]
u = [line.strip() for line in open('1March06-1-22.pdf.txt')]
len_ratio = 1.49
epsilon = 4

with open('1March.font','w') as src, open('1March.uni','w') as targ:
  for i,_ in enumerate(f):
    if len(f[i]) > len(u[i]):
      
    elif len(u[i]) > len(f[i]):
      
    else:
      src.write(f[i]+'\t'+u[i]+'\n')
