import yaml
import streamlit as st
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities import LoginError
from streamlit_extras.switch_page_button import switch_page



# st.session_state.update(st.session_state)

# import the yaml file
with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
    
# stauth.Hasher.hash_passwords(config['credentials'])

# authenticator object
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    auto_hash=False
)

try:
    authenticator.login()
except LoginError as e:
    st.error(e)
    
if st.session_state['authentication_status']:
    st.session_state.authenticator = authenticator
    st.session_state.logged_in_flag = 'Yes'
    switch_page('Homepage')
elif st.session_state['authentication_status'] is False:
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status'] is None:
    st.warning('Please enter your username and password')
