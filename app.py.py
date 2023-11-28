
import streamlit as st
import pandas as pd
import datetime
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go

 # reading from the excel file
import pandas as pd

file_path = r'C:\Users\Tarun\Downloads\Ecom data py.xlsx'
df = pd.read_excel(file_path)

#df = pd.read_excel("Ecomm data py.xlsx")
st.set_page_config(layout="wide")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

image_path = r'C:\Users\Tarun\Downloads\ecom logo.png'
image = Image.open(image_path)
#image.show()
col1, col2 = st.columns([0.1,0.9])
with col1:
  st.image(image,width = 150)
html_title = """
  <style>
    .title-test{ 
    font-weight:bold; 
    padding: 5px;
    border-radius:6px;
    }
</style>

<center><h1 class = "title-test">Ecommerce Sales dashboard</h1></center>"""
with col2 :
  st.markdown(html_title,unsafe_allow_html=True)

col3, col4, col5 = st.columns([0.1,0.45,0.45])
with col3:
  box_date = str(datetime.datetime.now().strftime("%d %B %Y"))
  st.write(f" Last Updated By:   \n {box_date}")

with col4:
  fig = px.bar(df, x = "Region", y ="Sales", labels= {"Sales": "Total Sales {$}"},
               title= "Total Sales by Region", hover_data=["Sales"],
               template="gridon",height=500)
  st.plotly_chart(fig,use_container_width=True)
_, view1, dwn1, view2, dwn2 = st.columns([0.15,0.20,0.20,0.20,0.20])
with view1:
    expander = st.expander("Region wise Sales")
    data = df[["Region","Sales"]].groupby(by="Region")["Sales"].sum()
    expander.write(data)
with dwn1:
    st.download_button("Get Data here", data = data.to_csv().encode("utf-8"),
      file_name = "Regionwisesales.csv", mime="text/csv")


  ###################### second chart####################################
with col5:
  fig = px.bar(df, x = "Segment", y ="Sales", labels= {"Sales": "Total Sales {$}"},
               title= "Total Sales by Segment", hover_data=["Sales"],
               template="gridon",height=500)
  st.plotly_chart(fig,use_container_width=True)

with view2:
  expander = st.expander("Segment wise Sales")
  data = df[["Segment","Sales"]].groupby(by="Segment")["Sales"].sum()
  expander.write(data)
with dwn2:
  st.download_button("Get Data here", data = data.to_csv().encode("utf-8"),
                     file_name = "Segmentwisesales.csv", mime="text/csv")
  ####################### third chart########################################

st.divider()

result1 = df.groupby (by = "Country")[["Sales","Quantity"]].sum().reset_index()


# add the units sold as a
fig3 = go.Figure()
fig3.add_trace(go.Bar(x = result1["Country"], y = result1["Sales"], name = "Total Sales"))
fig3.add_trace(go.Scatter(x = result1["Country"], y = result1["Quantity"], mode ="lines",
              name = "Quantity", yaxis = "y2"))

fig3.update_layout(
    title ="Total Sales and Units Sold by Country",
    xaxis = dict(title = "Country"),
    yaxis = dict(title= "Total Sales", showgrid = False),
    yaxis2 = dict(title = "Quantity", overlaying = "y",side = "right"),
    template = "gridon",
    legend =  dict(x=1, y=1)
)

_, col6 = st.columns([0.1,1])
with col6:
    st.plotly_chart(fig3,use_container_width=True)

_, view3, dwn3 = st.columns([0.5,0.45,0.45])
with view3:
    expander = st.expander("View Data for Sales by Units Sold")
    expander.write(result1)
with dwn3:
    st.download_button("Get Data", data = result1.to_csv().encode("utf-8"), 
                       file_name = "Sales_by_UnitsSold.csv", mime="text/csv")


st.divider()

_, col7 = st.columns([0.1,1])
treemap = df[["Region","State","Sales"]].groupby(by = ["Region","State"])["Sales"].sum().reset_index()


fig4 = px.treemap(treemap, path = ["Region","State"], values = "Sales",
                  hover_name = "Sales",
                  hover_data = ["Sales"],
                  color = "State", height = 700, width = 600)
fig4.update_traces(textinfo="label+value")

######################## Forth Chart########################################

with col7:
    st.subheader(":point_right: Total Sales by Region and State in Treemap")
    st.plotly_chart(fig4,use_container_width=True)


_, view4, dwn4 = st.columns([0.5,0.45,0.45])
with view4:
    result2 = df[["Region","State","Sales"]].groupby(by=["Region","State"])["Sales"].sum()
    expander = st.expander("View data for Total Sales by Region and State")
    expander.write(result2)
with dwn4:
    st.download_button("Get Data", data = result2.to_csv().encode("utf-8"),
                                        file_name="Sales_by_Region.csv", mime="text.csv")


################# fifth chart############################################

df ["Month_year"] = df["Order Date"].dt.strftime("%b '%y")
result =df.groupby(by=df["Month_year"])["Sales"].sum().reset_index()


_, col8 = st.columns([0.1,1])
with col8:
    fig1 = px.line(result,x = "Month_year", y= "Sales", title= "Total Sales over Time",
                   template= "gridon")
st.plotly_chart(fig1,use_container_width=True)

_, view6, dwn6 = st.columns([0.5,0.45,0.45])
with view6:
  expander = st.expander("Year wise Sales")
  data = df[["Month_year","Sales"]].groupby(by="Month_year")["Sales"].sum()
  expander.write(data)
with dwn6:
  st.download_button("Get Data here", data = data.to_csv().encode("utf-8"),
                     file_name = "Yearwisesales.csv", mime="text/csv")
  
######################Get Row data here##########################################
_,view7, dwn7 = st.columns([0.5,0.45,0.45])
with view7:
    expander = st.expander("View Sales Raw Data")
    expander.write(df)
with dwn7:
    st.download_button("Get Raw Data", data = df.to_csv().encode("utf-8"),
                       file_name = "SalesRawData.csv", mime="text/csv")
st.divider()


#streamlit run C:\Users\Tarun\Downloads\app.py --server.port 8080




