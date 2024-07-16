import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


# import json
# key_dict = json.loads(st.secrets["textkey"])

# Fetch the service account key JSON file contents

# Initialize the app with a service account, granting admin privileges
if not firebase_admin._apps:
    cred = credentials.Certificate('secrets.json')
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://streamlit-92189-default-rtdb.firebaseio.com/'
    })

ref = db.reference()
ref2 = db.reference()
ref3 = db.reference()
with st.form("my_form"):
    name = st.text_input("name")
    input1 = st.text_input("user")
    input2 = st.text_input("password", type="password")




    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        ref.push({"{0}".format(name):"({0}, {1})".format(input1, input2)})




if 'result' not in st.session_state:
    st.session_state['result'] = 0
if 'text' not in st.session_state:
    st.session_state['text'] = []
if 'next' not in st.session_state:
    st.session_state['next'] = 0


st.title("hello world")

st.header("hello world2")

st.subheader("hello world3")

st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")


code = '''import streamlit as st
st.write("hello world")'''
st.code(code, language='python')

st.divider()


temp = ""
temp = st.text_input("댓글", "")
if st.button("작성"):
    if temp != "":
        st.session_state['text'].append(temp)
    for i in st.session_state['text']:
        st.write(i)
