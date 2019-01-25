# To Sir. Park

1. What I need to..
- 서로 다른 아래 두 개의 데이터 파일에서 비슷한 기사 제목끼리 행(raw) 매칭
- data_set폴더에 있는 data_tagged.csv와 raw_data_tagged.csv
- 즉 raw_data_tagged 파일의 title_tagged 열에서 data_tagged 파일의 title_tagged 열의 각 행과 일치하는 행을 찾아 매칭하는 것 

2. why
- 대학원생들이 손으로 기사를 카운팅에서 만든 원본(data.xlsx)에 기사 제목만 있고, 본문이 없어서 제목 쿼리로 인터넷 검색시도
- 손입력때 제목을 조금씩 바꿔서(예: '탈당 사태 봇물..민주당 위기오나' -->'탈당 봇물..민주당 위기') if a==b 불가

3. I tried..
- 두 칼럼 데이터를 단어로 split해서 list로 만든 뒤,  for문으로 sequence matching하면 되겠다고 단순하게 생각
- 하여 데이터를 정제해서 data_tagged.csv와 raw_data_tagged.csv를 만들어 아래 같은 식으로 for문. 값을 보고 조정해갈 심산으로 일단 단어 매칭 threshold를 3으로 시작  
- for element in data_tagged['title_tagged']:
    for r_element in raw_data_tagged['title_tagged']:
      inter_value = set(element).intersection(set(r_element))
        if len(inter_value)> 3:
            raw_data1['new_filtered_column'] = inter_value
 
 4.fail...
 - 매칭 결과를 리턴하긴 하긴함.(예: [set() set() set() set() set() set() {민주당, 봇물, 탈당} set() set() ..]
 - 그러나 원하는 결과만(매칭값 3이상 같은) 뽑아 매칭하는 방법을 못찾겠음. 위 코드 마지막라인(원래 데이터프레임에 칼럼을 생성해 값을 넣어라) 같은 방식으로는 불가(당연하지만 length mismatching 에러 발생)     
 - 하여 파이썬 라이브러리 sequence matcher(https://www.programcreek.com/python/example/1936/difflib.SequenceMatcher )같은 것 찾아서
 뒤적뒤적 해보다가 모두 실패하고 스승님을 찾게된 것임
 - 요것만 이틀째..즉 노력 안한 것은 아니고 하다가 머리가 꼬였음 
 
 
