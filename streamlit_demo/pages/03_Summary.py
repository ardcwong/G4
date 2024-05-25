import streamlit as st

st.title("Clustering Summary")
st.write("Here you can provide a short summary and recommendations")


st.header("Top Customers")
st.image("streamlit_demo/images/top.png")
st.write("Segment: Top Customers")
st.text("Top 3 categories:grocery, kids and pets, gas and transport")
st.write(" Since these are highly active customers who purchase frequently, we can see relatively consistent spending patterns throughout the year. From the pattern, we can observe that the first few months (Jan-Feb) of the year have the lowest amount spent.We can Introduce special bonuses, such as extra cashback or double points during these months for the top categories to incentivize continued spending during the holiday season

Since these are valuable customers we could also 
develop loyalty programs and create a sense of exclusivity to make customers feel special and valued. Offer exclusive perks and benefits reserved for program members, such as VIP events or early access to sales.

To further improve the performance of the top categories, we could also explore opportunities for cross-selling and upselling. Encourage customers to explore related products or services that complement their purchases, thereby increasing transaction value.")

st.header("Engaged Customers")
st.image("streamlit_demo/images/engaged.png")
st.text("Top and Engaged customers spend the most in physical grocery stores (grocery_pos).")
st.header("At-risk Customers")
st.image("streamlit_demo/images/risk.png")
st.text("Top and Engaged customers spend the most in physical grocery stores (grocery_pos).")


st.title("Supervised Learning: Linear Regression")
st.write("Here you can provide a short summary and recommendations")
