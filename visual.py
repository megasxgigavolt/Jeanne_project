import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import warnings
warnings.filterwarnings("ignore")

st.set_page_config(layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)
final = pd.read_csv("stringency_final.csv")
final2 = pd.read_csv("stringency_normalized.csv")
opt = list(final["State_Code"].unique())
opt.append("USA")
series = st.selectbox("Select State",options=opt)
if series!="USA":
    data = final[final["State_Code"]==series]
else:
    data= final
    data = data.groupby("Date").sum().reset_index()
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    data["StringencyIndex"] = scaler.fit_transform(data[["StringencyIndex"]])
series2 = st.selectbox("Select Measure for Covid-19",options=["Stringency Index","Number of Covid Cases"])

col1, col2, col3 = st.columns(3)

# plt.figure(figsize=(18,9))
# sns.regplot(x="covid_cases",y="hate_crimes",data=final)
# st.pyplot()
# if series2=="Stringency Index":
#     st.line_chart(data=data,x="Date",y=["StringencyIndex","hate_tweets","hate_crimes"])
# else:
#     st.line_chart(data=data,x="Date",y=["covid_cases","hate_tweets","hate_crimes"])

# plt.figure(figsize=(18,9))
# sns.regplot(x="hate_crimes",y="hate_tweets",data=data)
# st.pyplot()
if series2=="Stringency Index":
    with col1:
        st.line_chart(data=data,x="Date",y=["StringencyIndex"])
        plt.figure(figsize=(18,9))
        # sns.regplot(x="StringencyIndex",y="hate_tweets",data=data)
        # st.pyplot()

        # x = data["StringencyIndex"]
        # y = data["hate_tweets"]
        # x = sm.add_constant(x)
        # model = sm.OLS(y, x).fit()
        # st.write(model.summary())

    with col2:
        st.line_chart(data=data,x="Date",y=["hate_crimes"])
        plt.figure(figsize=(18,9))
        # sns.regplot(x="hate_crimes",y="hate_tweets",data=data)
        # st.pyplot()

        # x = data["hate_crimes"]
        # y = data["hate_tweets"]
        # x = sm.add_constant(x)
        # model = sm.OLS(y, x).fit()
        # st.write(model.summary())


    with col3:
        st.line_chart(data=data,x="Date",y=["hate_tweets"])
        plt.figure(figsize=(18,9))
        # sns.regplot(x="StringencyIndex",y="hate_crimes",data=data)
        # st.pyplot()

        # x = data["StringencyIndex"]
        # y = data["hate_crimes"]
        # x = sm.add_constant(x)
        # model = sm.OLS(y, x).fit()
        # st.write(model.summary())
    

else:
    with col1:
        st.line_chart(data=data,x="Date",y=["covid_cases"])
        plt.figure(figsize=(18,9))
        # sns.regplot(x="covid_cases",y="hate_tweets",data=data)
        # st.pyplot()

        # x = data["covid_cases"]
        # y = data["hate_tweets"]
        # x = sm.add_constant(x)
        # model = sm.OLS(y, x).fit()
        # st.write(model.summary())

    with col2:
        st.line_chart(data=data,x="Date",y=["hate_tweets"])
        plt.figure(figsize=(18,9))
        # sns.regplot(x="hate_crimes",y="hate_tweets",data=data)
        # st.pyplot()

        # x = data["hate_crimes"]
        # y = data["hate_tweets"]
        # x = sm.add_constant(x)
        # model = sm.OLS(y, x).fit()
        # st.write(model.summary())

    with col3:
        st.line_chart(data=data,x="Date",y=["hate_crimes"])
        plt.figure(figsize=(18,9))
        # sns.regplot(x="covid_cases",y="hate_crimes",data=data)
        # st.pyplot()

        # x = data["covid_cases"]
        # y = data["hate_crimes"]
        # x = sm.add_constant(x)
        # model = sm.OLS(y, x).fit()
        # st.write(model.summary())



# # st.bar_chart(data=data,x="Date",y="hate_crimes")
# # st.bar_chart(data=data,x="Date",y="StringencyIndex")