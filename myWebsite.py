import streamlit as st
import pandas as pd
import plotly.express as px
mapboxToken = "pk.eyJ1IjoiZXJpY2hobyIsImEiOiJjanlmc2dtdWcwcDNyM2NxcXV3YTY1aXdxIn0.dg2jz0OJplKUiBEsn0jTIg"
def main():
	########## Leer datos con Pandas ####
	df = pd.read_csv('DB.csv', delimiter='|')
	########## Insertar titulo ##########
	st.markdown('# Hello Tiktok!')
	########## Insertar texto ##########
	st.markdown('## Como hacer una pagina WEB 💻 con PYTHON 🐍 EN 30 LINEAS DE CODIGO!')
	########## Mostrar datos ##########
	st.markdown('### Tabla de datos')
	st.dataframe(df.head(10))
	########## Histograma ##########
	st.markdown('### Histograma 📊')
	figHist = px.histogram(df, x='USD/M2',histnorm='percent')
	figHist.update_layout(title_text='DISTRIBUCION DEL VALOR DEL M²', title_x=0.5)
	figHist.update_yaxes(title_text='PORCENTAJE')
	figHist.update_xaxes(title_text='DISTRIBUCION DEL VALOR DEL M²')
	st.plotly_chart(figHist, use_container_width=True)
	########## Mostrar Mapa ##########
	st.markdown('### Mapas 🌎')
	px.set_mapbox_access_token(mapboxToken)
	figMap = px.scatter_mapbox(df, lat='latitud', lon='longitud',color='USD/M2', size='USD/M2',color_continuous_scale=px.colors.cyclical.IceFire, size_max=10,zoom=10)
	st.plotly_chart(figMap, use_container_width=True)
	st.markdown('### Mostrar Memes de Gatos 🐱')
	st.image('cat.jpeg')
if __name__ == "__main__":
    main()