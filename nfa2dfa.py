# ε-CLOSURE(q)를 구하는 함수
def Closure(delta: list, q: list):
    result = set([])
    for i in q:
        result.add(i)
        for d in delta:
            if d[1] == i:
                result = result | set(d[-1])
    return list(result)
    
# 상태집합 T를 구하는 함수
def FindT(delta: list, q: list, a):
    for i in range(len(delta[0])):
        if delta[0][i] == a: id = i
    result = set([])
    for i in q:
        for d in delta:
            if d[1] == i:
                result = result | set(d[id])
    return list(result)

# 1. 변환할 ε-NFA 파일 입력, input 테이블로 변환
input = []
f = open('input2.txt', 'r')         # ε-NFA 입력 파일 열고 저장
lines = f.read().split('\n')
for i in range(len(lines)):
    if len(lines[i].strip()) != 0:
        input.append(lines[i].split('\t'))

for i in input:
    print(i)
        
for i in range(len(input)):         # input 테이블로 저장
    if i == 0:
        input[i][1] = 'δ'
        input[i][-1] = 'ε'
    else:
        for j in range(2, len(input[i])):
            if input[i][j] == '.':
                input[i][j] = []
            else:
                input[i][j] = list(input[i][j].split(','))
                
# 2. input 테이블 분석
F = []
for i in input:
    if '->' in i[0]: q0 = i[1]      # 시작 심볼
    if '*' in i[0]: F.append(i[1])  # 종결 심볼 집합
    
sigma = []
for s in range(2, len(input[0])-1):
    sigma.append(input[0][s])       # 시그마 집합
    
# 3. output 테이블 정의
q0_ = Closure(input, [q0])          # DFA의 시작 심볼
Q_ = []                             # DFA의 상태 집합 
output = [['', 'δ', *sigma]]
queue = [q0_]                       # 계산할 상태 집합 대기열

while True:
    i = queue.pop(0)
    Q_.append(i)
    o = ['', i]                     # 새로운 델타함수 행
    for s in sigma:
        T = FindT(input, i, s)
        c = Closure(input, T)
        o.append(c)
        if (c not in Q_) and (c != []):
            queue.append(c)
    output.append(o)
    if queue == []: break           # 더 새로운 상태가 없으면 종료
    
output[1][0] = '->'                 # 시작/종결 구분자 표시
for i in output:
    if set(i[1]) & set(F):
        i[0] += '*'

# 4. 결과 출력
print(">> input (ε-NFA)")
for i in input:                     # input 출력
    print("%-5s" %i[0], end=" ")
    for t in range(1, len(i)):
        print("%-15s" %i[t], end=" ")
    print()
print(">> output (DFA)")
for i in output:                    # ouput 출력
    print("%-5s" %i[0], end=" ")
    for t in range(1, len(i)):
        print("%-15s" %i[t], end=" ")
    print()