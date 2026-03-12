import streamlit as st

# --- 1. SESSION STATE ---
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'saved' not in st.session_state:
    st.session_state.saved = False

# --- 2. PASSWORD PROTECTION ---
if not st.session_state.authenticated:
    st.title("🌌 Deep Space Terminal")
    pwd = st.text_input("Access Code Required:", type="password")
    if st.button("Initialize Terminal"):
        if pwd == "sagan":  # Your secret access password
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Access Denied: Terminal Locked.")
    st.stop()

# --- 3. MAIN APP INTERFACE ---
st.title("🌠 The Final Code")

if not st.session_state.saved:
    st.markdown("### Enter the last code to free **Teus**:")
    
    # Text area is better for long quotes than a single line input
    user_input = st.text_area("Input sequence here...", placeholder="Type the quote...")

    if st.button("Transmit Code"):
        # The specific quote you required
        target_code = "the cosmos is also within us we are made of star-stuff we are a way for the cosmos to know itself"
        
        if user_input.lower().strip() == target_code:
            st.session_state.saved = True
            st.rerun()
        else:
            st.error("The cosmos remains silent. Code incorrect.")
            st.info("Hint: It's a famous Carl Sagan quote.")

else:
    # --- 4. SUCCESS STATE ---
    st.balloons()
    st.success("## 🎊 You save Teus! Congratulations!")
    st.image("https://admision.tec.mx/talentoemprendedor/img/teus.webp") # Optional space gif
    
    if st.button("Reset Mission"):
        st.session_state.saved = False
        st.rerun()
