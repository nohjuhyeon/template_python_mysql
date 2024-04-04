## python_mysql
#### Main package
- java:17
- mysql:8

#### CLI with Dockerfile and compose.xml : duration 150.4s
```
# --project-name is docker container name
~$ docker-compose --project-name python_mysql up -d --build
```
#### samples
- [samples/python_mysql.py](./samples/python_mysql.py)

#### database infors
+ user='cocolabhub',
+ password='cocolabhub',
+ db='python_mysql'



### 역할분담
- 문제를 만들기 : 주현
    - 문제, 답항, 점수, 정답을 RDB에 넣기
    
- 문제 출력하기 : 유진
    - 문제, 답항 프린트
    - 사용자의 답 입력
    - 사용자의 답을 RDB에 넣기
    - 마지막에 사용자가 입력한 답안지 리스트 출력

- 응시자별 채점 결과 : 주현
    - 응시자별 채점 결과 프린트
    - 과목 평균 점수 프린트 

### 동작 순서도
1. 문제 입력
    1) 만들 문제 수와 문항 수를 입력
    2) 문제 입력
        - 만약에 중복 문제가 있다면 다시 입력
    3) 입력 받은 문제와 해당 문제의 question_id를 question_table에 저장
    4) 문항들을 입력 받아 리스트 작성
        - 리스트에 있는 문항을 또 입력할 경우 다시 입력
    5) 정답 입력
        - 정답이 숫자가 아니거나 문항 수보다 클 경우 다시 입력
    6) 점수 입력
        - 점수가 숫자가 아닐 경우 다시 입력
        - 점수를 score_table에서 확인하여 똑같은 점수가 있을 경우, 해당 점수의 score_id 가져오기
        - 만약에 없을 경우 새로운 score_id 생성
    7) choice_answer_table에 문항별 choice_id와 question_id, score_id, 문항, 문항 번호 저장
    8) 만들 문제 수를 충족시켰을 경우 종료.

2. 문제 응시
    1) 응시자 이름 입력
    2) 문제와 문제에 해당하는 문항들을 DB에서 가져와서 출력
    3) 응시자가 답 입력
        - 만약에 답이 숫자가 아니거나 문항 수보다 클 경우 다시 입력
    4) 모든 문제를 풀었을 경우, 응시자가 입력한 답안지 출력
    5) 다음 응시자가 있는지 확인
        - 다음 응시자가 있을 경우 다시 실행
        - 다음 응시자가 없을 경우 종료.

3. 응시자별 점수와 전체 응시자의 평균 출력
    1) 응시자별 채점 결과 출력
    2) 전체 응시자의 평균 출력