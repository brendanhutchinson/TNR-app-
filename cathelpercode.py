import pandas as pd
import streamlit as st

run TNR.py

num_new_rows = st.sidebar.number_input("Add Rows",1,50)                
with st.form(key='add_record_form',clear_on_submit= True):
     st.subheader("Add Record")
     ncol = len(df.columns)
     cols = st.columns(int(ncol))
     for i, x in enumerate(cols):
            for j, y in enumerate(range(int(num_new_rows))):
                  records_val = x.text_input(f"{df.columns[i]}", key=j)
                  records_val_list.append(records_val)
                  newrow = pd.DataFrame(records_val_list)

            if st.form_submit_button("Add"):
                 df = pd.concat([newrow,df],ignore_index=True)
st.write(df)