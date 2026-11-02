

import streamlit as st

st.set_page_config(
    page_title="ResQ AI",
    page_icon="🌊",
    layout="wide"
)

# Dashboard styling
st.markdown("""
<style>
.stApp {
    background-color: #0B1628;
    color: white;
}
h1, h2, h3, p, label {
    color: white !important;
}
div[data-testid="stMetric"] {
    background: #172A43;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #285078;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🌊 ResQ AI")
st.sidebar.caption("Disaster Management System")

page = st.sidebar.radio(
    "NAVIGATION",
    [
        "Dashboard",
        "Risk Assessment",
        "Emergency Alerts",
        "About"
    ]
)

# Dashboard
if page == "Dashboard":

    st.title("🌊 ResQ AI Dashboard")
    st.write("AI Disaster Management & Response System")

    st.success("Welcome to ResQ AI Monitoring System")

    st.subheader("Disaster Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Risk Areas", "04")
    col2.metric("Active Alerts", "02")
    col3.metric("Safe Shelters", "12")

    st.divider()

    st.subheader("Flood Monitoring")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rainfall", "120 mm")

    with col2:
        st.metric("Water Level", "8.2 m")

    st.subheader("System Status")
    st.info("Demo dashboard. Live monitoring is not connected.")

# Risk Assessment
elif page == "Risk Assessment":

    st.title("🌧️ Flood Risk Assessment")

    rainfall = st.slider(
        "Rainfall (mm)", 0, 300, 100
    )

    water = st.slider(
        "Water Level (m)", 0.0, 15.0, 5.0
    )

    location = st.selectbox(
        "Select Location",
        ["Lucknow", "Gomti River Area",
         "Alambagh", "Hazratganj"]
    )

    if st.button("Analyze Risk"):

        if rainfall >= 150 or water >= 10:
            risk = "HIGH"
        elif rainfall >= 70 or water >= 6:
            risk = "MEDIUM"
        else:
            risk = "LOW"

        st.subheader("Assessment Result")
        st.write("Location:", location)

        if risk == "HIGH":
            st.error("HIGH FLOOD RISK")
        elif risk == "MEDIUM":
            st.warning("MEDIUM FLOOD RISK")
        else:
            st.success("LOW FLOOD RISK")

        st.caption(
            "Demo rules only. Not an official flood warning."
        )

# Emergency Alerts
elif page == "Emergency Alerts":

    st.title("🚨 Emergency Alert Center")

    st.warning("Demo Alert: Monitor heavy rainfall.")

    st.info(
        "Follow verified instructions from local authorities "
        "during actual emergencies."
    )

# About
elif page == "About":

    st.title("About ResQ AI")

    st.write(
        "ResQ AI is an AI-powered student project "
        "for disaster management and response."
    )

    st.write("Developed by a team of five students.")

    st.write("Frontend Developer: Member 4")

