from collections import Counter
cc = Counter()

with open('src.txt') as src, open('targ.txt') as targ:
 src_words = [w.strip() for w in src]
 targ_words = [w.strip() for w in targ]
 #cf = Counter(''.join(src_words))
 #cu = Counter(''.join(targ_words))
 cf = Counter()
 cu = Counter()
 cfb = Counter()
 cub = Counter()
 ccfb = Counter()
 ccft = Counter()
 ccfq = Counter()
 
 for w in src_words:
  local_cf = Counter()
  local_cfb = Counter()
  for i,c in enumerate(w):
    if local_cf[c] == 0:
      local_cf[c] = 1
      cf[c] += 1
    if i>0 and local_cfb[w[i-1:i+1]] == 0:
      local_cfb[w[i-1:i+1]] = 1
      cfb[w[i-1:i+1]] += 1
 for w in targ_words:
  local_cu = Counter()
  local_cub = Counter()
  for i,c in enumerate(w):
    if local_cu[c] == 0:
      local_cu[c] = 1
      cu[c] += 1
    if i>0 and local_cub[w[i-1:i+1]] == 0:
      local_cub[w[i-1:i+1]] = 1
      cub[w[i-1:i+1]] += 1

 for i,_ in enumerate(src_words):
  local_cc = Counter()
  local_ccfb = Counter()
  local_ccft = Counter()
  local_ccfq = Counter()
  for k,wf in enumerate(src_words[i]):
    for wu in targ_words[i]:
      if local_cc[(wf, wu)] == 0:
        local_cc[(wf, wu)] += 1
        cc[(wf, wu)] += 1
      if k>0 and local_ccfb[(src_words[i][k-1:k+1], wu)] == 0:
        local_ccfb[(src_words[i][k-1:k+1], wu)] += 1
        ccfb[(src_words[i][k-1:k+1], wu)] += 1
      if k>1 and local_ccft[(src_words[i][k-2:k+1], wu)] == 0:
        local_ccft[(src_words[i][k-2:k+1], wu)] += 1
        ccft[(src_words[i][k-2:k+1], wu)] += 1
      if k>2 and local_ccfq[(src_words[i][k-3:k+1], wu)] == 0:
        local_ccfq[(src_words[i][k-3:k+1], wu)] += 1
        ccfq[(src_words[i][k-3:k+1], wu)] += 1
with open('co_occur.txt','w') as c:
  c.write(str(cc))
  
with open('countFont.txt','w') as ffile:
  ffile.write(str(cf))
  
with open('countUnicode.txt','w') as ufile:
  ufile.write(str(cu))
  
with open('co_occur_src_bi.txt','w') as fbfile:
  fbfile.write(str(ccfb))

with open('co_occur_src_tri.txt','w') as ftfile:
  ftfile.write(str(ccft))
  
with open('co_occur_src_q.txt','w') as fqfile:
  fqfile.write(str(ccfq))
    

for k in cc:
  '''print(k[0])
  print(k[1])
  print(cc[k])
  if cf[k[0]]:
    print(cc[k]/cf[k[0]])
  if cf[k[1]]:
    print(cc[k]/cf[k[1]])
  if cf[k[0]] and cf[k[1]] :
    if cc[k]/cf[k[0]] > 0.5 and cc[k]/cf[k[1]] > 0.5:
      print(k)
      print(cc[k]/cf[k[0]] * cc[k]/cf[k[1]])'''

with open('unigrams.txt', 'w') as uni:
  for b in cc:
    ratio  = cc[b] / cc[(b[0][0], b[1])]
    ratio2  = cc[b] / cu[( b[1])]
    if ratio2 > .70:#ratio > 0.95 and 
      uni.write(str(b)+'\n')
      uni.write(str((b[0][0], b[1]))+'\n')
      uni.write(str(cc[b])+'\n')
      uni.write(str(ratio)+'\n')


with open('bigrams.txt', 'w') as bi:
  for b in ccfb:
    ratio  = ccfb[b] / cc[(b[0][0], b[1])]
    ratio2  = ccfb[b] / cu[( b[1])]
    if ratio2 > .70:#ratio > 0.95 and 
      bi.write(str(b)+'\n')
      bi.write(str((b[0][0], b[1]))+'\n')
      bi.write(str(ccfb[b])+'\n')
      bi.write(str(ratio)+'\n')

with open('trigrams.txt', 'w') as tri:
  for b in ccft:
    ratio  = ccft[b] / ccfb[(b[0][0:-1], b[1])]
    ratio1  = ccft[b] / ccfb[(b[0][1:], b[1])]
    ratio2  = ccft[b] / cu[( b[1])]
    if ratio > 0.99 and ratio1 > 0.99 and ratio2 > .90:
      tri.write(str(b)+'\n')
      tri.write(str((b[0][0:-1], b[1]))+'\n')
      tri.write(str(ccft[b])+'\n')
      tri.write(str(ratio)+'\n')

