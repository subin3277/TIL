# Git

- Git (분산 버전 관리 프로그램)

  - 버전관리

    변경 내용 + 마지막 파일

  - 분산

    -중앙 집중식 버전관리

    -분산 버전 관리 (서버 컴퓨터(클라우드) + 2개의 컴퓨터(실물))

- github : git 기반의 저장소 서비스를 제공하는 서버(ect.. gitlab, bitbucket)

- gitlab(삼성) vs github(MS)

  - gitlab : 저장된 서버를 가지고 있음
  - github : MS의 서버에 저장이 된다

- Repository : 특정 디렉토리를 버전 관리하는 저장소
  - git init으로 로컬 저장소 생성
  - .git 디렉토리에 버전관리에 필요한 모든 것이 들어있음
  - 특정 버전으로 남긴다 = 커밋(commit) 한다.
- 커밋
  - Working Directory : 내가 작업하고 있는 실제 디렉토리
  - Staging Area : 커밋으로 남기고 싶은, 특정버전으로 관리하고 싶은 파일이 있는 곳
  - Repository : 커밋들이 저장되는 곳

- 명령어
  - add : Working Directory(untracked) → Staging Area(staged)
  - commit : Staging Area(staged)→ Repository(committed)
  - push : Repository(commited) → Working Directory(modified)
  - pull
  - clone
  - status : 현대 git으로 관리되고 있는 파일들의 상태를 알 수 있어요
  - git init
  - git add .
  - git commit -m “메세지”
  - git status : git 상태 확인
  - git log : log 확인
  - git diff A B (A가 기준) : 변경내용 확인
  - git remote add origin {remote_repo}
  - git push A B(A를 B에)
  - git push -u origin master 사용후에는 git push 만 해도 가능
  - git clone {주소} : 복제하기
  - code . : vs로 바로 열기
- local(컴퓨터에 있는 저장소) vs remote(서버에 있는 저장소)
