#실제 사용자인지 증명하기 위한 단어를 설정해주세요
magicword = '15'
#postgresql 접속 자격
credentials = "host=<db서버url이나ip> dbname=<db명> user=<db사용자명> password=<db사용자비밀번호> port=<db포트>"
#1회 연장시 추가 시간
add_time = 2
#최대 대여 기간
max_time = 8


question_for_magicword="우리는 몇팀?"
class sufa:
    success="성공"
    fail="실패"
    
class reason:
    register_success="정상적으로 사용자 등록이 완료되었습니다."
    extend_success="정상적으로 대여 연장이 완료되었습니다."
    extend_fail = "연장 횟수가 기준을 넘었습니다. 사용자가 없을 경우 신규 대여를 신청하세요."
    youre_not_the_one="현재 사용자의 학번이 아닙니다."
    checkin_success = "정상적으로 대여 신청이 완료되었습니다."
    checkin_fail_still_using = "아직 현 사용자의 대여 기간이 만료되지 않았습니다."
    db_access_fail = "DB 접근에 실패하였습니다."
    db_write_fail="DB 쓰기에 실패하였습니다."
    magicfail="가입 대상 인증용 단어가 일치하지 않습니다."
