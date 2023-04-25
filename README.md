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

2. reset 사용해서 과거로 돌아가기

​	아래 명령어로 커밋 내역 확인

```python
git log
```

- 되돌아갈 시점: `Add team Cheets`의 커밋 해시 복사
- `:q`로 빠져나가기

```python
git reset --hard (돌아갈 커밋 해시)
```

- reset의 옵션(--hard 등)은 섹션 5에서 다룰 것

