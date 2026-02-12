import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# -----------------------
# PAGE CONFIG
# -----------------------
st.set_page_config(
    page_title="Glacier Monitoring AI",
    page_icon="🗻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------
# SIDEBAR MENU
# -----------------------
st.sidebar.title("Navigation")
menu = ["Home", "Glacier Monitoring", "Melting Rate Detection", "Community Alerts"]
choice = st.sidebar.radio("Go to", menu)

# -----------------------
# HOME PAGE
# -----------------------
if choice == "Home":
    st.title("Glacier Monitoring & Melting Rate Detection ❄️")
    st.markdown("""
    ### AI-driven monitoring of glaciers using Sentinel-2 and Landsat satellite data.
    
    This system tracks glacier size changes, analyzes melting rates, and predicts potential climate impacts.  
    Alerts can help communities prepare for water shortages or flooding due to glacial melting.
    """)
    
    st.image("https://images.unsplash.com/photo-1504203702563-2a6f7680c3fa?auto=format&fit=crop&w=1650&q=80", use_column_width=True)
    
    st.markdown("---")
    st.subheader("Key Features")
    st.markdown("""
    - **Glacier Tracking:** Analyze glacier boundaries from satellite images.  
    - **Melting Rate Analysis:** Detect changes in glacier size over time.  
    - **AI Predictions:** Forecast climate impact and water availability.  
    - **Community Alerts:** Early warnings for floods or water shortages.
    """)

# -----------------------
# GLACIER MONITORING PAGE
# -----------------------
elif choice == "Glacier Monitoring":
    st.title("Glacier Monitoring 🗻")
    st.write("Analyze glacier size and coverage over time.")

    # Simulated glacier data (replace with real satellite data later)
    dates = pd.date_range(start="2015-01-01", end="2025-01-01", freq="Y")
    glacier_area = np.linspace(1000, 650, len(dates))  # Example decreasing glacier area
    df = pd.DataFrame({"Year": dates.year, "Glacier Area (km²)": glacier_area})

    fig = px.line(df, x="Year", y="Glacier Area (km²)", markers=True, title="Glacier Area Over Time")
    st.plotly_chart(fig, use_container_width=True)

# -----------------------
# MELTING RATE DETECTION PAGE
# -----------------------
elif choice == "Melting Rate Detection":
    st.title("Glacier Melting Rate Detection 🔥")
    st.write("Detecting melting rates and projecting future impacts.")

    # Example interactive slider for projection
    reduction_rate = st.slider("Select annual reduction rate (%)", 0, 10, 2)
    projected_area = glacier_area * (1 - reduction_rate / 100) ** np.arange(len(glacier_area))
    df["Projected Area"] = projected_area

    fig2 = px.line(df, x="Year", y=["Glacier Area (km²)", "Projected Area"], markers=True,
                   title="Glacier Area vs Projected Area")
    st.plotly_chart(fig2, use_container_width=True)

# -----------------------
# COMMUNITY ALERTS PAGE
# -----------------------
elif choice == "Community Alerts":
    st.title("Community Alerts 🚨")
    st.write("AI-based alerts for communities based on glacier melting trends.")

    st.markdown("""
    - **Water Shortage Risk:** Rising risk if glacier area falls below threshold.  
    - **Flood Risk:** Increased meltwater during summer months may cause flooding.  
    """)
    
    # Example alert
    latest_glacier_area = glacier_area[-1]
    if latest_glacier_area < 700:
        st.error(f"⚠️ Alert! Glacier area is critically low: {latest_glacier_area:.1f} km²")
    else:
        st.success(f"✅ Glacier area is stable: {latest_glacier_area:.1f} km²")
