
# 🏠 House Price Prediction – Delhi

This project predicts house prices in Delhi using machine learning models based on factors like location, size, and amenities. It involves data preprocessing, exploratory analysis, and regression techniques (Linear Regression, Decision Tree, Random Forest) to estimate prices accurately.

---

## 📁 Project Structure

```
House-Price-Prediction/
├── Data/                   # Dataset files
├── House_price.ipynb       # Jupyter notebook for EDA and modeling
├── app.py                  # Flask application for deployment
├── pipeline.pkl            # Serialized machine learning model
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ayushaggarwalx/House-Price-Prediction.git
   cd House-Price-Prediction
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

### Running the Flask App

1. **Start the Flask server:**
   ```bash
   python app.py
   ```

2. **Access the application:**
   Open your web browser and navigate to `http://127.0.0.1:5000/` to use the house price prediction interface.

---

## 📊 Model Details

- **Algorithms Used:**
  - Linear Regression
  - Decision Tree Regressor
  - Random Forest Regressor

- **Features Considered:**
  - Location
  - Size (e.g., square footage)
  - Number of bedrooms and bathrooms
  - Amenities (e.g., parking, garden)

- **Performance Metrics:**
  - Mean Absolute Error (MAE)
  - Root Mean Squared Error (RMSE)
  - R² Score

*Note: Detailed performance metrics and model evaluations are available in the `House_price.ipynb` notebook.*

---

## 🧪 Testing the Model

To test the model independently:

1. **Load the serialized model:**
   ```python
   import pickle

   with open('pipeline.pkl', 'rb') as file:
       model = pickle.load(file)
   ```

2. **Prepare your input data:**
   ```python
   input_data = {
       'location': 'Dwarka',
       'size': 1200,
       'bedrooms': 3,
       'bathrooms': 2,
       'amenities': ['parking', 'garden']
   }
   ```

3. **Make a prediction:**
   ```python
   predicted_price = model.predict([input_data])
   print(f"Predicted Price: ₹{predicted_price[0]:,.2f}")
   ```

*Ensure that the input data matches the format and preprocessing steps used during model training.*

---

## 📌 Future Enhancements

- Incorporate more granular location data (e.g., neighborhood-level insights)
- Integrate additional features like proximity to public transport, schools, and hospitals
- Deploy the application using cloud platforms like Heroku or AWS for broader accessibility
- Implement user authentication for personalized experiences

---

## 🤝 Contributing

Contributions are welcome! If you'd like to enhance the project:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a pull request
