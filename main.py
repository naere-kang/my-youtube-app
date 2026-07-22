스트림릿 앱 하나(main.py)를 만들어줘. 유튜브 댓글 분석 앱의 1단계야. 스트림릿 클라우드에 올릴 거야.

- 사용자가 유튜브 영상 링크를 붙여넣는 입력창을 만들어줘.
  입력창의 기본값은 https://youtu.be/d95J8yzvjbQ?si=LfL5DLwCL8Pk077r 로 해줘.
- 입력창 위에 예시 버튼 두 개를 나란히 넣어줘.
  '예시 1 · 딥마인드 다큐(영어 댓글)'를 누르면 기본값 링크가,
  '예시 2 · 2002 월드컵 추억(한국어 댓글)'을 누르면
  https://youtu.be/I9vK5EVTt0U?si=NEZ8L7MRuNvrzINa 링크가 입력창에 채워지게 해줘.
- 링크에서 영상 ID를 뽑아줘. youtu.be 짧은 주소든 youtube.com/watch 주소든
  다 처리하고, si= 처럼 링크 뒤에 붙는 값은 무시해.
- YouTube Data API v3의 commentThreads 창구에 requests로 요청해서
  댓글을 최대 100개 받아와. 요청변수 part는 snippet만,
  최신순 말고 좋아요가 많은 순으로 — 요청변수 order는 relevance로 줘.
  댓글 원문은 textOriginal, 좋아요 수는 likeCount 필드를 써.
  API 키는 비밀 금고(secrets)의 YOUTUBE_API_KEY에서 불러와.
- 받은 댓글을 좋아요가 많은 순으로 정렬해줘.
- 가져온 댓글 개수를 지표 카드로 크게 보여주고, 댓글 목록을 좋아요 수와 함께 표로 보여줘.
- 댓글을 못 가져오면(잘못된 링크, 댓글이 막힌 영상 등) 친절한 한국어 안내를 보여줘.
- 필요한 라이브러리 목록(requirements.txt)도 같이 줘.
  버전 숫자 없이 이름만, 스트림릿·판다스·넘파이는 기본 설치라 빼고.
  이 단계는 requests 하나면 돼.
- 초보자용 한국어 주석을 달고 main.py 전체 코드를 한 번에 줘.
