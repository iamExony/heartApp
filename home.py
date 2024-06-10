import streamlit as st
from streamlit_option_menu import option_menu
import pickle
import numpy as np
import heart, about

def app():
    st.write('<style>div.row-widget.stRadio>div{flex-direction:row;}</style>',unsafe_allow_html=True)
        
    selected2 = option_menu(None, ["Home", "PREDICT HEART DISEASE", 'DEVELOPER DETAILS'], 
    icons=['house', "activity", 'envelope'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={"container": {"padding": "0!important", "background-color": "#000000"},
        "icon": {"color": "red", "font-size": "20px"}, 
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#413839","color":"#FFFFFF"},
        "nav-link-selected": {"background-color": "#000000"},
         })
        
    
        
    if selected2 == 'Home':  
        new_title = '<p style="font-family:Georgia; color:#000000; font-size: 34px;">GUIDELINES OF THE HEART APP</p>'
        st.markdown(new_title, unsafe_allow_html=True)
        new_title = '<p style="font-family:Open Sans; font-size: 24px;">The Heart app aims at helping people by diagnosing coronary artery blockage and heart disease immediately. The main advantage is, it diagnose the disease automatically without the help of doctor. Using Artificial Intelligence(AI) the app is developed and make sure to consult the doctor for the confirmation of diseases.</p>'
        st.markdown(new_title, unsafe_allow_html=True)
        new_title = '<p style="font-family:Georgia; color:#000000; font-size: 34px;">HOW TO PREVENT HEART PROBLEMS ?</p>'
        st.markdown(new_title, unsafe_allow_html=True)
        
        st.write('⭕ Don’t smoke or use tobacco')
        st.write('⭕ Manage high cholesterol, high blood pressure and diabetes')
        st.write('⭕ Eat a heart-healthy diet.')
        
        st.write ('⭕ Limit alcohol use')
        st.write('⭕ Manage stress')
        st.write('⭕ Increase your activity level. Exercise helps you lose weight, improve your physical condition and relieve stress.')
        st.write('⭕ Do 30 minutes of walking 5 times per week or walking 10,000 steps per day')
        
        new_title = '<p style="font-family:Georgia; color:#000000; font-size: 34px;">SOME FACTS ABOUT THE HEART</p>'
        st.markdown(new_title, unsafe_allow_html=True)
        st.write('⭕ The average heart is the size of a fist in an adult')
        st.write('⭕ Your heart will beat about 115,000 times each day')
        st.write('⭕ Your heart pumps about 2,000 gallons of blood every day')
        st.write('⭕ The heart pumps blood through 60,000 miles of blood vessels')
        st.write('⭕ A woman’s heart beats slightly faster than a man’s heart')
        st.write ('⭕ The heart can continue beating even when it’s disconnected from the body')
        
        st.write('⭕ Laughing is good for your heart. It reduces stress and gives a boost to your immune system')
                    
    
    if selected2 == 'DEVELOPER DETAILS':
        new_title = '<p style="font-family:Georgia; color:##00FFFF; font-size: 29px;">CONSULT THE DOCTOR AND BOOK AN APPOINTMENT</p>'
        st.markdown(new_title, unsafe_allow_html=True)
        about.app()
        

                
    if selected2  == 'PREDICT HEART DISEASE':
        heart.app()
        