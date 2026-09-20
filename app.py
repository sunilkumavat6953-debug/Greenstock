import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="GreenStock Dashboard",
    page_icon="🌱",
    layout="wide"
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🌱 GreenStock")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Inventory",
        "Smart Alerts",
        "Recommendations",
        "Analytics",
        "ESG Report",
        "Settings"
    ]
)

# ---------------- DUMMY DATA ----------------
data = pd.DataFrame({
    "Product": [
        "Bread",
        "Milk",
        "Yogurt",
        "Apples",
        "Bananas",
        "Tomatoes",
        "Cheese",
        "Eggs"
    ],
    "Category": [
        "Bakery",
        "Dairy",
        "Dairy",
        "Fruit",
        "Fruit",
        "Vegetable",
        "Dairy",
        "Poultry"
    ],
    "Quantity": [
        50,
        120,
        80,
        150,
        100,
        180,
        60,
        90
    ],
    "Expiry Days": [
        1,
        2,
        5,
        4,
        2,
        3,
        10,
        7
    ]
})

# Risk Function
def get_risk(days):
    if days <= 1:
        return "High"
    elif days <= 3:
        return "Medium"
    else:
        return "Low"

data["Risk"] = data["Expiry Days"].apply(get_risk)

# Recommendation Function
def recommendation(days):
    if days <= 1:
        return "40% Discount"
    elif days <= 3:
        return "Bundle Offer"
    else:
        return "Keep Price"

data["Recommendation"] = data["Expiry Days"].apply(recommendation)

# ---------------- DASHBOARD ----------------

if page == "Dashboard":

    st.title("🌱 GreenStock Dashboard")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Revenue Saved", "₹1,28,000", "+12%")
    c2.metric("Food Saved", "3200 kg", "+15%")
    c3.metric("Waste Reduced", "72%", "+8%")
    c4.metric("Carbon Saved", "5.6 Tons", "+20%")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        fig = px.bar(
            data,
            x="Product",
            y="Quantity",
            color="Category",
            title="Current Inventory"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig2 = px.pie(
            data,
            names="Risk",
            title="Risk Distribution"
        )
        st.plotly_chart(fig2, use_container_width=True)

    st.divider()

    st.subheader("Today's Summary")

    st.info("🚨 3 products require immediate attention.")

    st.warning("⚠ Bread expires tomorrow.")

    st.success("✅ 12 products sold before expiry today.")

# ---------------- INVENTORY ----------------

elif page == "Inventory":

    st.title("📦 Inventory")

    st.dataframe(data, use_container_width=True)

# ---------------- ALERTS ----------------

elif page == "Smart Alerts":

    st.title("⚠ Smart Alerts")

    high = data[data["Risk"]=="High"]

    for i,row in high.iterrows():

        st.error(f"""
Product : {row['Product']}

Expiry : {row['Expiry Days']} day

Recommendation :
{row['Recommendation']}
""")

# ---------------- RECOMMENDATION ----------------

elif page == "Recommendations":

    st.title("💡 AI Recommendations")

    st.dataframe(
        data[
            [
                "Product",
                "Risk",
                "Recommendation"
            ]
        ],
        use_container_width=True
    )

# ---------------- ANALYTICS ----------------

elif page == "Analytics":

    st.title("📈 Analytics")

    fig3 = px.histogram(
        data,
        x="Category",
        title="Products by Category"
    )

    st.plotly_chart(fig3, use_container_width=True)

# ---------------- ESG ----------------

elif page == "ESG Report":

    st.title("🌍 ESG Report")

    a,b,c = st.columns(3)

    a.metric("Meals Saved","520")

    b.metric("CO₂ Saved","5.6 Tons")

    c.metric("Waste Prevented","72%")

# ---------------- SETTINGS ----------------

elif page == "Settings":

    st.title("⚙ Settings")

    st.text_input("Store Name","GreenMart")

    st.text_input("Manager Name","John")

    st.selectbox(
        "Theme",
        [
            "Green",
            "Dark",
            "Blue"
        ]
    )

    st.button("Save Settings")