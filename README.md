# 인터페이스 만들기

멀티캠퍼스 인터페이스 개인 프로젝트

> 2023.04.11 ~ 2023.04.13

> 간단한 기능이 있는 디스코드를 만들어 본다. 기능이 별로 없으므로 확장성을 생각하면서 기획한다.

## 목차

1. [기획](###-기획)
2. [체크리스트](###-체크리스트)
3. [결과](###-결과)

## 기획

### 모델

#### SURVER

- `Surver` [서버]
    - `name` : `CharField(200)`  [이름]
    - `manager` : `ForeignKey()`  [FK/관리자]

- `Category` [카테고리]
    - `name` : `CharField(200)`  [이름]
    - `surver` : `ForeignKey()`  [FK/소속 서버]

- `Channel` [채널]
    - `name` : `CharField(200)`  [이름]
    - `type` : `CharField(200)`  [채널 종류]
    - `category` : `ForeignKey()`  [FK/소속 카테고리]

- `Message` [메시지]
    - `user` : `ForeignKey()`  [FK/작성자]
    - `channel` : `ForeignKey()`  [FK/소속 채널]
    - `created_at` : `DateTimeField()`  [작성일자]
    - `updated_at` : `DateTimeField()`  [수정일자]
    - `content` : `TextField()`  [내용]
    - `reaction` : `CharField(200)`  [반응. 좋아요만 구현]
    
#### ACCOUNTS

- `User` [유저]
    - `name` : `CharField(200)`  [이름]
    - `star` : `ForeignKey(), self`  [FK/팔로우한 사람]

- `Access` [권한]
    - `user` : `ForeignKey()`  [FK/유저]
    - `type` : `CharField(200)`  [권한 종류]

## 체크리스트

### 1일차
1. 기획
2. 모델링
3. view
4. html 작성

### 2일차
1. template에 css 적용
2. 기타 수정사항 적용

### 3일차
1. 기타 수정사항 적용
2. 결과란 작성

## 결과
