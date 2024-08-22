import streamlit as st
import pandas as pd
import numpy as np
from plotly import graph_objs as go
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression


st.set_option('deprecation.showPyplotGlobalUse', False)
df = pd.read_csv("Data/Salary_Data.csv")
x = np.array(df["YearsExperience"]).reshape(-1,1)
y = np.array(df["Salary"])
lr = LinearRegression()
lr.fit(x,y)

st.image("DATA/sal.jpg",width = 850)
nav = st.sidebar.radio("Navigation",["Home","Prediction","Contribute"],index = 0)

if nav == "Home":
    st.title("SALARY PREDICTOR")
    if st.checkbox("Show Data"):
        st.table(df)

    type = st.selectbox("What type of graph you want to see",["Interactive","Non-interactive"])

    val = st.slider("FILTER DATA USING YEARS",0.0,20.0,step = 0.25)
    df = df.loc[df["YearsExperience"] >= val]
    if type == "Interactive" :
        layout = go.Layout(
            xaxis = dict(range = [0,16]),
            yaxis = dict(range = [0,210000])
        )

        fig = go.Figure(data=go.Scatter(x=df["YearsExperience"], y=df["Salary"], mode='markers'),layout = layout)
        st.plotly_chart(fig)

    else :
        plt.figure(figsize=(10,5))
        plt.scatter(df["YearsExperience"],df["Salary"])
        plt.ylim(0)
        plt.xlabel("EXPERIENCE")
        plt.ylabel("SALARY")
        plt.tight_layout()
        plt.title("EXPERIENCE VS SALARY")
        st.pyplot()

if nav == "Prediction":
    st.title("PREDICTION")

    st.header("KNOW YOUR SALARY")
    num = st.number_input("ENTER THE NUMBER OF YEARS : ",0.0,20.0,step = 0.25)
    num = np.array(num).reshape(1,-1)
    pred = lr.predict(num)[0]
    if st.button("SHOW RESULTS"):
        txt = "PREDICTED : "  + str(round(pred,5))
        st.success(txt)

if nav == "Contribute":
    st.title("CONTRIBUTE")
    st.header("CONTRIBUTE TO OUR WEBSITE")
    ex = st.number_input("ENTER YOUR EXPERICE",0.0,20.0)
    sal = st.number_input("ENTER YOUR SALARY",0.00,1000000.00,step = 1000.0)
    if st.button("SUBMIT"):
        to_add = {"YearsExperience":[ex],"Salary":[sal]}
        to_add = pd.DataFrame(to_add)
        to_add.to_csv("data//Salary_Data.csv",mode='a',header = False,index= False)
        st.success("THANK YOU FOR YOUR CONTRIBUTION")