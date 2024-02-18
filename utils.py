import streamlit as st


def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(http://placekitten.com/100/100);
                background-repeat: no-repeat;
                padding-top: 100px;
                background-position: 20px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "BetaCat Cooperation Ltd.";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 20px;
                position: relative;
                top: 50px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )