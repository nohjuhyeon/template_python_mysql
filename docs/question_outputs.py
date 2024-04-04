# 데이터베이스 연결 설정

def question_outputs():
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
            while True:
                sql = "SELECT USER_ID FROM USER_INFO_TABLE"
                cursor.execute(sql)
                user_data = cursor.fetchall()
                # 2-1 : 응시자 이름 입력
                user_name = input("응시자 이름 : ")
                # 2-2 : 응시자 이름과 id user_info_table에 저장
                user_id = "USER_ID_{}".format(len(user_data)+1)
                sql = "INSERT INTO USER_INFO_TABLE (USER_ID,USER_NAME) VALUES (%s, %s)"
                cursor.execute(sql, (user_id,user_name))
                conn.commit()
                sql = "SELECT * FROM QUESTION_TABLE"
                cursor.execute(sql)
                question_data = cursor.fetchall()

                user_pick_list = []
                for i in range(len(question_data)):
                    # 2-3 : 문제와 문제에 해당하는 문항들을 DB에서 가져와서 출력
                    print("문제 {} : {}".format(i+1,question_data[i][1]))  # 각 행 출력
                    sql = "SELECT * FROM CHOICE_ANSWER_TABLE WHERE QUESTION_ID = %s"
                    cursor.execute(sql,question_data[i][0])
                    choice_data = cursor.fetchall()
                    choice_dict = {}
                    for j in range(len(choice_data)):
                        choice_dict[choice_data[j][4]] = choice_data[j][3]

                    for j in range(len(choice_dict)):
                        print("{}. {}".format(j+1,choice_dict[str(j+1)]))
                    # 2-4 : 응시자가 답 입력
                    while True:
                        ## 만약에 답이 숫자가 아니거나 문항 수보다 클 경우 다시 입력
                        try:
                            user_pick = int(input("답 : "))
                            if user_pick <= len(choice_data):
                                break
                            else:
                                print("*** 숫자 {} 이하로 입력해주세요! ***".format(len(choice_data)))
                        except:
                            print("*** 숫자만 입력해주세요! ***")

                    user_pick_list.append(user_pick)
                    sql = "SELECT * FROM CHOICE_ANSWER_TABLE WHERE QUESTION_ID = %s AND CHOICE_NUMBER = %s"
                    cursor.execute(sql,(question_data[i][0],user_pick))
                    user_pick_data = cursor.fetchall()
                    user_choice_id = user_pick_data[0][0]
                    sql = "SELECT USER_ID FROM USER_ANSWER_TABLE"
                    cursor.execute(sql)
                    user_answer_data = cursor.fetchall()
                    user_answer_id = "USER_ANSWER_ID_{}".format(len(user_answer_data)+1)
                    # 2-5 : 응시자가 입력한 답 user_answer_table에 저장
                    sql = "INSERT INTO USER_ANSWER_TABLE (USER_ANSWER_ID, USER_ID,CHOICE_ID) VALUES (%s, %s, %s)"
                    cursor.execute(sql, (user_answer_id, user_id,user_choice_id))
                    conn.commit()
                    print("----------------------------")
                print("***** 시험이 종료되었습니다! *****")
                # 2-6 : 모든 문제를 풀었을 경우, 응시자가 입력한 답안지 출력
                print("{} 님이 푼 답안지".format(user_name))
                for i in range(len(user_pick_list)):
                    print("{}번 문제 답 : {}".format(i+1, user_pick_list[i]))
                # 2-7 : 다음 응시자가 있는지 확인
                while True:
                    continue_check = input("다음 응시자가 있나요? (계속 : c, 종료 : x) : ").lower()
                    if continue_check not in ['c','x']:
                        print('*** "c"나 "x"를 입력해주세요! ***')
                        pass
                    else:
                        break
                if continue_check == 'x':
                    break
    finally:
        conn.close
question_outputs()