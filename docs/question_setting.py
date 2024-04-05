# 데이터베이스 연결 설정

def question_settings():
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
            # Delete
            sql = "DELETE FROM USER_ANSWER_TABLE"
            cursor.execute(sql)
            conn.commit()
            sql = "DELETE FROM QUESTION_ANSWER_TABLE"
            cursor.execute(sql)
            conn.commit()
            sql = "DELETE FROM SCORE_TABLE"
            cursor.execute(sql)
            conn.commit()
            sql = "DELETE FROM USER_INFO_TABLE"
            cursor.execute(sql)
            conn.commit()
            ## 주제에 대한 ID QUESTION_ANSWER_TABLE 넣기
            sql = "INSERT INTO SCORE_TABLE(SCORE_ID,SCORE) VALUES (%s, %s)"
            cursor.execute(sql, ("SCORE_ID_0", 0))
            conn.commit()
            sql = "SELECT QNA_PK_ID FROM QUESTION_ANSWER_TABLE WHERE QNA_PK_ID LIKE 'S_%';"
            cursor.execute(sql)
            subject_data = cursor.fetchall()
            subject_id = "S_{}".format(len(subject_data)+1)
            exam_number = "{}번째 시험".format(len(subject_data)+1)
            sql = "INSERT INTO QUESTION_ANSWER_TABLE(QNA_PK_ID,QNA_INFO,CHOICE_NUMBER,SCORE_ID,QNA_FK_ID) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (subject_id,exam_number,"", "SCORE_ID_0","" ))
            conn.commit()

            # 1-1 문제 수와 문항 수 입력
            question_count = int(input("문항 수를 입력하세요 : "))
            choice_count = int(input("문제 유형을 입력하세요 : "))
            print("--------------------------------")
            # Create
            for i in range(question_count):
                ## score list와 score_id list 만들기
                sql = "SELECT * FROM SCORE_TABLE"
                cursor.execute(sql)
                score_data = cursor.fetchall()
                score_dict = {}
                for j in range(len(score_data)):
                    score_dict[score_data[j][0]] = int(score_data[j][1])       
                # 1-2 : 문제 입력
                while True:
                    question = input("문항 {} : ".format(i+1))
                    sql = "SELECT * FROM QUESTION_ANSWER_TABLE WHERE QNA_PK_ID LIKE %s AND QNA_INFO = %s;"
                    cursor.execute(sql,('Q_%', question))
                    question_data = cursor.fetchall()
                    if len(question_data) == 0:
                        break
                    else:
                        ## question list내에 입력한 값이 있을 경우 다시 입력
                        print("*** 중복 문제가 있습니다. ***")


                # 1-4 : 문항들을 입력 받아 리스트 작성
                choice_list = []
                for j in range(choice_count):
                    while True:
                        ## 답항 리스트에 중복값이 있을 경우 다시 입력
                        choice_element = input("선택지 {} : ".format(j+1))
                        if choice_element not in choice_list:
                            choice_list.append(choice_element)
                            break
                        else:
                            print("*** 중복 문항이 있습니다. ***") 

                # 1-5 : 정답 입력
                while True:
                    try:
                        answer = int(input("정답 : "))
                        if answer <= choice_count:
                            break
                        else:
                            print("*** 숫자 {} 이하로 입력해주세요! ***".format(choice_count))
                    except:
                        print("*** 숫자만 입력해주세요! ***")
                # 1-6 : 점수 입력
                while True:
                    try:
                        score = int(input("점수 : "))
                        break
                    except:
                        print("*** 숫자만 입력해주세요! ***")
                
                ## score_list에 score 값이 없을 경우 score_table에 값 추가하기
                if score not in (list(score_dict.values())):
                    sql = "INSERT INTO SCORE_TABLE(SCORE_ID,SCORE) VALUES (%s, %s)"
                    cursor.execute(sql, ("SCORE_ID_{}".format(len(score_dict.values())), score))
                    conn.commit()
                    question_score_id = "SCORE_ID_{}".format(len(score_dict.values()))
                else:
                    for j in range(len(score_dict.values())):
                        if score == list(score_dict.values())[j]:
                            question_score_id = list(score_dict.keys())[j]

                # 1-3 : 입력 받은 문제와 해당 문제의 question_id를 QUESTION_ANSWER_TABLE 저장
                question_id = "Q_{}".format(i+1)
                sql = "INSERT INTO QUESTION_ANSWER_TABLE(QNA_PK_ID,QNA_INFO,CHOICE_NUMBER,SCORE_ID,QNA_FK_ID) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (question_id,question,answer, question_score_id,subject_id ))
                conn.commit()

                for j in range(len(choice_list)):
                    ## choice의 고유값 choice_id 설정
                    choice_id = "C_{}".format(i*choice_count + j+1)

                    ## 정답과 보기의 번호가 다를 경우 score_id = 'score_id_0'
                    if j+1 != answer:
                        score_id = "SCORE_ID_0"
                    ## 정답과 보기가 같을 경우 score_id = camp_score_id
                    else:
                        score_id = question_score_id
                    
                    # 1-3 : 입력 받은 문제와 해당 문제의 question_id를 QUESTION_ANSWER_TABLE 저장
                    sql = "INSERT INTO QUESTION_ANSWER_TABLE(QNA_PK_ID,QNA_INFO,CHOICE_NUMBER,SCORE_ID,QNA_FK_ID) VALUES (%s,%s,%s,%s,%s)"
                    cursor.execute(sql, (choice_id,choice_list[j],j+1,score_id,question_id))
                    conn.commit()
                print("--------------------------------")
            # 1-8 : 만들 문제 수를 충족시켰을 경우 종료
            print(" ******** 문제 입력이 끝났습니다! ********")
    finally:
        conn.close()
