# LicenseReservationSystem
서울과학기술대학교 전자회로(2) 과목의 IDEC S/W를 팀내에서 팀원들에게 분배하기 위한 시스템입니다.
## 목차
1. [들어가기 전 주의사항](#들어가기-전-주의사항)
2. [바탕](#바탕)
    1. [기본 프로그래밍 언어](#기본-프로그래밍-언어)
    2. [Database 관리](#Database-관리)
3. [테스트를 위해 Python에서 꼭 추가적으로 설치해줘야 하는 모듈들](#테스트를-위해-Python에서-꼭-추가적으로-설치해줘야-하는-모듈들)
    1. [Flask](#Flask)
    2. [psycopg2](#psycopg)
    3. [gunicorn](#gunicorn)
4. [Deploy 방법](#Deploy-방법)
    1. [소스코드 다운로드](#소스코드-다운로드)
    2. [Postgresql 서버 설정 및 초기DB 생성](#postgresql-서버-설정-및-초기db-생성)
    3. [환경 변수 설정](#환경-변수-설정)
    4. [서버 세팅 방법](#서버-세팅-방법)
        1. Heroku 가입 및 Postgresql 서버 만들기
        2. Heroku Postgres 사용자 정보 반영하기
        3. Heroku에 업로드
5. [Deploy 이후 사용 방법](#Deploy-이후-사용-방법)
    1. [메인 페이지](#메인-페이지)
    2. [사용자 등록](#사용자-등록)
    3. [라이센스 접근](#라이센스-접근)
## 들어가기 전 주의사항
1. 본 소스코드는 시간에 대한 분배만 담당합니다.
  * 실제 라이센스는 본 프로그램에 따라 등록, 회수되지 않습니다.
  * 시간에 대한 약속이나 분배가 힘든 팀에게 사용을 권장합니다.
2. 본 문서의 하이퍼링크 중 괄호가 없는 링크는 문서의 다른 목차로 이동됩니다. 
  * 괄호가 존재하는 하이퍼링크들은 읽던 페이지를 빠져나오게 됩니다.
3. 본 문서는 순차적으로 읽을 것을 고려하지 않고 작성되었습니다. 
  * 순차적인 세팅 튜토리얼은 [서버 세팅 방법](#서버-세팅-방법)에 있습니다.
4. [서버 세팅 방법](#서버-세팅-방법) 목차만 읽게 될 경우, 하이퍼링크 중 다른 목차로 이동하는 링크들은 반드시 확인해주세요.


## 바탕
### 기본 프로그래밍 언어
* Python3 
### Database 관리
* Postgresql

## 테스트를 위해 Python에서 꼭 추가적으로 설치해줘야 하는 모듈들
### Flask
* Flask는 python의 웹 프레임워크입니다.
* Routing 등 백엔드 개발을 위해 사용되었습니다.
### psycopg2 
* psycopg2는 Postgresql 서버를 python에서 접근하기 위해 사용되는 모듈입니다.
* 현재 pip install psycopg2로 설치가 불가능하므로, 같은 소스로 이미 컴파일이 되어있는 psycopg2-binary 모듈을 추천합니다.
### gunicorn
* gunicorn은 WSGI 서버 프로그램입니다.
* flask와 같은 웹 프레임워크에 http 요청을 변환하여 전달하는 역할을 합니다.
## Deploy 방법
### 소스코드 다운로드
* git clone, fork등 각자의 방법으로 [(소스코드)본 소스코드](https://github.com/emshdev/LicenseReservationSystem)를 취득합니다.
### Postgresql 서버 설정 및 초기DB 생성
* heroku와 같은 PaaS에서 제공하는 Postgres [서버를 이용](#서버-세팅-방법)하거나, 이 [(외부링크)블로그](https://valuefactory.tistory.com/491)와 같이 직접 본인의 서버에 설치하여 운용합니다.
* 서버를 생성한 이후에는 아래와 같은 명령문을 통해 데이터베이스에 접속해 [(소스코드)dump.sql](https://github.com/emshdev/LicenseReservationSystem/blob/main/dump.sql)을 실행시켜줍니다. (필수)
```
PGPASSWORD=<사용자 비밀번호> psql -h <db서버url이나ip> -U <사용자명> -d <db명> -f dump.sql
```
### 환경 변수 설정
* 사용자의 입맛대로 변경이 가능한 변수들은 최대한 [(소스코드)Setting.py](https://github.com/emshdev/LicenseReservationSystem/blob/main/Setting.py)로 모아두려고 노력했습니다.
* 여기서 db를 연결해주기 위해 반드시 설정해야 하는 변수는 credentials 입니다.
1. host
* <db서버url이나ip> 를 postgresql 서버의 주소로 대체합니다.
* 직접 서버에 설치한 경우에는 localhost 
2. dbname
* <db명>을 Postgresql에서 생성한 데이터베이스명으로 대체합니다.
3. user
* <db사용자명>을 Postgresql에서 생성한 사용자명으로 대체합니다. 
4. password
* <db사용자비밀번호>를 사용자 비밀번호로 대체합니다. 
5. port
* <db포트>를 설정한 포트로 대체합니다.
* 기본값은 5432입니다.
### 서버 세팅 방법
#### "주의사항: 본 코드는 heroku에 업로드하여 사용하는 것만을 검증하였습니다."
* **소스코드를 먼저 다운로드 받고 진행해주세요**
1. Heroku 가입 및 Postgresql 서버 만들기
* [(외부링크)Heroku](https://www.heroku.com)에 접속하여 [(외부링크)사용자 가입을 진행](https://programming4myself.tistory.com/5#menu1)합니다.
* Heroku에 가입이 완료되면, [(외부링크)new app](https://dashboard.heroku.com/new-app)에서 **앱 이름**을 지정하고 create app을 클릭합니다. 
#### (곧 쓰일 예정으로 앱 이름은 반드시 정확하게 메모해두세요)
* 나타나는 페이지에서 Resources를 클릭합니다.
* Add-ons에서 Heroku Postgres를 검색하여 해당 항목을 클릭합니다.
* 나타나는 팝업스크린에서 Submit Order Form을 클릭합니다.
* Add-ons에 새롭게 생성된 Heroku Postgres 항목을 클릭합니다.
2. Heroku Postgres 사용자 정보 반영하기
* Heroku Postgres를 클릭하고 기다리면 페이지에 Settings 탭이 나타납니다. 이를 클릭해줍니다.
* Settings 탭에서 우측의 View Credentials를 클릭합니다.
* 나타난 정보를 다운로드 받은 소스코드의 [Setting.py에 적용](#환경-변수-설정)해주고 저장합니다.
3. Heroku에 업로드
* Heroku에 git 방식으로 업로드하기 위해서는 [(외부링크)git](https://git-scm.com/)과 [(외부링크)Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)가 필요합니다.
* 위의 두 프로그램의 설치 방법에 대해서는 문서화가 잘 되어있으므로 해당 사이트나 구글등에서 검색을 통해 [(외부링크)문서를 참조](https://programming4myself.tistory.com/5#menu2)하시는 것을 부탁드립니다.
* Heroku CLI에서 로그인을 진행합니다.[(외부링크)윈도우의 경우 참고](https://programming4myself.tistory.com/5#menu3)
```
$ heroku login
```
* 앞서 Heroku 가입후 작성한 앱 이름을 이용해 아래의 명령을 실행해줍니다.
```
$ heroku git:clone -a <앱 이름>
$ cd <앱 이름>
```
#### (터미널을 종료하거나 다른 폴더로 이동하지 말아주세요)
* 앱 이름과 동일한 이름으로 생성된 폴더에 수정한 Setting.py를 포함한 전체 소스코드를 붙여 넣어줍니다. 
* 터미널에서 ls나 dir 등의 명령어를 실행해 폴더의 최상단에 소스코드가 존재하는지 확인합니다. 
#### ([(소스코드)wsgi.py](https://github.com/emshdev/LicenseReservationSystem/blob/main/wsgi.py)와 [(소스코드)Procfile](https://github.com/emshdev/LicenseReservationSystem/blob/main/Procfile)이 보이면 됩니다.)
* 터미널에서 아래의 명령을 실행해줍니다. (일반적으로 깃허브에서 진행하는 커밋과 달리 앱 빌드 과정이 있습니다. 시간을 갖고 기다려주세요.)
```
$ git add .
$ git commit -am "<커밋 메세지>"
$ git push heroku master
```
* **다음 단계로 진행하기 전 [초기DB 설정을 완료](#postgresql-서버-설정-및-초기db-생성)했는지 확인하고 진행해주세요**
* 빌드가 완료되면 앱 이름을 이용하여 아래와 같은 웹사이트에 접속을 시도합니다.
```
http://<앱 이름>.herokuapp.com/
```
* **사용자 등록**, **1번 라이센스**, **2번 라이센스**가 적힌 버튼이 보이면 heroku에 업로드를 성공한 것입니다.
## Deploy 이후 사용 방법
### 메인 페이지 
* 사용자 등록 페이지와 각 라이센스에 대한 몇가지 작업이 가능한 페이지로 이동하는 버튼이 존재합니다.
### 사용자 등록
* 메인화면에서 사용자등록 버튼을 누릅니다.
* 사용자에게 Setting.py에서 설정한 magicword(기본값 15), 사용자의 학번, 사용자의 이름, 사용자의 긴급연락처(필수x) 순으로 기재하게 합니다. 
* 작은 버튼 '제출'을 클릭하여 등록을 마치고, 초기화면으로 돌아가기 버튼을 눌러 기본 페이지로 돌아옵니다.
* **등록을 마친 이후에 모든 자격증명은 본인의 학번으로 진행됩니다.**
### 라이센스 접근
* 대여하고자 하는 라이센스 번호에 따라 '1번 라이센스'와 '2번 라이센스' 버튼을 눌러 해당 라이센스에 접근합니다.
* 라이센스에 접근하면 '라이센스 대여' '대여 현황' '대여 연장' 옵션이 있습니다. 각 버튼을 눌러 옵션에 접근합니다.
1. 라이센스 대여
* 말 그대로 라이센스를 대여하는 페이지입니다. 
* 본인의 학번을 입력하고 조그만 버튼 '제출' 을 눌러 대여를 진행합니다. 
* 앞서 대여한 사람의 대여 기한이 만료되지 않았다면 대여할 수 없습니다.
2. 대여 현황
* 누가 해당 라이센스를 대여하고 있는지 목록의 형태로 체크할 수 있습니다. 
* 당장에 누가 대여중인지 각 페이지에 보여지므로 사후 판단을 위해 제공하고 있습니다.
3. 대여 연장
* 2시간 간격으로 최대 8시간까지 연장하는 옵션입니다. 
* 현 대여자가 본인의 학번을 입력하여 연장을 진행할 수 있습니다.
