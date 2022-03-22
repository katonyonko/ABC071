from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="071"
#問題
problem="d"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/arc081_b".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  mod=10**9+7
  N=int(input())
  S1=input()
  S2=input()
  if S1[0]==S2[0]: ans=3
  else: ans=6
  for i in range(N-1):
    if S1[i]==S1[i+1]: continue
    if S1[i]==S2[i]: ans=(ans*2)%mod
    elif S1[i+1]!=S2[i+1]: ans=(ans*3)%mod
  print(ans)
  """ここから上にコードを記述"""

  print(test_case[__+1])