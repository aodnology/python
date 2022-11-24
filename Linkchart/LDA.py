import pandas as pd
from pandas import DataFrame as df
# import numpy as np
# from konlpy import Okt
# import gensim
# from gensim import corpora, models
# from gensim.models import CoherenceModel

# okt = Okt()

Data = df.loc[:, ['cnt','title']]
Date = ['주가']
df = pd.read_json('주가.json',lines=False)
df = df[['cnt','title']]
Data = pd.concat([Data,df],ignore_index=True,axis= 0)
Data
# #데이터 프레임의 'text' 열의 값들을 str 형식으로 바꾸기
# Data.text = Data.text.astype(str)


# #데이터 프레임의 'text' 열의 값 중 keyword1이나 keyword 2가 포함된 행만 Data에 저장
# #clean_Data = Data.loc[Data['text'].str.contains('keyword1|keyword2')]

# #데이터 프레임의 'text' 열의 값 중 keyword1이나 keyword 2가 포함된 행은 삭제
# #clean_Data = Data[~Data['text'].str.contains('keyword1|keyword2')]


# #text와 timestamp 열을 기준으로 중복된 데이터를 삭제, inplace : 데이터 프레임을 변경할지 선택(원본을 대체)
# clean_Data.drop_duplicates(subset=['cnt','title'], inplace=True)

# #한글이 아니면 빈 문자열로 바꾸기
# clean_Data['title'] = clean_Data['title'].str.replace('[^ㄱ-ㅎㅏ-ㅣ가-힣]',' ',regex=True)

# #빈 문자열 NAN 값으로 바꾸기
# clean_Data = clean_Data.replace({'': np.nan})
# clean_Data = clean_Data.replace(r'^\s*$', None, regex=True)

# #NAN 이 있는 행은 삭제
# clean_Data.dropna(how='any', inplace=True)

# #인덱스 차곡차곡
# clean_Data = clean_Data.reset_index (drop = True)

# #데이터 프레임에 null 값이 있는지 확인
# print(clean_Data.isnull().values.any())

# #텍스트 데이터를 리스트로 변환
# Data_list=clean_Data.text.values.tolist()

# #리스트를 요소별로(기사 하나) 가져와서 명사만 추출한 후 리스트로 저장
# data_word=[]
# for i in range(len(Data_list)):
#     try:
#         data_word.append(okt.nouns(Data_list[i]))
#     except Exception as e:
#         continue

# #기사에서 명사만 추출해서 만든 리스트
# print(data_w)