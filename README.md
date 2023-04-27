### 숨김 파일 여는 법 (mac)

  ```python
command + '.' + shift
  ```

### Git 관리에서 특정 파일/폴더를 배제해야 할 경우

- 포함할 필요가 없을 때
  - 자동으로 생성 또는 다운로드 되는 파일들 (빌드 결과물, 라이브러리)

- 포함하지 말아야 할 때
  - 보안성 민감한 정보를 담은 파일

=> ``.gitignore`` 파일 사용해서 배제할 요소를 지정가능하다.

---

## Lesson1. 변화를 타임캡슐에 담아 묻기

1. 프로젝트의 변경사항들을 타임캡슐(버전)에 담기
   변경사항 확인

   ```python
   git status
   ```

   파일 하나 담기

   ```python
   git add [file name]
   ```

   모든 파일 담기

   ```python
   git add .
   ```

   - ``git status``로 확인하기

2. 타임캡슐 묻기
   아래 명령어로 commit

   ```
   git commit
   ```

   - Vi 입력 모드로 진입
     - 입력 시작: ``i``
     - 입력 종료: ``ESC``
     - 저장 없이 종료(입력한 것 없을 시): ``:q``
     - 저장 없이 강제 종료: ``:q!``
     - 저장하고 종료: ``:wq``
   - ``FIRST COMMIT`` 입력한 뒤 저장하고 종료

   커밋 메시지까지 함께 작성하기

   ```python
   git commit -m "FIRST COMMIT"
   ```

   아래 명령어와 소스트리로 확인

   ```python
   git log
   ```

   - 종료는 ```:q```

3. 다음 변경사항들 만들고 타임캡슐에 묻기
   **변경사항**

   - ```lions.yaml```파일 삭제
   - ``` tiger.yaml```의 manager를 ``Donald``로 변경
   - ```leopards.yaml``` 파일 추가

   ``` python
   team: Leopards
   
   manager: Luke
   
   members:
   - Linda
   - William
   - David
   ```

   - ```git status```로 확인
     - 파일의 추가, 변경, 삭제 모두 내역으로 저장할 대상
   - ``git diff``로 확인
     - `j` : 아래로 스크롤
     - `k` : 위로 스크롤
     - `:q` : 닫기


   캡슐에 담기

   ```python
git add .
   ```

   - `git status`로 확인

     

   ```python
git commit -m "Replace Lions with Leopards"
   ```

   

   ✅ TIP `add`와 `commit` 한꺼번에

   ```python
git commit -am "(메시지)"
   ```

   - ‼️ 새로 추가된(untracked) 파일이 없을 때 한정



## Lesson 2. 과거로 돌아가기 실습

1. 실습 전 내역 백업
   - `.git` 폴더를 복사해두기
     - 맥에서 숨김 파일 보기: `command` + `shift` + `.`
   - `.git` 폴더 없앤 다음 git 상태 확인해보기

---

2. **reset** 사용해서 과거로 돌아가기

 아래 명령어로 커밋 내역 확인

```python
git log
```

- 되돌아갈 시점: 돌아갈 시점의 커밋 해시 복사
- `:q`로 빠져나가기

```python
git reset --hard (돌아갈 커밋 해시)
```

- reset의 옵션(--hard 등)은 섹션 5에서 다룰 것

-----

3. **reset** 하기 전 시점으로 복원해보기

 백업해 둔 `.git` 폴더 사용

- `.git` 폴더 복원

- `git log`, `git status`로 상태 확인

- 아래 명령어로 현 커밋 상태로 초기화

  ```python
  git reset --hard
  ```

- 뒤에 커밋 해시가 없으면 마지막 커밋을 가리킴

-----

4. **revert**로 과거의 커밋 되돌리기

   `Add George to Tigers`의 커밋 해시 구하기

   아래 명령어로 **revert**

   ```python
   git revert (되돌릴 커밋 해시)
   ```

   - `:wq`로 커밋 메시지 저장

---

✅ 커밋해버리지 않고 revert하기

```
git revert --no-commit (되돌릴 커밋 해시)
```

- 원하는 다른 작업을 추가한 다음 함께 커밋
- 취소하려면 `git reset --hard`

 

## Lesson 3. SourceTree로 진행해보기

1. 변경사항  만들고 커밋하기
   - 파일 삭제, 수정 등등의 변경사항 만듦
   - `.gitignore`에 `*.config` 추가  
   - 파일 추가
   - 커밋 메시지: `commit with SourceTree`

---

2. revert

- 해당 커밋에 마우스 우클릭 - `커밋 되돌리기`

----

3. reset

- 해당 커밋에 마우스 우클릭 - `...이 커밋으로 초기화`
- 선택지에서 `Hard` 선택



## Lesson 4. 여러 branch 만들어보기

Branch: 분기된 가지 (다른 차원)

- 프로젝트를 하나 이상의 모습으로 관리해야 할 때
  - 예) 실배포용, 테스트서버용, 새로운 시도용
- 여러 작업들이 각각 독립되어 진행될 때
  - 예) 신기능 1, 신기능 2, 코드개선, 긴급수정..
  - 각각의 차원에서 작업한 뒤 확정된 것을 메인 차원에 통합

#### 이 모든 것을 하나의 프로젝트 폴더에서 진행할 수 있도록!

----

1. 브랜치 생성 / 이동 / 삭제하기

   `add-coach`란 이름의 브랜치 생성

   ```python
   git branch (새로운 브랜치명)
   ```

   브랜치 목록 확인

   ```python
   git branch
   ```

   `add-coach` 브랜치로 이동

   ```python
   git switch (새로운 브랜치명)
   ```

   - `checkout` 명령어가 Git2.23 버전부터 `switch`, `restore`로 분리

📌 브랜치 생성과 동시에 이동하기

```python
git switch -c (새로운 브랜치명)
```

- 기존의 `git checkout -b (새 브랜치명)`

🗑️ 브랜치 삭제하기

```
git branch -d (삭제할 브랜치명)
```

---

2. 결과 살펴보기

`git log`: 위치한 브랜치에서의 내역만 볼 수 있음

여러 브랜치의 내역 편리하게 보기

```python
git log --all --decorate --online --graph
```



** sourceTree에서 확인하면 더 쉽다. **



## Lesson 5. branch 합치기 실습

1. merge로 합치기

​	`add-coah` 브랜치를 `main` 브랜치로 merge

- `main`브랜치로 이동

- 아래의 명령어로 병합

  ```python
  git merge add-coach
  ```

- `:wq`로 자동입력된 커밋 메시지 저장하여 마무리

- 소스트리에서 확인

  

🩵 `merge`는 `reset`으로 되돌리기 가능

- `merge`도 하나의 커밋
- `merge` 하기 전 해당 브랜치의 마지막 시점으로



#### 병합된 브랜치는 삭제

삭제 전 소스트리에서 `add-coach` 위치 확인

```python
git branch -d add-coach
```

---

2. **rebase**로 합치기

   `new-team` 브랜치를 `main` 브랜치로 **rebase**

   - `new-team` 브랜치로 이동
     - `merge` 때와는 반대!
   - 아래의 명령어로 병합

   ```
   git rebase main
   ```

   - 소스트리에서 상태 확인

     - `main` 브랜치는 뒤쳐져 있는 상황

       

   - `main` 브랜치로 이동 후 아래 명령어로 `new-team`의 시점으로 **fast-forward**

     ```
     git merge new-teams
     ```

   - `new-teams` 브랜치 삭제



## Lesson 6. 충돌 해결하기

#### 브랜치간 충돌

- 파일의 같은 위치에 다른 내용이 입력된 상황

1. `merge` 충돌 해결하기

​	`git merge conflict-1`로 병합을 시도하면 충돌 발생

- 오류 메시지와 `git status` 확인
- VS code에서 해당부분 확인



당장 충돌 해결이 어려울 경우 아래 명령어로 `merge` 중단

```python
git merge --abort
```

해결 가능 시 충돌 부분을 수정한 뒤 `git add .`, `git commit` 으로 병합 완료

----

2. `rebase` 충돌 해결하기

`confilct-2`에서 `git rebase main`로 리베이스 시도하면 충돌 발생

- 오류 메시지와 `git status` 확인
- VS Code에서 해당 부분 확인

당장 충돌 해결이 어려울 경우 아래 명령어로 `merge` 중단

```python
git rebase --abort
```



#### 해결 가능 시

- 충돌 부분을 수정한 뒤  `git add .`
- 아래 명령어로 계속

```python
git rebase --continue
```

- 충돌이 모두 해결될 때까지 반복

`main`에서 `git merge conflict-2`로 마무리

`conflict-1`, `conflict-2` 삭제
