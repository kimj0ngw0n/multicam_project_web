# 인터페이스 만들기

멀티캠퍼스 인터페이스 개인 프로젝트

> 2023.04.11 ~ 2023.04.13

간단한 기능이 있는 디스코드를 만들어 본다.

기능이 별로 없으므로 확장성을 생각하면서 기획한다.

## 목차

1. [기획](###-기획)
2. [체크리스트](###-체크리스트)
3. [결과](###-결과)

## 기획

### Model
    
#### ACCOUNTS

- `User` [유저]
    - `friends` : `ForeignKey(), self`  [FK/친구]
    - `friend_reqs` : `ForeignKey(), self`  [FK/친구요청목록]

#### SURVER

- `Surver` [서버]
    - `name` : `CharField(20)`  [이름]

- `Access` [권한]
    - `surver` : `ForeignKey()`  [FK/서버]
    - `user` : `ForeignKey()`  [FK/유저]
    - `type` : `CharField(20)`  [권한 종류]

- `Category` [카테고리]
    - `name` : `CharField(20)`  [이름]
    - `type` : `CharField(20)`  [공개 여부]
    - `surver` : `ForeignKey()`  [FK/소속 서버]

- `Channel` [채널]
    - `name` : `CharField(20)`  [이름]
    - `type` : `CharField(20)`  [채널 종류]
    - `category` : `ForeignKey()`  [FK/소속 카테고리]

- `Message` [메시지]
    - `user` : `ForeignKey()`  [FK/작성자]
    - `channel` : `ForeignKey()`  [FK/소속 채널]
    - `created_at` : `DateTimeField()`  [작성일자]
    - `updated_at` : `DateTimeField()`  [수정일자]
    - `content` : `TextField()`  [내용]
    - `reaction` : `CharField(20)`  [반응. 좋아요만 구현]

### Views

- Accounts

    - signup (회원가입)
    
        - 회원가입 하지 않을 시, 접속 안됨.

    - signin (로그인)

    - signout (로그아웃)

    - friends (친구목록)

    - profile (프로필)

    - request friend (친구요청)

    - feedback request (요청에 대한 반응)

    - delete friend (친구삭제)

- Surver

    - create surver

    - create category

    - create channel

    - create message

    - message detail

        - 블로그 댓글처럼 보이도록 구현

    - update surver

    - update category

    - update channel

    - update message

    - delete surver

        - 관리자만 삭제 가능

    - delete category

    - delete channel

    - delete message
    
        - 본인 또는 관리자만 삭제 가능

    - reaction message

        - 반응이 있는 경우만 출력

    - add member

        - 서버에 멤버 추가

## 체크리스트

### 1일차
1. ~~기획~~
2. ~~모델링~~
3. view
4. html 작성

### 2일차
1. template에 css 적용
2. 기타 수정사항 적용

### 3일차
1. 기타 수정사항 적용
2. 결과란 작성

## 결과
