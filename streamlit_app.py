import streamlit

streamlit.title('My first web data application')
streamlit.header ('Application Header')
streamlit.text('👍Test line one')
streamlit.text('✌Test line 2')
streamlit.text('🤞Test line thrice')

streamlit.header ('🎶Get some data🤦‍♀️')

import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
