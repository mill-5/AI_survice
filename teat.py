# 신규 기능: 사용자 목록 출력
def get_user_list(users):
    # 비효율적인 리스트 합치기 방식
    result = ""
    for user in users:
        result += user + ", "
    return result

print(get_user_list(["Kim", "Lee", "Park"]))
