import streamlit as st
from watson_service import get_watson_response
from budget_module import generate_budget_summary
from insights_module import spending_insights
from response_tuner import tailor_response

# 🎨 Page Setup
st.set_page_config(page_title="Finance Chatbot", page_icon="💬", layout="wide")

# 🧭 Sidebar Navigation
with st.sidebar:
    st.title("🔧 Settings")
    user_type = st.radio("👤 You are a:", ["Student", "Professional"])
    st.markdown("---")
    st.markdown("💡 Tip: Try asking about savings, taxes, or investments.")
    st.caption("Customize your experience")

# 🏷 Main Title
st.markdown("## 💬 Personal Finance Chatbot")
st.markdown("Welcome to your AI-powered financial assistant. Let's make money management simple!")

# 🗂 Tabs for Navigation
tab1, tab2, tab3 = st.tabs(["💬 Chat", "📊 Budget Planner", "📈 Insights"])

# 💬 Chat Tab
with tab1:
    st.markdown("### 💡 Ask a Financial Question")
    query = st.text_area("Type your question here:", height=100)
    if st.button("🚀 Submit", key="chat_submit"):
        with st.spinner("Thinking..."):
            raw_response = get_watson_response(query)
            final_response = tailor_response(raw_response, user_type)
            st.success("✅ Here's what I found:")
            st.write(final_response)

# 📊 Budget Planner Tab
with tab2:
    st.markdown("### 🧾 Monthly Budget Input")
    income = st.number_input("💰 Monthly Income (₹)", min_value=0, step=1000)

    st.markdown("#### 💸 Your Expenses")
    cols = st.columns(3)
    categories = ["🍔 Food", "🏠 Rent", "🚌 Transport", "🎮 Entertainment", "💡 Utilities", "📚 Education"]
    expenses = {}

    for i, category in enumerate(categories):
        with cols[i % 3]:
            expenses[category] = st.number_input(f"{category} (₹)", min_value=0, step=500)

    if st.button("📈 Generate Summary", key="budget_submit"):
        summary = generate_budget_summary(income, expenses)
        st.info("📝 Budget Summary")
        st.write(summary)

# 📈 Insights Tab
with tab3:
    st.markdown("### 🔍 Spending Insights")
    if expenses:
        insights = spending_insights(expenses)
        st.success("📊 Here's what we noticed:")
        st.write(insights)
    else:
        st.warning("Please enter expenses in the Budget tab to view insights.")

# 📎 Footer
st.markdown("---")
st.markdown("✅ Built with Python, Streamlit, and AI services · Made with ❤")