import time
from collections import Counter

class Member:   # Member 클래스 생성
    def __init__(self): # 속성 정의 (입력값 없이 모두 디폴트값으로 정의됨)
        self.ID = "default"       # ID
        self.PW = "default"       # 비밀번호
        self.intro = ""           # 한줄 소개
        self.RP = 0               # RP (Reading Point)
        self.level = rank_list[0] # 레벨 (rank_list의 제일 낮은 레벨)
        self.prefer = "없음"      # 관심 태그
        self.my_timeline = []     # 나의 타임라인 (내가 직접 작성한 글만 저장됨)
        self.my_tags = []         # 나의 태그 리스트 (내가 사용한 모든 태그가 저장됨)
        self.my_tags_sort = []    # 많이 사용된 태그순으로 정렬된 리스트 -> Counter(나의 태그 리스트).most_common()
        self.like_post_list = []  # 내가 좋아요 누른 게시글들

    def show_profile(self): # 프로필 보기
        self.tag_prefer() # 프로필을 불러오기 전에 관심 태그 업데이트
        print("\n***************프로필 조회****************")
        print("[%s]님 (%s)\n"%(self.ID, self.level))         # 아이디, 레벨
        print("\"",self.intro,"\"\n")                        # 한줄 소개
        print("★ RP: %d"%(self.RP))                         # RP
        print("★ 관심 태그:",self.prefer)                   # 관심 태그 (최대 3개)
        print("******************************************")

    def join_member(self): # 회원 가입
        print("\n회원가입\n")
        ID = input("▷ 아이디:")
        ID_list = [member.ID for member in Member_list]
        while ID in ID_list:
            print("\n(!) 중복되는 아이디입니다. 다른 아이디를 사용하세요")
            ID = input("▷ 아이디:")
        PW = input("▷ 비밀번호:")
        intro = input("▷ 한줄 소개:")
        while len(intro) > 25:
            print("\n한줄 소개는 공백 포함 25자까지 입력 가능합니다")
            intro = input("▷ 한줄 소개:")
        self.ID = ID # "default"였던 ID 속성에 입력 값 저장
        self.PW = PW # "default"였던 PW 속성에 입력 값 저장
        if intro == "": self.intro = "(소개가 없습니다.)" # 한줄 소개에 입력값이 없을 경우
        else: self.intro = intro
        print("\n◎ 회원가입 완료! ◎\n")

    def log_in(): # 로그인
        find_num = 0 # 검사 횟수
        print("\n로그인\n")
        ID = input("▶ 아이디:")
        PW = input("▶ 비밀번호:")
        for member in Member_list: # 회원들이 저장된 Member_list 검사
            if [ID,PW] == [member.ID,member.PW]: # 검사 중 ID와 PW가 일치하면
                print("\n◎ 로그인 완료! ◎")     # 해당 member로 로그인 성공
                login_page(member)               # 로그인 페이지로 이동
            else: find_num += 1 # ID와 PW가 일치하지 않으면 find_num 1 증가
        # 모든 검사가 끝날 때 까지 ID와 PW가 일치하지 않으면
        if find_num == len(Member_list): # 즉, find_num==len(Member_list) 일 경우
            print("\n(!) 아이디 또는 비밀번호가 일치하지 않습니다.\n")
            login_initial_option() # {1.로그인하기 2.처음으로} 메뉴 출력

    def change_intro(self): # 한줄 소개 변경
        print("\n한줄 소개 변경\n")
        intro = input("▶ 한줄 소개:")
        while len(intro) > 25:
            intro = input("한줄 소개는 공백 포함 25자까지 입력 가능합니다:")
        self.intro = intro
        print("\n◎ 한줄 소개 변경 완료! ◎\n")

    def member_search(login_member): # 사용자 검색
        find_num = 0 # 검사 횟수
        print("사용자 검색\n")
        search_ID = input("▶ 검색할 ID:")
        for member in Member_list: # 회원들이 저장된 Member_list 검사
            if search_ID == member.ID: # 검사 중 ID가 일치하면
                member.show_profile()  # 해당 member 프로필 출력
                print("\n1. 다시검색 2. 돌아가기 3. 게시글 조회하기\n") # 프로필 출력 후의 메뉴
                option = input("→ 옵션을 선택하세요:")
                while option!="1" and option!="2" and option!="3": # 입력 예외처리
                    option = input("\n(!) 1 ~ 3 에서만 선택하세요:")
                if option == "1": # 다시검색
                    clear() # cmd창을 클리어 해주는 함수 (옵션값 들어올 때 마다 사용)
                    Member.member_search(login_member) # member_search 함수 다시 실행
                elif option == "2": # 돌아가기
                    clear()
                    login_page(login_member) # 로그인한 페이지로 돌아가기
                elif option == "3": # 게시글 조회하기
                    if len(member.my_timeline) == 0: print("\n게시글이 없습니다.\n")
                    else: # 검색한 회원이 작성한 글들을 출력
                        for post in member.my_timeline:
                            post.show_post()
                    back_logout_option(login_member) # {1. 돌아가기 2. 로그아웃} 메뉴 출력
            else: find_num += 1 # ID 일치하지 않으면 find_num 1 증가
        if find_num == len(Member_list): # 모든 검사가 끝날때까지 일치하는 ID가 없는 경우
            print("\n(!) 존재하지 않는 ID입니다.")
            print("\n1. 다시검색 2. 돌아가기\n")
            option = input("→ 옵션을 선택하세요:")
            while option!="1" and option!="2":
                option = input("\n(!) 1 ~ 2 에서만 선택하세요:")
            if option == "1": # 다시검색
                clear()
                Member.member_search(login_member)
            elif option == "2": # 돌아가기
                clear()
                login_page(login_member)

    def tag_prefer(self): # 관심 태그 업데이트
        # 나의 태그 리스트를 많이 사용된 태그 순으로 정렬
        self.my_tags_sort = Counter(self.my_tags).most_common()
        if len(self.my_tags_sort) == 0: # 총 태그가 0개인 경우
            self.prefer = "없음"   # "없음"으로 설정된 관심 태그를 그대로 유지
        elif len(self.my_tags_sort) < 3: # 총 태그가 3개보다 작은 경우
            self.prefer = "" # "없음"으로 설정된 관심 태그를 공백으로 변경 후
            for i in range (len(self.my_tags_sort)): # 총 태그 개수만큼 반복하여
                # 관심 태그 문자열에 하나씩 태그를 더해준다.
                self.prefer = self.prefer + self.my_tags_sort[i][0] +" "
        else:                  # 총 태그가 3개 이상인 경우
            self.prefer = ""   # "없음"으로 설정된 관심 태그를 공백으로 변경 후
            for i in range(3): # 정렬된 태그 리스트 중 앞의 3개만 관심 태그 문자열에 더해준다.
                self.prefer = self.prefer + self.my_tags_sort[i][0] +" "

    def rank(self): # 랭크 업데이트
        if self.RP < 10: self.level = rank_list[0]    # RP 0~9   -> 도서관 뉴비
        elif self.RP < 20: self.level = rank_list[1]  # RP 10~19 -> 도서관 라이트유저
        elif self.RP < 30: self.level = rank_list[2]  # RP 20~29 -> 도서관 애용자
        elif self.RP < 40: self.level = rank_list[3]  # RP 30~39 -> 도서관 은둔고수
        else: self.level = rank_list[4]               # RP 40~   -> 도서관 고인물

    def delete_my_timeline(self): # 게시글 삭제
        if len(self.my_timeline) == 0: # 내가 작성한 글이 0개 일 때
            print("게시글이 없습니다.\n")
        else:
            cnt = 1 # 게시글 번호 (1부터 시작, 하나씩 증가)
            for post in self.my_timeline:
                print("\n",cnt,"번 게시글")
                cnt += 1
                post.show_post() # 게시글 번호와 함께 나의 타임라인의 모든 글 출력
            num = input("→ 삭제할 게시글의 번호를 입력하세요:")
            num_list = [str(i+1) for i in range(len(self.my_timeline))]
            while num not in num_list: # 게시글 번호 외 값이 들어올 때
                num = input("\n(!) 게시글 번호 내에서 입력해주세요:")
            for post_info in Timeline:
                if post_info[1] is self.my_timeline[int(num)-1]:
                    Timeline.remove(post_info) # 전체 타임라인에서도 삭제할 글과 같은 글 삭제
                    break
            self.RP -= self.my_timeline[int(num)-1].thumbs_up # 삭제된 글의 좋아요 수만큼 RP 차감
            for tag in self.my_timeline[int(num)-1].tag_list:
                self.my_tags.remove(tag) # 나의 태그 리스트에서 삭제된 글의 태그 삭제
            self.tag_prefer() # 나의 태그 목록에 변화가 생겼으므로 관심 태그 업데이트
            del self.my_timeline[int(num)-1] # 내가 작성한 글 목록에서 해당 글 삭제
            self.RP -= 10 # 글을 작성했을 때 받은 10 RP 차감
            self.rank()   # RP 변화가 생겼으므로 랭크 업데이트
            print("\n해당 게시글이 삭제되었습니다.")

class Post:     # Post 클래스 생성
    def __init__(self, writer, post, tag_list): # 속성 정의 (작성자 객체, 글 내용, 태그 리스트 전달)
        self.writer = writer                # 작성자 (Member 클래스 인스턴스)
        self.writer_ID = writer.ID          # 작성자 ID
        self.writer_level = writer.level    # 작성자 레벨
        # 객체가 생성될 때의 시간을 게시 시간으로 저장
        self.upload_time = time.strftime("%Y-%m-%d(%X)",time.localtime(time.time()))
        self.post = post                    # 글 내용
        self.tag_list = tag_list            # 태그 리스트
        self.thumbs_up = 0                  # 좋아요 수
        self.comment_num = 0                # 댓글 수
        self.comment_list = []              # 댓글 리스트

    def input_post(): # 글 작성
        print("▶ 내용 입력(엔터 2번 입력시 입력종료):")
        post = "" # 글 내용
        while True: # -> 여러줄 입력을 받기 위해 while문 사용
            input_post = input()
            if input_post == "": # 엔터 2번 입력시
                break            # 입력 중지
            else:
                post = post + "\n" + input_post # 입력값을 줄바꿈과 함께 글 내용에 추가
        tags = input("▶ 태그할 항목(# 후 띄어쓰기):")
        tag_list = tags.split() # 띄어쓰기로 태그를 구분해 태그 리스트 생성
        return_info = [post,tag_list]
        return return_info # 글 내용과 태그 리스트를 리턴함

    def show_post(self): # 글 출력
        print("〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓")
        print("%s [%s]\t%s"%(self.writer_ID,self.writer_level,self.upload_time))
        print(self.post,"\n")
        for tag in self.tag_list:
            print(tag,end=" ")
        print("\n\n♥ 좋아요:%d\t⊙ 댓글:%d"%(self.thumbs_up,self.comment_num))
        print("\n<댓글>")
        if len(self.comment_list)>0: # 해당 글에 댓글이 있는 경우
            for comment_info in self.comment_list: # 댓글 리스트 출력
                print(comment_info[0],": ",comment_info[1]) # (댓글 작성자): (댓글 내용)
        print("〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓")

    def thumb_up(self): # 좋아요 누르기
        self.thumbs_up += 1 # 해당 글의 좋아요수 +1
        self.writer.RP += 1 # 해당 글의 작성자의 RP +1
        self.writer.rank()  # 작성자의 RP에 변화가 생겼으므로 작성자의 랭크 업데이트

    def add_comment(self, login_member): # 댓글 쓰기 (로그인한 회원 객체를 받음)
        comment = input("\n▶ 댓글 입력:")
        # 로그인한 회원의 ID와 댓글 내용을 리스트로 묶어서 해당 글의 댓글 리스트에 추가
        self.comment_list.append([login_member.ID,comment])
        self.comment_num += 1 # 해당 글의 댓글 수 +1

    def tag_search(login_member): # 태그 검색
        find_num = 0 # 검사 횟수
        print("태그 검색\n")
        search_tag = "#"+input("▶ 검색할 태그(# 없이 검색):")
        for post in Timeline: # 전체 타임라인 검사
            if search_tag in post[1].tag_list: # 검색 태그가 타임라인 속 게시글의 태그 리스트에 있으면
                post[1].show_post()            # 해당 글 출력
            else: find_num += 1 # 검색 태그가 태그 리스트에 없는 경우 검사 횟수 +1
        if find_num == len(Timeline): # 검사가 끝날때까지 검색 태그가 태그 리스트에 없는 경우
            print("\n검색 결과가 없습니다.")
        print("\n1. 다시검색 2. 돌아가기\n")
        option = input("→ 옵션을 선택하세요:")
        while option!="1" and option!="2":
            option = input("\n(!) 1 ~ 2 에서만 선택하세요:")
        if option == "1": # 다시검색
            clear()
            Post.tag_search(login_member) # 태그 검색 함수를 다시 실행한다
        elif option == "2": # 돌아가기
            clear()
            login_page(login_member)


import os # clear 함수를 사용하기 위해 import

def clear(): # cmd창을 클리어 해주는 함수
    os.system('cls')

def show_Timeline(): # 전체 타임라인 글 출력
    # [게시시간, Post 객체]가 저장된 타임라인 리스트를 게시시간이 늦은 순으로 정렬한다
    sorted_Timeline = sorted(Timeline, key=lambda x: x[0], reverse=True)
    for post_info in sorted_Timeline:
        post_info[1].show_post() # 타임라인 속 글들을 출력한다

def thumb_option_Timeline(login_member): # 좋아요를 누를 글 고르기
    cnt = 1 # 게시글 번호 (1부터 시작, 하나씩 증가)
    sorted_Timeline = sorted(Timeline, key=lambda x: x[0], reverse=True) # 타임라인의 글을 최신순으로 정렬
    for post_info in sorted_Timeline:
        print("\n",cnt,"번 게시글")
        cnt += 1
        post_info[1].show_post() # 정렬된 타임라인 속 글을 게시글 번호와 함께 출력
    num = input("→ 좋아요를 누를 게시글의 번호를 입력하세요:")
    num_list = [str(i+1) for i in range(len(sorted_Timeline))] # 게시글 번호들이 문자열로 저장된 리스트
    while num not in num_list: # 입력 예외처리
        num = input("\n(!) 게시글 번호 내에서 입력해주세요:")
    if sorted_Timeline[int(num)-1][1] in login_member.like_post_list: # 좋아요 누르려는 게시글이
        print("\n(!) 이미 좋아요를 누른 게시글입니다.") # 내가 좋아요 누른 게시글 목록에 포함된 경우
    else:
        sorted_Timeline[int(num)-1][1].thumb_up() # 선택된 글에 좋아요 누르기
        login_member.like_post_list.append(sorted_Timeline[int(num)-1][1]) # 내가 좋아요 누른 게시글 목록에 추가
        print("\n♥ 좋아요 누르기 성공! ♥")
    print("\n1. 돌아가기 2. 로그아웃 3. 좋아요 누르기\n")
    option = input("→ 옵션을 선택하세요:")
    while option!="1" and option!="2" and option!="3":
        option = input("\n(!) 1 ~ 3 에서만 선택하세요:")
    if option == "1": # 돌아가기
        clear()
        login_page(login_member)
    elif option == "2": # 로그아웃
        clear()
        initial_page()
    elif option == "3": # 좋아요 누르기
        clear()
        thumb_option_Timeline(login_member) # 좋아요를 누를 글 고르기 함수를 다시 실행한다

def add_comment_Timeline(login_member): # 댓글을 쓸 글 고리기
    cnt = 1 # 게시글 번호 (1부터 시작, 하나씩 증가)
    sorted_Timeline = sorted(Timeline, key=lambda x: x[0], reverse=True) # 타임라인의 글을 최신순으로 정렬
    for post_info in sorted_Timeline:
        print("\n",cnt,"번 게시글")
        cnt += 1
        post_info[1].show_post() # 정렬된 타임라인 속 글을 게시글 번호와 함께 출력
    num = input("→ 댓글을 쓸 게시글의 번호를 입력하세요:")
    num_list = [str(i+1) for i in range(len(sorted_Timeline))]
    while num not in num_list:  # 입력 예외처리
        num = input("\n(!) 게시글 번호 내에서 입력해주세요:")
    sorted_Timeline[int(num)-1][1].add_comment(login_member) # 선택된 글의 댓글 쓰기 함수 실행
    print("\n⊙ 댓글 작성 완료! ⊙")
    print("\n1. 돌아가기 2. 로그아웃 3. 댓글 쓰기\n")
    option = input("→ 옵션을 선택하세요:")
    while option!="1" and option!="2" and option!="3":
        option = input("\n(!) 1 ~ 3 에서만 선택하세요:")
    if option == "1": # 돌아가기
        clear()
        login_page(login_member)
    elif option == "2": # 로그아웃
        clear()
        initial_page()
    elif option == "3": # 댓글 쓰기
        clear()
        add_comment_Timeline(login_member) # 댓글을 쓸 글 고르기 함수를 다시 실행한다.

def back_logout_option(login_member): # {1. 돌아가기 2. 로그아웃} 메뉴
    print("1. 돌아가기 2. 로그아웃\n")
    option = input("→ 옵션을 선택하세요:")
    while option!="1" and option!="2":
        option = input("\n(!) 1 ~ 2 에서만 선택하세요:")
    if option == "1": # 돌아가기
        clear()
        login_page(login_member) # login_member객체로 로그인된 화면 실행
    elif option == "2": # 로그아웃
        clear()
        initial_page() # 초기화면 실행

def login_initial_option(): # {1. 로그인하기 2. 처음으로} 메뉴
    print("1. 로그인하기 2. 처음으로\n")
    option = input("→ 옵션을 선택하세요:")
    while option!="1" and option!="2":
        option = input("\n(!) 1 ~ 2 에서만 선택하세요:")
    if option == "1": # 로그인하기
        clear()
        Member.log_in() # Member 클래스의 로그인 함수 실행
    elif option == "2": # 처음으로
        clear()
        initial_page() # 초기화면 실행


def initial_page(): # 초기화면
    print("\n◈ 안녕하세요, [중앙도서관 리더즈SNS]입니다. ◈\n")
    print("1. 로그인\n2. 회원가입\n3. 비회원\n4. 회원목록\n5. 종료\n")
    option = input("→ 옵션을 선택하세요:")
    while option not in ["1","2","3","4","5"]:
        option = input("\n(!) 1 ~ 5 에서만 선택하세요:")

    if option == "1": # 로그인
        clear()
        Member.log_in()

    elif option == "2": # 회원가입
        clear()
        new_member = Member()            # Member 객체 새로 생성
        new_member.join_member()         # 생성된 객체로 회원가입 함수 실행
        Member_list.append(new_member)   # Member_list에 생성된 객체 추가
        login_initial_option()

    elif option == "3": # 비회원
        clear()
        print("▷ 비회원으로 열람중 ◁\n") # 비회원은 타임라인 글만 열람 가능하다
        if len(Timeline) == 0: # 타임라인에 게시글이 없는 경우
            print("\n게시글이 없습니다.\n")
            login_initial_option()
        else:
            show_Timeline() # 전체 타임라인 글 출력
            login_initial_option()

    elif option == "4": # 회원목록
        clear()
        print("\n회원목록 조회중\n")
        if len(Member_list) == 0: # Member_list에 저장된 회원이 없는 경우
            print("\n가입된 회원이 없습니다.\n")
            login_initial_option()
        else:
            for member in Member_list: # Member_list에 저장된 회원의 프로필 출력
                member.show_profile()
            login_initial_option()

    elif option == "5": # 종료
        clear()
        print("\n◈ [중앙도서관 리더즈SNS]를 종료합니다. ◈\n")


def login_page(login_member): # 로그인된 화면 (로그인한 회원 객체를 받는다)
    print("\n◆ 현재 사용자: [%s]님 ◆"%login_member.ID)
    print("\n1. 내 프로필 보기\n2. 내가 쓴 글 보기\n3. 글 올리기")
    print("4. 게시글 구경하기\n5. 사용자 검색\n6. 태그 검색\n7. 회원탈퇴")
    print("8. 로그아웃\n")
    option = input("→ 옵션을 선택하세요:")
    while option not in ["1","2","3","4","5","6","7","8"]:
        option = input("\n(!) 1 ~ 8 에서만 선택하세요:")

    if option == "1": # 내 프로필 보기
        clear()
        login_member.show_profile() # 로그인한 회원의 프로필 출력
        print("\n1. 돌아가기 2. 로그아웃\n3. 좋아요 누른 게시글 보기\n4. 한줄 소개 변경\n")
        option = input("→ 옵션을 선택하세요:")
        while option!="1" and option!="2" and option!="3" and option!="4":
            option = input("\n(!) 1 ~ 4 에서만 선택하세요:")
        if option == "1": # 돌아가기
            clear()
            login_page(login_member)
        elif option == "2": # 로그아웃
            clear()
            initial_page()
        elif option == "3": # 좋아요 누른 게시글 보기
            clear()
            print("\n내가 좋아요 누른 게시글 목록\n")
            Timeline_post = [post[1] for post in Timeline]
            for post in login_member.like_post_list: # 내가 좋아요 누른 게시글 목록 조사
                if post not in Timeline_post: # 이때 타임라인의 글에 해당 게시글이 포함돼있지 않으면
                    login_member.like_post_list.remove(post) # 좋아요 누른 게시글 목록에서 삭제
            # 위의 과정은 좋아요 누른 게시글 목록을 보여주기 전에
            # 삭제된 게시글을 좋아요 누른 게시글 목록에서 제거하여 목록을 업데이트 하는 것이다
            if len(login_member.like_post_list) == 0: # 내가 좋아요 누른 게시글이 없는 경우
                print("\n좋아요 누른 게시글이 없습니다\n")
            else:
                for post in login_member.like_post_list: # 업데이트된 목록 내 글들을 출력
                    post.show_post()
            back_logout_option(login_member)

        elif option == "4": # 한줄 소개 변경
            clear()
            login_member.change_intro()
            back_logout_option(login_member)

    elif option == "2": # 내가 쓴 글 보기
        clear()
        print("내가 쓴 글 보기\n")
        if len(login_member.my_timeline) == 0: # 작성한 글이 없는 경우
            print("\n게시글이 없습니다.\n")
        else:
            for post in login_member.my_timeline: # 나의 타임라인 내 글들을 출력
                post.show_post()
        print("1. 돌아가기 2. 로그아웃 3. 게시글 삭제\n")
        option = input("→ 옵션을 선택하세요:")
        while option!="1" and option!="2" and option!="3":
            option = input("\n(!) 1 ~ 3 에서만 선택하세요:")
        if option == "1": # 돌아가기
            clear()
            login_page(login_member)
        elif option == "2": # 로그아웃
            clear()
            initial_page()
        elif option == "3": # 게시글 삭제
            clear()
            print("게시글 삭제\n")
            login_member.delete_my_timeline()
            back_logout_option(login_member)

    elif option == "3": # 글 올리기
        clear()
        print("글 올리기\n")
        infos = Post.input_post() # [글 내용, 태그 리스트]를 리턴받아 infos 변수에 저장
        new_post = Post(login_member,infos[0],infos[1]) # 로그인한 회원과 infos를 통해 Post 객체 생성
        login_member.my_timeline.insert(0,new_post) # 로그인한 회원의 타임라인 맨 앞에 생성된 객체 추가
        login_member.my_tags += infos[1] # 로그인한 회원의 태그 목록에 작성한 글의 태그 리스트 추가
        login_member.RP += 10 # 로그인한 회원의 RP +10
        login_member.rank() # RP에 변화가 생겼으므로 랭크 업데이트
        Timeline.append([new_post.upload_time,new_post]) # 타임라인에 [게시시간, Post 객체] 저장
        print("글 작성 완료! 이전 페이지로 돌아가서 확인하세요\n")
        back_logout_option(login_member)

    elif option == "4": # 게시글 구경하기
        clear()
        print("게시글 구경중\n")
        if len(Timeline) == 0: # 타임라인에 저장된 글이 없는 경우
            print("\n게시글이 없습니다.\n")
            back_logout_option(login_member)
        else:
            show_Timeline() # 전체 타임라인 글 출력
            print("1. 돌아가기 2. 로그아웃 3. 좋아요 누르기 4. 댓글쓰기\n")
            option = input("→ 옵션을 선택하세요:")
            while option!="1" and option!="2" and option!="3" and option!="4":
                option = input("\n(!) 1 ~ 4 에서만 선택하세요:")
            if option == "1": # 돌아가기
                clear()
                login_page(login_member)
            elif option == "2": # 로그아웃
                clear()
                initial_page()
            elif option == "3": # 좋아요 누르기
                clear()
                thumb_option_Timeline(login_member) # 좋아요를 누를 글 고르기

            elif option == "4": # 댓글 쓰기
                clear()
                add_comment_Timeline(login_member) # 댓글을 쓸 글 고르기

    elif option == "5": # 사용자 검색
        clear()
        Member.member_search(login_member)

    elif option == "6": # 태그 검색
        clear()
        Post.tag_search(login_member)

    elif option == "7": # 회원탈퇴
        clear()
        option = input("\n→ 탈퇴하시겠습니까?(y:예/n:아니오):")
        while option not in ["y","n"]:
            option = input("\n(!) y 또는 n 중에서 선택하세요:")
        if option == "y":
            clear()
            Member_list.remove(login_member) # Member_list에서 로그인한 회원 제거
            for post_info in Timeline: # 전체 타임라인 글 검사
                if post_info[1].writer_ID == login_member.ID: # 해당 글이 탈퇴하려는 회원이 작성한 게시글이면
                    Timeline.remove(post_info) # 타임라인에서 제거
            print("\n탈퇴처리 되었습니다. 초기화면으로 돌아갑니다.")
            initial_page()
        elif option == "n":
            clear()
            print("\n이전화면으로 돌아갑니다.")
            login_page(login_member)

    elif option == "8": # 로그아웃
        clear()
        initial_page()
# -------------------------------------------------- 여기까지 클래스와 함수 정의

Timeline = []       # [글의 게시시간, 글(Post 클래스 인스턴스)]가 저장되는 리스트
Member_list = []    # 회원(Member 클래스 인스턴스)가 저장되는 리스트
rank_list = ["도서관 뉴비","도서관 라이트유저","도서관 애용자",    # 도서관 레벨
"도서관 은둔고수","도서관 고인물"]
initial_page()      # 초기화면 실행
