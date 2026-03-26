import streamlit as st
import random

# --- Keep facts in session state so they don’t reset ---
if "facts" not in st.session_state:
    st.session_state.facts = [
        "The first domain name ever registered was 'symbolics.com' on March            15, 1985.",
        "The entire Apollo 11 guidance computer code was less than 64KB—               smaller than a smartphone photo.",
        "IBM's Deep Blue beat world chess champion Garry Kasparov in 1997.",
        "The term 'Wi-Fi' doesn't stand for anything—it’s just a brand name.",
        "A 20TB hard drive can store about 5000 HD movies.",
        "A single Google search needs more power than the whole Apollo 11              mission.",
        "Error '404' was named after room 404 at CERN, birthplace of the              web.",
        "Siri comes from a Norwegian word meaning'beautiful victory'.",
        "Hi I'm Laiba"
    ]

st.set_page_config(page_title="Tech Facts displayed on tab", page_icon="💻")

st.title("💻 Tech Factsssss !!!!!!")
st.write("Click the button to see a random tech fact!")

# --- Show Random Fact ---
if st.button("Show Tech Fact"):
    random_fact = random.choice(st.session_state.facts)
    st.success(random_fact)

st.divider()

# --- Add New Fact ---
st.subheader("Add a New Fact")

new_fact = st.text_input("Type your new fact here:")

if st.button("Add Fact"):
    if new_fact.strip():
        st.session_state.facts.append(new_fact)
        st.success("Fact added successfully!")
    else:
        st.warning("Please enter a fact before adding.")
