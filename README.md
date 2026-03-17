# End-To-End-Data-Science-Project
Company : CODETECH IT SOLUTIONS

Name : V BHUVAN

Intern ID : CTIS6533

Domain : Data Science

Duration : 4 Weeks

Mentor : Neela Santhosh

Description about the Task :

This project demonstrates a complete data science workflow, starting from data collection and preprocessing to model development and deployment as a web application. The goal of the project is to build a simple machine learning model that predicts an employee’s salary based on their years of experience. The project highlights how machine learning techniques can be applied to solve real-world problems and how the resulting model can be deployed as an interactive application for users.

The first stage of the project involves data collection. A dataset is created in a CSV file containing two main attributes: years of experience and the corresponding salary. Each row represents a data record that shows how salary increases with experience. This dataset acts as the foundation for training the machine learning model. After collecting the dataset, the data is loaded and processed using the Python library pandas. Pandas helps in reading the CSV file, organizing the data into structured tables, and preparing it for machine learning tasks.

Once the dataset is loaded, preprocessing is performed to separate the input features and the target variable. In this project, the independent variable is the years of experience, while the dependent variable is the salary. These values are then used to train a machine learning model. A regression algorithm is applied using the library scikit-learn. Specifically, a Linear Regression model is used because the relationship between experience and salary is assumed to be approximately linear. The model learns patterns from the training data and identifies how salary changes as experience increases.

After training the model, it is saved using Python’s serialization technique. The trained model is stored as a file so that it can be reused later without retraining. This makes the system efficient and suitable for deployment. The saved model is then integrated into a web application built using the Flask framework. Flask is a lightweight web framework that allows developers to build simple web applications and APIs using Python.

In the deployment stage, a web interface is created where users can input the number of years of experience. When the user submits the input, the Flask application sends the data to the trained machine learning model. The model processes the input and predicts the expected salary. The predicted result is then displayed on the web page, allowing users to interact with the model easily.

This project demonstrates the entire lifecycle of a data science solution, including data collection, preprocessing, model training, model persistence, and deployment. It shows how machine learning models can be transformed into practical tools that users can access through a web interface. Even though the dataset and model are simple, the project provides a clear understanding of how real-world machine learning applications are developed and deployed.

Overall, the project serves as a beginner-friendly example of combining data science and web development. It helps in understanding how predictive models can support decision-making and how Python-based tools can be used to build scalable and interactive data-driven applications.

output of the task: 


<img width="503" height="257" alt="Image" src="https://github.com/user-attachments/assets/fe19880b-d3fc-4c33-adc3-77f7878b413a" />
<img width="1123" height="830" alt="Image" src="https://github.com/user-attachments/assets/bdcc13e3-5a1f-4505-8c1c-363e4a296f7e" />
