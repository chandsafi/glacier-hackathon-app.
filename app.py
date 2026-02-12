import streamlit as st

# -----------------------
# PAGE CONFIG
# -----------------------
st.set_page_config(
    page_title="Glacier Explorer",
    page_icon="🗻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------
# HERO SECTION
# -----------------------
st.markdown(
    """
    <div style="background-image: url('https://images.unsplash.com/photo-1504203702563-2a6f7680c3fa?auto=format&fit=crop&w=1650&q=80'); 
                background-size: cover; padding: 100px; text-align: center; color: white; border-radius: 10px;">
        <h1 style="font-size:60px; font-weight:bold;">Glacier Explorer</h1>
        <p style="font-size:24px;">Discover the Majesty of Glaciers and Their Impact on Our Planet</p>
        <a href="#about" style="font-size:20px; color:white; background-color:#1f77b4; padding:10px 20px; border-radius:5px; text-decoration:none;">Learn More</a>
    </div>
    """, unsafe_allow_html=True
)

st.markdown("---")

# -----------------------
# ABOUT SECTION
# -----------------------
st.subheader("About Glaciers ❄️")
st.write("""
Glaciers are massive, slow-moving rivers of ice that shape our landscape and regulate Earth's climate.
They act as freshwater reservoirs and are sensitive indicators of climate change.
Understanding glaciers is crucial for environmental sustainability and disaster prevention.
""")

# -----------------------
# IMAGE SECTION (URLs)
# -----------------------
st.subheader("Glacier Images")
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://images.unsplash.com/photo-1586304105611-312e1d7dbe3c?auto=format&fit=crop&w=800&q=80", caption="Snowy Glacier")

with col2:
    st.image("https://images.unsplash.com/photo-1504198453319-5ce911bafcde?auto=format&fit=crop&w=800&q=80", caption="Iceberg")

with col3:
    st.image("https://images.unsplash.com/photo-1502334204862-3c5f6d41d24e?auto=format&fit=crop&w=800&q=80", caption="Glacial Valley")

st.markdown("---")

# -----------------------
# INTERACTIVE SLIDER
# -----------------------
st.subheader("Glacier Sizes Around the World 🌎")
size = st.slider("Select Glacier Size in km²", 0, 10000, 500)
st.write(f"The selected glacier size is **{size} km²**.")

st.markdown("---")

# -----------------------
# CALL TO ACTION
# -----------------------
st.subheader("Want to Learn More?")
if st.button("Explore Glacier Facts"):
    st.write("""
    - Glaciers cover 10% of Earth's land area.
    - They store 69% of the world's freshwater.
    - Glacial melting contributes to sea level rise.
    """)

