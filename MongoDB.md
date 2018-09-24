# MongoDB

## NoSQL : 데이터베이스가 없는 NOT Only SQL이다. 기존의 RDBMS의 한계를 극복하기 위해 만들어진 새로운 형태의 데이터저장소이다.
 * RDBMS : 관계형 데이터베이스 관리 시스템 (Ex : Mysql)

 ## Document : Document란 RDMS의 record와 비슷한 개념이다. 그리고 동적 schema를 가지고 있다. == key-value 쌍으로 이루어져 있다. 
 * record : 정보 또는 개념의 단위 하나의 개체는 여러개의 속성을 가진다 == 행(row)이랑 같은 말
 ---
 ```
 "_id": ObjectId("5099803df3f4948bd2f98391"),
"username": "velopert",
"name": { first: "M.J.", last: "Kim" }
```
---
-   ####  _id, username, name 은 key 이고 그 오른쪽에 있는 값들은 value 이다.

## Collection : Collection안에 Document들이 들어있다. RDMS의 table과 비슷한 개념이다. 하지만 RDMS와 달리 schema를 가지고 있지 않다. 