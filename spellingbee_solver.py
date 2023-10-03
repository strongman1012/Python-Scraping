import solve
import datetime
import streamlit as st
import solve_custom

if __name__ == "__main__":
    OUTER_LETTERS = 'outer letters'
    MIDDLE_LETTER = 'middle letter'
    st.markdown("<h style=\"color:#ffda00;font-size:50px;font-weight:bold;\">Get words for todays NYT Spelling Bee</h>", unsafe_allow_html = True)
    if st.button(f"get answers for spelling bee {datetime.date.today()}"):
        st.write("solving the spelling bee")
        solve.solve()
    vert_space = '<div style="padding: 100px 5px;"></div>'
    st.markdown(vert_space, unsafe_allow_html=True)
    st.markdown("<h style=\"color:#ffda00;font-size:50px;font-weight:bold;\">Solve A Custom Spelling Bee</h>", unsafe_allow_html = True)

    gl = st.text_input(OUTER_LETTERS, max_chars=6)
    ml=st.text_input(MIDDLE_LETTER, max_chars=1)
    gl += ml
    if st.button('get answers for custom'):
        solve_custom.solve(gl,ml,OUTER_LETTERS,MIDDLE_LETTER)


    with st.sidebar:
        st.title("created by Brian Salkas")
        st.header("Contribute")
        st.write("missing a word and/or contains invalid word?")
        st.write("open an issue or submit a pull request [here](https://github.com/brianSalk/spelling-bee-solver-frontend)")

