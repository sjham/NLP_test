# To Sir. Park

--개인수업 질문들--

1. 처리한 결과를 저장..반복처리하지 않는게 좋다는 말에 대해?

2. 모듈 함수 폴더 관리 어떻게..중점을 둬야 하는 점은? 재사용, 편이성 
- 작은 function들 모듈 하나에 모아놓는게 좋은지 나눠놓는게 좋은지..합쳐놓으면 import all 가능. 나눠놓으면 하나하나 import.

3.모듈 여러개를 만들어놓고 실제 코딩을 하는 좋은 방법..모듈,function 이름, 패러미터, 리턴값 하나하나 기억하기 어려운데 하나하나 열어보면서 짜야하나?
개발자들은 어떻게?

4. 도커..내 개발환경을 개인저장소에 업로드..다른 곳에서 활용..필요한 것만 모아서 dockerfile 작성?  




***************************************



1. What I need to..
- 서로 다른 아래 두 개의 데이터 파일에서 비슷한 기사 제목끼리 행(raw) 매칭
- data_set폴더에 있는 data_tagged.csv와 raw_data_tagged.csv
- 즉 raw_data_tagged 파일의 title_tagged 열에서 data_tagged 파일의 title_tagged 열의 각 행과 일치하는 행을 찾아 매칭하는 것 

2. why
- 대학원생들이 손으로 기사를 카운팅에서 만든 원본(data.xlsx)에 기사 제목만 있고, 본문이 없어서 제목 쿼리로 인터넷 검색시도
- 손입력때 제목을 조금씩 바꿔서(예: '탈당 사태 봇물..민주당 위기오나' -->'탈당 봇물..민주당 위기') if a==b 불가
- 하여 대학원 파일에 기사 생성 날짜가 있어서 일단 방송국사이트(여기서는 KBS)에 들어가 해당 기간(data.xlsx의 198열까지)의 기사(제목, 본문 등)를 모두 긁음---> raw_data.csv    

3. I tried..
- 두 칼럼 데이터를 단어로 split해서 list로 만든 뒤,  for문으로 sequence matching하면 되겠다고 단순하게 생각
- 하여 원본 데이터를 정제해서 data_tagged.csv와 raw_data_tagged.csv를 만듦.
- 그런 뒤 아래 같은 식으로 for문 돌려보기로. 값을 보고 조정해갈 심산으로 일단 단어 매칭 threshold를 3으로 시작  
- for element in data_tagged['title_tagged']:
    for r_element in raw_data_tagged['title_tagged']:
      inter_value = set(element).intersection(set(r_element))
        if len(inter_value)> 3:
            raw_data1['new_filtered_column'] = inter_value
 
 4.fail...
 - 매칭 결과를 리턴하긴 하긴함.(예: [set() set() set() set() set() set() {민주당, 봇물, 탈당} set() set() ..]
 - 그러나 원하는 결과만(매칭값 3이상 같은) 뽑아 매칭하는 방법을 못찾겠음. 위 코드 마지막라인(원래 데이터프레임에 칼럼을 생성해 값을 넣어라) 같은 방식으로는 불가(당연하지만 length mismatching 에러 발생)     
 - 하여 파이썬 라이브러리 sequence matcher(https://www.programcreek.com/python/example/1936/difflib.SequenceMatcher )같은 것 찾아서
 뒤적뒤적 해보다가 모두 실패하고 "이런방식 말고 이렇게 해보시면.."이라는 한마디 듣기위해 스승님을 찾게된 것임
 - 요것만 이틀째..즉 노력 안한 것은 아니고 하다가 머리가 꼬였음 
 
 Test file... 
 
a = [['위반', '차량', '암행', '단속', '시작'], ['차량', '암행', '단속','사랑','운행'],['암행', '단속', '시작']]
b = [['무제한', '위반'] ,['토론','단속', '시작', '끝'], ['테러', '방지법'], ['등', '운행', '처리']]

for i in a:
    for j in b:
        print(set(i).intersection(set(j)))
        
:{'위반'}
{'단속', '시작'}
set()
set()
set()
{'단속'}
set()
{'운행'}
set()
{'단속', '시작'}
set()
set()
        
