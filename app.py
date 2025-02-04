import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# Load dataset with caching
@st.cache_data
def load_data():
    return pd.read_csv("Data/retail_sales_dataset.csv")

df = load_data()

# Convert Date to datetime and create Month column
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.strftime("%Y-%m")

# Sidebar Filters
st.sidebar.title("📊 Filters")
start_date = st.sidebar.date_input("Start date", df["Date"].min())
end_date = st.sidebar.date_input("End date", df["Date"].max())
categories = st.sidebar.multiselect("Product Category", df["Product Category"].unique(), df["Product Category"].unique())
genders = st.sidebar.multiselect("Select Gender", df["Gender"].unique(), df["Gender"].unique())

# Apply Filters
df_filtered = df[
    (df["Date"] >= pd.to_datetime(start_date)) &
    (df["Date"] <= pd.to_datetime(end_date)) &
    (df["Product Category"].isin(categories)) &
    (df["Gender"].isin(genders))
]

# KPI Metrics
total_sales = df_filtered["Total Amount"].sum()
total_orders = df_filtered.shape[0]
avg_sales = total_sales / total_orders if total_orders > 0 else 0
unique_customers = df_filtered["Customer ID"].nunique()

# Display KPIs
st.title("📈 Sales Dashboard")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Sales", f"${total_sales/1e6:.2f}M")
col2.metric("Total Orders", total_orders)
col3.metric("Avg Sale per Order", f"${avg_sales:.2f}")
col4.metric("Unique Customers", unique_customers)

# Sales Over Time - Line Chart
st.subheader("📅 Sales Over Time")
monthly_sales = df_filtered.groupby("Month")["Total Amount"].sum().reset_index()
fig_sales = px.line(
    monthly_sales,
    x="Month",
    y="Total Amount",
    title="Sales Over Time",
    template="plotly_dark",
    markers=True  
)
# Update traces to use spline interpolation and ensure mode includes markers
fig_sales.update_traces(mode="lines+markers", line_shape="spline")
st.plotly_chart(fig_sales, use_container_width=True)

# Sales by Product Category - Bar Chart
st.subheader("🛒 Sales by Product Category")
category_sales = df_filtered.groupby("Product Category")["Total Amount"].sum().reset_index()
fig_category = px.bar(
    category_sales,
    x="Product Category",
    y="Total Amount",
    title="Sales by Product Category",
    color="Total Amount",
    text_auto=True,
    color_continuous_scale="Blues",
    template="plotly_dark"
)
st.plotly_chart(fig_category, use_container_width=True)

# Sales by Gender - Pie Chart
st.subheader("👥 Sales by Gender")
gender_sales = df_filtered.groupby("Gender")["Total Amount"].sum().reset_index()
fig_gender = px.pie(
    gender_sales,
    names="Gender",
    values="Total Amount",
    title="Sales Distribution by Gender",
    color_discrete_sequence=["#ff6361", "#003f5c"],
    template="plotly_dark"
)
st.plotly_chart(fig_gender, use_container_width=True)

# Footer Branding in Sidebar
st.sidebar.markdown("### Created by Andrea Satria Nagari")
