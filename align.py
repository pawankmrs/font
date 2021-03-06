from collections import Counter
from itertools import izip



fc = Counter()
f = [line.strip() for line in open('/home/pawan/OCR/debate/text/SummaryReport2013Hindi.pdf.font')]
u = [line.strip() for line in open('/home/pawan/OCR/debate/text/SummaryReport2013Hindi.pdf.uni')]
len_ratio = float(len(' '.join(u))) / len(' '.join(f)) 
epsilon = 4



def unilen(u):
  if u.isnumberic():
    return len(u)
  else:
    return len_ratio * len(u)

def fontlen(f):
  return len(f)

def sigma(f, u):
  return fontlen(f) - unilen(u)

def path(i1, j1, i2, j2, a, b):
  if i1 + 1 == i2 or j1 == j2:
    #write aligned pairs for maximum-score path from (i1, j1) to (i2, j2)
    if j1== j2:
      for i in range(i1, i2):
        print([a[i+1], 0])
    else: ######FIXXXXXXXXXXXX
      for 
      print()
  else:
    mid = (i1 + i2)/2
    # find maximum path scores from (i1, j1)
    SMinus[j1] = 0
    for j in range(j1 + 1, j2):#OR j2+1
      SMinus[j] = SMinus[j-1] + sigma('', b[j])
    for i in range(i1 + 1, mid):#OR mid+1
      s = SMinus[j1]
      c = SMinus[j1] + sigma(a[i], '')
      SMinus[j1] = c
      for j in range(j1+1, j2):# OR j2+1
        c = max([SMinus[j] + sigma(a[i], ''), s + sigma(a[i], b[j]), c + sigma('', b[j])])
         s = SMinus[j]
         SMinus[j] = c
    #find maximum path scores to (i 2 , j 2 )
    SPlus[j2] = 0
    for j in  list(reversed(range(j1,j2-1))):#OR j2
      SPlus[j] = SPlus[j+1] + sigma('', b[j_1])
    for i in list(reversed(range(mid, i2 -1))):#OR i2
      s = SPlus[j2]
      c = SPlus[j2] + sigma(a[i+1], '')
      SPlus[j2] = c
      for j in list(reversed(range(j1, j2 -1))):# OR j2
        c = max([SPlus[j] + sigma(a[i+1], ''), s + sigma(a[i+1], b[j+1]), c + sigma('', b[j+1])])
         s = SPlus[j]
         SPlus[j] = c
     
     # find where maximum-score path crosses row mid
     j = j1#argmax(j1, j2)
     max_val = SMinus[j1] + SPlus[j1]
     for k in range(j1, j2): # OR j2+1
      if SMinus[k]+ SPlus[k] > max_val:
        j = k
        max_val = SMinus[k]+ SPlus[k]
     # value x ∈[ j1 , j2 ] that maximizes S − [x] + S + [x]
     path(i1 , j1 , mid, j, a, b)
     path(mid, j, i2 , j2, a, b)
     
def align(a, b):
  M = len(a)
  N = len(b)
  if M =0:
    for j in range(1, N): # OR N+1
      print([0, b[j]])
  else:
    path(0, 0, M, N, a, b)

for s, t in izip(f, u):
  align(s, t)

with open('SummaryReport2013Hindi.font','w') as src, open('SummaryReport2013Hindi.uni','w') as targ:
  for i,_ in enumerate(f):
    if len(f[i]) > len_ratio * len(u[i]) + epsilon:
      
    elif len(u[i]) > len(f[i]):
      
    else:
      src.write(f[i]+'\t'+u[i]+'\n')
