# 데이터베이스 연결 설정

def user_scoring():
    import pymysql
    conn = pymysql.connect(
    host='python_mysql_mysql',  # 컨테이너 이름 또는 IP
    user='cocolabhub',
    password='cocolabhub',
    db='python_mysql',  # 데이터베이스 이름
    charset='utf8mb4'
    )
    try:
        with conn.cursor() as cursor:
            # 3-1 : DB에서 응시자 이름과 응시자들의 문제별 점수 가져오기
            sql = "SELECT USER_SCORE.USER_ID, USER_SCORE.USER_NAME, SUM(USER_SCORE.SCORE) FROM(select USER_ANSWER_TABLE.USER_ID, USER_INFO_TABLE.USER_NAME, SCORE_TABLE.SCORE FROM USER_ANSWER_TABLE INNER JOIN QUESTION_ANSWER_TABLE ON QUESTION_ANSWER_TABLE.QNA_PK_ID = USER_ANSWER_TABLE.QNA_FK_ID INNER JOIN SCORE_TABLE ON SCORE_TABLE.SCORE_ID = QUESTION_ANSWER_TABLE.SCORE_ID INNER JOIN USER_INFO_TABLE ON USER_INFO_TABLE.USER_ID = USER_ANSWER_TABLE.USER_ID) AS USER_SCORE GROUP BY USER_SCORE.USER_ID"
            cursor.execute(sql)
            user_score_data = cursor.fetchall()
            print("------------------------------")
            # 3-2 : 응시자별 채점 결과 출력
            print("응시자별 채점 결과")
            total_score = 0
            for user_score in list(user_score_data):
                print("{} : {}점".format(user_score[1],user_score[2]))
                total_score += user_score[2]
            print("")
            # 3-3 : 전체 응시자의 평균 출력
            print("과목 평균 점수")     
            print(" {}점".format(total_score/len(user_score_data)))     

    finally:
        conn.close()
