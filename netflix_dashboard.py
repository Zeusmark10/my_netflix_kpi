# import streamlit as st

# # --- PAGE SETUP ---
# st.set_page_config(page_title="Netflix CRM KPI Dashboard", page_icon="🎬", layout="wide")

# # --- CSS ---
# st.markdown("""
# <style>
# /* Remove top padding/margin */
# main > div.block-container { padding-top: 1rem; }

# /* Dark background and white text */
# .stApp { background-color: #141414; color: #ffffff; font-family: 'Helvetica', sans-serif; }

# /* Headers */
# h1, h2, h3 { color: #e50914 !important; }

# /* Inputs styling */
# .stTextInput>div>div>input, .stNumberInput>div>input { 
#     background-color: #1e1e1e; color: #ffffff; border:1px solid #e50914; border-radius:6px; padding:5px; 
# }
# label, .stSlider>div>div>div>div>div>div>div { color: #ffffff !important; }

# /* KPI cards */
# .kpi-card { background-color:#1e1e1e; border-radius:12px; padding:15px; margin:5px; text-align:center; box-shadow:0 4px 12px rgba(0,0,0,0.4); cursor: help; }
# .kpi-title { color:#e50914; font-size:16px; margin-bottom:5px; }
# .kpi-value { color:#ffffff; font-size:28px; font-weight:bold; }
# .kpi-subtext { color:#bbbbbb; font-size:12px; }
# </style>
# """, unsafe_allow_html=True)

# # --- NETFLIX LOGO ---
# st.markdown("""
# <div style="text-align:center; margin-bottom:10px;">
# <img src="https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg" width="80">
# </div>
# """, unsafe_allow_html=True)

# # --- TITLE ---
# st.markdown("<h2 style='color:#e50914;text-align:center;margin-bottom:15px;'>Netflix CRM KPI Dashboard</h2>", unsafe_allow_html=True)
# st.markdown("<p style='text-align:center;color:#ffffff;'>Enter hypothetical data below to calculate and understand Netflix-style CRM KPIs.</p>", unsafe_allow_html=True)

# # --- HELPER FUNCTIONS ---
# def human_format(num):
#     if num >= 1_000_000_000: return f"{num/1_000_000_000:.2f}B"
#     elif num >= 1_000_000: return f"{num/1_000_000:.2f}M"
#     elif num >= 1_000: return f"{num/1_000:.2f}K"
#     else: return str(num)

# def parse_human_input(text):
#     text = text.strip().upper()
#     if text.endswith("B"): return float(text[:-1]) * 1_000_000_000
#     elif text.endswith("M"): return float(text[:-1]) * 1_000_000
#     elif text.endswith("K"): return float(text[:-1]) * 1_000
#     else: return float(text)

# # --- LAYOUT ---
# left_col, right_col = st.columns([1,2])

# with left_col:
#     st.header("Input Data")
#     total_users_input = st.text_input("Total Subscribers", value="250M")
#     churned_users_input = st.text_input("Churned Subscribers (this month)", value="5M")
#     new_users_input = st.text_input("New Subscribers (this month)", value="8M")
#     avg_monthly_revenue = st.number_input("Avg Monthly Revenue per User ($)", min_value=1.0, value=15.0)
#     avg_lifetime_months = st.number_input("Avg Customer Lifetime (months)", min_value=1, value=36)
#     marketing_spend_input = st.text_input("Monthly Marketing Spend ($)", value="100M")
#     daily_active_users_input = st.text_input("Daily Active Users", value="60M")
#     monthly_active_users_input = st.text_input("Monthly Active Users", value="100M")
#     csat_score = st.slider("Customer Satisfaction (CSAT %)", 0, 100, 85)
#     nps_score = st.slider("Net Promoter Score (NPS)", -100, 100, 60)

# # --- PARSE INPUTS ---
# total_users = parse_human_input(total_users_input)
# churned_users = parse_human_input(churned_users_input)
# new_users = parse_human_input(new_users_input)
# marketing_spend = parse_human_input(marketing_spend_input)
# daily_active_users = parse_human_input(daily_active_users_input)
# monthly_active_users = parse_human_input(monthly_active_users_input)

# # --- CALCULATIONS ---
# churn_rate = (churned_users / total_users) * 100
# retention_rate = 100 - churn_rate
# clv = avg_monthly_revenue * avg_lifetime_months
# dau_mau = (daily_active_users / monthly_active_users) * 100
# cac = marketing_spend / new_users if new_users > 0 else 0
# mrr = total_users * avg_monthly_revenue

# # --- KPI DATA WITH DETAILED TOOLTIPS INCLUDING FORMULA ---
# kpi_data = [
#     ("Churn Rate", f"{churn_rate:.2f} %", 
#      "Churn Rate: % of subscribers lost this month. \n "
#      "Formula: (Churned Users / Total Subscribers) * 100"),
#     ("Customer Retention", f"{retention_rate:.2f} %", 
#      "Customer Retention Rate: % of subscribers retained.\n"
#      " Formula: 100 - Churn Rate"),
#     ("Engagement (DAU/MAU)", f"{dau_mau:.1f} %", 
#      "Engagement (DAU/MAU): Daily active users / Monthly active users * 100. Shows stickiness."),
#     ("CLV", f"${human_format(clv)}", 
#      "Customer Lifetime Value: Total revenue per customer."
#      "\n Formula: Avg Monthly Revenue * Avg Lifetime (months)"),
#     ("CAC", f"${human_format(cac)}", 
#      "Customer Acquisition Cost: Marketing cost per new subscriber. \n"
#      "Formula: Marketing Spend / New Users"),
#     ("MRR", f"${human_format(mrr)}", 
#      "Monthly Recurring Revenue: Predictable revenue. \n"
#      "Formula: Total Subscribers * Avg Monthly Revenue"),
#     ("CSAT", f"{csat_score} %", 
#      "Customer Satisfaction Score: % of satisfied users.\n Formula: Survey-based score."),
#     ("NPS", f"{nps_score}", 
#      "Net Promoter Score: Customer loyalty. \n"
#      "Formula: %Promoters - %Detractors"),
#     ("Marketing Spend", f"${human_format(marketing_spend)}", 
#      "Marketing Spend: Total marketing investment this month.")
# ]

# # --- KPI DISPLAY ON RIGHT PANEL ---
# with right_col:
#     st.header("📊 KPI Results")
#     for i in range(0, len(kpi_data), 3):  # 3 cards per row
#         cols = st.columns(3)
#         for j, (title, value, hover) in enumerate(kpi_data[i:i+3]):
#             with cols[j]:
#                 st.markdown(f"""
#                 <div class="kpi-card" title="{hover}">
#                     <div class="kpi-title">{title}</div>
#                     <div class="kpi-value">{value}</div>
#                 </div>
#                 """, unsafe_allow_html=True)

#     # --- Quick Insights ---
#     st.header("💡 Quick Insights")
#     if churn_rate < 3:
#         st.success("✅ Low churn rate — customer retention looks strong!")
#     else:
#         st.warning("⚠️ Churn rate is relatively high — consider improving engagement or personalization.")
#     if nps_score > 50:
#         st.info("🌟 Excellent NPS — users are loyal and recommend Netflix often.")
#     elif nps_score > 0:
#         st.info("🙂 Good NPS — most users are satisfied but there’s room to grow.")
#     else:
#         st.error("🚨 Negative NPS — indicates dissatisfaction or potential churn risk.")
#     if dau_mau > 60:
#         st.success("🔥 High engagement — users are consistently active!")
#     else:
#         st.warning("📉 Engagement could be improved with more personalized or trending content.")

#     st.markdown("---")

# app.py
import streamlit as st
import pandas as pd
import pickle
from tmdbv3api import TMDb, Movie
import re
import compress_pickle

# --- Helper function ---
def clean_genre_string(genre_string):
    if isinstance(genre_string, str):
        cleaned = re.sub(r'[^a-zA-Z0-9\s,]', '', genre_string)
        cleaned = ', '.join([g.strip() for g in cleaned.split(',')])
        return cleaned
    return ""

# --- Load model ---
model = compress_pickle.load(
    "recommender_model_compressed.pkl",
    compression="lz4"
)

user_item_matrix = model['user_item_matrix']
similarity_matrix = model['similarity_matrix']
data = model['data']

# --- Initialize TMDb ---
tmdb = TMDb()
tmdb.api_key = "f9d8c6d8e0ffd758b616b84b38eef71c"
tmdb_movie = Movie()

# --- Streamlit Page Config ---
st.set_page_config(page_title="Netflix Movie Recommender", layout="wide", page_icon="🎬")

# --- Netflix Style CSS ---
st.markdown(
    """
    <style>
    /* Full app background */
    .stApp {
        background-color: #141414;
        color: #ffffff;
    }

    /* Main container padding */
    .block-container {
        padding-top: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
        background-color: #141414;
    }

    /* Header style */
    .title-text {
        color: #e50914;
        font-size: 50px;
        font-weight: bold;
        margin-bottom: 1rem;
    }

    /* Dropdown and input fields background */
    div.stSelectbox>div>div>select, 
    div.stTextInput>div>input {
        background-color: #333333;
        color: #ffffff;  /* Text color inside the dropdown */
    }

    /* Dropdown label text */
    label[for^="widget"] {
        color: #ffffff;  /* Label text white */
        font-weight: bold;
    }

    /* Movie title under poster */
    .movie-title {
        color: #ffffff;
        font-weight: bold;
        text-align: center;
        margin-top: 5px;
    }

    /* Subheader style */
    h2 {
        color: #ffffff;
        margin-top: 2rem;
    }

    /* Try to open dropdown upwards */
    div.stSelectbox>div>div>div[role='listbox'] {
        direction: up;
    }

    /* Links style */
    a {
        color: #ffffff;
        text-decoration: none;
    }
    a:hover {
        color: #e50914;
        text-decoration: underline;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Netflix Header ---
st.markdown("<h1 class='title-text'>🎬 Netflix Movie Recommender</h1>", unsafe_allow_html=True)
st.write("Select a movie to get top 5 recommendations.")

# Dropdown for movies
movie_options = list(user_item_matrix.columns)
selected_movie = st.selectbox("Choose a movie:", [""] + movie_options)

# --- Function to get recommendations ---
def get_recommendations(title):
    recommendations = []
    if title in user_item_matrix.columns:
        idx = user_item_matrix.columns.get_loc(title)
        similar_idx = similarity_matrix[idx].argsort()[::-1]
        similar_idx = [i for i in similar_idx if i != idx and i < len(user_item_matrix.columns)]
        similar_idx = similar_idx[:5]
        recommendations = user_item_matrix.columns[similar_idx].to_list()
    return recommendations

# --- Display recommendations ---
if selected_movie:
    recs = get_recommendations(selected_movie)
    
    if recs:
        st.subheader("Top Recommendations:")
        cols = st.columns(len(recs))
        
        for i, m in enumerate(recs):
            poster_url = None
            movie_url = "#"
            try:
                search_result = tmdb_movie.search(m)
                if search_result:
                    poster_path = getattr(search_result[0], "poster_path", None)
                    movie_id = getattr(search_result[0], "id", None)
                    if poster_path:
                        poster_url = f"https://image.tmdb.org/t/p/w200{poster_path}"
                    if movie_id:
                        movie_url = f"https://www.themoviedb.org/movie/{movie_id}"
            except Exception:
                poster_url = None

            # Fallback poster
            if not poster_url:
                poster_url = "https://via.placeholder.com/150x225?text=Poster+NA"

            with cols[i]:
                st.image(poster_url, width=150)
                st.markdown(f"<div class='movie-title'><a href='{movie_url}' target='_blank'>{m}</a></div>", unsafe_allow_html=True)
