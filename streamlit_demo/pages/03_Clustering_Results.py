import streamlit as st

st.title("CUSTOMER SEGMENTATION")
st.write("Based on AAC Credit Card Transactions as of December 7, 2021")


st.header("Elbow Method and Silhouette Score for Optimal Number of Cluster")
st.image("streamlit_demo/images/cluster.png")
st.text("1 | Based on our clustering analysis , the elbow method suggests 3 optimal")
st.text("    clusters while the silhouette score indicates 5.") 
st.text("2 | The 3-cluster model offers a simpler segmentation of high, medium, and")
st.text("    low-value customers. While the 5-cluster model provides more detailed")
st.text("    insights, identifying 5 distinct subgroups")


st.title("MEET THE CLUSTERS")
st.image("streamlit_demo/images/Kmeans.png")

st.header("Top Customers")
st.text("Highly active and valuable customers who purchase frequently and spend a lot")
st.image("streamlit_demo/images/top.png")

st.header("Engaged Customers")
st.text("Active but with a moderate level of spending compared to top customers")
st.image("streamlit_demo/images/engaged.png")


st.header("At-Risk Customers")
st.text("No recent purchases, buy infrequently, and spend less. They might be at risk of churning")
st.image("streamlit_demo/images/risk.png")
