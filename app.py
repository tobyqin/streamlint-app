"""
# My app

My first app made with Streamlit.
"""

import streamlit as st
import pandas as pd
import numpy as np
from utils import add_logo
from st_pages import show_pages_from_config,add_page_title

st.set_page_config(
   page_title="My Cool App",
   page_icon="🧊",
   layout="wide",
   initial_sidebar_state="expanded",
)

# from streamlit_extras.app_logo import add_logo

add_page_title()
show_pages_from_config()
add_logo()

# add kitten logo
# add_logo("https://placekitten.com/100/100")
# add_logo("https://placekitten.com/100/100", height=100)
st.header("Welcome to my app!")

# add_logo()


#
# from streamlit_extras.app_logo import add_logo
#
# # add kitten logo
# add_logo("https://placekitten.com/100/100")

df = pd.DataFrame({
    'first': [1, 3, 4, 5, 5],
    'second': [4, 5, 6, 7, 8],
})

# st.sidebar.page_link('app.py', label="Home", icon="🏠")
# st.sidebar.page_link("pages/demo.py", label="Demo", icon="🌠")
# st.sidebar.page_link("pages/example.py", label="Example", icon="🧭")
# st.sidebar.page_link("pages/footer.py", label="Footer")
# st.sidebar.page_link("pages/better_footer.py", label="Better Footer")
# st.sidebar.page_link("pages/logo.py", label="Logo")
# st.sidebar.page_link("pages/example.py", label="Example")
# st.sidebar.page_link("pages/hello.py", label="Hello")
# st.sidebar.page_link("pages/show_image.py", label="Image")


# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

st.sidebar.caption("Powered by tobyqin.cn")

# Insert containers separated into tabs:
tab1, tab2, tab3 = st.tabs(["Document", "API Reference", "Demo"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")

# You can also use "with" notation:
with tab1:
    st.radio('Select one:', [1, 2])
    # Three columns with different widths
    col1, col2, col3 = st.columns([3, 2, 2])
    # col1 is wider

    # Using 'with' notation:
    with col1:
        st.markdown(__doc__)

        st.text('Fixed width text')
        st.markdown('_Markdown_')  # see #*
        st.caption('Balloons. Hundreds of them...')
        st.latex(r''' e^{i\pi} + 1 = 0 ''')
        st.write('Most objects')  # df, err, func, keras!
        st.write(['st', 'is <', 3])  # see *
        st.title('My title')
        st.header('My header')
        st.subheader('My sub')
        st.code('for i in range(8): foo()')

    with col2:
        st.dataframe(df)
        st.table(df.iloc[0:10])
        st.json({'foo': 'bar', 'fu': 'ba'})
        st.metric(label="Temp", value="273 K", delta="1.2 K")

with tab2:
    data = 'hello'
    st.write("this is tab 2, hello guys")
    st.button('Hit me')
    st.checkbox('Check me out')
    st.radio('Pick one:', ['nose', 'ear'])
    st.selectbox('Select', [1, 2, 3])
    st.multiselect('Multiselect', [1, 2, 3])
    st.slider('Slide me', min_value=0, max_value=10)
    st.select_slider('Slide to select', options=[1, '2'])
    st.text_input('Enter some text')
    st.number_input('Enter a number')
    st.text_area('Area for textual entry')
    st.date_input('Date input')
    st.time_input('Time entry')
    st.file_uploader('File uploader')
    st.download_button('On the dl', data)
    # st.camera_input("一二三,茄子!")
    st.color_picker('Pick a color')

with tab3:
    st.balloons()
    st.snow()
    # st.toast('Mr Stay-Puft')
    st.error('Error message')
    st.warning('Warning message')
    st.info('Info message')
    st.success('Success message')
    st.exception(ValueError())
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

    x = st.slider('x')  # 👈 this is a widget
    st.write(x, 'squared is', x * x)

    name = st.text_input("Your name", key="name")

    # You can access the value at any point with:
    # st.session_state.name
    st.write(name)
