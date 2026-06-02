import streamlit as st
import pandas as pd
import joblib
import os
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="AI-Powered Delivery Intelligence Platform",
    page_icon="🚚",
    layout="wide"
)

st.title("🚚 Amazon Delivery Intelligence Platform")

st.markdown("""
### Predictive Logistics & Operational Analytics

Monitor delivery performance, predict ETAs, and identify delivery risks using Machine Learning.
""")

# -------------------------------------------------
# Professional Chart Style
# -------------------------------------------------
sns.set_style("darkgrid")
sns.set_palette("Set2")
plt.rcParams.update({
    "figure.figsize": (8, 4),
    "axes.titlesize": 14,
    "axes.labelsize": 12,
})

# -------------------------------------------------
# Load Model
# -------------------------------------------------
MODEL_PATH = "best_delivery_model.joblib"

@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
        return None
    return joblib.load(MODEL_PATH)

model = load_model()

if model is None:
    st.error("❌ Model file not found.")
    st.stop()

# -------------------------------------------------
# Sidebar Inputs
# -------------------------------------------------
st.sidebar.header("📋 Order Details")

distance = st.sidebar.number_input("Distance (km)", 0.1, 50.0, 5.0)
agent_age = st.sidebar.number_input("Agent Age", 18, 60, 30)
agent_rating = st.sidebar.slider("Agent Rating", 1.0, 5.0, 4.5)

weather = st.sidebar.selectbox("Weather", ["Sunny", "Cloudy", "Rainy", "Fog"])
traffic = st.sidebar.selectbox("Traffic", ["Low", "Medium", "High", "Jam"])
vehicle = st.sidebar.selectbox("Vehicle", ["motorcycle", "scooter", "van"])
area = st.sidebar.selectbox("Area", ["Urban", "Semi-Urban", "Metropolitan"])
category = st.sidebar.selectbox("Category", ["Clothing", "Electronics", "Groceries", "Food"])

# -------------------------------------------------
# Prepare Input
# -------------------------------------------------
input_df = pd.DataFrame({
    "Distance_km": [distance],
    "Agent_Age": [agent_age],
    "Agent_Rating": [agent_rating],
    "Weather": [weather],
    "Traffic": [traffic],
    "Vehicle": [vehicle],
    "Area": [area],
    "Category": [category]
})

prediction = model.predict(input_df)[0]

# -------------------------------------------------
# Delivery Status
# -------------------------------------------------

if prediction < 90:
    st.success("🟢 On-Time Delivery Expected")

elif prediction < 150:
    st.warning("🟡 Moderate Delay Risk")

else:
    st.error("🔴 High Delay Risk")

# -------------------------------------------------
# KPI Section
# -------------------------------------------------

st.subheader("📊 Key Metrics")

hours = int(prediction // 60)
minutes = int(prediction % 60)

col1, col2, col3, col4, col5 = st.columns(5)

if prediction < 90:
    risk = "Low"
elif prediction < 150:
    risk = "Medium"
else:
    risk = "High"

customer_score = max(60, 100 - prediction/2)


col1.metric(
    "🚚 Estimated Delivery Time",
    f"{hours}h {minutes}m"
)

col2.metric(
    "⭐ Agent Rating",
    f"{agent_rating:.1f}"
)

col3.metric(
    "📍 Distance",
    f"{distance} km"
)

col4.metric("⚠️ Risk Score", risk)

col5.metric(
    "😊 Customer Satisfaction",
    f"{customer_score:.0f}%"
)  

st.divider()

st.markdown("### Operational Decision Support")

st.subheader("🤖 AI Recommendations")

if prediction < 90:
    st.success(
        "Delivery is expected to arrive on time. Current route and resources are optimal."
    )

elif prediction < 150:
    st.warning(
        "Moderate delay risk detected. Consider alternative routing if available."
    )

else:
    st.error(
        "High delay risk detected. Recommend route reassignment or additional delivery resources."
    )

# -------------------------------------------------
# Delivery Time Insights
# -------------------------------------------------
st.subheader("📈 Delivery Analytics Dashboard")

# -------------------------------------
# 1️⃣ Distance Impact (Colorful Line Chart)
# -------------------------------------
simulated_distances = list(range(1, 21))
simulated_predictions = []

for d in simulated_distances:
    temp_df = input_df.copy()
    temp_df["Distance_km"] = d
    simulated_predictions.append(model.predict(temp_df)[0])

fig1, ax1 = plt.subplots()
sns.lineplot(
    x=simulated_distances,
    y=simulated_predictions,
    marker="o",
    linewidth=3,
    color="#1f77b4",
    ax=ax1
)

ax1.set_title("🚚 Impact of Distance on Delivery Time")
ax1.set_xlabel("Distance (km)")
ax1.set_ylabel("Predicted Time (minutes)")
st.pyplot(fig1)

# -------------------------------------
# 2️⃣ Traffic Impact (Gradient Bar Chart)
# -------------------------------------
traffic_levels = ["Low", "Medium", "High", "Jam"]
traffic_predictions = []

for t in traffic_levels:
    temp_df = input_df.copy()
    temp_df["Traffic"] = t
    traffic_predictions.append(model.predict(temp_df)[0])

fig2, ax2 = plt.subplots()
sns.barplot(
    x=traffic_levels,
    y=traffic_predictions,
    palette="viridis",
    ax=ax2
)

ax2.set_title("🚦 Impact of Traffic on Delivery Time")
ax2.set_xlabel("Traffic Condition")
ax2.set_ylabel("Predicted Time (minutes)")
st.pyplot(fig2)

# -------------------------------------
# 3️⃣ Weather Impact (Soft Color Bar Chart)
# -------------------------------------
weather_types = ["Sunny", "Cloudy", "Rainy", "Fog"]
weather_predictions = []

for w in weather_types:
    temp_df = input_df.copy()
    temp_df["Weather"] = w
    weather_predictions.append(model.predict(temp_df)[0])

fig3, ax3 = plt.subplots()
sns.barplot(
    x=weather_types,
    y=weather_predictions,
    palette="coolwarm",
    ax=ax3
)

ax3.set_title("🌦 Impact of Weather on Delivery Time")
ax3.set_xlabel("Weather Condition")
ax3.set_ylabel("Predicted Time (minutes)")
st.pyplot(fig3)

st.info(
    "🚚 AI-Powered Delivery Intelligence Platform | Built using Python, Scikit-Learn, Streamlit & MLflow"
)
