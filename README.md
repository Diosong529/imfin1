# 실행방법

먼저 python이 컴퓨터 내에 설치되어 있어야합니다.
3.10.9버전 권장합니다.

vscode와 vscode 내의 터미널을 사용하면 훨씬 편리합니다.

###1. git clone
```
$ git clone <repo link> 를 통해서 파일을 다운 받습니다.
```
### 2. venv 설정
터미널에 들어가서 (git powershell 기타등등)

가상환경인 venv 만들어서 실행하여야 합니다.
venv 는 해당 프로젝트를 실행시키기 위한 python 버전과 패키지를 일치시키기 위해서 사용합니다

원하는 폴더 위치에 가서
```
$ python -m venv venv
```
venv 를 생성합니다
```
$ ./venv/Scripts/activate.bat
```
cd를 사용해서 들어가서 직접 activate.bat 하는것도 좋지만 번거로우니 이렇게 합니다.
venv안의 activate.bat 파일을 실행시킵니다.

그 후에 환경이 venv로 변화하였다면

(venv) ~~~  이런식으로 변합니다.
### 3. pip로 python 패키지 다운
프로젝트 실행을 위해 패키지를 다운받아야하는데

터미널에서 pip
```
$ pip install django
$ pip install django-taggit
$ pip install django-taggit-templatetags2
$ pip install django-widget-tweaks
```
패키지들을 설치합니다.

### 4. 로컬로 서버 실행 
python을 통해서
manage.py 를 실행하여 로컬로 서버를 엽니다.
```
$ python manage.py runserver 8080
```
그리고 

February 01, 2023 - 18:10:29
Django version 4.1.5, using settings 'imfin1.settings'
Starting development server at http://127.0.0.1:8080/
Quit the server with CTRL-BREAK.

나오면 
http 링크를 복사해서 주소창에 붙혀 넣어 실행시켜 봅니다.

# 계정 ID 비밀번호

syh4533
sG199500



