'''
itertoolsの使い方
https://docs.python.org/ja/3/library/itertools.html
'''

import itertools

(a,b,c,d,e)の並び方を考える
seq = ('a','b','c','d','e')
'''
順列、階乗
(a,b,c,d,e)のすべての並べ方は5!=120通り
'''
list(itertools.permutations(seq))
'''
出力結果
[('a', 'b', 'c', 'd', 'e'),
 ('a', 'b', 'c', 'e', 'd'),
 ('a', 'b', 'd', 'c', 'e'),
 ('a', 'b', 'd', 'e', 'c'),
           中略
 ('e', 'd', 'c', 'a', 'b'),
 ('e', 'd', 'c', 'b', 'a')]
 '''
len(list(itertools.permutations(seq)))  # 120

'''
permutationsの第二引数に数値を指定するといくつ選ぶかを指定できる。
(a,b,c,d,e)から3つ選ぶとき、並べ方は5P3=60通りとなる
'''
list(itertools.permutations(seq, 3))
'''
出力結果
[('a', 'b', 'c'),
 ('a', 'b', 'd'),
 ('a', 'b', 'e'),
 ('a', 'c', 'b'),
       中略
 ('e', 'd', 'a'),
 ('e', 'd', 'b'),
 ('e', 'd', 'c')]
'''
len(list(itertools.permutations(seq, 3)))   # 60

'''
組み合わせ
(a,b,c,d,e)から5つ選ぶ組み合わせは5C5=1通り
'''
list(itertools.combinations(seq,5))
'''
出力結果
[('a','b','c','d','e')]
'''
'''
(a,b,c,d,e)から3つ選ぶ組み合わせは5C3=10通り
'''
list(itertools.combinations(seq,3))
'''
出力結果
[('a', 'b', 'c'),
 ('a', 'b', 'd'),
 ('a', 'b', 'e'),
 ('a', 'c', 'd'),
 ('a', 'c', 'e'),
 ('a', 'd', 'e'),
 ('b', 'c', 'd'),
 ('b', 'c', 'e'),
 ('b', 'd', 'e'),
 ('c', 'd', 'e')]
'''
'''
最後に直積を考える。
直積とは A={a, b, c}, B={d, e}のような2つの集合が与えられたとすると
A×B={(a,d),(a,e),(b,d),(b,e),(c,d),(c,e)}A×B={(a,d),(a,e),(b,d),(b,e),(c,d),(c,e)}
を返すような操作のこと。Aから一つ、Bから一つ要素を取り、組としている。
'''
A = ('a', 'b', 'c')
B = ('d', 'e')
C = ('f')

list(itertools.product(A, B))
'''
[('a', 'd'), ('a', 'e'), ('b', 'd'), ('b', 'e'), ('c', 'd'), ('c', 'e')]
'''

list(itertools.product(A, B, C))
'''
[('a', 'd', 'f'),
 ('a', 'e', 'f'),
 ('b', 'd', 'f'),
 ('b', 'e', 'f'),
 ('c', 'd', 'f'),
 ('c', 'e', 'f')]
 '''
