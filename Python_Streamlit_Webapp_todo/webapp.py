"""Streamlit powered todo webapp
you need to pip install streamlit To run the app type in streamlit run webapp.py to the terminal
(if you rename the file then use that file name)
make sure you are on the same directory
"""
import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)



st.title('Python ToDo App')
st.subheader('Streamlit powered ToDo App')
st.write('This app is designed to keep your ToDos in order.')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()



st.text_input(label='', placeholder='Add new ToDo and press enter...',
              on_change=add_todo, key='new_todo')
