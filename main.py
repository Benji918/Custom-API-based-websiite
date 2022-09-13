import requests
import streamlit as st

title = st.text_input('Type the anime name and press Enter!')
if title:
    try:
        URL = 'https://api.jikan.moe/v4/anime'
        PARAMS = {
            'q': f'{title}'
        }
        re = requests.get(url=URL, params=PARAMS)
        response = re.json()
        print(response['data'][0])
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(response['data'][0]['images']['jpg']['large_image_url'])
        with col2:
            st.subheader(response['data'][0]['titles'][0]['title'])
            st.caption(f'Genre:  {response["data"][0]["genres"][0]["name"]} Year:  {response["data"][0]["year"]}')
            st.write(response['data'][0]['synopsis'])
            st.write(f"Anime url:  [link]({response['data'][0]['url']})")
            st.text(f"Rating: {response['data'][0]['score']}")
            st.progress(float(response['data'][0]['score'])/10)
    except:
        st.error('Anime not found!')
