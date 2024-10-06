import streamlit as st

# drones, environmental - air, temp plot, data visualization, sensors - cattle temp, location, 
# live videos
# inventory items - livestock - cattle, hen, hogs, turkeys
# commodities - milk, eggs, honey, wool, butter, cheese, beef, buttermilk, mutton, whey
#     


st.set_page_config(layout='wide')
st.title('Inventory')
st.subheader('Livestock')
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image('images/cow.jpg')
    st.markdown("""
    <div class="card">
        <center><h4><b>Cows</b></h4></center>
        <center><p>Quantity: 200</p></center>
    </div>

    <style>
    .card {
        /* Add shadows to create the "card" effect */
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        transition: 0.3s;
        padding: 2px 16px;
    }

    /* On mouse-over, add a deeper shadow */
    .card:hover {
        box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

with col2:
    st.image('images/hog.jpg')
    st.markdown("""
    <div class="card">
        <center><h4><b>Pigs</b></h4></center>
        <center><p>Quantity: 30</p></center>
    </div>

    <style>
    .card {
        /* Add shadows to create the "card" effect */
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        transition: 0.3s;
        padding: 2px 16px;
    }

    /* On mouse-over, add a deeper shadow */
    .card:hover {
        box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

with col3:
    st.image('images/turkey.jpg')
    st.markdown("""
    <div class="card">
        <center><h4><b>Turkeys</b></h4></center>
        <center><p>Quantity: 10</p></center>
    </div>

    <style>
    .card {
        /* Add shadows to create the "card" effect */
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        transition: 0.3s;
        padding: 2px 16px;
    }

    /* On mouse-over, add a deeper shadow */
    .card:hover {
        box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

with col4:
    st.image('images/hen.jpg')
    st.markdown("""
    <div class="card">
        <center><h4><b>Hen</b></h4></center>
        <center><p>Quantity: 10</p></center>
    </div>

    <style>
    .card {
        /* Add shadows to create the "card" effect */
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        transition: 0.3s;
        padding: 2px 16px;
    }

    /* On mouse-over, add a deeper shadow */
    .card:hover {
        box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

st.write('')
st.subheader('Commodities')
col1, col2, col3, col4 = st.columns(4)

with col1:
    # st.image('images/cow.jpg')
    st.markdown("""
    <div class="card">
        <center><h4><b>Beef</b></h4></center>
        <center><p>Quantity: 200</p></center>
    </div>
    <div class="card">
        <center><h4><b>Eggs</b></h4></center>
        <center><p>Quantity: 200</p></center>
    </div>

    <style>
    .card {
        /* Add shadows to create the "card" effect */
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        transition: 0.3s;
        padding: 2px 16px;
    }

    /* On mouse-over, add a deeper shadow */
    .card:hover {
        box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

with col2:
    # st.image('images/hog.jpg')
    st.markdown("""
    <div class="card">
        <center><h4><b>Pork</b></h4></center>
        <center><p>Quantity: 30</p></center>
    </div>
    <div class="card">
        <center><h4><b>Honey</b></h4></center>
        <center><p>Quantity: 30</p></center>
    </div>

    <style>
    .card {
        /* Add shadows to create the "card" effect */
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        transition: 0.3s;
        padding: 2px 16px;
    }

    /* On mouse-over, add a deeper shadow */
    .card:hover {
        box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

with col3:
    # st.image('images/turkey.jpg')
    st.markdown("""
    <div class="card">
        <center><h4><b>Mutton</b></h4></center>
        <center><p>Quantity: 10</p></center>
    </div>
    <div class="card">
        <center><h4><b>Wool</b></h4></center>
        <center><p>Quantity: 30</p></center>
    </div>

    <style>
    .card {
        /* Add shadows to create the "card" effect */
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        transition: 0.3s;
        padding: 2px 16px;
    }

    /* On mouse-over, add a deeper shadow */
    .card:hover {
        box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

with col4:
    # st.image('images/hen.jpg')
    st.markdown("""
    <div class="card">
        <center><h4><b>Milk</b></h4></center>
        <center><p>Quantity: 10</p></center>
    </div>
    <div class="card">
        <center><h4><b>Butter</b></h4></center>
        <center><p>Quantity: 30</p></center>
    </div>

    <style>
    .card {
        /* Add shadows to create the "card" effect */
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        transition: 0.3s;
        padding: 2px 16px;
    }

    /* On mouse-over, add a deeper shadow */
    .card:hover {
        box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

