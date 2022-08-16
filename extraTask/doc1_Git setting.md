# Git 환경 구축하기
v1.0 2022.07.29 first release
v1.1 2022.08.01 local managing update


EMC part에서 생성하는 데이터들을 온라인 저장소에서 공동으로 관리하기 위해 Git 환경을 구축 함.
그러나 Git Hub는 공개저장소로 만들기 때문에 보안과 관련된 파일들을 관리할 수 없어 EMC part에서 생성하는 업무 외 모든 파일들을 관리하는 것으로 범위를 한정한다.

예를 들면,
- 3d printer 파일들
- EMC jig 도면 들
- 업무 외 문서들(git 환경 구축하기 등)

## 1. 작업 순서

1. (계정이 없다면)github에 접속해서 계정 생성.
여기에서는 예시로 epsEMC(ngkim.mando@gmail.com) 라는 깃허브 계정 생성.
epsEMC 계정 내에 epsEMC라는 main 저장소(=폴더)를 생성하고 저장소의 소개를 위한 README.md 를 작성 함.
epsEMC내에 하부 폴더로 extraTask, imageTemp 등을 구성할 계획 임.

2. 로컬 저장소로 사용할 PC에 Git program 설치

3. Git hub 의 epsEMC 저장소에서 운영할 폴더를 로컬저장소에서 생성

4.  로컬 저장소와 온라인 저장소 연결

5.  Push/pull 해보기


## 2. 저장소(repository) 구성

Git으로 데이터를 공동 관리하기 위해서는 온라인으로 공유가 가능한 Github 사이트의 저장소가 필요하고, 데이터의 수정 및 다운로드/업로드를 위해서 작업 PC 내에 Git 이라는 program 설치가 필요하다.
이 때, 작업 PC의 공간을 Local repository 라고 한다.
폴더 구성은 아래와 같다.
 d:\EMCgit\내에 git 목적별로 구분하여 관리 예정
 d:\EMCgit\epsEMC\ 						# 메인 폴더
 d:\EMCgit\epsEMC\extraTask\		# 하부 폴더1
 d:\EMCgit\epsEMC\imageTemp\	# 하부폴더2

만약 github에서 다운로드하여 사용할 사용자라면, Chapter 5. 로 이동.



## 3. Git hub 사이트에서 계정 생성

git program을 통한 데이터 공동관리를 위해서는 온라인 저장소가 필요하며 이 온라인 저장소가 github 라는 웹사이트 임.

아래 블로그를 참조하여 깃허브에서 계정 생성
https://geundung.dev/46

참고로 git에 대한 간단한 설명이다.

Git :  데이터의 Push/Pull 작업을 하기 위한 파일 관리(?) 프로그램
github : 온라인 저장소
repository : 저장소
운영방식 : 온라인 저장소의 내용들을 로컬로 내려받아(pull) 수정하여 온라인으로 push 하는 방식으로 운영. 이 때,  기본이 되는 버전라인이 main 이며, 수정하려고 내려받거나 내가 수정하고 있던 건 별도의 branch가 됨. 이를 github 에서 비교, 머지  등을 통해 하나의 main 으로 병합하게 됨.
이러한 작업으로 main 버전이 유지가 되고 각 각이 수정한 버전이 이력에 따라 반영 되면서 문서의 공동 버전 관리(단일의 버전) 가 가능하게 됨.

github를 이용하게 되면 온라인으로 내용을 관리하므로 어디에서나 접근 가능 함.

대신, git에 대한 초기 개념 이해가 어렵고, 현재 사용하고 있는 네트워크드라이브에 비해 별도의 명령어를 사용해야 하므로 불편함.
무료로 사용하기 위해 public 으로 저장소 생성.
보안 설정 불가하므로 공개 가능한 자료만 이용해야 함.

## 3. Git 프로그램 설치하기

아래 블로그를 참조하여 Git을 설치
https://codevkr.tistory.com/45

> Local 저장소와 연동하기

윈도우 탐색기에서 Github에 연결하고자 하는 폴더의 상위에서 마우스 우클릭, 
Ggit Bash Here로 Git Terminal 에 진입.

여기에서는 epsEMC폴더내용들을 github에 연결 함.

![Figure1](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc1_gitbash.JPG?raw=true)

실행 결과 아래와 같은 Terminal 창이 뜸.

![생성된 git bash terminal](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc1_gitbashInit.JPG?raw=true)

만약 경로가 다르다면 Terminal 창에서 cd 명령어를 이용하여 원하는 Local 저장소로 이동

```
rds_user@MDSD000P9012521 MINGW64 ~
$ cd d:\EMCgit\epsEMC
rds_user@MDSD000P9012521 MINGW64 /d/epsEMC (main)
```

이 때, 정상적으로 연결된 local 저장소 일 경우(git initial 작업 완료) (main) 이라는 꼬리가 달린다. 참고로 과거 git은 (master) 가 달림.
master 로 설정된 구 방식을 main으로 변경하기
(master는 노예제도를 연상시킨다 하여 Black lives matter  운동의 일환으로 main으로 변경 됨.)

https://velog.io/@cychann/Github-default-branch-%EB%B3%80%EA%B2%BD%ED%95%98%EA%B8%B0-master-to-main


git initial 작업은 다음 장에서 설명.



## 4. Local 연동 및 데이터 내보내기

다음 명령어를 차례로 입력해 주면 됨.
초기 저장소 연결을 위한 git init 을 제외하고는
간단하게 add -> commit -> push 의 작업순서로 파일을 올린다고 보면 됨.


```python
git init #최초 1회만 입력
git add . #.은 전체폴더와 파일을 올릴때 사용, 단독파일은 파일명.확장자로 입력해주면 됨
git status # 상태확인용으로 생략가능하지만 간혹 add가 안된 경우가 있으멸 확인 하면 좋음
git commit -m "first commit" # " " 내에 history를 입력, commit 없이 push 안됨.
git remote add origin (해당 깃 주소) # 연결고리 만드는 작업으로 이미 있으면 생략. 해당 깃 주소는 github 에서 code 를 선택하고 탭에서 ssh를 입력하면 사용가능한 경로가 나옴
git remote -v #선택사항, 연결상태 확인
git push origin main
```

github 온라인에서 변경사항이 제대로 업로드 되었는지 확인.

반대로 온라인의 내용을 내려받을 때는 아래 명령 사용

```
>git pull orign main
```

## 5. 데이터 가져오기(download, pull...)

github에 있는 내용을 가져오는 방법에는 3가지가 있다.
1. pull
2. fetch
3. clone



### 1) Git pull

pull과 fetch는 병합의 유무의 차이이며, pull은 원격저장소에 있는 변경사항을 그대로 로컬저장소로 옮겨와 자동으로 병합해 주는 기능이다. 개인적으로 github를 사용한다면 pull을 가장 많이 사용하게 된다.


```
cd d:\EMCgit\epsEMC\ # cd 명령어를 이용하여 해당 폴더로 이동
git remote -v # git 연결상태 확인
git pull origin main #또는 git pull [원격저장소이름] [원격저장소에서 받아고자하는 브랜치 이름]

```


> git pull = git fetch + git merge


### 2) Git Fetch
git fetcg 사용법은 동일하므로 생략한다.

fetch는 변경 사항을 가져오지만 병합(merge)는 하지 않는다. 이를 이용하여 다른 사람이 수정한 부분을 확인하고 병합할 수 있는 장점이 있지만 초보나 개인적인 목적에서는 사용할 일이 없다.


### 3) Git clone

clone 은 원격저장소의 내용을 새로운 폴더에 그대로 복사하는 것으로 새로운 작업pc에서 작업해야할 경우 유용하다.

우선 가져올 폴더를 생성한다.
github 에서 clone 할 원격 저장소의 주소를 복사한다.

![git 에서 주소 가져오기](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc1_git%20add.JPG?raw=true)

```
git clone https://github.com/epsEMC/epsEMC.git # 복사한 주소 삽입

```
clone은 초기혹은 push pull 사용하면서 history가 꼬여  오류가 발생한다면 기존의 Local 저장소를 지우고 clone 해 오면 쉽게 해결 된다.

### 3) 온라인에서 작업하기
수정하고자 하는 파일에 접속하여 편집하기 클릭
![온라인에서 수정하기](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc1_git%20modi%20doc.JPG?raw=true)

내용을 수정하고 아래의 commit changes 에서 commit 사항을 입력 후 commit changes 클릭
![온라인 커밋하기](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc1_git%20modi%20commit.JPG?raw=true)

로컬 저장소에 github 온라인 저장소에서 수정된 사항을 아래 명령을 통해 내려받아 자동 병합을 시켜준다.

```
git pull origin amin

```
그러면 아래와 같은 문구와 함께 변경된 파일, 변경 범위 등이 간략히 표시되며 병합이 완료 된다.

![pull result](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc1_git%20pull%20result.JPG?raw=true)


# Reference

1. Github easy guide:
https://geundung.dev/46

3. Github에 폴더 업로드 하는 법 :
https://y-oni.tistory.com/126, https://vanillacreamdonut.tistory.com/193
폴더에 파일 없으면 진행 안됨. 

4. Markdown guide :  https://gist.github.com/ihoneymon/652be052a0727ad59601

5. github에서 imagae 관리하여 md 문서 내에 삽 시 경로 안 잃게 하는 방법 : https://theorydb.github.io/envops/2019/05/22/envops-blog-how-to-use-md/

 5. Stackedit 에서 github 연동하기 :
https://danggai.github.io/github.io/StackEdit%EC%97%90%EC%84%9C-Github.io%EB%A1%9C-%ED%8E%B8%ED%95%98%EA%B2%8C-%EB%B8%94%EB%A1%9C%EA%B9%85%ED%95%98%EA%B8%B0!/
 










> Written with [StackEdit](https://stackedit.io/).


