
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="ResQ AI | Disaster Response",
    page_icon="🚨",
    layout="wide"
)

# ---------------- DARK THEME ----------------

st.markdown("""
<style>
.stApp {
    background-color: #101820;
    color: #EAF2F8;
}

section[data-testid="stSidebar"] {
    background-color: #17232E;
}

h1, h2, h3 {
    color: #EAF2F8 !important;
}

p, label {
    color: #C7D5E0;
}

div[data-testid="stMetric"] {
    background-color: #1B2B38;
    border: 1px solid #29465A;
    padding: 15px;
    border-radius: 12px;
}

div[data-testid="stMetricValue"] {
    color: #55B8F5;
}

.stButton button {
    background-color: #1677B8;
    color: white;
    border-radius: 8px;
    border: none;
}

hr {
    border-color: #29465A;
}
</style>
""", unsafe_allow_html=True)

# ---------------- DEMO DATA ----------------

data = {
    "Location": [
        "Gomti River Area",
        "Alambagh",
        "Hazratganj",
        "Lucknow Central"
    ],
    "Latitude": [
        26.8560,
        26.8137,
        26.8500,
        26.8467
    ],
    "Longitude": [
        80.9462,
        80.9020,
        80.9460,
        80.9366
    ],
    "Rainfall (mm)": [
        185,
        120,
        65,
        95
    ],
    "Water Level (m)": [
        9.2,
        7.8,
        5.1,
        6.2
    ],
    "Risk": [
        "HIGH",
        "MEDIUM",
        "LOW",
        "MEDIUM"
    ]
}

df = pd.DataFrame(data)

risk_colors = {
    "LOW": "green",
    "MEDIUM": "orange",
    "HIGH": "red"
}

# ---------------- SIDEBAR ----------------

st.sidebar.title("🚨 ResQ AI")

st.sidebar.caption("Disaster Management & Response System")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Risk Assessment",
        "Emergency Alerts",
        "About"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("Prototype project using illustrative demo data.")

# ---------------- DASHBOARD ----------------

if page == "Dashboard":

    st.title("🚨 ResQ AI Dashboard")
    st.write(
        "AI-assisted disaster monitoring and risk visualization."
    )

    st.markdown("---")

    # KPI METRICS

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Monitored Areas", len(df))
    col2.metric("High Risk", len(df[df["Risk"] == "HIGH"]))
    col3.metric("Medium Risk", len(df[df["Risk"] == "MEDIUM"]))
    col4.metric("Low Risk", len(df[df["Risk"] == "LOW"]))

    st.markdown("---")

    # RISK FILTER

    st.subheader("🗺️ Interactive Disaster Risk Map")

    selected_risks = st.multiselect(
        "Filter locations by risk level",
        ["LOW", "MEDIUM", "HIGH"],
        default=["LOW", "MEDIUM", "HIGH"]
    )

    filtered_df = df[df["Risk"].isin(selected_risks)]

    # CREATE MAP

    disaster_map = folium.Map(
        location=[26.8467, 80.9366],
        zoom_start=12,
        tiles="OpenStreetMap"
    )

    # ADD RISK MARKERS

    for _, row in filtered_df.iterrows():

        popup_text = f"""
        <b>{row['Location']}</b><br>
        Risk: {row['Risk']}<br>
        Rainfall: {row['Rainfall (mm)']} mm<br>
        Water Level: {row['Water Level (m)']} m
        """

        folium.CircleMarker(
            location=[
                row["Latitude"],
                row["Longitude"]
            ],
            radius=11,
            color=risk_colors[row["Risk"]],
            fill=True,
            fill_color=risk_colors[row["Risk"]],
            fill_opacity=0.8,
            popup=folium.Popup(popup_text, max_width=250),
            tooltip=f"{row['Location']} - {row['Risk']} RISK"
        ).add_to(disaster_map)

    st_folium(
        disaster_map,
        height=430,
        width=None,
        use_container_width=True,
        returned_objects=[]
    )

    # MAP LEGEND

    st.markdown("""
    **Risk Legend**

    🟢 LOW &nbsp;&nbsp;&nbsp;
    🟠 MEDIUM &nbsp;&nbsp;&nbsp;
    🔴 HIGH
    """)

    st.markdown("---")

    # CHARTS

    st.subheader("📊 Environmental Data")

    chart1, chart2 = st.columns(2)

    with chart1:
        st.write("Rainfall by Location")
        st.bar_chart(
            df.set_index("Location")["Rainfall (mm)"]
        )

    with chart2:
        st.write("Water Level by Location")
        st.bar_chart(
            df.set_index("Location")["Water Level (m)"]
        )

    st.markdown("---")

    st.subheader("📋 Location Risk Details")

    st.dataframe(
        filtered_df[
            [
                "Location",
                "Rainfall (mm)",
                "Water Level (m)",
                "Risk"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )

# ---------------- RISK ASSESSMENT ----------------

elif page == "Risk Assessment":

    st.title("🌧️ Disaster Risk Assessment")

    st.write(
        "Enter sample environmental readings to calculate "
        "a basic demonstration risk category."
    )

    rainfall = st.slider(
        "Rainfall (mm)",
        min_value=0,
        max_value=300,
        value=100
    )

    water_level = st.slider(
        "Water Level (m)",
        min_value=0.0,
        max_value=15.0,
        value=5.0,
        step=0.1
    )

    if st.button("Calculate Risk"):

        if rainfall >= 150 or water_level >= 8:
            risk = "HIGH"
            message = "Increased risk indicators detected."

        elif rainfall >= 80 or water_level >= 6:
            risk = "MEDIUM"
            message = "Moderate risk indicators detected."

        else:
            risk = "LOW"
            message = "Lower risk indicators in this demonstration."

        st.markdown("---")
        st.subheader("Assessment Result")

        if risk == "HIGH":
            st.error(f"🔴 {risk} RISK")

        elif risk == "MEDIUM":
            st.warning(f"🟠 {risk} RISK")

        else:
            st.success(f"🟢 {risk} RISK")

        st.write(message)

        st.caption(
            "This is a simple rule-based demonstration, "
            "not a validated prediction or official warning."
        )

# ---------------- EMERGENCY ALERTS ----------------

elif page == "Emergency Alerts":

    st.title("📢 Emergency Alerts")

    st.write(
        "Example alert categories for demonstrating "
        "the ResQ AI interface."
    )

    st.error(
        "🔴 HIGH RISK: Sample flood-risk indicator "
        "for the Gomti River Area."
    )

    st.warning(
        "🟠 MEDIUM RISK: Sample rainfall indicator "
        "for Alambagh."
    )

    st.info(
        "ℹ️ These are fictional demonstration alerts, "
        "not live emergency notifications."
    )

    st.markdown("---")

    st.subheader("Emergency Preparedness")

    st.markdown("""
    - Follow instructions from official local authorities.
    - Keep emergency contact information accessible.
    - Avoid entering flooded roads or waterways.
    - Use official weather and disaster-management updates.
    """)

# ---------------- ABOUT ----------------

elif page == "About":

    st.title("ℹ️ About ResQ AI")

    st.write("""
    **ResQ AI** is a student prototype for an
    AI-assisted disaster management and response system.

    The project demonstrates how technology can help
    organize environmental information and visualize
    possible disaster-risk indicators.
    """)

    st.subheader("Main Features")

    st.markdown("""
    - 🗺️ Interactive disaster-risk map
    - 📊 Environmental data visualization
    - 🌧️ Basic risk assessment
    - 📢 Demonstration emergency alerts
    - 🌑 Dark charcoal user interface
    """)

    st.subheader("Technology Used")

    st.markdown("""
    - Python
    - Streamlit
    - Pandas
    - Folium
    - OpenStreetMap
    """)

    st.markdown("---")

    st.caption(
        "ResQ AI is an educational prototype. "
        "Its sample locations, readings, risk levels, "
        "and alerts are illustrative only. "
        "It is not an operational emergency service."
    )

# ---------------- FOOTER ----------------

st.markdown("---")

st.caption(
    "ResQ AI | Student Disaster Management Prototype"
)
