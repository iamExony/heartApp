import pickle
import streamlit as st
import numpy as np

# loading the saved models
loaded_model = pickle.load(open('heart_disease_model.sav', 'rb'))

def heart(input_data):

    input_data_as_numpy_array = np.asarray(input_data)
    input_reshape = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_reshape)
    
    if (prediction[0]==0):
        return st.success('The person does not have any heart disease')
    else:
        return st.error('The person is having heart disease')
        
        
def app():
    
    new_title = '<p style="font-family:Georgia; color:##000000; font-size: 34px;">HEART DISEASE PREDICTION</p>'
    st.markdown(new_title, unsafe_allow_html=True)
                                
    age = st.number_input('AGE')
    
    sex = st.radio("Select Gender: ", (1, 0))
    if (sex == 1):
        st.info("Male")
    else:
        st.info("Female")
    st.write('<style>div.row-widget.stRadio>div{flex-direction:row;}</style>',unsafe_allow_html=True)
        
    chestpaintype = st.radio("CHEST PAIN TYPE (0 = typical angina,1 = atypical angina,2 = non — anginal pain,3= asymptotic)",(0,1,2,3))
    
    restingbps = st.number_input('RESTING BLOOD PRESSURE')
    cholestrol = st.number_input('CHOLESTROL')
    
    fastingbloodsugar = st.radio("FASTING BLOOD SUGAR( > 120mg/dl : 1, else : 0)",(1,0))
    restingecg = st.radio("RESTING ECG(0-normal, 1-abnormal)",(0,1))
    maxheartrate = st.number_input('MAXIMUM HEART RATE ACHIEVED') 
    exerciseangina = st.radio("EXERCISE INDUCED ANGINA(1-yes, 0-no)",(1,0))
    oldpeak = st.number_input('ST DEPRESSION INDUCED BY EXERCISE REALTIVE TO REST')
    STslope = st.radio("PEAK EXERCISE ST SEGMENT(0 = upsloping,1 = flat,2= downsloping)",(0,1,2))
    ca = st.radio("NUMBER OF MAJOR VESSELS (0 = normal,1 = fixed defect,2 = reversable defect)",(0,1,2))
    thal = st.radio("THAL ((0-3) colored by flourosopy)",(0,1,2,3))
    #number of major vessels (0-3) colored by flourosopy
    #thal: 0 = normal; 1 = fixed defect; 2 = reversable defect
    
    diagnosis = ''
    
    if st.button('PREDICT'):
        diagnosis = heart([age,sex,chestpaintype,restingbps,cholestrol,fastingbloodsugar,restingecg,maxheartrate,exerciseangina,oldpeak,STslope,ca,thal])
        
    



