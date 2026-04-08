######## QUERY 1 ######



# import pandas as pd
# import streamlit as st
# import requests

# st.header("USDA Recall API Search")

# search_value_usda = st.text_input("Search USDA Recalls (summary search):")

# @st.cache_data(show_spinner=False)
# def fetch_usda_data(query):
#     url = f"https://www.fsis.usda.gov/fsis/api/recall/v/1?field_summary_value={query}"
#     response = requests.get(url)
#     response.raise_for_status()
#     return response.json()

# def flatten_usda_item(item):
#     return {
#         "Recall Number": item.get("field_recall_number"),
#         "Title": item.get("field_title"),
#         "Company": item.get("field_establishment"),
#         "Reason": item.get("field_recall_reason"),
#         "Classification": item.get("field_recall_classification"),
#         "Status": item.get("field_recall_type"),
#         "Recall Date": item.get("field_recall_date"),
#         "URL": item.get("field_recall_url"),
#         "Summary": item.get("field_summary")
#     }

# if st.button("Search"):

#     data = fetch_usda_data(search_value_usda)

#     df = pd.DataFrame([flatten_usda_item(i) for i in data])

#     df["Recall Date"] = pd.to_datetime(df["Recall Date"], errors="coerce")
#     df["Year"] = df["Recall Date"].dt.year

#     st.subheader("USDA Recall Results")
#     st.dataframe(df)

#     if not df.empty:
#         class_chart = (
#             df.groupby("Classification")
#             .size()
#             .reset_index(name="Count")
#             .sort_values("Count", ascending=False)
#         )

#         st.subheader("Recalls by Classification (Class I, II, III)")
#         st.bar_chart(class_chart, x="Classification", y="Count")

########## QUERY 2 #######
import pandas as pd
import streamlit as st
import requests

st.header("USDA Recall Search")

# User search input
search_value_usda = st.text_input("Search USDA Recalls (full text search):")

# Stable USDA endpoint
BASE_URL = "https://www.fsis.usda.gov/fsis/api/recall/v/1?q="

# Flatten USDA recall object
def flatten_usda_item(item):
    return {
        "Recall Number": item.get("field_recall_number"),
        "Title": item.get("field_title"),
        "Company": item.get("field_establishment"),
        "Reason": item.get("field_recall_reason"),
        "Classification": item.get("field_recall_classification"),
        "Risk Level": item.get("field_risk_level"),
        "Recall Type": item.get("field_recall_type"),
        "Recall Date": item.get("field_recall_date"),
        "States": item.get("field_states"),
        "URL": item.get("field_recall_url"),
    }

if st.button("Search"):

    if not search_value_usda.strip():
        st.warning("Please enter a search term.")
        st.stop()

    url = BASE_URL + search_value_usda

    try:
        response = requests.get(url, timeout=12)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        st.error(f"USDA API error: {e}")
        st.stop()

    # Ensure list format
    if isinstance(data, dict):
        data = [data]

    # Convert to DataFrame
    df = pd.DataFrame([flatten_usda_item(item) for item in data])

    st.subheader("USDA Recall Results")
    st.dataframe(df)

    # ---- BAR CHART: Classification Counts ----
    if not df.empty:
        class_chart = (
            df.groupby("Classification")
            .size()
            .reset_index(name="Count")
            .sort_values("Count", ascending=False)
        )

        st.subheader("Recalls by Classification (Class I, II, III)")
        st.bar_chart(class_chart, x="Classification", y="Count")


