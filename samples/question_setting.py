import pymysql

# 데이터베이스 연결 설정
conn = pymysql.connect(
    host='python_mysql_mysql',  # 컨테이너 이름 또는 IP
    user='cocolabhub',
    password='cocolabhub',
    db='python_mysql',  # 데이터베이스 이름
    charset='utf8mb4'
)

try:
    with conn.cursor() as cursor:
        # Delete
        sql = "DELETE FROM CHOICE_ANSWER_TABLE"
        cursor.execute(sql)
        conn.commit()
        sql = "DELETE FROM QUESTION_TABLE"
        cursor.execute(sql)
        conn.commit()
        sql = "DELETE FROM SCORE_TABLE"
        cursor.execute(sql)
        conn.commit()

        # 오답에 대한 score table에 넣기
        sql = "INSERT INTO SCORE_TABLE(SCORE_ID,SCORE) VALUES (%s, %s)"
        cursor.execute(sql, ("SCORE_ID_0", 0))
        conn.commit()

        # 문제 수와 문항 수 입력
        question_count = int(input("문항 수를 입력하세요 : "))
        choice_count = int(input("문제 유형을 입력하세요 : "))

        # Create
        for i in range(question_count):
            # score list와 score_id list 만들기
            sql = "SELECT * FROM SCORE_TABLE"
            cursor.execute(sql)
            score_data = cursor.fetchall()
            score_list = []
            score_id_list = []
            for j in range(len(score_data)):
                score_list.append(int(score_data[j][1]))
                score_id_list.append(score_data[j][0])
            
            # question table에 값 추가하기
            while True:
                question = input("문항 {} : ".format(i+1))
                sql = "SELECT * FROM QUESTION_TABLE WHERE QUESTION = %s"
                cursor.execute(sql, (question))
                data = cursor.fetchall()
                if len(data) == 0:
                    break
                else:
                    # question list내에 입력한 값이 있을 경우 다시 입력
                    print("*** 중복 문제가 있습니다. ***")

            # question_table에 추가
            question_id = "QUESTION_ID_{}".format(i+1)
            sql = "INSERT INTO QUESTION_TABLE(QUESTEION_ID,QUESTION) VALUES (%s, %s)"
            cursor.execute(sql, (question_id, question))
            conn.commit()

            # 답항 리스트 만들기
            choice_list = []
            for j in range(choice_count):
                while True:
                    # 답항 리스트에 중복값이 있을 경우 다시 입력
                    choice_element = input("선택지 {} : ".format(j+1))
                    if choice_element not in choice_list:
                        choice_list.append(choice_element)
                        break
                    else:
                        print("*** 중복 문항이 있습니다. ***") 

            # 정답 입력
            answer = int(input("정답 : "))

            # score 입력
            score = int(input("점수 : "))
            
            # score_list에 score 값이 없을 경우 score_table에 값 추가하기
            if score not in score_list:
                sql = "INSERT INTO SCORE_TABLE(SCORE_ID,SCORE) VALUES (%s, %s)"
                cursor.execute(sql, ("SCORE_ID_{}".format(len(score_list)), score))
                conn.commit()
                camp_score_id = "SCORE_ID_{}".format(len(score_list))
            else:
                for j in range(len(score_list)):
                    if score == score_list[j]:
                        camp_score_id = score_id_list[j]

            for j in range(len(choice_list)):
                # choice의 고유값 choice_id 설정
                choice_id = "CHOICE_ID_{}".format(i*choice_count + j+1)

                # 정답과 보기의 번호가 다를 경우 score_id = 'score_id_0'
                if j+1 != answer:
                    score_id = "SCORE_ID_0"
                # 정답과 보기가 같을 경우 score_id = camp_score_id
                else:
                    score_id = camp_score_id
                
                # choice_answer_table에 값 추가
                sql = "INSERT INTO CHOICE_ANSWER_TABLE(CHOICE_ID,QUESTEION_ID,SCORE_ID,CHOICE, CHOICE_NUMBER) VALUES (%s,%s,%s,%s,%s)"
                cursor.execute(sql, (choice_id,question_id,score_id, choice_list[j], j+1))
                conn.commit()
            print("--------------------------------")
finally:
    conn.close()
