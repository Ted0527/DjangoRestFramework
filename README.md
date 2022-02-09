## Practice Note for DjangoRestFramework

## 각 레포별 설명(난이도 순)

### school
- 가장 처음 Django 에서 DRF로 연습해본 코드
- Teacher(name), Student(name, FK=Teacher), Score(ko, en, math, FK=Student) 로 Model 구성
- Django 로 CRUD 작성 후 DRF로 변환
##### 세부 과제
- Teacher 검색 시, student_name 같이 출력
- Student 검색 시, teacher_name, score_total, avg 같이 출력

### quntum
- DRF로 구현한 첫 과제
- Category(name), Shop(name, FK=Category), Customer(name), Visited(visited_time, FK=Shop, FK=Customer) 로 Model 구성

##### 세부 과제
- router 적용, admin page 적용
- Category 검색시 shop_name 같이 출력
- Shop 검색시 shop 을 방문한 customer_name, customer_total 결과값 출력
- Customer 검색시 방문한 visited_shop 결과값 출력

### MovieListAPI-Django(Udemy 강의 코드), IMDB-Clone-DRF(Udemy 강의 풀 코드), snippet(DRF 공식문서 예제)
- DRF 예제용 코드

### Brokurly_v2
- 1차 프로젝트 리팩토링
