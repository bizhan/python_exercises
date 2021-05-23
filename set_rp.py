#It can only contains Unique values

def count_unique(s):
  '''
  Count number of unique characters in s
  >>> count_unique("aabb")
  2
  >>> count_unique("abcdef")
  6
  '''
  seen_c = []
  for c in s:
    if c not in seen_c:
      seen_c.append(c)
  return len(seen_c)

