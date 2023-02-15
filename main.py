
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
from utils import hide_table_index, hide_dataframe_index
import pandas as pd
from pathlib import Path

Image.MAX_IMAGE_PIXELS = None

page_style = """
        <style>
        #MainMenu {visibility: hidden;}  
        footer  {visibility: hidden;}  
        div.css-1vq4p4l.e1fqkh3o4{padding: 2rem 1rem 1.5rem;}
        div.block-container{padding-top:3rem;}
        </style>
        """

# st.write('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)
# st.write('<style>div.css-1vq4p4l.e1fqkh3o4{padding: 4rem 1rem 1.5rem;}</style>', unsafe_allow_html=True)
path = "./data"
spartan_data1 = pd.read_csv(
    Path(path)/"celltype_info_first.csv", index_col=0)
spartan_data2 = pd.read_csv(
    Path(path)/"celltype_info_second.csv", index_col=0)

spartan_data1.dropna(inplace=True)
spartan_data2.dropna(inplace=True)


cell_count1 = pd.read_csv( Path(path)/"cell_count_first.csv")
cell_count1.index.name = None

cell_count2 = pd.read_csv( Path(path)/"cell_count_second.csv")
cell_count2.index.name = None

hide_dataframe_index()
hide_table_index()
def set_page_container_style(prcnt_width: int = 75):
    max_width_str = f"max-width: {prcnt_width}%;"
    st.markdown(page_style, unsafe_allow_html=True)
    st.markdown(f"""
                <style> 
                
                .appview-container .main .block-container{{{max_width_str}}}
                </style>    
                """,
                unsafe_allow_html=True,
                )


set_page_container_style(75)

with st.sidebar:
       
        choose2 = option_menu("Datasets", ["first sent", "second sent"],
                            icons=['clipboard-data',
                                    'lightning-charge'],
                            menu_icon="arrow-return-right", default_index=0,
                            styles={
            "container": {"padding": "5!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "18px"},
            "nav-link": {"font-size": "14px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "orange"},
        }
        )

if choose2 == "first sent":
    st.markdown('''###### Cell count:''')
    st.table(cell_count1)
    st.markdown('''###### Cell type info:''')
    st.dataframe(spartan_data1.style.format({'Number of genes': '{:.0f}','Number of proteins': '{:.0f}','Number of TFs': '{:.0f}', 'RNArate': '{:.2f}'}), use_container_width=True)

elif choose2 == "second sent":
    st.markdown('''###### Cell count:''')
    st.table(cell_count2)
    st.markdown('''###### Cell type info:''')        
    st.dataframe(spartan_data2.style.format({'number of genes': '{:.0f}','number of proteins': '{:.0f}', 'RNArate': '{:.2f}'}), use_container_width=True)