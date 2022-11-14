#script inspiré de Sven Bo

import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import warnings
import folium
import geopandas as gpd
from streamlit_folium import folium_static
st.set_page_config(layout="wide")
warnings.filterwarnings('ignore')

# ---- READ EXCEL ----
@st.cache
def read_csv():
    df = pd.read_csv(('beneficiairesdashboard.csv'))
    return df

df = read_csv()
sf = gpd.read_file('departements-version-simplifiee.geojson')
# ---- SIDEBAR ----
st.sidebar.header("Filtrages")
annee = st.sidebar.multiselect(
    "annee",
    options=df["annee"].unique(),
    default=df["annee"].unique()
)



genre = st.sidebar.multiselect(
    "genre",
    options=df["genre"].unique(),
    default=df["genre"].unique()
)

df_selection = df.query(
    "annee == @annee & genre == @genre"
)

# ---- MAINPAGE ----
st.title(":bar_chart: Tableau de bord Transparence Santé")
st.markdown("##")

# TOP KPI's
total_sales = int(df_selection["montant"].sum())

left_column, middle_column, right_column = st.columns(3)

    
with middle_column:
    st.subheader("Montant total:")
    st.subheader(f" {total_sales:,} euros")


st.markdown("""---""")


# SALES BY PRODUCT LINE [BAR CHART]
sales_by_product_line = (
    df_selection.groupby(by=["profession"])["montant"].sum().sort_values(ascending=False).head(10)
)
fig_product_sales = px.bar(
    sales_by_product_line,
    x="montant",
    y=sales_by_product_line.index,
    orientation="h",
    title="<b>Montant par profession</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    template="plotly_white",
)
fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

st.markdown("""---""")


# SALES BY HOUR [BAR CHART]
sales_by_hour = df_selection.groupby(by=["motif"])["montant"].sum().sort_values(ascending=False).head(10)
fig_hourly_sales = px.bar(
    sales_by_hour,
    x=sales_by_hour.index,
    y="montant",
    title="<b>Montant par motif</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_hour),
    template="plotly_white",
)
fig_hourly_sales.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)



left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_hourly_sales, use_container_width=True)
right_column.plotly_chart(fig_product_sales, use_container_width=True)


st.markdown("##")

##en terre inconnus chloropeth interactif
df_selectdep = df_selection.groupby(by=["departement"])["montant"].sum()
json1 = f"departements-version-simplifiee.geojson"

m = folium.Map(location=[47.75,1.5], tiles='CartoDB positron', name="Light Map",
               zoom_start=6.5, attr="My Data attribution")



folium.Choropleth(
    geo_data=json1,
    name="choropleth",
    data=df_selectdep,
    columns=["departement",'montant'],
    key_on="feature.properties.code",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=.1,
    legend_name='montant'
).add_to(m)
folium.features.GeoJson('departements-version-simplifiee.geojson',
                        name="nom", popup=folium.features.GeoJsonPopup(fields=["nom"])).add_to(m)

folium_static(m, width=1600, height=1400)
# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)





