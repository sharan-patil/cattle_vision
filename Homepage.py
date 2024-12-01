import streamlit as st
import folium

from streamlit_folium import st_folium
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.app_logo import add_logo

### need a dependency packages installing file
### make it so that the config.yaml is loaded from GCP into strealit server

# from streamlit_authenticator.utilities.hasher import Hasher

# initiate and update global variables
if 'map_markers' not in st.session_state:
    st.session_state.map_markers = {
        1: {
            'type': 'Camera',
            'location': [30.885, -96.90]
        },
        2: {
            'type': 'Camera',
            'location': [30.885, -96.91]
        },
        3: {
            'type': 'Drone',
            'location': [30.881, -96.905]
        }
    }

#--- Init session_state
if 'active_page' not in st.session_state:
    st.session_state.active_page = 'Home'

if 'logged_in_flag' not in st.session_state:
    st.session_state.logged_in_flag = 'No'

if st.session_state.logged_in_flag == 'No':
    switch_page('Login')

# check if logged in
if not st.session_state['authentication_status']:
    switch_page('Login')

st.set_page_config(layout='wide')
st.title('Cattle Vision')

# st.markdown("""
#     <style>
#         .block-container {
#             padding-top: 5rem;
#             padding-bottom: 0rem;
#             padding-left: 10rem;
#             padding-right: 10rem;
#         }
#     </style>
# """, unsafe_allow_html=True)


st.markdown(f"<p style='font-size: 27px;'>Welcome, {st.session_state['name']}. Here's your ranch!</p>",
            unsafe_allow_html=True)

if "selected_camera" not in st.session_state:
    st.session_state.selected_camera = None

# menu = st.sidebar.selectbox("Select an option", ["Home", "User Input"])
# [30.885, -96.92]

# create buttons to add a camera or drone marker
@st.dialog("Provide the location info")
def provide_location(item, item_number):
    st.write(f"What is the location of the {item}?")
    reason = st.text_input("30.885, -96.92")
    location = reason.split(', ')
    if st.button("Submit"):
        if item == 'Camera':
            st.session_state.map_markers[item_number] = {
                'type': 'Camera',
                'location': location,
            }
        elif item == 'Drone':
            st.session_state.map_markers[item_number] = {
                'type': 'Drone',
                'location': location,
            }
        st.rerun()

st.markdown(f"<p style='font-size: 21px;'>What would you like to do today?</p>",
            unsafe_allow_html=True)
camera_col, drone_col = st.columns([1, 5])
map_markers = st.session_state.map_markers
with camera_col:
    if st.button("Add a camera 📸"):
        provide_location('Camera', max(map_markers.keys()) + 1)
with drone_col:
    if st.button("Add a drone 🚁"):
        provide_location('Drone', max(map_markers.keys()) + 1)

# Display the map
st.markdown(f"<p style='font-size: 21px;'>Here's a map of your ranch :)</p>",
            unsafe_allow_html=True)

m = folium.Map(
    location = [30.884841266378725, -96.90262402599888],
    zoom_start = 14,
    attr = 'Esri', 
    tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'
    )

# generate markers on map using map_markers dict
for marker in map_markers:
    icon = ''
    color = ''
    if map_markers[marker]['type'] == 'Camera':
        icon = 'fa-camera'
        color = 'blue'
    elif map_markers[marker]['type'] == 'Drone':
        icon = 'fa-helicopter'
        color = 'green'
    folium.Marker(
        location=map_markers[marker]['location'],
        tooltip=map_markers[marker]['type'] + ' ' + str(marker),
        icon=folium.Icon(color=color, icon=icon, prefix='fa')
    ).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width=775)

# 'Camera 1' or 'Camera 2'
st.session_state.selected_camera = st_data['last_object_clicked_tooltip']  

if st.session_state.selected_camera is not None:
    switch_page('Satellite Cameras')

st.session_state.authenticator.logout()



# http://localhost:8501/Contact_Us

# import urllib.parse
# session = st.runtime.get_instance()._session_mgr.list_active_sessions()[0]
# st_base_url = urllib.parse.urlunparse([session.client.request.protocol, session.client.request.host, "", "", "", ""])

# print(st_base_url)