# 🚚 AmazonDeliveryTimePrediction
A machine learning project that predicts delivery times using factors like distance, traffic, weather, area, and agent details. Built with Python, scikit-learn, and MLflow; deployed via Streamlit for real-time ETA predictions.
This project involves building an end-to-end machine learning pipeline to predict the estimated delivery time (ETA) for Amazon orders using various factors such as:
Order details
Delivery agent characteristics
Traffic and weather conditions
Geographical coordinates

📝 **Project Overview**

This project focuses on predicting the estimated delivery time (ETA) for Amazon orders using various factors such as order details, agent characteristics, traffic, weather conditions, and geospatial data.
By applying machine learning regression models, this project aims to improve delivery time estimation, which is crucial for:

* ⏱️Enhancing customer experience through accurate ETAs

* 🚀Optimizing delivery operations and route planning

* 📈 Improving agent performance analysis and resource allocation

**Key Contributions**

* 📊 Exploratory Data Analysis (EDA) to understand delivery patterns

* 🧮 Feature Engineering (distance calculations, temporal patterns, categorical encoding)

* Training Multiple Regression Models (Linear Regression, Random Forest, Gradient Boosting)

* 🧪 Experiment Tracking with MLflow for model comparison and reproducibility

* 🖼️ Streamlit UI Integration for interactive ETA predictions


🧾 **Dataset Summary**

The dataset amazon_delivery.csv contains realistic delivery order details.
Key columns include:

* 🆔 Order_ID – Unique order identifier

* 🧍‍♂️ Agent_Age, Agent_Rating – Delivery agent profile

* 📍 Store_Latitude, Store_Longitude, Drop_Latitude, Drop_Longitude – Geospatial coordinates

* 🕒 Order_Date, Order_Time, Pickup_Time – Temporal data

* 🌦️ Weather, 🚦 Traffic, 🚗 Vehicle, 🌆 Area – Contextual factors

* 🕑 Delivery_Time – Target variable (actual delivery duration in minutes)


**My Opinion / Insight**

For tabular ETA prediction problems like this, tree-based ensemble models (Random Forest / Gradient Boosting) tend to perform significantly better than linear models due to their ability to handle nonlinear interactions and mixed feature types.

Also, MLflow brings tremendous value by making experiment tracking transparent, especially when you're iterating fast between models and hyperparameters.


🪄 **Technologies Used**

* 🐍 Python 3.9+

* 🧮 Pandas, NumPy, Scikit-Learn

* 📊 Matplotlib / Seaborn (for visualization)

* 📌 MLflow (for experiment tracking)

* 🌐 Streamlit (for deployment demo)


🏁 **Conclusion**

The Amazon Delivery Time Prediction project demonstrates the practical application of machine learning in real-world logistics. By leveraging historical order data, contextual factors, and advanced regression techniques, we can build a system that predicts delivery ETAs with improved accuracy and consistency.

Through a structured pipeline of data cleaning, feature engineering, model experimentation, and evaluation, this project highlights how data-driven insights can transform last-mile delivery operations.

The integration of MLflow ensures transparent experiment tracking and reproducibility, while the Streamlit interface offers an intuitive way to interact with the trained model — bridging the gap between data science and real-world deployment.


✨ **This project reflects how the fusion of data, algorithms, and domain knowledge can solve impactful business problems in the e-commerce ecosystem.**
