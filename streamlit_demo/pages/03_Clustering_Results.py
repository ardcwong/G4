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


st.title("Meet the Clusters")
st.text("1 | Based on our clustering analysis , the elbow method suggests 3 optimal")
st.image("streamlit_demo/images/Top.png")
