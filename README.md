# 🇰🇪 Kenyantics/Africa is a Country API

A collection of humorous African-themed APIs that capture everyday experiences and cultural nuances with a touch of humour.

## 📋 Overview

Kenyantics is a FastAPI-based service that provides light-hearted, culturally relevant APIs inspired by everyday African experiences. From predicting mama mboga prices to generating traffic excuses, this API brings African humour to your applications.

## 🚀 Features

- **Mama Mboga Price Forecast**: Get predictions on vegetable prices at your local market
- **African Parent Response Generator**: Authentic responses from typical African parents
- **Traffic Excuse Generator**: Creative excuses for why you're late (again)
- **Wedding Contribution Calculator**: Know exactly how much to contribute based on your relationship
- **Electricity Availability Predictor**: Will the power stay on today?
- **African Superstition Advice**: Interpretations of common superstitions
- **Matatu DJ Song Predictor**: What's playing on public transport in different areas
- **African Auntie Gossip Generator**: What your aunt might be saying about you

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/kenyantics.git

# Navigate to the project directory
cd kenyantics

# Install dependencies
pip install -r requirements.txt
```

## 📝 Requirements

Create a `requirements.txt` file with:

```
fastapi==0.104.0
uvicorn==0.23.2
```

## 🏃‍♂️ Running the API

```bash
# Run the API server
uvicorn kenyantics:app --reload
```

The API will be available at `https://kenyantics.onrender.com:8000`

## 📚 API Documentation

Once the server is running, visit `https://kenyantics.onrender.com:8000/docs` for the interactive API documentation.

### Endpoints

#### 1. Mama Mboga Price Forecast
```
GET /mama-mboga-price
```
Returns the current vegetable price status and a reason.

#### 2. African Parent Response
```
GET /african-parent-response?question=Can%20I%20go%20out%20tonight
```
Returns a typical African parent response to your question.

#### 3. Traffic Excuse Generator
```
GET /traffic-excuse
```
Returns a creative excuse for being late due to traffic.

#### 4. Wedding Contribution Calculator
```
GET /wedding-contribution?relation=Cousin
```
Returns the appropriate amount to contribute at a wedding based on your relationship.

#### 5. Electricity Availability Predictor
```
GET /electricity-status
```
Returns the current electricity status and advice.

#### 6. African Superstition Advice
```
GET /superstition-advice
```
Returns interpretation of common African superstitious signs.

#### 7. Matatu DJ Song Predictor
```
GET /matatu-dj-song?location=Nairobi%20CBD
```
Predicts what music is playing on public transport in different locations.

#### 8. African Auntie Gossip Generator
```
GET /auntie-gossip
```
Returns what your African auntie might be gossiping about you.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- Inspired by everyday African experiences and humor
- Built with [FastAPI](https://fastapi.tiangolo.com/)
