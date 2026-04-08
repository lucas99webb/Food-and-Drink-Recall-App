################################################## V1 ######################################################


# # necessary packages

# import pandas as pd
# import numpy as np
# import streamlit as st
# import requests

# # streamlit intro

# st.header('Recall FDA API Testing')

# search_fields = {
#     "Recalling Firm": "recalling_firm",
#     "Reason for Recall": "reason_for_recall",
#     "Product Description": "product_description"
# }


# search_field_select = st.selectbox("Choose a search field:",list(search_fields.keys()))

# api_field = search_fields[search_field_select]

# firm_name = st.text_input('Firm Name:')


# # set up API call

# BASE_URL = "https://api.fda.gov/food/enforcement.json"

# def search_fda_food(field, value, limit=1000):
#     """
#     Search FDA Food Enforcement API by any field and value.
#     """
#     search_query = f'{field}:"{value}"'

#     params = {
#         "search": search_query,
#         "limit": limit
#     }

#     response = requests.get(BASE_URL, params=params)
#     response.raise_for_status()
#     return response.json()

# # Button to search the value and run  the function, then return

# if st.button('Search'):

#     data = search_fda_food(api_field, firm_name)

#     df = pd.DataFrame((data.get("results",[])))

#     column_map = {
#             "event_id": "Event ID",
#             "classification": "Classification",
#             "recalling_firm": "Recalling Firm",
#             "voluntary_mandated": "Voluntary / Mandated",
#             "product_description": "Product Description",
#             "product_quantity": "Product Quantity",
#             "reason_for_recall": "Reason for Recall",
#             "recall_initiation_date": "Recall Initiation Date"
#         }

#     df_filtered = df[list(column_map.keys())]
    
#     df_filtered = df_filtered.rename(columns=column_map)
#     df_filtered = df_filtered.sort_values("Recall Initiation Date", ascending=False)

#     st.write("FDA Recall Events")
#     st.dataframe(df_filtered)   

########################################## V2 with graph #####################################################

import pandas as pd
import numpy as np
import streamlit as st
import requests

st.header('Recall FDA API Testing')

search_fields = {
    "Recalling Firm": "recalling_firm",
    "Reason for Recall": "reason_for_recall",
    "Product Description": "product_description"
}

search_field_select = st.selectbox("Choose a search field:", list(search_fields.keys()))
api_field = search_fields[search_field_select]

firm_name = st.text_input('Search Term:')

BASE_URL = "https://api.fda.gov/food/enforcement.json"

def search_fda_food(field, value, limit=1000):
    search_query = f'{field}:"{value}"'
    params = {"search": search_query, "limit": limit}
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()

if st.button('Search'):

    data = search_fda_food(api_field, firm_name)
    df = pd.DataFrame(data.get("results", []))

    column_map = {
        "event_id": "Event ID",
        "classification": "Classification",
        "recalling_firm": "Recalling Firm",
        "voluntary_mandated": "Voluntary / Mandated",
        "product_description": "Product Description",
        "product_quantity": "Product Quantity",
        "reason_for_recall": "Reason for Recall",
        "recall_initiation_date": "Recall Initiation Date"
    }

    df_filtered = df[list(column_map.keys())].rename(columns=column_map)
    df_filtered = df_filtered.sort_values("Recall Initiation Date", ascending=False)

    # Warn if max results reached
    if len(df_filtered) >= 999:
        st.warning("⚠️ Maximum number of results reached (999). Your search may have more matches than shown.")

    st.write("FDA Recall Events")
    st.dataframe(df_filtered)

    # ---- GRAPH: Recalls by Year + Classification ----
    if not df_filtered.empty:
        df_filtered["Year"] = df_filtered["Recall Initiation Date"].str[:4]

        chart_data = (
            df_filtered.groupby(["Year", "Classification"])
            .size()
            .reset_index(name="Count")
        )

        st.subheader("Recalls by Year and Classification")
        st.bar_chart(chart_data, x="Year", y="Count", color="Classification")
