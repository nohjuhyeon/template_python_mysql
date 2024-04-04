# 문제 작성 및 응시 프로그램 만들기

<h2>파이썬 파일 개요</h2>

|구분| 파일 이름|설명|담당자|
|--|--|--|--|
|0|[questionnaires_main.py](docs/questionnaires_main.py)|메인 ||
|1|[question_setting.py](docs/question_setting.py)|문제 입력|노주현|
|2| [question_outputs.py](docs/question_outputs.py)|시험 응시|김유진|
|3| [question_ouuser_scoringtputs.py](docs/user_scoring.py) |응시자별 채점 결과|노주현|

<br>

## 역할분담
###  문제 입력 : 주현
```
- 할 일
    - 문제와 관련된 정보(문제, 답항, 점수, 정답)을 DB에 저장
``` 

### 시험 응시 : 유진
```
- 할 일 
    - 문제 리스트 출력
    - 사용자의 답 입력
    - 사용자 정보와 사용자가 입력한 답 DB에 저장
    - 사용자가 입력한 답안지 리스트 출력
```

### 응시자별 채점 결과 : 주현
```
- 할 일 
    - 응시자별 채점 결과 출력
    - 과목 평균 점수 출력
```
<br>

## 동작 순서도
### 1. 문제 입력
    1. 만들 문제 수와 문항 수를 입력
    2. 문제 입력
        - 만약에 중복 문제가 있다면 다시 입력
    3. 입력 받은 문제와 해당 문제의 question_id를 question_table에 저장
    4. 문항들을 입력 받아 리스트 작성
        - 리스트에 있는 문항을 또 입력할 경우 다시 입력
    5. 정답 입력
        - 정답이 숫자가 아니거나 문항 수보다 클 경우 다시 입력
    6. 점수 입력
        - 점수가 숫자가 아닐 경우 다시 입력
        - 점수를 score_table에서 확인하여 똑같은 점수가 있을 경우, 해당 점수의 score_id 가져오기
        - 만약에 없을 경우 새로운 score_id 생성
    7. choice_answer_table에 문항별 choice_id와 question_id, score_id, 문항, 문항 번호 저장
    8. 만들 문제 수를 충족시켰을 경우 종료.

### 2. 시험 응시
    1. 응시자 이름 입력
    2. 응시자 이름과 id user_info_table에 저장
    3. 문제와 문제에 해당하는 문항들을 DB에서 가져와서 출력
    4. 응시자가 답 입력
        - 만약에 답이 숫자가 아니거나 문항 수보다 클 경우 다시 입력
    5. 응시자가 입력한 답 user_answer_table에 저장
    6. 모든 문제를 풀었을 경우, 응시자가 입력한 답안지 출력
    7. 다음 응시자가 있는지 확인
        - 다음 응시자가 있을 경우 다시 실행
        - 다음 응시자가 없을 경우 종료.

### 3. 응시자별 점수와 전체 응시자의 평균 출력
    1. DB에서 응시자 이름과 응시자들의 문제별 점수 가져오기
    2. 응시자별 채점 결과 출력
    3. 전체 응시자의 평균 출력

<br>

## 프로젝트 결과
- ERD 다이어그램
![TOY_ERDs_diagram](https://github.com/nohjuhyeon/toy_ERDs/assets/151099474/89dec672-c1a5-47a6-a56c-618a9b0c16ce)
- DB 구성
![TOY_DATABASE구성_YJH](https://github.com/nohjuhyeon/toy_ERDs/assets/151099474/5069d6c9-e9f7-43b6-b000-405e1ecff69f)

- 프로그램 동작 영상 : https://www.youtube.com/watch?v=QAIcF4GyOG4

<br>

<h2>데이터 예시</h2>

|구분|테이블 이름|링크|구성 컬럼|
|--|--|--|--|
|1|QUESTION_TABLE|[QUESTION_TABLE](DATABASE/TOY_ERDs_QUESTION_TABLE.csv)|QUESTION_ID, QUESTION|
|2|SCORE_TABLE|[SCORE_TABLE](DATABASE/TOY_ERDs_SCORE_TABLE.csv)|SCORE_ID, SCORE|
|3|CHOICE_ANSWER_TABLE|[CHOICE_ANSWER_TABLE](DATABASE/TOY_ERDs_CHOICE_ANSWER_TABLE.csv)|CHOICE_ID, QUESTION_ID, SCORE_ID, CHOICE, CHOICE_NUMBER|
|4|USER_INFO_TABLE|[USER_INFO_TABLE](DATABASE/TOY_ERDs_USER_INFO_TABLE.csv)|USER_ID, USER_NAME|
|5|USER_ANSWER_TABLE|[USER_ANSWER_TABLE](DATABASE/TOY_ERDs_USER_ANSWER_TABLE.csv)|USER_ANSWER_ID, USER_ID, CHOICE_ID|


<br>

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


