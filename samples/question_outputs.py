import pymysql

# 데이터베이스 연결 설정
conn = pymysql.connect(
    host='python_mysql_mysql',  # 컨테이너 이름 또는 IP
    user='cocolabhub',
    password='cocolabhub',
    db='python_mysql',  # 데이터베이스 이름
    charset='utf8mb4'
)

# 문제, 답항 프린트
try:
    with conn.cursor() as cursor:
        
    question_id = "QUESTION_ID_{}".format(i+1)
    sql = "INSERT INTO QUESTION_TABLE(QUESTEION_ID,QUESTION) VALUES (%s, %s)"
    cursor.execute(sql, (question_id, question))
    conn.commit()
# 사용자의 답 입력
# 사용자가 입력한 답안지 리스트 출력