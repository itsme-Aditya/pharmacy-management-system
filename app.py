import streamlit as st
import pandas as pd
from pharmacy_db import init_db, add_drug, add_customer, add_order, view_drugs, view_customers, view_orders, update_drug_quantity

# Initialize the database
init_db()

# Streamlit Sidebar Menu
st.sidebar.title("Pharmacy Management System")
menu = st.sidebar.selectbox("Menu", ["Add Drug", "Add Customer", "Add Order", "View Drugs", "View Customers", "View Orders"])

# Add Drug Section
if menu == "Add Drug":
    st.title("Add a Drug")
    
    drug_name = st.text_input("Drug Name")
    expiry_date = st.date_input("Expiry Date")
    drug_use = st.text_area("Drug Use")
    drug_qty = st.number_input("Quantity", min_value=1)
    drug_price = st.number_input("Price", min_value=0.0)

    if st.button("Add Drug"):
        add_drug(drug_name, expiry_date, drug_use, drug_qty, drug_price)
        st.success(f"Drug '{drug_name}' added successfully!")

# Add Customer Section
elif menu == "Add Customer":
    st.title("Add a Customer")
    
    cust_name = st.text_input("Customer Name")
    cust_email = st.text_input("Email")
    cust_phone = st.text_input("Phone")

    if st.button("Add Customer"):
        add_customer(cust_name, cust_email, cust_phone)
        st.success(f"Customer '{cust_name}' added successfully!")

# Add Order Section
elif menu == "Add Order":
    st.title("Add an Order")
    
    customers = view_customers()
    drugs = view_drugs()

    customer_id = st.selectbox("Select Customer", [f"{c[0]}: {c[1]}" for c in customers])
    drug_id = st.selectbox("Select Drug", [f"{d[0]}: {d[1]}" for d in drugs])
    qty = st.number_input("Quantity", min_value=1)

    if st.button("Add Order"):
        selected_drug = [d for d in drugs if str(d[0]) in drug_id][0]
        drug_price = selected_drug[5]
        available_qty = selected_drug[4]

        if qty > available_qty:
            st.error("Cannot place order. Requested quantity exceeds available quantity.")
        else:
            total = drug_price * qty
            add_order(int(customer_id.split(":")[0]), int(drug_id.split(":")[0]), qty, total)
            # Update the drug quantity in the database
            update_drug_quantity(int(drug_id.split(":")[0]), available_qty - qty)
            st.success(f"Order placed successfully! Total: ₹{total:.2f}")

# View Drugs Section
elif menu == "View Drugs":
    st.title("View All Drugs")
    drugs = view_drugs()
    df = pd.DataFrame(drugs, columns=["ID", "Name", "Expiry Date", "Use", "Quantity", "Price"])
    st.dataframe(df)

# View Customers Section
elif menu == "View Customers":
    st.title("View All Customers")
    customers = view_customers()
    df = pd.DataFrame(customers, columns=["ID", "Name", "Email", "Phone"])
    st.dataframe(df)

# View Orders Section
elif menu == "View Orders":
    st.title("View All Orders")
    orders = view_orders()
    df = pd.DataFrame(orders, columns=["Order ID", "Customer", "Drug", "Quantity", "Total", "Order Date"])
    st.dataframe(df)

