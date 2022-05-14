# nfa2dfa
<b>1. 변환할 ε-NFA 파일 입력, input 테이블로 변환</b>
<br/>ε-NFA의 상태 전이표를 txt 파일로 저장하고 이를 프로그램 내에서 불러온다. 상태 전이표의 행은 ‘\n’으로 구분하고, 열은 ‘\t’로 구분한다. 또한 공집합은 ‘.’로 표시한다.<br/><br/>
<b>2. input 테이블 분석</b>
<br/>input 테이블의 첫 번째 열은 시작/종결 구분자이다. 구분자가 ‘->’이라면 시작 심볼이고, ‘*’이라면 종결 심볼이다. 테이블의 열의 개수를 N이라고 했을 때, 첫 번째 행에서 세 번째 열부터 N-1번째 열까지는 시그마 집합이고, 마지막 N번째 열은 ε-CLOSURE이다.<br/><br/>
<b>3. output 테이블 정의</b>
<br/>변환되는 DFA의 시작 심볼 q0_은 ε-CLOSURE(q0)이다. 여기서 Q_는 DFA의 상태 집합이 되고, queue는 새로 만들어져서 계산을 기다리는 상태 집합의 대기열이 된다. 대기열에 있는 집합부터 차례로 각 시그마에 대한 ε-CLOSURE를 구하고 새로운 상태 집합이 있다면 대기열에 추가하며 이를 반복한다. 대기열이 비었다면 더 이상 새로운 상태 집합이 없다는 것이므로 반복을 중단한다. 마지막으로 output 테이블에 대한 시작/종결 구분자를 표시한다.<br/><br/>
<b>4. 결과 출력<br/></b>
4-1. input1.txt
<br/>![image](https://user-images.githubusercontent.com/82702064/168448460-f67e7517-205d-4136-81e1-0b34b0072423.png)
![image](https://user-images.githubusercontent.com/82702064/168448465-635fe792-d273-40aa-8d9f-4e0bd7f0da94.png)
<br/><br/>4-2. input2.txt
<br/>![image](https://user-images.githubusercontent.com/82702064/168448469-882fdd5e-9fc0-4687-bfc4-3977f0462b36.png)
![image](https://user-images.githubusercontent.com/82702064/168448475-92604848-76a1-4c0b-8473-57104103ccad.png)
