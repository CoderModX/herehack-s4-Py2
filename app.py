#Import the required Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
# Add a title and intro text
df = pd.read_excel("HousePredTab.xlsx")
st.title('GeoPrice')

st.sidebar.title("Here Technology Hackathon")
st.sidebar.markdown(
"""
Project Based on Prediction of House/Land Prices based on Geo Location Data and then use the data and visualize over maps.
"""
)


st.text('Dataset header for Predicted Price for California Houses')
st.write(df.head())


st.header('Map Plot of Data')

html_temp = """<div class='tableauPlaceholder' id='viz1669392635418' style='position: relative'>
<noscript>
<a href='#'>
<img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ca&#47;CaliforniaHousePricePrediction&#47;Sheet1&#47;1_rss.png' style='border: none' /></a>
</noscript>
<object class='tableauViz'  style='display:none;'>
<param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
<param name='embed_code_version' value='3' /> <param name='site_root' value='' /
><param name='name' value='CaliforniaHousePricePrediction&#47;Sheet1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ca&#47;CaliforniaHousePricePrediction&#47;Sheet1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-GB' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1669392635418');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
components.html(html_temp,height=600)
# url = "https://public.tableau.com/views/CaliforniaHousePricePrediction/Sheet1?:language=en-GB&:display_count=n&:origin=viz_share_link"
# st.components.v1.iframe(src=url)

