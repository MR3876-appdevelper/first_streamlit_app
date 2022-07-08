import streamlit

streamlit.title('My first web data application')
streamlit.header ('Application Header')
streamlit.text('👍Test line one')
streamlit.text('✌Test line 2')
streamlit.text('🤞Test line thrice')

streamlit.header ('🎶Get some data🤦‍♀️')

import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#create a pick list so a fruit can be selected
streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index))

#display the table on the page
streamlit.dataframe(my_fruit_list)
