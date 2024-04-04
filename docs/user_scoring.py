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
            sql = "select USER_INFO_TABLE.USER_NAME, SCORE_TABLE.SCORE FROM USER_ANSWER_TABLE INNER JOIN CHOICE_ANSWER_TABLE ON CHOICE_ANSWER_TABLE.CHOICE_ID = USER_ANSWER_TABLE.CHOICE_ID INNER JOIN SCORE_TABLE ON SCORE_TABLE.SCORE_ID = CHOICE_ANSWER_TABLE.SCORE_ID INNER JOIN USER_INFO_TABLE ON USER_INFO_TABLE.USER_ID = USER_ANSWER_TABLE.USER_ID"
            cursor.execute(sql)
            user_info_data = cursor.fetchall()
            user_score_dict = {}
            for row in user_info_data:
                if row[0] not in user_score_dict.keys():
                    user_score_dict[row[0]] = int(row[1])
                else:
                    user_score_dict[row[0]] += int(row[1])
            print("------------------------------")
            # 3-2 : 응시자별 채점 결과 출력
            print("응시자별 채점 결과")
            total_score = 0
            for user_name in list(user_score_dict.keys()):
                print("{} : {}점".format(user_name,user_score_dict[user_name]))
                total_score += user_score_dict[user_name]
            print("")
            # 3-3 : 전체 응시자의 평균 출력
            print("과목 평균 점수")     
            print(" {}점".format(total_score/len(user_score_dict)))     

    finally:
        conn.close()
