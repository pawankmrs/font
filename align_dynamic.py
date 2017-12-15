from collections import Counter

from numpy import argmax
import numpy as np


fc = Counter()
f = [line.strip() for line in open('1March06-1-22.pdf.font.txt')]
u = [line.strip() for line in open('1March06-1-22.pdf.txt')]
len_ratio = float(len(' '.join(u))) / len(' '.join(f)) 
epsilon = 4



def unilen(u):
  if u.isdigit():
    return len(u)
  else:
    return len_ratio * len(u)

def fontlen(f):
  return len(f)

def sigma(f, u):
  return (fontlen(f) - unilen(u)) * (fontlen(f) - unilen(u))

def path(a, b):
  M = len(a)
  N = len(b)
  print(M)
  print(N)
  
  previous = np.full((M+1, N+1, 2), 0)
  scores = np.full((M+1, N+1), -0.0)
  for i in range(M+1):
    scores[i,0] = 0
  for j in range(N+1):
    scores[0, j] = 0
  for i in range(1, M+1):
    for j in range(1, N+1):
      local_scores = []
      local_scores.append( (i-1, j-1, scores[i-1][j-1] + sigma(a[i-1], b[j-1])))
      if i-2 > 0:
        local_scores.append( (i-2, j-1, scores[i-2][j-1] + sigma(''.join(a[i-2:i-1]), b[j-1])))
      if i-3 > 0:
        local_scores.append( (i-3, j-1, scores[i-2][j-1] + sigma(''.join(a[i-3:i-1]), b[j-1])))
      if j-2 > 0:
        local_scores.append( (i-1, j-2, scores[i-1][j-2] + sigma(a[i-1], ''.join(b[j-2:j-1]))))
      if j-3 > 0:
        local_scores.append( (i-1, j-3, scores[i-1][j-3] + sigma(a[i-1], ''.join(b[j-3:j-1]))))
      index = argmax([l[2] for l in local_scores])
      scores[i][j] = local_scores[index][2]
      previous[i][j][0] = local_scores[index][0]
      previous[i][j][1] = local_scores[index][1]
  pre = (M,N)
  print(scores)
  for i in range(1, M+1):
    #for j in range(1, N+1):
    print("%s %s" %(previous[i][:][0], previous[i][:][1]))
  while pre != (0,0):
    print(pre)
    pre = (previous[int(pre[0])][int(pre[1])][0], previous[int(pre[0])][int(pre[1])][1])


a = 'ÁÖß ˆ ̄ÖÃÖ3ÖÖ ̄Ö×ŸÖ : Ûéú ̄ÖμÖÖ ‡®ÖÛêú †®Öã ̄Öæ ̧üÛú  ̄ÖÏ¿®Ö ÛúÖ ˆ¢Ö ̧ü ¤üß×•Ö‹...'
b = 'श्री उपसभाषति : देखिए।...(व्यवधान)...कुछ भी अभिलिखित नहीं होगा। यह नहीं'
path(a.split(),b.split())


'''with open('1March.font','w') as src, open('1March.uni','w') as targ:
  for i,_ in enumerate(f):
    if len(f[i]) > len_ratio * len(u[i]) + epsilon:
      
    elif len(u[i]) > len(f[i]):
      
    else:
      src.write(f[i]+'\t'+u[i]+'\n')'''
