
import streamlit as st

st.set_page_config(
    page_title="ResQ AI | Disaster Response",
    page_icon="🌊",
    layout="wide"
)

# ---------- DESIGN ----------
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
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1150px;
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
    margin: 0;
    color: white;
}
.hero p {
    color: #C5D8EA;
    margin-bottom: 0;
    font-size: 16px;
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
    font-size: 23px;
    font-weight: 700;
    margin: 25px 0 14px 0;
}
.info-card {
    background: #10243A;
    border: 1px solid #29435E;
    border-radius: 15px;
    padding: 18px;
    margin: 10px 0;
}
.info-card p {
    color: #B8C9DB;
    margin-bottom: 0;
}
.status {
    display: inline-block;
    padding: 5px 11px;
    border-radius: 30px;
    font-size: 12px;
    font-weight: 700;
}
.safe { background: #123D35; color: #70E0B4; }
.warning { background: #493817; color: #FFD477; }
.danger { background: #4B202B; color: #FF9BA8; }

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
.stSlider [data-baseweb="slider"] {
    margin-top: 10px;
}
footer {visibility: hidden;}
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
}
</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.markdown("## 🌊 ResQ AI")
    st.caption("DISASTER RESPONSE PLATFORM")
    st.divider()

    page = st.radio(
        "NAVIGATION",
        ["🏠 Dashboard", "📊 Risk Assessment",
         "🚨 Emergency Alerts", "ℹ️ About"]
    )

    st.divider()
    st.caption("PROTOTYPE VERSION 1.0")
    st.caption("Built for smarter disaster response.")

# ---------- REUSABLE CARDS ----------
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
    return f'<span class="status {styles[level]}">{level} RISK</span>'

# ---------- DASHBOARD ----------
if page == "🏠 Dashboard":
    st.markdown("""
    <div class="hero">
        <div class="eyebrow">AI-POWERED DISASTER MANAGEMENT</div>
        <h1>🌊 ResQ AI Dashboard</h1>
        <p>Monitor risks. Understand threats. Support faster response.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Disaster Overview</div>',
                unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        metric_card("Risk Areas", "04", "Sample monitored locations")
    with c2:
        metric_card("Active Alerts", "02", "Demo alert records")

    c3, c4 = st.columns(2)
    with c3:
        metric_card("Safe Shelters", "12", "Sample shelter count")
    with c4:
        metric_card("Monitoring Status", "DEMO", "Illustrative dashboard data")

    st.markdown('<div class="section-title">Environmental Snapshot</div>',
                unsafe_allow_html=True)

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

    st.info("Demo dashboard: figures are sample data, not live sensor readings or official warnings.")

# ---------- RISK ASSESSMENT ----------
elif page == "📊 Risk Assessment":
    st.markdown("""
    <div class="hero">
        <div class="eyebrow">PREDICTIVE RISK MODULE</div>
        <h1>📊 Risk Assessment</h1>
        <p>Explore how sample rainfall and water levels affect a demo risk category.</p>
    </div>
    """, unsafe_allow_html=True)

    location = st.selectbox(
        "Select monitoring area",
        ["Gomti River Area", "Alambagh", "Hazratganj", "Lucknow"]
    )

    rainfall = st.slider("🌧️ Rainfall (mm)", 0, 300, 120)
    water = st.slider("🌊 Water level (metres)", 0.0, 15.0, 8.2, 0.1)

    if rainfall >= 200 or water >= 10:
        risk = "HIGH"
        explanation = "The sample readings cross the high-risk demo thresholds."
    elif rainfall >= 100 or water >= 7:
        risk = "MEDIUM"
        explanation = "The sample readings fall in the medium-risk demo range."
    else:
        risk = "LOW"
        explanation = "The sample readings fall in the low-risk demo range."

    st.markdown('<div class="section-title">Assessment Result</div>',
                unsafe_allow_html=True)

    st.markdown(f"""
    <div class="info-card">
        <div class="metric-label">Selected location</div>
        <h3>{location}</h3>
        {status_badge(risk)}
        <p style="margin-top:12px">{explanation}</p>
    </div>
    """, unsafe_allow_html=True)

    st.caption("Educational prototype only. These simple rules are not a validated forecasting model.")

# ---------- EMERGENCY ALERTS ----------
elif page == "🚨 Emergency Alerts":
    st.markdown("""
    <div class="hero">
        <div class="eyebrow">ALERT CENTRE</div>
        <h1>🚨 Emergency Alerts</h1>
        <p>Example notifications for the project demonstration.</p>
    </div>
    """, unsafe_allow_html=True)

    alerts = [
        ("HIGH", "River monitoring demo",
         "Sample high-risk condition for demonstration.",
         "Gomti River Area"),
        ("MEDIUM", "Heavy rainfall demo",
         "Sample rainfall condition for demonstration.",
         "Alambagh")
    ]

    for level, title, message, place in alerts:
        st.markdown(f"""
        <div class="info-card">
            {status_badge(level)}
            <h3 style="margin-top:12px">{title}</h3>
            <p>{message}</p>
            <p>📍 {place}</p>
        </div>
        """, unsafe_allow_html=True)

    st.warning("These are simulated alerts, not official emergency notifications.")

# ---------- ABOUT ----------
elif page == "ℹ️ About":
    st.markdown("""
    <div class="hero">
        <div class="eyebrow">ABOUT THE PROJECT</div>
        <h1>ℹ️ About ResQ AI</h1>
        <p>Technology supporting disaster awareness and response planning.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🎯 Our Mission")
    st.write(
        "ResQ AI is a student project prototype designed to demonstrate "
        "how a digital platform could present disaster-related information "
        "and support better response planning."
    )

    st.markdown("### ⚙️ Project Modules")
    st.markdown("""
    - **Dashboard:** Overview of sample disaster indicators.
    - **Risk Assessment:** Rule-based demonstration using rainfall and water levels.
    - **Emergency Alerts:** Example alert notifications.
    - **About:** Project purpose and scope.
    """)

    st.markdown("### 🛠️ Technology")
    st.write("Python • Streamlit • Custom CSS")

    st.info(
        "ResQ AI is a prototype. It does not connect to live sensors, "
        "official emergency services, or verified shelter databases."
    )

st.divider()
st.caption("ResQ AI • Student Project Prototype • For demonstration purposes only")

