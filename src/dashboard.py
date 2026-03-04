import streamlit as st
import pandas as pd
import plotly.express as px

# Load processed data
df = pd.read_csv("data/processed/aris_games_processed.csv")

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Aris Basketball Analytics",
    page_icon="🏀",
    layout="wide"
)

# --- TITLE ---
st.title("🏀 Aris Thessaloniki - Season 2024-2025")
st.markdown("Basketball analytics dashboard")

# --- TOP METRICS ---
# Metrics are the big numbers displayed at the top of the dashboard
col1, col2, col3, col4 = st.columns(4)

wins = df["aris_won"].sum()
losses = len(df) - wins
avg_scored = df["aris_score"].mean()
avg_conceded = df["opponent_score"].mean()

col1.metric("Total Games", len(df))
col2.metric("Wins", int(wins))
col3.metric("Losses", int(losses))
col4.metric("Avg Points Scored", f"{avg_scored:.1f}")

st.divider()

# --- CHART 1: POINTS PER GAME ---
# Bar chart showing Aris score vs opponent score for each game
st.subheader("Points Per Game")
fig1 = px.bar(
    df,
    x="date",
    y=["aris_score", "opponent_score"],
    barmode="group",
    labels={"value": "Points", "date": "Date", "variable": "Team"},
    color_discrete_map={
        "aris_score": "#FFD700",
        "opponent_score": "#333333"
    }
)
st.plotly_chart(fig1, width='stretch')

st.divider()

# --- CHART 2: OVERALL WIN/LOSS PIE CHART ---
st.subheader("Results by League")
col1, col2 = st.columns(2)

fig2 = px.pie(
    df,
    names="aris_won",
    color="aris_won",
    color_discrete_map={True: "#FFD700", False: "#333333"},
    labels={"aris_won": "Result"},
    title="Overall Win/Loss"
)
fig2.update_traces(labels=["Loss", "Win"])
col1.plotly_chart(fig2, width='stretch')
# --- CHART 3: POINTS DISTRIBUTION BY LEAGUE ---
# Box chart showing scoring range per league
fig3 = px.box(
    df,
    x="league",
    y="aris_score",
    color="league",
    title="Points Distribution by League",
    labels={"aris_score": "Points", "league": "League"}
)
col2.plotly_chart(fig3, width='stretch')

st.divider()

# --- GAME LOG TABLE ---
st.subheader("Game Log")

# Select and rename columns for display
# Fixed: renamed opponent score column to "Opp. Score" to avoid duplicate names
display_df = df[["date", "opponent", "aris_score", "opponent_score", "aris_won", "league"]].copy()
display_df.columns = ["Date", "Opponent", "Aris Score", "Opp. Score", "Win", "League"]
display_df["Win"] = display_df["Win"].map({True: "✅", False: "❌"})
st.dataframe(display_df, width='stretch')
