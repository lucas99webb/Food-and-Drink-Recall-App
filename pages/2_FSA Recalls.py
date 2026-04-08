# necessary packages

import pandas as pd
import numpy as np
import streamlit as st
import requests

# streamlit intro

st.header('Recall FSA API Testing')

# search_fields2 = {
#     "Title": "title",
#     "Description": "description",
#     "Product Name": "productDetails.productName",
#     "Business Name": "reportingBusiness.commonName"
# }

# search_field_label = st.selectbox("Search Field", list(search_fields2.keys()))
# search_field2 = search_fields2[search_field_label]

firm_name2 = st.text_input('Search Term:')


# set up API call

BASE_URL = "http://data.food.gov.uk/food-alerts/id?type=PRIN&search="


# Button to search the value and run  the function, then return

##### BLOCK 1 #########

# if st.button('Search'):

#     response = requests.get(BASE_URL+firm_name)
#     response.raise_for_status()

#     data = response.json()

#     df = pd.DataFrame((data.get("items",[])))

#     # column_map = {
#     #     "id": "Alert ID",
#     #     "title": "Title",
#     #     "description": "Description",
#     #     "alertType": "Alert Type",
#     #     "created": "Created Date",
#     #     "modified": "Modified Date",
#     #     "notifyingCountry": "Notifying Country",
#     #     "products": "Products",
#     #     "riskStatement": "Risk Statement",
#     #     "actionTaken": "Action Taken",
#     #     "severity": "Severity",
#     #     "distributionStatus": "Distribution Status",
#     #     "source": "Source",
#     #     "subject": "Subject",
#     #     "notes": "Notes",
#     #     "references": "References",
#     #     "relatedAlerts": "Related Alerts",
#     #     "reportingBusiness": "Reporting Business",
#     #     "businessDetails": "Business Details",
#     #     "allergen": "Allergen",
#     #     "hazard": "Hazard",
#     #     "foodType": "Food Type",
#     #     "country": "Country",
#     # }
#     #
#     column_map = {
#     "id": "Alert ID",
#     "title": "Title",
#     "description": "Description",
#     "alertType": "Alert Type",
#     "created": "Created Date",
#     "modified": "Modified Date",
#     "notifyingCountry": "Notifying Country",
#     "products": "Products",
#     "riskStatement": "Risk Statement",
#     "actionTaken": "Action Taken",
#     "severity": "Severity",
#     "distributionStatus": "Distribution Status",
#     "source": "Source",
#     "subject": "Subject",
#     "notes": "Notes",
#     "references": "References",
#     "relatedAlerts": "Related Alerts",
#     "reportingBusiness": "Reporting Business",
#     "businessDetails": "Business Details",
#     "allergen": "Allergen",
#     "hazard": "Hazard",
#     "foodType": "Food Type",
#     "country": "Country",
# }


#     # Only keep columns that exist
#     available_cols = [c for c in column_map.keys() if c in df.columns]

#     df_filtered = df[available_cols].rename(columns=column_map)

#     # Sort by created date (newest first)
#     if "Created Date" in df_filtered.columns:
#         df_filtered["Created Date"] = pd.to_datetime(df_filtered["Created Date"])
#         df_filtered = df_filtered.sort_values("Created Date", ascending=False)

#     st.write("FSA Recall Events")
#     st.dataframe(df_filtered)


###### BLOCK 2 #####

# if st.button("Search"):

#     response = requests.get(BASE_URL + firm_name)
#     response.raise_for_status()
#     data = response.json()

#     def flatten_fsa_item(item):
#         flat = {}
#         flat["Alert ID URL"] = item.get("@id")
#         flat["Alert Types"] = ", ".join(item.get("type", []))
#         flat["Title"] = item.get("title")
#         flat["Alert Code"] = item.get("notation")
#         flat["Created Date"] = item.get("created")
#         flat["Modified Date"] = item.get("modified")
#         flat["Alert Webpage"] = item.get("alertURL")

#         status = item.get("status", {})
#         flat["Status"] = status.get("label")

#         business = item.get("reportingBusiness", {})
#         flat["Reporting Business"] = business.get("commonName")

#         problems = item.get("problem", [])
#         flat["Risk Statement"] = problems[0].get("riskStatement") if problems else None

#         products = item.get("productDetails", [])
#         flat["Product Name"] = products[0].get("productName") if products else None

#         return flat

#     items = data.get("items", [])
#     df = pd.DataFrame([flatten_fsa_item(i) for i in items])


#     st.write("FSA Recall Events")

#     if "Created Date" in df.columns:
#         df["Created Date"] = pd.to_datetime(df["Created Date"], errors="coerce")
#         df = df.sort_values("Created Date", ascending=False)

#     st.dataframe(df)

####### Flattening Function

def flatten_fsa_item(item):
        flat = {}
        flat["Alert ID URL"] = item.get("@id")
        flat["Alert Types"] = ", ".join(item.get("type", []))
        flat["Title"] = item.get("title")
        flat["Alert Code"] = item.get("notation")
        flat["Created Date"] = item.get("created")
        flat["Modified Date"] = item.get("modified")
        flat["Alert Webpage"] = item.get("alertURL")

        status = item.get("status", {})
        flat["Status"] = status.get("label")

        business = item.get("reportingBusiness", {})
        flat["Reporting Business"] = business.get("commonName")

        problems = item.get("problem", [])
        flat["Risk Statement"] = problems[0].get("riskStatement") if problems else None

        products = item.get("productDetails", [])
        flat["Product Name"] = products[0].get("productName") if products else None

        return flat

##### BLOCK 3 #####


# if st.button("Search"):

#     # Build query (no field filtering supported)
#     query = firm_name2
#     url = f"http://data.food.gov.uk/food-alerts/id?type=PRIN&search={query}"

#     response = requests.get(url)
#     response.raise_for_status()
#     data = response.json()

#     items = data.get("items", [])
#     df = pd.DataFrame([flatten_fsa_item(i) for i in items])

#     if "Created Date" in df.columns:
#         df["Created Date"] = pd.to_datetime(df["Created Date"], errors="coerce")
#         df = df.sort_values("Created Date", ascending=False)

#     st.write("FSA Recall Events")
#     st.dataframe(df)


######## BLOCK 4 #########

if st.button("Search"):

    # Build query (no field filtering supported)
    query = firm_name2
    url = f"http://data.food.gov.uk/food-alerts/id?type=PRIN&search={query}"

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    items = data.get("items", [])
    df = pd.DataFrame([flatten_fsa_item(i) for i in items])

    # Convert Created Date → datetime + Year
    df["Created Date"] = pd.to_datetime(df["Created Date"], errors="coerce")
    df["Year"] = df["Created Date"].dt.year

    # Reorder columns exactly as requested
    desired_columns = [
        "Alert Code",
        "Title",
        "Reporting Business",
        "Product Name",
        "Risk Statement",
        "Year",
        "Alert Webpage"
    ]

    # Keep only columns that exist
    df = df[[c for c in desired_columns if c in df.columns]]

    # Sort newest first
    df = df.sort_values("Year", ascending=False)

    st.write("FSA Recall Events")
    st.dataframe(df)

    # ---- BAR CHART OF RECALLS PER YEAR ----
    if not df.empty:
        chart_data = (
            df.groupby("Year")
            .size()
            .reset_index(name="Count")
            .sort_values("Year")
        )

        st.subheader("Number of Recalls per Year")
        st.bar_chart(chart_data, x="Year", y="Count")

