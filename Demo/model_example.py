import streamlit as st
import pandas as pd
import numpy as np

from scipy.stats import pearsonr
from statsmodels import api as sm
from statsmodels.formula.api import ols

import seaborn as sns
from matplotlib import pyplot as plt
from plotly import express as px
from plotly.figure_factory import create_distplot
from matplotlib import use

import pickle

from wordcloud import WordCloud
use("Agg")

st.set_option('deprecation.showPyplotGlobalUse', False)

class DataFrame_Loader():
    def __init__(self):
        print("Loading DataFrame")
    
    def read_csv(self, data):
        self.df = pd.read_csv(data)
        return self.df

class EDA_DataFrame_Analysis():
    def __init__(self):
        print("General_EDA object created")
    
    def show_dtypes(self, x):
        return x.dtypes
    
    def show_columns(self, x):
        return x.columns
    
    def show_hist(self, x):
        fig = plt.figure(figsize=(15, 20))
        ax = fig.gca()
        x.hist(ax=ax)
    
    def Numerical_variables(self, x):
        Num_var = [var for var in x.columns if x[var].dtypes != 'object']
        return x[Num_var]
    
    def categorical_variables(self, x):
        cat_var = [var for var in x.columns if x[var].dtypes == 'object']
        return x[cat_var]
    
    def impute(self, x):
        return x.dropna()
    
    def show_pearsonr(self, x, y):
        return pearsonr(x, y)
    
    def show_scatter(self, k, a, b):
        fig, ax = plt.subplots(figsize=(18,8))
        return sns.scatterplot(data=k, x=a, y=b)
    
    def show_boxplot(self, k, a, b):
        fig, ax = plt.subplots(figsize=(18,8))
        return sns.boxplot(data=k, x=a, y=b)
    
    def show_sunburst(self, a, path_col):
        for col in a.columns:
            if(col not in path_col):
                free_col = col
                break
        grouped = a.groupby(by=path_col)[free_col].count().reset_index()
        grouped['#' + path_col[0]] = '#' + path_col[0]
        path_col.insert(0, '#' + path_col[0])
        fig = px.sunburst(grouped,
                          path=path_col,
                          values=free_col,
                          width=1500, height=1500)
        st.plotly_chart(fig)
    
    def show_displot(self, x):
        plt.figure(1)
        plt.subplot(121)
        sns.distplot(x)
        
        plt.subplot(122)
        x.plot.box(figsize=(16,5))
        plt.show()
    
    def ply_displot(self, k, x):
        return create_distplot([k[x]], 
                               group_labels=[x], 
                               show_hist=False)
    
    def ply_hist(self, k, x):
        return px.histogram(k[x], title='Histogram plot', marginal='box')
    
    def ply_box(self, k, a, b):
        return px.box(k, x=a, y=b, title='BoxPlot')
    
    def ply_scatter(self, k, a, b):
        return px.scatter(k, x=a, y=b, title='Regression plot', trendline='ols', trendline_color_override='red')
    
    def show_countplot(self, x):
        fig, ax = plt.subplot(figsize=(18,8))
        return sns.countplot(x, ax=ax)
    
    def show_circle(self, x):
        data = x.value_count().values.tolist()
        labels = x.value_count().index.tolist()
        
        plt.figure(figsize=(8,8))
        plt.pie(data, labels=labels, autopct='%1.1f%%', pctdistance=.85, explode=None)
        my_pie = plt.Circle((0,0), .7, color='white')
        p = plt.gcf()
        p.gca().add_artist(my_pie)
        plt.show()
    
    def show_bar(self, k, a, b):
        fig, ax = plt.subplots(figsize=(18,8))
        return sns.barplot(data=k, x=a, y=b)
    
    def show_violin(self, k, a, b):
        fig, ax = plt.subplots(figsize=(18,8))
        return sns.violinplot(data=k, x=a, y=b)
    
    def show_pairplot(self, x):
        return sns.pairplot(x, corner=True)
    
    def show_heatmap(self, x):
        fig, ax = plt.subplots(figsize=(18,8))
        return sns.heatmap(x.corr(), annot=True, ax=ax, cmap='Blues')
    
    def wordcloud(self, x):
        wordcloud = WordCloud(width=1000, height=500).generate(" ".join(x))
        plt.imshow(wordcloud)
        plt.axis("off")
    
    def show_residplot(self, k, a, b):
        fig, ax = plt.subplots(figsize=(18,8))
        plt.title('Residual plot')
        return sns.residplot(data=k, x=a, y=b)
    
    def show_pearsonr(self, x, y):
        return pearsonr(x, y)


class Attribute_Information():
    def __init__(self):
        print("Attribute Information object created")
    
    def Column_information(self,data):
        data_info = pd.DataFrame(columns=['Số dòng dữ liệu',
                                          'Số lượng thuộc tính',
                                          'Số lượng biến định lượng',
                                          'Số lượng biến định tính',])
        data_info.loc[0,'Số dòng dữ liệu'] = data.shape[0]
        data_info.loc[0,'Số lượng thuộc tính'] = data.shape[1]
        data_info.loc[0,'Số lượng biến định lượng'] = data._get_numeric_data().shape[1]
        data_info.loc[0,'Số lượng biến định tính'] = data.select_dtypes(include='object').shape[1]
        
        data_info = data_info.transpose()
        data_info.columns = ['value']
        data_info['value'] = data_info['value'].astype(int)
        
        return data_info
    
    def statistical_summary(self,df):
        return df.describe().transpose()

def main():
    
    st.set_page_config(layout='wide', initial_sidebar_state='expanded')
    
    with open("C:/Users/trinh/OneDrive/Máy tính/DS105 _Final project/Code source/Demo/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
    st.title("Nhóm 13")
    st.markdown('''
                # **DEMO**
                **Phân tích các yếu tố ảnh hưởng đến giá kết hợp dự đoán giá và mức độ bán chạy Laptop**
                ---
                ''')
    
    activities = ["Khảo sát dữ liệu","Phân tích thăm dò","Phân tích yếu tố ảnh hưởng đến thuộc tính hồi quy","Model"]
    choice = st.sidebar.selectbox('Select activities', activities)
    
    if choice == 'Khảo sát dữ liệu':
        st.subheader("KHẢO SÁT DỮ LIỆU")
        
        data = st.file_uploader("Upload dataset", type=['csv'])
        if data is not None:
            df = load.read_csv(data)
            st.dataframe(df.head())
            st.success("DataFrame Loaded successfully")
            
            if st.checkbox('Xuất toàn bộ thuộc tính'):
                st.write(dataframe.show_columns(df))
            
            if st.checkbox("Xuất kiểu dữ liệu của từng thuộc tính"):
                st.write(dataframe.show_dtypes(df))
            
            if st.checkbox("Xuất tổng quát và phân loại thuộc tính"):
                st.write(info.Column_information(df))
            
            if st.checkbox("Tổng hợp các giá trị thống kê từng thuộc tính"):
                st.write(info.statistical_summary(df))
            
            if st.checkbox("Xuất các biến định lượng"):
                num_df = dataframe.Numerical_variables(df)
                st.dataframe(pd.DataFrame(num_df))
            
            if st.checkbox("Xuất các biến định tính"):
                new_df = dataframe.categorical_variables(df)
                st.dataframe(pd.DataFrame(new_df))
            
            if st.checkbox("Xuất các thuộc tính theo lựa chọn"):
                selected_columns = st.multiselect("Select Columns",dataframe.show_columns(df))
                st.dataframe(df[selected_columns])
        
    elif choice == 'Phân tích thăm dò':
        st.subheader('EDA')
        data = st.file_uploader("Upload a Dataset", type=["csv"])
            
        if data is not None:
            df = load.read_csv(data)
            st.dataframe(df.head())
            st.success("Data Frame Loaded successfully")
                
            option_1b = st.selectbox('Chọn loại biểu đồ?',('Histogram', 'Distplot', 'CountPlot','Pie_Donut','ScatterPlot', 'BarPlot', 'ViolinPlot','BoxPlot','SunburstPlot'))
            if option_1b == 'Histogram':
                all_columns_names = dataframe.show_columns(df)
                selected_columns_names = st.selectbox("Chọn thuộc tính phân tích ", all_columns_names)
                if st.button('Show'):
                    st.write(dataframe.show_hist(df[selected_columns_names]))
                    st.pyplot()
                
            elif option_1b == 'Distplot':
                all_columns_names = dataframe.show_columns(df)
                selected_columns_names = st.selectbox("Chọn thuộc tính phân tích ", all_columns_names)
                if st.button('Show'):
                    st.write(dataframe.show_displot(df[selected_columns_names]))
                    st.pyplot()
                
            elif option_1b == 'CountPlot':
                all_columns_names = dataframe.show_columns(df)
                selected_columns_names = st.selectbox("Chọn thuộc tính phân tích ", all_columns_names)
                if st.button('Show'):
                    st.write(dataframe.show_countplot(df[selected_columns_names]))
                    st.pyplot()
                
            elif option_1b == 'Pie_Donut':
                all_columns_names = dataframe.show_columns(df)
                selected_columns_names = st.selectbox("Chọn thuộc tính phân tích ", all_columns_names)
                if st.button('Show'):
                    st.write(dataframe.show_circle(df[selected_columns_names]))
                    st.pyplot()
                
            elif option_1b == 'ScatterPlot':
                scatter1 = st.selectbox("Chọn thuộc tính thứ nhất (Numerical Columns)", dataframe.show_columns(df))
                scatter2 = st.selectbox("Chọn thuộc tính thứ hai (Numerical Columns)", dataframe.show_columns(df))
                if st.button('Show'):
                    st.write(dataframe.show_scatter(df, df[scatter1], df[scatter2]))
                    st.pyplot()
                
            elif option_1b == 'BarPlot':
                bar1 = st.selectbox("Chọn thuộc tính thứ nhất", dataframe.show_columns(df))
                bar2 = st.selectbox("Chọn thuộc tính thứ hai", dataframe.show_columns(df))
                if st.button('Show'):
                    st.write(dataframe.show_bar(df, df[bar1], df[bar2]))
                    st.pyplot()
                
            elif option_1b == 'ViolinPlot':
                violin1 = st.selectbox("Chọn thuộc tính thứ nhất", dataframe.show_columns(df))
                violin2 = st.selectbox("Chọn thuộc tính thứ hai", dataframe.show_columns(df))
                if st.button('Show'):
                    st.write(dataframe.show_bar(df, df[violin1], df[violin2]))
                    st.pyplot()
                
            elif option_1b == 'BoxPlot':
                box1 = st.selectbox("Chọn thuộc tính thứ nhất", dataframe.show_columns(df))
                box2 = st.selectbox("Chọn thuộc tính thứ hai", dataframe.show_columns(df))
                if st.button('Show'):
                    st.write(dataframe.show_bar(df, df[box1], df[box2]))
                    st.pyplot()
                
            elif option_1b == 'SunburstPlot':
                sun1 = st.multiselect("Chọn các thuộc tính", dataframe.show_columns(df))
                if st.button('Show'):
                    st.write(dataframe.show_sunburst(df, sun1))
                
            st.write("Trực quan tổng quát")
                
            if st.checkbox("Show Histogram"):
                st.write(dataframe.show_hist(df))
                st.pyplot()
                
            if st.checkbox("Show HeatMap"):
                st.write(dataframe.show_heatmap(df))
                st.pyplot()
                
            if st.checkbox("Show PairPlot"):
                st.write(dataframe.show_pairplot(df))
                st.pyplot()
                
            if st.checkbox("Show WordCloud"):
                st.write(dataframe.wordcloud(df['Brand']))
                st.pyplot()
    
    elif choice == 'Phân tích yếu tố ảnh hưởng đến thuộc tính hồi quy':
        st.subheader('Phân tích yếu tổ ảnh hưởng đến thuộc tính hồi quy')
        data = st.file_uploader("Upload a Dataset", type=["csv"])
        
        if data is not None:
            df = load.read_csv(data)
            st.dataframe(df.head())
            st.success("Data Frame Loaded successfully")
            
            tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8,tab9,tab10,tab11 = st.tabs(['Weight', 'RAM size', 'CPU rank', 'GPU performance', 'Brand', 'Laptop type', 'Laptop purpose', 'Hard Drive Type', 'RAM type','Optical Drive Type','Operating System'])
            with tab1:
                st.plotly_chart(dataframe.ply_displot(df,'weight'))
                st.plotly_chart(dataframe.ply_hist(df, 'weight'))
                df['weight_cate'] = pd.cut(df['weight'],
                                            bins=(0,1,1.5,2,2.5,10),
                                            labels=['Super light', 'Light', 'Normal', 'Heavy', 'Super Heavy'])
                st.plotly_chart(dataframe.ply_box(df, 'weight_cate', 'price'))
                st.plotly_chart(dataframe.ply_scatter(df, 'weight', 'price'))
                st.write(dataframe.show_residplot(df, 'weight', 'price'))
                st.pyplot()
                st.text(f"Probalility: {dataframe.show_pearsonr(df['weight'], df['price'])[0]}")
                st.text(f"P-value: {dataframe.show_pearsonr(df['weight'], df['price'])[1]}")
            
            with tab2:
                st.plotly_chart(dataframe.ply_displot(df,'RAM size'))
                st.write(dataframe.show_hist(df['RAM size']))
                st.pyplot()
                st.plotly_chart(dataframe.ply_hist(df,'RAM size'))
                st.plotly_chart(dataframe.ply_scatter(df,'RAM size','price'))
                st.write(dataframe.show_residplot(df,'RAM size','price'))
                st.pyplot()
                st.text(f"Probability: {dataframe.show_pearsonr(df['RAM size'], df['price'])[0]}")
                st.text(f"P-value: {dataframe.show_pearsonr(df['RAM size'], df['price'])[1]}")
            
            with tab3:
                st.plotly_chart(dataframe.ply_displot(df,'CPU rank'))
                st.plotly_chart(dataframe.ply_hist(df,'CPU rank'))
                st.plotly_chart(dataframe.ply_scatter(df,'CPU rank','price'))
                st.write(dataframe.show_residplot(df,'CPU rank','price'))
                st.pyplot()
                st.text(f"Probability: {dataframe.show_pearsonr(df['CPU rank'], df['price'])[0]}")
                st.text(f"P-value: {dataframe.show_pearsonr(df['CPU rank'], df['price'])[1]}")
            
            with tab4:
                st.plotly_chart(dataframe.ply_displot(df,'GPU performance'))
                st.write(dataframe.show_displot(df['GPU performance']))
                st.pyplot()
                st.plotly_chart(dataframe.ply_hist(df,'GPU performance'))
                st.plotly_chart(dataframe.ply_scatter(df,'GPU performance','price'))
                st.write(dataframe.show_residplot(df,'GPU performance','price'))
                st.pyplot()
                st.text(f"Probability: {dataframe.show_pearsonr(df['GPU performance'], df['price'])[0]}")
                st.text(f"P-value: {dataframe.show_pearsonr(df['GPU performance'], df['price'])[1]}")
            
            with tab5:
                st.plotly_chart(dataframe.ply_hist(df,'Brand'))
                st.plotly_chart(dataframe.ply_box(df,'Brand','price'))
                st.text("Anova Test:")
                model = ols("price ~ Brand", data=df).fit()
                st.dataframe(sm.stats.anova_lm(model, typ=2), width=500)
            
            with tab6:
                st.plotly_chart(dataframe.ply_hist(df,'Laptop type'))
                st.plotly_chart(dataframe.ply_box(df,'Laptop type','price'))
                st.text("Anova Test:")
                model = ols("price ~ Q('Laptop type')", data=df).fit()
                st.dataframe(sm.stats.anova_lm(model, typ=2), width=500)
            
            with tab7:
                st.plotly_chart(dataframe.ply_hist(df,'Laptop purpose'))
                st.plotly_chart(dataframe.ply_box(df,'Laptop purpose','price'))
                st.text("Anova Test:")
                model = ols("price ~ Q('Laptop purpose')", data=df).fit()
                st.dataframe(sm.stats.anova_lm(model, typ=2), width=500)
            
            with tab8:
                st.plotly_chart(dataframe.ply_hist(df,'Hard Drive Type'))
                st.plotly_chart(dataframe.ply_box(df,'Hard Drive Type','price'))
                st.text("Anova Test:")
                model = ols("price ~ Q('Hard Drive Type')", data=df).fit()
                st.dataframe(sm.stats.anova_lm(model, typ=2), width=500)
            
            with tab9:
                st.plotly_chart(dataframe.ply_hist(df,'RAM type'))
                st.plotly_chart(dataframe.ply_box(df,'RAM type','price'))
                st.text("Anova Test:")
                model = ols("price ~ Q('RAM type')", data=df).fit()
                st.dataframe(sm.stats.anova_lm(model, typ=2), width=500)
            
            with tab10:
                st.plotly_chart(dataframe.ply_hist(df,'Optical Drive Type'))
                st.plotly_chart(dataframe.ply_box(df,'Optical Drive Type','price'))
                st.text("Anova Test:")
                model = ols("price ~ Q('Optical Drive Type')", data=df).fit()
                st.dataframe(sm.stats.anova_lm(model, typ=2), width=500)
            
            with tab11:
                st.plotly_chart(dataframe.ply_hist(df,'Operating System'))
                st.plotly_chart(dataframe.ply_box(df,'Operating System','price'))
                st.text("Anova Test:")
                model = ols("price ~ Q('Operating System')", data=df).fit()
                st.dataframe(sm.stats.anova_lm(model, typ=2), width=500)

    
    elif choice == 'Model':
        st.subheader("Model")
        data = st.file_uploader("Upload a Dataset", type=["csv"])
        
        if data is not None:
            df = load.read_csv(data)
            st.dataframe(df.head())
            st.success("Data Frame Loaded successfully")
            
            Decision_Tree_model = pickle.load(open('tree.pkl','rb'))
            Random_Forest_model = pickle.load(open('forest.pkl','rb'))
            Ridge_model = pickle.load(open('ridge.pkl','rb'))
            SVM_model = pickle.load(open('svm.pkl','rb'))
            
            st.subheader("--Dự đoán giá Laptop--")
            weight_ft = st.text_input('weight_ft')
            
            CPU_rank = st.text_input('CPU_rank')
            if st.checkbox("Xem danh sách CPU rank"):
                new_df = df[['CPU rank','CPU']]
                st.dataframe(new_df)
            
            GPU_performance = st.text_input('GPU_performance')
            if st.checkbox("Xem danh sách GPU performance rank"):
                new_df = df['GPU performance']
                st.dataframe(new_df)
            
            Brand_select = pd.Series(df['Brand'].value_counts().index)
            Brand_ft = st.selectbox("Brand",Brand_select)
            
            Laptop_tsl = pd.Series(df['Laptop type'].value_counts().index)
            Laptop_type = st.selectbox("Laptop type",Laptop_tsl)
            
            Laptop_psl = pd.Series(df['Laptop purpose'].value_counts().index)
            Laptop_purpose = st.selectbox("Laptop purpose",Laptop_psl)
            
            HDT_slt = pd.Series(df['Hard Drive Type'].value_counts().index)
            Hard_Drive_Type = st.selectbox("Hard Drive Type",HDT_slt)
            
            RAM_tlt = pd.Series(df['RAM type'].value_counts().index)
            RAM_type = st.selectbox("RAM type",RAM_tlt)
            
            OS_slt = pd.Series(df['Operating System'].value_counts().index)
            Operating_System = st.selectbox("Operating System",OS_slt)
            
            option_model = st.selectbox('Chọn mô hình?',('Random_Forest_model', 'Decision_Tree_model','Ridge_model','SVM_model'))
            if option_model == 'Random_Forest_model':
                model_train = Random_Forest_model
                
            elif option_model == 'Decision_Tree_model':
                model_train = Decision_Tree_model
            
            elif option_model == 'Ridge_model':
                model_train = Ridge_model
            
            elif option_model == 'SVM_model':
                model_train = SVM_model
            
            df_input = pd.DataFrame({'weight':[weight_ft], 'CPU rank': [CPU_rank], 'GPU performance': [GPU_performance], 'Brand': [Brand_ft],'Laptop type':[Laptop_type], 'Laptop purpose':[Laptop_purpose], 'Hard Drive Type':[Hard_Drive_Type], 'RAM type':[RAM_type], 'Operating System':[Operating_System]}).apply(lambda x: int(x) if str(x).isdigit() else x)
            df_cut = df[['weight','CPU rank','GPU performance','Brand','Laptop type','Laptop purpose','Hard Drive Type','RAM type','Operating System']]
            new = pd.concat([df_cut, df_input], axis=0, ignore_index=True)
            new = pd.get_dummies(new, columns=['Brand', 'Laptop type', 'Laptop purpose', 'Hard Drive Type', 'RAM type', 'Operating System'])
            df_done = new.take([-1])
            
            if st.button('Predict'):
                makeprediction = model_train.predict(df_done)
                output=round(makeprediction[0],2)
                st.success(f'Laptop được dự đoán có giá khoảng: {output}')


if __name__ == '__main__':
	load = DataFrame_Loader()
	dataframe = EDA_DataFrame_Analysis()
	info = Attribute_Information()
	main()
