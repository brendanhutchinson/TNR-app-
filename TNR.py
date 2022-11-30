import pandas as pd
import streamlit as st
import folium 
from streamlit_js_eval import get_geolocation
import numpy as np


# create empty data frame with necessary columns

df = pd.read_csv('TNR_data.csv')

colums = ['TNR', 'num_kittens', 'health', 'borough', 'neighborhood', 'relative_loc', 
            'food', 'color','latitude', 'longitude' ]

st.cache(allow_output_mutation=True)


st.title('TNR data Collection App')

with st.form('myform', clear_on_submit= True):


    # get user location 

    location_box = st.checkbox("check box for Coordinates")

    if location_box:
        loc = get_geolocation()
        print(loc)



    a = st.multiselect(label = 'Previous TNR/Ear Snip' , options = ['yes','no','unsure'])
    b= st.number_input(label = 'number of kittens observed')
    c =st.multiselect(label = 'health', options = ['poor', 'fair', 'good', 'excellent'])
    d =st.multiselect(label='borough', options= ['manhattan', 'brooklyn', 'queens', 'Bronx', 'Staten Island'])
    e = st.text_input(label = 'neighborhood')
    f= st.text_input(label='relative location(text)')
    g= st.multiselect(label = 'food available', options=['yes','no'])
    h = st.text_input(label= 'color')


    submit = st.form_submit_button('Submit')


    if(submit):
        add = []
        # if loc['coords']['latitude'] != np.nan:
        if location_box == True:
            add.append([a,b, c,d,e,f,g,h,loc['coords']['latitude'],loc['coords']['longitude']])
        else:
            add.append([a,b,c,d,e,f,g,h,np.nan,np.nan])
        df.append(pd.DataFrame(add, columns=colums)) ## problem child 
        st.write(df.tail(1))
        #df.to_csv('TNR_data.csv')







    
    








