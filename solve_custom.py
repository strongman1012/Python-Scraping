import word_proc
import re
import streamlit as st

def solve(good, middle_letter, ml_label, ol_label):
    middle_letter = middle_letter.lower()
    good = good.lower()
    s = set([c for c in good])
    if not middle_letter:
        st.write(f"please indicate {ml_label}")
        return 1;
    if len(good) != 7:
        st.write("please enter 6 characters into '{ol_label}' and one letter into '{ml_label}'")
        return 1
    if not re.match(r'^[a-zA-Z]+$',good):
        st.write("please only enter letters for custom board")
        return 1;
    if len(s) != 7:
        st.write("do not include duplicate letters")
        return 1
    if 's' in good:
        st.write("spelling bee words cannot include 's'")
        return 1

    bad_letters = word_proc.get_bad_letters(good)
    words = word_proc.get_words()
    good_words = word_proc.get_good_words(bad_letters,words, middle_letter)
    st.write(good_words)
if __name__ == "__main__":
    pass
