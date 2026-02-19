import streamlit as st
import random

# Initialize scores
if "uscore" not in st.session_state:
    st.session_state.uscore = 0
    st.session_state.cscore = 0

choices = {
    1: "Stone 🪨",
    2: "Paper 📄",
    3: "Scissors ✂️"
}

# Title
st.title("🎮 Stone Paper Scissors Game")

# Score
st.subheader(f"Score → You: {st.session_state.uscore} | Computer: {st.session_state.cscore}")

# Buttons
user_choice = None

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Stone 🪨"):
        user_choice = 1

with col2:
    if st.button("Paper 📄"):
        user_choice = 2

with col3:
    if st.button("Scissors ✂️"):
        user_choice = 3

# Game Logic
if user_choice is not None:
    comp_choice = random.randint(1, 3)

    st.write(f"You chose: {choices[user_choice]}")
    st.write(f"Computer chose: {choices[comp_choice]}")

    if (user_choice == 1 and comp_choice == 3) or \
       (user_choice == 2 and comp_choice == 1) or \
       (user_choice == 3 and comp_choice == 2):

        st.session_state.uscore += 1
        st.success("You won this round 😎")

    elif user_choice == comp_choice:
        st.info("It's a draw 🤝")

    else:
        st.session_state.cscore += 1
        st.error("Computer won this round 🤖")

# Winner
if st.session_state.uscore == 5:
    st.success("🎉 You won the game!")
    st.balloons()

elif st.session_state.cscore == 5:
    st.error("💀 Computer won the game!")

# Reset
if st.button("Reset Game 🔄"):
    st.session_state.uscore = 0
    st.session_state.cscore = 0
    st.rerun()
