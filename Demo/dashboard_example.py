import streamlit as st
import itertools
import pandas as pd
import numpy as np

from matplotlib import pyplot as plt
from plotly import express as px
from plotly.figure_factory import create_distplot
from wordcloud import WordCloud
import seaborn as sns

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

st.set_option('deprecation.showPyplotGlobalUse', False)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.sidebar.header('Dashboard')

df = pd.read_csv('tidy_data.csv')

# Row A

col1, col2, col3 = st.columns((4,3,3))

with col1:
	st.markdown('### Displot Plot')
	sns.set(rc={"figure.figsize":(10, 5)}) 
	sns.displot(data=df, x='price', kde=True, kind='hist', height=10, aspect=1.5)
	plt.xticks(np.arange(0, df['price'].max(), 200))
	plt.title('Biểu đồ phân phối của giá tiền')
	st.pyplot()
	

with col2:
	st.markdown('### Dot Plot')
	temp = df.groupby(by=['Laptop purpose', 'Brand'])['Best Sellers Rank'].min().reset_index()
	fig1 = px.scatter(temp, y="Laptop purpose", x="Best Sellers Rank", color="Brand", symbol="Brand")
	plt.title("Tốp bán hàng cao nhất của các thương hiệu ở mỗi loại laptop")
	fig1.update_traces(marker_size=10)
	st.plotly_chart(fig1)

with col3:
	st.markdown('### Scatter Plot')
	fig2, ax = plt.subplots(figsize=(7,7))
	sns.set(rc={"figure.figsize":(10, 10)}) 
	sns.scatterplot(data=df, x="price", y="Best Sellers Rank", hue="Best Sellers Rank", palette='rocket')
	plt.title('Biểu đồ phân tán giữa giá tiền và tốp bán chạy')
	st.pyplot(fig2)

# Row B
st.markdown('### BoxPlot')
c1, c2, c3 = st.columns((2,3,5))
with c1:
	df['weight_cate'] = pd.cut(df['weight'], bins=(0,1,1.5,2,2.5,10), labels=['Super light', 'Light', 'Normal', 'Heavy', 'Super Heavy'])

	df['price_cate'] = pd.cut(df['price'], bins=[0, 300, 500, 900, 1500, np.inf], labels=['< 300$', '< 500$', '< 900$', '< 1500$', 'Luxury'])
	fig_dims = (5,5)
	fig4, ax = plt.subplots(figsize=fig_dims)
	sns.boxplot(x = 'weight_cate', y = 'price',data=df)
	st.pyplot(fig4)

with c2:
	fig, ax = plt.subplots(figsize=(5,4))
	sns.boxplot(data=df, x=df["Laptop purpose"], y=df['price'])
	st.pyplot(fig)

with c3:
	fig1, ax = plt.subplots(figsize=(10,4))
	sns.boxplot(data=df, x=df["Brand"], y=df['price'])
	st.pyplot(fig1)

# Row C
st.markdown('### Histogram Plot')
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
	
	fig1 = px.histogram(df['weight'], title='Distribution of weight', marginal='box')
	st.plotly_chart(fig1)
	
with col2:

	fig2 = px.histogram(df['CPU rank'], title='Distribution of CPU rank', marginal='box')
	st.plotly_chart(fig2)

with col3:

	fig3 = px.histogram(df['GPU performance'], title='Distribution of GPU performance', marginal='box')
	st.plotly_chart(fig3)

with col4:

	fig4 = px.histogram(df['Brand'], title='Distribution of Brand', marginal='box')
	st.plotly_chart(fig4)

with col5:

	fig5 = px.histogram(df['RAM type'], title='Distribution of RAM type', marginal='box')
	st.plotly_chart(fig5)

# Row D
c1, c3 = st.columns((5,5))
with c1:
	st.markdown('### Sunburst Plot')
	path_col = ['Brand', 'Laptop purpose']
	for col in df.columns:
		if(col not in path_col):
				free_col=col
				break
	grouped=df.groupby(by=path_col)[free_col].count().reset_index()
	grouped['#'+path_col[0]]='#'+path_col[0]
	path_col.insert(0, '#'+path_col[0])
	fig3 = px.sunburst(grouped, path=path_col, values=free_col, width=750, height=750)
	st.plotly_chart(fig3)

with c3:
	st.markdown('### Heatmap')
	fig = plt.figure(figsize=(12,12))
	sns.heatmap(df.corr(),annot=True,cmap='Blues')
	st.pyplot(fig)
