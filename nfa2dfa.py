# ε-NFA := M = (Q, Σ(sigma), δ(delta), q0, F)
# DFA := M' = (Q', Σ(sigma), δ(delta)', q0', F')
# 
# input => ε-NFA = [[δ, a, b, c, ε],
#                   [->1, [2], [], [], [1,3,4]],
#                   [2, [], [4], [], [2]],
#                   [3, [], [], [3], [3,4]],
#                   [*4, [], [], [], [4]]]
# output => DFA = [[δ, a, b, c],
#                  [->*[1,3,4], [2], [], [3,4]],
#                  [[2], [], [4], []],
#                  [*[3,4], [], [], [3,4]],
#                  [*[4], [], [], []]]
# 
# -> := start symbol, * := finite symbol
# input is (len(Q)+1)x(len(sigma)+3) matrix
# output is (len(Q')+1)x(len(sigma)+2) matrix
#            δ          a          b          c          ε->         1          ['2']      []         []         ['1', '3', '4']
#            2          []         ['4']      []         ['2']
#            3          []         []         ['3']      ['3', '4']
# *          4          []         []         []         ['4']

#            δ          a          b          c
# ->*        [1, 3, 4]  [2]        []         [3, 4]
#            [2]        []         [4]        []
# *          [3, 4]     []         []         [3, 4]
# *          [4]        []         []         []


delta1 = [['', 'δ', 'a', 'b', 'c', 'ε'],
        ['->', '1', ['2'], [], [], ['1','3','4']],
        ['', '2', [], ['4'], [], ['2']],
        ['', '3', [], [], ['3'], ['3','4']],
        ['*', '4', [], [], [], ['4']]]

delta2 = [['', 'δ', 'a', 'b', 'c'],
        ['->*', [1,3,4], [2], [], [3,4]],
        ['', [2], [], [4], []],
        ['*', [3,4], [], [], [3,4]],
        ['*', [4], [], [], []]]

for d in delta1:
    for t in d:
        print("%-10s" %t, end=" ")
    print()
    
print()
for d in delta2:
    for t in d:
        print("%-10s" %t, end=" ")
    print()