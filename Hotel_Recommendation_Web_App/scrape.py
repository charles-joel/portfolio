from pathlib import Path
import requests
import streamlit as st
import requests
from PIL import Image
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


THIS_DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
CSS_FILE = THIS_DIR / "style-css.css"


def load_css_file(css_file_path):
    with open(css_file_path) as f:
        return st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)



st.set_page_config("Recommend-er",layout="centered")
st.markdown(" <h1 style='text-align: center'> Recommend-er  <h1> ", unsafe_allow_html=True)

load_css_file(CSS_FILE)


with st.form("search",True):
    col1,col2 = st.columns(2)
    keyword = col1.multiselect("Select hotels or restarants",['Hotels','Restaurants','Museums','Malls','Cinemas','Resorts','Beaches','Parks'])
    location = col2.text_input('Enter a location') 
    search = st.form_submit_button("Search")


st.write("")
st.write("")
st.write("")
st.write("")
st.write("")


if search:

    for keywords in keyword:
        if keywords == 'Hotels':
            page = requests.get(f'https://hotelbooking.com.ng/?s={location}')
            soup = BeautifulSoup(page.text,'lxml')
            hotels = soup.find_all('div',class_='rooms-loops clear')
            

            for index,hotel in enumerate(hotels):
                tname = hotel.find_all("h3")
                tinfo = hotel.find_all("div",class_="rooms-content")
                image = hotel.find_all("img")
                
                for images in image:
                    img = images["src"]
                    response = requests.get(img, stream=True)
                    Img = Image.open(response.raw)

                    container = st.container()
                    col1,col2 = container.columns(2)

                    col1.image(Img)

                for names in tname:
                    name = names.getText()
                    redirect = names.find("a")['href']

                    col2.markdown(f"<h3 style='text-align: center'> {name} <h1> ", unsafe_allow_html=True)

                    
                    
                for infos in tinfo:
                    info = infos.getText()
                    
                    col2.write(f'{info}')
                    col2.markdown(f"<button class='btn'><a href='{redirect}'> Read More <a/></button>",unsafe_allow_html=True)


                    st.write("")
                    st.write("")
                    st.write("")
                    st.write("")
                    st.write("")


        if keywords == 'Restaurants':
                page = requests.get(f'https://hotels.ng/places/restaurants-in-{location}')
                soup = BeautifulSoup(page.text,'lxml')
                rest = soup.find_all("div",class_="listings-card card-house-dE01")

                for index,rests in enumerate(rest):
                        tname = rests.find_all("h2")
                        tinfo = rests.find_all("p",class_="sub-details")
                        image = rests.find_all("img")
                        link = rests.find_all("a",limit=1)
                            
                            
                        for images in image:
                            img = images["src"]
                            response = requests.get(img, stream=True)
                            Img = Image.open(response.raw)

                            container = st.container()
                            col1,col2 = container.columns(2)

                            col1.image(Img)
                            

                        for names in tname:
                            name = names.getText()

                            col2.markdown(f"<h3 style='text-align: center'> {name} <h1> ", unsafe_allow_html=True)


                            
                        for infos in tinfo:
                            info = infos.getText().split(".")[0:2]
                            

                            col2.write(f'{info}')
                            


                        for links in link:
                            redirect = links['href']
                            redirect = 'https://hotels.ng' + redirect

                            col2.markdown(f"<button class='btn'><a href='{redirect}'> Read More <a/></button>",unsafe_allow_html=True)
                            
                            st.write("")
                            st.write("")
                            st.write("")
                            st.write("")
                            st.write("")

                        



        if keywords == 'Museums':
                page = requests.get(f'https://hotels.ng/places/museums-in-{location}')
                soup = BeautifulSoup(page.text,'lxml')
                rest = soup.find_all("div",class_="listings-card card-house-dE01")

                for index,rests in enumerate(rest):
                        tname = rests.find_all("h2")
                        tinfo = rests.find_all("p",class_="sub-details")
                        image = rests.find_all("img")
                        link = rests.find_all("a",limit=1)
                            
                            
                        for images in image:
                            img = images["src"]
                            response = requests.get(img, stream=True)
                            Img = Image.open(response.raw)

                            container = st.container()
                            col1,col2 = container.columns(2)

                            col1.image(Img)
                            

                        for names in tname:
                            name = names.getText()

                            col2.markdown(f"<h3 style='text-align: center'> {name} <h1> ", unsafe_allow_html=True)


                            
                        for infos in tinfo:
                             info = infos.getText().split(".")[0:2]
                             col2.write(f'{info}')
                            


                        for links in link:
                            redirect = links['href']
                            redirect = 'https://hotels.ng' + redirect

                            col2.markdown(f"<button class='btn'><a href='{redirect}'> Read More <a/></button>",unsafe_allow_html=True)
                   
                            st.write("")
                            st.write("")
                            st.write("")
                            st.write("")
                            st.write("")


        if keywords == 'Cinemas':
                page = requests.get(f'https://hotels.ng/places/cinemas-in-{location}')
                soup = BeautifulSoup(page.text,'lxml')
                rest = soup.find_all("div",class_="listings-card card-house-dE01")

                for index,rests in enumerate(rest):
                        tname = rests.find_all("h2")
                        tinfo = rests.find_all("p",class_="sub-details")
                        image = rests.find_all("img")
                        link = rests.find_all("a",limit=1)
                            
                            
                        for images in image:
                            img = images["src"]
                            response = requests.get(img, stream=True)
                            Img = Image.open(response.raw)

                            container = st.container()
                            col1,col2 = container.columns(2)

                            col1.image(Img)
                            

                        for names in tname:
                            name = names.getText()

                            col2.markdown(f"<h3 style='text-align: center'> {name} <h1> ", unsafe_allow_html=True)


                            
                        for infos in tinfo:
                             info = infos.getText().split(".")[0:2]
                             col2.write(f'{info}')
                            


                        for links in link:
                            redirect = links['href']
                            redirect = 'https://hotels.ng' + redirect

                            col2.markdown(f"<button class='btn'><a href='{redirect}'> Read More <a/></button>",unsafe_allow_html=True)
                   
                            st.write("")
                            st.write("")
                            st.write("")
                            st.write("")
                            st.write("")
                            
                            
                        
        if keywords == 'Malls':
                page = requests.get(f'https://hotels.ng/places/malls-in-{location}')
                soup = BeautifulSoup(page.text,'lxml')
                rest = soup.find_all("div",class_="listings-card card-house-dE01")

                for index,rests in enumerate(rest):
                        tname = rests.find_all("h2")
                        tinfo = rests.find_all("p",class_="sub-details")
                        image = rests.find_all("img")
                        link = rests.find_all("a",limit=1)
                            
                            
                        for images in image:
                            img = images["src"]
                            response = requests.get(img, stream=True)
                            Img = Image.open(response.raw)

                            container = st.container()
                            col1,col2 = container.columns(2)

                            col1.image(Img)
                            

                        for names in tname:
                            name = names.getText()

                            col2.markdown(f"<h3 style='text-align: center'> {name} <h1> ", unsafe_allow_html=True)


                            
                        for infos in tinfo:
                             info = infos.getText().split(".")[0:2]
                             col2.write(f'{info}')
                            


                        for links in link:
                            redirect = links['href']
                            redirect = 'https://hotels.ng' + redirect

                            col2.markdown(f"<button class='btn'><a href='{redirect}'> Read More <a/></button>",unsafe_allow_html=True)
                   
                            
                            st.write("")
                            st.write("")
                            st.write("")
                            st.write("")
                            st.write("") 
                            
                        
        if keywords == 'Resorts':
                page = requests.get(f'https://hotels.ng/places/resorts-in-{location}')
                soup = BeautifulSoup(page.text,'lxml')
                rest = soup.find_all("div",class_="listings-card card-house-dE01")

                for index,rests in enumerate(rest):
                        tname = rests.find_all("h2")
                        tinfo = rests.find_all("p",class_="sub-details")
                        image = rests.find_all("img")
                        link = rests.find_all("a",limit=1)
                            
                            
                        for images in image:
                            img = images["src"]
                            response = requests.get(img, stream=True)
                            Img = Image.open(response.raw)

                            container = st.container()
                            col1,col2 = container.columns(2)

                            col1.image(Img)
                            

                        for names in tname:
                            name = names.getText()

                            col2.markdown(f"<h3 style='text-align: center'> {name} <h1> ", unsafe_allow_html=True)


                            
                        for infos in tinfo:
                             info = infos.getText().split(".")[0:2]
                             col2.write(f'{info}')
                            


                        for links in link:
                            redirect = links['href']
                            redirect = 'https://hotels.ng' + redirect

                            col2.markdown(f"<button class='btn'><a href='{redirect}'> Read More <a/></button>",unsafe_allow_html=True)
                   
                            st.write("")
                            st.write("")
                            st.write("")
                            st.write("")
                            st.write("")


                            
        if keywords == 'Beaches':
                page = requests.get(f'https://hotels.ng/places/beaches-in-{location}')
                soup = BeautifulSoup(page.text,'lxml')
                rest = soup.find_all("div",class_="listings-card card-house-dE01")

                for index,rests in enumerate(rest):
                        tname = rests.find_all("h2")
                        tinfo = rests.find_all("p",class_="sub-details")
                        image = rests.find_all("img")
                        link = rests.find_all("a",limit=1)
                            
                            
                        for images in image:
                            img = images["src"]
                            response = requests.get(img, stream=True)
                            Img = Image.open(response.raw)

                            container = st.container()
                            col1,col2 = container.columns(2)

                            col1.image(Img)
                            

                        for names in tname:
                            name = names.getText()

                            col2.markdown(f"<h3 style='text-align: center'> {name} <h1> ", unsafe_allow_html=True)


                            
                        for infos in tinfo:
                             info = infos.getText().split(".")[0:2]
                             col2.write(f'{info}')
                            


                        for links in link:
                            redirect = links['href']
                            redirect = 'https://hotels.ng' + redirect

                            col2.markdown(f"<button class='btn'><a href='{redirect}'> Read More <a/></button>",unsafe_allow_html=True)

                            st.write("")
                            st.write("")
                            st.write("")
                            st.write("")
                            st.write("")


                            
        if keywords == 'Parks':
                page = requests.get(f'https://hotels.ng/places/parks-in-{location}')
                soup = BeautifulSoup(page.text,'lxml')
                rest = soup.find_all("div",class_="listings-card card-house-dE01")

                for index,rests in enumerate(rest):
                        tname = rests.find_all("h2")
                        tinfo = rests.find_all("p",class_="sub-details")
                        image = rests.find_all("img")
                        link = rests.find_all("a",limit=1)
                            
                            
                        for images in image:
                            img = images["src"]
                            response = requests.get(img, stream=True)
                            Img = Image.open(response.raw)

                            container = st.container()
                            col1,col2 = container.columns(2)

                            col1.image(Img)
                            

                        for names in tname:
                            name = names.getText()

                            col2.markdown(f"<h3 style='text-align: center'> {name} <h1> ", unsafe_allow_html=True)


                            
                        for infos in tinfo:
                             info = infos.getText().split(".")[0:2]
                             col2.write(f'{info}')
                            


                        for links in link:
                            redirect = links['href']
                            redirect = 'https://hotels.ng' + redirect
                            col2.markdown(f"<button class='btn'><a href='{redirect}'> Read More <a/></button>",unsafe_allow_html=True)
                   
                            st.write("")
                            st.write("")
                            st.write("")
                            st.write("")
                            st.write("")
                            
                            
                        
                            
                            
                        
                                               
                        
                                                                               
                            
                        
                            