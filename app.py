# Importing Required Libraries
import streamlit as st
import pandas as pd
from PIL import Image 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import base64

#Load Data
df = pd.read_csv("final_data.csv")
#Splitting Dataset into train & test
x = df[['age', 'sex', 'cp', 'trestbps', 
        'chol', 'fbs', 'restecg', 'thalach',
       'exang', 'oldpeak', 'slope']]
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
#Fitting Model
r_forest = RandomForestClassifier()
r_forest = r_forest.fit(X_train, y_train)

#Logo
image = Image.open('logo.jpg')
st.sidebar.image(image)

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('image.jpg') 

html_temp = """
    <div style ="background-color:#427f7e ;padding:8px; border-radius: 15px 50px ; font-family:Times, serif">
    <h1 style = "color:white; font-family:Times, serif;text-align:center;">Coronary Heart Disease Prediction</h2>
    </div>
    """    
st.markdown(html_temp, unsafe_allow_html=True)
st.markdown("##### *This is a Machine Learning Web App to predict whether a person is suffering from Coronary Heart Disease or not. A patient can enter his/her data by using sliders and click button from side bar penal.*")

st.sidebar.header("Patient Data")

#Function
st.subheader("Patient Data Input By User")
def user_report():
    age  = st.sidebar.slider("Age", 20, 100, 40)
    st.markdown("***Age***")
    st.info(age)
    sex = st.sidebar.radio("Gender: ", ('1', '0'))
    st.markdown("***Gender***")
    if (sex == '1'):
        st.info("Male")
    else:
        st.info("Female")
    cp = st.sidebar.radio("Chest Pain Type: ", ('0','1','2','3'))
    st.markdown("***Chest Pain Type***")        
    if (cp == '0'):
        st.info("Typical Angina")
    elif(cp == '1'):
        st.info("Atypical Angina")
    elif(cp == '2'):
        st.info("Non—Anginal Pain")
    else:
        st.info("Asymptotic")
    trestbps  = st.sidebar.slider('Resting Blood Pressure',0, 250, 150 )
    st.markdown("***Resting Blood Pressure***")        
    st.info(trestbps)
    st.markdown("***Cholesterol***")        
    chol  = st.sidebar.slider('Cholesterol',0, 603, 450)
    st.info(chol)
    st.markdown("***Blood Sugar***")        
    fbs = st.sidebar.radio("Blood Sugar: ", ('1', '0'))
    if (fbs == '1'):
        st.info("Yes")
    else:
        st.info("No")
    restecg = st.sidebar.radio("ECG: ", ('0','1'))
    st.markdown("***ECG Report***")        
    if (restecg == '0'):
        st.info("Normal")
    else:
        st.info("Abnormal")
    st.markdown("***Maximum Heart Rate Achieved***")        
    thalach = st.sidebar.slider('Maximum Heart Rate Achieved',0, 202, 150)
    st.info(thalach)
    exang  = st.sidebar.radio("Exercise Induced Angina(1-yes, 0-no)",('1','0'))
    st.markdown("***Exercise Induced Angina***")        
    if (exang == '1'):
        st.info("Yes")
    else:
        st.info("No")
    st.markdown("***ST Depression Induced by Exercise Relative to Rest***")        
    oldpeak = st.sidebar.slider('ST Depression Induced by Exercise Relative to Rest',0.0, 6.2, 3.0)
    st.info(oldpeak)
    slope = st.sidebar.radio("Slope of the peak exercise ST segment: ", ('0','1','2'))
    st.markdown("***Slope of the Peak Exercise ST Segment***")
    if (slope == '0'):
        st.info("Upsloping")
    elif(slope == '1'):
        st.info("Flat")
    else:
        st.info("Downsloping")
    
    user_report_data = {
    "age" : age,
    "sex" : sex,
    "cp" : cp,
    "trestbps" : trestbps,
    "chol" : chol,
    "fbs": fbs,
    "restecg" : restecg,
    "thalach" :thalach,
    "exang" :exang,
    "oldpeak" :oldpeak,
    "slope" :slope,
    }
    report_data = pd.DataFrame(user_report_data, index=[0])
    return report_data


#Patient Data
user_data = user_report()

user_result = r_forest.predict(user_data)
    
#Output
if st.button('Check Result'):
    st.header("Your Result: ")
    if user_result == 1:
        st.markdown('#### Please  Visit  to  a  Doctor,  Heart Condition is not Good 💔')
    else:
        st.markdown('#### Congratulations No Disease Detected ❤️')
        st.balloons()

#Mailbox
st.header(":mailbox: Comments")
st.markdown("**If you have any questions or suggestions, please leave a comment below.**")
contact_form = """
<form action="https://formsubmit.co/musharafahsan6@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button> 
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name, encoding='utf-8') as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style.css")


html_temp1 = """
    <div style="background-color:#427f7e">
    <p style="color:white; font-family:Times, serif;text-align:center;" >Made By: <b>Musharaf Ahsan</b> </p>
    </div>
    """
st.markdown(html_temp1,unsafe_allow_html=True)
