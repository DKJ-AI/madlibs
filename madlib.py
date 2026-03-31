import streamlit as st

st.set_page_config(page_title="MIDLABS", layout="centered")
st.title("MIDLABS")

st.subheader("Fill in the blanks to generate your interview story!")

noun = st.text_input("Noun:")
verb = st.text_input("Verb (-ing):")
adjective = st.text_input("Adjective:")
animal = st.text_input("Animal:")
past_tense_verb = st.text_input("Past Tense Verb:")
plural_noun = st.text_input("Plural Noun:")

story = f"""
Good morning!
My name is **{noun}** and I am extremely passionate about **{verb}**.
My greatest strength is that I am incredibly **{adjective}**.
In my last role, I managed a team of twelve **{animal}s**,
and together we successfully **{past_tense_verb}** over 400 **{plural_noun}** per quarter.
I believe I would be a perfect fit for this company.
"""

if st.button("Generate Story"):
    if all([noun, verb, adjective, animal, past_tense_verb, plural_noun]):
        st.markdown(story)
    else:
        st.warning("Please fill in all the blanks first!")