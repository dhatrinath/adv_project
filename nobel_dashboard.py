
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit.components.v1 as components

# Load data
df = pd.read_csv("nobel_winners.csv")
df_1 = pd.read_csv("nobel_winners_all_pubs.csv")

# Clean birth year and age
df['birth_date'] = pd.to_datetime(df['birth_date'], errors='coerce')
df['birth_year'] = df['birth_date'].dt.year
df['age'] = df['prize_year'] - df['birth_year']

st.set_page_config(page_title="Nobel Prize Dashboard", layout="wide")

st.title("🏅 The Story of the Nobel Prize")
st.markdown("""
Welcome to an interactive storytelling dashboard about Nobel Prize laureates.
We'll walk through key insights on categories, gender distribution, age trends, and more —
bringing data to life using real-world Nobel prize winners history.
""")

st.markdown("---")

# --- Chapter 1: Nobel Prize Distribution by Category ---
st.header("📊 Chapter 1: Where Are the Prizes Going?")
st.markdown("""
Since 1901, the Nobel Prize has honored groundbreaking contributions in various disciplines.
Medicine leads the way, followed closely by Physics and Chemistry.
""")

category_dist = df['category'].value_counts().reset_index()
category_dist.columns = ['category', 'count']
fig_cat = px.bar(category_dist, x='category', y='count', color='category',
                 title='Nobel Prizes Awarded by Category')
fig_cat.update_xaxes(showgrid=False)
fig_cat.update_yaxes(showgrid=False)
st.plotly_chart(fig_cat, use_container_width=True)


st.markdown("---")

# --- Chapter 2: Gender Dynamics Over Time ---
st.header("👥 Chapter 2: Gender Dynamics")
st.markdown("""
The Nobel Prize has historically been awarded to men, but female representation is growing.
Here's a view of how gender distribution evolved over time.
""")
try:
    with open("nobel_prize_per_gender_year.html", "r", encoding="utf-8", errors="replace") as f:
        html_content = f.read()
    components.html(html_content, height=600, scrolling=True)
except FileNotFoundError:
    st.warning("nobel_prize_per_gender_year.html not found. Please place the file in the same directory.")




st.markdown("---")

# --- Chapter 3: Age of Winners ---
st.header("🎂 Chapter 3: How Old Are Nobel Laureates?")
st.markdown("""
Laureates are often recognized later in life — the average age hovers around 60.
But outliers exist: the youngest was just 17!
""")
age_data = df['age'][(df['age'] > 10) & (df['age'] < 100)].dropna()
fig_age = px.histogram(age_data, nbins=150, 
                   title='Distribution of Laureates Age at Award',
                   labels={'value':'Age', 'count':'Frequency'},
                   template='plotly_white')
fig_age.update_xaxes(showgrid=False)
fig_age.update_yaxes(showgrid=False)

# fig_age = px.box(df, x='category', y='age', color='category', points='all',
#                  title='Age Distribution by Nobel Prize Category')
st.plotly_chart(fig_age, use_container_width=True,showgrid=False)

st.markdown("---")


# # Sidebar filters
# st.sidebar.header("Filters")
# category = st.sidebar.multiselect("Select Category", sorted(df['category'].dropna().unique()), default=None)
# gender = st.sidebar.multiselect("Select Gender", sorted(df['gender'].dropna().unique()), default=None)
# year_range = st.sidebar.slider("Prize Year Range", int(df['prize_year'].min()), int(df['prize_year'].max()), (1950, 2020))

# # Apply filters
# filtered_df = df.copy()
# if category:
#     filtered_df = filtered_df[filtered_df['category'].isin(category)]
# if gender:
#     filtered_df = filtered_df[filtered_df['gender'].isin(gender)]
# filtered_df = filtered_df[(filtered_df['prize_year'] >= year_range[0]) & (filtered_df['prize_year'] <= year_range[1])]

# # KPIs
# col1, col2, col3, col4 = st.columns(4)
# col1.metric("Total Prizes", f"{filtered_df.shape[0]}")
# col2.metric("Unique Laureates", f"{filtered_df['full_name'].nunique()}")
# col3.metric("Avg Age at Award", f"{filtered_df['age'].mean():.1f}")
# col4.metric("Female Laureates", f"{(filtered_df['gender'] == 'Female').sum()}")

# st.markdown("---")

# # Plot: Prizes per Year
# st.subheader("📈 Nobel Prizes Awarded per Year")
# yearly_awards = filtered_df.groupby(['prize_year', 'category']).size().reset_index(name='count')
# fig1 = px.line(yearly_awards, x='prize_year', y='count', color='category', markers=True)
# fig1.update_layout(legend_title="Category", xaxis_title="Year", yaxis_title="Number of Awards")
# st.plotly_chart(fig1, use_container_width=True)

# # Plot: Gender Distribution Over Time
# st.subheader("👥 Gender Distribution Over the Years")
# gender_time = filtered_df.groupby(['prize_year', 'gender']).size().reset_index(name='count')
# fig2 = px.line(gender_time, x='prize_year', y='count', color='gender', markers=True)
# fig2.update_layout(legend_title="Gender", xaxis_title="Year", yaxis_title="Awards Count")
# st.plotly_chart(fig2, use_container_width=True)

# # Plot: Age Distribution
# st.subheader("🎂 Age at Award Over Time")
# fig3 = px.box(filtered_df, x='prize_year', y='age', points="all", color='category')
# fig3.update_layout(xaxis_title="Prize Year", yaxis_title="Age")
# st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")
# --- Chapter 4: Global Origins ---
st.header("🌍 Chapter 4: Where Do Nobel Laureates Come From?")
st.markdown("""
Although the Nobel is a global award, the majority of recipients hail from the United States and Europe.
""")

try:
    with open("nobel_prize_geo.html", "r", encoding="utf-8", errors="replace") as f:
        html_content = f.read()
    components.html(html_content, height=600, scrolling=True)
except FileNotFoundError:
    st.warning("nobel_prize_geo.html not found. Please place the file in the same directory.")

st.markdown("---")



# --- Chapter 5: Animated Trends ---
st.header("🎞️ Chapter 5: Awards Over Time (Animated)")
st.markdown("""
Watch how Nobel Prize awards have evolved across the 20th and 21st centuries.
""")

try:
    with open("nobel_prize_animation.html", "r", encoding="utf-8", errors="replace") as f:
        html_content = f.read()
    components.html(html_content, height=600, scrolling=True)
except FileNotFoundError:
    st.warning("nobel_prize_animation.html not found. Please place the file in the same directory.")
st.markdown("---")

# try:
#     with open("nobel_prize_per_gender_year.html", "r", encoding="utf-8", errors="replace") as f:
#         html_content = f.read()
#     components.html(html_content, height=600, scrolling=True)
# except FileNotFoundError:
#     st.warning("nobel_prize_per_gender_year.html not found. Please place the file in the same directory.")




st.markdown("---")
# --- Conclusion ---
st.header("📚 The Journey Continues")
st.markdown("""
The Nobel Prize remains one of the most prestigious honors in the world.
I hope this dashboard offered you a compelling glimpse into the history and data behind the prize.

_“For the greatest benefit to humankind.”_ – Alfred Nobel
""")