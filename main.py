import streamlit as st
import requests
import json
import webbrowser
import os
from flask import Flask, render_template
import googlemaps
import time
from IPython.display import HTML

st.title('KICT, REC')

col1, col2 = st.columns(2)

import streamlit as st
# Using "with" notation

import base64
import requests
import streamlit as st
import googlemaps
import gmaps
import requests
import json

# import requests
# import streamlit as st
#
# # Google Cloud Console에서 발급 받은 API 키
# API_KEY = "AIzaSyDp_ImeL1d6jFP3sSmfUHz0-7fCn7qNM0s"
#
# # Google Places API에서 Autocomplete 요청 보내기
# def autocomplete(query):
#     url = f"https://maps.googleapis.com/maps/api/place/autocomplete/json?input={query}&types=geocode&key={API_KEY}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         results = response.json().get("predictions")
#         if results:
#             return [result["description"] for result in results]
#     return []
#
# # Streamlit에서 검색창 생성하기
# search_query = st.text_input("Enter a location", "한국건설기술연구원")
#
# # 검색창에 입력한 내용과 유사한 지명 출력하기
# if search_query:
#     search_results = autocomplete(search_query)
#     if search_results:
#         st.write("Related locations:")
#         for result in search_results:
#             st.write(result)

# Maps Static API 사용자 키
API_KEY = "AIzaSyAp8lyCAnY6olMYEDW-dyGM6-GgMsJfQ3U"

# def get_autocomplete_predictions(input_text):
#     url = f'https://maps.googleapis.com/maps/api/place/autocomplete/json?input={input_text}&key={API_KEY}'
#     response = requests.get(url)
#     predictions = response.json().get('predictions')
#     suggestion_list = [prediction['description'] for prediction in predictions] if predictions else []
#     return suggestion_list

# 검색하려는 지역의 이름
with st.sidebar:
    location = st.text_input("Searching", "한국건설기술연구원")
    # # 검색어 추천 목록 가져오기
    # suggestion_list = get_autocomplete_predictions(location)
    # # 검색어 선택
    # selected_location = st.selectbox('검색어를 선택하세요', suggestion_list)
    # # 선택한 장소의 좌표 가져오기
    # url = f'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?key={API_KEY}&input={selected_location}&inputtype=textquery&fields=geometry'
    # response = requests.get(url)
    # result = response.json()
    #
    # if result['status'] == 'OK':
    #     candidates = result['candidates']
    #     if candidates:
    #         geometry = candidates[0].get('geometry')
    #         if geometry:
    #             location = geometry['location']
    #             lat, lng = location['lat'], location['lng']
    #         else:
    #             st.error('검색 결과에서 좌표 값을 찾을 수 없습니다.')
    #     else:
    #         st.warning('검색 결과가 없습니다.')
    # else:
    #     st.error(f'API 요청 실패: {result["status"]}')

# 지도 확대/축소 수준
zoom = st.slider('+/-', 10, 20, 15)

# 지도 이미지 크기
size = "640x640"

# Streamlit sidebar에서 지도 유형 선택
map_type = st.sidebar.selectbox(
    "Select a Map Type  ",
    ("roadmap", "satellite", "hybrid")
)

# Maps Static API 요청 URL 생성
url = f"https://maps.googleapis.com/maps/api/staticmap?center={location}&zoom={zoom}&size={size}&maptype={map_type}&key={API_KEY}"

# Maps Static API에서 이미지 가져오기
response = requests.get(url)

# 이미지 데이터를 base64로 인코딩
image_data = base64.b64encode(response.content).decode("utf-8")

# 인코딩된 이미지를 HTML 이미지 태그에 삽입
html_img = f'<img src="data:image/png;base64,{image_data}" alt="{location}">'


#Streamlit에서 이미지 표시
st.write(html_img, unsafe_allow_html=True)
