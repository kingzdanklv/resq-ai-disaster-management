import streamlit as st
import pandas as pd
import folium

from streamlit_folium import st_folium

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="ResQ AI | Monitoring System",
    page_icon="R",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# SAMPLE MONITORING DATA
# ==========================================

locations = pd.DataFrame([
    {
        "Location": "Gomti River Area",
        "Latitude": 26.8560,
        "Longitude": 80.9462,
        "Rainfall": 185,
        "Water Level": 9.2,
        "Risk": "HIGH"
    },
    {
        "Location": "Alambagh",
        "Latitude": 26.8137,
        "Longitude": 80.9020,
        "Rainfall": 120,
        "Water Level": 7.8,
        "Risk": "MEDIUM"
    },
    {
        "Location": "Hazratganj",
        "Latitude": 26.8500,
        "Longitude": 80.9460,
        "Rainfall": 65,
        "Water Level": 5.1,
        "Risk": "LOW"
    },
    {
        "Location": "Lucknow Central",
        "Latitude": 26.8467,
        "Longitude": 80.9366,
        "Rainfall": 95,
        "Water Level": 6.2,
        "Risk": "MEDIUM"
    }
])

# All coordinates and readings above are illustrative.
# They are not verified monitoring stations or measurements.

RISK_COLORS = {
    "LOW": "#36B37E",
    "MEDIUM": "#E5AA45",
    "HIGH": "#E46B70"
}

# ==========================================
# PROFESSIONAL DARK THEME
# ==========================================

st.markdown("""
<style>
@import url(
'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap'
);

:root {
    --background: #101820;
    --panel: #192530;
    --border: #344451;
    --text: #E8EDF2;
    --muted: #9BAAB7;
    --blue: #4B9FE1;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: var(--background);
    color: var(--text);
}

.block-container {
    max-width: 1400px;
    padding: 2rem 2rem 3rem 2rem;
}

[data-testid="stSidebar"] {
    background: #151F29;
    border-right: 1px solid var(--border);
}

h1, h2, h3 {
    color: var(--text);
}

.page-header {
    border-bottom: 1px solid var(--border);
    padding-bottom: 20px;
    margin-bottom: 25px;
}

.page-header h1 {
    font-size: 29px;
    font-weight: 700;
    margin: 8px 0;
}

.page-header p {
    color: var(--muted);
    font-size: 14px;
}

.eyebrow {
    color: var(--blue);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.5px;
}

.section-heading {
    font-size: 18px;
    font-weight: 600;
    margin: 28px 0 15px 0;
}

.metric-card {
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 7px;
    padding: 18px;
    min-height: 105px;
    margin-bottom: 12px;
}

.metric-label {
    color: var(--muted);
    font-size: 12px;
    font-weight: 600;
    letter-spacing: .4px;
}

.metric-value {
    color: var(--text);
    font-size: 29px;
    font-weight: 700;
    margin-top: 8px;
}

.metric-note {
    color: var(--muted);
    font-size: 11px;
    margin-top: 4px;
}

.panel {
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 7px;
    padding: 18px;
    margin-bottom: 14px;
}

.status {
    display: inline-block;
    font-size: 23px;
    font-weight: 800;
    letter-spacing: 1px;
    padding: 10px 17px;
    border-radius: 5px;
    margin: 10px 0;
}

.low {
    color: #54D6A0;
    background: #183A30;
    border: 1px solid #28684F;
}

.medium {
    color: #F3C46A;
    background: #3D321E;
    border: 1px solid #79602D;
}

.high {
    color: #FF8B91;
    background: #40262B;
    border: 1px solid #82434A;
}

div.stButton > button {
    background: #276DA6;
    color: white;
    border: 1px solid #3989C8;
    border-radius: 5px;
    font-weight: 600;
}

div.stButton > button:hover {
    background: #3586C3;
    color: white;
}

hr {
    border-color: var(--border);
}

footer {
    visibility: hidden;
}

@media(max-width: 640px) {
    .block-container {
        padding: 1rem 1rem 2rem 1rem;
    }

    .page-header h1 {
        font-size: 24px;
    }

    .metric-card {
        padding: 13px;
    }

    .metric-value {
        font-size: 24px;
    }

    .status {
        font-size: 19px;
    }
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# REUSABLE FUNCTIONS
# ==========================================

def page_header(title, subtitle, section):
    st.markdown(f"""
    <div class="page-header">
        <div class="eyebrow">{section}</div>
        <h1>{title}</h1>
        <p>{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)


def metric_card(label, value, note):
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">{label}</div>
        <div class="metric-value">{value}</div>
        <div class="metric-note">{note}</div>
    </div>
    """, unsafe_allow_html=True)


def risk_badge(level):
    css = {
        "LOW": "low",
        "MEDIUM": "medium",
        "HIGH": "high"
    }
    return (
        f'<span class="status {css[level]}">'
        f'{level} RISK</span>'
    )


def create_map(data):
    """Build an interactive demonstration monitoring map."""

    m = folium.Map(
        location=[26.8467, 80.9366],
        zoom_start=12,
        tiles="CartoDB dark_matter",
        control_scale=True
    )

    for _, row in data.iterrows():

        color = RISK_COLORS[row["Risk"]]

        popup_html = f"""
        <div style="width:190px;font-family:Arial;color:#202830">
            <h4>{row['Location']}</h4>
            <b>Risk:</b> {row['Risk']}<br>
            <b>Rainfall:</b> {row['Rainfall']} mm<br>
            <b>Water level:</b> {row['Water Level']} m
            <p style="font-size:11px">
                Demonstration data only
            </p>
        </div>
        """

        folium.CircleMarker(
            location=[
                row["Latitude"],
                row["Longitude"]
            ],
            radius=11,
            color=color,
            weight=2,
            fill=True,
            fill_color=color,
            fill_opacity=0.85,
            tooltip=row["Location"],
            popup=folium.Popup(
                popup_html,
                max_width=240
            )
        ).add_to(m)

    return m


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.markdown("# ResQ AI")
    st.caption("DISASTER MANAGEMENT SYSTEM")

    st.divider()

    page = st.radio(
        "MAIN MENU",
        [
            "Dashboard",
            "Risk Assessment",
            "Emergency Alerts",
            "About"
        ]
    )

    st.divider()

    st.markdown("**SYSTEM INFORMATION**")
    st.caption("Version 3.0")
    st.caption("Student project prototype")
    st.caption("Data mode: Demonstration")


# ==========================================
# DASHBOARD
# ==========================================

if page == "Dashboard":

    page_header(
        "Disaster Monitoring Dashboard",
        "Location-based overview of sample environmental indicators.",
        "RESQ AI / OVERVIEW"
    )

    # KPI CARDS

    st.markdown(
        '<div class="section-heading">Key Indicators</div>',
        unsafe_allow_html=True
    )

    high_count = int(
        (locations["Risk"] == "HIGH").sum()
    )
    medium_count = int(
        (locations["Risk"] == "MEDIUM").sum()
    )
    low_count = int(
        (locations["Risk"] == "LOW").sum()
    )

    c1, c2 = st.columns(2)

    with c1:
        metric_card(
            "MONITORED AREAS",
            str(len(locations)).zfill(2),
            "Sample locations"
        )

    with c2:
        metric_card(
            "HIGH-RISK AREAS",
            str(high_count).zfill(2),
            "Illustrative classification"
        )

    c3, c4 = st.columns(2)

    with c3:
        metric_card(
            "MEDIUM-RISK AREAS",
            str(medium_count).zfill(2),
            "Illustrative classification"
        )

    with c4:
        metric_card(
            "LOW-RISK AREAS",
            str(low_count).zfill(2),
            "Illustrative classification"
        )

    # INTERACTIVE MAP

    st.markdown(
        '<div class="section-heading">Geographic Risk Monitoring</div>',
        unsafe_allow_html=True
    )

    st.caption(
        "Select a risk category to filter the map. "
        "Tap a marker to inspect its sample readings."
    )

    risk_filter = st.multiselect(
        "Display risk categories",
        ["LOW", "MEDIUM", "HIGH"],
        default=["LOW", "MEDIUM", "HIGH"]
    )

    filtered_locations = locations[
        locations["Risk"].isin(risk_filter)
    ]

    map_object = create_map(filtered_locations)

    st_folium(
        map_object,
        height=430,
        width=None,
        use_container_width=True,
        returned_objects=[]
    )

    # MAP LEGEND

    l1, l2, l3 = st.columns(3)

    with l1:
        st.markdown(
            '<span style="color:#36B37E">● LOW</span>',
            unsafe_allow_html=True
        )

    with l2:
        st.markdown(
            '<span style="color:#E5AA45">● MEDIUM</span>',
            unsafe_allow_html=True
        )

    with l3:
        st.markdown(
            '<span style="color:#E46B70">● HIGH</span>',
            unsafe_allow_html=True
        )

    st.caption(
        "Map locations and risk readings are illustrative. "
        "They are not verified flood-risk zones or monitoring stations."
    )

    # ENVIRONMENTAL CHARTS

    st.markdown(
        '<div class="section-heading">Environmental Analytics</div>',
        unsafe_allow_html=True
    )

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:

        st.markdown("**Rainfall by Location**")

        rainfall_df = locations.set_index("Location")[
            ["Rainfall"]
        ]

        st.bar_chart(
            rainfall_df,
            color="#4B9FE1",
            height=260
        )

    with chart_col2:

        st.markdown("**Water Level by Location**")

        water_df = locations.set_index("Location")[
            ["Water Level"]
        ]

        st.bar_chart(
            water_df,
            color="#36B37E",
            height=260
        )

    # PIE CHART

    st.markdown(
        '<div class="section-heading">Risk Distribution</div>',
        unsafe_allow_html=True
    )

    pie_data = pd.DataFrame({
        "Risk": ["LOW", "MEDIUM", "HIGH"],
        "Areas": [
            low_count,
            medium_count,
            high_count
        ]
    })

    pie_spec = {
        "mark": {
            "type": "arc",
            "innerRadius": 55,
            "stroke": "#192530"
        },
        "encoding": {
            "theta": {
                "field": "Areas",
                "type": "quantitative"
            },
            "color": {
                "field": "Risk",
                "type": "nominal",
                "scale": {
                    "domain": ["LOW", "MEDIUM", "HIGH"],
                    "range": [
                        "#36B37E",
                        "#E5AA45",
                        "#E46B70"
                    ]
                },
                "legend": {
                    "title": "Risk category",
                    "labelColor": "#E8EDF2",
                    "titleColor": "#E8EDF2"
                }
            },
            "tooltip": [
                {"field": "Risk"},
                {"field": "Areas"}
            ]
        }
    }

    st.vega_lite_chart(
        pie_data,
        pie_spec,
        use_container_width=True
    )

    # LOCATION TABLE

    st.markdown(
        '<div class="section-heading">Location Register</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        locations[
            [
                "Location",
                "Rainfall",
                "Water Level",
                "Risk"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )

    st.info(
        "All dashboard figures are sample data. "
        "The system is not connected to live sensors, "
        "official alerts or verified shelter databases."
    )


# ==========================================
# RISK ASSESSMENT
# ==========================================

elif page == "Risk Assessment":

    page_header(
        "Risk Assessment",
        "Evaluate sample rainfall and water-level readings.",
        "RESQ AI / ASSESSMENT"
    )

    location_name = st.selectbox(
        "Monitoring location",
        locations["Location"].tolist()
    )

    rainfall = st.slider(
        "Rainfall (mm)",
        0,
        300,
        120
    )

    water = st.slider(
        "Water level (metres)",
        0.0,
        15.0,
        8.2,
        0.1
    )

    if rainfall >= 200 or water >= 10:
        risk = "HIGH"
        explanation = (
            "The sample readings cross the demonstration "
            "high-risk thresholds."
        )

    elif rainfall >= 100 or water >= 7:
        risk = "MEDIUM"
        explanation = (
            "The sample readings fall within the "
            "demonstration medium-risk range."
        )

    else:
        risk = "LOW"
        explanation = (
            "The sample readings fall within the "
            "demonstration low-risk range."
        )

    st.markdown(
        '<div class="section-heading">Assessment Result</div>',
        unsafe_allow_html=True
    )

    st.markdown(f"""
    <div class="panel">
        <div class="metric-label">MONITORING LOCATION</div>
        <h2>{location_name}</h2>
        <div class="metric-label">DEMO CLASSIFICATION</div>
        {risk_badge(risk)}
        <p>{explanation}</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        metric_card(
            "RAINFALL",
            f"{rainfall} mm",
            "Selected input"
        )

    with c2:
        metric_card(
            "WATER LEVEL",
            f"{water:.1f} m",
            "Selected input"
        )

    st.caption(
        "This is a rule-based demonstration, "
        "not a validated flood prediction model."
    )


# ==========================================
# EMERGENCY ALERTS
# ==========================================

elif page == "Emergency Alerts":

    page_header(
        "Emergency Alerts",
        "Illustrative notifications for monitored locations.",
        "RESQ AI / ALERT CENTRE"
    )

    alerts = [
        {
            "level": "HIGH",
            "title": "River Monitoring",
            "location": "Gomti River Area",
            "message": "Example high-risk notification."
        },
        {
            "level": "MEDIUM",
            "title": "Rainfall Monitoring",
            "location": "Alambagh",
            "message": "Example medium-risk notification."
        }
    ]

    for alert in alerts:

        st.markdown(f"""
        <div class="panel">
            <div class="metric-label">DEMONSTRATION ALERT</div>
            {risk_badge(alert["level"])}
            <h3>{alert["title"]}</h3>
            <p>{alert["message"]}</p>
            <p><b>Location:</b> {alert["location"]}</p>
        </div>
        """, unsafe_allow_html=True)

    st.warning(
        "These are simulated notifications, "
        "not official emergency warnings."
    )


# ==========================================
# ABOUT
# ==========================================

elif page == "About":

    page_header(
        "About ResQ AI",
        "Project information and system overview.",
        "RESQ AI / INFORMATION"
    )

    st.markdown("### Project Overview")

    st.write(
        "ResQ AI is a student project prototype that "
        "demonstrates how a digital disaster-management "
        "platform can organise environmental indicators, "
        "risk classifications and geographic information."
    )

    st.markdown("### System Modules")

    modules = [
        (
            "Monitoring Dashboard",
            "Overview of sample environmental indicators."
        ),
        (
            "Interactive Risk Map",
            "Geographic display of illustrative risk categories."
        ),
        (
            "Risk Assessment",
            "Rule-based classification of sample readings."
        ),
        (
            "Emergency Alerts",
            "Illustrative notifications by location."
        ),
        (
            "Analytics",
            "Rainfall, water-level and risk distribution charts."
        )
    ]

    for title, description in modules:

        st.markdown(f"""
        <div class="panel">
            <b>{title}</b>
            <p>{description}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### Technology Stack")

    st.write(
        "Python | Streamlit | Pandas | Folium | OpenStreetMap"
    )

    st.info(
        "The current application uses demonstration data. "
        "It does not connect to live sensors, official emergency "
        "services or verified geographic risk datasets."
    )


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "ResQ AI | Disaster Management Prototype | Version 3.0"
)
