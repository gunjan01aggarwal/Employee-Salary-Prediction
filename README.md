# Employee-Salary-Prediction
**Problem Statement:->
                    To Predict the Salary of an employee according to the information given in dataset..............
                    
                    
![Picture!](https://github.com/gunjan01aggarwal/Employee-Salary-Prediction/blob/main/Image.jpg)
                    
                    
![image](https://user-images.githubusercontent.com/62065619/160145894-a6adf9e9-4479-4c50-a0f5-ff8867feb3cd.png)


**Data Preprocessing:->
                    As we saw it, our dataset doesn't have any null values. This dataset contains 10,00000 rows and 9 columns.But i trained the model on 300000 rows and 9 columns.It contains mutiple categorical feature as compared to numerical feature. Machine learning algorithm understands numeric input. So first i have to convert those features into numerical. I used some encoding techniques like Label Encoder. Label Encoder applied on ordinal features like degree and jobtype. Both have its order. Other Encoding Techniques is One Hot Encoding which applied on nominal features like industry,major domain and etc. 
                    
**Exploratory Data Analysis:->
 
Analyse each feature by using seaborn and matplotlib library.How correlate the independent features with the dependent feature ?

> Experience and Salary are linearly increases.

> TOP 3 Positions like CEO,CTO,CFO are getting high salary in each industry.Min Salary is 51k$.

> Janitor Position is getting lowest salary in each industry. Min and Max salary are 17k$ and 189k$ respectively.

> Janitor has highest qualifications either high school or none .

> The industry with highest income is OIL ,second is FINANCE and third is WEB.

> For every jobType, those employees have higher degree have higher income.



![degree](https://user-images.githubusercontent.com/62065619/160466251-2591c60d-452e-4cb0-93eb-a435f006179a.png)




<<HEAD
WebApp Link:https://employeesalarypredict-api.herokuapp.com/
=========           
           
           




