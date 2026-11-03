
import streamlit as st

st.set_page_config(
    page_title="ResQ AI | Disaster Response",
    page_icon="🌊",
    layout="wide"
)

# ==============================
# CUSTOM DESIGN
# ==============================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #071426;
    color: #F1F5F9;
}

.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

[data-testid="stSidebar"] {
    background: #0D1D33;
    border-right: 1px solid #243B58;
}

.hero {
    background: linear-gradient(120deg, #102B4C, #124C70);
    border: 1px solid #285579;
    border-radius: 20px;
    padding: 28px;
    margin: 12px 0 26px 0;
}

.hero h1 {
    font-size: clamp(30px, 5vw, 46px);
    color: white;
    margin: 8px 0;
}

.hero p {
    color: #C5D8EA;
    font-size: 16px;
    margin-bottom: 0;
}

.eyebrow {
    color: #63D6E8;
    font-weight: 700;
    letter-spacing: 2px;
    font-size: 12px;
}

.metric-card {
    background: #142A43;
    border: 1px solid #2B4563;
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 12px;
}

.metric-label {
    color: #B8C9DB;
    font-size: 14px;
}

.metric-value {
    font-size: 32px;
    font-weight: 800;
    color: white;
    margin-top: 8px;
}

.metric-note {
    color: #8DA9C3;
    font-size: 12px;
    margin-top: 5px;
}

.section-title {
    font-size: 24px;
    font-weight: 800;
    margin: 28px 0 15px 0;
}

.info-card {
    background: #10243A;
    border: 1px solid #29435E;
    border-radius: 16px;
    padding: 20px;
    margin: 12px 0;
}

.info-card p {
    color: #B8C9DB;
}

.status {
    display: inline-block;
    padding: 12px 22px;
    border-radius: 30px;
    font-size: 24px;
    font-weight: 800;
    letter-spacing: 1px;
    margin: 10px 0;
}

.safe {
    background: #123D35;
    color: #70E0B4;
    border: 1px solid #23866A;
}

.warning {
    background: #493817;
    color: #FFD477;
    border: 1px solid #A77B23;
}

.danger {
    background: #4B202B;
    color: #FF9BA8;
    border: 1px solid #B74358;
}

.risk-result {
    background: #10243A;
    border: 2px solid #385673;
    border-radius: 18px;
    padding: 24px;
    margin: 15px 0;
}

.risk-result h2 {
    font-size: 30px;
    color: white;
}

.risk-result .status {
    font-size: 30px;
    padding: 14px 28px;
}

div.stButton > button {
    background: #1687D9;
    color: white;
    border: 0;
    border-radius: 10px;
    font-weight: 700;
    min-height: 44px;
}

div.stButton > button:hover {
    background: #0872BE;
    color: white;
}

@media (max-width: 640px) {
    .block-container {
        padding: 1rem 1rem 2rem 1rem;
    }

    .hero {
        padding: 21px;
        border-radius: 15px;
    }

    .metric-card {
        padding: 16px;
    }

    .status {
        font-size: 21px;
    }

    .risk-result .status {
        font-size: 25px;
    }
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


# ==============================
# REUSABLE FUNCTIONS
# ==============================

def metric_card(label, value, note):
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">{label}</div>
        <div class="metric-value">{value}</div>
        <div class="metric-note">{note}</div>
    </div>
    """, unsafe_allow_html=True)


def status_badge(level):
    styles = {
        "LOW": "safe",
        "MEDIUM": "warning",
        "HIGH": "danger"
    }

    return (
        f'<span class="status {styles[level]}">'
        f'{level} RISK</span>'
    )


def hero(title, subtitle, eyebrow):
    st.markdown(f"""
    <div class="hero">
        <div class="eyebrow">{eyebrow}</div>
        <h1>{title}</h1>
        <p>{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)


# ==============================
# SIDEBAR NAVIGATION
# ==============================

with st.sidebar:
    st.markdown("## 🌊 ResQ AI")
    st.caption("DISASTER RESPONSE PLATFORM")

    st.divider()

    page = st.radio(
        "NAVIGATION",
        [
            "🏠 Dashboard",
            "📊 Risk Assessment",
            "🚨 Emergency Alerts",
            "ℹ️ About"
        ]
    )

    st.divider()

    st.caption("PROTOTYPE VERSION 2.0")
    st.caption("Built for smarter disaster response.")


# ==============================
# DASHBOARD
# ==============================

if page == "🏠 Dashboard":

    hero(
        "🌊 ResQ AI Dashboard",
        "Monitor risks. Understand threats. Support faster response.",
        "AI-POWERED DISASTER MANAGEMENT"
    )

    st.markdown(
        '<div class="section-title">📌 Disaster Overview</div>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    with c1:
        metric_card(
            "Risk Areas",
            "04",
            "Sample monitored locations"
        )

    with c2:
        metric_card(
            "Active Alerts",
            "02",
            "Demo alert records"
        )

    c3, c4 = st.columns(2)

    with c3:
        metric_card(
            "Safe Shelters",
            "12",
            "Sample shelter count"
        )

    with c4:
        metric_card(
            "Monitoring Status",
            "DEMO",
            "Illustrative dashboard data"
        )

    # Environmental snapshot

    st.markdown(
        '<div class="section-title">🌦️ Environmental Snapshot</div>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("""
        <div class="info-card">
            <div class="metric-label">🌧️ Sample Rainfall</div>
            <div class="metric-value">120 mm</div>
            <p>Illustrative measurement</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="info-card">
            <div class="metric-label">🌊 Sample Water Level</div>
            <div class="metric-value">8.2 m</div>
            <p>Illustrative measurement</p>
        </div>
        """, unsafe_allow_html=True)

    # Analytics

    st.markdown(
        '<div class="section-title">📊 Disaster Analytics</div>',
        unsafe_allow_html=True
    )

    st.markdown("### 🌧️ Rainfall Comparison")

    rainfall_data = {
        "Rainfall (mm)": [65, 90, 120, 155, 110, 180]
    }

    st.bar_chart(
        rainfall_data,
        height=280
    )

    st.caption("Sample rainfall readings across six demo periods.")

    st.markdown("### 🌊 Water Level Trend")

    water_data = {
        "Water Level (m)": [4.2, 5.1, 5.8, 6.4, 7.2, 8.2]
    }

    st.line_chart(
        water_data,
        height=280
    )

    st.caption("Illustrative water-level trend.")

    st.markdown("### 🎯 Risk Distribution")

    risk_data = [
        {"risk": "Low Risk", "areas": 5},
        {"risk": "Medium Risk", "areas": 3},
        {"risk": "High Risk", "areas": 2}
    ]

    pie_chart = {
        "mark": {
            "type": "arc",
            "innerRadius": 55,
            "stroke": "#071426"
        },
        "encoding": {
            "theta": {
                "field": "areas",
                "type": "quantitative"
            },
            "color": {
                "field": "risk",
                "type": "nominal",
                "scale": {
                    "domain": [
                        "Low Risk",
                        "Medium Risk",
                        "High Risk"
                    ],
                    "range": [
                        "#22C55E",
                        "#FACC15",
                        "#EF4444"
                    ]
                },
                "legend": {
                    "title": "Risk Category",
                    "labelColor": "#FFFFFF",
                    "titleColor": "#FFFFFF"
                }
            },
            "tooltip": [
                {"field": "risk", "type": "nominal"},
                {"field": "areas", "type": "quantitative"}
            ]
        }
    }

    st.vega_lite_chart(
        risk_data,
        pie_chart,
        use_container_width=True
    )

    st.caption(
        "Demo distribution: 5 low-risk, 3 medium-risk "
        "and 2 high-risk sample areas."
    )

    st.info(
        "All dashboard figures and charts use sample data. "
        "They are not live sensor readings or official warnings."
    )


# ==============================
# RISK ASSESSMENT
# ==============================

elif page == "📊 Risk Assessment":

    hero(
        "📊 Risk Assessment",
        "Explore how sample rainfall and water levels affect a demo risk category.",
        "PREDICTIVE RISK MODULE"
    )

    location = st.selectbox(
        "📍 Select monitoring area",
        [
            "Gomti River Area",
            "Alambagh",
            "Hazratganj",
            "Lucknow"
        ]
    )

    rainfall = st.slider(
        "🌧️ Rainfall (mm)",
        0,
        300,
        120
    )

    water = st.slider(
        "🌊 Water level (metres)",
        0.0,
        15.0,
        8.2,
        0.1
    )

    # Demo risk calculation

    if rainfall >= 200 or water >= 10:
        risk = "HIGH"
        explanation = (
            "The sample readings cross the high-risk "
            "demo thresholds."
        )

    elif rainfall >= 100 or water >= 7:
        risk = "MEDIUM"
        explanation = (
            "The sample readings fall in the medium-risk "
            "demo range."
        )

    else:
        risk = "LOW"
        explanation = (
            "The sample readings fall in the low-risk "
            "demo range."
        )

    st.markdown(
        '<div class="section-title">🎯 Assessment Result</div>',
        unsafe_allow_html=True
    )

    st.markdown(f"""
    <div class="risk-result">
        <div class="metric-label">SELECTED LOCATION</div>
        <h2>{location}</h2>
        {status_badge(risk)}
        <p>{explanation}</p>
    </div>
    """, unsafe_allow_html=True)

    # Input summary

    st.markdown("### 📋 Measurement Summary")

    c1, c2 = st.columns(2)

    with c1:
        metric_card(
            "Rainfall",
            f"{rainfall} mm",
            "Selected sample reading"
        )

    with c2:
        metric_card(
            "Water Level",
            f"{water:.1f} m",
            "Selected sample reading"
        )

    st.caption(
        "Educational prototype only. These simple rules "
        "are not a validated forecasting model."
    )


# ==============================
# EMERGENCY ALERTS
# ==============================

elif page == "🚨 Emergency Alerts":

    hero(
        "🚨 Emergency Alerts",
        "Example notifications for the project demonstration.",
        "ALERT CENTRE"
    )

    alerts = [
        (
            "HIGH",
            "River Monitoring Demo",
            "Sample high-risk condition for demonstration.",
            "Gomti River Area"
        ),
        (
            "MEDIUM",
            "Heavy Rainfall Demo",
            "Sample rainfall condition for demonstration.",
            "Alambagh"
        )
    ]

    for level, title, message, place in alerts:

        st.markdown(f"""
        <div class="info-card">
            {status_badge(level)}
            <h3>{title}</h3>
            <p>{message}</p>
            <p>📍 {place}</p>
        </div>
        """, unsafe_allow_html=True)

    st.warning(
        "These are simulated alerts, not official "
        "emergency notifications."
    )


# ==============================
# ABOUT
# ==============================

elif page == "ℹ️ About":

    hero(
        "ℹ️ About ResQ AI",
        "Technology supporting disaster awareness and response planning.",
        "ABOUT THE PROJECT"
    )

    st.markdown("### 🎯 Our Mission")

    st.write(
        "ResQ AI is a student project prototype designed "
        "to demonstrate how a digital platform could "
        "present disaster-related information and support "
        "better response planning."
    )

    st.markdown("### ⚙️ Project Modules")

    st.markdown("""
    - **Dashboard:** Overview of sample disaster indicators.
    - **Risk Assessment:** Rule-based demonstration using rainfall and water levels.
    - **Emergency Alerts:** Example alert notifications.
    - **Disaster Analytics:** Graphs and risk distribution charts.
    - **About:** Project purpose and scope.
    """)

    st.markdown("### 🛠️ Technology")

    st.write(
        "Python • Streamlit • Custom CSS • Vega-Lite Charts"
    )

    st.info(
        "ResQ AI is a prototype. It does not connect to "
        "live sensors, official emergency services, "
        "or verified shelter databases."
    )


# ==============================
# FOOTER
# ==============================

st.divider()

st.caption(
    "🌊 ResQ AI | Student Project Prototype | "
    "For demonstration purposes only"
)

