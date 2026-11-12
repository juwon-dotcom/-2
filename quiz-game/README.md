# Python Quiz Game

## 프로젝트 개요

파이썬으로 만든 콘솔 기반 퀴즈 게임입니다.  
사용자는 운동역학과 관련된 퀴즈를 풀고, 퀴즈를 추가하거나 삭제할 수 있습니다.  
퀴즈 데이터와 최고 점수는 `state.json` 파일에 저장됩니다.

## 퀴즈 주제 선정 이유

운동역학은 인체 움직임과 힘의 작용을 이해하는 데 중요한 학습 주제입니다.  
관절 운동, 근수축, 지레 원리, 무게중심, 운동량 등 주요 개념을 퀴즈로 학습할 수 있도록 선정했습니다.

## 실행 방법

터미널에서 프로젝트 폴더로 이동한 뒤 아래 명령어를 실행합니다.

```bash
py main.py
```

환경에 따라 아래 명령어를 사용할 수도 있습니다.

```bash
python main.py
```

## 기능 목록

- 퀴즈 풀기
- 퀴즈 추가
- 퀴즈 목록 보기
- 퀴즈 삭제
- 최고 점수 보기
- 퀴즈 데이터 저장 및 불러오기
- 최고 점수 저장

## 파일 구조

```text
프로젝트 루트/
├── main.py
├── state.json
├── README.md
└── .gitignore
```

## 데이터 파일 설명

### state.json

`state.json` 파일은 프로젝트 루트에 생성됩니다.  
퀴즈 목록과 최고 점수를 저장하는 JSON 파일입니다.

저장되는 주요 데이터는 다음과 같습니다.

```json
{
  "high_score": 0,
  "quizzes": [
    {
      "question": "문제 내용",
      "choices": ["선택지1", "선택지2", "선택지3", "선택지4"],
      "answer": 1
    }
  ]
}
```

프로그램은 `state.json`을 UTF-8 인코딩으로 저장하고 불러옵니다.

## Git 워크플로우
![alt text](<git log 그래프 결과-1.png>)

## 제출물

### GitHub 저장소 URL

https://github.com/내 아이디/파일 이름

### 개발 환경 설정
![alt text](<개발 환경 설정 1.png>) ![alt text](<개발 환경 설정 2.png>)

### 프로그램 실행 결과
![alt text](<퀴즈 1.png>)![alt text](<퀴즈 2.png>) ![alt text](<퀴즈 3.png>) ![alt text](<퀴즈 4-1.png>) ![alt text](<퀴즈 4-2.png>) ![alt text](<퀴즈 5.png>) ![alt text](<퀴즈 6.png>) 

### git log 그래프 결과
![alt text](<git log 그래프 결과.png>)
