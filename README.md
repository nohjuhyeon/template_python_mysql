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

- 응시자별 채점 결과
    - 응시자별 채점 결과 프린트
    - 과목 평균 점수 프린트 