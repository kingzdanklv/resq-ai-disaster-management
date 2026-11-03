
import streamlit as st
import pandas as pd

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="ResQ AI | Disaster Management",
    page_icon="R",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# PROFESSIONAL THEME
# ==========================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

:root {
    --background: #101820;
    --panel: #192530;
    --panel-light: #202F3B;
    --border: #344451;
    --text: #E8EDF2;
    --muted: #9BAAB7;
    --blue: #4B9FE1;
    --green: #36B37E;
    --amber: #E5AA45;
    --red: #E46B70;
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

[data-testid="stSidebar"] h1 {
    font-size: 23px;
    font-weight: 700;
}

h1, h2, h3 {
    color: var(--text);
    letter-spacing: -0.5px;
}

h1 {
    font-weight: 700;
}

p {
    color: var(--muted);
}

hr {
    border-color: var(--border);
}

.header-label {
    color: var(--blue);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
}

.page-header {
    border-bottom: 1px solid var(--border);
    padding-bottom: 20px;
    margin-bottom: 25px;
}

.page-header h1 {
    font-size: 30px;
    margin: 8px 0;
}

.page-header p {
    font-size: 14px;
    margin: 0;
}

.metric-card {
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 7px;
    padding: 19px;
    min-height: 112px;
    margin-bottom: 12px;
}

.metric-label {
    color: var(--muted);
    font-size: 13px;
    font-weight: 500;
}

.metric-value {
    color: var(--text);
    font-size: 30px;
    font-weight: 700;
    margin-top: 9px;
}

.metric-note {
    color: var(--muted);
    font-size: 11px;
    margin-top: 4px;
}

.section-heading {
    font-size: 18px;
    font-weight: 600;
    margin-top: 28px;
    margin-bottom: 15px;
}

.panel {
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 7px;
    padding: 20px;
    margin-bottom: 15px;
}

.status {
    display: inline-block;
    font-size: 22px;
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

.small-label {
    color: var(--muted);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
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
    border-color: #4B9FE1;
}

div[data-testid="stMetric"] {
    background: var(--panel);
    padding: 15px;
    border: 1px solid var(--border);
    border-radius: 6px;
}

[data-testid="stMetricLabel"] {
    color: var(--muted);
}

[data-testid="stMetricValue"] {
    color: var(--text);
}

.stSelectbox, .stSlider {
    margin-bottom: 12px;
}

footer {
    visibility: hidden;
}

@media (max-width: 640px) {
    .block-container {
        padding: 1rem 1rem 2rem 1rem;
    }

    .page-header h1 {
        font-size: 25px;
    }

    .metric-card {
        padding: 14px;
        min-height: 100px;
    }

    .metric-value {
        font-size: 25px;
    }

    .status {
        font-size: 19px;
    }
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# REUSABLE COMPONENTS
# ==========================================

def page_header(title, subtitle, section):
    st.markdown(f"""
    <div class="page-header">
        <div class="header-label">{section}</div>
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
    css_class = {
        "LOW": "low",
        "MEDIUM": "medium",
        "HIGH": "high"
    }[level]

    return f'<span class="status {css_class}">{level} RISK</span>'


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
    st.caption("Version 2.0")
    st.caption("Student project prototype")
    st.caption("Data mode: Demonstration")


# ==========================================
# DASHBOARD
# ==========================================

if page == "Dashboard":

    page_header(
        "Disaster Monitoring Dashboard",
        "Overview of sample environmental indicators and risk information.",
        "RESQ AI / OVERVIEW"
    )

    # Key indicators

    st.markdown(
        '<div class="section-heading">Key Indicators</div>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    with c1:
        metric_card(
            "MONITORED AREAS",
            "04",
            "Sample locations"
        )

    with c2:
        metric_card(
            "ACTIVE ALERTS",
            "02",
            "Simulated notifications"
        )

    c3, c4 = st.columns(2)

    with c3:
        metric_card(
            "SAFE SHELTERS",
            "12",
            "Sample shelter records"
        )

    with c4:
        metric_card(
            "DATA STATUS",
            "DEMO",
            "Illustrative information"
        )

    # Environmental snapshot

    st.markdown(
        '<div class="section-heading">Environmental Indicators</div>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    with c1:
        metric_card(
            "RAINFALL",
            "120 mm",
            "Illustrative reading"
        )

    with c2:
        metric_card(
            "WATER LEVEL",
            "8.2 m",
            "Illustrative reading"
        )

    # Graphs

    st.markdown(
        '<div class="section-heading">Rainfall Analysis</div>',
        unsafe_allow_html=True
    )

    rainfall_df = pd.DataFrame({
        "Rainfall (mm)": [65, 90, 120, 155, 110, 180]
    }, index=[
        "Period 1",
        "Period 2",
        "Period 3",
        "Period 4",
        "Period 5",
        "Period 6"
    ])

    st.bar_chart(
        rainfall_df,
        height=270,
        color="#4B9FE1"
    )

    st.caption("Illustrative rainfall values across six periods.")

    st.markdown(
        '<div class="section-heading">Water Level Trend</div>',
        unsafe_allow_html=True
    )

    water_df = pd.DataFrame({
        "Water level (m)": [4.2, 5.1, 5.8, 6.4, 7.2, 8.2]
    }, index=[
        "Period 1",
        "Period 2",
        "Period 3",
        "Period 4",
        "Period 5",
        "Period 6"
    ])

    st.line_chart(
        water_df,
        height=270,
        color="#36B37E"
    )

    st.caption("Illustrative water-level trend.")

    # Pie chart

    st.markdown(
        '<div class="section-heading">Risk Distribution</div>',
        unsafe_allow_html=True
    )

    risk_data = pd.DataFrame({
        "Risk Category": ["Low Risk", "Medium Risk", "High Risk"],
        "Areas": [5, 3, 2]
    })

    pie_spec = {
        "mark": {
            "type": "arc",
            "innerRadius": 45,
            "outerRadius": 115,
            "stroke": "#192530"
        },
        "encoding": {
            "theta": {
                "field": "Areas",
                "type": "quantitative"
            },
            "color": {
                "field": "Risk Category",
                "type": "nominal",
                "scale": {
                    "domain": [
                        "Low Risk",
                        "Medium Risk",
                        "High Risk"
                    ],
                    "range": [
                        "#36B37E",
                        "#E5AA45",
                        "#E46B70"
                    ]
                },
                "legend": {
                    "title": "Risk level",
                    "labelColor": "#E8EDF2",
                    "titleColor": "#E8EDF2"
                }
            },
            "tooltip": [
                {"field": "Risk Category"},
                {"field": "Areas", "type": "quantitative"}
            ]
        },
        "view": {
            "stroke": None
        }
    }

    st.vega_lite_chart(
        risk_data,
        pie_spec,
        use_container_width=True
    )

    st.caption(
        "Illustrative distribution across ten sample areas."
    )

    st.info(
        "Demonstration data only. No live sensors, "
        "verified shelter records or official alerts are connected."
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

    st.markdown(
        '<div class="section-heading">Monitoring Parameters</div>',
        unsafe_allow_html=True
    )

    location = st.selectbox(
        "Monitoring location",
        [
            "Gomti River Area",
            "Alambagh",
            "Hazratganj",
            "Lucknow"
        ]
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

    # Demo classification

    if rainfall >= 200 or water >= 10:
        risk = "HIGH"
        explanation = (
            "The selected readings exceed the demonstration "
            "high-risk thresholds."
        )

    elif rainfall >= 100 or water >= 7:
        risk = "MEDIUM"
        explanation = (
            "The selected readings fall within the "
            "demonstration medium-risk range."
        )

    else:
        risk = "LOW"
        explanation = (
            "The selected readings fall within the "
            "demonstration low-risk range."
        )

    st.markdown(
        '<div class="section-heading">Assessment Result</div>',
        unsafe_allow_html=True
    )

    st.markdown(f"""
    <div class="panel">
        <div class="small-label">MONITORING LOCATION</div>
        <h2>{location}</h2>
        <div class="small-label">DEMO CLASSIFICATION</div>
        {risk_badge(risk)}
        <p>{explanation}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-heading">Measurement Summary</div>',
        unsafe_allow_html=True
    )

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
        "This is a basic rule-based demonstration, "
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
            <div class="small-label">DEMONSTRATION ALERT</div>
            {risk_badge(alert["level"])}
            <h3>{alert["title"]}</h3>
            <p>{alert["message"]}</p>
            <p><b>Location:</b> {alert["location"]}</p>
        </div>
        """, unsafe_allow_html=True)

    st.warning(
        "These notifications are simulated. "
        "They are not official emergency warnings."
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
        "dashboard can organise environmental indicators, "
        "risk classifications and example emergency alerts."
    )

    st.markdown("### System Modules")

    modules = [
        ("Dashboard", "Environmental indicators and data visualisations."),
        ("Risk Assessment", "Rule-based classification of sample readings."),
        ("Emergency Alerts", "Illustrative notifications by location."),
        ("Analytics", "Rainfall, water-level and risk distribution charts.")
    ]

    for title, description in modules:
        st.markdown(f"""
        <div class="panel">
            <b>{title}</b>
            <p>{description}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### Technology Stack")

    st.write("Python | Streamlit | Pandas | Vega-Lite")

    st.info(
        "The current version uses static demonstration data. "
        "It is not connected to live monitoring infrastructure "
        "or emergency response services."
    )


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "ResQ AI | Disaster Management Prototype | Version 2.0"
)
