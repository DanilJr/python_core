def filter_words(st):
    st.lower()
    while '  ' in st:
        st.replace('  ',' ')
    return st.capitalize()