import streamlit as st

st.set_page_config(page_title="Personal Expense Tracker")

st.title("💰 Personal Expense Tracker")
st.write("Track your expenses easily.")

if "expenses" not in st.session_state:
    st.session_state.expenses = []

st.header("Add Expense")

name = st.text_input("Expense name")
amount = st.number_input("Amount (₹)", min_value=0.0, step=10.0)

if st.button("Add Expense"):
    if name and amount > 0:
        st.session_state.expenses.append((name, amount))
        st.success("Expense added successfully!")
    else:
        st.warning("Please enter an expense name and amount.")

st.header("Your Expenses")

if st.session_state.expenses:
    total = 0

    for name, amount in st.session_state.expenses:
        st.write(f"**{name}** — ₹{amount:.2f}")
        total += amount

    st.subheader(f"Total Expense: ₹{total:.2f}")
else:
    st.info("No expenses added yet.")
